from __future__ import annotations

import json

from viruse_fabric.writing.safe_abstract_toy_citation_retrieval_batch_1_source_verification_decision_register import (
    SafeAbstractToyCitationRetrievalBatch1SourceVerificationDecisionRegisterBuilder,
)


def main() -> None:
    builder = SafeAbstractToyCitationRetrievalBatch1SourceVerificationDecisionRegisterBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "citation-retrieval-batch-1-source-verification-decision-register-only"
    assert report["plan_phrase"] == (
        "batch_1_metadata_verification_decisions_recorded_but_not_accepted_cited_or_integrated"
    )

    assert report["source_candidate_count"] == 7
    assert report["evidence_record_count"] == 7
    assert report["decision_record_count"] == 7
    assert report["decision_candidate_coverage_complete"] is True
    assert report["source_verification_decision_register_completed"] is True
    assert report["metadata_verification_decisions_recorded"] is True
    assert report["bibliographic_metadata_verified_sources_recorded"] is True

    assert report["source_verification_performed"] is False
    assert report["full_source_verification_claimed"] is False
    assert report["verified_sources_claimed"] is False
    assert report["acceptance_decisions_recorded"] is False
    assert report["rejection_decisions_recorded"] is False
    assert report["accepted_sources_recorded"] is False
    assert report["rejected_sources_recorded"] is False
    assert report["citation_ready_sources_recorded"] is False
    assert report["actual_citations_added"] is False
    assert report["fabricated_references_introduced"] is False
    assert report["citation_integration_completed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["validation_claim_made"] is False
    assert report["applied_patch_count"] == 0

    decision_records = report["source_verification_decision_records"]
    assert len(decision_records) == 7
    assert len({record["decision_record_id"] for record in decision_records}) == 7
    assert len({record["candidate_id"] for record in decision_records}) == 7

    expected_candidate_ids = {
        "CAND-B1-001",
        "CAND-B1-002",
        "CAND-B1-003",
        "CAND-B1-004",
        "CAND-B1-005",
        "CAND-B1-006",
        "CAND-B1-007",
    }
    assert {record["candidate_id"] for record in decision_records} == expected_candidate_ids

    for record in decision_records:
        assert record["decision_scope"] == "metadata_only"
        assert record["decision_kind"] == "bibliographic_metadata_verification_decision"
        assert record["decision_result"] == "metadata_verified_not_accepted"
        assert record["metadata_verification_status"] == "bibliographic_metadata_verified"
        assert record["metadata_verified_source_status"] == "metadata_verified_source_recorded"
        assert record["full_source_verification_status"] == "full_source_verification_not_claimed"
        assert record["source_acceptance_decision"] == "no_acceptance_decision_recorded"
        assert record["source_rejection_decision"] == "no_rejection_decision_recorded"
        assert record["citation_readiness_status"] == "not_citation_ready"
        assert record["citation_integration_status"] == "not_integrated"
        assert record["manuscript_mutation_status"] == "no_mutation"
        assert record["scientific_validation_status"] == "scientific_validation_not_claimed"
        assert record["source_operational_scope"] == "non_operational_methodological_source_only"

    expected_counts = {
        "Toy citation batch 1 source verification decision record count": 7,
        "Toy citation batch 1 metadata-only verification decision count": 7,
        "Toy citation batch 1 bibliographic metadata verified source count": 7,
        "Toy citation batch 1 metadata verified not accepted source count": 7,
        "Toy citation batch 1 metadata verified source recorded count": 7,
        "Toy citation batch 1 verification decision evidence coverage count": 7,
        "Toy citation batch 1 verification decision control count": 10,
        "Toy citation batch 1 full source verification claim count": 0,
        "Toy citation batch 1 citation-ready verified source count": 0,
        "Toy citation batch 1 accepted source count": 0,
        "Toy citation batch 1 rejected source count": 0,
        "Toy citation batch 1 acceptance decision count": 0,
        "Toy citation batch 1 rejection decision count": 0,
        "Toy citation batch 1 actual citation count": 0,
        "Toy citation batch 1 fabricated reference count": 0,
        "Toy citation batch 1 citation integration completion count": 0,
        "Toy citation batch 1 added to manuscript count": 0,
        "Toy citation batch 1 manuscript mutation count": 0,
        "Toy citation batch 1 prior evidence record count": 7,
        "Toy citation batch 1 prior evidence recorded count": 7,
        "Toy citation batch 1 prior evidence candidate coverage count": 7,
        "Toy citation batch 1 prior evidence locator claim count": 29,
        "Toy citation batch 1 prior final verification decision count": 0,
        "Toy citation batch 1 prior verified source count": 0,
        "Toy citation batch 1 prior actual citation count": 0,
        "Toy citation batch 1 prior candidate source row count": 7,
        "Toy citation batch 1 prior candidate source recorded count": 7,
        "Toy citation batch 1 prior source retrieval count": 7,
        "Toy citation batch 1 prior empty ledger row count": 0,
        "Toy citation batch 1 source candidate ledger field count": 16,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "Toy citation batch 1 full source verification claim count",
        "Toy citation batch 1 citation-ready verified source count",
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
        json.dumps(report["source_verification_decision_records"], ensure_ascii=False)
        + " "
        + json.dumps(report["source_verification_decision_controls"], ensure_ascii=False)
        + " "
        + report["non_readiness_disclaimer"]
    )

    for phrase in [
        "Metadata-only source verification decision register",
        "bibliographic_metadata_verification_decision",
        "metadata_verified_not_accepted",
        "bibliographic_metadata_verified",
        "metadata_verified_source_recorded",
        "full_source_verification_not_claimed",
        "no_acceptance_decision_recorded",
        "no_rejection_decision_recorded",
        "not_citation_ready",
        "not_integrated",
        "no_mutation",
        "scientific_validation_not_claimed",
        "Full source verification is not claimed",
        "No accepted source is recorded",
        "No rejected source is recorded",
        "No source is marked citation-ready",
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

    print("V8_226_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_DECISION_REGISTER_OK")
    print("TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_VERIFICATION_DECISION_REGISTER_DIRECT_CHECK_OK")
    print(f"Decision record count: {counters['Toy citation batch 1 source verification decision record count']}")
    print(f"Metadata-only verification decision count: {counters['Toy citation batch 1 metadata-only verification decision count']}")
    print(f"Bibliographic metadata verified source count: {counters['Toy citation batch 1 bibliographic metadata verified source count']}")
    print(f"Metadata verified not accepted source count: {counters['Toy citation batch 1 metadata verified not accepted source count']}")
    print(f"Metadata verified source recorded count: {counters['Toy citation batch 1 metadata verified source recorded count']}")
    print(f"Verification decision evidence coverage count: {counters['Toy citation batch 1 verification decision evidence coverage count']}")
    print(f"Verification decision control count: {counters['Toy citation batch 1 verification decision control count']}")
    print(f"Full source verification claim count: {counters['Toy citation batch 1 full source verification claim count']}")
    print(f"Citation-ready verified source count: {counters['Toy citation batch 1 citation-ready verified source count']}")
    print(f"Accepted source count: {counters['Toy citation batch 1 accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation batch 1 rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation batch 1 actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation batch 1 fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation batch 1 citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation batch 1 added to manuscript count']}")
    print(f"Manuscript mutation count: {counters['Toy citation batch 1 manuscript mutation count']}")
    print(f"Prior evidence record count: {counters['Toy citation batch 1 prior evidence record count']}")
    print(f"Prior evidence locator claim count: {counters['Toy citation batch 1 prior evidence locator claim count']}")
    print(f"Prior final verification decision count: {counters['Toy citation batch 1 prior final verification decision count']}")
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
