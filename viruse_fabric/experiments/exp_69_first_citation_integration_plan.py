"""Experiment 69: First Citation Integration Plan.

This experiment runs the v6.9 first citation integration plan generator.

It verifies that the project can plan citation integration from audited evidence
rows while keeping citation execution, added citations, and manuscript revision
at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_citation_integration_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Citation Integration Plan v6.9",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does plan citation integration",
    "does not add citations",
    "does not revise the manuscript",
    "citation integration plan is not citation integration",
    "planned citation slot is not a citation",
    "planned citation slot is not manuscript revision",
    "evidence row pass is not citation readiness",
    "citation planning is not external validation",
    "citations are not external validation",
    "conditional hold remains outside citation planning",
    "future citation use is separate",
    "future manuscript revision is separate",
    "Source Artifacts",
    "Citation Integration Plan Metadata",
    "Planned Citation Slot Rows",
    "Conditional Hold Rows",
    "Citation Plan Fields",
    "Citation Plan Action Values",
    "Citation Plan Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Citation Plan Interpretation",
    "Planning Boundary",
    "Evidence Row Boundary",
    "Citation Boundary",
    "Manuscript Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v7.5",
    "Citation integration plan count",
    "Audited evidence row count",
    "Planned citation slot count",
    "Citation integration execution count",
    "Citation added count",
    "Manuscript revised count",
    "Conditional hold count",
    "CIT-PLAN-0001",
    "CIT-PLAN-0002",
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

    if result.source_artifact_count < 19:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.citation_integration_plan_count != 1:
        errors.append(
            "Citation integration plan count should be one, got: "
            f"{result.citation_integration_plan_count}"
        )

    if result.audited_evidence_row_count != 2:
        errors.append(
            f"Audited evidence row count should be two, got: {result.audited_evidence_row_count}"
        )

    if result.planned_citation_slot_count != 2:
        errors.append(
            "Planned citation slot count should be two, got: "
            f"{result.planned_citation_slot_count}"
        )

    if result.planned_citation_slot_count != result.audited_evidence_row_count:
        errors.append("Planned citation slot count must equal audited evidence row count")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    for label, value in [
        ("Citation integration execution count", result.citation_integration_execution_count),
        ("Citation added count", result.citation_added_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.citation_plan_field_count < 12:
        errors.append(f"Citation plan field count too low: {result.citation_plan_field_count}")

    if result.citation_plan_action_value_count < 4:
        errors.append(
            f"Citation plan action value count too low: {result.citation_plan_action_value_count}"
        )

    if result.citation_plan_gate_count < 15:
        errors.append(f"Citation plan gate count too low: {result.citation_plan_gate_count}")

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
        errors.append(f"Word count too low for first citation integration plan: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 69: First Citation Integration Plan")
    print(
        "Question: Can Viruse Fabric plan citation integration while keeping "
        "citation execution, added citations, and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Citation integration plan count: {result.citation_integration_plan_count}")
    print(f"Audited evidence row count: {result.audited_evidence_row_count}")
    print(f"Planned citation slot count: {result.planned_citation_slot_count}")
    print(f"Citation integration execution count: {result.citation_integration_execution_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation plan field count: {result.citation_plan_field_count}")
    print(f"Citation plan action value count: {result.citation_plan_action_value_count}")
    print(f"Citation plan gate count: {result.citation_plan_gate_count}")
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

    print("Experiment 69 completed successfully.")


if __name__ == "__main__":
    main()
