from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.viruse_fabric_safe_toy_replicate_grid_and_signal_robustness_check import (
    ViruseFabricSafeToyReplicateGridAndSignalRobustnessCheckBuilder,
)


def main() -> None:
    builder = ViruseFabricSafeToyReplicateGridAndSignalRobustnessCheckBuilder()
    report = builder.run()

    counters = report["counters"]
    summary = report["robustness_summary"]

    assert report["passed"] is True
    assert report["scope"] == "safe-toy-replicate-grid-and-signal-robustness-check-only"
    assert report["plan_phrase"] == "v9_7_safe_toy_replicate_grid_and_signal_robustness_check_without_validation_or_readiness"

    assert report["safe_abstract_toy_only"] is True
    assert report["replicate_grid_executed"] is True
    assert report["signal_robustness_checked"] is True

    assert report["validation_claim_made"] is False
    assert report["readiness_approval_recorded"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["new_citation_added"] is False

    assert report["primary_hypothesis_under_test"] == "VF-H2"
    assert report["primary_signal_under_test"] == "ledger_effect_size"
    assert report["reduced_toy_core_under_test"] == "memory-ledger-driven toy dynamics"

    assert len(report["replicate_grid"]) == 6
    assert len(report["replicate_run_records"]) == 12
    assert len(report["robustness_records"]) == 6
    assert len(report["non_upgrade_records"]) == 3
    assert len(report["allowed_robustness_claims_register"]) == 3
    assert len(report["forbidden_robustness_claims_register"]) == 5

    assert summary["summary_id"] == "V9-7-MEMORY-LEDGER-ROBUSTNESS-SUMMARY-001"
    assert summary["hypothesis_id"] == "VF-H2"
    assert summary["signal_metric"] == "ledger_effect_size"
    assert summary["reference_variant"] == "VF-FULL"
    assert summary["ablation_variant"] == "VF-BASE-C"
    assert summary["replicate_count"] == 6

    assert summary["positive_signal_replicate_count"] + summary["zero_signal_replicate_count"] + summary["negative_signal_replicate_count"] == 6
    assert 0.0 <= summary["positive_signal_rate"] <= 1.0

    expected_verdicts = {
        "robust_in_this_safe_toy_replicate_grid",
        "partially_robust_in_this_safe_toy_replicate_grid",
        "not_robust_in_this_safe_toy_replicate_grid",
    }
    assert summary["robustness_verdict"] in expected_verdicts
    assert set(summary["robustness_verdict_options"]) == expected_verdicts

    for item in report["robustness_records"]:
        assert item["hypothesis_id"] == "VF-H2"
        assert item["reference_variant"] == "VF-FULL"
        assert item["ablation_variant"] == "VF-BASE-C"
        assert item["signal_metric"] == "ledger_effect_size"
        assert isinstance(item["positive_signal"], bool)
        assert "ledger_effect_size" in item["metric_deltas"]
        assert "Safe abstract toy replicate comparison only" in item["boundary"]

    assert {item["hypothesis_id"] for item in report["non_upgrade_records"]} == {"VF-H1", "VF-H3", "VF-H4"}
    assert all(item["status_after_v9_7"] == "not_upgraded" for item in report["non_upgrade_records"])

    expected_static_counts = {
        "V9 safe toy replicate robustness artifact count": 1,
        "V9 safe toy replicate grid execution count": 1,
        "V9 safe toy replicate grid config count": 6,
        "V9 safe toy replicate run record count": 12,
        "V9 VF-H2 robustness comparison record count": 6,
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
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    assert counters["V9 VF-H2 positive ledger signal replicate count"] == summary["positive_signal_replicate_count"]
    assert counters["V9 VF-H2 zero ledger signal replicate count"] == summary["zero_signal_replicate_count"]
    assert counters["V9 VF-H2 negative ledger signal replicate count"] == summary["negative_signal_replicate_count"]

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
        assert counters[name] == 0, f"Expected zero counter for {name}, got {counters[name]}"

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
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

    print("V9_7_VIRUSE_FABRIC_SAFE_TOY_REPLICATE_GRID_AND_SIGNAL_ROBUSTNESS_CHECK_OK")
    print("VIRUSE_FABRIC_SAFE_TOY_REPLICATE_GRID_AND_SIGNAL_ROBUSTNESS_CHECK_DIRECT_CHECK_OK")
    print(f"Primary hypothesis under test: {report['primary_hypothesis_under_test']}")
    print(f"Primary signal under test: {report['primary_signal_under_test']}")
    print(f"Reduced toy core under test: {report['reduced_toy_core_under_test']}")
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
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
