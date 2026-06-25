"""Experiment 51: Literature Search Log Template.

This experiment runs the v5.1 literature search log template generator.

It verifies that the project can define a controlled structure for future
literature search logging without adding sources, adding citations, populating
the evidence matrix, revising the manuscript, or implying submission readiness.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.literature_search_log_template import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Literature Search Log Template v5.1",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "No source is added by this template",
    "No citation is added by this template",
    "The evidence matrix is not populated by this template",
    "The manuscript is not revised by this template",
    "Citation placeholders are not citations",
    "Source Artifacts",
    "Search Run Fields",
    "Candidate Source Review Fields",
    "Claim Mapping Fields",
    "Source Status Values",
    "Source Role Values",
    "Decision Values",
    "Empty Search Run Template",
    "Empty Candidate Source Template",
    "Audit Rules",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Relationship to Evidence Matrix",
    "Source added count",
    "Citation added count",
    "Populated source count",
    "Evidence matrix populated count",
    "Manuscript revised count",
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

    if result.search_log_field_count < 16:
        errors.append(f"Search log field count too low: {result.search_log_field_count}")

    if result.source_review_field_count < 14:
        errors.append(f"Source review field count too low: {result.source_review_field_count}")

    if result.claim_mapping_field_count < 10:
        errors.append(f"Claim mapping field count too low: {result.claim_mapping_field_count}")

    if result.source_status_value_count < 6:
        errors.append(f"Source status value count too low: {result.source_status_value_count}")

    if result.source_role_value_count < 6:
        errors.append(f"Source role value count too low: {result.source_role_value_count}")

    if result.decision_value_count < 5:
        errors.append(f"Decision value count too low: {result.decision_value_count}")

    if result.audit_rule_count < 10:
        errors.append(f"Audit rule count too low: {result.audit_rule_count}")

    if result.boundary_phrase_count < 12:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 10:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.source_added_count != 0:
        errors.append(f"Source added count should be zero, got: {result.source_added_count}")

    if result.citation_added_count != 0:
        errors.append(f"Citation added count should be zero, got: {result.citation_added_count}")

    if result.populated_source_count != 0:
        errors.append(f"Populated source count should be zero, got: {result.populated_source_count}")

    if result.evidence_matrix_populated_count != 0:
        errors.append(
            f"Evidence matrix populated count should be zero, got: {result.evidence_matrix_populated_count}"
        )

    if result.manuscript_revised_count != 0:
        errors.append(f"Manuscript revised count should be zero, got: {result.manuscript_revised_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(
            f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}"
        )

    if result.word_count < 1200:
        errors.append(f"Word count too low for literature search log template: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 51: Literature Search Log Template")
    print(
        "Question: Can Viruse Fabric define a controlled future literature search "
        "log without adding sources, citations, evidence rows, or manuscript revisions?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Search log field count: {result.search_log_field_count}")
    print(f"Source review field count: {result.source_review_field_count}")
    print(f"Claim mapping field count: {result.claim_mapping_field_count}")
    print(f"Source status value count: {result.source_status_value_count}")
    print(f"Source role value count: {result.source_role_value_count}")
    print(f"Decision value count: {result.decision_value_count}")
    print(f"Audit rule count: {result.audit_rule_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Populated source count: {result.populated_source_count}")
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

    print("Experiment 51 completed successfully.")


if __name__ == "__main__":
    main()
