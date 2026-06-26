"""Experiment 79: First Full Manuscript Revision Package Execution.

This experiment runs the v7.9 first full manuscript revision package execution generator.

It verifies that the project can execute a controlled full manuscript revision
package while keeping new citation additions at zero and preserving
non-submission-ready boundaries.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_full_manuscript_revision_package_execution import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Full Manuscript Revision Package Execution v7.9",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does execute full manuscript revision package",
    "controlled full manuscript revision package artifact",
    "full manuscript rewrite count is one",
    "does not add new citations",
    "does not claim external validation",
    "does not make the manuscript submission-ready",
    "package execution is not external validation",
    "package execution is not submission readiness",
    "package execution is not final paper production",
    "full manuscript rewrite is controlled package artifact only",
    "controlled package artifact is not acceptance",
    "controlled package artifact is not peer review",
    "citation-grounded revised claim is not biological validation",
    "citation-grounded revised claim is not clinical validation",
    "citation record pass is not manuscript support",
    "citations are not external validation",
    "conditional hold remains outside package execution",
    "future package audit is separate",
    "future submission readiness audit is separate",
    "Source Artifacts",
    "Full Manuscript Revision Package Execution Metadata",
    "Executed Package Revision Rows",
    "Package Linkage Rows",
    "Package Text Rows",
    "Package Execution Boundary Rows",
    "Controlled Manuscript Package Sections",
    "Conditional Hold Rows",
    "Package Execution Fields",
    "Package Execution Status Values",
    "Full Manuscript Revision Package Execution Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Package Execution Interpretation",
    "Execution Boundary",
    "Linkage Boundary",
    "Controlled Package Text Boundary",
    "Full Manuscript Boundary",
    "New Citation Boundary",
    "Conditional Hold Boundary",
    "Claim Boundary Toward v8.0",
    "Full manuscript revision package execution count",
    "Planned package revision count",
    "Executed package revision count",
    "Full manuscript revision package count",
    "Full manuscript rewrite count",
    "New citation added count",
    "Conditional hold count",
    "FMRPE-ROW-0001",
    "FMRPE-ROW-0002",
    "FMRPP-ROW-0001",
    "FMRPP-ROW-0002",
    "BRCA-ROW-0001",
    "BRCA-ROW-0002",
    "CGRX-0001",
    "CGRX-0002",
    "CGRP-0001",
    "CGRP-0002",
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

    if result.source_artifact_count < 29:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.full_manuscript_revision_package_execution_count != 1:
        errors.append(
            "Full manuscript revision package execution count should be one, got: "
            f"{result.full_manuscript_revision_package_execution_count}"
        )

    if result.planned_package_revision_count != 2:
        errors.append(
            "Planned package revision count should be two, got: "
            f"{result.planned_package_revision_count}"
        )

    if result.executed_package_revision_count != 2:
        errors.append(
            "Executed package revision count should be two, got: "
            f"{result.executed_package_revision_count}"
        )

    if result.planned_package_revision_count != result.executed_package_revision_count:
        errors.append("Each planned package revision should be executed in v7.9")

    if result.full_manuscript_revision_package_count != 1:
        errors.append(
            "Full manuscript revision package count should be one, got: "
            f"{result.full_manuscript_revision_package_count}"
        )

    if result.full_manuscript_rewrite_count != 1:
        errors.append(
            "Full manuscript rewrite count should be one for controlled package execution, got: "
            f"{result.full_manuscript_rewrite_count}"
        )

    if result.new_citation_added_count != 0:
        errors.append(f"New citation added count should be zero, got: {result.new_citation_added_count}")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.package_execution_field_count < 21:
        errors.append(
            f"Package execution field count too low: {result.package_execution_field_count}"
        )

    if result.package_execution_status_value_count < 6:
        errors.append(
            "Package execution status value count too low: "
            f"{result.package_execution_status_value_count}"
        )

    if result.package_execution_gate_count < 22:
        errors.append(
            f"Package execution gate count too low: {result.package_execution_gate_count}"
        )

    if result.controlled_package_section_count != 2:
        errors.append(
            "Controlled package section count should be two, got: "
            f"{result.controlled_package_section_count}"
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

    if result.word_count < 1550:
        errors.append(
            f"Word count too low for first full manuscript revision package execution: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 79: First Full Manuscript Revision Package Execution")
    print(
        "Question: Can Viruse Fabric execute the first full manuscript revision package "
        "while keeping new citation additions at zero and preserving non-submission-ready boundaries?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Full manuscript revision package execution count: "
        f"{result.full_manuscript_revision_package_execution_count}"
    )
    print(f"Planned package revision count: {result.planned_package_revision_count}")
    print(f"Executed package revision count: {result.executed_package_revision_count}")
    print(
        "Full manuscript revision package count: "
        f"{result.full_manuscript_revision_package_count}"
    )
    print(f"Full manuscript rewrite count: {result.full_manuscript_rewrite_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Package execution field count: {result.package_execution_field_count}")
    print(
        "Package execution status value count: "
        f"{result.package_execution_status_value_count}"
    )
    print(f"Package execution gate count: {result.package_execution_gate_count}")
    print(f"Controlled package section count: {result.controlled_package_section_count}")
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

    print("Experiment 79 completed successfully.")


if __name__ == "__main__":
    main()
