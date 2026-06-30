from __future__ import annotations

import json

from viruse_fabric.writing.safe_abstract_toy_citation_retrieval_batch_1_candidate_intake import (
    SafeAbstractToyCitationRetrievalBatch1CandidateIntakeBuilder,
)


def main() -> None:
    builder = SafeAbstractToyCitationRetrievalBatch1CandidateIntakeBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "citation-retrieval-batch-1-candidate-intake-only"
    assert report["plan_phrase"] == "batch_1_candidate_sources_recorded_but_not_verified_accepted_or_integrated"

    assert report["candidate_intake_completed"] is True
    assert report["candidate_sources_recorded"] is True
    assert report["source_retrieval_performed"] is True
    assert report["source_retrieval_scope"] == "metadata-only-methodological-source-intake"
    assert report["candidate_source_count"] == 7

    assert report["verification_performed"] is False
    assert report["verified_sources_claimed"] is False
    assert report["acceptance_decisions_recorded"] is False
    assert report["rejection_decisions_recorded"] is False
    assert report["accepted_sources_recorded"] is False
    assert report["rejected_sources_recorded"] is False
    assert report["actual_citations_added"] is False
    assert report["fabricated_references_introduced"] is False
    assert report["citation_integration_completed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["validation_claim_made"] is False

    candidates = report["candidate_sources"]
    assert len(candidates) == 7
    assert len({item["candidate_id"] for item in candidates}) == 7

    for candidate in candidates:
        assert candidate["retrieval_status"] == "retrieved_not_verified"
        assert candidate["verification_status"] == "not_verified"
        assert candidate["acceptance_status"] == "pending_review_not_accepted"
        assert candidate["citation_integration_status"] == "not_integrated"
        assert candidate["manuscript_mutation_status"] == "no_mutation"
        assert candidate["safety_screen_status"] == "passed_non_operational_method_source_screen"
        assert candidate["claim_validation_status"] == "does_not_validate_scientific_claims"
        assert candidate["readiness_status"] == "does_not_approve_readiness"

    expected_counts = {
        "Toy citation batch 1 candidate source row count": 7,
        "Toy citation batch 1 candidate source recorded count": 7,
        "Toy citation batch 1 retrieved not verified candidate count": 7,
        "Toy citation batch 1 metadata-only candidate count": 7,
        "Toy citation batch 1 methodological source count": 7,
        "Toy citation batch 1 non-operational safety pass count": 7,
        "Toy citation batch 1 source retrieval execution count": 1,
        "Toy citation batch 1 source retrieval count": 7,
        "Toy citation batch 1 source book count": 5,
        "Toy citation batch 1 source article count": 2,
        "Toy citation batch 1 source DOI locator count": 4,
        "Toy citation batch 1 source ISBN locator count": 3,
        "Toy citation source retrieval execution count": 1,
        "Toy citation candidate source retrieval count": 7,
    }

    for name, expected in expected_counts.items():
        actual = counters.get(name)
        assert actual == expected, f"Expected {expected} for {name}, got {actual}"

    must_be_zero = [
        "Toy citation batch 1 verification execution count",
        "Toy citation batch 1 verified source count",
        "Toy citation batch 1 acceptance decision count",
        "Toy citation batch 1 rejection decision count",
        "Toy citation batch 1 accepted source count",
        "Toy citation batch 1 rejected source count",
        "Toy citation batch 1 blocked source count",
        "Toy citation batch 1 actual citation count",
        "Toy citation batch 1 fabricated reference count",
        "Toy citation batch 1 citation integration completion count",
        "Toy citation batch 1 added to manuscript count",
        "Toy citation batch 1 manuscript mutation count",
        "Toy citation actual citation count",
        "Toy citation verified source count",
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
        json.dumps(report["candidate_sources"], ensure_ascii=False)
        + " "
        + json.dumps(report["intake_controls"], ensure_ascii=False)
        + " "
        + report["non_readiness_disclaimer"]
    )

    for phrase in [
        "Candidate source intake only",
        "retrieved_not_verified",
        "not_verified",
        "pending_review_not_accepted",
        "not_integrated",
        "no_mutation",
        "metadata-only-methodological-source-intake",
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

    print("V8_224_SAFE_ABSTRACT_TOY_CITATION_RETRIEVAL_BATCH_1_CANDIDATE_INTAKE_OK")
    print("TOY_CITATION_RETRIEVAL_BATCH_1_CANDIDATE_INTAKE_DIRECT_CHECK_OK")
    print(f"Candidate source row count: {counters['Toy citation batch 1 candidate source row count']}")
    print(f"Candidate source recorded count: {counters['Toy citation batch 1 candidate source recorded count']}")
    print(f"Retrieved not verified candidate count: {counters['Toy citation batch 1 retrieved not verified candidate count']}")
    print(f"Metadata-only candidate count: {counters['Toy citation batch 1 metadata-only candidate count']}")
    print(f"Methodological source count: {counters['Toy citation batch 1 methodological source count']}")
    print(f"Non-operational safety pass count: {counters['Toy citation batch 1 non-operational safety pass count']}")
    print(f"Source retrieval execution count: {counters['Toy citation batch 1 source retrieval execution count']}")
    print(f"Source retrieval count: {counters['Toy citation batch 1 source retrieval count']}")
    print(f"Verification execution count: {counters['Toy citation batch 1 verification execution count']}")
    print(f"Verified source count: {counters['Toy citation batch 1 verified source count']}")
    print(f"Acceptance decision count: {counters['Toy citation batch 1 acceptance decision count']}")
    print(f"Rejection decision count: {counters['Toy citation batch 1 rejection decision count']}")
    print(f"Accepted source count: {counters['Toy citation batch 1 accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation batch 1 rejected source count']}")
    print(f"Blocked source count: {counters['Toy citation batch 1 blocked source count']}")
    print(f"Actual citation count: {counters['Toy citation batch 1 actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation batch 1 fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation batch 1 citation integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation batch 1 added to manuscript count']}")
    print(f"Manuscript mutation count: {counters['Toy citation batch 1 manuscript mutation count']}")
    print(f"Book source count: {counters['Toy citation batch 1 source book count']}")
    print(f"Article source count: {counters['Toy citation batch 1 source article count']}")
    print(f"DOI locator count: {counters['Toy citation batch 1 source DOI locator count']}")
    print(f"ISBN locator count: {counters['Toy citation batch 1 source ISBN locator count']}")
    print(f"Toy citation source retrieval execution count: {counters['Toy citation source retrieval execution count']}")
    print(f"Toy citation candidate source retrieval count: {counters['Toy citation candidate source retrieval count']}")
    print(f"Toy citation actual citation count: {counters['Toy citation actual citation count']}")
    print(f"Toy citation verified source count: {counters['Toy citation verified source count']}")
    print(f"Toy citation fabricated reference count: {counters['Toy citation fabricated reference count']}")
    print(f"Toy citation integration completion count: {counters['Toy citation integration completion count']}")
    print(f"Toy citation added to manuscript count: {counters['Toy citation added to manuscript count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
