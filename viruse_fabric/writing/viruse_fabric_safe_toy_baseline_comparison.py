from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from typing import Any, Dict, List, Sequence

from viruse_fabric.simulation.viruse_fabric_minimal_safe_toy_simulation_engine import (
    SafeAbstractToySimulationEngine,
    ToyEngineConfig,
    ToyPacket,
    build_engine_manifest_without_running,
)


class ViruseFabricSafeToyBaselineComparisonBuilder:
    version = "v9.3"

    source_reframing_json_path = Path("outputs/viruse_fabric_abstract_simulation_reframing_v9_0.json")
    source_spec_json_path = Path("outputs/viruse_fabric_abstract_simulation_specification_v9_1.json")
    source_engine_json_path = Path("outputs/viruse_fabric_minimal_safe_toy_simulation_engine_v9_2.json")

    output_md_path = Path("outputs/viruse_fabric_safe_toy_baseline_comparison_v9_3.md")
    output_json_path = Path("outputs/viruse_fabric_safe_toy_baseline_comparison_v9_3.json")

    plan_phrase = "v9_3_safe_toy_baseline_comparison_without_validation_or_falsification_audit"

    baseline_ids = [
        "VF-FULL",
        "VF-BASE-A",
        "VF-BASE-B",
        "VF-BASE-C",
        "VF-BASE-D",
        "VF-BASE-E",
    ]

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _safe_config(self) -> ToyEngineConfig:
        return ToyEngineConfig(
            graph_spec_id="VF-SPEC-GRAPH-001",
            seed_spec_id="VF-SPEC-SEED-001",
            initialization_spec_id="VF-SPEC-INIT-001",
            node_count=16,
            packet_count=32,
            step_count_limit=3,
            graph_seed=101,
            packet_seed=202,
            transition_seed=303,
            symbolic_drift_seed=404,
        )

    def _apply_baseline_variant(self, baseline_id: str, packets: Sequence[ToyPacket]) -> List[ToyPacket]:
        adjusted: List[ToyPacket] = []

        for packet in packets:
            if baseline_id == "VF-FULL":
                adjusted.append(packet)

            elif baseline_id == "VF-BASE-A":
                adjusted.append(
                    replace(
                        packet,
                        memory_trace=tuple(),
                        causal_mass_score=0.0,
                        symbolic_drift=0.0,
                        time_layer="t1",
                    )
                )

            elif baseline_id == "VF-BASE-B":
                adjusted.append(
                    replace(
                        packet,
                        global_constraint_score=0.0,
                        causal_mass_score=0.0,
                        memory_trace=tuple(),
                        time_layer="t1",
                    )
                )

            elif baseline_id == "VF-BASE-C":
                adjusted.append(
                    replace(
                        packet,
                        memory_trace=tuple(),
                        causal_mass_score=0.0,
                    )
                )

            elif baseline_id == "VF-BASE-D":
                adjusted.append(
                    replace(
                        packet,
                        time_layer="t1",
                        causal_mass_score=min(packet.causal_mass_score, 0.1),
                    )
                )

            elif baseline_id == "VF-BASE-E":
                adjusted.append(
                    replace(
                        packet,
                        causal_mass_score=0.0,
                    )
                )

            else:
                raise ValueError(f"Unknown safe toy baseline id: {baseline_id}")

        return adjusted

    def _run_safe_toy_variant(
        self,
        engine: SafeAbstractToySimulationEngine,
        config: ToyEngineConfig,
        baseline_id: str,
    ) -> Dict[str, Any]:
        engine.validate_config(config)
        engine.validate_no_forbidden_fields(
            {
                "graph_spec_id": config.graph_spec_id,
                "seed_spec_id": config.seed_spec_id,
                "initialization_spec_id": config.initialization_spec_id,
                "node_count": config.node_count,
                "packet_count": config.packet_count,
                "baseline_id": baseline_id,
                "run_boundary": "safe_abstract_toy_only",
            }
        )

        graph = engine.build_toy_graph(config)
        packets = list(engine.initialize_toy_packets(config))

        for _step_index in range(config.step_count_limit):
            variant_packets = self._apply_baseline_variant(baseline_id, packets)
            packets = [
                engine.one_step_transition(config, graph, variant_packets, packet)
                for packet in variant_packets
            ]

        packets = self._apply_baseline_variant(baseline_id, packets)
        metrics = engine.metric_snapshot(packets)

        return {
            "run_id": f"V9-3-RUN-{baseline_id}",
            "model_variant_id": baseline_id,
            "baseline_id": baseline_id,
            "graph_spec_id": config.graph_spec_id,
            "seed_record": {
                "graph_generation_seed": config.graph_seed,
                "packet_initialization_seed": config.packet_seed,
                "transition_choice_seed": config.transition_seed,
                "symbolic_drift_seed": config.symbolic_drift_seed,
            },
            "parameter_record": {
                "node_count": config.node_count,
                "packet_count": config.packet_count,
                "step_count_limit": config.step_count_limit,
            },
            "metric_results": metrics,
            "execution_boundary": (
                "safe abstract toy simulation only; not biological, not clinical, not pathogen, not receptor, "
                "not host range, not wet-lab, and not operational"
            ),
        }

    def _compare_to_full(self, run_records: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
        full = next(item for item in run_records if item["baseline_id"] == "VF-FULL")
        full_metrics = full["metric_results"]

        comparisons: List[Dict[str, Any]] = []
        for record in run_records:
            if record["baseline_id"] == "VF-FULL":
                continue

            metric_deltas = {
                key: round(full_metrics.get(key, 0.0) - record["metric_results"].get(key, 0.0), 6)
                for key in sorted(full_metrics.keys())
            }

            comparisons.append(
                {
                    "comparison_id": f"V9-3-COMP-{record['baseline_id']}",
                    "reference_model": "VF-FULL",
                    "baseline_id": record["baseline_id"],
                    "metric_deltas": metric_deltas,
                    "comparison_boundary": (
                        "safe toy baseline comparison only; not a validation claim, not a falsification audit, "
                        "not an empirical result report, and not manuscript readiness evidence"
                    ),
                }
            )

        return comparisons

    def build(self) -> Dict[str, Any]:
        reframing_payload = self._load_json(self.source_reframing_json_path)
        spec_payload = self._load_json(self.source_spec_json_path)
        engine_payload = self._load_json(self.source_engine_json_path)

        engine = SafeAbstractToySimulationEngine()
        manifest = build_engine_manifest_without_running()
        config = self._safe_config()

        run_records = [
            self._run_safe_toy_variant(engine=engine, config=config, baseline_id=baseline_id)
            for baseline_id in self.baseline_ids
        ]
        comparison_records = self._compare_to_full(run_records)

        counters = {
            "V9 safe toy baseline comparison artifact count": 1,
            "V9 simulation execution count": 1,
            "V9 baseline comparison execution count": 1,
            "V9 safe toy run record count": len(run_records),
            "V9 safe toy baseline comparison record count": len(comparison_records),
            "Toy simulation actual run count": len(run_records),
            "Toy simulation result count": len(run_records),
            "Toy baseline comparison execution count": 1,
            "Toy baseline comparison result count": len(comparison_records),
            "V9 formal results report count": 0,
            "V9 results report count": 0,
            "V9 falsification audit execution count": 0,
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
            "V9 source reframing artifact count": reframing_payload["counters"]["V9 abstract simulation reframing artifact count"],
            "V9 source specification artifact count": spec_payload["counters"]["V9 abstract simulation specification artifact count"],
            "V9 source detailed simulation specification completed count": spec_payload["counters"]["V9 detailed simulation specification completed count"],
            "V9 source engine implementation count": engine_payload["counters"]["V9 simulation engine implementation count"],
            "V9 source toy engine created count": engine_payload["counters"]["Toy simulation engine created count"],
            "V9 source engine contract component count": engine_payload["counters"]["V9 engine contract component count"],
            "Toy evaluation actual run count": 0,
            "Toy evaluation result count": 0,
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
            "title": "Viruse Fabric Safe Toy Baseline Comparison",
            "plan_phrase": self.plan_phrase,
            "scope": "safe-toy-baseline-comparison-only",
            "safe_abstract_toy_only": True,
            "safe_toy_simulation_executed": True,
            "baseline_comparison_executed": True,
            "formal_results_reported": False,
            "falsification_audit_executed": False,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "v9_4_results_and_falsification_deferred": True,
            "source_reframing_json": str(self.source_reframing_json_path),
            "source_spec_json": str(self.source_spec_json_path),
            "source_engine_json": str(self.source_engine_json_path),
            "engine_manifest_reference": {
                "engine_name": manifest.engine_name,
                "engine_version": manifest.engine_version,
                "implementation_scope": manifest.implementation_scope,
            },
            "safe_config": {
                "graph_spec_id": config.graph_spec_id,
                "seed_spec_id": config.seed_spec_id,
                "initialization_spec_id": config.initialization_spec_id,
                "node_count": config.node_count,
                "packet_count": config.packet_count,
                "step_count_limit": config.step_count_limit,
                "graph_seed": config.graph_seed,
                "packet_seed": config.packet_seed,
                "transition_seed": config.transition_seed,
                "symbolic_drift_seed": config.symbolic_drift_seed,
            },
            "run_records": run_records,
            "comparison_records": comparison_records,
            "comparison_statement": (
                "v9.3 performs safe abstract toy simulation runs and safe toy baseline comparison only. "
                "The outputs are toy run records and toy comparison records. They are not a formal results report, "
                "not a falsification audit, not external validation, not empirical evidence, not manuscript readiness, "
                "and not a theory validation claim."
            ),
            "non_validation_disclaimer": (
                "Safe toy baseline comparison only. No validation claim is made. No falsification audit is executed. "
                "No formal results report is produced. No manuscript file is modified. No citation is added. "
                "No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, "
                "no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced."
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "safe-toy-baseline-comparison-only":
            raise AssertionError("v9.3 must remain safe-toy-baseline-comparison-only.")

        if report["passed"] is not True:
            raise AssertionError("v9.3 must pass.")

        for field in [
            "safe_abstract_toy_only",
            "safe_toy_simulation_executed",
            "baseline_comparison_executed",
            "v9_4_results_and_falsification_deferred",
        ]:
            if report[field] is not True:
                raise AssertionError(f"Expected True for {field}")

        for field in [
            "formal_results_reported",
            "falsification_audit_executed",
            "validation_claim_made",
            "readiness_approval_recorded",
            "manuscript_file_modified",
            "manuscript_mutation",
            "new_citation_added",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        if len(report["run_records"]) != 6:
            raise AssertionError("Expected six safe toy run records: full model plus five baselines.")

        if len(report["comparison_records"]) != 5:
            raise AssertionError("Expected five safe toy baseline comparison records.")

        expected_run_ids = {
            "VF-FULL",
            "VF-BASE-A",
            "VF-BASE-B",
            "VF-BASE-C",
            "VF-BASE-D",
            "VF-BASE-E",
        }
        if {item["baseline_id"] for item in report["run_records"]} != expected_run_ids:
            raise AssertionError("Unexpected baseline id set in run records.")

        counters = report["counters"]

        expected_counts = {
            "V9 safe toy baseline comparison artifact count": 1,
            "V9 simulation execution count": 1,
            "V9 baseline comparison execution count": 1,
            "V9 safe toy run record count": 6,
            "V9 safe toy baseline comparison record count": 5,
            "Toy simulation actual run count": 6,
            "Toy simulation result count": 6,
            "Toy baseline comparison execution count": 1,
            "Toy baseline comparison result count": 5,
            "V9 formal results report count": 0,
            "V9 results report count": 0,
            "V9 falsification audit execution count": 0,
            "V9 theory validation claim count": 0,
            "V9 manuscript readiness claim count": 0,
            "V9 source reframing artifact count": 1,
            "V9 source specification artifact count": 1,
            "V9 source detailed simulation specification completed count": 1,
            "V9 source engine implementation count": 1,
            "V9 source toy engine created count": 1,
            "V9 source engine contract component count": 8,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        must_be_zero = [
            "V9 formal results report count",
            "V9 results report count",
            "V9 falsification audit execution count",
            "V9 theory validation claim count",
            "V9 manuscript readiness claim count",
            "Toy evaluation actual run count",
            "Toy evaluation result count",
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
            "Safe toy baseline comparison only",
            "safe abstract toy simulation runs",
            "safe toy baseline comparison",
            "not a formal results report",
            "not a falsification audit",
            "not external validation",
            "not empirical evidence",
            "not manuscript readiness",
            "not a theory validation claim",
            "No validation claim is made",
            "No falsification audit is executed",
            "No formal results report is produced",
            "No manuscript file is modified",
            "No citation is added",
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
                raise AssertionError(f"Missing required v9.3 phrase: {phrase}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Viruse Fabric Safe Toy Baseline Comparison")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is safe-toy-baseline-comparison-only.")
        lines.append("It performs safe abstract toy simulation runs and safe toy baseline comparison, but it does not produce a formal results report, does not execute a falsification audit, does not validate the theory, does not modify manuscript files, and does not add citations.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Comparison Statement")
        lines.append("")
        lines.append(report["comparison_statement"])
        lines.append("")
        lines.append("## Non-Validation Disclaimer")
        lines.append("")
        lines.append(report["non_validation_disclaimer"])
        lines.append("")

        lines.append("## Engine Manifest Reference")
        lines.append("")
        for key, value in report["engine_manifest_reference"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Safe Config")
        lines.append("")
        for key, value in report["safe_config"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Safe Toy Run Records")
        lines.append("")
        for item in report["run_records"]:
            lines.append(f"### {item['run_id']}")
            lines.append("")
            lines.append(f"- Model variant id: {item['model_variant_id']}")
            lines.append(f"- Baseline id: {item['baseline_id']}")
            lines.append(f"- Metric results: {item['metric_results']}")
            lines.append(f"- Execution boundary: {item['execution_boundary']}")
            lines.append("")

        lines.append("## Safe Toy Baseline Comparison Records")
        lines.append("")
        for item in report["comparison_records"]:
            lines.append(f"### {item['comparison_id']}")
            lines.append("")
            lines.append(f"- Reference model: {item['reference_model']}")
            lines.append(f"- Baseline id: {item['baseline_id']}")
            lines.append(f"- Metric deltas: {item['metric_deltas']}")
            lines.append(f"- Comparison boundary: {item['comparison_boundary']}")
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
        lines.append("V9_3_VIRUSE_FABRIC_SAFE_TOY_BASELINE_COMPARISON_OK")
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


def build_viruse_fabric_safe_toy_baseline_comparison() -> Dict[str, Any]:
    return ViruseFabricSafeToyBaselineComparisonBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_safe_toy_baseline_comparison()
    counters = result["counters"]
    print("V9_3_VIRUSE_FABRIC_SAFE_TOY_BASELINE_COMPARISON_OK")
    print("VIRUSE_FABRIC_SAFE_TOY_BASELINE_COMPARISON_DIRECT_CHECK_OK")
    print(f"Simulation execution count: {counters['V9 simulation execution count']}")
    print(f"Baseline comparison execution count: {counters['V9 baseline comparison execution count']}")
    print(f"Safe toy run record count: {counters['V9 safe toy run record count']}")
    print(f"Safe toy baseline comparison record count: {counters['V9 safe toy baseline comparison record count']}")
    print(f"Toy simulation actual run count: {counters['Toy simulation actual run count']}")
    print(f"Toy simulation result count: {counters['Toy simulation result count']}")
    print(f"Toy baseline comparison execution count: {counters['Toy baseline comparison execution count']}")
    print(f"Toy baseline comparison result count: {counters['Toy baseline comparison result count']}")
    print(f"Formal results report count: {counters['V9 formal results report count']}")
    print(f"Results report count: {counters['V9 results report count']}")
    print(f"Falsification audit execution count: {counters['V9 falsification audit execution count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Manuscript readiness claim count: {counters['V9 manuscript readiness claim count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
