"""Experiment 70: First Citation Integration Execution.

This experiment runs the v7.0 first citation integration execution generator.

It verifies that the project can add verified citation records while keeping
manuscript citation markers and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_citation_integration_execution import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Citation Integration Execution v7.0",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does execute citation integration",
    "does add citation records",
    "does not revise the manuscript",
    "does not insert manuscript citation markers",
    "citation record is not manuscript revision",
    "citation record is not external validation",
    "citation integration is not proof",
    "citations are not external validation",
    "conditional hold remains outside citation integration",
    "future manuscript revision is separate",
    "future citation audit is separate",
    "Source Artifacts",
    "Citation Integration Execution Metadata",
    "Verified Citation Records",
    "Verified Reference Details",
    "Conditional Hold Rows",
    "Citation Execution Fields",
    "Citation Execution Status Values",
    "Citation Execution Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Citation Integration Interpretation",
    "Execution Boundary",
    "Source Verification Boundary",
    "Manuscript Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v7.5",
    "Citation integration execution count",
    "Planned citation slot count",
    "Executed citation slot count",
    "Citation record count",
    "Citation added count",
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

    if result.source_artifact_count < 20:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.citation_integration_execution_count != 1:
        errors.append(
            "Citation integration execution count should be one, got: "
            f"{result.citation_integration_execution_count}"
        )

    if result.planned_citation_slot_count != 2:
        errors.append(
            "Planned citation slot count should be two, got: "
            f"{result.planned_citation_slot_count}"
        )

    if result.executed_citation_slot_count != 2:
        errors.append(
            "Executed citation slot count should be two, got: "
            f"{result.executed_citation_slot_count}"
        )

    if result.citation_record_count != 2:
        errors.append(f"Citation record count should be two, got: {result.citation_record_count}")

    if result.citation_added_count != 2:
        errors.append(f"Citation added count should be two, got: {result.citation_added_count}")

    if result.planned_citation_slot_count != result.executed_citation_slot_count:
        errors.append("Planned citation slot count must equal executed citation slot count")

    if result.executed_citation_slot_count != result.citation_record_count:
        errors.append("Executed citation slot count must equal citation record count")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    for label, value in [
        ("Manuscript citation marker count", result.manuscript_citation_marker_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.citation_execution_field_count < 20:
        errors.append(
            f"Citation execution field count too low: {result.citation_execution_field_count}"
        )

    if result.citation_execution_status_value_count < 4:
        errors.append(
            "Citation execution status value count too low: "
            f"{result.citation_execution_status_value_count}"
        )

    if result.citation_execution_gate_count < 16:
        errors.append(f"Citation execution gate count too low: {result.citation_execution_gate_count}")

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
            f"Word count too low for first citation integration execution: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 70: First Citation Integration Execution")
    print(
        "Question: Can Viruse Fabric add verified citation records while keeping "
        "manuscript citation markers and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Citation integration execution count: {result.citation_integration_execution_count}")
    print(f"Planned citation slot count: {result.planned_citation_slot_count}")
    print(f"Executed citation slot count: {result.executed_citation_slot_count}")
    print(f"Citation record count: {result.citation_record_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript citation marker count: {result.manuscript_citation_marker_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation execution field count: {result.citation_execution_field_count}")
    print(
        "Citation execution status value count: "
        f"{result.citation_execution_status_value_count}"
    )
    print(f"Citation execution gate count: {result.citation_execution_gate_count}")
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

    print("Experiment 70 completed successfully.")


if __name__ == "__main__":
    main()
