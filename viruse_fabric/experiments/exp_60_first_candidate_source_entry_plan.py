"""Experiment 60: First Candidate Source Entry Plan.

This experiment runs the v6.0 first candidate source entry plan generator.

It verifies that the project can plan candidate source entry after screening
execution while keeping candidate sources, retained sources, citations, evidence
matrix population, and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_candidate_source_entry_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Candidate Source Entry Plan v6.0",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "candidate source entry plan is not candidate source creation",
    "candidate source planning is not source retention",
    "candidate sources are not retained sources",
    "retained sources are not citations",
    "citations are not external validation",
    "does not create candidate sources",
    "does not retain sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "Source Artifacts",
    "Candidate Entry Plan Metadata",
    "Planned Candidate Entry Rows",
    "Required Candidate Metadata Fields",
    "Candidate Status Values",
    "Proposed Source Role Values",
    "Entry Creation Gates",
    "Metadata Audit Requirements",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Candidate Entry Interpretation",
    "Metadata Boundary",
    "Retention Boundary",
    "Candidate entry plan count",
    "Planned candidate entry row count",
    "Pass to candidate planning count",
    "Defer to candidate planning count",
    "Candidate source count",
    "Retained source count",
    "Source added count",
    "Citation added count",
    "Evidence matrix populated count",
    "Manuscript revised count",
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

    if result.source_artifact_count < 10:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.candidate_entry_plan_count != 1:
        errors.append(
            f"Candidate entry plan count should be one, got: {result.candidate_entry_plan_count}"
        )

    if result.planned_candidate_entry_row_count != 5:
        errors.append(
            "Planned candidate entry row count should be five, got: "
            f"{result.planned_candidate_entry_row_count}"
        )

    if result.pass_to_candidate_planning_count != 3:
        errors.append(
            "Pass to candidate planning count should be three, got: "
            f"{result.pass_to_candidate_planning_count}"
        )

    if result.defer_to_candidate_planning_count != 2:
        errors.append(
            "Defer to candidate planning count should be two, got: "
            f"{result.defer_to_candidate_planning_count}"
        )

    for label, value in [
        ("Candidate source count", result.candidate_source_count),
        ("Retained source count", result.retained_source_count),
        ("Source added count", result.source_added_count),
        ("Citation added count", result.citation_added_count),
        ("Evidence matrix populated count", result.evidence_matrix_populated_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.required_metadata_field_count < 16:
        errors.append(
            f"Required metadata field count too low: {result.required_metadata_field_count}"
        )

    if result.candidate_status_value_count < 5:
        errors.append(
            f"Candidate status value count too low: {result.candidate_status_value_count}"
        )

    if result.proposed_source_role_count < 6:
        errors.append(f"Proposed source role count too low: {result.proposed_source_role_count}")

    if result.entry_creation_gate_count < 12:
        errors.append(f"Entry creation gate count too low: {result.entry_creation_gate_count}")

    if result.metadata_audit_requirement_count < 12:
        errors.append(
            "Metadata audit requirement count too low: "
            f"{result.metadata_audit_requirement_count}"
        )

    if result.boundary_phrase_count < 17:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 11:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(
            f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}"
        )

    if result.word_count < 1200:
        errors.append(f"Word count too low for first candidate source entry plan: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 60: First Candidate Source Entry Plan")
    print(
        "Question: Can Viruse Fabric plan the first candidate source entry workflow "
        "after screening execution without creating candidate sources, retaining "
        "sources, adding citations, populating the evidence matrix, or revising the manuscript?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Candidate entry plan count: {result.candidate_entry_plan_count}")
    print(f"Planned candidate entry row count: {result.planned_candidate_entry_row_count}")
    print(f"Pass to candidate planning count: {result.pass_to_candidate_planning_count}")
    print(f"Defer to candidate planning count: {result.defer_to_candidate_planning_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Required metadata field count: {result.required_metadata_field_count}")
    print(f"Candidate status value count: {result.candidate_status_value_count}")
    print(f"Proposed source role count: {result.proposed_source_role_count}")
    print(f"Entry creation gate count: {result.entry_creation_gate_count}")
    print(f"Metadata audit requirement count: {result.metadata_audit_requirement_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
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

    print("Experiment 60 completed successfully.")


if __name__ == "__main__":
    main()
