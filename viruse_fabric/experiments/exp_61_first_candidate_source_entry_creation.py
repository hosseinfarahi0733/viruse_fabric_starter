"""Experiment 61: First Candidate Source Entry Creation.

This experiment runs the v6.1 first candidate source entry creation generator.

It verifies that the project can create three candidate source entries from the
v5.9 pass-to-candidate-planning decisions while keeping retained sources,
citations, evidence matrix population, and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_candidate_source_entry_creation import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Candidate Source Entry Creation v6.1",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does create candidate source entries",
    "does not retain sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "candidate source entries are not retained sources",
    "candidate source entries are not citations",
    "candidate source entries are not external validation",
    "retained sources are not citations",
    "citations are not external validation",
    "Source Artifacts",
    "Candidate Entry Creation Metadata",
    "Candidate Source Entries Created",
    "Deferred Raw Observations Not Created as Candidate Sources",
    "Candidate Entry Fields",
    "Candidate Audit Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Candidate Entry Interpretation",
    "Metadata Integrity Boundary",
    "Retention Boundary",
    "Candidate entry creation count",
    "Candidate source count",
    "Deferred source count",
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

    if result.source_artifact_count < 11:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.candidate_entry_creation_count != 1:
        errors.append(
            "Candidate entry creation count should be one, got: "
            f"{result.candidate_entry_creation_count}"
        )

    if result.candidate_source_count != 3:
        errors.append(f"Candidate source count should be three, got: {result.candidate_source_count}")

    if result.deferred_source_count != 2:
        errors.append(f"Deferred source count should be two, got: {result.deferred_source_count}")

    if result.source_added_count != 3:
        errors.append(
            "Source added count should be three candidate entries, got: "
            f"{result.source_added_count}"
        )

    for label, value in [
        ("Retained source count", result.retained_source_count),
        ("Citation added count", result.citation_added_count),
        ("Evidence matrix populated count", result.evidence_matrix_populated_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.candidate_entry_field_count < 16:
        errors.append(f"Candidate entry field count too low: {result.candidate_entry_field_count}")

    if result.candidate_audit_gate_count < 14:
        errors.append(f"Candidate audit gate count too low: {result.candidate_audit_gate_count}")

    if result.boundary_phrase_count < 18:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 11:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 9:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(
            f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}"
        )

    if result.word_count < 1200:
        errors.append(
            f"Word count too low for first candidate source entry creation: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 61: First Candidate Source Entry Creation")
    print(
        "Question: Can Viruse Fabric create first candidate source entries while "
        "keeping retained sources, citations, evidence matrix population, and "
        "manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Candidate entry creation count: {result.candidate_entry_creation_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Deferred source count: {result.deferred_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Candidate entry field count: {result.candidate_entry_field_count}")
    print(f"Candidate audit gate count: {result.candidate_audit_gate_count}")
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

    print("Experiment 61 completed successfully.")


if __name__ == "__main__":
    main()
