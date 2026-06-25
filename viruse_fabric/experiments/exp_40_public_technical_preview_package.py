"""Experiment 40: Public Technical Preview Package.

This experiment runs the v4.0 public technical preview package generator.

It verifies that the public-facing preview:
- uses source artifacts from v2.1, v2.3, v3.0, v3.7, v3.8, and v3.9,
- preserves the project's internal-validation boundary,
- avoids overclaiming,
- avoids fake citations,
- states that the project is not externally validated,
- states that the manuscript is not submission-ready,
- keeps biological, clinical, laboratory, and operational boundaries visible.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.public_technical_preview_package import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Public Technical Preview Package v4.0",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "not operational guidance",
    "not biological guidance",
    "not clinical guidance",
    "not laboratory guidance",
    "citation placeholders are not citations",
    "What the Project Is",
    "What the Project Is Not",
    "Validation Status",
    "Manuscript Status",
    "Citation Status",
    "Limitations",
    "Safe Public Description",
    "Suggested Public Abstract",
    "Review Checklist",
    "Final Boundary Statement",
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

    if result.source_artifact_count < 6:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}")

    if result.section_count < 18:
        errors.append(f"Section count too low: {result.section_count}")

    if result.word_count < 1500:
        errors.append(f"Word count too low for public technical preview: {result.word_count}")

    if result.boundary_phrase_count < 12:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.public_section_count < 14:
        errors.append(f"Public section count too low: {result.public_section_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.limitation_count < 20:
        errors.append(f"Limitation language count too low: {result.limitation_count}")

    if result.next_step_count < 6:
        errors.append(f"Next-step count too low: {result.next_step_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 40: Public Technical Preview Package")
    print(
        "Question: Can Viruse Fabric produce a public-safe technical preview "
        "without overclaiming or inventing citations?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Section count: {result.section_count}")
    print(f"Word count: {result.word_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Public section count: {result.public_section_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Limitation language count: {result.limitation_count}")
    print(f"Next-step count: {result.next_step_count}")
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

    print("Experiment 40 completed successfully.")


if __name__ == "__main__":
    main()
