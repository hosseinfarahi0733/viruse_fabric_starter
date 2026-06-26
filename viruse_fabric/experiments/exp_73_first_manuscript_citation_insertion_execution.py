"""Experiment 73: First Manuscript Citation Insertion Execution.

This experiment runs the v7.3 first manuscript citation insertion execution generator.

It verifies that the project can add bounded manuscript citation marker records
while keeping manuscript claim revision and new citation additions at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_manuscript_citation_insertion_execution import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Manuscript Citation Insertion Execution v7.3",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does execute manuscript citation insertion",
    "does insert manuscript citation markers",
    "does not revise manuscript claims",
    "does not add new citations",
    "manuscript citation marker is not manuscript claim revision",
    "marker insertion is not external validation",
    "citation marker is not proof",
    "citations are not external validation",
    "citation record pass is not manuscript support",
    "conditional hold remains outside manuscript citation insertion",
    "future manuscript revision is separate",
    "future marker audit is separate",
    "Source Artifacts",
    "Manuscript Citation Insertion Execution Metadata",
    "Inserted Manuscript Citation Marker Rows",
    "Manuscript Citation Marker Details",
    "Conditional Hold Rows",
    "Manuscript Citation Insertion Execution Fields",
    "Manuscript Citation Insertion Status Values",
    "Manuscript Citation Insertion Execution Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Manuscript Citation Insertion Interpretation",
    "Execution Boundary",
    "Marker Boundary",
    "Manuscript Claim Boundary",
    "New Citation Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v7.5",
    "Manuscript citation insertion execution count",
    "Planned manuscript citation slot count",
    "Executed manuscript citation slot count",
    "Manuscript citation marker count",
    "Manuscript revised count",
    "New citation added count",
    "Conditional hold count",
    "MCM-0001",
    "MCM-0002",
    "MCIS-PLAN-0001",
    "MCIS-PLAN-0002",
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

    if result.source_artifact_count < 23:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.manuscript_citation_insertion_execution_count != 1:
        errors.append(
            "Manuscript citation insertion execution count should be one, got: "
            f"{result.manuscript_citation_insertion_execution_count}"
        )

    if result.planned_manuscript_citation_slot_count != 2:
        errors.append(
            "Planned manuscript citation slot count should be two, got: "
            f"{result.planned_manuscript_citation_slot_count}"
        )

    if result.executed_manuscript_citation_slot_count != 2:
        errors.append(
            "Executed manuscript citation slot count should be two, got: "
            f"{result.executed_manuscript_citation_slot_count}"
        )

    if result.manuscript_citation_marker_count != 2:
        errors.append(
            "Manuscript citation marker count should be two, got: "
            f"{result.manuscript_citation_marker_count}"
        )

    if result.planned_manuscript_citation_slot_count != result.executed_manuscript_citation_slot_count:
        errors.append(
            "Planned manuscript citation slot count must equal executed manuscript citation slot count"
        )

    if result.executed_manuscript_citation_slot_count != result.manuscript_citation_marker_count:
        errors.append(
            "Executed manuscript citation slot count must equal manuscript citation marker count"
        )

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    for label, value in [
        ("Manuscript revised count", result.manuscript_revised_count),
        ("New citation added count", result.new_citation_added_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.insertion_execution_field_count < 15:
        errors.append(
            f"Insertion execution field count too low: {result.insertion_execution_field_count}"
        )

    if result.insertion_execution_status_value_count < 4:
        errors.append(
            "Insertion execution status value count too low: "
            f"{result.insertion_execution_status_value_count}"
        )

    if result.insertion_execution_gate_count < 16:
        errors.append(f"Insertion execution gate count too low: {result.insertion_execution_gate_count}")

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
        errors.append(
            "Word count too low for first manuscript citation insertion execution: "
            f"{result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 73: First Manuscript Citation Insertion Execution")
    print(
        "Question: Can Viruse Fabric add bounded manuscript citation marker records while "
        "keeping manuscript claim revision and new citation additions at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Manuscript citation insertion execution count: "
        f"{result.manuscript_citation_insertion_execution_count}"
    )
    print(
        "Planned manuscript citation slot count: "
        f"{result.planned_manuscript_citation_slot_count}"
    )
    print(
        "Executed manuscript citation slot count: "
        f"{result.executed_manuscript_citation_slot_count}"
    )
    print(f"Manuscript citation marker count: {result.manuscript_citation_marker_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Insertion execution field count: {result.insertion_execution_field_count}")
    print(
        "Insertion execution status value count: "
        f"{result.insertion_execution_status_value_count}"
    )
    print(f"Insertion execution gate count: {result.insertion_execution_gate_count}")
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

    print("Experiment 73 completed successfully.")


if __name__ == "__main__":
    main()
