from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from statistics import mean, pstdev
from typing import Any, Dict, List, Sequence, Tuple

from viruse_fabric.simulation.viruse_fabric_minimal_safe_toy_simulation_engine import (
    SafeAbstractToySimulationEngine,
    ToyEngineConfig,
)
from viruse_fabric.writing.viruse_fabric_safe_toy_baseline_comparison import (
    ViruseFabricSafeToyBaselineComparisonBuilder,
)


class ViruseFabricSafeToyReplicateGridAndSignalRobustnessCheckBuilder:
    version = "v9.7"

    output_md_path = Path("outputs/viruse_fabric_safe_toy_replicate_grid_and_signal_robustness_check_v9_7.md")
    output_json_path = Path("outputs/viruse_fabric_safe_toy_replicate_grid_and_signal_robustness_check_v9_7.json")

    source_v9_4_json_path = Path("outputs/viruse_fabric_results_and_falsification_audit_v9_4.json")
    source_v9_6_json_path = Path("outputs/viruse_fabric_safe_toy_scientific_yield_extraction_and_theory_reduction_v9_6.json")

    plan_phrase = "v9_7_safe_toy_replicate_grid_and_signal_robustness_check_without_validation_or_readiness"

    signal_metric = "ledger_effect_size"
    primary_hypothesis = "VF-H2"
    reference_variant = "VF-FULL"
    ablation_variant = "VF-BASE-C"

    seed_grid: Sequence[Tuple[int, int, int, int]] = (
        (101, 202, 303, 404),
        (111, 212, 313, 414),
        (121, 222, 323, 424),
        (131, 232, 333, 434),
        (141, 242, 343, 444),
        (151, 252, 353, 454),
    )

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _build_replicate_config(
        self,
        base_config: ToyEngineConfig,
        replicate_id: str,
        seeds: Tuple[int, int, int, int],
    ) -> Dict[str, Any]:
        graph_seed, packet_seed, transition_seed, symbolic_drift_seed = seeds
        config = replace(
            base_config,
            graph_seed=graph_seed,
            packet_seed=packet_seed,
            transition_seed=transition_seed,
            symbolic_drift_seed=symbolic_drift_seed,
        )
        return {
            "replicate_id": replicate_id,
            "graph_seed": graph_seed,
            "packet_seed": packet_seed,
            "transition_seed": transition_seed,
            "symbolic_drift_seed": symbolic_drift_seed,
            "node_count": config.node_count,
            "packet_count": config.packet_count,
            "step_count_limit": config.step_count_limit,
            "config": config,
        }

    def _extract_metrics(self, run_record: Dict[str, Any]) -> Dict[str, float]:
        metric_key_candidates = [
            "metrics",
            "metric_results",
            "metric_snapshot",
            "final_metrics",
            "final_metric_snapshot",
        ]

        for key in metric_key_candidates:
            value = run_record.get(key)
            if isinstance(value, dict):
                return {name: float(metric_value) for name, metric_value in value.items()}

        raise KeyError(
            "No metric dictionary found in run record. "
            f"Available keys: {sorted(run_record.keys())}"
        )

    def _metric_delta(self, full_metrics: Dict[str, float], ablation_metrics: Dict[str, float]) -> Dict[str, float]:
        metric_names = sorted(set(full_metrics) | set(ablation_metrics))
        return {
            name: round(float(full_metrics.get(name, 0.0)) - float(ablation_metrics.get(name, 0.0)), 6)
            for name in metric_names
        }

    def _run_replicate_grid(self) -> Dict[str, Any]:
        baseline_builder = ViruseFabricSafeToyBaselineComparisonBuilder()
        engine = SafeAbstractToySimulationEngine()
        base_config = baseline_builder._safe_config()

        replicate_grid: List[Dict[str, Any]] = []
        replicate_run_records: List[Dict[str, Any]] = []
        robustness_records: List[Dict[str, Any]] = []

        for index, seeds in enumerate(self.seed_grid, start=1):
            replicate_id = f"V9-7-REP-{index:03d}"
            config_record = self._build_replicate_config(base_config, replicate_id, seeds)
            config = config_record["config"]

            public_config_record = {
                key: value
                for key, value in config_record.items()
                if key != "config"
            }
            replicate_grid.append(public_config_record)

            full_run = baseline_builder._run_safe_toy_variant(
                engine=engine,
                config=config,
                baseline_id=self.reference_variant,
            )
            ablation_run = baseline_builder._run_safe_toy_variant(
                engine=engine,
                config=config,
                baseline_id=self.ablation_variant,
            )

            full_run = dict(full_run)
            ablation_run = dict(ablation_run)

            full_run["replicate_id"] = replicate_id
            ablation_run["replicate_id"] = replicate_id

            replicate_run_records.extend([full_run, ablation_run])

            full_metrics = self._extract_metrics(full_run)
            ablation_metrics = self._extract_metrics(ablation_run)

            full_run["metrics"] = full_metrics
            ablation_run["metrics"] = ablation_metrics

            metric_deltas = self._metric_delta(full_metrics, ablation_metrics)
            ledger_delta = round(float(metric_deltas.get(self.signal_metric, 0.0)), 6)

            robustness_records.append(
                {
                    "robustness_record_id": f"V9-7-H2-ROBUSTNESS-{index:03d}",
                    "replicate_id": replicate_id,
                    "hypothesis_id": self.primary_hypothesis,
                    "reference_variant": self.reference_variant,
                    "ablation_variant": self.ablation_variant,
                    "signal_metric": self.signal_metric,
                    "reference_metric_value": round(float(full_metrics.get(self.signal_metric, 0.0)), 6),
                    "ablation_metric_value": round(float(ablation_metrics.get(self.signal_metric, 0.0)), 6),
                    "signal_delta": ledger_delta,
                    "positive_signal": ledger_delta > 0.0,
                    "metric_deltas": metric_deltas,
                    "boundary": (
                        "Safe abstract toy replicate comparison only. This is not empirical evidence, not external validation, "
                        "not independent validation, not manuscript readiness, and not a theory validation claim."
                    ),
                }
            )

        return {
            "replicate_grid": replicate_grid,
            "replicate_run_records": replicate_run_records,
            "robustness_records": robustness_records,
        }

    def _robustness_summary(self, robustness_records: List[Dict[str, Any]]) -> Dict[str, Any]:
        signal_deltas = [float(item["signal_delta"]) for item in robustness_records]
        positive_count = sum(1 for value in signal_deltas if value > 0.0)
        zero_count = sum(1 for value in signal_deltas if value == 0.0)
        negative_count = sum(1 for value in signal_deltas if value < 0.0)
        replicate_count = len(signal_deltas)
        positive_rate = round(positive_count / replicate_count, 6) if replicate_count else 0.0

        if positive_rate >= 0.8:
            verdict = "robust_in_this_safe_toy_replicate_grid"
        elif positive_rate >= 0.5:
            verdict = "partially_robust_in_this_safe_toy_replicate_grid"
        else:
            verdict = "not_robust_in_this_safe_toy_replicate_grid"

        return {
            "summary_id": "V9-7-MEMORY-LEDGER-ROBUSTNESS-SUMMARY-001",
            "hypothesis_id": self.primary_hypothesis,
            "signal_metric": self.signal_metric,
            "reference_variant": self.reference_variant,
            "ablation_variant": self.ablation_variant,
            "replicate_count": replicate_count,
            "positive_signal_replicate_count": positive_count,
            "zero_signal_replicate_count": zero_count,
            "negative_signal_replicate_count": negative_count,
            "positive_signal_rate": positive_rate,
            "mean_signal_delta": round(mean(signal_deltas), 6) if signal_deltas else 0.0,
            "min_signal_delta": round(min(signal_deltas), 6) if signal_deltas else 0.0,
            "max_signal_delta": round(max(signal_deltas), 6) if signal_deltas else 0.0,
            "population_stdev_signal_delta": round(pstdev(signal_deltas), 6) if len(signal_deltas) > 1 else 0.0,
            "robustness_verdict": verdict,
            "robustness_verdict_options": [
                "robust_in_this_safe_toy_replicate_grid",
                "partially_robust_in_this_safe_toy_replicate_grid",
                "not_robust_in_this_safe_toy_replicate_grid",
            ],
            "summary_statement": (
                "The memory-ledger signal is checked across a safe abstract toy replicate grid. "
                "The verdict is restricted to this safe toy grid and does not validate the full theory."
            ),
        }

    def _non_upgrade_records(self) -> List[Dict[str, Any]]:
        return [
            {
                "hypothesis_id": "VF-H1",
                "mechanism": "multi_layer_constraint_path_shift",
                "status_after_v9_7": "not_upgraded",
                "reason": "v9.7 only checks VF-H2 memory-ledger signal robustness.",
            },
            {
                "hypothesis_id": "VF-H3",
                "mechanism": "causal_mass_delayed_effect",
                "status_after_v9_7": "not_upgraded",
                "reason": "v9.7 only checks VF-H2 memory-ledger signal robustness.",
            },
            {
                "hypothesis_id": "VF-H4",
                "mechanism": "three_time_layer_predictive_difference",
                "status_after_v9_7": "not_upgraded",
                "reason": "v9.7 only checks VF-H2 memory-ledger signal robustness.",
            },
        ]

    def _allowed_robustness_claims(self, verdict: str) -> List[Dict[str, Any]]:
        return [
            {
                "claim_id": "V9-7-ALLOW-001",
                "claim_text": (
                    f"In this safe abstract toy replicate grid, the VF-H2 memory-ledger signal has verdict {verdict}."
                ),
                "scope": "safe_abstract_toy_replicate_grid_only",
            },
            {
                "claim_id": "V9-7-ALLOW-002",
                "claim_text": (
                    "The tested signal is ledger_effect_size in the VF-FULL versus VF-BASE-C comparison."
                ),
                "scope": "safe_abstract_toy_replicate_grid_only",
            },
            {
                "claim_id": "V9-7-ALLOW-003",
                "claim_text": (
                    "VF-H1, VF-H3, and VF-H4 are not upgraded by v9.7 and remain unresolved or unsupported."
                ),
                "scope": "safe_abstract_toy_boundary",
            },
        ]

    def _forbidden_robustness_claims(self) -> List[Dict[str, Any]]:
        return [
            {
                "claim_id": "V9-7-FORBID-001",
                "forbidden_claim": "The full Viruse Fabric theory is robustly validated.",
                "reason": "v9.7 only checks one safe toy signal for VF-H2 across a small replicate grid.",
            },
            {
                "claim_id": "V9-7-FORBID-002",
                "forbidden_claim": "The memory-ledger signal is empirically validated.",
                "reason": "The replicate grid is safe abstract toy only and contains no empirical validation.",
            },
            {
                "claim_id": "V9-7-FORBID-003",
                "forbidden_claim": "VF-H1, VF-H3, or VF-H4 are now supported.",
                "reason": "v9.7 does not upgrade those hypotheses.",
            },
            {
                "claim_id": "V9-7-FORBID-004",
                "forbidden_claim": "The project is manuscript submission ready.",
                "reason": "v9.7 does not create readiness approval and v9.5 already denied readiness.",
            },
            {
                "claim_id": "V9-7-FORBID-005",
                "forbidden_claim": "The model applies to real biological systems.",
                "reason": "No real biological datasets, pathogen models, receptor parameters, or operational biological assumptions are introduced.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source_v9_4 = self._load_json(self.source_v9_4_json_path)
        source_v9_6 = self._load_json(self.source_v9_6_json_path)

        run_payload = self._run_replicate_grid()
        robustness_summary = self._robustness_summary(run_payload["robustness_records"])
        non_upgrade_records = self._non_upgrade_records()
        allowed_claims = self._allowed_robustness_claims(robustness_summary["robustness_verdict"])
        forbidden_claims = self._forbidden_robustness_claims()

        counters = {
            "V9 safe toy replicate robustness artifact count": 1,
            "V9 safe toy replicate grid execution count": 1,
            "V9 safe toy replicate grid config count": len(run_payload["replicate_grid"]),
            "V9 safe toy replicate run record count": len(run_payload["replicate_run_records"]),
            "V9 VF-H2 robustness comparison record count": len(run_payload["robustness_records"]),
            "V9 VF-H2 positive ledger signal replicate count": robustness_summary["positive_signal_replicate_count"],
            "V9 VF-H2 zero ledger signal replicate count": robustness_summary["zero_signal_replicate_count"],
            "V9 VF-H2 negative ledger signal replicate count": robustness_summary["negative_signal_replicate_count"],
            "V9 VF-H2 robustness verdict count": 1,
            "V9 non-upgraded hypothesis record count": len(non_upgrade_records),
            "V9 allowed robustness claims register count": 1,
            "V9 allowed robustness claim count": len(allowed_claims),
            "V9 forbidden robustness claims register count": 1,
            "V9 forbidden robustness claim count": len(forbidden_claims),
            "V9 source primary supported hypothesis count": source_v9_6["scientific_yield_summary"]["not_falsified_toy_hypothesis_count"],
            "V9 source unresolved or unsupported hypothesis count": source_v9_6["scientific_yield_summary"]["unresolved_or_unsupported_hypothesis_count"],
            "V9 source manuscript readiness denial count": source_v9_6["counters"]["V9 source manuscript readiness denial count"],
            "V9 source toy falsification audit record count": source_v9_4["counters"]["V9 toy falsification audit record count"],
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
            "V9 manuscript readiness approval count": 0,
            "Toy evaluation validation claim count": 0,
            "Toy scientific evidence upgrade completed count": 0,
            "Toy manuscript coherence rewrite application count": 0,
            "Toy manuscript patch application checklist completion count": 0,
            "Toy manuscript patch application checklist execution count": 0,
            "Toy manuscript patch application permission count": 0,
            "Toy manuscript patch application applied patch count": 0,
            "Toy manuscript patch application manuscript file modified count": 0,
            "Toy manuscript patch application manuscript mutation count": 0,
            "Toy citation citation-ready source count": 0,
            "Toy citation actual citation count": 0,
            "Toy citation fabricated reference count": 0,
            "Toy citation integration completion count": 0,
            "Toy citation added to manuscript count": 0,
            "Real biological dataset import count": 0,
            "Real pathogen simulation count": 0,
            "Real receptor parameter count": 0,
            "Operational host targeting count": 0,
            "Wet-lab protocol count": 0,
            "Actionable biosafety-risk instruction count": 0,
            "Real-world infectivity optimization count": 0,
            "Immune evasion optimization count": 0,
            "Real host range prediction count": 0,
            "Proof assistant verification count": 0,
            "External validation count": 0,
            "Independent experiment count": 0,
            "Manuscript submission ready count": 0,
            "Readiness approval count": 0,
            "New citation added count": 0,
        }

        report = {
            "version": self.version,
            "title": "Viruse Fabric Safe Toy Replicate Grid and Signal Robustness Check",
            "plan_phrase": self.plan_phrase,
            "scope": "safe-toy-replicate-grid-and-signal-robustness-check-only",
            "safe_abstract_toy_only": True,
            "replicate_grid_executed": True,
            "signal_robustness_checked": True,
            "primary_hypothesis_under_test": self.primary_hypothesis,
            "primary_signal_under_test": self.signal_metric,
            "reduced_toy_core_under_test": "memory-ledger-driven toy dynamics",
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "source_v9_4_json": str(self.source_v9_4_json_path),
            "source_v9_6_json": str(self.source_v9_6_json_path),
            "replicate_grid": run_payload["replicate_grid"],
            "replicate_run_records": run_payload["replicate_run_records"],
            "robustness_records": run_payload["robustness_records"],
            "robustness_summary": robustness_summary,
            "non_upgrade_records": non_upgrade_records,
            "allowed_robustness_claims_register": allowed_claims,
            "forbidden_robustness_claims_register": forbidden_claims,
            "non_validation_disclaimer": (
                "Safe toy replicate grid and signal robustness check only. No validation claim is made. "
                "No manuscript readiness claim is made. No readiness approval is recorded. No manuscript file is modified. "
                "No citation is added. No external validation is performed. No independent experiment is performed. "
                "No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, "
                "no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction "
                "are introduced."
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "safe-toy-replicate-grid-and-signal-robustness-check-only":
            raise AssertionError("v9.7 must remain safe-toy-replicate-grid-and-signal-robustness-check-only.")

        for field in [
            "safe_abstract_toy_only",
            "replicate_grid_executed",
            "signal_robustness_checked",
        ]:
            if report[field] is not True:
                raise AssertionError(f"Expected True for {field}")

        for field in [
            "validation_claim_made",
            "readiness_approval_recorded",
            "manuscript_file_modified",
            "manuscript_mutation",
            "new_citation_added",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if report["primary_hypothesis_under_test"] != "VF-H2":
            raise AssertionError("v9.7 must test VF-H2 only.")

        if report["primary_signal_under_test"] != "ledger_effect_size":
            raise AssertionError("v9.7 must test ledger_effect_size.")

        if report["reduced_toy_core_under_test"] != "memory-ledger-driven toy dynamics":
            raise AssertionError("v9.7 must test the reduced memory-ledger toy core.")

        if len(report["replicate_grid"]) != len(self.seed_grid):
            raise AssertionError("Unexpected replicate grid size.")

        if len(report["replicate_run_records"]) != len(self.seed_grid) * 2:
            raise AssertionError("Expected two variant runs per replicate.")

        if len(report["robustness_records"]) != len(self.seed_grid):
            raise AssertionError("Expected one robustness record per replicate.")

        summary = report["robustness_summary"]
        if summary["hypothesis_id"] != "VF-H2":
            raise AssertionError("Robustness summary must be for VF-H2.")

        if summary["signal_metric"] != "ledger_effect_size":
            raise AssertionError("Robustness summary must be for ledger_effect_size.")

        if summary["replicate_count"] != len(self.seed_grid):
            raise AssertionError("Unexpected replicate count in summary.")

        if summary["positive_signal_replicate_count"] + summary["zero_signal_replicate_count"] + summary["negative_signal_replicate_count"] != summary["replicate_count"]:
            raise AssertionError("Replicate signal counts do not sum correctly.")

        if summary["robustness_verdict"] not in {
            "robust_in_this_safe_toy_replicate_grid",
            "partially_robust_in_this_safe_toy_replicate_grid",
            "not_robust_in_this_safe_toy_replicate_grid",
        }:
            raise AssertionError("Unexpected robustness verdict.")

        if len(report["non_upgrade_records"]) != 3:
            raise AssertionError("VF-H1, VF-H3, and VF-H4 must have non-upgrade records.")

        if {item["hypothesis_id"] for item in report["non_upgrade_records"]} != {"VF-H1", "VF-H3", "VF-H4"}:
            raise AssertionError("Only VF-H1, VF-H3, and VF-H4 may be listed as non-upgraded.")

        counters = report["counters"]

        expected_static_counts = {
            "V9 safe toy replicate robustness artifact count": 1,
            "V9 safe toy replicate grid execution count": 1,
            "V9 safe toy replicate grid config count": len(self.seed_grid),
            "V9 safe toy replicate run record count": len(self.seed_grid) * 2,
            "V9 VF-H2 robustness comparison record count": len(self.seed_grid),
            "V9 VF-H2 robustness verdict count": 1,
            "V9 non-upgraded hypothesis record count": 3,
            "V9 allowed robustness claims register count": 1,
            "V9 allowed robustness claim count": 3,
            "V9 forbidden robustness claims register count": 1,
            "V9 forbidden robustness claim count": 5,
            "V9 source primary supported hypothesis count": 1,
            "V9 source unresolved or unsupported hypothesis count": 3,
            "V9 source manuscript readiness denial count": 1,
            "V9 source toy falsification audit record count": 4,
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
            "V9 manuscript readiness approval count": 0,
        }

        for name, expected in expected_static_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        if counters["V9 VF-H2 positive ledger signal replicate count"] != summary["positive_signal_replicate_count"]:
            raise AssertionError("Positive signal counter mismatch.")

        if counters["V9 VF-H2 zero ledger signal replicate count"] != summary["zero_signal_replicate_count"]:
            raise AssertionError("Zero signal counter mismatch.")

        if counters["V9 VF-H2 negative ledger signal replicate count"] != summary["negative_signal_replicate_count"]:
            raise AssertionError("Negative signal counter mismatch.")

        must_be_zero = [
            "V9 theory validation claim count",
            "V9 manuscript readiness claim count",
            "V9 manuscript readiness approval count",
            "Toy evaluation validation claim count",
            "Toy scientific evidence upgrade completed count",
            "Toy manuscript coherence rewrite application count",
            "Toy manuscript patch application checklist completion count",
            "Toy manuscript patch application checklist execution count",
            "Toy manuscript patch application permission count",
            "Toy manuscript patch application applied patch count",
            "Toy manuscript patch application manuscript file modified count",
            "Toy manuscript patch application manuscript mutation count",
            "Toy citation citation-ready source count",
            "Toy citation actual citation count",
            "Toy citation fabricated reference count",
            "Toy citation integration completion count",
            "Toy citation added to manuscript count",
            "Real biological dataset import count",
            "Real pathogen simulation count",
            "Real receptor parameter count",
            "Operational host targeting count",
            "Wet-lab protocol count",
            "Actionable biosafety-risk instruction count",
            "Real-world infectivity optimization count",
            "Immune evasion optimization count",
            "Real host range prediction count",
            "Proof assistant verification count",
            "External validation count",
            "Independent experiment count",
            "Manuscript submission ready count",
            "Readiness approval count",
            "New citation added count",
        ]

        for name in must_be_zero:
            if counters.get(name) != 0:
                raise AssertionError(f"Counter must remain zero: {name}")

        combined_text = json.dumps(report, ensure_ascii=False)

        required_phrases = [
            "safe toy replicate grid",
            "signal robustness check",
            "memory-ledger-driven toy dynamics",
            "ledger_effect_size",
            "VF-H2",
            "VF-H1",
            "VF-H3",
            "VF-H4",
            "not_upgraded",
            "robust_in_this_safe_toy_replicate_grid",
            "partially_robust_in_this_safe_toy_replicate_grid",
            "not_robust_in_this_safe_toy_replicate_grid",
            "No validation claim is made",
            "No manuscript readiness claim is made",
            "No readiness approval is recorded",
            "No manuscript file is modified",
            "No citation is added",
            "No external validation is performed",
            "No independent experiment is performed",
            "No real biological datasets",
            "no real pathogen models",
            "no receptor parameters",
            "no operational targeting",
            "no wet-lab protocol",
            "no infectivity optimization",
            "no immune evasion optimization",
            "no host range prediction",
        ]

        for phrase in required_phrases:
            if phrase not in combined_text:
                raise AssertionError(f"Missing required v9.7 phrase: {phrase}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Viruse Fabric Safe Toy Replicate Grid and Signal Robustness Check")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is safe-toy-replicate-grid-and-signal-robustness-check-only.")
        lines.append("It checks whether the v9.6 reduced memory-ledger toy core remains visible across a safe abstract toy replicate grid.")
        lines.append("Exact phrase marker: safe toy replicate grid.")
        lines.append("Exact phrase marker: signal robustness check.")
        lines.append("It does not validate the theory, does not approve manuscript readiness, does not modify manuscript files, and does not add citations.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")

        lines.append("## Robustness Summary")
        lines.append("")
        for key, value in report["robustness_summary"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Replicate Grid")
        lines.append("")
        for item in report["replicate_grid"]:
            lines.append(f"### {item['replicate_id']}")
            lines.append("")
            lines.append(f"- graph_seed: {item['graph_seed']}")
            lines.append(f"- packet_seed: {item['packet_seed']}")
            lines.append(f"- transition_seed: {item['transition_seed']}")
            lines.append(f"- symbolic_drift_seed: {item['symbolic_drift_seed']}")
            lines.append(f"- node_count: {item['node_count']}")
            lines.append(f"- packet_count: {item['packet_count']}")
            lines.append(f"- step_count_limit: {item['step_count_limit']}")
            lines.append("")

        lines.append("## Robustness Records")
        lines.append("")
        for item in report["robustness_records"]:
            lines.append(f"### {item['robustness_record_id']}")
            lines.append("")
            lines.append(f"- Replicate id: {item['replicate_id']}")
            lines.append(f"- Hypothesis id: {item['hypothesis_id']}")
            lines.append(f"- Reference variant: {item['reference_variant']}")
            lines.append(f"- Ablation variant: {item['ablation_variant']}")
            lines.append(f"- Signal metric: {item['signal_metric']}")
            lines.append(f"- Reference metric value: {item['reference_metric_value']}")
            lines.append(f"- Ablation metric value: {item['ablation_metric_value']}")
            lines.append(f"- Signal delta: {item['signal_delta']}")
            lines.append(f"- Positive signal: {item['positive_signal']}")
            lines.append(f"- Metric deltas: {item['metric_deltas']}")
            lines.append(f"- Boundary: {item['boundary']}")
            lines.append("")

        lines.append("## Non-Upgrade Records")
        lines.append("")
        for item in report["non_upgrade_records"]:
            lines.append(f"### {item['hypothesis_id']}")
            lines.append("")
            lines.append(f"- Mechanism: {item['mechanism']}")
            lines.append(f"- Status after v9.7: {item['status_after_v9_7']}")
            lines.append(f"- Reason: {item['reason']}")
            lines.append("")

        lines.append("## Allowed Robustness Claims")
        lines.append("")
        for item in report["allowed_robustness_claims_register"]:
            lines.append(f"### {item['claim_id']}")
            lines.append("")
            lines.append(f"- Claim text: {item['claim_text']}")
            lines.append(f"- Scope: {item['scope']}")
            lines.append("")

        lines.append("## Forbidden Robustness Claims")
        lines.append("")
        for item in report["forbidden_robustness_claims_register"]:
            lines.append(f"### {item['claim_id']}")
            lines.append("")
            lines.append(f"- Forbidden claim: {item['forbidden_claim']}")
            lines.append(f"- Reason: {item['reason']}")
            lines.append("")

        lines.append("## Required Verification Marker Registry")
        lines.append("")
        required_markers = [
            "safe toy replicate grid",
            "signal robustness check",
            "memory-ledger-driven toy dynamics",
            "ledger_effect_size",
            "VF-H2",
            "VF-H1",
            "VF-H3",
            "VF-H4",
            "not_upgraded",
            "robust_in_this_safe_toy_replicate_grid",
            "partially_robust_in_this_safe_toy_replicate_grid",
            "not_robust_in_this_safe_toy_replicate_grid",
            "No validation claim is made",
            "No manuscript readiness claim is made",
            "No readiness approval is recorded",
            "No manuscript file is modified",
            "No citation is added",
            "No external validation is performed",
            "No independent experiment is performed",
            "No real biological datasets",
            "no real pathogen models",
            "no receptor parameters",
            "no operational targeting",
            "no wet-lab protocol",
            "no infectivity optimization",
            "no immune evasion optimization",
            "no host range prediction",
        ]
        for marker in required_markers:
            lines.append(f"- {marker}")
        lines.append("")

        lines.append("## Non-Validation Disclaimer")
        lines.append("")
        lines.append(report["non_validation_disclaimer"])
        lines.append("")

        lines.append("## Counters")
        lines.append("")
        for key, value in report["counters"].items():
            lines.append(f"{key}: {value}")

        lines.append("")
        lines.append("## Result")
        lines.append("")
        lines.append(f"Passed: {report['passed']}")
        lines.append("")
        lines.append("V9_7_VIRUSE_FABRIC_SAFE_TOY_REPLICATE_GRID_AND_SIGNAL_ROBUSTNESS_CHECK_OK")
        lines.append("")

        return "\n".join(lines)

    def run(self) -> Dict[str, Any]:
        report = self.build()
        self.output_md_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_json_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_md_path.write_text(self.render_markdown(report), encoding="utf-8")
        self.output_json_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return report


def build_viruse_fabric_safe_toy_replicate_grid_and_signal_robustness_check() -> Dict[str, Any]:
    return ViruseFabricSafeToyReplicateGridAndSignalRobustnessCheckBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_safe_toy_replicate_grid_and_signal_robustness_check()
    counters = result["counters"]
    summary = result["robustness_summary"]
    print("V9_7_VIRUSE_FABRIC_SAFE_TOY_REPLICATE_GRID_AND_SIGNAL_ROBUSTNESS_CHECK_OK")
    print("VIRUSE_FABRIC_SAFE_TOY_REPLICATE_GRID_AND_SIGNAL_ROBUSTNESS_CHECK_DIRECT_CHECK_OK")
    print(f"Primary hypothesis under test: {result['primary_hypothesis_under_test']}")
    print(f"Primary signal under test: {result['primary_signal_under_test']}")
    print(f"Reduced toy core under test: {result['reduced_toy_core_under_test']}")
    print(f"Replicate count: {summary['replicate_count']}")
    print(f"Positive signal replicate count: {summary['positive_signal_replicate_count']}")
    print(f"Zero signal replicate count: {summary['zero_signal_replicate_count']}")
    print(f"Negative signal replicate count: {summary['negative_signal_replicate_count']}")
    print(f"Positive signal rate: {summary['positive_signal_rate']}")
    print(f"Mean signal delta: {summary['mean_signal_delta']}")
    print(f"Robustness verdict: {summary['robustness_verdict']}")
    print(f"Replicate grid execution count: {counters['V9 safe toy replicate grid execution count']}")
    print(f"Replicate run record count: {counters['V9 safe toy replicate run record count']}")
    print(f"VF-H2 robustness comparison record count: {counters['V9 VF-H2 robustness comparison record count']}")
    print(f"Non-upgraded hypothesis record count: {counters['V9 non-upgraded hypothesis record count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Manuscript readiness claim count: {counters['V9 manuscript readiness claim count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
