"""Experiment 92: formal definition pre-execution checklist audit."""

from __future__ import annotations

import re
from pathlib import Path

from viruse_fabric.writing.formal_definition_pre_execution_checklist_audit import (
    AUDIT_ROWS,
    BOUNDARY_PHRASES,
    HARD_ZERO_FIELDS,
    NEXT_STEPS,
    OUTPUT_PATH,
    PROHIBITED_BEHAVIORS,
    REQUIRED_SOURCE_PATHS,
    SOURCE_ARTIFACT_COUNT,
    write_report,
)


TITLE = "Experiment 92: Formal Definition Pre-Execution Checklist Audit"
QUESTION = (
    "Can Viruse Fabric audit formal definition pre-execution checklist rows while "
    "keeping checklist completion, completed formal definitions, definition execution "
    "approval, definition execution, proof execution, formal proof, theorem proof, "
    "lemma proof, formalization completion, submission readiness, independent "
    "experiment, external validation, and new citation additions at zero?"
)

REQUIRED_REPORT_PHRASES = [
    "Formal Definition Pre-Execution Checklist Audit v8.12",
    "formal_definition_pre_execution_checklist_audit_count: 1",
    "definition_pre_execution_checklist_audit_row_count: 4",
    "definition_pre_execution_checklist_source_row_count: 4",
    "definition_pre_execution_checklist_completed_count: 0",
    "formal_definition_completed_count: 0",
    "formal_definition_execution_count: 0",
    "definition_execution_approved_count: 0",
    "formal_mathematical_proof_count: 0",
    "proof_execution_count: 0",
    "theorem_proven_count: 0",
    "lemma_proven_count: 0",
    "formalization_complete_count: 0",
    "proof_gap_resolution_count: 0",
    "manuscript_submission_ready_count: 0",
    "readiness_approval_count: 0",
    "independent_experiment_count: 0",
    "external_validation_count: 0",
    "new_citation_added_count: 0",
    "CAND_0003_conditional_hold_count: 1",
    "FDECA-ROW-0001",
    "FDECA-ROW-0002",
    "FDECA-ROW-0003",
    "FDECA-ROW-0004",
    "constraint_geometry",
    "attractor_concentration",
    "path_compatibility",
    "observer_projection",
    "audited_not_completed",
    "CAND-0003 remains conditional hold",
    "research prototype with internal validation",
]

