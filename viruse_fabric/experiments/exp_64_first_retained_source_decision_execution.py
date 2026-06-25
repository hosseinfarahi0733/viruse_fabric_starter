"""Experiment 64: First Retained Source Decision Execution.

This experiment runs the v6.4 first retained source decision execution generator.

It verifies that the project can create retained source records from two
metadata-pass candidate sources while keeping citations, evidence matrix
population, and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_retained_source_decision_execution import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Retained Source Decision Execution v6.4",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does create retained source records",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "retained source records are not citations",
    "retained source records are not evidence matrix population",
    "retained source records are not manuscript revision",
    "retained sources are not citations",
    "citations are not external validation",
    "Source Artifacts",
    "Retention Decision Execution Metadata",
    "Retained Source Records Created",
    "Conditional Hold Records",
    "Retained Source Fields",
    "Retention Execution Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Retention Execution Interpretation",
    "Retained Source Boundary",
    "Citation Boundary",
    "Evidence Boundary",
    "Retention Consequence Boundary",
    "Conditional Hold Boundary",
    "Retention decision execution count",
    "Candidate source count",
    "Retained source count",
    "Conditional hold count",
    "Source added count",
    "Citation added count",
    "Evidence matrix populated count",
    "Manuscript revised count",
    "RET-0001",
    "RET-0002",
    "CAND-0003",
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

    if result.source_artifact_count < 14:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.retention_decision_execution_count != 1:
        errors.append(
            "Retention decision execution count should be one, got: "
            f"{result.retention_decision_execution_count}"
        )

    if result.candidate_source_count != 3:
        errors.append(f"Candidate source count should be three, got: {result.candidate_source_count}")

    if result.retained_source_count != 2:
        errors.append(f"Retained source count should be two, got: {result.retained_source_count}")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.retained_source_count + result.conditional_hold_count != result.candidate_source_count:
        errors.append("Retained source and hold counts do not sum to candidate source count")

    if result.source_added_count != 2:
        errors.append(f"Source added count should be two, got: {result.source_added_count}")

    for label, value in [
        ("Citation added count", result.citation_added_count),
        ("Evidence matrix populated count", result.evidence_matrix_populated_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.retained_source_field_count < 17:
        errors.append(f"Retained source field count too low: {result.retained_source_field_count}")

    if result.retention_execution_gate_count < 13:
        errors.append(
            f"Retention execution gate count too low: {result.retention_execution_gate_count}"
        )

    if result.boundary_phrase_count < 18:
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
            f"Word count too low for first retained source decision execution: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 64: First Retained Source Decision Execution")
    print(
        "Question: Can Viruse Fabric create retained source records while keeping "
        "citations, evidence matrix population, and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Retention decision execution count: {result.retention_decision_execution_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Retained source field count: {result.retained_source_field_count}")
    print(f"Retention execution gate count: {result.retention_execution_gate_count}")
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

    print("Experiment 64 completed successfully.")


if __name__ == "__main__":
    main()
