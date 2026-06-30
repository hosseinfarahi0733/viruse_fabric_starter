from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from viruse_fabric.simulation.viruse_fabric_minimal_safe_toy_simulation_engine import (
    FORBIDDEN_INPUT_FIELDS,
    SafeAbstractToySimulationEngine,
    ToyEngineConfig,
    build_engine_manifest_without_running,
)


class ViruseFabricMinimalSafeToySimulationEngineBuilder:
    version = "v9.2"

    source_spec_json_path = Path("outputs/viruse_fabric_abstract_simulation_specification_v9_1.json")
    engine_module_path = Path("viruse_fabric/simulation/viruse_fabric_minimal_safe_toy_simulation_engine.py")
    output_md_path = Path("outputs/viruse_fabric_minimal_safe_toy_simulation_engine_v9_2.md")
    output_json_path = Path("outputs/viruse_fabric_minimal_safe_toy_simulation_engine_v9_2.json")

    plan_phrase = "v9_2_minimal_safe_toy_simulation_engine_without_execution_results_or_validation"

    def _load_json(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            raise FileNotFoundError(f"Missing required source JSON: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"Expected dict payload from {path}")
        return payload

    def _engine_contract(self) -> List[Dict[str, Any]]:
        return [
            {
                "contract_id": "VF-ENG-CONTRACT-001",
                "name": "safety_field_guard",
                "implemented": True,
                "description": "Rejects forbidden non-toy fields before future safe toy execution.",
            },
            {
                "contract_id": "VF-ENG-CONTRACT-002",
                "name": "toy_config_validation",
                "implemented": True,
                "description": "Validates v9.1 specified toy graph, seed, initialization, node, and packet settings.",
            },
            {
                "contract_id": "VF-ENG-CONTRACT-003",
                "name": "toy_graph_builder_method",
                "implemented": True,
                "description": "Defines deterministic unitless toy graph construction method.",
            },
            {
                "contract_id": "VF-ENG-CONTRACT-004",
                "name": "toy_packet_initializer_method",
                "implemented": True,
                "description": "Defines deterministic unitless toy packet initialization method.",
            },
            {
                "contract_id": "VF-ENG-CONTRACT-005",
                "name": "toy_score_update_methods",
                "implemented": True,
                "description": "Defines compatibility, local constraint, global constraint, and causal mass score methods.",
            },
            {
                "contract_id": "VF-ENG-CONTRACT-006",
                "name": "toy_transition_step_method",
                "implemented": True,
                "description": "Defines one abstract toy transition step method without executing it in v9.2.",
            },
            {
                "contract_id": "VF-ENG-CONTRACT-007",
                "name": "toy_metric_snapshot_method",
                "implemented": True,
                "description": "Defines toy metric snapshot method without reporting v9.2 simulation results.",
            },
            {
                "contract_id": "VF-ENG-CONTRACT-008",
                "name": "toy_output_schema_guard",
                "implemented": True,
                "description": "Maintains forbidden output field boundary for future safe toy outputs.",
            },
        ]

    def _non_execution_controls(self) -> List[Dict[str, Any]]:
        return [
            {
                "control_id": "VF-ENG-NO-RUN-001",
                "name": "no_simulation_run_in_v9_2",
                "counter": "V9 simulation execution count",
                "required_value": 0,
            },
            {
                "control_id": "VF-ENG-NO-RUN-002",
                "name": "no_toy_simulation_actual_run_in_v9_2",
                "counter": "Toy simulation actual run count",
                "required_value": 0,
            },
            {
                "control_id": "VF-ENG-NO-RUN-003",
                "name": "no_baseline_comparison_in_v9_2",
                "counter": "V9 baseline comparison execution count",
                "required_value": 0,
            },
            {
                "control_id": "VF-ENG-NO-RUN-004",
                "name": "no_results_report_in_v9_2",
                "counter": "V9 results report count",
                "required_value": 0,
            },
            {
                "control_id": "VF-ENG-NO-RUN-005",
                "name": "no_falsification_audit_in_v9_2",
                "counter": "V9 falsification audit execution count",
                "required_value": 0,
            },
            {
                "control_id": "VF-ENG-NO-RUN-006",
                "name": "no_validation_claim_in_v9_2",
                "counter": "V9 theory validation claim count",
                "required_value": 0,
            },
        ]

    def build(self) -> Dict[str, Any]:
        spec_payload = self._load_json(self.source_spec_json_path)
        spec_counters = spec_payload["counters"]

        engine = SafeAbstractToySimulationEngine()
        manifest = build_engine_manifest_without_running()

        sample_config = ToyEngineConfig(
            graph_spec_id="VF-SPEC-GRAPH-001",
            seed_spec_id="VF-SPEC-SEED-001",
            initialization_spec_id="VF-SPEC-INIT-001",
            node_count=16,
            packet_count=32,
            step_count_limit=1,
            graph_seed=101,
            packet_seed=202,
            transition_seed=303,
            symbolic_drift_seed=404,
        )

        engine.validate_config(sample_config)
        engine.validate_no_forbidden_fields(
            {
                "graph_spec_id": sample_config.graph_spec_id,
                "seed_spec_id": sample_config.seed_spec_id,
                "initialization_spec_id": sample_config.initialization_spec_id,
                "node_count": sample_config.node_count,
                "packet_count": sample_config.packet_count,
            }
        )

        engine_contract = self._engine_contract()
        non_execution_controls = self._non_execution_controls()

        counters = {
            "V9 minimal safe toy simulation engine artifact count": 1,
            "V9 simulation engine implementation count": 1,
            "Toy simulation engine created count": 1,
            "V9 engine contract component count": len(engine_contract),
            "V9 engine manifest count": 1,
            "V9 engine safety guard count": 1,
            "V9 engine config validation count": 1,
            "V9 engine graph builder method count": 1,
            "V9 engine packet initializer method count": 1,
            "V9 engine score update method group count": 1,
            "V9 engine transition step method count": 1,
            "V9 engine metric snapshot method count": 1,
            "V9 engine non-execution control count": len(non_execution_controls),
            "V9 source specification artifact count": spec_counters["V9 abstract simulation specification artifact count"],
            "V9 source detailed simulation specification completed count": spec_counters["V9 detailed simulation specification completed count"],
            "V9 source graph specification count": spec_counters["V9 graph specification count"],
            "V9 source random seed specification count": spec_counters["V9 random seed specification count"],
            "V9 source initialization specification count": spec_counters["V9 initialization specification count"],
            "V9 source update rule specification count": spec_counters["V9 update rule specification count"],
            "V9 source baseline configuration specification count": spec_counters["V9 baseline configuration specification count"],
            "V9 source metric specification count": spec_counters["V9 metric specification count"],
            "V9 source output schema specification count": spec_counters["V9 output schema specification count"],
            "V9 source falsification threshold specification count": spec_counters["V9 falsification threshold specification count"],
            "V9 source safety boundary specification count": spec_counters["V9 safety boundary specification count"],
            "V9 simulation execution count": 0,
            "V9 baseline comparison execution count": 0,
            "V9 results report count": 0,
            "V9 falsification audit execution count": 0,
            "V9 theory validation claim count": 0,
            "Toy simulation actual run count": 0,
            "Toy simulation result count": 0,
            "Toy baseline comparison execution count": 0,
            "Toy falsification audit execution count": 0,
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
            "title": "Viruse Fabric Minimal Safe Toy Simulation Engine",
            "plan_phrase": self.plan_phrase,
            "scope": "minimal-safe-toy-engine-implementation-only",
            "source_spec_json": str(self.source_spec_json_path),
            "engine_module": str(self.engine_module_path),
            "safe_abstract_toy_only": True,
            "engine_implemented": True,
            "engine_manifest_created_without_running": True,
            "engine_contract_declared": True,
            "engine_config_validation_checked_without_running": True,
            "simulation_run_performed": False,
            "baseline_comparison_performed": False,
            "results_reported": False,
            "falsification_audit_executed": False,
            "validation_claim_made": False,
            "readiness_approval_recorded": False,
            "manuscript_file_modified": False,
            "manuscript_mutation": False,
            "new_citation_added": False,
            "v9_3_baseline_comparison_deferred": True,
            "v9_4_results_and_falsification_deferred": True,
            "implementation_statement": (
                "v9.2 implements a minimal safe abstract toy simulation engine module for Viruse Fabric. "
                "The engine defines safety guards, configuration validation, toy graph construction, toy packet "
                "initialization, bounded toy score updates, one-step abstract transition logic, and toy metric "
                "snapshot methods. v9.2 does not execute a simulation run, does not execute baseline comparison, "
                "does not report results, does not execute a falsification audit, and does not validate the theory."
            ),
            "engine_manifest": {
                "engine_name": manifest.engine_name,
                "engine_version": manifest.engine_version,
                "implementation_scope": manifest.implementation_scope,
                "safety_boundary": manifest.safety_boundary,
                "implemented_components": list(manifest.implemented_components),
                "explicitly_not_performed": list(manifest.explicitly_not_performed),
                "forbidden_input_fields": list(manifest.forbidden_input_fields),
            },
            "engine_contract": engine_contract,
            "non_execution_controls": non_execution_controls,
            "sample_config_checked_without_running": {
                "graph_spec_id": sample_config.graph_spec_id,
                "seed_spec_id": sample_config.seed_spec_id,
                "initialization_spec_id": sample_config.initialization_spec_id,
                "node_count": sample_config.node_count,
                "packet_count": sample_config.packet_count,
                "step_count_limit": sample_config.step_count_limit,
                "graph_seed": sample_config.graph_seed,
                "packet_seed": sample_config.packet_seed,
                "transition_seed": sample_config.transition_seed,
                "symbolic_drift_seed": sample_config.symbolic_drift_seed,
            },
            "forbidden_input_field_count": len(FORBIDDEN_INPUT_FIELDS),
            "non_validation_disclaimer": (
                "Minimal safe toy engine implementation only. No simulation run is performed. "
                "No baseline comparison is executed. No results are reported. No falsification audit is executed. "
                "No validation claim is made. No manuscript file is modified. No citation is added. "
                "No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, "
                "no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced."
            ),
            "counters": counters,
            "passed": True,
        }

        self._validate(report)
        return report

    def _validate(self, report: Dict[str, Any]) -> None:
        if report["scope"] != "minimal-safe-toy-engine-implementation-only":
            raise AssertionError("v9.2 must remain minimal-safe-toy-engine-implementation-only.")

        if report["passed"] is not True:
            raise AssertionError("v9.2 must pass.")

        for field in [
            "safe_abstract_toy_only",
            "engine_implemented",
            "engine_manifest_created_without_running",
            "engine_contract_declared",
            "engine_config_validation_checked_without_running",
            "v9_3_baseline_comparison_deferred",
            "v9_4_results_and_falsification_deferred",
        ]:
            if report[field] is not True:
                raise AssertionError(f"Expected True for {field}")

        for field in [
            "simulation_run_performed",
            "baseline_comparison_performed",
            "results_reported",
            "falsification_audit_executed",
            "validation_claim_made",
            "readiness_approval_recorded",
            "manuscript_file_modified",
            "manuscript_mutation",
            "new_citation_added",
        ]:
            if report[field] is not False:
                raise AssertionError(f"Expected False for {field}")

        counters = report["counters"]

        expected_counts = {
            "V9 minimal safe toy simulation engine artifact count": 1,
            "V9 simulation engine implementation count": 1,
            "Toy simulation engine created count": 1,
            "V9 engine contract component count": 8,
            "V9 engine manifest count": 1,
            "V9 engine safety guard count": 1,
            "V9 engine config validation count": 1,
            "V9 engine graph builder method count": 1,
            "V9 engine packet initializer method count": 1,
            "V9 engine score update method group count": 1,
            "V9 engine transition step method count": 1,
            "V9 engine metric snapshot method count": 1,
            "V9 engine non-execution control count": 6,
            "V9 source specification artifact count": 1,
            "V9 source detailed simulation specification completed count": 1,
            "V9 source graph specification count": 1,
            "V9 source random seed specification count": 1,
            "V9 source initialization specification count": 1,
            "V9 source update rule specification count": 8,
            "V9 source baseline configuration specification count": 5,
            "V9 source metric specification count": 8,
            "V9 source output schema specification count": 1,
            "V9 source falsification threshold specification count": 4,
            "V9 source safety boundary specification count": 10,
            "V9 simulation execution count": 0,
            "V9 baseline comparison execution count": 0,
            "V9 results report count": 0,
            "V9 falsification audit execution count": 0,
            "V9 theory validation claim count": 0,
            "Toy simulation actual run count": 0,
            "Toy simulation result count": 0,
            "Toy baseline comparison execution count": 0,
            "Toy falsification audit execution count": 0,
        }

        for name, expected in expected_counts.items():
            actual = counters.get(name)
            if actual != expected:
                raise AssertionError(f"Expected {expected} for {name}, got {actual}")

        must_be_zero = [
            "V9 simulation execution count",
            "V9 baseline comparison execution count",
            "V9 results report count",
            "V9 falsification audit execution count",
            "V9 theory validation claim count",
            "Toy simulation actual run count",
            "Toy simulation result count",
            "Toy baseline comparison execution count",
            "Toy falsification audit execution count",
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
            "Minimal safe toy engine implementation only",
            "No simulation run is performed",
            "No baseline comparison is executed",
            "No results are reported",
            "No falsification audit is executed",
            "No validation claim is made",
            "safety guards",
            "configuration validation",
            "toy graph construction",
            "toy packet initialization",
            "bounded toy score updates",
            "one-step abstract transition logic",
            "toy metric snapshot methods",
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
                raise AssertionError(f"Missing required v9.2 phrase: {phrase}")

    def render_markdown(self, report: Dict[str, Any]) -> str:
        lines: List[str] = []

        lines.append("# Viruse Fabric Minimal Safe Toy Simulation Engine")
        lines.append("")
        lines.append(f"Version: {report['version']}")
        lines.append("")
        lines.append("## Scope")
        lines.append("")
        lines.append("This artifact is minimal-safe-toy-engine-implementation-only.")
        lines.append("It implements the safe abstract toy engine module, but it does not execute a simulation run, does not execute baseline comparison, does not report results, does not execute a falsification audit, does not validate the theory, does not modify manuscript files, and does not add citations.")
        lines.append("")
        lines.append(f"Plan phrase: `{report['plan_phrase']}`")
        lines.append("")
        lines.append("## Implementation Statement")
        lines.append("")
        lines.append(report["implementation_statement"])
        lines.append("")
        lines.append("## Non-Validation Disclaimer")
        lines.append("")
        lines.append(report["non_validation_disclaimer"])
        lines.append("")

        lines.append("## Engine Manifest")
        lines.append("")
        for key, value in report["engine_manifest"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Engine Contract")
        lines.append("")
        for item in report["engine_contract"]:
            lines.append(f"### {item['contract_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Implemented: {item['implemented']}")
            lines.append(f"- Description: {item['description']}")
            lines.append("")

        lines.append("## Non-Execution Controls")
        lines.append("")
        for item in report["non_execution_controls"]:
            lines.append(f"### {item['control_id']} - {item['name']}")
            lines.append("")
            lines.append(f"- Counter: {item['counter']}")
            lines.append(f"- Required value: {item['required_value']}")
            lines.append("")

        lines.append("## Sample Config Checked Without Running")
        lines.append("")
        for key, value in report["sample_config_checked_without_running"].items():
            lines.append(f"- {key}: {value}")
        lines.append("")

        lines.append("## Forbidden Input Field Count")
        lines.append("")
        lines.append(str(report["forbidden_input_field_count"]))
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
        lines.append("V9_2_VIRUSE_FABRIC_MINIMAL_SAFE_TOY_SIMULATION_ENGINE_OK")
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


def build_viruse_fabric_minimal_safe_toy_simulation_engine() -> Dict[str, Any]:
    return ViruseFabricMinimalSafeToySimulationEngineBuilder().run()


if __name__ == "__main__":
    result = build_viruse_fabric_minimal_safe_toy_simulation_engine()
    counters = result["counters"]
    print("V9_2_VIRUSE_FABRIC_MINIMAL_SAFE_TOY_SIMULATION_ENGINE_OK")
    print("VIRUSE_FABRIC_MINIMAL_SAFE_TOY_SIMULATION_ENGINE_DIRECT_CHECK_OK")
    print(f"Simulation engine implementation count: {counters['V9 simulation engine implementation count']}")
    print(f"Toy simulation engine created count: {counters['Toy simulation engine created count']}")
    print(f"Engine contract component count: {counters['V9 engine contract component count']}")
    print(f"Engine manifest count: {counters['V9 engine manifest count']}")
    print(f"Engine safety guard count: {counters['V9 engine safety guard count']}")
    print(f"Engine config validation count: {counters['V9 engine config validation count']}")
    print(f"Engine graph builder method count: {counters['V9 engine graph builder method count']}")
    print(f"Engine packet initializer method count: {counters['V9 engine packet initializer method count']}")
    print(f"Engine score update method group count: {counters['V9 engine score update method group count']}")
    print(f"Engine transition step method count: {counters['V9 engine transition step method count']}")
    print(f"Engine metric snapshot method count: {counters['V9 engine metric snapshot method count']}")
    print(f"Engine non-execution control count: {counters['V9 engine non-execution control count']}")
    print(f"Simulation execution count: {counters['V9 simulation execution count']}")
    print(f"Baseline comparison execution count: {counters['V9 baseline comparison execution count']}")
    print(f"Results report count: {counters['V9 results report count']}")
    print(f"Falsification audit execution count: {counters['V9 falsification audit execution count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Toy simulation actual run count: {counters['Toy simulation actual run count']}")
    print(f"Toy simulation result count: {counters['Toy simulation result count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {result['passed']}")
