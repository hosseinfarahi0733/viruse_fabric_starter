"""Experiment 47: Literature Search Protocol.

This experiment runs the v4.7 literature search protocol generator.

It verifies that the project can define a real future literature-search
protocol without adding citations, inventing sources, overclaiming, or
weakening project boundaries.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.literature_search_protocol import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Literature Search Protocol v4.7",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "No citation is added by this protocol",
    "Citation placeholders are not citations",
    "Search Venues",
    "Literature Families",
    "Claim-to-Literature Map",
    "Inclusion Criteria",
    "Exclusion Criteria",
    "Search Procedure",
    "Evidence Record Template",
    "Source Evaluation Notes",
    "Claim Discipline",
    "Search Log Requirements",
    "Boundary Phrases",
    "Prohibited Behaviors",
    "v4.8 — Literature Family Evidence Matrix",
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

    if result.source_artifact_count < 4:
        errors.append(f"Source artifact count too low: {result.source_artifact_count}")

    if result.missing_source_artifact_count != 0:
        errors.append(
            f"Missing source artifact count should be zero, got: {result.missing_source_artifact_count}"
        )

    if result.search_venue_count < 7:
        errors.append(f"Search venue count too low: {result.search_venue_count}")

    if result.literature_family_count < 8:
        errors.append(f"Literature family count too low: {result.literature_family_count}")

    if result.future_query_count < 32:
        errors.append(f"Future query count too low: {result.future_query_count}")

    if result.claim_category_count < 8:
        errors.append(f"Claim category count too low: {result.claim_category_count}")

    if result.inclusion_criteria_count < 8:
        errors.append(f"Inclusion criteria count too low: {result.inclusion_criteria_count}")

    if result.exclusion_criteria_count < 8:
        errors.append(f"Exclusion criteria count too low: {result.exclusion_criteria_count}")

    if result.search_step_count < 10:
        errors.append(f"Search step count too low: {result.search_step_count}")

    if result.boundary_phrase_count < 9:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.prohibited_behavior_count < 8:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.word_count < 1200:
        errors.append(f"Word count too low for literature search protocol: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 47: Literature Search Protocol")
    print(
        "Question: Can Viruse Fabric define a real literature-search protocol "
        "without adding citations or inventing sources?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Search venue count: {result.search_venue_count}")
    print(f"Literature family count: {result.literature_family_count}")
    print(f"Future query count: {result.future_query_count}")
    print(f"Claim category count: {result.claim_category_count}")
    print(f"Inclusion criteria count: {result.inclusion_criteria_count}")
    print(f"Exclusion criteria count: {result.exclusion_criteria_count}")
    print(f"Search step count: {result.search_step_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
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

    print("Experiment 47 completed successfully.")


if __name__ == "__main__":
    main()
