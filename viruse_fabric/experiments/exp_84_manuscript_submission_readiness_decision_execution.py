"""Experiment 84: manuscript submission readiness decision execution.

This experiment validates that v8.4 executes the planned decision rows while
keeping the manuscript not submission-ready and preserving all scientific
boundaries.
"""

from __future__ import annotations

import re
from pathlib import Path

from viruse_fabric.writing.manuscript_submission_readiness_decision_execution import (
    BOUNDARY_PHRASES,
    HARD_GATES,
    NEXT_STEPS,
    OUTPUT_PATH,
    PROHIBITED_BEHAVIORS,
    REQUIRED_SOURCE_PATHS,
    SOURCE_ARTIFACT_COUNT,
    write_report,
)


TITLE = "Experiment 84: Manuscript Submission Readiness Decision Execution"
QUESTION = (
    "Can Viruse Fabric execute manuscript submission readiness decision rows "
    "while keeping manuscript submission readiness, formal proof, independent "
    "experiment, external validation, and new citation additions unavailable?"
)

REQUIRED_REPORT_PHRASES = [
    "Manuscript Submission Readiness Decision Execution v8.4",
    "submission_readiness_decision_execution: yes",
    "submission_readiness_decision_execution_count: 1",
    "executed_decision_row_count: 2",
    "manuscript_submission_ready_count: 0",
    "not_ready_decision_count: 2",
    "new_citation_added_count: 0",
    "conditional_hold_count: 1",
    "MSRDE-ROW-0001 -> SRDP-ROW-0001 -> SRAE-ROW-0001",
    "MSRDE-ROW-0002 -> SRDP-ROW-0002 -> SRAE-ROW-0002",
    "decision_outcome: not_ready",
    "formal_mathematical_proof: no",
    "independent_experiment: no",
    "external_validation: no",
    "CAND-0003 remains conditional hold",
    "research prototype with internal validation",
    "This is a decision execution milestone, not a submission-readiness milestone.",
]

OVERCLAIM_PATTERNS = [
    r"\bmanuscript_submission_ready:\s*yes\b",
    r"\bmanuscript_submission_ready_count:\s*[1-9][0-9]*\b",
    r"\bformal_mathematical_proof:\s*yes\b",
    r"\bindependent_experiment:\s*yes\b",
    r"\bexternal_validation:\s*yes\b",
    r"\bnew_citation_added:\s*yes\b",
    r"\bnew_citation_added_count:\s*[1-9][0-9]*\b",
    r"\breadiness_approval:\s*yes\b",
    r"\bvenue_acceptance:\s*yes\b",
    r"\bpeer_reviewed_manuscript:\s*yes\b",
    r"\bdecision_outcome:\s*ready\b",
    r"\bdecision_outcome:\s*approved\b",
]

INVENTED_CITATION_LIKE_PATTERNS = [
    r"\[[0-9]{1,3}\]",
    r"\([A-Z][A-Za-z\-]+,\s*20[0-9]{2}\)",
]


def _word_count(text: str) -> int:
    return len(re.findall(r"\b\S+\b", text))


def _count_heading_rows(text: str) -> int:
    row_ids = re.findall(
        r"^\s*###\s+(MSRDE-ROW-\d{4})\s*$",
        text,
        flags=re.MULTILINE,
    )
    return len(set(row_ids))


def _count_pattern_list(text: str, patterns: list[str]) -> int:
    return sum(len(re.findall(pattern, text)) for pattern in patterns)


