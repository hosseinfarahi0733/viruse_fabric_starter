"""Experiment 65: First Retained Source Role Audit.

This experiment runs the v6.5 first retained source role audit generator.

It verifies that the project can audit the roles of two retained source records
while keeping citations, evidence matrix population, and manuscript revision at
zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_retained_source_role_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Retained Source Role Audit v6.5",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does audit retained source roles",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "role pass is not citation readiness",
    "role pass is not external validation",
    "role audit is not evidence matrix population",
    "role audit is not manuscript revision",
    "retained source roles are not citations",
    "citations are not external validation",
    "conditional hold remains outside role audit",
    "future use is bounded",
    "Source Artifacts",
    "Retained Source Role Audit Metadata",
    "Role Audit Rows",
    "Conditional Hold Rows",
    "Role Audit Fields",
    "Role Decision Values",
    "Role Audit Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Role Audit Interpretation",
    "Role Boundary",
    "Citation Boundary",
    "Evidence Boundary",
    "Conditional Hold Boundary",
    "Retained source role audit count",
    "Retained source count",
    "Retained source audited count",
    "Source role pass count",
    "Source role conditional count",
    "Source role fail count",
    "Conditional hold count",
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

    if result.source_artifact_count < 15:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.retained_source_role_audit_count != 1:
        errors.append(
            "Retained source role audit count should be one, got: "
            f"{result.retained_source_role_audit_count}"
        )

    if result.retained_source_count != 2:
        errors.append(f"Retained source count should be two, got: {result.retained_source_count}")

    if result.retained_source_audited_count != 2:
        errors.append(
            "Retained source audited count should be two, got: "
            f"{result.retained_source_audited_count}"
        )

    if result.source_role_pass_count != 2:
        errors.append(f"Source role pass count should be two, got: {result.source_role_pass_count}")

    if result.source_role_conditional_count != 0:
        errors.append(
            "Source role conditional count should be zero, got: "
            f"{result.source_role_conditional_count}"
        )

    if result.source_role_fail_count != 0:
        errors.append(f"Source role fail count should be zero, got: {result.source_role_fail_count}")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.retained_source_audited_count != result.retained_source_count:
        errors.append("Retained source audited count must equal retained source count")

    for label, value in [
        ("Citation added count", result.citation_added_count),
        ("Evidence matrix populated count", result.evidence_matrix_populated_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.role_audit_field_count < 12:
        errors.append(f"Role audit field count too low: {result.role_audit_field_count}")

    if result.role_decision_value_count < 4:
        errors.append(f"Role decision value count too low: {result.role_decision_value_count}")

    if result.role_audit_gate_count < 13:
        errors.append(f"Role audit gate count too low: {result.role_audit_gate_count}")

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
        errors.append(f"Word count too low for first retained source role audit: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 65: First Retained Source Role Audit")
    print(
        "Question: Can Viruse Fabric audit retained-source roles while keeping "
        "citations, evidence matrix population, and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Retained source role audit count: {result.retained_source_role_audit_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Retained source audited count: {result.retained_source_audited_count}")
    print(f"Source role pass count: {result.source_role_pass_count}")
    print(f"Source role conditional count: {result.source_role_conditional_count}")
    print(f"Source role fail count: {result.source_role_fail_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Role audit field count: {result.role_audit_field_count}")
    print(f"Role decision value count: {result.role_decision_value_count}")
    print(f"Role audit gate count: {result.role_audit_gate_count}")
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

    print("Experiment 65 completed successfully.")


if __name__ == "__main__":
    main()
