"""Experiment 55: First Search Run Artifact.

This experiment runs the v5.5 first search-run artifact generator.

It verifies that the project can instantiate one controlled search-run shell
without executing a live search, adding sources, adding citations, populating
the evidence matrix, revising the manuscript, or implying submission readiness.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_search_run_artifact import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Search Run Artifact v5.5",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "No live search is executed by this artifact",
    "No source is added by this artifact",
    "No citation is added by this artifact",
    "The evidence matrix is not populated by this artifact",
    "The manuscript is not revised by this artifact",
    "Citation placeholders are not citations",
    "Source Artifacts",
    "First Search Run Shell",
    "Run Shell Fields",
    "Pending Field Values",
    "Execution Gates",
    "Inclusion Criteria Links",
    "Exclusion Criteria Links",
    "Audit Checks for Next Milestone",
    "Artifact Logic",
    "Evidence Boundary",
    "Run shell count",
    "Executed search count",
    "Search run count",
    "Candidate source count",
    "Retained source count",
    "Source added count",
    "Citation added count",
    "Evidence matrix populated count",
    "Manuscript revised count",
    "does not execute a live search",
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

    if result.run_shell_count != 1:
        errors.append(f"Run shell count should be one, got: {result.run_shell_count}")

    if result.executed_search_count != 0:
        errors.append(f"Executed search count should be zero, got: {result.executed_search_count}")

    if result.run_shell_field_count < 18:
        errors.append(f"Run shell field count too low: {result.run_shell_field_count}")

    if result.pending_field_count < 8:
        errors.append(f"Pending field count too low: {result.pending_field_count}")

    if result.execution_gate_count < 12:
        errors.append(f"Execution gate count too low: {result.execution_gate_count}")

    if result.inclusion_link_count < 8:
        errors.append(f"Inclusion link count too low: {result.inclusion_link_count}")

    if result.exclusion_link_count < 8:
        errors.append(f"Exclusion link count too low: {result.exclusion_link_count}")

    if result.audit_check_count < 10:
        errors.append(f"Audit check count too low: {result.audit_check_count}")

    if result.boundary_phrase_count < 13:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 10:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    for label, value in [
        ("Search run count", result.search_run_count),
        ("Candidate source count", result.candidate_source_count),
        ("Retained source count", result.retained_source_count),
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
        errors.append(f"Word count too low for first search run artifact: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 55: First Search Run Artifact")
    print(
        "Question: Can Viruse Fabric instantiate one controlled first-search run "
        "shell without executing live search, adding sources, citations, evidence "
        "rows, or manuscript revisions?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Run shell count: {result.run_shell_count}")
    print(f"Executed search count: {result.executed_search_count}")
    print(f"Run shell field count: {result.run_shell_field_count}")
    print(f"Pending field count: {result.pending_field_count}")
    print(f"Execution gate count: {result.execution_gate_count}")
    print(f"Inclusion link count: {result.inclusion_link_count}")
    print(f"Exclusion link count: {result.exclusion_link_count}")
    print(f"Audit check count: {result.audit_check_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Search run count: {result.search_run_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
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

    print("Experiment 55 completed successfully.")


if __name__ == "__main__":
    main()