def run() -> dict[str, object]:
    report = write_report()

    missing_sources = [str(path) for path in REQUIRED_SOURCE_PATHS if not Path(path).exists()]
    missing_required_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    executed_decision_row_count = _count_heading_rows(report)
    submission_readiness_decision_execution_count = report.count(
        "submission_readiness_decision_execution: yes"
    )
    manuscript_submission_ready_count = report.count("manuscript_submission_ready: yes")
    not_ready_decision_count = report.count("decision_outcome: not_ready")
    new_citation_added_count = report.count("new_citation_added: yes")

    conditional_hold_count = 1 if "conditional_hold_count: 1" in report else 0

    hard_gate_count = report.count("hard_gate:")
    boundary_phrase_count = report.count("boundary_phrase:")
    prohibited_behavior_count = report.count("prohibited_behavior:")
    next_step_count = report.count("next_step:")

    overclaim_count = _count_pattern_list(report, OVERCLAIM_PATTERNS)
    invented_citation_like_pattern_count = _count_pattern_list(
        report,
        INVENTED_CITATION_LIKE_PATTERNS,
    )

    errors: list[str] = []

    if missing_sources:
        errors.append(f"Missing required source artifacts: {missing_sources}")

    if missing_required_phrases:
        errors.append(f"Missing required report phrases: {missing_required_phrases}")

    if SOURCE_ARTIFACT_COUNT != 34:
        errors.append(f"Expected source artifact count 34, got {SOURCE_ARTIFACT_COUNT}")

    if executed_decision_row_count != 2:
        errors.append(
            f"Expected 2 executed decision rows, got {executed_decision_row_count}"
        )

    if submission_readiness_decision_execution_count != 1:
        errors.append(
            "Expected exactly one submission readiness decision execution marker, "
            f"got {submission_readiness_decision_execution_count}"
        )

    if manuscript_submission_ready_count != 0:
        errors.append(
            f"Expected manuscript submission ready count 0, got {manuscript_submission_ready_count}"
        )

    if not_ready_decision_count != 2:
        errors.append(f"Expected 2 not-ready decisions, got {not_ready_decision_count}")

    if new_citation_added_count != 0:
        errors.append(f"Expected new citation added count 0, got {new_citation_added_count}")

    if conditional_hold_count != 1:
        errors.append(f"Expected conditional hold count 1, got {conditional_hold_count}")

    if hard_gate_count != len(HARD_GATES):
        errors.append(f"Expected hard gate count {len(HARD_GATES)}, got {hard_gate_count}")

    if boundary_phrase_count != len(BOUNDARY_PHRASES):
        errors.append(
            f"Expected boundary phrase count {len(BOUNDARY_PHRASES)}, got {boundary_phrase_count}"
        )

    if prohibited_behavior_count != len(PROHIBITED_BEHAVIORS):
        errors.append(
            "Expected prohibited behavior count "
            f"{len(PROHIBITED_BEHAVIORS)}, got {prohibited_behavior_count}"
        )

    if next_step_count != len(NEXT_STEPS):
        errors.append(f"Expected next step count {len(NEXT_STEPS)}, got {next_step_count}")

    if overclaim_count != 0:
        errors.append(f"Expected overclaim count 0, got {overclaim_count}")

    if invented_citation_like_pattern_count != 0:
        errors.append(
            "Expected invented citation-like pattern count 0, got "
            f"{invented_citation_like_pattern_count}"
        )

    warnings = [
        "Decision execution exists, but the executed decision is not-ready.",
        "No formal mathematical proof, independent experiment, or external validation is created.",
    ]

    report_exists = OUTPUT_PATH.exists()
    report_size = OUTPUT_PATH.stat().st_size if report_exists else 0

    result = {
        "title": TITLE,
        "question": QUESTION,
        "output_path": str(OUTPUT_PATH),
        "source_artifact_count": SOURCE_ARTIFACT_COUNT,
        "missing_source_artifact_count": len(missing_sources),
        "submission_readiness_decision_execution_count": submission_readiness_decision_execution_count,
        "executed_decision_row_count": executed_decision_row_count,
        "manuscript_submission_ready_count": manuscript_submission_ready_count,
        "not_ready_decision_count": not_ready_decision_count,
        "new_citation_added_count": new_citation_added_count,
        "conditional_hold_count": conditional_hold_count,
        "hard_gate_count": hard_gate_count,
        "boundary_phrase_count": boundary_phrase_count,
        "prohibited_behavior_count": prohibited_behavior_count,
        "next_step_count": next_step_count,
        "overclaim_count": overclaim_count,
        "invented_citation_like_pattern_count": invented_citation_like_pattern_count,
        "word_count": _word_count(report),
        "errors": errors,
        "warnings": warnings,
        "passed": not errors,
        "report_exists": report_exists,
        "report_size": report_size,
        "missing_required_report_phrases": len(missing_required_phrases),
        "interpretation": (
            "The v8.4 artifact executes two planned manuscript submission readiness "
            "decision rows, and both executed decisions remain not-ready while formal "
            "proof, independent experiment, external validation, manuscript submission "
            "readiness, and new citation additions remain unavailable."
        ),
    }

    return result


def main() -> None:
    result = run()

    print(TITLE)
    print(f"Question: {QUESTION}")
    print("Title: Manuscript Submission Readiness Decision Execution v8.4")
    print(f"Output path: {result['output_path']}")
    print(f"Source artifact count: {result['source_artifact_count']}")
    print(f"Missing source artifact count: {result['missing_source_artifact_count']}")
    print(
        "Submission readiness decision execution count: "
        f"{result['submission_readiness_decision_execution_count']}"
    )
    print(f"Executed decision row count: {result['executed_decision_row_count']}")
    print(f"Manuscript submission ready count: {result['manuscript_submission_ready_count']}")
    print(f"Not-ready decision count: {result['not_ready_decision_count']}")
    print(f"New citation added count: {result['new_citation_added_count']}")
    print(f"Conditional hold count: {result['conditional_hold_count']}")
    print(f"Hard gate count: {result['hard_gate_count']}")
    print(f"Boundary phrase count: {result['boundary_phrase_count']}")
    print(f"Prohibited behavior count: {result['prohibited_behavior_count']}")
    print(f"Next step count: {result['next_step_count']}")
    print(f"Overclaim count: {result['overclaim_count']}")
    print(
        "Invented citation-like pattern count: "
        f"{result['invented_citation_like_pattern_count']}"
    )
    print(f"Word count: {result['word_count']}")
    print(f"Errors: {len(result['errors'])}")
    print(f"Warnings: {len(result['warnings'])}")
    print(f"Passed: {result['passed']}")
    print(f"Report exists: {result['report_exists']}")
    print(f"Report size: {result['report_size']}")
    print(
        "Missing required report phrases: "
        f"{result['missing_required_report_phrases']}"
    )
    print(f"Interpretation: {result['interpretation']}")

    if result["warnings"]:
        print("Warnings:")
        for warning in result["warnings"]:
            print(f"- {warning}")

    if result["errors"]:
        print("Errors:")
        for error in result["errors"]:
            print(f"- {error}")
        raise SystemExit(1)

    print("Experiment 84 completed successfully.")


if __name__ == "__main__":
    main()
