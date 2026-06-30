from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.viruse_fabric_toy_evidence_limitation_and_manuscript_readiness_gate import (
    ViruseFabricToyEvidenceLimitationAndManuscriptReadinessGateBuilder,
)


def main() -> None:
    builder = ViruseFabricToyEvidenceLimitationAndManuscriptReadinessGateBuilder()
    report = builder.run()
    counters = report["counters"]
    gate = report["readiness_gate"]
    toy_summary = report["toy_evidence_summary"]
    limitations = report["limitation_register"]

    assert report["passed"] is True
    assert report["scope"] == "toy-evidence-limitation-and-manuscript-readiness-gate-only"
    assert report["plan_phrase"] == "v9_5_toy_evidence_limitation_and_manuscript_readiness_gate_without_submission_approval"

    for field in [
        "safe_abstract_toy_only",
        "toy_evidence_limitation_analysis_performed",
        "manuscript_readiness_gate_executed",
        "manuscript_readiness_denied",
    ]:
        assert report[field] is True, f"Expected True for {field}"

    for field in [
        "manuscript_readiness_approved",
        "submission_ready",
        "validation_claim_made",
        "readiness_approval_recorded",
        "manuscript_file_modified",
        "manuscript_mutation",
        "new_citation_added",
    ]:
        assert report[field] is False, f"Expected False for {field}"

    assert toy_summary["summary_id"] == "V9-5-TOY-EVIDENCE-SUMMARY-001"
    assert toy_summary["safe_abstract_toy_only"] is True
    assert toy_summary["reframed_hypothesis_count"] == 4
    assert toy_summary["detailed_specification_completed_count"] == 1
    assert toy_summary["engine_implementation_count"] == 1
    assert toy_summary["safe_toy_simulation_execution_count"] == 1
    assert toy_summary["safe_toy_baseline_comparison_execution_count"] == 1
    assert toy_summary["safe_toy_run_record_count"] == 6
    assert toy_summary["safe_toy_baseline_comparison_record_count"] == 5
    assert toy_summary["formal_toy_results_report_count"] == 1
    assert toy_summary["toy_falsification_audit_execution_count"] == 1
    assert toy_summary["toy_falsification_audit_record_count"] == 4
    assert "not empirical evidence" in toy_summary["evidence_boundary"]
    assert "not external validation" in toy_summary["evidence_boundary"]
    assert "not independent validation" in toy_summary["evidence_boundary"]
    assert "not a theory validation claim" in toy_summary["evidence_boundary"]
    assert "not manuscript readiness" in toy_summary["evidence_boundary"]
    assert "not submission readiness" in toy_summary["evidence_boundary"]

    assert len(limitations) == 8
    assert all(item["blocking"] is True for item in limitations)

    expected_limitations = {
        "V9-5-LIMIT-001",
        "V9-5-LIMIT-002",
        "V9-5-LIMIT-003",
        "V9-5-LIMIT-004",
        "V9-5-LIMIT-005",
        "V9-5-LIMIT-006",
        "V9-5-LIMIT-007",
        "V9-5-LIMIT-008",
    }
    assert {item["limitation_id"] for item in limitations} == expected_limitations

    assert gate["gate_id"] == "V9-5-MANUSCRIPT-READINESS-GATE-001"
    assert gate["gate_scope"] == "toy-evidence-limitation-and-readiness-denial-only"
    assert gate["gate_decision"] == "not_ready_for_manuscript_submission"
    assert gate["approval_recorded"] is False
    assert gate["submission_ready"] is False
    assert gate["theory_validation_claim_made"] is False
    assert gate["hard_requirement_count"] == 7
    assert gate["hard_requirement_passed_count"] == 2
    assert gate["hard_requirement_failed_count"] == 5
    assert gate["blocking_limitation_count"] == 8
    assert len(gate["hard_requirements"]) == 7
    assert len(gate["blocking_limitations"]) == 8

    expected_requirements = {
        "V9-5-GATE-REQ-001": True,
        "V9-5-GATE-REQ-002": True,
        "V9-5-GATE-REQ-003": False,
        "V9-5-GATE-REQ-004": False,
        "V9-5-GATE-REQ-005": False,
        "V9-5-GATE-REQ-006": False,
        "V9-5-GATE-REQ-007": False,
    }

    for item in gate["hard_requirements"]:
        assert item["requirement_id"] in expected_requirements
        assert item["passed"] is expected_requirements[item["requirement_id"]]

    assert "safe toy evidence" in gate["decision_reason"]
    assert "formal toy results report" in gate["decision_reason"]
    assert "toy falsification audit" in gate["decision_reason"]
    assert "lacks external validation" in gate["decision_reason"]
    assert "independent experiment" in gate["decision_reason"]
    assert "proof assistant verification" in gate["decision_reason"]
    assert "citation integration" in gate["decision_reason"]
    assert "manuscript mutation" in gate["decision_reason"]
    assert "readiness approval" in gate["decision_reason"]
    assert "manuscript submission readiness is denied" in gate["decision_reason"]

    expected_counts = {
        "V9 toy evidence limitation and readiness gate artifact count": 1,
        "V9 toy evidence limitation analysis count": 1,
        "V9 manuscript readiness gate execution count": 1,
        "V9 manuscript readiness denial count": 1,
        "V9 manuscript readiness approval count": 0,
        "V9 readiness hard requirement count": 7,
        "V9 readiness hard requirement passed count": 2,
        "V9 readiness hard requirement failed count": 5,
        "V9 blocking evidence limitation count": 8,
        "V9 source formal results report count": 1,
        "V9 source results report count": 1,
        "V9 source falsification audit execution count": 1,
        "V9 source toy result summary count": 1,
        "V9 source toy falsification audit record count": 4,
        "V9 source theory validation claim count": 0,
        "V9 source manuscript readiness claim count": 0,
        "V9 theory validation claim count": 0,
        "V9 manuscript readiness claim count": 0,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "V9 manuscript readiness approval count",
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

    required_phrases = [
        "toy evidence limitation analysis",
        "manuscript readiness gate",
        "not_ready_for_manuscript_submission",
        "denies manuscript submission readiness",
        "toy-only",
        "lacks external validation",
        "independent experiment",
        "proof assistant verification",
        "citation integration",
        "manuscript mutation",
        "readiness approval",
        "No validation claim is made",
        "No manuscript readiness claim is made",
        "No submission readiness approval is recorded",
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
    ]

    for phrase in required_phrases:
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

    print("V9_5_VIRUSE_FABRIC_TOY_EVIDENCE_LIMITATION_AND_MANUSCRIPT_READINESS_GATE_OK")
    print("VIRUSE_FABRIC_TOY_EVIDENCE_LIMITATION_AND_MANUSCRIPT_READINESS_GATE_DIRECT_CHECK_OK")
    print(f"Toy evidence limitation analysis count: {counters['V9 toy evidence limitation analysis count']}")
    print(f"Manuscript readiness gate execution count: {counters['V9 manuscript readiness gate execution count']}")
    print(f"Manuscript readiness denial count: {counters['V9 manuscript readiness denial count']}")
    print(f"Manuscript readiness approval count: {counters['V9 manuscript readiness approval count']}")
    print(f"Hard requirement count: {counters['V9 readiness hard requirement count']}")
    print(f"Hard requirement passed count: {counters['V9 readiness hard requirement passed count']}")
    print(f"Hard requirement failed count: {counters['V9 readiness hard requirement failed count']}")
    print(f"Blocking evidence limitation count: {counters['V9 blocking evidence limitation count']}")
    print(f"Gate decision: {gate['gate_decision']}")
    print(f"Submission ready: {gate['submission_ready']}")
    print(f"Approval recorded: {gate['approval_recorded']}")
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
