from __future__ import annotations

import json

from viruse_fabric.writing.safe_abstract_toy_citation_retrieval_candidate_ledger_schema import (
    SafeAbstractToyCitationRetrievalCandidateLedgerSchemaBuilder,
)


def main() -> None:
    builder = SafeAbstractToyCitationRetrievalCandidateLedgerSchemaBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "citation-retrieval-candidate-ledger-schema-only"
    assert report["plan_phrase"] == (
        "citation_retrieval_candidate_ledger_schema_created_but_no_candidates_recorded"
    )

    assert report["candidate_ledger_schema_completed"] is True
    assert report["candidate_ledger_rows_created"] is False
    assert report["candidate_sources_recorded"] is False
    assert report["candidate_acceptance_decisions_recorded"] is False
    assert report["candidate_rejection_decisions_recorded"] is False
    assert report["retrieval_authorization_granted"] is False
    assert report["source_retrieval_performed"] is False
    assert report["verified_sources_claimed"] is False
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

    assert counters["Toy citation candidate ledger field count"] == 16
    assert counters["Toy citation candidate status enum count"] == 8
    assert counters["Toy citation candidate provenance field count"] == 10
    assert counters["Toy citation candidate safety screen field count"] == 10
    assert counters["Toy citation candidate hallucination control count"] == 10

    assert counters["Toy citation candidate ledger row count"] == 0
    assert counters["Toy citation candidate source recorded count"] == 0
    assert counters["Toy citation candidate acceptance decision count"] == 0
    assert counters["Toy citation candidate rejection decision count"] == 0
    assert counters["Toy citation candidate blocked decision count"] == 0
    assert counters["Toy citation candidate retrieval authorization count"] == 0
    assert counters["Toy citation candidate retrieval execution count"] == 0
    assert counters["Toy citation candidate source retrieval count"] == 0
    assert counters["Toy citation candidate verified source count"] == 0
    assert counters["Toy citation candidate accepted source count"] == 0
    assert counters["Toy citation candidate rejected source count"] == 0
    assert counters["Toy citation candidate actual citation count"] == 0
    assert counters["Toy citation candidate fabricated reference count"] == 0
    assert counters["Toy citation candidate integration completion count"] == 0
    assert counters["Toy citation candidate added to manuscript count"] == 0

    assert counters["Toy citation candidate source retrieval gate item count"] == 12
    assert counters["Toy citation candidate source allowed query family count"] == 12
    assert counters["Toy citation candidate source acceptance schema field count"] == 12
    assert counters["Toy citation candidate source rejection reason count"] == 10
    assert counters["Toy citation candidate source preflight check count"] == 10

    assert counters["Toy citation candidate source prior retrieval authorization count"] == 0
    assert counters["Toy citation candidate source prior retrieval execution count"] == 0
    assert counters["Toy citation candidate source prior source retrieval count"] == 0
    assert counters["Toy citation candidate source prior verified source count"] == 0
    assert counters["Toy citation candidate source prior accepted source count"] == 0
    assert counters["Toy citation candidate source prior rejected source count"] == 0
    assert counters["Toy citation candidate source prior actual citation count"] == 0
    assert counters["Toy citation candidate source prior fabricated reference count"] == 0
    assert counters["Toy citation candidate source prior integration completion count"] == 0
    assert counters["Toy citation candidate source prior added to manuscript count"] == 0

    assert counters["Toy citation candidate source eligibility rule count"] == 12
    assert counters["Toy citation candidate source query plan count"] == 12
    assert counters["Toy citation candidate source exclusion group count"] == 4
    assert counters["Toy citation candidate source slot count"] == 12
    assert counters["Toy citation candidate source unresolved slot count"] == 12
    assert counters["Toy citation candidate source slot group count"] == 4
    assert counters["Toy citation candidate source assembly section count"] == 9
    assert counters["Toy citation candidate source gap item count"] == 12
    assert counters["Toy citation candidate source P0 gap count"] == 6
    assert counters["Toy citation candidate source evidence upgrade completed count"] == 0
    assert counters["Toy citation candidate source evaluation design module count"] == 10
    assert counters["Toy citation candidate source actual evaluation run count"] == 0
    assert counters["Toy citation candidate source validation claim count"] == 0
    assert counters["Toy citation candidate source coherence improvement item count"] == 10
    assert counters["Toy citation candidate source coherence rewrite application count"] == 0

    assert counters["Toy citation candidate ledger schema execution count"] == 1
    assert counters["Toy citation candidate ledger schema direct execution count"] == 1

    combined_text = (
        json.dumps(report["ledger_fields"], ensure_ascii=False)
        + " "
        + json.dumps(report["status_enums"], ensure_ascii=False)
        + " "
        + json.dumps(report["provenance_fields"], ensure_ascii=False)
        + " "
        + json.dumps(report["safety_screen_fields"], ensure_ascii=False)
        + " "
        + json.dumps(report["hallucination_controls"], ensure_ascii=False)
        + " "
        + report["non_readiness_disclaimer"]
    )

    for phrase in [
        "citation retrieval candidate ledger schema",
        "Candidate ledger schema only",
        "No candidate source is recorded",
        "not_recorded",
        "pending_future_retrieval",
        "accepted_candidate",
        "rejected_candidate",
        "blocked_for_safety",
        "No retrieval authorization is granted",
        "No source retrieval is performed",
        "No actual citation is added",
        "No fabricated reference is introduced",
        "No source is claimed as verified",
        "Future source retrieval requires a separate official milestone",
        "does not complete citation integration",
        "does not validate scientific claims",
        "No real biological datasets",
        "no real pathogen models",
        "no receptor parameters",
        "no operational targeting",
        "No new citation is added",
        "No manuscript file is modified",
    ]:
        assert phrase in combined_text, f"Missing candidate ledger phrase: {phrase}"

    must_be_zero = [
        "Toy citation candidate ledger row count",
        "Toy citation candidate source recorded count",
        "Toy citation candidate acceptance decision count",
        "Toy citation candidate rejection decision count",
        "Toy citation candidate blocked decision count",
        "Toy citation candidate retrieval authorization count",
        "Toy citation candidate retrieval execution count",
        "Toy citation candidate source retrieval count",
        "Toy citation candidate verified source count",
        "Toy citation candidate accepted source count",
        "Toy citation candidate rejected source count",
        "Toy citation candidate actual citation count",
        "Toy citation candidate fabricated reference count",
        "Toy citation candidate integration completion count",
        "Toy citation candidate added to manuscript count",
        "Toy citation actual citation count",
        "Toy citation verified source count",
        "Toy citation fabricated reference count",
        "Toy citation source retrieval execution count",
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

    print("V8_222_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_CANDIDATE_LEDGER_SCHEMA_OK")
    print("TOY_CITATION_RETRIEVAL_CANDIDATE_LEDGER_SCHEMA_DIRECT_CHECK_OK")
    print(f"Candidate ledger field count: {counters['Toy citation candidate ledger field count']}")
    print(f"Candidate status enum count: {counters['Toy citation candidate status enum count']}")
    print(f"Candidate provenance field count: {counters['Toy citation candidate provenance field count']}")
    print(f"Candidate safety screen field count: {counters['Toy citation candidate safety screen field count']}")
    print(f"Candidate hallucination control count: {counters['Toy citation candidate hallucination control count']}")
    print(f"Candidate ledger row count: {counters['Toy citation candidate ledger row count']}")
    print(f"Candidate source recorded count: {counters['Toy citation candidate source recorded count']}")
    print(f"Candidate acceptance decision count: {counters['Toy citation candidate acceptance decision count']}")
    print(f"Candidate rejection decision count: {counters['Toy citation candidate rejection decision count']}")
    print(f"Candidate blocked decision count: {counters['Toy citation candidate blocked decision count']}")
    print(f"Retrieval authorization count: {counters['Toy citation candidate retrieval authorization count']}")
    print(f"Retrieval execution count: {counters['Toy citation candidate retrieval execution count']}")
    print(f"Source retrieval count: {counters['Toy citation candidate source retrieval count']}")
    print(f"Verified source count: {counters['Toy citation candidate verified source count']}")
    print(f"Accepted source count: {counters['Toy citation candidate accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation candidate rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation candidate actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation candidate fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation candidate integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation candidate added to manuscript count']}")
    print(f"Source retrieval gate item count: {counters['Toy citation candidate source retrieval gate item count']}")
    print(f"Source allowed query family count: {counters['Toy citation candidate source allowed query family count']}")
    print(f"Source acceptance schema field count: {counters['Toy citation candidate source acceptance schema field count']}")
    print(f"Source rejection reason count: {counters['Toy citation candidate source rejection reason count']}")
    print(f"Source preflight check count: {counters['Toy citation candidate source preflight check count']}")
    print(f"Source eligibility rule count: {counters['Toy citation candidate source eligibility rule count']}")
    print(f"Source query plan count: {counters['Toy citation candidate source query plan count']}")
    print(f"Source exclusion group count: {counters['Toy citation candidate source exclusion group count']}")
    print(f"Source slot count: {counters['Toy citation candidate source slot count']}")
    print(f"Source unresolved slot count: {counters['Toy citation candidate source unresolved slot count']}")
    print(f"Source slot group count: {counters['Toy citation candidate source slot group count']}")
    print(f"Source assembly section count: {counters['Toy citation candidate source assembly section count']}")
    print(f"Source gap item count: {counters['Toy citation candidate source gap item count']}")
    print(f"Source P0 gap count: {counters['Toy citation candidate source P0 gap count']}")
    print(f"Source evidence upgrade completed count: {counters['Toy citation candidate source evidence upgrade completed count']}")
    print(f"Source evaluation design module count: {counters['Toy citation candidate source evaluation design module count']}")
    print(f"Source actual evaluation run count: {counters['Toy citation candidate source actual evaluation run count']}")
    print(f"Source validation claim count: {counters['Toy citation candidate source validation claim count']}")
    print(f"Source coherence improvement item count: {counters['Toy citation candidate source coherence improvement item count']}")
    print(f"Source coherence rewrite application count: {counters['Toy citation candidate source coherence rewrite application count']}")
    print(f"Evaluation actual run count: {counters['Toy evaluation actual run count']}")
    print(f"Evaluation result count: {counters['Toy evaluation result count']}")
    print(f"Validation claim count: {counters['Toy evaluation validation claim count']}")
    print(f"Evidence upgrade completed count: {counters['Toy scientific evidence upgrade completed count']}")
    print(f"Coherence rewrite application count: {counters['Toy manuscript coherence rewrite application count']}")
    print(f"Checklist completion count: {counters['Toy manuscript patch application checklist completion count']}")
    print(f"Checklist execution count: {counters['Toy manuscript patch application checklist execution count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Proof assistant verification count: {counters['Proof assistant verification count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
