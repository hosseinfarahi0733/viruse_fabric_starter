"""Experiment 76: First Citation-Grounded Manuscript Claim Revision Execution.

This experiment runs the v7.6 first citation-grounded manuscript claim revision
execution generator.

It verifies that the project can execute bounded claim revisions from the v7.5
plan while keeping full manuscript rewrite and new citation additions at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_citation_grounded_manuscript_claim_revision_execution import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Citation-Grounded Manuscript Claim Revision Execution v7.6",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does execute citation-grounded manuscript claim revision",
    "does create bounded revised claim records",
    "does not rewrite the full manuscript",
    "does not add new citations",
    "does not claim external validation",
    "bounded revised claim record is not full manuscript rewrite",
    "claim revision execution is not external validation",
    "claim revision execution is not proof",
    "citation-grounded claim revision is not biological validation",
    "citation-grounded claim revision is not clinical validation",
    "citation marker audit pass is not manuscript support",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "conditional hold remains outside claim revision execution",
    "future revised claim audit is separate",
    "future manuscript package audit is separate",
    "future public claims must remain bounded",
    "Source Artifacts",
    "Citation-Grounded Manuscript Claim Revision Execution Metadata",
    "Executed Claim Revision Rows",
    "Claim Revision Linkage Rows",
    "Bounded Revised Claim Records",
    "Conditional Hold Rows",
    "Claim Revision Execution Fields",
    "Claim Revision Execution Status Values",
    "Claim Revision Execution Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Claim Revision Execution Interpretation",
    "Execution Boundary",
    "Linkage Boundary",
    "Bounded Claim Boundary",
    "Full Manuscript Boundary",
    "New Citation Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v7.7",
    "Citation-grounded manuscript claim revision execution count",
    "Planned claim revision count",
    "Executed claim revision count",
    "Bounded revised claim record count",
    "Manuscript revised count",
    "Full manuscript rewrite count",
    "New citation added count",
    "Conditional hold count",
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

    if result.source_artifact_count < 26:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.citation_grounded_claim_revision_execution_count != 1:
        errors.append(
            "Citation-grounded claim revision execution count should be one, got: "
            f"{result.citation_grounded_claim_revision_execution_count}"
        )

    if result.planned_claim_revision_count != 2:
        errors.append(
            "Planned claim revision count should be two, got: "
            f"{result.planned_claim_revision_count}"
        )

    if result.executed_claim_revision_count != 2:
        errors.append(
            "Executed claim revision count should be two, got: "
            f"{result.executed_claim_revision_count}"
        )

    if result.bounded_revised_claim_record_count != 2:
        errors.append(
            "Bounded revised claim record count should be two, got: "
            f"{result.bounded_revised_claim_record_count}"
        )

    if result.planned_claim_revision_count != result.executed_claim_revision_count:
        errors.append("Every planned claim revision should be executed in v7.6")

    if result.executed_claim_revision_count != result.bounded_revised_claim_record_count:
        errors.append("Every executed claim revision should create one bounded revised claim record")

    if result.manuscript_revised_count != 1:
        errors.append(f"Manuscript revised count should be one, got: {result.manuscript_revised_count}")

    if result.full_manuscript_rewrite_count != 0:
        errors.append(
            "Full manuscript rewrite count should be zero, got: "
            f"{result.full_manuscript_rewrite_count}"
        )

    if result.new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {result.new_citation_added_count}")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.claim_revision_execution_field_count < 20:
        errors.append(
            "Claim revision execution field count too low: "
            f"{result.claim_revision_execution_field_count}"
        )

    if result.claim_revision_execution_status_value_count < 4:
        errors.append(
            "Claim revision execution status value count too low: "
            f"{result.claim_revision_execution_status_value_count}"
        )

    if result.claim_revision_execution_gate_count < 19:
        errors.append(
            "Claim revision execution gate count too low: "
            f"{result.claim_revision_execution_gate_count}"
        )

    if result.boundary_phrase_count < 24:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 12:
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

    if result.word_count < 1350:
        errors.append(
            "Word count too low for first citation-grounded manuscript claim revision execution: "
            f"{result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 76: First Citation-Grounded Manuscript Claim Revision Execution")
    print(
        "Question: Can Viruse Fabric execute bounded citation-grounded manuscript claim "
        "revision while keeping full manuscript rewrite and new citation additions at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Citation-grounded claim revision execution count: "
        f"{result.citation_grounded_claim_revision_execution_count}"
    )
    print(f"Planned claim revision count: {result.planned_claim_revision_count}")
    print(f"Executed claim revision count: {result.executed_claim_revision_count}")
    print(f"Bounded revised claim record count: {result.bounded_revised_claim_record_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Claim revision execution field count: {result.claim_revision_execution_field_count}")
    print(
        "Claim revision execution status value count: "
        f"{result.claim_revision_execution_status_value_count}"
    )
    print(f"Claim revision execution gate count: {result.claim_revision_execution_gate_count}")
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

    print("Experiment 76 completed successfully.")


if __name__ == "__main__":
    main()
