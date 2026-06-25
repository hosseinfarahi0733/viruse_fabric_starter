"""Experiment 44: Public Release Bundle Index.

This experiment runs the v4.4 public release bundle index generator.

It verifies that the project can organize its public-safe release artifacts
without overclaiming, inventing citations, weakening boundaries, or implying
external validation or submission readiness.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.public_release_bundle_index import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Public Release Bundle Index v4.4",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "Artifact Table",
    "Artifact Details",
    "Required Boundary Phrases",
    "Unsafe Uses",
    "Release Gates",
    "Recommended Next Steps",
    "Audience Map",
    "citation placeholders are not citations",
    "does not certify external validation",
    "biological guidance",
    "clinical guidance",
    "laboratory guidance",
    "operational guidance",
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

    if result.artifact_count < 8:
        errors.append(f"Artifact count too low: {result.artifact_count}")

    if result.missing_artifact_count != 0:
        errors.append(f"Missing artifact count should be zero, got: {result.missing_artifact_count}")

    if result.audience_count < 6:
        errors.append(f"Audience count too low: {result.audience_count}")

    if result.status_count < 5:
        errors.append(f"Status count too low: {result.status_count}")

    if result.boundary_phrase_count < 9:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.unsafe_use_count < 7:
        errors.append(f"Unsafe use count too low: {result.unsafe_use_count}")

    if result.release_gate_count < 6:
        errors.append(f"Release gate count too low: {result.release_gate_count}")

    if result.next_step_count < 6:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.word_count < 900:
        errors.append(f"Word count too low for release bundle index: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 44: Public Release Bundle Index")
    print(
        "Question: Can Viruse Fabric organize its public-safe release artifacts "
        "without weakening boundaries or overclaiming?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Artifact count: {result.artifact_count}")
    print(f"Missing artifact count: {result.missing_artifact_count}")
    print(f"Audience count: {result.audience_count}")
    print(f"Status count: {result.status_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Unsafe use count: {result.unsafe_use_count}")
    print(f"Release gate count: {result.release_gate_count}")
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

    print("Experiment 44 completed successfully.")


if __name__ == "__main__":
    main()
