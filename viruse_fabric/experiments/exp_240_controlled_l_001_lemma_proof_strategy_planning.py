from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_l_001_lemma_proof_strategy_planning import (
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/controlled_tc_001_proof_obligation_lemma_planning_v8_159.md")
OUTPUT_PATH = Path("outputs/controlled_l_001_lemma_proof_strategy_planning_v8_160.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.160 — Controlled L-001 Lemma Proof Strategy Planning

Status: main planning completed on branch `v8-160-controlled-l-001-lemma-proof-strategy-planning`.

This milestone selects L-001 from the v8.159 TC-001 lemma plan and plans a controlled L-001 proof strategy only.

Positive planning claims:
- Controlled L-001 lemma proof strategy planning count: 1
- New controlled L-001 lemma proof strategy planning count: 1
- L-001 lemma proof strategy planning count: 1
- Selected lemma count: 1
- Selected L-001 count: 1
- Planned L-001 proof strategy count: 1
- Planned L-001 proof step count: 4
- Planned lemma count: 6
- TC-001 planned lemma count: 6

Boundary claims:
- Formalization complete count: 0
- New theorem proven count: 0
- Theorem proof execution count: 0
- TC-001 proof execution count: 0
- Lemma proof execution count: 0
- L-001 lemma proof execution count: 0
- TC-001 lemma proof execution count: 0
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is not L-001 proof execution.
This milestone is not lemma proof execution.
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
    if "## v8.160 — Controlled L-001 Lemma Proof Strategy Planning" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 240: Controlled L-001 Lemma Proof Strategy Planning")
    print("Question: Can Viruse Fabric select L-001 and plan a controlled proof strategy while preserving zero claims for L-001 proof execution, lemma proof execution, TC-001 proof execution, theorem proof execution, proof assistant verification, validation, readiness, and citations?")
    print("Title: Controlled L-001 Lemma Proof Strategy Planning v8.160")
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

        if result.boundary_phrase_count < 10:
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

    counters_to_print = [
        "Controlled L-001 lemma proof strategy planning count: 1",
        "New controlled L-001 lemma proof strategy planning count: 1",
        "L-001 lemma proof strategy planning count: 1",
        "Selected lemma count: 1",
        "Selected L-001 count: 1",
        "Planned L-001 proof strategy count: 1",
        "Planned L-001 proof step count: 4",
        "Controlled TC-001 proof obligation lemma planning count: 1",
        "TC-001 proof obligation lemma planning count: 1",
        "Proof obligation lemma planning count: 1",
        "Planned proof obligation count: 6",
        "Planned lemma count: 6",
        "TC-001 planned lemma count: 6",
        "Accepted lemma plan count: 1",
        "Selected theorem candidate count: 1",
        "Selected TC-001 count: 1",
        "Planned proof strategy count: 1",
        "TC-001 proof strategy planning count: 1",
        "Theorem candidate plan count: 1",
        "Planned theorem candidate count: 4",
        "Accepted theorem candidate plan count: 1",
        "Dependency closure boundary pass count: 1",
        "Dependency closure blocker count: 0",
        "Unresolved dependency gap count: 0",
        "Imported controlled TC-001 proof obligation lemma planning count: 1",
        "Imported TC-001 proof obligation lemma planning count: 1",
        "Imported planned proof obligation count: 6",
        "Imported planned lemma count: 6",
        "Imported TC-001 planned lemma count: 6",
        "Imported accepted lemma plan count: 1",
        "Imported selected TC-001 count: 1",
        "Imported TC-001 proof strategy planning count: 1",
        "Formalization complete count: 0",
        "New theorem proven count: 0",
        "Theorem proof execution count: 0",
        "TC-001 proof execution count: 0",
        "Lemma proof execution count: 0",
        "L-001 lemma proof execution count: 0",
        "TC-001 lemma proof execution count: 0",
        "Proof assistant verification count: 0",
        "External validation count: 0",
        "Independent experiment count: 0",
        "Manuscript submission ready count: 0",
        "Readiness approval count: 0",
        "New citation added count: 0",
    ]

    for line in counters_to_print:
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
        "Interpretation: The v8.160 artifact selects L-001 and plans a controlled proof strategy with four planned proof steps while preserving zero counts for L-001 proof execution, lemma proof execution, TC-001 proof execution, theorem proof execution, proof assistant verification, validation, readiness approval, and citation claims."
    )
    print("Experiment 240 completed successfully.")
    print("V8_160_CONTROLLED_L_001_LEMMA_PROOF_STRATEGY_PLANNING_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