OVERCLAIM_PATTERNS = [
    r"\bpre_execution_checklist_completed:\s*yes\b",
    r"\bdefinition_pre_execution_checklist_completed_count:\s*[1-9][0-9]*\b",
    r"\bformal_definition_completed:\s*yes\b",
    r"\bformal_definition_completed_count:\s*[1-9][0-9]*\b",
    r"\bformal_definition_executed:\s*yes\b",
    r"\bformal_definition_execution_count:\s*[1-9][0-9]*\b",
    r"\bdefinition_execution_approved:\s*yes\b",
    r"\bdefinition_execution_approved_count:\s*[1-9][0-9]*\b",
    r"\bformal_mathematical_proof:\s*yes\b",
    r"\bformal_mathematical_proof_count:\s*[1-9][0-9]*\b",
    r"\bproof_executed:\s*yes\b",
    r"\bproof_execution_count:\s*[1-9][0-9]*\b",
    r"\btheorem_proven:\s*yes\b",
    r"\btheorem_proven_count:\s*[1-9][0-9]*\b",
    r"\blemma_proven:\s*yes\b",
    r"\blemma_proven_count:\s*[1-9][0-9]*\b",
    r"\bformalization_complete:\s*yes\b",
    r"\bformalization_complete_count:\s*[1-9][0-9]*\b",
    r"\bproof_gap_resolved:\s*yes\b",
    r"\bproof_gap_resolution_count:\s*[1-9][0-9]*\b",
    r"\bmanuscript_submission_ready:\s*yes\b",
    r"\bmanuscript_submission_ready_count:\s*[1-9][0-9]*\b",
    r"\breadiness_approval:\s*yes\b",
    r"\breadiness_approval_count:\s*[1-9][0-9]*\b",
    r"\bindependent_experiment_count:\s*[1-9][0-9]*\b",
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


def _count_audit_rows(text: str) -> int:
    row_ids = re.findall(
        r"^\s*###\s+(FDECA-ROW-\d{4})\s*$",
        text,
        flags=re.MULTILINE,
    )
    return len(set(row_ids))


def _count_official_bullets(text: str, label: str) -> int:
    return len(re.findall(rf"^\s*-\s+{re.escape(label)}:", text, flags=re.MULTILINE))


def _count_pattern_list(text: str, patterns: list[str]) -> int:
    return sum(len(re.findall(pattern, text)) for pattern in patterns)


def run() -> dict[str, object]:
    report = write_report()

    missing_sources = [str(path) for path in REQUIRED_SOURCE_PATHS if not Path(path).exists()]
    missing_required_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    formal_definition_pre_execution_checklist_audit_count = report.count(
        "formal_definition_pre_execution_checklist_audit_count: 1"
    )
    definition_pre_execution_checklist_audit_row_count = _count_audit_rows(report)
    definition_pre_execution_checklist_source_row_count = len(
        {row["source_checklist"] for row in AUDIT_ROWS}
    )

    definition_pre_execution_checklist_completed_count = report.count(
        "pre_execution_checklist_completed: yes"
    )
    formal_definition_completed_count = report.count("formal_definition_completed: yes")
    formal_definition_execution_count = report.count("formal_definition_executed: yes")
    definition_execution_approved_count = report.count("definition_execution_approved: yes")
    formal_mathematical_proof_count = report.count("formal_mathematical_proof: yes")
    proof_execution_count = report.count("proof_executed: yes")
    theorem_proven_count = report.count("theorem_proven: yes")
    lemma_proven_count = report.count("lemma_proven: yes")
    formalization_complete_count = report.count("formalization_complete: yes")
    proof_gap_resolution_count = report.count("proof_gap_resolved: yes")
    manuscript_submission_ready_count = report.count("manuscript_submission_ready: yes")
    readiness_approval_count = report.count("readiness_approval: yes")
    new_citation_added_count = report.count("new_citation_added: yes")
    conditional_hold_count = 1 if "CAND_0003_conditional_hold_count: 1" in report else 0

    hard_zero_count = _count_official_bullets(report, "hard_zero")
    boundary_phrase_count = _count_official_bullets(report, "boundary_phrase")
    prohibited_behavior_count = _count_official_bullets(report, "prohibited_behavior")
    next_step_count = _count_official_bullets(report, "next_step")

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

    if SOURCE_ARTIFACT_COUNT != 42:
        errors.append(f"Expected source artifact count 42, got {SOURCE_ARTIFACT_COUNT}")

    if formal_definition_pre_execution_checklist_audit_count != 1:
        errors.append(
            "Expected formal definition pre-execution checklist audit count 1, got "
            f"{formal_definition_pre_execution_checklist_audit_count}"
        )

    if definition_pre_execution_checklist_audit_row_count != len(AUDIT_ROWS):
        errors.append(
            f"Expected {len(AUDIT_ROWS)} formal definition pre-execution checklist audit rows, got "
            f"{definition_pre_execution_checklist_audit_row_count}"
        )

    if definition_pre_execution_checklist_source_row_count != 4:
        errors.append(
            "Expected definition pre-execution checklist source row count 4, got "
            f"{definition_pre_execution_checklist_source_row_count}"
        )

    zero_checks = {
        "definition_pre_execution_checklist_completed_count": definition_pre_execution_checklist_completed_count,
        "formal_definition_completed_count": formal_definition_completed_count,
        "formal_definition_execution_count": formal_definition_execution_count,
        "definition_execution_approved_count": definition_execution_approved_count,
        "formal_mathematical_proof_count": formal_mathematical_proof_count,
        "proof_execution_count": proof_execution_count,
        "theorem_proven_count": theorem_proven_count,
        "lemma_proven_count": lemma_proven_count,
        "formalization_complete_count": formalization_complete_count,
        "proof_gap_resolution_count": proof_gap_resolution_count,
        "manuscript_submission_ready_count": manuscript_submission_ready_count,
        "readiness_approval_count": readiness_approval_count,
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
        "Formal definition pre-execution checklist rows are audited, but no checklist is completed.",
        "No execution approval, formal definition execution, proof execution, theorem proof, or lemma proof is created.",
        "Formalization remains incomplete and manuscript submission readiness remains unavailable.",
    ]

    report_exists = OUTPUT_PATH.exists()
    report_size = OUTPUT_PATH.stat().st_size if report_exists else 0

    return {
        "title": TITLE,
        "question": QUESTION,
        "output_path": str(OUTPUT_PATH),
        "source_artifact_count": SOURCE_ARTIFACT_COUNT,
        "missing_source_artifact_count": len(missing_sources),
        "formal_definition_pre_execution_checklist_audit_count": formal_definition_pre_execution_checklist_audit_count,
        "definition_pre_execution_checklist_audit_row_count": definition_pre_execution_checklist_audit_row_count,
        "definition_pre_execution_checklist_source_row_count": definition_pre_execution_checklist_source_row_count,
        "definition_pre_execution_checklist_completed_count": definition_pre_execution_checklist_completed_count,
        "formal_definition_completed_count": formal_definition_completed_count,
        "formal_definition_execution_count": formal_definition_execution_count,
        "definition_execution_approved_count": definition_execution_approved_count,
        "formal_mathematical_proof_count": formal_mathematical_proof_count,
        "proof_execution_count": proof_execution_count,
        "theorem_proven_count": theorem_proven_count,
        "lemma_proven_count": lemma_proven_count,
        "formalization_complete_count": formalization_complete_count,
        "proof_gap_resolution_count": proof_gap_resolution_count,
        "manuscript_submission_ready_count": manuscript_submission_ready_count,
        "readiness_approval_count": readiness_approval_count,
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
            "The v8.12 artifact audits four formal definition pre-execution checklist "
            "rows while keeping checklist completion, completed formal definitions, "
            "definition execution approval, definition execution, proof execution, "
            "formal mathematical proof, theorem proof, lemma proof, formalization "
            "completion, submission readiness, readiness approval, and new citation "
            "additions at zero."
        ),
    }


