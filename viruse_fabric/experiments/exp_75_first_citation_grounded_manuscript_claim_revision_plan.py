"""Experiment 75: First Citation-Grounded Manuscript Claim Revision Plan.

This experiment runs the v7.5 first citation-grounded manuscript claim revision
plan generator.

It verifies that the project can plan bounded manuscript claim revisions from
audited manuscript citation markers while keeping manuscript claim revision
execution, manuscript revision, and new citation additions at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_citation_grounded_manuscript_claim_revision_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Citation-Grounded Manuscript Claim Revision Plan v7.5",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does plan citation-grounded manuscript claim revision",
    "does not execute manuscript claim revision",
    "does not revise manuscript claims",
    "does not rewrite manuscript paragraphs",
    "does not add new citations",
    "claim revision plan is not claim revision execution",
    "planned claim language is not applied manuscript prose",
    "citation-grounded revision plan is not proof",
    "citation-grounded revision plan is not external validation",
    "citation marker audit pass is not manuscript support",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "conditional hold remains outside claim revision planning",
    "future claim revision execution is separate",
    "future revised manuscript audit is separate",
    "future public claims must remain bounded",
    "Source Artifacts",
    "Citation-Grounded Manuscript Claim Revision Plan Metadata",
    "Planned Claim Revision Rows",
    "Claim Revision Linkage Rows",
    "Planned Bounded Claim Language",
    "Conditional Hold Rows",
    "Claim Revision Plan Fields",
    "Claim Revision Plan Status Values",
    "Claim Revision Plan Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Claim Revision Plan Interpretation",
    "Planning Boundary",
    "Linkage Boundary",
    "Planned Language Boundary",
    "Manuscript Claim Boundary",
    "New Citation Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v7.6",
    "Citation-grounded manuscript claim revision plan count",
    "Audited manuscript citation marker count",
    "Planned claim revision count",
    "Manuscript claim revision execution count",
    "Manuscript revised count",
    "New citation added count",
    "Conditional hold count",
    "CGRP-0001",
    "CGRP-0002",
    "MCMA-ROW-0001",
    "MCMA-ROW-0002",
    "MCM-0001",
    "MCM-0002",
    "MCIS-PLAN-0001",
    "MCIS-PLAN-0002",
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

    if result.source_artifact_count < 25:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.citation_grounded_claim_revision_plan_count != 1:
        errors.append(
            "Citation-grounded manuscript claim revision plan count should be one, got: "
            f"{result.citation_grounded_claim_revision_plan_count}"
        )

    if result.audited_manuscript_citation_marker_count != 2:
        errors.append(
            "Audited manuscript citation marker count should be two, got: "
            f"{result.audited_manuscript_citation_marker_count}"
        )

    if result.planned_claim_revision_count != 2:
        errors.append(
            "Planned claim revision count should be two, got: "
            f"{result.planned_claim_revision_count}"
        )

    if result.audited_manuscript_citation_marker_count != result.planned_claim_revision_count:
        errors.append("Each audited manuscript citation marker should map to one planned claim revision")

    if result.manuscript_claim_revision_execution_count != 0:
        errors.append(
            "Manuscript claim revision execution count should be zero, got: "
            f"{result.manuscript_claim_revision_execution_count}"
        )

    if result.manuscript_revised_count != 0:
        errors.append(f"Manuscript revised count should be zero, got: {result.manuscript_revised_count}")

    if result.new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {result.new_citation_added_count}")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.claim_revision_plan_field_count < 19:
        errors.append(
            f"Claim revision plan field count too low: {result.claim_revision_plan_field_count}"
        )

    if result.claim_revision_plan_status_value_count < 4:
        errors.append(
            "Claim revision plan status value count too low: "
            f"{result.claim_revision_plan_status_value_count}"
        )

    if result.claim_revision_plan_gate_count < 18:
        errors.append(
            f"Claim revision plan gate count too low: {result.claim_revision_plan_gate_count}"
        )

    if result.boundary_phrase_count < 22:
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

    if result.word_count < 1250:
        errors.append(
            "Word count too low for first citation-grounded manuscript claim revision plan: "
            f"{result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 75: First Citation-Grounded Manuscript Claim Revision Plan")
    print(
        "Question: Can Viruse Fabric plan citation-grounded manuscript claim revision "
        "from audited manuscript citation markers while keeping execution, manuscript "
        "revision, and new citation additions at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Citation-grounded manuscript claim revision plan count: "
        f"{result.citation_grounded_claim_revision_plan_count}"
    )
    print(
        "Audited manuscript citation marker count: "
        f"{result.audited_manuscript_citation_marker_count}"
    )
    print(f"Planned claim revision count: {result.planned_claim_revision_count}")
    print(
        "Manuscript claim revision execution count: "
        f"{result.manuscript_claim_revision_execution_count}"
    )
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Claim revision plan field count: {result.claim_revision_plan_field_count}")
    print(
        "Claim revision plan status value count: "
        f"{result.claim_revision_plan_status_value_count}"
    )
    print(f"Claim revision plan gate count: {result.claim_revision_plan_gate_count}")
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

    print("Experiment 75 completed successfully.")


if __name__ == "__main__":
    main()
