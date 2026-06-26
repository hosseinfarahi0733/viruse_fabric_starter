"""Experiment 82: First Submission Readiness Audit Execution.

This experiment runs the v8.2 submission readiness audit execution generator.

It verifies that Viruse Fabric can execute readiness audit against planned
readiness criteria while keeping manuscript submission readiness and new
citation additions at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_submission_readiness_audit_execution import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Submission Readiness Audit Execution v8.2",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does execute submission readiness audit",
    "does not make the manuscript submission-ready",
    "does not add new citations",
    "does not claim external validation",
    "readiness audit execution is not manuscript submission readiness",
    "criterion pass is not submission readiness",
    "criterion pass is not external validation",
    "criterion pass is not final paper production",
    "criterion pass is not peer review",
    "audited package is not submission-ready manuscript",
    "controlled package audit is not peer review",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "conditional hold remains outside readiness audit pass rows",
    "future manuscript submission readiness decision is separate",
    "venue acceptance remains unclaimed",
    "Source Artifacts",
    "Submission Readiness Audit Execution Metadata",
    "Readiness Audit Rows",
    "Readiness Audit Linkage Rows",
    "Readiness Audit Boundary Rows",
    "Conditional Hold Rows",
    "Readiness Audit Fields",
    "Readiness Audit Status Values",
    "Submission Readiness Audit Execution Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Audit Execution Interpretation",
    "Execution Boundary",
    "Readiness Audit Boundary",
    "Submission Readiness Boundary",
    "Full Manuscript Boundary",
    "New Citation Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v8.3",
    "Submission readiness audit execution count",
    "Planned readiness criterion count",
    "Executed readiness criterion count",
    "Readiness criterion pass count",
    "Readiness criterion conditional count",
    "Readiness criterion fail count",
    "Manuscript submission ready count",
    "Full manuscript rewrite count",
    "New citation added count",
    "Conditional hold count",
    "SRAE-ROW-0001",
    "SRAE-ROW-0002",
    "SRCP-ROW-0001",
    "SRCP-ROW-0002",
    "FMRPA-ROW-0001",
    "FMRPA-ROW-0002",
    "FMRPE-ROW-0001",
    "FMRPE-ROW-0002",
    "FMRPP-ROW-0001",
    "FMRPP-ROW-0002",
    "BRCA-ROW-0001",
    "BRCA-ROW-0002",
    "CGRX-0001",
    "CGRX-0002",
    "CIT-REC-0001",
    "CIT-REC-0002",
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

    if result.source_artifact_count < 32:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.submission_readiness_audit_execution_count != 1:
        errors.append(
            "Submission readiness audit execution count should be one, got: "
            f"{result.submission_readiness_audit_execution_count}"
        )

    if result.planned_readiness_criterion_count != 2:
        errors.append(
            "Planned readiness criterion count should be two, got: "
            f"{result.planned_readiness_criterion_count}"
        )

    if result.executed_readiness_criterion_count != 2:
        errors.append(
            "Executed readiness criterion count should be two, got: "
            f"{result.executed_readiness_criterion_count}"
        )

    if result.planned_readiness_criterion_count != result.executed_readiness_criterion_count:
        errors.append("Every planned readiness criterion should be executed in v8.2")

    if result.readiness_criterion_pass_count != 2:
        errors.append(
            "Readiness criterion pass count should be two, got: "
            f"{result.readiness_criterion_pass_count}"
        )

    if result.readiness_criterion_conditional_count != 0:
        errors.append(
            "Readiness criterion conditional count should be zero, got: "
            f"{result.readiness_criterion_conditional_count}"
        )

    if result.readiness_criterion_fail_count != 0:
        errors.append(
            "Readiness criterion fail count should be zero, got: "
            f"{result.readiness_criterion_fail_count}"
        )

    if result.executed_readiness_criterion_count != result.readiness_criterion_pass_count:
        errors.append("Every executed readiness criterion should pass in v8.2")

    if result.manuscript_submission_ready_count != 0:
        errors.append(
            "Manuscript submission ready count should remain zero, got: "
            f"{result.manuscript_submission_ready_count}"
        )

    if result.full_manuscript_rewrite_count != 1:
        errors.append(
            "Full manuscript rewrite count should remain one, got: "
            f"{result.full_manuscript_rewrite_count}"
        )

    if result.new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {result.new_citation_added_count}")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.readiness_audit_field_count < 19:
        errors.append(f"Readiness audit field count too low: {result.readiness_audit_field_count}")

    if result.readiness_audit_status_value_count < 6:
        errors.append(
            "Readiness audit status value count too low: "
            f"{result.readiness_audit_status_value_count}"
        )

    if result.readiness_audit_gate_count < 23:
        errors.append(f"Readiness audit gate count too low: {result.readiness_audit_gate_count}")

    if result.boundary_phrase_count < 26:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 14:
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

    if result.word_count < 1650:
        errors.append(
            f"Word count too low for first submission readiness audit execution: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 82: First Submission Readiness Audit Execution")
    print(
        "Question: Can Viruse Fabric execute the first submission readiness audit "
        "from planned readiness criteria while keeping manuscript submission readiness "
        "and new citation additions at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Submission readiness audit execution count: "
        f"{result.submission_readiness_audit_execution_count}"
    )
    print(f"Planned readiness criterion count: {result.planned_readiness_criterion_count}")
    print(f"Executed readiness criterion count: {result.executed_readiness_criterion_count}")
    print(f"Readiness criterion pass count: {result.readiness_criterion_pass_count}")
    print(
        "Readiness criterion conditional count: "
        f"{result.readiness_criterion_conditional_count}"
    )
    print(f"Readiness criterion fail count: {result.readiness_criterion_fail_count}")
    print(f"Manuscript submission ready count: {result.manuscript_submission_ready_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Readiness audit field count: {result.readiness_audit_field_count}")
    print(f"Readiness audit status value count: {result.readiness_audit_status_value_count}")
    print(f"Readiness audit gate count: {result.readiness_audit_gate_count}")
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

    print("Experiment 82 completed successfully.")


if __name__ == "__main__":
    main()
