from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_tc_001_proof_execution_strategy_planning import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/controlled_tc_001_supporting_lemma_chain_completion_audit_v8_172.md")
OUTPUT_PATH = Path("outputs/controlled_tc_001_proof_execution_strategy_planning_v8_173.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.173 - Controlled TC-001 Proof Execution Strategy Planning

Status: main planning completed on branch `v8-173-controlled-tc-001-proof-execution-strategy-planning`.

This milestone selects TC-001 and plans a controlled TC-001 proof execution strategy only.

Positive planning claims:
- Controlled TC-001 proof execution strategy planning count: 1
- New controlled TC-001 proof execution strategy planning count: 1
- TC-001 proof execution strategy planning count: 1
- Selected theorem candidate count: 1
- Selected TC-001 count: 1
- Planned TC-001 proof execution strategy count: 1
- Planned TC-001 proof execution step count: 8

Imported existing audit and proof claims:
- Controlled TC-001 supporting lemma chain completion audit count: 1
- TC-001 supporting lemma chain completion audit count: 1
- Supporting lemma chain audit pass count: 1
- Supporting lemma chain audit blocker count: 0
- Unresolved supporting lemma chain gap count: 0
- Completed TC-001 supporting lemma chain count: 1
- Accepted TC-001 supporting lemma chain completion count: 1
- Lemma proof execution count: 6
- TC-001 lemma proof execution count: 6
- Proved TC-001 supporting lemma count: 6
- Internal lemma proof count: 6

Boundary claims:
- New lemma proof execution count: 0
- New TC-001 proof execution count: 0
- TC-001 proof execution count: 0
- TC-001 theorem proven count: 0
- New theorem proven count: 0
- Theorem proof execution count: 0
- Formalization complete count: 0
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is not new lemma proof execution.
This milestone is not TC-001 proof execution.
This milestone is not theorem proof execution.
This milestone is not proof assistant verification.
This milestone is not external validation.
This milestone is not independent experimentation.
This milestone is not manuscript readiness.
This milestone is not citation work.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.173 - Controlled TC-001 Proof Execution Strategy Planning" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 253: Controlled TC-001 Proof Execution Strategy Planning")
    print("Question: Can Viruse Fabric plan controlled TC-001 proof execution using the completed supporting lemma chain while preserving zero claims for TC-001 proof execution, theorem proof, proof assistant verification, validation, readiness, and citations?")
    print("Title: Controlled TC-001 Proof Execution Strategy Planning v8.173")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")

    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_PATH.exists():
        errors.append(f"Missing source artifact: {SOURCE_PATH}")
    else:
        result = write_report(SOURCE_PATH, OUTPUT_PATH)

        for phrase in result.missing_source_phrases:
            errors.append(f"Missing required source phrase: {phrase}")

        for phrase in result.missing_report_phrases:
            errors.append(f"Missing required report phrase: {phrase}")

        if result.prohibited_behavior_count != 0:
            errors.append(
                f"Prohibited behavior count must be 0, got {result.prohibited_behavior_count}"
            )

        if result.boundary_phrase_count < 8:
            warnings.append(
                f"Boundary phrase count is low: {result.boundary_phrase_count}"
            )

        warnings.extend(result.warning_messages)

    if OUTPUT_PATH.exists():
        report_text = OUTPUT_PATH.read_text(encoding="utf-8", errors="replace")
        report_size = OUTPUT_PATH.stat().st_size
    else:
        report_text = ""
        report_size = 0

    missing_required_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report_text
    ]

    if missing_required_report_phrases:
        for phrase in missing_required_report_phrases:
            errors.append(f"Missing required report phrase after write: {phrase}")

    append_note()

    for line in COUNTER_LINES:
        print(line)

    print(f"Report exists: {OUTPUT_PATH.exists()}")
    print(f"Report size: {report_size}")
    print(f"Missing required report phrases: {len(missing_required_report_phrases)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        print("Passed: False")
        return 1

    print("Passed: True")
    print(
        "Interpretation: The v8.173 artifact selects TC-001 and plans a controlled TC-001 proof execution strategy while preserving zero counts for TC-001 proof execution, theorem proof execution, proof assistant verification, validation, readiness approval, and citation claims."
    )
    print("Experiment 253 completed successfully.")
    print("V8_173_CONTROLLED_TC_001_PROOF_EXECUTION_STRATEGY_PLANNING_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
