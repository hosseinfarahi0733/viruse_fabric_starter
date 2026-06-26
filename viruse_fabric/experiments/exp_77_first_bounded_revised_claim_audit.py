"""Experiment 77: First Bounded Revised Claim Audit.

This experiment runs the v7.7 first bounded revised claim audit generator.

It verifies that the project can audit bounded revised claim records while
keeping full manuscript rewrite and new citation additions at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_bounded_revised_claim_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Bounded Revised Claim Audit v7.7",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does audit bounded revised claim records",
    "does not rewrite the full manuscript",
    "does not add new citations",
    "does not claim external validation",
    "bounded revised claim audit is not full manuscript audit",
    "bounded revised claim audit is not proof",
    "bounded revised claim audit is not external validation",
    "bounded revised claim audit is not submission readiness",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation marker audit pass is not manuscript support",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "conditional hold remains outside revised claim audit pass rows",
    "future full manuscript package is separate",
    "future manuscript package audit is separate",
    "future public claims must remain bounded",
    "future submission readiness audit is separate",
    "Source Artifacts",
    "Bounded Revised Claim Audit Metadata",
    "Revised Claim Audit Rows",
    "Revised Claim Linkage Rows",
    "Revised Claim Boundary Audit Rows",
    "Conditional Hold Rows",
    "Revised Claim Audit Fields",
    "Revised Claim Audit Status Values",
    "Bounded Revised Claim Audit Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Revised Claim Audit Interpretation",
    "Audit Boundary",
    "Linkage Boundary",
    "Claim Boundary Audit",
    "Full Manuscript Boundary",
    "New Citation Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v7.8",
    "Bounded revised claim audit count",
    "Bounded revised claim record count",
    "Bounded revised claim audited count",
    "Revised claim audit pass count",
    "Revised claim audit conditional count",
    "Revised claim audit fail count",
    "Full manuscript rewrite count",
    "New citation added count",
    "Conditional hold count",
    "BRCA-ROW-0001",
    "BRCA-ROW-0002",
    "CGRX-0001",
    "CGRX-0002",
    "CGRP-0001",
    "CGRP-0002",
    "MCMA-ROW-0001",
    "MCMA-ROW-0002",
    "MCM-0001",
    "MCM-0002",
    "CIT-REC-0001",
    "CIT-REC-0002",
    "EMR-0001",
    "EMR-0002",
    "RET-0001",
    "RET-0002",
    "CAND-0001",
    "CAND-0002",
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

    if result.source_artifact_count < 27:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.bounded_revised_claim_audit_count != 1:
        errors.append(
            "Bounded revised claim audit count should be one, got: "
            f"{result.bounded_revised_claim_audit_count}"
        )

    if result.bounded_revised_claim_record_count != 2:
        errors.append(
            "Bounded revised claim record count should be two, got: "
            f"{result.bounded_revised_claim_record_count}"
        )

    if result.bounded_revised_claim_audited_count != 2:
        errors.append(
            "Bounded revised claim audited count should be two, got: "
            f"{result.bounded_revised_claim_audited_count}"
        )

    if result.revised_claim_audit_pass_count != 2:
        errors.append(
            "Revised claim audit pass count should be two, got: "
            f"{result.revised_claim_audit_pass_count}"
        )

    if result.revised_claim_audit_conditional_count != 0:
        errors.append(
            "Revised claim audit conditional count should be zero, got: "
            f"{result.revised_claim_audit_conditional_count}"
        )

    if result.revised_claim_audit_fail_count != 0:
        errors.append(
            "Revised claim audit fail count should be zero, got: "
            f"{result.revised_claim_audit_fail_count}"
        )

    if result.bounded_revised_claim_record_count != result.bounded_revised_claim_audited_count:
        errors.append("Every bounded revised claim record must be audited")

    if result.bounded_revised_claim_audited_count != result.revised_claim_audit_pass_count:
        errors.append("Every audited bounded revised claim must pass in v7.7")

    if result.full_manuscript_rewrite_count != 0:
        errors.append(
            "Full manuscript rewrite count should be zero, got: "
            f"{result.full_manuscript_rewrite_count}"
        )

    if result.new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {result.new_citation_added_count}")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.revised_claim_audit_field_count < 21:
        errors.append(
            f"Revised claim audit field count too low: {result.revised_claim_audit_field_count}"
        )

    if result.revised_claim_audit_status_value_count < 6:
        errors.append(
            "Revised claim audit status value count too low: "
            f"{result.revised_claim_audit_status_value_count}"
        )

    if result.revised_claim_audit_gate_count < 20:
        errors.append(
            f"Revised claim audit gate count too low: {result.revised_claim_audit_gate_count}"
        )

    if result.boundary_phrase_count < 25:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 13:
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

    if result.word_count < 1400:
        errors.append(
            f"Word count too low for first bounded revised claim audit: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 77: First Bounded Revised Claim Audit")
    print(
        "Question: Can Viruse Fabric audit bounded revised claim records while keeping "
        "full manuscript rewrite and new citation additions at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Bounded revised claim audit count: {result.bounded_revised_claim_audit_count}")
    print(f"Bounded revised claim record count: {result.bounded_revised_claim_record_count}")
    print(f"Bounded revised claim audited count: {result.bounded_revised_claim_audited_count}")
    print(f"Revised claim audit pass count: {result.revised_claim_audit_pass_count}")
    print(f"Revised claim audit conditional count: {result.revised_claim_audit_conditional_count}")
    print(f"Revised claim audit fail count: {result.revised_claim_audit_fail_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Revised claim audit field count: {result.revised_claim_audit_field_count}")
    print(
        "Revised claim audit status value count: "
        f"{result.revised_claim_audit_status_value_count}"
    )
    print(f"Revised claim audit gate count: {result.revised_claim_audit_gate_count}")
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

    print("Experiment 77 completed successfully.")


if __name__ == "__main__":
    main()
