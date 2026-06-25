"""Experiment 67: First Evidence Matrix Population Execution.

This experiment runs the v6.7 first evidence matrix population execution generator.

It verifies that the project can create evidence matrix rows from planned
retained-source mappings while keeping citations and manuscript revision at zero.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.first_evidence_matrix_population_execution import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "First Evidence Matrix Population Execution v6.7",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "does populate the evidence matrix",
    "does not add citations",
    "does not revise the manuscript",
    "evidence matrix row is not a citation",
    "evidence matrix population is not citation integration",
    "evidence matrix population is not manuscript revision",
    "contextual support is not external validation",
    "retained source role pass is not manuscript support",
    "citations are not external validation",
    "conditional hold remains outside evidence matrix population",
    "future citation use is separate",
    "future manuscript revision is separate",
    "Source Artifacts",
    "Evidence Matrix Population Execution Metadata",
    "Populated Evidence Matrix Rows",
    "Conditional Hold Rows",
    "Evidence Row Fields",
    "Matrix Population Decision Values",
    "Population Execution Gates",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Population Execution Interpretation",
    "Evidence Matrix Boundary",
    "Citation Boundary",
    "Manuscript Boundary",
    "Conditional Hold Boundary",
    "Evidence matrix population execution count",
    "Retained source count",
    "Planned evidence mapping count",
    "Evidence matrix populated count",
    "Evidence matrix row count",
    "Conditional hold count",
    "Citation added count",
    "Manuscript revised count",
    "EMR-0001",
    "EMR-0002",
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

    if result.source_artifact_count < 17:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            "Missing source artifact count should be zero, got: "
            f"{result.missing_source_artifact_count}"
        )

    if result.evidence_matrix_population_execution_count != 1:
        errors.append(
            "Evidence matrix population execution count should be one, got: "
            f"{result.evidence_matrix_population_execution_count}"
        )

    if result.retained_source_count != 2:
        errors.append(f"Retained source count should be two, got: {result.retained_source_count}")

    if result.planned_evidence_mapping_count != 2:
        errors.append(
            "Planned evidence mapping count should be two, got: "
            f"{result.planned_evidence_mapping_count}"
        )

    if result.evidence_matrix_populated_count != 2:
        errors.append(
            "Evidence matrix populated count should be two, got: "
            f"{result.evidence_matrix_populated_count}"
        )

    if result.evidence_matrix_row_count != 2:
        errors.append(f"Evidence matrix row count should be two, got: {result.evidence_matrix_row_count}")

    if result.conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {result.conditional_hold_count}")

    if result.evidence_matrix_populated_count != result.evidence_matrix_row_count:
        errors.append("Evidence matrix populated count must equal evidence matrix row count")

    if result.evidence_matrix_row_count != result.planned_evidence_mapping_count:
        errors.append("Evidence matrix row count must equal planned evidence mapping count")

    for label, value in [
        ("Citation added count", result.citation_added_count),
        ("Manuscript revised count", result.manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if result.evidence_row_field_count < 13:
        errors.append(f"Evidence row field count too low: {result.evidence_row_field_count}")

    if result.matrix_population_decision_value_count < 4:
        errors.append(
            "Matrix population decision value count too low: "
            f"{result.matrix_population_decision_value_count}"
        )

    if result.population_execution_gate_count < 16:
        errors.append(
            f"Population execution gate count too low: {result.population_execution_gate_count}"
        )

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
        errors.append(
            f"Word count too low for first evidence matrix population execution: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 67: First Evidence Matrix Population Execution")
    print(
        "Question: Can Viruse Fabric populate evidence matrix rows while keeping "
        "citations and manuscript revision at zero?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Evidence matrix population execution count: {result.evidence_matrix_population_execution_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Planned evidence mapping count: {result.planned_evidence_mapping_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Evidence matrix row count: {result.evidence_matrix_row_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Evidence row field count: {result.evidence_row_field_count}")
    print(f"Matrix population decision value count: {result.matrix_population_decision_value_count}")
    print(f"Population execution gate count: {result.population_execution_gate_count}")
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

    print("Experiment 67 completed successfully.")


if __name__ == "__main__":
    main()
