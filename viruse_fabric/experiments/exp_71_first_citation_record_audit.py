"""Experiment 71: First Citation Record Audit.

This experiment runs the v7.1 first citation record audit generator.

It verifies that the project can audit verified citation records while keeping
new citation additions, manuscript citation markers, and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_citation_record_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Citation Record Audit v7.1",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does audit citation records",
    "does not add new citations",
    "does not insert manuscript citation markers",
    "does not revise the manuscript",
    "citation record audit is not citation integration execution",
    "citation record pass is not manuscript support",
    "citation record pass is not external validation",
    "citation record pass is not proof",
    "citations are not external validation",
    "conditional hold remains outside citation record audit",
    "future manuscript revision is separate",
    "future manuscript citation insertion is separate",
    "Source Artifacts",
    "Citation Record Audit Metadata",
    "Citation Record Audit Rows",
    "Audited Reference Details",
    "Conditional Hold Rows",
    "Citation Record Audit Fields",
    "Citation Record Audit Decision Values",
    "Citation Record Audit Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Citation Record Audit Interpretation",
    "Audit Boundary",
    "Field Completeness Boundary",
    "Linkage Boundary",
    "Manuscript Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v7.5",
    "Citation record audit count",
    "Citation record count",
    "Citation record audited count",
    "Citation record audit pass count",
    "Citation record audit conditional count",
    "Citation record audit fail count",
    "New citation added count",
    "Manuscript citation marker count",
    "Manuscript revised count",
    "Conditional hold count",
    "CIT-REC-0001",
    "CIT-REC-0002",
    "CAND-0003",
    "pmlr-v115-blom20a",
    "pmlr-v124-wengel-mogensen20a",
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

    if result.source_artifact_count < 21:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.citation_record_audit_count != 1:
        errors.append(
            "Citation record audit count should be one, got: "
            f"{result.citation_record_audit_count}"
        )

    if result.citation_record_count != 2:
        errors.append(f"Citation record count should be two, got: {result.citation_record_count}")

    if result.citation_record_audited_count != 2:
        errors.append(
            "Citation record audited count should be two, got: "
            f"{result.citation_record_audited_count}"
        )

    if result.citation_record_audit_pass_count != 2:
        errors.append(
            "Citation record audit pass count should be two, got: "
            f"{result.citation_record_audit_pass_count}"
        )

    if result.citation_record_audit_conditional_count != 0:
        errors.append(
            "Citation record audit conditional count should be zero, got: "
            f"{result.citation_record_audit_conditional_count}"
        )

    if result.citation_record_audit_fail_count != 0:
        errors.append(
            "Citation record audit fail count should be zero, got: "
            f"{result.citation_record_audit_fail_count}"
        )

    if result.citation_record_audited_count != result.citation_record_count:
        errors.append("Citation record audited count must equal citation record count")

    if result.citation_record_audit_pass_count != result.citation_record_count:
        errors.append("Citation record audit pass count must equal citation record count")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    for label, value in [
        ("New citation added count", result.new_citation_added_count),
        ("Manuscript citation marker count", result.manuscript_citation_marker_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.citation_record_audit_field_count < 24:
        errors.append(
            f"Citation record audit field count too low: {result.citation_record_audit_field_count}"
        )

    if result.citation_record_audit_decision_value_count < 4:
        errors.append(
            "Citation record audit decision value count too low: "
            f"{result.citation_record_audit_decision_value_count}"
        )

    if result.citation_record_audit_gate_count < 16:
        errors.append(
            f"Citation record audit gate count too low: {result.citation_record_audit_gate_count}"
        )

    if result.boundary_phrase_count < 20:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 11:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.invented_citation_like_pattern_count != 0:
        errors.append(
            "Invented citation-like pattern count should be zero, got: "
            f"{result.invented_citation_like_pattern_count}"
        )

    if result.word_count < 1200:
        errors.append(f"Word count too low for first citation record audit: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 71: First Citation Record Audit")
    print(
        "Question: Can Viruse Fabric audit verified citation records while keeping "
        "new citation additions, manuscript citation markers, and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Citation record audit count: {result.citation_record_audit_count}")
    print(f"Citation record count: {result.citation_record_count}")
    print(f"Citation record audited count: {result.citation_record_audited_count}")
    print(f"Citation record audit pass count: {result.citation_record_audit_pass_count}")
    print(
        "Citation record audit conditional count: "
        f"{result.citation_record_audit_conditional_count}"
    )
    print(f"Citation record audit fail count: {result.citation_record_audit_fail_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Manuscript citation marker count: {result.manuscript_citation_marker_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation record audit field count: {result.citation_record_audit_field_count}")
    print(
        "Citation record audit decision value count: "
        f"{result.citation_record_audit_decision_value_count}"
    )
    print(f"Citation record audit gate count: {result.citation_record_audit_gate_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Invented citation-like pattern count: {result.invented_citation_like_pattern_count}")
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

    print("Experiment 71 completed successfully.")


if __name__ == "__main__":
    main()
