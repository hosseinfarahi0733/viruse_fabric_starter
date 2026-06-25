"""Experiment 43: One-Page Public Preview Audit.

This experiment runs the v4.3 audit over the v4.2 one-page public preview.

It verifies that the compressed public preview:
- remains compact,
- preserves required sections,
- preserves boundary language,
- avoids overclaiming,
- avoids fake citations,
- keeps limitation language visible,
- remains not externally validated and not submission-ready.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.one_page_public_preview_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "One-Page Public Preview Audit v4.3",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "Boundary Retention",
    "Compactness Check",
    "Concept Coverage",
    "Overclaim Control",
    "Citation Safety",
    "Limitation Visibility",
    "One-page readiness score",
    "does not certify external validation",
    "biological applicability",
    "submission readiness",
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
        errors.append("Source one-page public preview is missing.")

    if not result.full_preview_exists:
        errors.append("Full public technical preview is missing.")

    if not result.public_audit_exists:
        errors.append("Public preview quality audit is missing.")

    if result.section_count < 9:
        errors.append(f"Section count too low: {result.section_count}")

    if result.word_count < 650:
        errors.append(f"Word count too low for one-page preview: {result.word_count}")

    if result.word_count > 950:
        errors.append(f"Word count too high for one-page preview: {result.word_count}")

    if result.required_section_count < 9:
        errors.append(f"Required section count too low: {result.required_section_count}")

    if result.missing_required_section_count != 0:
        errors.append(
            f"Missing required section count should be zero, got: {result.missing_required_section_count}"
        )

    if result.boundary_phrase_count < 8:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.core_term_count < 7:
        errors.append(f"Core term coverage count too low: {result.core_term_count}")

    if result.limitation_language_count < 18:
        errors.append(f"Limitation language count too low: {result.limitation_language_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.one_page_readiness_score < 90:
        errors.append(f"One-page readiness score too low: {result.one_page_readiness_score}")

    if result.recommendation_count < 6:
        errors.append(f"Recommendation count too low: {result.recommendation_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 43: One-Page Public Preview Audit")
    print(
        "Question: Does the compressed v4.2 one-page preview remain compact, "
        "bounded, citation-safe, and free from overclaim?"
    )
    print(f"Title: {result.title}")
    print(f"Source preview: {result.source_path.relative_to(PROJECT_ROOT)}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source exists: {result.source_exists}")
    print(f"Full public preview exists: {result.full_preview_exists}")
    print(f"Public preview quality audit exists: {result.public_audit_exists}")
    print(f"Section count: {result.section_count}")
    print(f"Word count: {result.word_count}")
    print(f"Required section count: {result.required_section_count}")
    print(f"Missing required section count: {result.missing_required_section_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Core term coverage count: {result.core_term_count}")
    print(f"Limitation language count: {result.limitation_language_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Compactness status: {result.compactness_status}")
    print(f"One-page readiness score: {result.one_page_readiness_score}")
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

    print("Experiment 43 completed successfully.")


if __name__ == "__main__":
    main()
