"""Experiment 39: Citation Placeholder Plan.

This experiment runs the v3.9 citation placeholder and literature mapping plan.

It verifies that the project can prepare a citation-safe map for later
literature search without inventing citations, references, authors, dates,
DOIs, arXiv identifiers, or bibliography entries.

The experiment preserves the project status:

research prototype with internal validation
"""

from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.citation_placeholder_plan import (
    PROJECT_ROOT,
    generate_report,
)


REQUIRED_REPORT_PHRASES = [
    "Citation Placeholder Plan v3.9",
    "research prototype with internal validation",
    "not a bibliography",
    "not a literature review",
    "not a submission-ready reference section",
    "Literature Families",
    "Citation Slot Plan",
    "No slot is a citation",
    "Internal-Only Claims",
    "Prohibited Citation Behaviors",
    "Readiness Boundaries",
    "Search Workflow for Later Versions",
    "Claim Classification Rules",
    "The manuscript remains not submission-ready",
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

    if not result.source_manuscript_exists:
        errors.append("Source integrated manuscript is missing.")

    if not result.source_audit_exists:
        errors.append("Source integrated manuscript audit is missing.")

    if result.literature_family_count < 8:
        errors.append(f"Literature family count too low: {result.literature_family_count}")

    if result.citation_slot_count < 8:
        errors.append(f"Citation slot count too low: {result.citation_slot_count}")

    if result.query_count < 24:
        errors.append(f"Future query count too low: {result.query_count}")

    if result.internal_only_claim_count < 4:
        errors.append(f"Internal-only claim count too low: {result.internal_only_claim_count}")

    if result.prohibited_behavior_count < 8:
        errors.append(f"Prohibited citation behavior count too low: {result.prohibited_behavior_count}")

    if result.readiness_boundary_count < 6:
        errors.append(f"Readiness boundary count too low: {result.readiness_boundary_count}")

    if result.fake_citation_count != 0:
        errors.append(f"Fake citation-like pattern count should be zero, got: {result.fake_citation_count}")

    if result.word_count < 1400:
        errors.append(f"Word count too low for citation planning artifact: {result.word_count}")

    if missing_phrases:
        errors.append(f"Missing required report phrases: {len(missing_phrases)}")

    passed = not errors and result.passed

    print("Experiment 39: Citation Placeholder Plan")
    print(
        "Question: Can the integrated manuscript prepare a citation-safe literature "
        "mapping plan without inventing citations?"
    )
    print(f"Title: {result.title}")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source manuscript exists: {result.source_manuscript_exists}")
    print(f"Source audit exists: {result.source_audit_exists}")
    print(f"Literature family count: {result.literature_family_count}")
    print(f"Citation slot count: {result.citation_slot_count}")
    print(f"Future query count: {result.query_count}")
    print(f"Internal-only claim count: {result.internal_only_claim_count}")
    print(f"Prohibited citation behavior count: {result.prohibited_behavior_count}")
    print(f"Readiness boundary count: {result.readiness_boundary_count}")
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

    print("Experiment 39 completed successfully.")


if __name__ == "__main__":
    main()
