"""Experiment 50: Citation-Grounded Manuscript Revision Plan.

This experiment runs the v5.0 citation-grounded manuscript revision plan.

It verifies that the project can connect the manuscript, literature search
protocol, evidence matrix, and claim readiness map into a controlled future
revision plan without adding sources, adding citations, revising the manuscript,
or implying submission readiness.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.citation_grounded_manuscript_revision_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Citation-Grounded Manuscript Revision Plan v5.0",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "No citation is added by this plan",
    "No source is added by this plan",
    "The manuscript is not revised by this plan",
    "Citation placeholders are not citations",
    "Source Artifacts",
    "Revision Target Map",
    "Revision Phases",
    "Manuscript Revision Gates",
    "Readiness Statements",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "Integration Logic",
    "Revision Discipline",
    "Manuscript Section Handling",
    "Source Integration Order",
    "Revision Output Boundary",
    "Source added count",
    "Citation added count",
    "Manuscript revised count",
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

    if result.source_artifact_count < 6:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.revision_target_count < 8:
        errors.append(f"Revision target count too low: {result.revision_target_count}")

    if result.revision_phase_count < 8:
        errors.append(f"Revision phase count too low: {result.revision_phase_count}")

    if result.manuscript_gate_count < 10:
        errors.append(f"Manuscript gate count too low: {result.manuscript_gate_count}")

    if result.boundary_phrase_count < 11:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.readiness_statement_count < 8:
        errors.append(f"Readiness statement count too low: {result.readiness_statement_count}")

    if result.prohibited_behavior_count < 10:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.source_added_count != 0:
        errors.append(f"Source added count should be zero, got: {result.source_added_count}")

    if result.citation_added_count != 0:
        errors.append(f"Citation added count should be zero, got: {result.citation_added_count}")

    if result.manuscript_revised_count != 0:
        errors.append(
            f"Manuscript revised count should be zero, got: {result.manuscript_revised_count}"
        )

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(
            f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}"
        )

    if result.word_count < 1100:
        errors.append(
            f"Word count too low for citation-grounded manuscript revision plan: {result.word_count}"
        )

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 50: Citation-Grounded Manuscript Revision Plan")
    print(
        "Question: Can Viruse Fabric connect manuscript revision planning to "
        "citation protocol, evidence matrix, and claim readiness without adding "
        "sources, citations, or manuscript revisions?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Revision target count: {result.revision_target_count}")
    print(f"Revision phase count: {result.revision_phase_count}")
    print(f"Manuscript gate count: {result.manuscript_gate_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Readiness statement count: {result.readiness_statement_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
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

    print("Experiment 50 completed successfully.")


if __name__ == "__main__":
    main()