def main() -> None:
    result = run()

    print(TITLE)
    print(f"Question: {QUESTION}")
    print("Title: Formal Definition Pre-Execution Checklist Audit v8.12")
    print(f"Output path: {result['output_path']}")
    print(f"Source artifact count: {result['source_artifact_count']}")
    print(f"Missing source artifact count: {result['missing_source_artifact_count']}")
    print(
        "Formal definition pre-execution checklist audit count: "
        f"{result['formal_definition_pre_execution_checklist_audit_count']}"
    )
    print(
        "Definition pre-execution checklist audit row count: "
        f"{result['definition_pre_execution_checklist_audit_row_count']}"
    )
    print(
        "Definition pre-execution checklist source row count: "
        f"{result['definition_pre_execution_checklist_source_row_count']}"
    )
    print(
        "Definition pre-execution checklist completed count: "
        f"{result['definition_pre_execution_checklist_completed_count']}"
    )
    print(f"Formal definition completed count: {result['formal_definition_completed_count']}")
    print(f"Formal definition execution count: {result['formal_definition_execution_count']}")
    print(f"Definition execution approved count: {result['definition_execution_approved_count']}")
    print(f"Formal mathematical proof count: {result['formal_mathematical_proof_count']}")
    print(f"Proof execution count: {result['proof_execution_count']}")
    print(f"Theorem proven count: {result['theorem_proven_count']}")
    print(f"Lemma proven count: {result['lemma_proven_count']}")
    print(f"Formalization complete count: {result['formalization_complete_count']}")
    print(f"Proof gap resolution count: {result['proof_gap_resolution_count']}")
    print(f"Manuscript submission ready count: {result['manuscript_submission_ready_count']}")
    print(f"Readiness approval count: {result['readiness_approval_count']}")
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

    print("Experiment 92 completed successfully.")


if __name__ == "__main__":
    main()
