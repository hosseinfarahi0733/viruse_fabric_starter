"""Experiment 52: Empty Literature Search Log.

This experiment runs the v5.2 empty literature search log generator.

It verifies that the project can instantiate a real empty literature search log
artifact without running searches, adding sources, adding citations, populating
the evidence matrix, revising the manuscript, or implying submission readiness.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.empty_literature_search_log import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Empty Literature Search Log v5.2",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "No search is run by this artifact",
    "No source is added by this artifact",
    "No citation is added by this artifact",
    "The evidence matrix is not populated by this artifact",
    "The manuscript is not revised by this artifact",
    "Citation placeholders are not citations",
    "Source Artifacts",
    "Empty Registry Summary",
    "Empty Search Run Columns",
    "Empty Candidate Source Columns",
    "Empty Claim Mapping Columns",
    "Initial Status Values",
    "Log Rules",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Empty-State Audit Meaning",
    "Evidence Discipline",
    "Search run count",
    "Candidate source count",
    "Retained source count",
    "Deferred source count",
    "Rejected source count",
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

    if result.source_artifact_count < 5:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.empty_registry_count < 8:
        errors.append(f"Empty registry count too low: {result.empty_registry_count}")

    if result.search_run_column_count < 16:
        errors.append(f"Search run column count too low: {result.search_run_column_count}")

    if result.candidate_source_column_count < 16:
        errors.append(
            f"Candidate source column count too low: {result.candidate_source_column_count}"
        )

    if result.claim_mapping_column_count < 11:
        errors.append(f"Claim mapping column count too low: {result.claim_mapping_column_count}")

    if result.initial_status_value_count < 7:
        errors.append(f"Initial status value count too low: {result.initial_status_value_count}")

    if result.log_rule_count < 10:
        errors.append(f"Log rule count too low: {result.log_rule_count}")

    if result.boundary_phrase_count < 13:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 12:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    for label, value in [
        ("Search run count", result.search_run_count),
        ("Candidate source count", result.candidate_source_count),
        ("Retained source count", result.retained_source_count),
        ("Deferred source count", result.deferred_source_count),
        ("Rejected source count", result.rejected_source_count),
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
        errors.append(f"Word count too low for empty literature search log: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 52: Empty Literature Search Log")
    print(
        "Question: Can Viruse Fabric instantiate a real empty literature search "
        "log without running searches, adding sources, citations, evidence rows, "
        "or manuscript revisions?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Empty registry count: {result.empty_registry_count}")
    print(f"Search run column count: {result.search_run_column_count}")
    print(f"Candidate source column count: {result.candidate_source_column_count}")
    print(f"Claim mapping column count: {result.claim_mapping_column_count}")
    print(f"Initial status value count: {result.initial_status_value_count}")
    print(f"Log rule count: {result.log_rule_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Search run count: {result.search_run_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Deferred source count: {result.deferred_source_count}")
    print(f"Rejected source count: {result.rejected_source_count}")
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

    print("Experiment 52 completed successfully.")


if __name__ == "__main__":
    main()
