"""Experiment 85: manuscript submission readiness blocking gap register."""

from __future__ import annotations

import re
from pathlib import Path

from viruse_fabric.writing.manuscript_submission_readiness_blocking_gap_register import (
    BOUNDARY_PHRASES,
    GAP_ROWS,
    HARD_ZERO_FIELDS,
    NEXT_STEPS,
    OUTPUT_PATH,
    PROHIBITED_BEHAVIORS,
    REQUIRED_SOURCE_PATHS,
    SOURCE_ARTIFACT_COUNT,
    write_report,
)


TITLE = "Experiment 85: Manuscript Submission Readiness Blocking Gap Register"
QUESTION = (
    "Can Viruse Fabric register the blockers behind the v8.4 not-ready decision "
    "while keeping gap resolution, submission readiness, formal proof, independent "
    "experiment, external validation, and new citation additions at zero?"
)

REQUIRED_REPORT_PHRASES = [
    "Manuscript Submission Readiness Blocking Gap Register v8.5",
    "blocking_gap_register_count: 1",
    "blocking_gap_row_count: 4",
    "primary_submission_blocker_count: 3",
    "citation_boundary_gap_count: 1",
    "gap_resolution_count: 0",
    "manuscript_submission_ready_count: 0",
    "readiness_approval_count: 0",
    "formal_mathematical_proof_count: 0",
    "independent_experiment_count: 0",
    "external_validation_count: 0",
    "new_citation_added_count: 0",
    "CAND_0003_conditional_hold_count: 1",
    "MSRBG-ROW-0001",
    "MSRBG-ROW-0002",
    "MSRBG-ROW-0003",
    "MSRBG-ROW-0004",
    "formal_mathematical_proof_gap",
    "independent_experiment_gap",
    "external_validation_gap",
    "CAND_0003_retention_boundary_gap",
    "CAND-0003 remains conditional hold",
    "research prototype with internal validation",
]

OVERCLAIM_PATTERNS = [
    r"\bgap_resolved:\s*yes\b",
    r"\bgap_resolution_count:\s*[1-9][0-9]*\b",
    r"\bmanuscript_submission_ready:\s*yes\b",
    r"\bmanuscript_submission_ready_count:\s*[1-9][0-9]*\b",
    r"\breadiness_approval:\s*yes\b",
    r"\breadiness_approval_count:\s*[1-9][0-9]*\b",
    r"\bformal_mathematical_proof:\s*yes\b",
    r"\bformal_mathematical_proof_count:\s*[1-9][0-9]*\b",
    r"\bindependent_experiment:\s*yes\b",
    r"\bindependent_experiment_count:\s*[1-9][0-9]*\b",
    r"\bexternal_validation:\s*yes\b",
    r"\bexternal_validation_count:\s*[1-9][0-9]*\b",
    r"\bnew_citation_added:\s*yes\b",
    r"\bnew_citation_added_count:\s*[1-9][0-9]*\b",
]

INVENTED_CITATION_LIKE_PATTERNS = [
    r"\[[0-9]{1,3}\]",
    r"\([A-Z][A-Za-z\-]+,\s*20[0-9]{2}\)",
]


def _word_count(text: str) -> int:
    return len(re.findall(r"\b\S+\b", text))


