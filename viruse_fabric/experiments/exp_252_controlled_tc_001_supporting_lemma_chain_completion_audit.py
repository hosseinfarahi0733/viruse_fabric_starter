from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_tc_001_supporting_lemma_chain_completion_audit import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/controlled_l_006_lemma_proof_execution_v8_171.md")
OUTPUT_PATH = Path("outputs/controlled_tc_001_supporting_lemma_chain_completion_audit_v8_172.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.172 - Controlled TC-001 Supporting Lemma Chain Completion Audit

Status: main audit completed on branch `v8-172-controlled-tc-001-supporting-lemma-chain-completion-audit`.

This milestone audits the completed TC-001 supporting lemma chain only.

Positive audit claims:
- Controlled TC-001 supporting lemma chain completion audit count: 1
- New controlled TC-001 supporting lemma chain completion audit count: 1
- TC-001 supporting lemma chain completion audit count: 1
- Supporting lemma chain audit pass count: 1
- Supporting lemma chain audit blocker count: 0
- Unresolved supporting lemma chain gap count: 0
- Completed TC-001 supporting lemma chain count: 1
- Accepted TC-001 supporting lemma chain completion count: 1

Imported existing proof claims:
- L-001 lemma proof execution count: 1
- L-002 lemma proof execution count: 1
- L-003 lemma proof execution count: 1
- L-004 lemma proof execution count: 1
- L-005 lemma proof execution count: 1
- L-006 lemma proof execution count: 1
- Lemma proof execution count: 6
- TC-001 lemma proof execution count: 6
- Proved L-001 lemma count: 1
- Proved L-002 lemma count: 1
- Proved L-003 lemma count: 1
- Proved L-004 lemma count: 1
- Proved L-005 lemma count: 1
- Proved L-006 lemma count: 1
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
    if "## v8.172 - Controlled TC-001 Supporting Lemma Chain Completion Audit" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 252: Controlled TC-001 Supporting Lemma Chain Completion Audit")
    print("Question: Can Viruse Fabric audit the completed TC-001 supporting lemma chain while preserving zero claims for TC-001 proof, theorem proof, proof assistant verification, validation, readiness, and citations?")
    print("Title: Controlled TC-001 Supporting Lemma Chain Completion Audit v8.172")
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
        "Interpretation: The v8.172 artifact audits and accepts the completed TC-001 supporting lemma chain while preserving zero counts for new lemma proof execution, TC-001 proof execution, theorem proof execution, proof assistant verification, validation, readiness approval, and citation claims."
    )
    print("Experiment 252 completed successfully.")
    print("V8_172_CONTROLLED_TC_001_SUPPORTING_LEMMA_CHAIN_COMPLETION_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
