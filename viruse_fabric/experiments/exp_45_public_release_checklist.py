"""Experiment 45: Public Release Checklist.

This experiment runs the v4.5 public release checklist generator.

It verifies that the public release bundle can be converted into practical
release gates, allowed language, disallowed language, audit requirements,
and boundary-preserving release rules.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.public_release_checklist import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Public Release Checklist v4.5",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "Required Artifact Check",
    "Release Gates",
    "Allowed Public Language",
    "Disallowed Public Language",
    "Boundary Phrases",
    "Audit Requirements",
    "Release Procedure",
    "Checklist Use Notes",
    "Public Release Decision Rule",
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

    if not result.source_exists:
        errors.append("Source bundle index is missing.")

    if result.required_artifact_count < 8:
        errors.append(f"Required artifact count too low: {result.required_artifact_count}")

    if result.missing_artifact_count != 0:
        errors.append(f"Missing artifact count should be zero, got: {result.missing_artifact_count}")

    if result.release_gate_count < 12:
        errors.append(f"Release gate count too low: {result.release_gate_count}")

    if result.allowed_language_count < 9:
        errors.append(f"Allowed language count too low: {result.allowed_language_count}")

    if result.disallowed_language_count < 9:
        errors.append(f"Disallowed language count too low: {result.disallowed_language_count}")

    if result.boundary_phrase_count < 9:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.audit_requirement_count < 6:
        errors.append(f"Audit requirement count too low: {result.audit_requirement_count}")

    if result.next_step_count < 6:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.word_count < 850:
        errors.append(f"Word count too low for public release checklist: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 45: Public Release Checklist")
    print(
        "Question: Can Viruse Fabric convert the public release bundle into "
        "practical release gates without weakening boundaries?"
    )
    print(f"Title: {result.title}")
    print(f"Source bundle index: {result.source_bundle_index.relative_to(PROJECT_ROOT)}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source exists: {result.source_exists}")
    print(f"Required artifact count: {result.required_artifact_count}")
    print(f"Missing artifact count: {result.missing_artifact_count}")
    print(f"Release gate count: {result.release_gate_count}")
    print(f"Allowed language count: {result.allowed_language_count}")
    print(f"Disallowed language count: {result.disallowed_language_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Audit requirement count: {result.audit_requirement_count}")
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

    print("Experiment 45 completed successfully.")


if __name__ == "__main__":
    main()
