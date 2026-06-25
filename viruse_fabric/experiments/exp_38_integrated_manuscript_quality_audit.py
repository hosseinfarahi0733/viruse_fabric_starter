"""Experiment 38: Integrated Manuscript Quality Audit.

This experiment runs the v3.8 audit over the v3.7 integrated manuscript draft.

It verifies that the integrated manuscript:
- preserves cautious research boundaries,
- avoids overclaiming,
- does not invent citations,
- does not claim submission readiness,
- integrates formal notation,
- includes related-work positioning,
- includes validation mapping and a compact validation table.

The experiment keeps the project status unchanged:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.integrated_manuscript_quality_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Integrated Manuscript Quality Audit v3.8",
    "research prototype with internal validation",
    "not a final paper",
    "not a submission-ready manuscript",
    "does not certify external validation",
    "biological applicability",
    "submission readiness",
    "Formal Notation Integration",
    "Related-Work Positioning",
    "Validation Mapping",
    "Overclaim Control",
    "Possible fake citation count",
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

    if not result.source_exists:
        errors.append("Source manuscript is missing.")

    if result.section_count < 20:
        errors.append(f"Section count below expected integrated manuscript threshold: {result.section_count}")

    if result.word_count < 2500:
        errors.append(f"Word count below audit threshold: {result.word_count}")

    if result.boundary_count < 6:
        errors.append(f"Boundary phrase count too low: {result.boundary_count}")

    if result.notation_count < 12:
        errors.append(f"Formal notation integration count too low: {result.notation_count}")

    if result.related_work_count < 7:
        errors.append(f"Related-work positioning count too low: {result.related_work_count}")

    if result.validation_count < 7:
        errors.append(f"Validation mapping count too low: {result.validation_count}")

    if not result.validation_table_present:
        errors.append("Validation table not detected.")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Possible fake citation count should be zero, got: {result.fake_citation_count}")

    if result.submission_ready_claim_count != 0:
        errors.append(
            f"Submission-ready claim count should be zero, got: {result.submission_ready_claim_count}"
        )

    if result.recommendation_count < 6:
        errors.append(f"Recommendation count too low: {result.recommendation_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 38: Integrated Manuscript Quality Audit")
    print(
        "Question: Does the v3.7 integrated manuscript preserve quality, caution, "
        "and internal coherence after integration?"
    )
    print(f"Title: {result.title}")
    print(f"Source manuscript: {result.source_path.relative_to(PROJECT_ROOT)}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source exists: {result.source_exists}")
    print(f"Section count: {result.section_count}")
    print(f"Word count: {result.word_count}")
    print(f"Boundary phrase count: {result.boundary_count}")
    print(f"Formal notation integration count: {result.notation_count}")
    print(f"Related-work positioning count: {result.related_work_count}")
    print(f"Validation mapping count: {result.validation_count}")
    print(f"Validation table present: {result.validation_table_present}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Possible fake citation count: {result.fake_citation_count}")
    print(f"Submission-ready claim count: {result.submission_ready_claim_count}")
    print(f"Recommendation count: {result.recommendation_count}")
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

    print("Experiment 38 completed successfully.")


if __name__ == "__main__":
    main()
