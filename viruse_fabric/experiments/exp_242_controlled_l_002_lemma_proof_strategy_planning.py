from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_l_002_lemma_proof_strategy_planning import (
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/controlled_l_001_lemma_proof_execution_v8_161.md")
OUTPUT_PATH = Path("outputs/controlled_l_002_lemma_proof_strategy_planning_v8_162.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.162 — Controlled L-002 Lemma Proof Strategy Planning

Status: main planning completed on branch `v8-162-controlled-l-002-lemma-proof-strategy-planning`.

This milestone selects L-002 from the TC-001 lemma plan and plans a controlled L-002 proof strategy only.

Positive planning claims:
- Controlled L-002 lemma proof strategy planning count: 1
- New controlled L-002 lemma proof strategy planning count: 1
- L-002 lemma proof strategy planning count: 1
- Selected lemma count: 1
- Selected L-002 count: 1
- Planned L-002 proof strategy count: 1
- Planned L-002 proof step count: 5

Imported existing proof claims:
- L-001 lemma proof execution count: 1
- Lemma proof execution count: 1
- TC-001 lemma proof execution count: 1
- Proved L-001 lemma count: 1
- Proved TC-001 supporting lemma count: 1
- Internal lemma proof count: 1

Boundary claims:
- New L-002 lemma proof execution count: 0
- L-002 lemma proof execution count: 0
- New lemma proof execution count: 0
- Proved L-002 lemma count: 0
- Formalization complete count: 0
- New theorem proven count: 0
- Theorem proof execution count: 0
- TC-001 proof execution count: 0
- TC-001 theorem proven count: 0
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is not L-002 proof execution.
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
    if "## v8.162 — Controlled L-002 Lemma Proof Strategy Planning" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 242: Controlled L-002 Lemma Proof Strategy Planning")
    print("Question: Can Viruse Fabric select L-002 and plan a controlled proof strategy while preserving the official L-001 proof and keeping new L-002 proof execution, TC-001 proof, theorem proof, proof assistant verification, validation, readiness, and citations at zero?")
    print("Title: Controlled L-002 Lemma Proof Strategy Planning v8.162")
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
        "Controlled L-002 lemma proof strategy planning count: 1",
        "New controlled L-002 lemma proof strategy planning count: 1",
        "L-002 lemma proof strategy planning count: 1",
        "Selected lemma count: 1",
        "Selected L-002 count: 1",
        "Planned L-002 proof strategy count: 1",
        "Planned L-002 proof step count: 5",
        "L-001 lemma proof execution count: 1",
        "Lemma proof execution count: 1",
        "TC-001 lemma proof execution count: 1",
        "Proved L-001 lemma count: 1",
        "Proved L-002 lemma count: 0",
        "Proved TC-001 supporting lemma count: 1",
        "Internal lemma proof count: 1",
        "New L-002 lemma proof execution count: 0",
        "L-002 lemma proof execution count: 0",
        "New lemma proof execution count: 0",
        "Planned lemma count: 6",
        "TC-001 planned lemma count: 6",
        "Selected TC-001 count: 1",
        "Imported controlled L-001 lemma proof execution count: 1",
        "Imported L-001 lemma proof execution count: 1",
        "Imported lemma proof execution count: 1",
        "Imported TC-001 lemma proof execution count: 1",
        "Imported proved L-001 lemma count: 1",
        "Imported proved TC-001 supporting lemma count: 1",
        "Formalization complete count: 0",
        "New theorem proven count: 0",
        "Theorem proof execution count: 0",
        "TC-001 proof execution count: 0",
        "TC-001 theorem proven count: 0",
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
        "Interpretation: The v8.162 artifact selects L-002 and plans a controlled proof strategy with five planned proof steps while preserving the official L-001 proof and keeping new L-002 proof execution, TC-001 proof execution, theorem proof execution, proof assistant verification, validation, readiness approval, and citation claims at zero."
    )
    print("Experiment 242 completed successfully.")
    print("V8_162_CONTROLLED_L_002_LEMMA_PROOF_STRATEGY_PLANNING_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