def _count_gap_rows(text: str) -> int:
    row_ids = re.findall(
        r"^\s*###\s+(MSRBG-ROW-\d{4})\s*$",
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

    blocking_gap_register_count = report.count("blocking_gap_register_count: 1")
    blocking_gap_row_count = _count_gap_rows(report)
    primary_submission_blocker_count = report.count("severity: hard_blocker")
    citation_boundary_gap_count = report.count("severity: citation_boundary_hold")
    unresolved_gap_count = report.count("gap_resolved: no")
    gap_resolution_count = report.count("gap_resolved: yes")
    manuscript_submission_ready_count = report.count("manuscript_submission_ready: yes")
    readiness_approval_count = report.count("readiness_approval: yes")
    formal_mathematical_proof_count = report.count("formal_mathematical_proof: yes")
    independent_experiment_count = report.count("independent_experiment: yes")
    external_validation_count = report.count("external_validation: yes")
    new_citation_added_count = report.count("new_citation_added: yes")
    conditional_hold_count = 1 if "CAND_0003_conditional_hold_count: 1" in report else 0

    hard_zero_count = report.count("hard_zero:")
    boundary_phrase_count = report.count("boundary_phrase:")
    prohibited_behavior_count = report.count("prohibited_behavior:")
    next_step_count = len(re.findall(r"^\s*-\s+next_step:", report, flags=re.MULTILINE))

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

    if SOURCE_ARTIFACT_COUNT != 35:
        errors.append(f"Expected source artifact count 35, got {SOURCE_ARTIFACT_COUNT}")

    if blocking_gap_register_count != 1:
        errors.append(
            f"Expected blocking gap register count 1, got {blocking_gap_register_count}"
        )

    if blocking_gap_row_count != len(GAP_ROWS):
        errors.append(f"Expected {len(GAP_ROWS)} blocking gap rows, got {blocking_gap_row_count}")

    if primary_submission_blocker_count != 3:
        errors.append(
            f"Expected 3 primary submission blockers, got {primary_submission_blocker_count}"
        )

    if citation_boundary_gap_count != 1:
        errors.append(f"Expected 1 citation boundary gap, got {citation_boundary_gap_count}")

    if unresolved_gap_count != 4:
        errors.append(f"Expected 4 unresolved gaps, got {unresolved_gap_count}")

    zero_checks = {
        "gap_resolution_count": gap_resolution_count,
        "manuscript_submission_ready_count": manuscript_submission_ready_count,
        "readiness_approval_count": readiness_approval_count,
        "formal_mathematical_proof_count": formal_mathematical_proof_count,
        "independent_experiment_count": independent_experiment_count,
        "external_validation_count": external_validation_count,
        "new_citation_added_count": new_citation_added_count,
    }

    for name, value in zero_checks.items():
        if value != 0:
            errors.append(f"Expected {name} 0, got {value}")

    if conditional_hold_count != 1:
        errors.append(f"Expected conditional hold count 1, got {conditional_hold_count}")

    if hard_zero_count != len(HARD_ZERO_FIELDS):
        errors.append(f"Expected hard zero count {len(HARD_ZERO_FIELDS)}, got {hard_zero_count}")

    if boundary_phrase_count != len(BOUNDARY_PHRASES):
        errors.append(
            f"Expected boundary phrase count {len(BOUNDARY_PHRASES)}, got {boundary_phrase_count}"
        )

    if prohibited_behavior_count != len(PROHIBITED_BEHAVIORS):
        errors.append(
            f"Expected prohibited behavior count {len(PROHIBITED_BEHAVIORS)}, got {prohibited_behavior_count}"
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
        "Blocking gaps are registered, but no gap is resolved.",
        "Manuscript submission readiness remains unavailable.",
        "No formal proof, independent experiment, or external validation is created.",
    ]

    report_exists = OUTPUT_PATH.exists()
    report_size = OUTPUT_PATH.stat().st_size if report_exists else 0

    return {
        "title": TITLE,
        "question": QUESTION,
        "output_path": str(OUTPUT_PATH),
        "source_artifact_count": SOURCE_ARTIFACT_COUNT,
        "missing_source_artifact_count": len(missing_sources),
        "blocking_gap_register_count": blocking_gap_register_count,
        "blocking_gap_row_count": blocking_gap_row_count,
        "primary_submission_blocker_count": primary_submission_blocker_count,
        "citation_boundary_gap_count": citation_boundary_gap_count,
        "unresolved_gap_count": unresolved_gap_count,
        "gap_resolution_count": gap_resolution_count,
        "manuscript_submission_ready_count": manuscript_submission_ready_count,
        "readiness_approval_count": readiness_approval_count,
        "formal_mathematical_proof_count": formal_mathematical_proof_count,
        "independent_experiment_count": independent_experiment_count,
        "external_validation_count": external_validation_count,
        "new_citation_added_count": new_citation_added_count,
        "conditional_hold_count": conditional_hold_count,
        "hard_zero_count": hard_zero_count,
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
            "The v8.5 artifact registers four unresolved blocking gaps after the "
            "v8.4 not-ready decision execution while keeping gap resolution, "
            "submission readiness, formal proof, independent experiment, external "
            "validation, and new citation additions at zero."
        ),
    }


def main() -> None:
    result = run()

    print(TITLE)
    print(f"Question: {QUESTION}")
    print("Title: Manuscript Submission Readiness Blocking Gap Register v8.5")
    print(f"Output path: {result['output_path']}")
    print(f"Source artifact count: {result['source_artifact_count']}")
    print(f"Missing source artifact count: {result['missing_source_artifact_count']}")
    print(f"Blocking gap register count: {result['blocking_gap_register_count']}")
    print(f"Blocking gap row count: {result['blocking_gap_row_count']}")
    print(f"Primary submission blocker count: {result['primary_submission_blocker_count']}")
    print(f"Citation boundary gap count: {result['citation_boundary_gap_count']}")
    print(f"Unresolved gap count: {result['unresolved_gap_count']}")
    print(f"Gap resolution count: {result['gap_resolution_count']}")
    print(f"Manuscript submission ready count: {result['manuscript_submission_ready_count']}")
    print(f"Readiness approval count: {result['readiness_approval_count']}")
    print(f"Formal mathematical proof count: {result['formal_mathematical_proof_count']}")
    print(f"Independent experiment count: {result['independent_experiment_count']}")
    print(f"External validation count: {result['external_validation_count']}")
    print(f"New citation added count: {result['new_citation_added_count']}")
    print(f"Conditional hold count: {result['conditional_hold_count']}")
    print(f"Hard zero count: {result['hard_zero_count']}")
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

    print("Experiment 85 completed successfully.")


if __name__ == "__main__":
    main()
