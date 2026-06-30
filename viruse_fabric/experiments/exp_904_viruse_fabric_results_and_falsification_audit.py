from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.viruse_fabric_results_and_falsification_audit import (
    ViruseFabricResultsAndFalsificationAuditBuilder,
)


def main() -> None:
    builder = ViruseFabricResultsAndFalsificationAuditBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "formal-toy-results-and-falsification-audit-only"
    assert report["plan_phrase"] == "v9_4_results_and_falsification_audit_without_validation_or_manuscript_readiness"

    for field in [
        "safe_abstract_toy_only",
        "formal_results_reported",
        "results_reported",
        "falsification_audit_executed",
        "toy_evaluation_executed",
    ]:
        assert report[field] is True, f"Expected True for {field}"

    for field in [
        "validation_claim_made",
        "readiness_approval_recorded",
        "manuscript_file_modified",
        "manuscript_mutation",
        "new_citation_added",
    ]:
        assert report[field] is False, f"Expected False for {field}"

    result_summary = report["result_summary"]
    falsification_audit = report["falsification_audit"]

    assert result_summary["summary_id"] == "V9-4-TOY-RESULT-SUMMARY-001"
    assert result_summary["scope"] == "formal-toy-results-report-only"
    assert result_summary["run_record_count"] == 6
    assert result_summary["comparison_record_count"] == 5
    assert len(result_summary["metric_table"]) == 6
    assert len(result_summary["comparison_table"]) == 5

    assert "strongest_safe_toy_divergence" in result_summary
    assert "weakest_safe_toy_divergence" in result_summary
    assert result_summary["strongest_safe_toy_divergence"]["absolute_delta_total"] >= result_summary["weakest_safe_toy_divergence"]["absolute_delta_total"]

    expected_metric_baselines = {
        "VF-FULL",
        "VF-BASE-A",
        "VF-BASE-B",
        "VF-BASE-C",
        "VF-BASE-D",
        "VF-BASE-E",
    }
    assert {item["baseline_id"] for item in result_summary["metric_table"]} == expected_metric_baselines

    expected_comparison_baselines = {
        "VF-BASE-A",
        "VF-BASE-B",
        "VF-BASE-C",
        "VF-BASE-D",
        "VF-BASE-E",
    }
    assert {item["baseline_id"] for item in result_summary["comparison_table"]} == expected_comparison_baselines

    for item in result_summary["metric_table"]:
        assert "metric_results" in item
        for metric in [
            "survival_rate",
            "constraint_violation_rate",
            "symbolic_drift_rate",
            "ledger_effect_size",
        ]:
            assert metric in item["metric_results"], metric
        assert item["execution_boundary"].startswith("safe abstract toy simulation only")

    for item in result_summary["comparison_table"]:
        assert item["reference_model"] == "VF-FULL"
        assert "metric_deltas" in item
        assert "absolute_delta_total" in item
        assert isinstance(item["absolute_delta_total"], float)
        assert item["comparison_boundary"].startswith("safe toy baseline comparison only")
        for metric in [
            "survival_rate",
            "constraint_violation_rate",
            "symbolic_drift_rate",
            "ledger_effect_size",
        ]:
            assert metric in item["metric_deltas"], metric

    assert falsification_audit["audit_summary_id"] == "V9-4-TOY-FALSIFICATION-AUDIT-001"
    assert falsification_audit["scope"] == "toy-falsification-audit-only"
    assert falsification_audit["audit_record_count"] == 4
    assert len(falsification_audit["audit_records"]) == 4
    assert "toy_audit_verdict_counts" in falsification_audit

    expected_hypotheses = {
        "VF-H1",
        "VF-H2",
        "VF-H3",
        "VF-H4",
    }
    assert {item["hypothesis_id"] for item in falsification_audit["audit_records"]} == expected_hypotheses

    expected_sensitive_baselines = {
        "VF-H1": "VF-BASE-B",
        "VF-H2": "VF-BASE-C",
        "VF-H3": "VF-BASE-E",
        "VF-H4": "VF-BASE-D",
    }

    for item in falsification_audit["audit_records"]:
        hypothesis_id = item["hypothesis_id"]
        assert item["expected_sensitive_baseline"] == expected_sensitive_baselines[hypothesis_id]
        assert item["comparison_id"].startswith("V9-3-COMP-")
        assert item["toy_audit_verdict"] in {
            "not_falsified_in_this_safe_toy_audit",
            "falsified_or_unresolved_in_this_safe_toy_audit",
        }
        assert isinstance(item["selected_delta_total"], float)
        assert "audit_reason" in item
        assert item["audit_boundary"].startswith("Toy falsification audit only")
        assert "not external validation" in item["audit_boundary"]
        assert "not empirical evidence" in item["audit_boundary"]
        assert "not manuscript readiness" in item["audit_boundary"]
        assert "not a theory validation claim" in item["audit_boundary"]

    expected_counts = {
        "V9 results and falsification audit artifact count": 1,
        "V9 formal results report count": 1,
        "V9 results report count": 1,
        "V9 falsification audit execution count": 1,
        "V9 toy result summary count": 1,
        "V9 toy falsification audit summary count": 1,
        "V9 toy falsification audit record count": 4,
        "V9 toy hypothesis audit count": 4,
        "Toy evaluation actual run count": 1,
        "Toy evaluation result count": 1,
        "Toy falsification audit execution count": 1,
        "Toy falsification audit result count": 4,
        "V9 source safe toy baseline comparison artifact count": 1,
        "V9 source simulation execution count": 1,
        "V9 source baseline comparison execution count": 1,
        "V9 source safe toy run record count": 6,
        "V9 source safe toy baseline comparison record count": 5,
        "V9 source engine implementation count": 1,
        "V9 source detailed simulation specification completed count": 1,
        "V9 source reframed hypothesis count": 4,
        "V9 theory validation claim count": 0,
        "V9 manuscript readiness claim count": 0,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "V9 theory validation claim count",
        "V9 manuscript readiness claim count",
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
        "Formal toy results report only",
        "toy falsification audit",
        "toy metric summaries",
        "toy baseline divergences",
        "not empirical evidence",
        "not external validation",
        "not independent validation",
        "not manuscript readiness",
        "not a theory validation claim",
        "No validation claim is made",
        "No manuscript readiness claim is made",
        "No external validation is performed",
        "No independent experiment is performed",
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

    print("V9_4_VIRUSE_FABRIC_RESULTS_AND_FALSIFICATION_AUDIT_OK")
    print("VIRUSE_FABRIC_RESULTS_AND_FALSIFICATION_AUDIT_DIRECT_CHECK_OK")
    print(f"Formal results report count: {counters['V9 formal results report count']}")
    print(f"Results report count: {counters['V9 results report count']}")
    print(f"Falsification audit execution count: {counters['V9 falsification audit execution count']}")
    print(f"Toy result summary count: {counters['V9 toy result summary count']}")
    print(f"Toy falsification audit summary count: {counters['V9 toy falsification audit summary count']}")
    print(f"Toy falsification audit record count: {counters['V9 toy falsification audit record count']}")
    print(f"Toy hypothesis audit count: {counters['V9 toy hypothesis audit count']}")
    print(f"Toy evaluation actual run count: {counters['Toy evaluation actual run count']}")
    print(f"Toy evaluation result count: {counters['Toy evaluation result count']}")
    print(f"Toy falsification audit execution count: {counters['Toy falsification audit execution count']}")
    print(f"Toy falsification audit result count: {counters['Toy falsification audit result count']}")
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
