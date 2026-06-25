"""Experiment 68: First Evidence Matrix Row Audit.

This experiment runs the v6.8 first evidence matrix row audit generator.

It verifies that the project can audit populated evidence matrix rows while
keeping citations and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_evidence_matrix_row_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Evidence Matrix Row Audit v6.8",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does audit evidence matrix rows",
    "does not add citations",
    "does not revise the manuscript",
    "evidence row pass is not citation readiness",
    "evidence row pass is not manuscript support",
    "evidence row audit is not citation integration",
    "evidence row audit is not manuscript revision",
    "contextual support is not external validation",
    "citations are not external validation",
    "conditional hold remains outside evidence row audit",
    "future citation use is separate",
    "future manuscript revision is separate",
    "Source Artifacts",
    "Evidence Matrix Row Audit Metadata",
    "Evidence Row Audit Rows",
    "Conditional Hold Rows",
    "Row Audit Fields",
    "Row Audit Decision Values",
    "Row Audit Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Row Audit Interpretation",
    "Linkage Boundary",
    "Citation Boundary",
    "Manuscript Boundary",
    "Conditional Hold Boundary",
    "Evidence matrix row audit count",
    "Evidence matrix row count",
    "Evidence matrix row audited count",
    "Evidence row audit pass count",
    "Evidence row audit conditional count",
    "Evidence row audit fail count",
    "Conditional hold count",
    "Citation added count",
    "Manuscript revised count",
    "EMR-0001",
    "EMR-0002",
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

    if result.source_artifact_count < 18:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.evidence_matrix_row_audit_count != 1:
        errors.append(
            "Evidence matrix row audit count should be one, got: "
            f"{result.evidence_matrix_row_audit_count}"
        )

    if result.evidence_matrix_row_count != 2:
        errors.append(f"Evidence matrix row count should be two, got: {result.evidence_matrix_row_count}")

    if result.evidence_matrix_row_audited_count != 2:
        errors.append(
            "Evidence matrix row audited count should be two, got: "
            f"{result.evidence_matrix_row_audited_count}"
        )

    if result.evidence_row_audit_pass_count != 2:
        errors.append(
            "Evidence row audit pass count should be two, got: "
            f"{result.evidence_row_audit_pass_count}"
        )

    if result.evidence_row_audit_conditional_count != 0:
        errors.append(
            "Evidence row audit conditional count should be zero, got: "
            f"{result.evidence_row_audit_conditional_count}"
        )

    if result.evidence_row_audit_fail_count != 0:
        errors.append(
            "Evidence row audit fail count should be zero, got: "
            f"{result.evidence_row_audit_fail_count}"
        )

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.evidence_matrix_row_audited_count != result.evidence_matrix_row_count:
        errors.append("Evidence matrix row audited count must equal evidence matrix row count")

    if result.evidence_row_audit_pass_count != result.evidence_matrix_row_count:
        errors.append("Evidence row audit pass count must equal evidence matrix row count")

    for label, value in [
        ("Citation added count", result.citation_added_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.row_audit_field_count < 14:
        errors.append(f"Row audit field count too low: {result.row_audit_field_count}")

    if result.row_audit_decision_value_count < 4:
        errors.append(f"Row audit decision value count too low: {result.row_audit_decision_value_count}")

    if result.row_audit_gate_count < 16:
        errors.append(f"Row audit gate count too low: {result.row_audit_gate_count}")

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
        errors.append(f"Word count too low for first evidence matrix row audit: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 68: First Evidence Matrix Row Audit")
    print(
        "Question: Can Viruse Fabric audit populated evidence matrix rows while keeping "
        "citations and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Evidence matrix row audit count: {result.evidence_matrix_row_audit_count}")
    print(f"Evidence matrix row count: {result.evidence_matrix_row_count}")
    print(f"Evidence matrix row audited count: {result.evidence_matrix_row_audited_count}")
    print(f"Evidence row audit pass count: {result.evidence_row_audit_pass_count}")
    print(f"Evidence row audit conditional count: {result.evidence_row_audit_conditional_count}")
    print(f"Evidence row audit fail count: {result.evidence_row_audit_fail_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Row audit field count: {result.row_audit_field_count}")
    print(f"Row audit decision value count: {result.row_audit_decision_value_count}")
    print(f"Row audit gate count: {result.row_audit_gate_count}")
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

    print("Experiment 68 completed successfully.")


if __name__ == "__main__":
    main()
