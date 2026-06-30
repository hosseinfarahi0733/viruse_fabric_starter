from __future__ import annotations

import json

from viruse_fabric.writing.safe_abstract_toy_citation_retrieval_batch_1_source_acceptance_decision_register import (
    SafeAbstractToyCitationRetrievalBatch1SourceAcceptanceDecisionRegisterBuilder,
)


def main() -> None:
    builder = SafeAbstractToyCitationRetrievalBatch1SourceAcceptanceDecisionRegisterBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "citation-retrieval-batch-1-source-acceptance-decision-register-only"
    assert report["plan_phrase"] == (
        "batch_1_source_acceptance_decisions_recorded_but_not_citation_ready_cited_integrated_or_mutated"
    )

    assert report["source_eligibility_gate_record_count"] == 7
    assert report["source_acceptance_decision_record_count"] == 7
    assert report["acceptance_decision_candidate_coverage_complete"] is True

    for field in [
        "source_acceptance_decision_register_completed",
        "source_acceptance_decisions_recorded",
        "accepted_sources_recorded",
        "accepted_for_methodological_source_pool_recorded",
        "source_acceptance_performed",
    ]:
        assert report[field] is True, f"Expected True for {field}"

    for field in [
        "source_rejection_performed",
        "rejected_sources_recorded",
        "citation_ready_sources_recorded",
        "actual_citations_added",
        "fabricated_references_introduced",
        "citation_integration_completed",
        "manuscript_rewrite_applied",
        "application_permission_granted",
        "application_execution_performed",
        "checklist_completion_performed",
        "checklist_execution_performed",
        "manuscript_file_modified",
        "manuscript_mutation",
        "evaluation_execution_performed",
        "evidence_upgrade_completed",
        "validation_claim_made",
        "readiness_approval_recorded",
        "new_citation_added",
    ]:
        assert report[field] is False, f"Expected False for {field}"

    assert report["applied_patch_count"] == 0

    acceptance_records = report["source_acceptance_decision_records"]
    criteria = report["source_acceptance_criteria"]
    controls = report["source_acceptance_controls"]

    assert len(acceptance_records) == 7
    assert len(criteria) == 7
    assert len(controls) == 13
    assert len({record["acceptance_decision_record_id"] for record in acceptance_records}) == 7
    assert len({record["candidate_id"] for record in acceptance_records}) == 7

    expected_candidate_ids = {
        "CAND-B1-001",
        "CAND-B1-002",
        "CAND-B1-003",
        "CAND-B1-004",
        "CAND-B1-005",
        "CAND-B1-006",
        "CAND-B1-007",
    }
    assert {record["candidate_id"] for record in acceptance_records} == expected_candidate_ids

    for record in acceptance_records:
        assert record["acceptance_scope"] == "methodological_source_pool_acceptance_only"
        assert record["acceptance_decision_status"] == "accepted_for_methodological_source_pool_only"
        assert record["accepted_source_status"] == "accepted_not_citation_ready"
        assert record["rejection_decision_status"] == "no_rejection_decision_recorded"
        assert record["citation_readiness_status"] == "not_citation_ready"
        assert record["citation_integration_status"] == "not_integrated"
        assert record["actual_citation_status"] == "no_actual_citation_added"
        assert record["fabricated_reference_status"] == "no_fabricated_reference_introduced"
        assert record["manuscript_mutation_status"] == "no_mutation"
        assert record["manuscript_file_status"] == "no_manuscript_file_modified"
        assert record["scientific_validation_status"] == "scientific_validation_not_claimed"
        assert record["readiness_approval_status"] == "no_readiness_approval_recorded"
        assert record["new_citation_status"] == "no_new_citation_added"
        assert record["source_operational_scope"] == "non_operational_methodological_source_only"
        assert len(record["criterion_results"]) == 7

        for criterion_result in record["criterion_results"]:
            assert criterion_result["criterion_result"] == "passed_for_methodological_source_pool_acceptance_only"
            assert "does not create citation readiness" in criterion_result["criterion_boundary"]
            assert "citation insertion" in criterion_result["criterion_boundary"]
            assert "manuscript mutation" in criterion_result["criterion_boundary"]

    expected_counts = {
        "Toy citation batch 1 source acceptance decision record count": 7,
        "Toy citation batch 1 acceptance decision count": 7,
        "Toy citation batch 1 accepted source count": 7,
        "Toy citation batch 1 accepted methodological source pool count": 7,
        "Toy citation batch 1 accepted not citation-ready source count": 7,
        "Toy citation batch 1 acceptance decision candidate coverage count": 7,
        "Toy citation batch 1 acceptance decision criterion group count": 7,
        "Toy citation batch 1 acceptance decision criterion evaluation count": 49,
        "Toy citation batch 1 acceptance decision control count": 13,
        "Toy citation batch 1 rejection decision count": 0,
        "Toy citation batch 1 rejected source count": 0,
        "Toy citation batch 1 citation-ready source count": 0,
        "Toy citation batch 1 actual citation count": 0,
        "Toy citation batch 1 fabricated reference count": 0,
        "Toy citation batch 1 citation integration completion count": 0,
        "Toy citation batch 1 added to manuscript count": 0,
        "Toy citation batch 1 manuscript mutation count": 0,
        "Toy citation batch 1 prior acceptance eligibility gate record count": 7,
        "Toy citation batch 1 prior eligible for future acceptance review count": 7,
        "Toy citation batch 1 prior acceptance decision count": 0,
        "Toy citation batch 1 prior accepted source count": 0,
        "Toy citation batch 1 prior citation-ready source count": 0,
        "Toy citation batch 1 prior actual citation count": 0,
        "Toy citation batch 1 prior source verification decision record count": 7,
        "Toy citation batch 1 prior metadata-only verification decision count": 7,
        "Toy citation batch 1 prior bibliographic metadata verified source count": 7,
        "Toy citation batch 1 prior evidence record count": 7,
        "Toy citation batch 1 prior evidence locator claim count": 29,
        "Toy citation batch 1 prior candidate source row count": 7,
        "Toy citation batch 1 source candidate ledger field count": 16,
        "Toy citation accepted source count": 7,
        "Toy citation accepted methodological source pool count": 7,
        "Toy citation accepted not citation-ready source count": 7,
        "Toy citation rejected source count": 0,
        "Toy citation citation-ready source count": 0,
        "Toy citation actual citation count": 0,
        "Toy citation fabricated reference count": 0,
        "Toy citation integration completion count": 0,
        "Toy citation added to manuscript count": 0,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "Toy citation batch 1 rejection decision count",
        "Toy citation batch 1 rejected source count",
        "Toy citation batch 1 citation-ready source count",
        "Toy citation batch 1 actual citation count",
        "Toy citation batch 1 fabricated reference count",
        "Toy citation batch 1 citation integration completion count",
        "Toy citation batch 1 added to manuscript count",
        "Toy citation batch 1 manuscript mutation count",
        "Toy citation rejected source count",
        "Toy citation citation-ready source count",
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
        json.dumps(report["source_acceptance_criteria"], ensure_ascii=False)
        + " "
        + json.dumps(report["source_acceptance_decision_records"], ensure_ascii=False)
        + " "
        + json.dumps(report["source_acceptance_controls"], ensure_ascii=False)
        + " "
        + report["non_readiness_disclaimer"]
    )

    for phrase in [
        "Source acceptance decision register only",
        "Accepted for methodological source pool only",
        "Accepted source does not mean citation-ready source",
        "methodological_source_pool_acceptance_only",
        "accepted_for_methodological_source_pool_only",
        "accepted_not_citation_ready",
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
        "No readiness approval is recorded",
        "No new citation is added",
        "No manuscript file is modified",
        "not_integrated",
        "no_mutation",
        "scientific_validation_not_claimed",
        "non_operational_methodological_source_only",
    ]:
        assert phrase in combined_text, f"Missing required phrase: {phrase}"

    print("V8_228_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_ACCEPTANCE_DECISION_REGISTER_OK")
    print("TOY_CITATION_RETRIEVAL_BATCH_1_SOURCE_ACCEPTANCE_DECISION_REGISTER_DIRECT_CHECK_OK")
    print(f"Acceptance decision record count: {counters['Toy citation batch 1 source acceptance decision record count']}")
    print(f"Acceptance decision count: {counters['Toy citation batch 1 acceptance decision count']}")
    print(f"Accepted source count: {counters['Toy citation batch 1 accepted source count']}")
    print(f"Accepted methodological source pool count: {counters['Toy citation batch 1 accepted methodological source pool count']}")
    print(f"Accepted not citation-ready source count: {counters['Toy citation batch 1 accepted not citation-ready source count']}")
    print(f"Acceptance decision candidate coverage count: {counters['Toy citation batch 1 acceptance decision candidate coverage count']}")
    print(f"Acceptance decision criterion group count: {counters['Toy citation batch 1 acceptance decision criterion group count']}")
    print(f"Acceptance decision criterion evaluation count: {counters['Toy citation batch 1 acceptance decision criterion evaluation count']}")
    print(f"Acceptance decision control count: {counters['Toy citation batch 1 acceptance decision control count']}")
    print(f"Rejection decision count: {counters['Toy citation batch 1 rejection decision count']}")
    print(f"Rejected source count: {counters['Toy citation batch 1 rejected source count']}")
    print(f"Citation-ready source count: {counters['Toy citation batch 1 citation-ready source count']}")
    print(f"Actual citation count: {counters['Toy citation batch 1 actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation batch 1 fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation batch 1 citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation batch 1 added to manuscript count']}")
    print(f"Manuscript mutation count: {counters['Toy citation batch 1 manuscript mutation count']}")
    print(f"Prior eligibility gate record count: {counters['Toy citation batch 1 prior acceptance eligibility gate record count']}")
    print(f"Prior eligible for future acceptance review count: {counters['Toy citation batch 1 prior eligible for future acceptance review count']}")
    print(f"Prior acceptance decision count: {counters['Toy citation batch 1 prior acceptance decision count']}")
    print(f"Prior accepted source count: {counters['Toy citation batch 1 prior accepted source count']}")
    print(f"Toy citation accepted source count: {counters['Toy citation accepted source count']}")
    print(f"Toy citation accepted not citation-ready source count: {counters['Toy citation accepted not citation-ready source count']}")
    print(f"Toy citation citation-ready source count: {counters['Toy citation citation-ready source count']}")
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
