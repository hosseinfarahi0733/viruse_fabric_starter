from __future__ import annotations

import json

from viruse_fabric.writing.safe_abstract_toy_citation_retrieval_batch_1_source_verification_evidence_packet import (
    SafeAbstractToyCitationRetrievalBatch1SourceVerificationEvidencePacketBuilder,
)


def main() -> None:
    builder = SafeAbstractToyCitationRetrievalBatch1SourceVerificationEvidencePacketBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "citation-retrieval-batch-1-source-verification-evidence-packet-only"
    assert report["plan_phrase"] == (
        "batch_1_source_verification_evidence_recorded_but_not_verified_accepted_or_integrated"
    )

    assert report["source_candidate_count"] == 7
    assert report["verification_evidence_packet_completed"] is True
    assert report["verification_evidence_records_recorded"] is True
    assert report["verification_evidence_record_count"] == 7
    assert report["verification_evidence_candidate_coverage_complete"] is True

    assert report["source_verification_performed"] is False
    assert report["verified_sources_claimed"] is False
    assert report["acceptance_decisions_recorded"] is False
    assert report["rejection_decisions_recorded"] is False
    assert report["accepted_sources_recorded"] is False
    assert report["rejected_sources_recorded"] is False
    assert report["actual_citations_added"] is False
    assert report["fabricated_references_introduced"] is False
    assert report["citation_integration_completed"] is False
    assert report["manuscript_rewrite_applied"] is False
    assert report["application_permission_granted"] is False
    assert report["application_execution_performed"] is False
    assert report["checklist_completion_performed"] is False
    assert report["checklist_execution_performed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["evaluation_execution_performed"] is False
    assert report["evidence_upgrade_completed"] is False
    assert report["validation_claim_made"] is False
    assert report["applied_patch_count"] == 0

    evidence_records = report["verification_evidence_records"]
    assert len(evidence_records) == 7
    assert len({record["evidence_record_id"] for record in evidence_records}) == 7
    assert len({record["candidate_id"] for record in evidence_records}) == 7

    expected_candidate_ids = {
        "CAND-B1-001",
        "CAND-B1-002",
        "CAND-B1-003",
        "CAND-B1-004",
        "CAND-B1-005",
        "CAND-B1-006",
        "CAND-B1-007",
    }
    assert set(report["source_candidate_ids"]) == expected_candidate_ids
    assert {record["candidate_id"] for record in evidence_records} == expected_candidate_ids

    for record in evidence_records:
        assert record["verification_evidence_status"] == "verification_evidence_recorded_not_accepted"
        assert record["source_verification_decision"] == "no_verification_decision_recorded"
        assert record["source_acceptance_decision"] == "no_acceptance_decision_recorded"
        assert record["source_rejection_decision"] == "no_rejection_decision_recorded"
        assert record["citation_integration_status"] == "not_integrated"
        assert record["manuscript_mutation_status"] == "no_mutation"
        assert record["safety_scope"] == "non_operational_methodological_source_only"

    expected_counts = {
        "Toy citation batch 1 source verification evidence record count": 7,
        "Toy citation batch 1 source verification evidence recorded count": 7,
        "Toy citation batch 1 source verification evidence candidate coverage count": 7,
        "Toy citation batch 1 source verification evidence official locator count": 7,
        "Toy citation batch 1 source verification evidence publisher page count": 5,
        "Toy citation batch 1 source verification evidence database record count": 1,
        "Toy citation batch 1 source verification evidence official book website count": 1,
        "Toy citation batch 1 source verification evidence field check count": 42,
        "Toy citation batch 1 source verification evidence locator claim count": 29,
        "Toy citation batch 1 source verification evidence control count": 8,
        "Toy citation batch 1 source verification final decision count": 0,
        "Toy citation batch 1 verified source count": 0,
        "Toy citation batch 1 accepted source count": 0,
        "Toy citation batch 1 rejected source count": 0,
        "Toy citation batch 1 actual citation count": 0,
        "Toy citation batch 1 citation integration completion count": 0,
        "Toy citation batch 1 added to manuscript count": 0,
        "Toy citation batch 1 manuscript mutation count": 0,
        "Toy citation batch 1 prior candidate source row count": 7,
        "Toy citation batch 1 prior candidate source recorded count": 7,
        "Toy citation batch 1 prior source retrieval count": 7,
        "Toy citation batch 1 prior verified source count": 0,
        "Toy citation batch 1 prior actual citation count": 0,
        "Toy citation batch 1 prior empty ledger row count": 0,
        "Toy citation batch 1 source candidate ledger field count": 16,
        "Toy citation batch 1 source retrieval gate item count": 12,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "Toy citation batch 1 source verification final decision count",
        "Toy citation batch 1 verified source count",
        "Toy citation batch 1 accepted source count",
        "Toy citation batch 1 rejected source count",
        "Toy citation batch 1 acceptance decision count",
        "Toy citation batch 1 rejection decision count",
        "Toy citation batch 1 actual citation count",
        "Toy citation batch 1 fabricated reference count",
        "Toy citation batch 1 citation integration completion count",
        "Toy citation batch 1 added to manuscript count",
        "Toy citation batch 1 manuscript mutation count",
        "Toy citation verified source count",
        "Toy citation actual citation count",
        "Toy citation fabricated reference count",
        "Toy citation integration completion count",
        "Toy citation added to manuscript count",
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

    combined_text = (
        json.dumps(report["verification_evidence_records"], ensure_ascii=False)
        + " "
        + json.dumps(report["verification_evidence_controls"], ensure_ascii=False)
        + " "
        + report["non_readiness_disclaimer"]
    )

    for phrase in [
        "Verification evidence packet only",
        "verification_evidence_recorded_not_accepted",
        "no_verification_decision_recorded",
        "no_acceptance_decision_recorded",
        "no_rejection_decision_recorded",
        "not_integrated",
        "no_mutation",
        "No source is claimed as verified",
        "No accepted source is recorded",
        "No rejected source is recorded",
        "No actual citation is added",
        "No fabricated reference is introduced",
        "does not complete citation integration",
        "does not validate scientific claims",
        "No real biological datasets",
        "no real pathogen models",
        "no receptor parameters",
        "no operational targeting",
        "No new citation is added",
        "No manuscript file is modified",
    ]:
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

    print("V8_225_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_EVIDENCE_PACKET_OK")
    print("TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_EVIDENCE_PACKET_DIRECT_CHECK_OK")
    print(f"Evidence record count: {counters['Toy citation batch 1 source verification evidence record count']}")
    print(f"Evidence recorded count: {counters['Toy citation batch 1 source verification evidence recorded count']}")
    print(f"Evidence candidate coverage count: {counters['Toy citation batch 1 source verification evidence candidate coverage count']}")
    print(f"Official locator count: {counters['Toy citation batch 1 source verification evidence official locator count']}")
    print(f"Publisher page count: {counters['Toy citation batch 1 source verification evidence publisher page count']}")
    print(f"Database record count: {counters['Toy citation batch 1 source verification evidence database record count']}")
    print(f"Official book website count: {counters['Toy citation batch 1 source verification evidence official book website count']}")
    print(f"Evidence field check count: {counters['Toy citation batch 1 source verification evidence field check count']}")
    print(f"Evidence locator claim count: {counters['Toy citation batch 1 source verification evidence locator claim count']}")
    print(f"Evidence control count: {counters['Toy citation batch 1 source verification evidence control count']}")
    print(f"Final verification decision count: {counters['Toy citation batch 1 source verification final decision count']}")
    print(f"Verified source count: {counters['Toy citation batch 1 verified source count']}")
    print(f"Accepted source count: {counters['Toy citation batch 1 accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation batch 1 rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation batch 1 actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation batch 1 fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation batch 1 citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation batch 1 added to manuscript count']}")
    print(f"Manuscript mutation count: {counters['Toy citation batch 1 manuscript mutation count']}")
    print(f"Prior candidate source row count: {counters['Toy citation batch 1 prior candidate source row count']}")
    print(f"Prior source retrieval count: {counters['Toy citation batch 1 prior source retrieval count']}")
    print(f"Toy citation verified source count: {counters['Toy citation verified source count']}")
    print(f"Toy citation actual citation count: {counters['Toy citation actual citation count']}")
    print(f"Toy citation fabricated reference count: {counters['Toy citation fabricated reference count']}")
    print(f"Toy citation integration completion count: {counters['Toy citation integration completion count']}")
    print(f"Toy citation added to manuscript count: {counters['Toy citation added to manuscript count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
