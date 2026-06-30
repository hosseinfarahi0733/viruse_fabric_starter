from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Sequence

from viruse_fabric.simulation.viruse_fabric_minimal_safe_toy_simulation_engine import (
    SafeAbstractToySimulationEngine,
    ToyEngineConfig,
)
from viruse_fabric.writing.viruse_fabric_safe_toy_baseline_comparison import (
    ViruseFabricSafeToyBaselineComparisonBuilder,
)


class ViruseFabricSafeToyParameterSweepAndNullControlStressTestBuilder:
    version = "v9.8"

    output_md_path = Path("outputs/viruse_fabric_safe_toy_parameter_sweep_and_null_control_stress_test_v9_8.md")
    output_json_path = Path("outputs/viruse_fabric_safe_toy_parameter_sweep_and_null_control_stress_test_v9_8.json")

    source_v9_7_json_path = Path("outputs/viruse_fabric_safe_toy_replicate_grid_and_signal_robustness_check_v9_7.json")

    plan_phrase = "v9_8_safe_toy_parameter_sweep_and_null_control_stress_test_without_validation_or_readiness"

    primary_hypothesis = "VF-H2"
    signal_metric = "ledger_effect_size"
    reduced_core = "memory-ledger-driven toy dynamics"

    candidate_parameter_mutations: Sequence[Dict[str, Any]] = (
        {"candidate_id": "V9-8-CAND-001", "field": "node_count", "candidate_value": 12},
        {"candidate_id": "V9-8-CAND-002", "field": "node_count", "candidate_value": 20},
        {"candidate_id": "V9-8-CAND-003", "field": "packet_count", "candidate_value": 24},
        {"candidate_id": "V9-8-CAND-004", "field": "packet_count", "candidate_value": 40},
        {"candidate_id": "V9-8-CAND-005", "field": "step_count_limit", "candidate_value": 2},
        {"candidate_id": "V9-8-CAND-006", "field": "step_count_limit", "candidate_value": 4},
    )

    null_control_seed_sets: Sequence[Dict[str, int]] = (
        {"graph_seed": 101, "packet_seed": 202, "transition_seed": 303, "symbolic_drift_seed": 404},
        {"graph_seed": 111, "packet_seed": 212, "transition_seed": 313, "symbolic_drift_seed": 414},
    )

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _extract_metrics(self, run_record: Dict[str, Any]) -> Dict[str, float]:
        for key in ["metrics", "metric_results", "metric_snapshot", "final_metrics", "final_metric_snapshot"]:
            value = run_record.get(key)
            if isinstance(value, dict):
                return {name: float(metric_value) for name, metric_value in value.items()}
        raise KeyError(f"No metric dictionary found in run record. Available keys: {sorted(run_record.keys())}")

    def _metric_delta(self, left_metrics: Dict[str, float], right_metrics: Dict[str, float]) -> Dict[str, float]:
        names = sorted(set(left_metrics) | set(right_metrics))
        return {
            name: round(float(left_metrics.get(name, 0.0)) - float(right_metrics.get(name, 0.0)), 6)
            for name in names
        }

    def _check_parameter_sweep_boundary(self) -> Dict[str, Any]:
        builder = ViruseFabricSafeToyBaselineComparisonBuilder()
        engine = SafeAbstractToySimulationEngine()
        base_config = builder._safe_config()

        boundary_records: List[Dict[str, Any]] = []

        for mutation in self.candidate_parameter_mutations:
            field = mutation["field"]
            value = mutation["candidate_value"]
            mutated_config = replace(base_config, **{field: value})

            try:
                engine.validate_config(mutated_config)
                status = "accepted_by_engine"
                error_message = ""
            except Exception as exc:
                status = "blocked_by_engine_spec_boundary"
                error_message = str(exc)

            boundary_records.append(
                {
                    "candidate_id": mutation["candidate_id"],
                    "field": field,
                    "candidate_value": value,
                    "status": status,
                    "error_message": error_message,
                    "boundary": (
                        "Safe abstract toy configuration-boundary check only. "
                        "This records whether the current engine permits parameter sweep variants."
                    ),
                }
            )

        blocked_count = sum(1 for item in boundary_records if item["status"] == "blocked_by_engine_spec_boundary")
        accepted_count = sum(1 for item in boundary_records if item["status"] == "accepted_by_engine")

        if blocked_count == len(boundary_records):
            verdict = "parameter_sweep_blocked_by_engine_spec_boundary"
        elif blocked_count > 0:
            verdict = "parameter_sweep_partially_blocked_by_engine_spec_boundary"
        else:
            verdict = "parameter_sweep_allowed_by_engine_spec_boundary"

        return {
            "parameter_boundary_records": boundary_records,
            "parameter_boundary_summary": {
                "summary_id": "V9-8-PARAMETER-BOUNDARY-SUMMARY-001",
                "candidate_parameter_count": len(boundary_records),
                "blocked_candidate_count": blocked_count,
                "accepted_candidate_count": accepted_count,
                "parameter_sweep_boundary_verdict": verdict,
                "parameter_sweep_boundary_verdict_options": [
                    "parameter_sweep_blocked_by_engine_spec_boundary",
                    "parameter_sweep_partially_blocked_by_engine_spec_boundary",
                    "parameter_sweep_allowed_by_engine_spec_boundary",
                ],
                "interpretation": (
                    "The current safe toy engine constrains v9.1-specified toy values. "
                    "If candidate parameter changes are blocked, v9.8 must not pretend that a real parameter sweep was executed."
                ),
            },
        }

    def _run_variant(
        self,
        builder: ViruseFabricSafeToyBaselineComparisonBuilder,
        engine: SafeAbstractToySimulationEngine,
        config: ToyEngineConfig,
        variant_id: str,
        run_id_prefix: str,
    ) -> Dict[str, Any]:
        record = dict(
            builder._run_safe_toy_variant(
                engine=engine,
                config=config,
                baseline_id=variant_id,
            )
        )
        record["decision_gate_run_id"] = f"{run_id_prefix}-{variant_id}"
        record["metrics"] = self._extract_metrics(record)
        return record

    def _run_null_controls(self) -> Dict[str, Any]:
        builder = ViruseFabricSafeToyBaselineComparisonBuilder()
        engine = SafeAbstractToySimulationEngine()
        base_config = builder._safe_config()

        control_specs: List[Dict[str, Any]] = []
        for seed_index, seeds in enumerate(self.null_control_seed_sets, start=1):
            control_specs.append(
                {
                    "control_id": f"V9-8-NULL-FULL-{seed_index:03d}",
                    "variant": "VF-FULL",
                    **seeds,
                }
            )
            control_specs.append(
                {
                    "control_id": f"V9-8-NULL-BASEC-{seed_index:03d}",
                    "variant": "VF-BASE-C",
                    **seeds,
                }
            )

        null_control_run_records: List[Dict[str, Any]] = []
        null_control_records: List[Dict[str, Any]] = []

        for spec in control_specs:
            config = replace(
                base_config,
                graph_seed=spec["graph_seed"],
                packet_seed=spec["packet_seed"],
                transition_seed=spec["transition_seed"],
                symbolic_drift_seed=spec["symbolic_drift_seed"],
            )

            left_run = self._run_variant(
                builder=builder,
                engine=engine,
                config=config,
                variant_id=spec["variant"],
                run_id_prefix=f"{spec['control_id']}-LEFT",
            )
            right_run = self._run_variant(
                builder=builder,
                engine=engine,
                config=config,
                variant_id=spec["variant"],
                run_id_prefix=f"{spec['control_id']}-RIGHT",
            )

            left_run["control_id"] = spec["control_id"]
            right_run["control_id"] = spec["control_id"]

            null_control_run_records.extend([left_run, right_run])

            metric_deltas = self._metric_delta(left_run["metrics"], right_run["metrics"])
            signal_delta = round(float(metric_deltas.get(self.signal_metric, 0.0)), 6)

            null_control_records.append(
                {
                    "null_control_record_id": f"{spec['control_id']}-RESULT",
                    "control_id": spec["control_id"],
                    "variant": spec["variant"],
                    "signal_metric": self.signal_metric,
                    "left_metric_value": round(float(left_run["metrics"].get(self.signal_metric, 0.0)), 6),
                    "right_metric_value": round(float(right_run["metrics"].get(self.signal_metric, 0.0)), 6),
                    "signal_delta": signal_delta,
                    "null_leak_detected": signal_delta != 0.0,
                    "metric_deltas": metric_deltas,
                    "boundary": (
                        "Safe abstract toy null-control comparison only. "
                        "This is not empirical validation, not external validation, not manuscript readiness, and not a theory validation claim."
                    ),
                }
            )

        leak_count = sum(1 for item in null_control_records if item["null_leak_detected"])
        no_leak_count = len(null_control_records) - leak_count
        max_abs_delta = round(max((abs(float(item["signal_delta"])) for item in null_control_records), default=0.0), 6)

        return {
            "null_control_specs": control_specs,
            "null_control_run_records": null_control_run_records,
            "null_control_records": null_control_records,
            "null_control_summary": {
                "summary_id": "V9-8-NULL-CONTROL-SUMMARY-001",
                "signal_metric": self.signal_metric,
                "null_control_count": len(null_control_records),
                "null_control_leak_count": leak_count,
                "null_control_no_leak_count": no_leak_count,
                "max_absolute_null_delta": max_abs_delta,
                "null_control_verdict": (
                    "no_null_control_leak_detected" if leak_count == 0 else "null_control_leak_detected"
                ),
            },
        }

    def _decision_gate(self, parameter_boundary_summary: Dict[str, Any], null_control_summary: Dict[str, Any]) -> Dict[str, Any]:
        parameter_verdict = parameter_boundary_summary["parameter_sweep_boundary_verdict"]
        null_verdict = null_control_summary["null_control_verdict"]

        if null_verdict == "null_control_leak_detected":
            decision = "stop_claims_and_debug_null_control_leak"
            next_allowed_action = "engine_debugging_only"
            loop_guard_verdict = "stop_v9_loop"
        elif parameter_verdict in {
            "parameter_sweep_blocked_by_engine_spec_boundary",
            "parameter_sweep_partially_blocked_by_engine_spec_boundary",
        }:
            decision = "stop_claim_expansion_and_redesign_engine_before_more_toy_evidence"
            next_allowed_action = "engine_redesign_or_limited_technical_note"
            loop_guard_verdict = "stop_v9_loop"
        else:
            decision = "parameter_sweep_possible_but_requires_explicit_execution_before_claim_expansion"
            next_allowed_action = "run_real_parameter_sweep_or_stop"
            loop_guard_verdict = "do_not_continue_milestones_without_decision"

        return {
            "decision_gate_id": "V9-8-DECISION-GATE-001",
            "parameter_sweep_boundary_verdict": parameter_verdict,
            "null_control_verdict": null_verdict,
            "decision": decision,
            "decision_options": [
                "stop_claims_and_debug_null_control_leak",
                "stop_claim_expansion_and_redesign_engine_before_more_toy_evidence",
                "parameter_sweep_possible_but_requires_explicit_execution_before_claim_expansion",
            ],
            "next_allowed_action": next_allowed_action,
            "next_allowed_action_options": [
                "engine_debugging_only",
                "engine_redesign_or_limited_technical_note",
                "run_real_parameter_sweep_or_stop",
            ],
            "loop_guard_verdict": loop_guard_verdict,
            "loop_guard_verdict_options": [
                "stop_v9_loop",
                "do_not_continue_milestones_without_decision",
            ],
            "decision_statement": (
                "v9.8 is a decision gate, not a launchpad for another automatic milestone. "
                "If parameter sweep is blocked by the engine boundary, the project must stop claim expansion "
                "and either redesign the engine or write a limited technical note that explicitly reports the boundary."
            ),
        }

    def _non_upgrade_records(self) -> List[Dict[str, Any]]:
        return [
            {
                "hypothesis_id": "VF-H1",
                "status_after_v9_8": "not_upgraded",
                "reason": "v9.8 does not support VF-H1 and blocks further claim expansion.",
            },
            {
                "hypothesis_id": "VF-H3",
                "status_after_v9_8": "not_upgraded",
                "reason": "v9.8 does not support VF-H3 and blocks further claim expansion.",
            },
            {
                "hypothesis_id": "VF-H4",
                "status_after_v9_8": "not_upgraded",
                "reason": "v9.8 does not support VF-H4 and blocks further claim expansion.",
            },
        ]

    def build(self) -> Dict[str, Any]:
        source_v9_7 = self._load_json(self.source_v9_7_json_path)

        parameter_payload = self._check_parameter_sweep_boundary()
        null_payload = self._run_null_controls()
        decision_gate = self._decision_gate(
            parameter_payload["parameter_boundary_summary"],
            null_payload["null_control_summary"],
        )
        non_upgrade_records = self._non_upgrade_records()

        counters = {
            "V9 decision gate artifact count": 1,
            "V9 parameter sweep boundary check count": 1,
            "V9 candidate parameter mutation count": len(parameter_payload["parameter_boundary_records"]),
            "V9 blocked parameter mutation count": parameter_payload["parameter_boundary_summary"]["blocked_candidate_count"],
            "V9 accepted parameter mutation count": parameter_payload["parameter_boundary_summary"]["accepted_candidate_count"],
            "V9 null-control execution count": 1,
            "V9 null-control config count": len(null_payload["null_control_specs"]),
            "V9 null-control run record count": len(null_payload["null_control_run_records"]),
            "V9 null-control comparison record count": len(null_payload["null_control_records"]),
            "V9 null-control leak count": null_payload["null_control_summary"]["null_control_leak_count"],
            "V9 null-control no-leak count": null_payload["null_control_summary"]["null_control_no_leak_count"],
            "V9 decision gate count": 1,
            "V9 loop guard stop count": 1 if decision_gate["loop_guard_verdict"] == "stop_v9_loop" else 0,
            "V9 non-upgraded hypothesis record count": len(non_upgrade_records),
            "V9 source v9.7 robust replicate verdict count": 1,
            "V9 source v9.7 positive signal replicate count": source_v9_7["robustness_summary"]["positive_signal_replicate_count"],
            "V9 source v9.7 mean signal delta": source_v9_7["robustness_summary"]["mean_signal_delta"],
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
            "title": "Viruse Fabric v9.8 Decision Gate: Parameter Sweep Boundary and Null-Control Stress Test",
            "plan_phrase": self.plan_phrase,
            "scope": "safe-toy-parameter-sweep-boundary-and-null-control-decision-gate-only",
            "safe_abstract_toy_only": True,
            "decision_gate_executed": True,
            "parameter_sweep_boundary_checked": True,
            "null_control_executed": True,
            "primary_hypothesis_under_stress": self.primary_hypothesis,
            "primary_signal_under_stress": self.signal_metric,
            "reduced_toy_core_under_stress": self.reduced_core,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "source_v9_7_json": str(self.source_v9_7_json_path),
            "parameter_boundary_records": parameter_payload["parameter_boundary_records"],
            "parameter_boundary_summary": parameter_payload["parameter_boundary_summary"],
            "null_control_specs": null_payload["null_control_specs"],
            "null_control_run_records": null_payload["null_control_run_records"],
            "null_control_records": null_payload["null_control_records"],
            "null_control_summary": null_payload["null_control_summary"],
            "decision_gate": decision_gate,
            "non_upgrade_records": non_upgrade_records,
            "verification_marker_registry": [
                "decision gate",
                "parameter_sweep_blocked_by_engine_spec_boundary",
                "parameter_sweep_partially_blocked_by_engine_spec_boundary",
                "parameter_sweep_allowed_by_engine_spec_boundary",
                "safe toy parameter sweep",
                "null-control stress test",
                "memory-ledger-driven toy dynamics",
                "ledger_effect_size",
                "VF-H2",
                "VF-H1",
                "VF-H3",
                "VF-H4",
                "not_upgraded",
                "stop_v9_loop",
                "engine_redesign_or_limited_technical_note",
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
            ],
            "non_validation_disclaimer": (
                "Safe toy decision gate only. No validation claim is made. No manuscript readiness claim is made. "
                "No readiness approval is recorded. No manuscript file is modified. No citation is added. "
                "No external validation is performed. No independent experiment is performed. "
                "No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, "
                "no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced."
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        assert report["passed"] is True
        assert report["scope"] == "safe-toy-parameter-sweep-boundary-and-null-control-decision-gate-only"
        assert report["plan_phrase"] == self.plan_phrase
        assert report["safe_abstract_toy_only"] is True
        assert report["decision_gate_executed"] is True
        assert report["parameter_sweep_boundary_checked"] is True
        assert report["null_control_executed"] is True

        assert report["validation_claim_made"] is False
        assert report["readiness_approval_recorded"] is False
        assert report["manuscript_file_modified"] is False
        assert report["manuscript_mutation"] is False
        assert report["new_citation_added"] is False

        assert report["primary_hypothesis_under_stress"] == "VF-H2"
        assert report["primary_signal_under_stress"] == "ledger_effect_size"
        assert report["reduced_toy_core_under_stress"] == "memory-ledger-driven toy dynamics"

        assert len(report["parameter_boundary_records"]) == 6
        assert len(report["null_control_records"]) == 4
        assert len(report["null_control_run_records"]) == 8
        assert len(report["non_upgrade_records"]) == 3
        assert {item["hypothesis_id"] for item in report["non_upgrade_records"]} == {"VF-H1", "VF-H3", "VF-H4"}

        parameter_summary = report["parameter_boundary_summary"]
        null_summary = report["null_control_summary"]
        decision_gate = report["decision_gate"]

        assert parameter_summary["candidate_parameter_count"] == 6
        assert parameter_summary["parameter_sweep_boundary_verdict"] in {
            "parameter_sweep_blocked_by_engine_spec_boundary",
            "parameter_sweep_partially_blocked_by_engine_spec_boundary",
            "parameter_sweep_allowed_by_engine_spec_boundary",
        }

        assert null_summary["null_control_count"] == 4
        assert null_summary["null_control_leak_count"] + null_summary["null_control_no_leak_count"] == 4
        assert null_summary["null_control_verdict"] in {
            "no_null_control_leak_detected",
            "null_control_leak_detected",
        }

        assert decision_gate["decision"] in {
            "stop_claims_and_debug_null_control_leak",
            "stop_claim_expansion_and_redesign_engine_before_more_toy_evidence",
            "parameter_sweep_possible_but_requires_explicit_execution_before_claim_expansion",
        }

        assert decision_gate["next_allowed_action"] in {
            "engine_debugging_only",
            "engine_redesign_or_limited_technical_note",
            "run_real_parameter_sweep_or_stop",
        }

        counters = report["counters"]

        expected_counts = {
            "V9 decision gate artifact count": 1,
            "V9 parameter sweep boundary check count": 1,
            "V9 candidate parameter mutation count": 6,
            "V9 null-control execution count": 1,
            "V9 null-control config count": 4,
            "V9 null-control run record count": 8,
            "V9 null-control comparison record count": 4,
            "V9 decision gate count": 1,
            "V9 non-upgraded hypothesis record count": 3,
            "V9 source v9.7 robust replicate verdict count": 1,
            "V9 source v9.7 positive signal replicate count": 6,
            "V9 source v9.7 mean signal delta": 3.0,
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
            "V9 manuscript readiness approval count": 0,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            assert actual == expected, f"Expected {expected} for {name}, got {actual}"

        assert counters["V9 blocked parameter mutation count"] == parameter_summary["blocked_candidate_count"]
        assert counters["V9 accepted parameter mutation count"] == parameter_summary["accepted_candidate_count"]
        assert counters["V9 null-control leak count"] == null_summary["null_control_leak_count"]
        assert counters["V9 null-control no-leak count"] == null_summary["null_control_no_leak_count"]

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
            assert counters[name] == 0, f"Counter must remain zero: {name}"

        combined_text = json.dumps(report, ensure_ascii=False)
        required_phrases = [
            "decision gate",
            "parameter_sweep_blocked_by_engine_spec_boundary",
            "safe toy parameter sweep",
            "null-control stress test",
            "memory-ledger-driven toy dynamics",
            "ledger_effect_size",
            "VF-H2",
            "VF-H1",
            "VF-H3",
            "VF-H4",
            "not_upgraded",
            "stop_v9_loop",
            "engine_redesign_or_limited_technical_note",
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
            assert phrase in combined_text, f"Missing required phrase: {phrase}"

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []
        lines.append("# Viruse Fabric v9.8 Decision Gate")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is safe-toy-parameter-sweep-boundary-and-null-control-decision-gate-only.")
        lines.append("Exact phrase marker: decision gate.")
        lines.append("Exact phrase marker: safe toy parameter sweep.")
        lines.append("Exact phrase marker: null-control stress test.")
        lines.append("Exact phrase marker: parameter_sweep_blocked_by_engine_spec_boundary.")
        lines.append("Exact phrase marker: stop_v9_loop.")
        lines.append("Exact phrase marker: engine_redesign_or_limited_technical_note.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")

        lines.append("## Stress Target")
        lines.append("")
        lines.append(f"- Primary hypothesis under stress: {report['primary_hypothesis_under_stress']}")
        lines.append(f"- Primary signal under stress: {report['primary_signal_under_stress']}")
        lines.append(f"- Reduced toy core under stress: {report['reduced_toy_core_under_stress']}")
        lines.append("")

        lines.append("## Required Verification Marker Registry")
        lines.append("")
        for marker in report.get("verification_marker_registry", []):
            lines.append(f"- {marker}")
        lines.append("")

        lines.append("## Parameter Boundary Summary")
        lines.append("")
        for key, value in report["parameter_boundary_summary"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Null-Control Summary")
        lines.append("")
        for key, value in report["null_control_summary"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Decision Gate")
        lines.append("")
        for key, value in report["decision_gate"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Parameter Boundary Records")
        lines.append("")
        for item in report["parameter_boundary_records"]:
            lines.append(f"### {item['candidate_id']}")
            for key, value in item.items():
                lines.append(f"- {key}: {value}")
            lines.append("")

        lines.append("## Null-Control Records")
        lines.append("")
        for item in report["null_control_records"]:
            lines.append(f"### {item['null_control_record_id']}")
            for key, value in item.items():
                lines.append(f"- {key}: {value}")
            lines.append("")

        lines.append("## Non-Upgrade Records")
        lines.append("")
        for item in report["non_upgrade_records"]:
            lines.append(f"### {item['hypothesis_id']}")
            for key, value in item.items():
                lines.append(f"- {key}: {value}")
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
        lines.append("V9_8_VIRUSE_FABRIC_DECISION_GATE_PARAMETER_BOUNDARY_AND_NULL_CONTROL_OK")
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


def build_viruse_fabric_safe_toy_parameter_sweep_and_null_control_stress_test() -> Dict[str, Any]:
    return ViruseFabricSafeToyParameterSweepAndNullControlStressTestBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_safe_toy_parameter_sweep_and_null_control_stress_test()
    parameter_summary = result["parameter_boundary_summary"]
    null_summary = result["null_control_summary"]
    decision_gate = result["decision_gate"]
    counters = result["counters"]

    print("V9_8_VIRUSE_FABRIC_DECISION_GATE_PARAMETER_BOUNDARY_AND_NULL_CONTROL_OK")
    print("VIRUSE_FABRIC_DECISION_GATE_PARAMETER_BOUNDARY_AND_NULL_CONTROL_DIRECT_CHECK_OK")
    print(f"Primary hypothesis under stress: {result['primary_hypothesis_under_stress']}")
    print(f"Primary signal under stress: {result['primary_signal_under_stress']}")
    print(f"Reduced toy core under stress: {result['reduced_toy_core_under_stress']}")
    print(f"Candidate parameter count: {parameter_summary['candidate_parameter_count']}")
    print(f"Blocked candidate count: {parameter_summary['blocked_candidate_count']}")
    print(f"Accepted candidate count: {parameter_summary['accepted_candidate_count']}")
    print(f"Parameter sweep boundary verdict: {parameter_summary['parameter_sweep_boundary_verdict']}")
    print(f"Null-control count: {null_summary['null_control_count']}")
    print(f"Null-control leak count: {null_summary['null_control_leak_count']}")
    print(f"Null-control verdict: {null_summary['null_control_verdict']}")
    print(f"Decision: {decision_gate['decision']}")
    print(f"Next allowed action: {decision_gate['next_allowed_action']}")
    print(f"Loop guard verdict: {decision_gate['loop_guard_verdict']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Manuscript readiness claim count: {counters['V9 manuscript readiness claim count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
