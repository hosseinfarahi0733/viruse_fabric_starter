"""Experiment 81: First Submission Readiness Criteria Plan.

This experiment runs the v8.1 submission readiness criteria plan generator.

It verifies that Viruse Fabric can plan submission readiness criteria from the
audited manuscript package while keeping readiness audit execution, manuscript
submission readiness, and new citation additions at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_submission_readiness_criteria_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Submission Readiness Criteria Plan v8.1",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does plan submission readiness criteria",
    "does not execute submission readiness audit",
    "does not make the manuscript submission-ready",
    "does not add new citations",
    "does not claim external validation",
    "submission readiness criteria plan is not submission readiness audit",
    "criteria plan is not readiness execution",
    "criteria plan is not submission readiness",
    "criteria plan is not external validation",
    "criteria plan is not final paper production",
    "audited package is not submission-ready manuscript",
    "controlled package audit is not peer review",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "conditional hold remains outside readiness criteria planning",
    "future readiness audit is separate",
    "Source Artifacts",
    "Submission Readiness Criteria Plan Metadata",
    "Planned Readiness Criteria Rows",
    "Readiness Criteria Linkage Rows",
    "Readiness Criteria Boundary Rows",
    "Conditional Hold Rows",
    "Readiness Criteria Fields",
    "Readiness Criteria Status Values",
    "Submission Readiness Criteria Plan Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Criteria Plan Interpretation",
    "Planning Boundary",
    "Readiness Criteria Boundary",
    "Submission Readiness Boundary",
    "Full Manuscript Boundary",
    "New Citation Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v8.2",
    "Submission readiness criteria plan count",
    "Audited package revision count",
    "Planned readiness criterion count",
    "Submission readiness audit execution count",
    "Manuscript submission ready count",
    "Full manuscript rewrite count",
    "New citation added count",
    "Conditional hold count",
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

    if result.source_artifact_count < 31:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.submission_readiness_criteria_plan_count != 1:
        errors.append(
            "Submission readiness criteria plan count should be one, got: "
            f"{result.submission_readiness_criteria_plan_count}"
        )

    if result.audited_package_revision_count != 2:
        errors.append(
            "Audited package revision count should be two, got: "
            f"{result.audited_package_revision_count}"
        )

    if result.planned_readiness_criterion_count != 2:
        errors.append(
            "Planned readiness criterion count should be two, got: "
            f"{result.planned_readiness_criterion_count}"
        )

    if result.audited_package_revision_count != result.planned_readiness_criterion_count:
        errors.append("Each audited package revision should map to one readiness criterion plan")

    if result.submission_readiness_audit_execution_count != 0:
        errors.append(
            "Submission readiness audit execution count should be zero, got: "
            f"{result.submission_readiness_audit_execution_count}"
        )

    if result.manuscript_submission_ready_count != 0:
        errors.append(
            "Manuscript submission ready count should be zero, got: "
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

    if result.readiness_criteria_field_count < 17:
        errors.append(
            f"Readiness criteria field count too low: {result.readiness_criteria_field_count}"
        )

    if result.readiness_criteria_status_value_count < 5:
        errors.append(
            "Readiness criteria status value count too low: "
            f"{result.readiness_criteria_status_value_count}"
        )

    if result.readiness_criteria_gate_count < 20:
        errors.append(
            f"Readiness criteria gate count too low: {result.readiness_criteria_gate_count}"
        )

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
            f"Word count too low for first submission readiness criteria plan: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 81: First Submission Readiness Criteria Plan")
    print(
        "Question: Can Viruse Fabric plan submission readiness criteria from the audited "
        "manuscript package while keeping readiness audit execution, manuscript submission "
        "readiness, and new citation additions at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Submission readiness criteria plan count: "
        f"{result.submission_readiness_criteria_plan_count}"
    )
    print(f"Audited package revision count: {result.audited_package_revision_count}")
    print(f"Planned readiness criterion count: {result.planned_readiness_criterion_count}")
    print(
        "Submission readiness audit execution count: "
        f"{result.submission_readiness_audit_execution_count}"
    )
    print(f"Manuscript submission ready count: {result.manuscript_submission_ready_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Readiness criteria field count: {result.readiness_criteria_field_count}")
    print(
        "Readiness criteria status value count: "
        f"{result.readiness_criteria_status_value_count}"
    )
    print(f"Readiness criteria gate count: {result.readiness_criteria_gate_count}")
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

    print("Experiment 81 completed successfully.")


if __name__ == "__main__":
    main()
