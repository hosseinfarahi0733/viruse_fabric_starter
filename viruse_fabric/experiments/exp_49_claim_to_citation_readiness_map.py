"""Experiment 49: Claim-to-Citation Readiness Map.

This experiment runs the v4.9 claim-to-citation readiness map generator.

It verifies that project claims can be classified by citation readiness,
evidence need, allowed use, and validation boundary without adding sources,
adding citations, inventing references, or implying submission readiness.

The official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.claim_to_citation_readiness_map import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Claim-to-Citation Readiness Map v4.9",
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "No citation is added by this map",
    "No source is added by this map",
    "Citation placeholders are not citations",
    "Source Artifacts",
    "Readiness Category Summary",
    "Claim-to-Citation Map",
    "Citation Actions",
    "Claim Use Levels",
    "Evidence Needs",
    "Map Rules",
    "Prohibited Behaviors",
    "Claim Readiness Notes",
    "Manuscript Integration Notes",
    "Public Communication Notes",
    "Source added count",
    "Citation added count",
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

    if result.claim_count < 8:
        errors.append(f"Claim count too low: {result.claim_count}")

    if result.readiness_category_count < 6:
        errors.append(f"Readiness category count too low: {result.readiness_category_count}")

    if result.citation_action_count < 6:
        errors.append(f"Citation action count too low: {result.citation_action_count}")

    if result.claim_use_level_count < 6:
        errors.append(f"Claim use level count too low: {result.claim_use_level_count}")

    if result.evidence_need_count < 8:
        errors.append(f"Evidence need count too low: {result.evidence_need_count}")

    if result.map_row_count < 8:
        errors.append(f"Map row count too low: {result.map_row_count}")

    if result.literature_needed_count < 2:
        errors.append(f"Literature-needed count too low: {result.literature_needed_count}")

    if result.boundary_rule_count < 3:
        errors.append(f"Boundary rule count too low: {result.boundary_rule_count}")

    if result.internal_status_count < 1:
        errors.append(f"Internal status count too low: {result.internal_status_count}")

    if result.source_added_count != 0:
        errors.append(f"Source added count should be zero, got: {result.source_added_count}")

    if result.citation_added_count != 0:
        errors.append(f"Citation added count should be zero, got: {result.citation_added_count}")

    if result.boundary_phrase_count < 10:
        errors.append(f"Boundary phrase count too low: {result.boundary_phrase_count}")

    if result.map_rule_count < 10:
        errors.append(f"Map rule count too low: {result.map_rule_count}")

    if result.prohibited_behavior_count < 10:
        errors.append(f"Prohibited behavior count too low: {result.prohibited_behavior_count}")

    if result.next_step_count < 8:
        errors.append(f"Next step count too low: {result.next_step_count}")

    if result.overclaim_count != 0:
        errors.append(f"Overclaim count should be zero, got: {result.overclaim_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.word_count < 1300:
        errors.append(f"Word count too low for claim-to-citation readiness map: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 49: Claim-to-Citation Readiness Map")
    print(
        "Question: Can Viruse Fabric classify project claims by citation readiness "
        "without adding sources or citations?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Claim count: {result.claim_count}")
    print(f"Readiness category count: {result.readiness_category_count}")
    print(f"Citation action count: {result.citation_action_count}")
    print(f"Claim use level count: {result.claim_use_level_count}")
    print(f"Evidence need count: {result.evidence_need_count}")
    print(f"Map row count: {result.map_row_count}")
    print(f"Citation-ready count: {result.citation_ready_count}")
    print(f"Literature-needed count: {result.literature_needed_count}")
    print(f"Future-validation-needed count: {result.future_validation_needed_count}")
    print(f"Boundary rule count: {result.boundary_rule_count}")
    print(f"Internal status count: {result.internal_status_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Map rule count: {result.map_rule_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
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

    print("Experiment 49 completed successfully.")


if __name__ == "__main__":
    main()
