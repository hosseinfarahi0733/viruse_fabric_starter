"""Experiment 54: First Literature Family Search Plan.

This experiment runs the v5.4 first literature family search plan.

It verifies that the project can select the first literature family and define
controlled future search parameters without running searches, adding sources,
adding citations, populating the evidence matrix, revising the manuscript, or
implying submission readiness.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_literature_family_search_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Literature Family Search Plan v5.4",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "No search is run by this plan",
    "No source is added by this plan",
    "No citation is added by this plan",
    "The evidence matrix is not populated by this plan",
    "The manuscript is not revised by this plan",
    "Citation placeholders are not citations",
    "Source Artifacts",
    "Selected Literature Family",
    "Planned Search Venues",
    "Planned Query Strings",
    "Claim Categories for First Search",
    "Inclusion Criteria",
    "Exclusion Criteria",
    "Search Run Fields to Fill Later",
    "Candidate Screening Steps",
    "First Search Run Gates",
    "Planning Logic",
    "Search Discipline",
    "Search run count",
    "Source added count",
    "Citation added count",
    "Evidence matrix populated count",
    "Manuscript revised count",
    "does not run searches",
    "does not add sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "biological, clinical, laboratory, or operational guidance",
]


def missing_required_report_phrases(report_path: Path) -> list[str]:
    if not report_path.exists():
        return REQUIRED_REPORT_PHRASES[:]

    text = report_path.read_text(encoding="utf-8").lower()
    return [phrase for phrase in REQUIRED_REPORT_PHRASES if phrase.lower() not in text]


def main() -> None:
    result = generate_report()
    missing_phrases = missing_required_report_phrases(result.output_path)

    errors: list[str] = []
    warnings: list[str] = list(result.warnings)

    if result.source_artifact_count < 6:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.selected_family_count != 1:
        errors.append(f"Selected family count should be one, got: {result.selected_family_count}")

    if result.planned_venue_count < 8:
        errors.append(f"Planned venue count too low: {result.planned_venue_count}")

    if result.planned_query_count < 10:
        errors.append(f"Planned query count too low: {result.planned_query_count}")

    if result.claim_category_count < 6:
        errors.append(f"Claim category count too low: {result.claim_category_count}")

    if result.inclusion_criteria_count < 8:
        errors.append(f"Inclusion criteria count too low: {result.inclusion_criteria_count}")

    if result.exclusion_criteria_count < 8:
        errors.append(f"Exclusion criteria count too low: {result.exclusion_criteria_count}")

    if result.search_run_field_count < 16:
        errors.append(f"Search run field count too low: {result.search_run_field_count}")

    if result.screening_step_count < 8:
        errors.append(f"Screening step count too low: {result.screening_step_count}")

    if result.search_run_gate_count < 10:
        errors.append(f"Search run gate count too low: {result.search_run_gate_count}")

    if result.boundary_phrase_count < 13:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 10:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    for label, value in [
        ("Search run count", result.search_run_count),
        ("Source added count", result.source_added_count),
        ("Citation added count", result.citation_added_count),
        ("Evidence matrix populated count", result.evidence_matrix_populated_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(
            f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}"
        )

    if result.word_count < 1200:
        errors.append(
            f"Word count too low for first literature family search plan: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 54: First Literature Family Search Plan")
    print(
        "Question: Can Viruse Fabric select the first literature family and define "
        "controlled future search parameters without running searches, adding "
        "sources, citations, evidence rows, or manuscript revisions?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Selected family count: {result.selected_family_count}")
    print(f"Planned venue count: {result.planned_venue_count}")
    print(f"Planned query count: {result.planned_query_count}")
    print(f"Claim category count: {result.claim_category_count}")
    print(f"Inclusion criteria count: {result.inclusion_criteria_count}")
    print(f"Exclusion criteria count: {result.exclusion_criteria_count}")
    print(f"Search run field count: {result.search_run_field_count}")
    print(f"Screening step count: {result.screening_step_count}")
    print(f"Search run gate count: {result.search_run_gate_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Search run count: {result.search_run_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Word count: {result.word_count}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Passed: {passed}")
    print(f"Report exists: {result.output_path.exists()}")
    print(f"Report size: {result.output_path.stat().st_size if result.output_path.exists() else 0}")
    print(f"Missing required report phrases: {len(missing_phrases)}")
    print(f"Interpretation: {result.interpretation}")

    if missing_phrases:
        print("Missing phrases:")
        for phrase in missing_phrases:
            print(f"- {phrase}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if not passed:
        raise SystemExit(1)

    print("Experiment 54 completed successfully.")


if __name__ == "__main__":
    main()
