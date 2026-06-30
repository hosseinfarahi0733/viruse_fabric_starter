from __future__ import annotations

import json

from viruse_fabric.writing.safe_abstract_toy_citation_source_eligibility_and_query_plan import (
    SafeAbstractToyCitationSourceEligibilityAndQueryPlanBuilder,
)


def main() -> None:
    builder = SafeAbstractToyCitationSourceEligibilityAndQueryPlanBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "citation-source-eligibility-and-query-plan-only"
    assert report["plan_phrase"] == (
        "citation_source_eligibility_and_queries_planned_but_no_source_retrieval_performed"
    )

    assert report["citation_source_eligibility_plan_completed"] is True
    assert report["query_plan_completed"] is True
    assert report["source_retrieval_performed"] is False
    assert report["verified_sources_claimed"] is False
    assert report["accepted_sources_recorded"] is False
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

    assert counters["Toy citation source eligibility rule count"] == 12
    assert counters["Toy citation source query plan count"] == 12
    assert counters["Toy citation source exclusion group count"] == 4

    assert counters["Toy citation source retrieval count"] == 0
    assert counters["Toy citation source verified source count"] == 0
    assert counters["Toy citation source accepted source count"] == 0
    assert counters["Toy citation source rejected source count"] == 0
    assert counters["Toy citation source actual citation count"] == 0
    assert counters["Toy citation source fabricated reference count"] == 0
    assert counters["Toy citation source integration completion count"] == 0
    assert counters["Toy citation source added to manuscript count"] == 0

    assert counters["Toy citation source source slot count"] == 12
    assert counters["Toy citation source unresolved slot count"] == 12
    assert counters["Toy citation source slot group count"] == 4
    assert counters["Toy citation source prior actual citation count"] == 0
    assert counters["Toy citation source prior verified source count"] == 0
    assert counters["Toy citation source prior fabricated reference count"] == 0
    assert counters["Toy citation source prior source retrieval count"] == 0
    assert counters["Toy citation source prior integration completion count"] == 0
    assert counters["Toy citation source prior citation added to manuscript count"] == 0

    assert counters["Toy citation source source assembly section count"] == 9
    assert counters["Toy citation source source gap item count"] == 12
    assert counters["Toy citation source source P0 gap count"] == 6
    assert counters["Toy citation source source evidence upgrade completed count"] == 0
    assert counters["Toy citation source source evaluation design module count"] == 10
    assert counters["Toy citation source source actual evaluation run count"] == 0
    assert counters["Toy citation source source validation claim count"] == 0
    assert counters["Toy citation source source coherence improvement item count"] == 10
    assert counters["Toy citation source source coherence rewrite application count"] == 0

    assert counters["Toy citation source eligibility plan execution count"] == 1
    assert counters["Toy citation source eligibility plan direct execution count"] == 1

    combined_text = (
        json.dumps(report["eligibility_rules"], ensure_ascii=False)
        + " "
        + json.dumps(report["query_plans"], ensure_ascii=False)
        + " "
        + json.dumps(report["exclusion_groups"], ensure_ascii=False)
        + " "
        + report["non_readiness_disclaimer"]
    )

    for phrase in [
        "citation source eligibility and query plan",
        "planned eligibility rule only",
        "Query plans are planned search instructions only",
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
        "Future work may only introduce stronger claims",
    ]:
        assert phrase in combined_text, f"Missing eligibility/query phrase: {phrase}"

    must_be_zero = [
        "Toy citation source retrieval count",
        "Toy citation source verified source count",
        "Toy citation source accepted source count",
        "Toy citation source rejected source count",
        "Toy citation source actual citation count",
        "Toy citation source fabricated reference count",
        "Toy citation source integration completion count",
        "Toy citation source added to manuscript count",
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

    print("V8_220_SAFE_ABSTRACT_TOY_CITATION_SOURCE_ELIGIBILITY_AND_QUERY_PLAN_OK")
    print("TOY_CITATION_SOURCE_ELIGIBILITY_AND_QUERY_PLAN_DIRECT_CHECK_OK")
    print(f"Eligibility rule count: {counters['Toy citation source eligibility rule count']}")
    print(f"Query plan count: {counters['Toy citation source query plan count']}")
    print(f"Exclusion group count: {counters['Toy citation source exclusion group count']}")
    print(f"Source retrieval count: {counters['Toy citation source retrieval count']}")
    print(f"Verified source count: {counters['Toy citation source verified source count']}")
    print(f"Accepted source count: {counters['Toy citation source accepted source count']}")
    print(f"Rejected source count: {counters['Toy citation source rejected source count']}")
    print(f"Actual citation count: {counters['Toy citation source actual citation count']}")
    print(f"Fabricated reference count: {counters['Toy citation source fabricated reference count']}")
    print(f"Citation integration completion count: {counters['Toy citation source integration completion count']}")
    print(f"Citation added to manuscript count: {counters['Toy citation source added to manuscript count']}")
    print(f"Source slot count: {counters['Toy citation source source slot count']}")
    print(f"Source unresolved slot count: {counters['Toy citation source unresolved slot count']}")
    print(f"Source slot group count: {counters['Toy citation source slot group count']}")
    print(f"Source assembly section count: {counters['Toy citation source source assembly section count']}")
    print(f"Source gap item count: {counters['Toy citation source source gap item count']}")
    print(f"Source P0 gap count: {counters['Toy citation source source P0 gap count']}")
    print(f"Source evidence upgrade completed count: {counters['Toy citation source source evidence upgrade completed count']}")
    print(f"Source evaluation design module count: {counters['Toy citation source source evaluation design module count']}")
    print(f"Source actual evaluation run count: {counters['Toy citation source source actual evaluation run count']}")
    print(f"Source validation claim count: {counters['Toy citation source source validation claim count']}")
    print(f"Source coherence improvement item count: {counters['Toy citation source source coherence improvement item count']}")
    print(f"Source coherence rewrite application count: {counters['Toy citation source source coherence rewrite application count']}")
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
