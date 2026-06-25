"""Experiment 58: First Raw Result Screening Plan.

This experiment runs the v5.8 first raw-result screening plan generator.

It verifies that the project can plan screening for raw results observed in v5.7
without executing screening, creating candidate sources, retaining sources,
adding citations, populating the evidence matrix, or revising the manuscript.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_raw_result_screening_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Raw Result Screening Plan v5.8",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "screening plan, not screening execution",
    "does not create candidate sources",
    "does not retain sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "Source Artifacts",
    "Screening Plan Metadata",
    "Raw Observations to Be Screened Later",
    "Screening Fields",
    "Planned Screening Rows",
    "Inclusion Criteria",
    "Exclusion Criteria",
    "Screening Steps",
    "Screening Recommendation Values",
    "Screening Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Screening Interpretation",
    "Screening Boundary",
    "Candidate Boundary",
    "Raw result count",
    "Raw result observation count",
    "Screening plan count",
    "Screening execution count",
    "Screened result count",
    "Candidate source count",
    "Retained source count",
    "Source added count",
    "Citation added count",
    "Evidence matrix populated count",
    "Manuscript revised count",
    "raw results are not candidate sources",
    "candidate sources are not retained sources",
    "retained sources are not citations",
    "citations are not external validation",
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

    if result.source_artifact_count < 8:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.raw_result_count < 1:
        errors.append(f"Raw result count should be positive, got: {result.raw_result_count}")

    if result.raw_result_observation_count < 5:
        errors.append(
            f"Raw result observation count too low: {result.raw_result_observation_count}"
        )

    if result.screening_plan_count != 1:
        errors.append(f"Screening plan count should be one, got: {result.screening_plan_count}")

    if result.screening_execution_count != 0:
        errors.append(
            f"Screening execution count should be zero, got: {result.screening_execution_count}"
        )

    if result.screening_field_count < 12:
        errors.append(f"Screening field count too low: {result.screening_field_count}")

    if result.inclusion_criteria_count < 8:
        errors.append(f"Inclusion criteria count too low: {result.inclusion_criteria_count}")

    if result.exclusion_criteria_count < 8:
        errors.append(f"Exclusion criteria count too low: {result.exclusion_criteria_count}")

    if result.screening_step_count < 10:
        errors.append(f"Screening step count too low: {result.screening_step_count}")

    if result.screening_recommendation_value_count < 5:
        errors.append(
            "Screening recommendation value count too low: "
            f"{result.screening_recommendation_value_count}"
        )

    if result.screening_row_count < 5:
        errors.append(f"Screening row count too low: {result.screening_row_count}")

    if result.screening_gate_count < 12:
        errors.append(f"Screening gate count too low: {result.screening_gate_count}")

    for label, value in [
        ("Screened result count", result.screened_result_count),
        ("Candidate source count", result.candidate_source_count),
        ("Retained source count", result.retained_source_count),
        ("Source added count", result.source_added_count),
        ("Citation added count", result.citation_added_count),
        ("Evidence matrix populated count", result.evidence_matrix_populated_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.boundary_phrase_count < 16:
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
        errors.append(f"Word count too low for first raw result screening plan: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 58: First Raw Result Screening Plan")
    print(
        "Question: Can Viruse Fabric plan the first raw-result screening step "
        "without executing screening, creating candidate sources, retaining sources, "
        "adding citations, populating the evidence matrix, or revising the manuscript?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Raw result count: {result.raw_result_count}")
    print(f"Raw result observation count: {result.raw_result_observation_count}")
    print(f"Screening plan count: {result.screening_plan_count}")
    print(f"Screening execution count: {result.screening_execution_count}")
    print(f"Screening field count: {result.screening_field_count}")
    print(f"Inclusion criteria count: {result.inclusion_criteria_count}")
    print(f"Exclusion criteria count: {result.exclusion_criteria_count}")
    print(f"Screening step count: {result.screening_step_count}")
    print(f"Screening recommendation value count: {result.screening_recommendation_value_count}")
    print(f"Screening row count: {result.screening_row_count}")
    print(f"Screening gate count: {result.screening_gate_count}")
    print(f"Screened result count: {result.screened_result_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
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

    print("Experiment 58 completed successfully.")


if __name__ == "__main__":
    main()
