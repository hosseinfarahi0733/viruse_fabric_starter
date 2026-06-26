"""Experiment 83: Manuscript Submission Readiness Decision Plan.

This experiment runs the v8.3 manuscript submission readiness decision plan
generator.

It verifies that Viruse Fabric can plan a decision layer from readiness audit
pass rows while keeping decision execution, manuscript submission readiness,
formal proof, independent experiment, external validation, and new citation
additions at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.manuscript_submission_readiness_decision_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Manuscript Submission Readiness Decision Plan v8.3",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does plan manuscript submission readiness decision",
    "does not execute submission readiness decision",
    "does not make the manuscript submission-ready",
    "does not add new citations",
    "does not claim external validation",
    "does not claim formal mathematical proof",
    "does not claim independent experiment",
    "decision plan is not decision execution",
    "decision plan is not submission readiness",
    "decision plan is not external validation",
    "decision plan is not formal proof",
    "decision plan is not independent experiment",
    "decision plan is not final paper production",
    "readiness criterion pass is not submission approval",
    "readiness audit pass is not manuscript support",
    "audited package is not submission-ready manuscript",
    "citations are not external validation",
    "conditional hold remains outside decision planning",
    "future submission readiness decision execution is separate",
    "venue acceptance remains unclaimed",
    "Source Artifacts",
    "Submission Readiness Decision Plan Metadata",
    "Planned Decision Rows",
    "Decision Boundary Rows",
    "Conditional Hold Rows",
    "Decision Plan Fields",
    "Decision Plan Status Values",
    "Manuscript Submission Readiness Decision Plan Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Decision Plan Interpretation",
    "Decision Planning Boundary",
    "Submission Readiness Boundary",
    "Proof and Validation Boundary",
    "New Citation Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v8.4",
    "Submission readiness decision plan count",
    "Executed readiness criterion count",
    "Planned decision row count",
    "Submission readiness decision execution count",
    "Manuscript submission ready count",
    "Full manuscript rewrite count",
    "New citation added count",
    "Conditional hold count",
    "SRDP-ROW-0001",
    "SRDP-ROW-0002",
    "SRAE-ROW-0001",
    "SRAE-ROW-0002",
    "SRCP-ROW-0001",
    "SRCP-ROW-0002",
    "FMRPA-ROW-0001",
    "FMRPA-ROW-0002",
    "FMRPE-ROW-0001",
    "FMRPE-ROW-0002",
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

    if result.source_artifact_count < 33:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.submission_readiness_decision_plan_count != 1:
        errors.append(
            "Submission readiness decision plan count should be one, got: "
            f"{result.submission_readiness_decision_plan_count}"
        )

    if result.executed_readiness_criterion_count != 2:
        errors.append(
            "Executed readiness criterion count should be two, got: "
            f"{result.executed_readiness_criterion_count}"
        )

    if result.planned_decision_row_count != 2:
        errors.append(f"Planned decision row count should be two, got: {result.planned_decision_row_count}")

    if result.executed_readiness_criterion_count != result.planned_decision_row_count:
        errors.append("Each executed readiness criterion should map to one decision plan row")

    if result.submission_readiness_decision_execution_count != 0:
        errors.append(
            "Submission readiness decision execution count should be zero, got: "
            f"{result.submission_readiness_decision_execution_count}"
        )

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

    if result.decision_plan_field_count < 18:
        errors.append(f"Decision plan field count too low: {result.decision_plan_field_count}")

    if result.decision_plan_status_value_count < 8:
        errors.append(
            f"Decision plan status value count too low: {result.decision_plan_status_value_count}"
        )

    if result.decision_plan_gate_count < 24:
        errors.append(f"Decision plan gate count too low: {result.decision_plan_gate_count}")

    if result.boundary_phrase_count < 27:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 15:
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
            f"Word count too low for manuscript submission readiness decision plan: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 83: Manuscript Submission Readiness Decision Plan")
    print(
        "Question: Can Viruse Fabric plan a manuscript submission readiness decision "
        "layer from readiness audit pass rows while keeping decision execution, "
        "manuscript submission readiness, formal proof, independent experiment, "
        "external validation, and new citation additions at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Submission readiness decision plan count: "
        f"{result.submission_readiness_decision_plan_count}"
    )
    print(f"Executed readiness criterion count: {result.executed_readiness_criterion_count}")
    print(f"Planned decision row count: {result.planned_decision_row_count}")
    print(
        "Submission readiness decision execution count: "
        f"{result.submission_readiness_decision_execution_count}"
    )
    print(f"Manuscript submission ready count: {result.manuscript_submission_ready_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Decision plan field count: {result.decision_plan_field_count}")
    print(f"Decision plan status value count: {result.decision_plan_status_value_count}")
    print(f"Decision plan gate count: {result.decision_plan_gate_count}")
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

    print("Experiment 83 completed successfully.")


if __name__ == "__main__":
    main()
