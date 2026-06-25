"""Experiment 53: Empty Search Log Audit.

This experiment runs the v5.3 empty search log audit.

It verifies that the v5.2 empty literature search log remains a controlled
baseline with zero search runs, zero sources, zero citations, zero evidence
matrix population, and zero manuscript revision.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.empty_search_log_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Empty Search Log Audit v5.3",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does not run searches",
    "does not add sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "Citation placeholders are not citations",
    "Source Artifacts",
    "Required Section Audit",
    "Zero Count Audit",
    "Audit Dimensions",
    "Audit Findings",
    "Audit Rules",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Empty-State Interpretation",
    "Transition Readiness",
    "Audit Consequences",
    "Failure Modes Prevented",
    "Source added count",
    "Citation added count",
    "Search run added count",
    "Evidence matrix populated count",
    "Manuscript revised count",
    "zero search runs",
    "zero sources",
    "zero citations",
    "zero evidence matrix population",
    "zero manuscript revision",
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

    if result.source_artifact_count < 4:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if not result.empty_log_exists:
        errors.append("Empty log artifact should exist")

    if not result.template_exists:
        errors.append("Template artifact should exist")

    if result.required_section_count < 12:
        errors.append(f"Required section count too low: {result.required_section_count}")

    if result.missing_required_section_count != 0:
        errors.append(
            f"Missing required section count should be zero, got: {result.missing_required_section_count}"
        )

    if result.zero_count_field_count < 9:
        errors.append(f"Zero count field count too low: {result.zero_count_field_count}")

    if result.zero_count_pass_count < result.zero_count_field_count:
        errors.append(
            f"Zero count pass count should equal zero count field count, got: "
            f"{result.zero_count_pass_count}/{result.zero_count_field_count}"
        )

    if result.zero_count_fail_count != 0:
        errors.append(f"Zero count fail count should be zero, got: {result.zero_count_fail_count}")

    if result.audit_dimension_count < 12:
        errors.append(f"Audit dimension count too low: {result.audit_dimension_count}")

    if result.audit_finding_count < 12:
        errors.append(f"Audit finding count too low: {result.audit_finding_count}")

    if result.boundary_phrase_count < 12:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.audit_rule_count < 10:
        errors.append(f"Audit rule count too low: {result.audit_rule_count}")

    if result.prohibited_behavior_count < 10:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    for label, value in [
        ("Source added count", result.source_added_count),
        ("Citation added count", result.citation_added_count),
        ("Search run added count", result.search_run_added_count),
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

    if result.word_count < 1100:
        errors.append(f"Word count too low for empty search log audit: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 53: Empty Search Log Audit")
    print(
        "Question: Can Viruse Fabric audit the empty literature search log as a "
        "controlled baseline without adding searches, sources, citations, evidence "
        "rows, or manuscript revisions?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Empty log exists: {result.empty_log_exists}")
    print(f"Template exists: {result.template_exists}")
    print(f"Required section count: {result.required_section_count}")
    print(f"Missing required section count: {result.missing_required_section_count}")
    print(f"Zero count field count: {result.zero_count_field_count}")
    print(f"Zero count pass count: {result.zero_count_pass_count}")
    print(f"Zero count fail count: {result.zero_count_fail_count}")
    print(f"Audit dimension count: {result.audit_dimension_count}")
    print(f"Audit finding count: {result.audit_finding_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Audit rule count: {result.audit_rule_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Search run added count: {result.search_run_added_count}")
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

    print("Experiment 53 completed successfully.")


if __name__ == "__main__":
    main()
