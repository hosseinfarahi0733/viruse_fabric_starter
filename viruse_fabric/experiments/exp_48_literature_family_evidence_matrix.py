"""Experiment 48: Literature Family Evidence Matrix.

This experiment runs the v4.8 literature family evidence matrix generator.

It verifies that the project can create an empty evidence matrix for future
real sources without inventing citations, populating source rows prematurely,
overclaiming, or weakening project boundaries.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.literature_family_evidence_matrix import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Literature Family Evidence Matrix v4.8",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "No source is added by this matrix",
    "No citation is added by this matrix",
    "Citation placeholders are not citations",
    "Literature Family Summary",
    "Claim Category Summary",
    "Evidence Matrix",
    "Evidence Fields",
    "Source Status Values",
    "Source Role Values",
    "Decision Values",
    "Matrix Rules",
    "Prohibited Behaviors",
    "Populated source count",
    "Invented source count",
    "does not provide citations",
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

    if not result.source_protocol_exists:
        errors.append("Source literature search protocol is missing.")

    if result.literature_family_count < 8:
        errors.append(f"Literature family count too low: {result.literature_family_count}")

    if result.claim_category_count < 8:
        errors.append(f"Claim category count too low: {result.claim_category_count}")

    expected_rows = result.literature_family_count * result.claim_category_count
    if result.matrix_row_count != expected_rows:
        errors.append(f"Matrix row count mismatch: {result.matrix_row_count} != {expected_rows}")

    if result.matrix_row_count < 64:
        errors.append(f"Matrix row count too low: {result.matrix_row_count}")

    if result.source_status_count < 5:
        errors.append(f"Source status count too low: {result.source_status_count}")

    if result.source_role_count < 6:
        errors.append(f"Source role count too low: {result.source_role_count}")

    if result.decision_value_count < 4:
        errors.append(f"Decision value count too low: {result.decision_value_count}")

    if result.evidence_field_count < 12:
        errors.append(f"Evidence field count too low: {result.evidence_field_count}")

    if result.boundary_phrase_count < 10:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.matrix_rule_count < 10:
        errors.append(f"Matrix rule count too low: {result.matrix_rule_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.prohibited_behavior_count < 10:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.populated_source_count != 0:
        errors.append(f"Populated source count should be zero, got: {result.populated_source_count}")

    if result.invented_source_count != 0:
        errors.append(f"Invented source count should be zero, got: {result.invented_source_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.word_count < 1400:
        errors.append(f"Word count too low for literature family evidence matrix: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 48: Literature Family Evidence Matrix")
    print(
        "Question: Can Viruse Fabric create an empty evidence matrix for future "
        "real sources without inventing citations or populating rows prematurely?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source protocol exists: {result.source_protocol_exists}")
    print(f"Literature family count: {result.literature_family_count}")
    print(f"Claim category count: {result.claim_category_count}")
    print(f"Matrix row count: {result.matrix_row_count}")
    print(f"Source status count: {result.source_status_count}")
    print(f"Source role count: {result.source_role_count}")
    print(f"Decision value count: {result.decision_value_count}")
    print(f"Evidence field count: {result.evidence_field_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Matrix rule count: {result.matrix_rule_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Populated source count: {result.populated_source_count}")
    print(f"Invented source count: {result.invented_source_count}")
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

    print("Experiment 48 completed successfully.")


if __name__ == "__main__":
    main()
