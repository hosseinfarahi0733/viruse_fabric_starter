from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.viruse_fabric_safe_toy_baseline_comparison import (
    ViruseFabricSafeToyBaselineComparisonBuilder,
)


def main() -> None:
    builder = ViruseFabricSafeToyBaselineComparisonBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "safe-toy-baseline-comparison-only"
    assert report["plan_phrase"] == "v9_3_safe_toy_baseline_comparison_without_validation_or_falsification_audit"

    for field in [
        "safe_abstract_toy_only",
        "safe_toy_simulation_executed",
        "baseline_comparison_executed",
        "v9_4_results_and_falsification_deferred",
    ]:
        assert report[field] is True, f"Expected True for {field}"

    for field in [
        "formal_results_reported",
        "falsification_audit_executed",
        "validation_claim_made",
        "readiness_approval_recorded",
        "manuscript_file_modified",
        "manuscript_mutation",
        "new_citation_added",
    ]:
        assert report[field] is False, f"Expected False for {field}"

    assert report["engine_manifest_reference"]["engine_name"] == "SafeAbstractToySimulationEngine"
    assert report["engine_manifest_reference"]["engine_version"] == "v9.2"
    assert report["engine_manifest_reference"]["implementation_scope"] == "minimal-safe-toy-engine-implementation-only"

    assert report["safe_config"]["graph_spec_id"] == "VF-SPEC-GRAPH-001"
    assert report["safe_config"]["seed_spec_id"] == "VF-SPEC-SEED-001"
    assert report["safe_config"]["initialization_spec_id"] == "VF-SPEC-INIT-001"
    assert report["safe_config"]["node_count"] == 16
    assert report["safe_config"]["packet_count"] == 32
    assert report["safe_config"]["step_count_limit"] == 3

    assert len(report["run_records"]) == 6
    assert len(report["comparison_records"]) == 5

    expected_baselines = {
        "VF-FULL",
        "VF-BASE-A",
        "VF-BASE-B",
        "VF-BASE-C",
        "VF-BASE-D",
        "VF-BASE-E",
    }
    assert {item["baseline_id"] for item in report["run_records"]} == expected_baselines

    expected_comparison_baselines = {
        "VF-BASE-A",
        "VF-BASE-B",
        "VF-BASE-C",
        "VF-BASE-D",
        "VF-BASE-E",
    }
    assert {item["baseline_id"] for item in report["comparison_records"]} == expected_comparison_baselines

    for run_record in report["run_records"]:
        assert run_record["execution_boundary"].startswith("safe abstract toy simulation only")
        assert "metric_results" in run_record
        assert "survival_rate" in run_record["metric_results"]
        assert "constraint_violation_rate" in run_record["metric_results"]
        assert "symbolic_drift_rate" in run_record["metric_results"]
        assert "ledger_effect_size" in run_record["metric_results"]
        assert "seed_record" in run_record
        assert run_record["seed_record"]["graph_generation_seed"] == 101
        assert run_record["seed_record"]["packet_initialization_seed"] == 202
        assert run_record["seed_record"]["transition_choice_seed"] == 303
        assert run_record["seed_record"]["symbolic_drift_seed"] == 404

    for comparison_record in report["comparison_records"]:
        assert comparison_record["reference_model"] == "VF-FULL"
        assert comparison_record["comparison_boundary"].startswith("safe toy baseline comparison only")
        assert "not a validation claim" in comparison_record["comparison_boundary"]
        assert "not a falsification audit" in comparison_record["comparison_boundary"]
        assert "metric_deltas" in comparison_record
        assert "survival_rate" in comparison_record["metric_deltas"]
        assert "constraint_violation_rate" in comparison_record["metric_deltas"]
        assert "symbolic_drift_rate" in comparison_record["metric_deltas"]
        assert "ledger_effect_size" in comparison_record["metric_deltas"]

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
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

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
        assert counters[name] == 0, f"Expected zero counter for {name}, got {counters[name]}"

    combined_text = json.dumps(report, ensure_ascii=False)

    for phrase in [
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
    ]:
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

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
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
