"""Experiment 41: Public Preview Quality Audit.

This experiment runs the v4.1 audit over the v4.0 public technical preview.

It verifies that the public preview:
- preserves the internal-validation boundary,
- contains all required public-facing sections,
- remains understandable to a technical public audience,
- avoids overclaiming,
- avoids fake citations,
- keeps limitations visible,
- remains not externally validated and not submission-ready.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.public_preview_quality_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Public Preview Quality Audit v4.1",
    "research prototype with internal validation",
    "public-safe technical preview",
    "not externally validated",
    "not submission-ready",
    "Boundary Visibility",
    "Public Clarity",
    "Overclaim Control",
    "Citation Safety",
    "Limitations",
    "Public readiness score",
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
        errors.append("Source public technical preview is missing.")

    if result.source_section_count < 18:
        errors.append(f"Source section count too low: {result.source_section_count}")

    if result.source_word_count < 1500:
        errors.append(f"Source word count too low: {result.source_word_count}")

    if result.required_section_count < 17:
        errors.append(f"Required section count too low: {result.required_section_count}")

    if result.missing_required_section_count != 0:
        errors.append(f"Missing required section count should be zero, got: {result.missing_required_section_count}")

    if result.boundary_phrase_count < 12:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.core_concept_count < 8:
        errors.append(f"Core concept coverage count too low: {result.core_concept_count}")

    if result.public_clarity_count < 8:
        errors.append(f"Public clarity count too low: {result.public_clarity_count}")

    if result.limitation_language_count < 40:
        errors.append(f"Limitation language count too low: {result.limitation_language_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.public_readiness_score < 85:
        errors.append(f"Public readiness score too low: {result.public_readiness_score}")

    if result.recommendation_count < 6:
        errors.append(f"Recommendation count too low: {result.recommendation_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 41: Public Preview Quality Audit")
    print(
        "Question: Does the v4.0 public technical preview remain bounded, "
        "clear, citation-safe, and free from public-facing overclaim?"
    )
    print(f"Title: {result.title}")
    print(f"Source preview: {result.source_path.relative_to(PROJECT_ROOT)}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source exists: {result.source_exists}")
    print(f"Source section count: {result.source_section_count}")
    print(f"Source word count: {result.source_word_count}")
    print(f"Required public section count: {result.required_section_count}")
    print(f"Missing required section count: {result.missing_required_section_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Core concept coverage count: {result.core_concept_count}")
    print(f"Public clarity count: {result.public_clarity_count}")
    print(f"Limitation language count: {result.limitation_language_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Public readiness score: {result.public_readiness_score}")
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

    print("Experiment 41 completed successfully.")


if __name__ == "__main__":
    main()
