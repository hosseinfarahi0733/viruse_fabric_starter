from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.simulation.viruse_fabric_minimal_safe_toy_simulation_engine import (
    SafeAbstractToySimulationEngine,
    ToyEngineConfig,
    build_engine_manifest_without_running,
)
from viruse_fabric.writing.viruse_fabric_minimal_safe_toy_simulation_engine import (
    ViruseFabricMinimalSafeToySimulationEngineBuilder,
)


def main() -> None:
    engine = SafeAbstractToySimulationEngine()
    manifest = build_engine_manifest_without_running()

    assert manifest.engine_name == "SafeAbstractToySimulationEngine"
    assert manifest.engine_version == "v9.2"
    assert manifest.implementation_scope == "minimal-safe-toy-engine-implementation-only"

    assert "safety_field_guard" in manifest.implemented_components
    assert "toy_config_validation" in manifest.implemented_components
    assert "toy_graph_builder_method" in manifest.implemented_components
    assert "toy_packet_initializer_method" in manifest.implemented_components
    assert "toy_score_update_methods" in manifest.implemented_components
    assert "toy_transition_step_method" in manifest.implemented_components
    assert "toy_metric_snapshot_method" in manifest.implemented_components
    assert "toy_output_schema_guard" in manifest.implemented_components

    assert "no_simulation_run_performed_in_v9_2" in manifest.explicitly_not_performed
    assert "no_baseline_comparison_executed_in_v9_2" in manifest.explicitly_not_performed
    assert "no_results_reported_in_v9_2" in manifest.explicitly_not_performed
    assert "no_falsification_audit_executed_in_v9_2" in manifest.explicitly_not_performed
    assert "no_validation_claim_made_in_v9_2" in manifest.explicitly_not_performed
    assert "no_manuscript_file_modified_in_v9_2" in manifest.explicitly_not_performed
    assert "no_citation_added_in_v9_2" in manifest.explicitly_not_performed

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

    try:
        engine.validate_no_forbidden_fields({"pathogen_name": "forbidden"})
        raise AssertionError("Forbidden field guard failed.")
    except ValueError as exc:
        assert "Forbidden non-toy fields detected" in str(exc)

    builder = ViruseFabricMinimalSafeToySimulationEngineBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "minimal-safe-toy-engine-implementation-only"
    assert report["plan_phrase"] == "v9_2_minimal_safe_toy_simulation_engine_without_execution_results_or_validation"

    for field in [
        "safe_abstract_toy_only",
        "engine_implemented",
        "engine_manifest_created_without_running",
        "engine_contract_declared",
        "engine_config_validation_checked_without_running",
        "v9_3_baseline_comparison_deferred",
        "v9_4_results_and_falsification_deferred",
    ]:
        assert report[field] is True, f"Expected True for {field}"

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
        assert report[field] is False, f"Expected False for {field}"

    assert len(report["engine_contract"]) == 8
    assert len(report["non_execution_controls"]) == 6
    assert report["forbidden_input_field_count"] >= 20

    expected_contract_ids = {
        "VF-ENG-CONTRACT-001",
        "VF-ENG-CONTRACT-002",
        "VF-ENG-CONTRACT-003",
        "VF-ENG-CONTRACT-004",
        "VF-ENG-CONTRACT-005",
        "VF-ENG-CONTRACT-006",
        "VF-ENG-CONTRACT-007",
        "VF-ENG-CONTRACT-008",
    }
    assert {item["contract_id"] for item in report["engine_contract"]} == expected_contract_ids

    expected_control_ids = {
        "VF-ENG-NO-RUN-001",
        "VF-ENG-NO-RUN-002",
        "VF-ENG-NO-RUN-003",
        "VF-ENG-NO-RUN-004",
        "VF-ENG-NO-RUN-005",
        "VF-ENG-NO-RUN-006",
    }
    assert {item["control_id"] for item in report["non_execution_controls"]} == expected_control_ids

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
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

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
        assert counters[name] == 0, f"Expected zero counter for {name}, got {counters[name]}"

    combined_text = json.dumps(report, ensure_ascii=False)

    for phrase in [
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
    ]:
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

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
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
