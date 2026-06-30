from __future__ import annotations

import json

from viruse_fabric.writing.viruse_fabric_abstract_simulation_specification import (
    ViruseFabricAbstractSimulationSpecificationBuilder,
)


def main() -> None:
    builder = ViruseFabricAbstractSimulationSpecificationBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "abstract-simulation-specification-only"
    assert report["plan_phrase"] == "v9_1_abstract_simulation_specification_without_engine_execution_or_validation"

    for field in [
        "safe_abstract_toy_only",
        "formal_specification_only",
        "simulation_specification_completed",
        "v9_2_engine_deferred",
        "v9_3_baseline_comparison_deferred",
        "v9_4_results_and_falsification_deferred",
    ]:
        assert report[field] is True, f"Expected True for {field}"

    for field in [
        "simulation_engine_implemented",
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

    assert report["graph_specification"]["graph_spec_id"] == "VF-SPEC-GRAPH-001"
    assert report["random_seed_specification"]["seed_spec_id"] == "VF-SPEC-SEED-001"
    assert report["initialization_specification"]["initialization_spec_id"] == "VF-SPEC-INIT-001"

    assert len(report["update_rule_specification"]) == 8
    assert len(report["baseline_configuration"]) == 5
    assert len(report["metric_specification"]) == 8
    assert len(report["falsification_threshold_specification"]) == 4
    assert len(report["safety_boundary_specification"]) == 10

    expected_update_rules = {
        "VF-SPEC-RULE-001",
        "VF-SPEC-RULE-002",
        "VF-SPEC-RULE-003",
        "VF-SPEC-RULE-004",
        "VF-SPEC-RULE-005",
        "VF-SPEC-RULE-006",
        "VF-SPEC-RULE-007",
        "VF-SPEC-RULE-008",
    }
    assert {item["rule_id"] for item in report["update_rule_specification"]} == expected_update_rules

    expected_baselines = {
        "VF-BASE-A",
        "VF-BASE-B",
        "VF-BASE-C",
        "VF-BASE-D",
        "VF-BASE-E",
    }
    assert {item["baseline_id"] for item in report["baseline_configuration"]} == expected_baselines

    expected_metrics = {
        "VF-MET-001",
        "VF-MET-002",
        "VF-MET-003",
        "VF-MET-004",
        "VF-MET-005",
        "VF-MET-006",
        "VF-MET-007",
        "VF-MET-008",
    }
    assert {item["metric_id"] for item in report["metric_specification"]} == expected_metrics

    expected_thresholds = {
        "VF-THRESH-H1",
        "VF-THRESH-H2",
        "VF-THRESH-H3",
        "VF-THRESH-H4",
    }
    assert {item["threshold_id"] for item in report["falsification_threshold_specification"]} == expected_thresholds

    output_schema = report["output_schema_specification"]
    assert output_schema["schema_id"] == "VF-SPEC-OUTPUT-001"
    for required_field in [
        "run_id",
        "model_variant_id",
        "baseline_id",
        "graph_spec_id",
        "seed_record",
        "parameter_record",
        "metric_results",
        "safety_counters",
        "execution_boundary",
    ]:
        assert required_field in output_schema["required_top_level_fields"]

    for forbidden_field in [
        "real_biological_dataset",
        "pathogen_name",
        "host_species",
        "receptor_name",
        "binding_affinity",
        "infectivity_score",
        "immune_evasion_score",
        "host_range_prediction",
        "wet_lab_protocol",
    ]:
        assert forbidden_field in output_schema["forbidden_output_fields"]

    expected_counts = {
        "V9 abstract simulation specification artifact count": 1,
        "V9 detailed simulation specification completed count": 1,
        "V9 graph specification count": 1,
        "V9 random seed specification count": 1,
        "V9 initialization specification count": 1,
        "V9 update rule specification count": 8,
        "V9 baseline configuration specification count": 5,
        "V9 metric specification count": 8,
        "V9 output schema specification count": 1,
        "V9 falsification threshold specification count": 4,
        "V9 safety boundary specification count": 10,
        "V9 source reframing artifact count": 1,
        "V9 source model object definition count": 8,
        "V9 source state variable definition count": 12,
        "V9 source reframed hypothesis count": 4,
        "V9 source baseline plan count": 5,
        "V9 source metric proposal count": 8,
        "V9 source falsification rule count": 6,
        "V9 simulation engine implementation count": 0,
        "V9 simulation execution count": 0,
        "V9 baseline comparison execution count": 0,
        "V9 results report count": 0,
        "V9 falsification audit execution count": 0,
        "V9 theory validation claim count": 0,
        "Toy simulation engine created count": 0,
        "Toy simulation actual run count": 0,
        "Toy simulation result count": 0,
        "Toy baseline comparison execution count": 0,
        "Toy falsification audit execution count": 0,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "V9 simulation engine implementation count",
        "V9 simulation execution count",
        "V9 baseline comparison execution count",
        "V9 results report count",
        "V9 falsification audit execution count",
        "V9 theory validation claim count",
        "Toy simulation engine created count",
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
        "Abstract simulation specification only",
        "No simulation engine is implemented",
        "No simulation run is performed",
        "No baseline comparison is executed",
        "No results are reported",
        "No falsification audit is executed",
        "No validation claim is made",
        "graph generation",
        "random seed control",
        "initialization",
        "update rules",
        "baseline configurations",
        "metrics",
        "output schema",
        "falsification thresholds",
        "safety boundaries",
        "No manuscript file is modified",
        "No citation is added",
        "No real biological datasets",
        "no real pathogen models",
        "no receptor parameters",
        "no operational targeting",
    ]:
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

    print("V9_1_VIRUSE_FABRIC_ABSTRACT_SIMULATION_SPECIFICATION_OK")
    print("VIRUSE_FABRIC_ABSTRACT_SIMULATION_SPECIFICATION_DIRECT_CHECK_OK")
    print(f"Graph specification count: {counters['V9 graph specification count']}")
    print(f"Random seed specification count: {counters['V9 random seed specification count']}")
    print(f"Initialization specification count: {counters['V9 initialization specification count']}")
    print(f"Update rule specification count: {counters['V9 update rule specification count']}")
    print(f"Baseline configuration specification count: {counters['V9 baseline configuration specification count']}")
    print(f"Metric specification count: {counters['V9 metric specification count']}")
    print(f"Output schema specification count: {counters['V9 output schema specification count']}")
    print(f"Falsification threshold specification count: {counters['V9 falsification threshold specification count']}")
    print(f"Safety boundary specification count: {counters['V9 safety boundary specification count']}")
    print(f"Simulation engine implementation count: {counters['V9 simulation engine implementation count']}")
    print(f"Simulation execution count: {counters['V9 simulation execution count']}")
    print(f"Baseline comparison execution count: {counters['V9 baseline comparison execution count']}")
    print(f"Results report count: {counters['V9 results report count']}")
    print(f"Falsification audit execution count: {counters['V9 falsification audit execution count']}")
    print(f"Theory validation claim count: {counters['V9 theory validation claim count']}")
    print(f"Toy simulation actual run count: {counters['Toy simulation actual run count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
