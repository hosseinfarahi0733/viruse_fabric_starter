"""Experiment 63: First Retained Source Decision Plan.

This experiment runs the v6.3 first retained source decision plan generator.

It verifies that the project can plan retained-source decisions while keeping
retention execution, retained sources, citations, evidence matrix population,
and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_retained_source_decision_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Retained Source Decision Plan v6.3",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does plan retained source decisions",
    "does not execute retention decisions",
    "does not create retained sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "retained source decision plan is not retained source creation",
    "retention planning is not retention execution",
    "metadata pass is not source retention",
    "conditional metadata pass is not source retention",
    "candidate source entries are not retained sources",
    "retained sources are not citations",
    "citations are not external validation",
    "Source Artifacts",
    "Retained Source Decision Plan Metadata",
    "Planned Retention Decision Rows",
    "Retention Criteria",
    "Retention Decision Values",
    "Retention Plan Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Retention Plan Interpretation",
    "Planning Boundary",
    "Retention Boundary",
    "Evidence Boundary",
    "Retention Decision Consequence Boundary",
    "Plan Failure Modes Prevented",
    "Retained source decision plan count",
    "Candidate source count",
    "Metadata audit pass count",
    "Metadata audit conditional pass count",
    "Planned retention candidate count",
    "Conditional hold count",
    "Retention decision execution count",
    "Retained source count",
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

    if result.source_artifact_count < 13:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.retained_source_decision_plan_count != 1:
        errors.append(
            "Retained source decision plan count should be one, got: "
            f"{result.retained_source_decision_plan_count}"
        )

    if result.candidate_source_count != 3:
        errors.append(f"Candidate source count should be three, got: {result.candidate_source_count}")

    if result.metadata_audit_pass_count != 2:
        errors.append(
            "Metadata audit pass count should be two, got: "
            f"{result.metadata_audit_pass_count}"
        )

    if result.metadata_audit_conditional_pass_count != 1:
        errors.append(
            "Metadata audit conditional pass count should be one, got: "
            f"{result.metadata_audit_conditional_pass_count}"
        )

    if result.planned_retention_candidate_count != 2:
        errors.append(
            "Planned retention candidate count should be two, got: "
            f"{result.planned_retention_candidate_count}"
        )

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.planned_retention_candidate_count + result.conditional_hold_count != result.candidate_source_count:
        errors.append("Planned retention and hold counts do not sum to candidate source count")

    for label, value in [
        ("Retention decision execution count", result.retention_decision_execution_count),
        ("Retained source count", result.retained_source_count),
        ("Citation added count", result.citation_added_count),
        ("Evidence matrix populated count", result.evidence_matrix_populated_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.retention_criteria_count < 14:
        errors.append(f"Retention criteria count too low: {result.retention_criteria_count}")

    if result.retention_decision_value_count < 4:
        errors.append(
            f"Retention decision value count too low: {result.retention_decision_value_count}"
        )

    if result.retention_plan_gate_count < 12:
        errors.append(f"Retention plan gate count too low: {result.retention_plan_gate_count}")

    if result.boundary_phrase_count < 20:
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
        errors.append(
            f"Word count too low for first retained source decision plan: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 63: First Retained Source Decision Plan")
    print(
        "Question: Can Viruse Fabric plan retained-source decisions while keeping "
        "retention execution, retained sources, citations, evidence matrix population, "
        "and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Retained source decision plan count: {result.retained_source_decision_plan_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Metadata audit pass count: {result.metadata_audit_pass_count}")
    print(f"Metadata audit conditional pass count: {result.metadata_audit_conditional_pass_count}")
    print(f"Planned retention candidate count: {result.planned_retention_candidate_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Retention decision execution count: {result.retention_decision_execution_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Retention criteria count: {result.retention_criteria_count}")
    print(f"Retention decision value count: {result.retention_decision_value_count}")
    print(f"Retention plan gate count: {result.retention_plan_gate_count}")
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

    print("Experiment 63 completed successfully.")


if __name__ == "__main__":
    main()
