"""Experiment 46: Public Release Readiness Audit.

This experiment runs the v4.6 public release readiness audit.

It verifies that the public-safe release path is internally complete,
bounded, citation-safe, and free from overclaim, while remaining clearly
not externally validated and not submission-ready.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.public_release_readiness_audit import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Public Release Readiness Audit v4.6",
    "research prototype with internal validation",
    "ready for cautious public orientation",
    "not ready for submission",
    "not externally validated",
    "not a final paper",
    "not a validation claim",
    "Public Path Artifact Check",
    "Supporting Artifact Check",
    "Readiness Dimensions",
    "Release Path Gates",
    "Boundary Retention",
    "Readiness Statements",
    "Approved Use Cases",
    "Disallowed Use Cases",
    "Risk Register",
    "Readiness Verdict",
    "What This Audit Does Not Mean",
    "Public Orientation Readiness",
    "Remaining Work Before Submission",
    "Transformation Rule",
    "visual or slide versions require a separate audit",
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

    if result.public_artifact_count < 6:
        errors.append(f"Public artifact count too low: {result.public_artifact_count}")

    if result.missing_public_artifact_count != 0:
        errors.append(
            f"Missing public artifact count should be zero, got: {result.missing_public_artifact_count}"
        )

    if result.supporting_artifact_count < 3:
        errors.append(f"Supporting artifact count too low: {result.supporting_artifact_count}")

    if result.missing_supporting_artifact_count != 0:
        errors.append(
            f"Missing supporting artifact count should be zero, got: {result.missing_supporting_artifact_count}"
        )

    if result.readiness_dimension_count < 10:
        errors.append(f"Readiness dimension count too low: {result.readiness_dimension_count}")

    if result.boundary_phrase_count < 10:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.readiness_statement_count < 10:
        errors.append(f"Readiness statement count too low: {result.readiness_statement_count}")

    if result.release_gate_count < 12:
        errors.append(f"Release gate count too low: {result.release_gate_count}")

    if result.risk_item_count < 8:
        errors.append(f"Risk item count too low: {result.risk_item_count}")

    if result.approved_use_case_count < 6:
        errors.append(f"Approved use case count too low: {result.approved_use_case_count}")

    if result.disallowed_use_case_count < 8:
        errors.append(f"Disallowed use case count too low: {result.disallowed_use_case_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.readiness_score < 95:
        errors.append(f"Readiness score too low: {result.readiness_score}")

    if result.word_count < 950:
        errors.append(f"Word count too low for public release readiness audit: {result.word_count}")

    if "ready for cautious public orientation" not in result.verdict:
        errors.append("Verdict does not include cautious public orientation readiness.")

    if "not ready for submission" not in result.verdict:
        errors.append("Verdict does not include submission boundary.")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 46: Public Release Readiness Audit")
    print(
        "Question: Is the public-safe release path ready for cautious public "
        "orientation while remaining not submission-ready?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Public artifact count: {result.public_artifact_count}")
    print(f"Missing public artifact count: {result.missing_public_artifact_count}")
    print(f"Supporting artifact count: {result.supporting_artifact_count}")
    print(f"Missing supporting artifact count: {result.missing_supporting_artifact_count}")
    print(f"Readiness dimension count: {result.readiness_dimension_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Readiness statement count: {result.readiness_statement_count}")
    print(f"Release gate count: {result.release_gate_count}")
    print(f"Risk item count: {result.risk_item_count}")
    print(f"Approved use case count: {result.approved_use_case_count}")
    print(f"Disallowed use case count: {result.disallowed_use_case_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Readiness score: {result.readiness_score}")
    print(f"Word count: {result.word_count}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Passed: {passed}")
    print(f"Report exists: {result.output_path.exists()}")
    print(f"Report size: {result.output_path.stat().st_size if result.output_path.exists() else 0}")
    print(f"Missing required report phrases: {len(missing_phrases)}")
    print(f"Verdict: {result.verdict}")
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

    print("Experiment 46 completed successfully.")


if __name__ == "__main__":
    main()
