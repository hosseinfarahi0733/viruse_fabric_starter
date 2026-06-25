"""Experiment 62: Candidate Source Metadata Audit.

This experiment runs the v6.2 candidate source metadata audit generator.

It verifies that the project can audit metadata for three candidate source
entries while keeping retained sources, citations, evidence matrix population,
and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.candidate_source_metadata_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Candidate Source Metadata Audit v6.2",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does audit candidate metadata",
    "does not retain sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "metadata audit is not source retention",
    "metadata pass is not source retention",
    "conditional metadata pass is not source retention",
    "candidate source entries are not retained sources",
    "candidate source entries are not citations",
    "retained sources are not citations",
    "citations are not external validation",
    "Source Artifacts",
    "Candidate Metadata Audit Metadata",
    "Candidate Metadata Audit Rows",
    "Metadata Field Checks",
    "Audit Decision Values",
    "Retention Gates Not Executed",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Metadata Audit Interpretation",
    "Retention Boundary",
    "Evidence Boundary",
    "Audit Consequence Boundary",
    "Candidate Audit Failure Modes Prevented",
    "Candidate metadata audit count",
    "Candidate source count",
    "Candidate source audited count",
    "Metadata audit pass count",
    "Metadata audit conditional pass count",
    "Metadata audit fail count",
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

    if result.source_artifact_count < 12:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.candidate_metadata_audit_count != 1:
        errors.append(
            "Candidate metadata audit count should be one, got: "
            f"{result.candidate_metadata_audit_count}"
        )

    if result.candidate_source_count != 3:
        errors.append(f"Candidate source count should be three, got: {result.candidate_source_count}")

    if result.candidate_source_audited_count != 3:
        errors.append(
            "Candidate source audited count should be three, got: "
            f"{result.candidate_source_audited_count}"
        )

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

    if result.metadata_audit_fail_count != 0:
        errors.append(
            "Metadata audit fail count should be zero, got: "
            f"{result.metadata_audit_fail_count}"
        )

    if (
        result.metadata_audit_pass_count
        + result.metadata_audit_conditional_pass_count
        + result.metadata_audit_fail_count
        != result.candidate_source_audited_count
    ):
        errors.append("Metadata audit decision counts do not sum to audited candidate source count")

    for label, value in [
        ("Retained source count", result.retained_source_count),
        ("Citation added count", result.citation_added_count),
        ("Evidence matrix populated count", result.evidence_matrix_populated_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.audit_field_check_count < 16:
        errors.append(f"Audit field check count too low: {result.audit_field_check_count}")

    if result.audit_decision_value_count < 4:
        errors.append(f"Audit decision value count too low: {result.audit_decision_value_count}")

    if result.retention_gate_not_executed_count < 10:
        errors.append(
            "Retention gate not executed count too low: "
            f"{result.retention_gate_not_executed_count}"
        )

    if result.boundary_phrase_count < 20:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 11:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 10:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(
            f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}"
        )

    if result.word_count < 1200:
        errors.append(f"Word count too low for candidate source metadata audit: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 62: Candidate Source Metadata Audit")
    print(
        "Question: Can Viruse Fabric audit candidate source metadata while keeping "
        "retained sources, citations, evidence matrix population, and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Candidate metadata audit count: {result.candidate_metadata_audit_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Candidate source audited count: {result.candidate_source_audited_count}")
    print(f"Metadata audit pass count: {result.metadata_audit_pass_count}")
    print(f"Metadata audit conditional pass count: {result.metadata_audit_conditional_pass_count}")
    print(f"Metadata audit fail count: {result.metadata_audit_fail_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Audit field check count: {result.audit_field_check_count}")
    print(f"Audit decision value count: {result.audit_decision_value_count}")
    print(f"Retention gate not executed count: {result.retention_gate_not_executed_count}")
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

    print("Experiment 62 completed successfully.")


if __name__ == "__main__":
    main()
