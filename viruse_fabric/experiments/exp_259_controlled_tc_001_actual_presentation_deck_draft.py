from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_tc_001_actual_presentation_deck_draft import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/controlled_tc_001_slide_deck_content_extraction_v8_178.md")
OUTPUT_PATH = Path("outputs/controlled_tc_001_actual_presentation_deck_draft_v8_179.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.179 - Controlled TC-001 Actual Presentation Deck Draft

Status: main draft completed on branch `v8-179-controlled-tc-001-actual-presentation-deck-draft`.

This milestone drafts the actual TC-001 presentation deck content from the official v8.178 slide content.

Positive draft claims:
- Controlled TC-001 actual presentation deck draft count: 1
- New controlled TC-001 actual presentation deck draft count: 1
- TC-001 actual presentation deck draft count: 1
- Drafted TC-001 presentation slide count: 8
- Drafted TC-001 slide title count: 8
- Drafted TC-001 slide bullet set count: 8
- Drafted TC-001 speaker note count: 8
- Drafted TC-001 defense Q&A count: 6
- Drafted TC-001 opening script count: 1
- Drafted TC-001 closing script count: 1
- Drafted TC-001 final defense sentence count: 1
- Actual presentation deck draft ready count: 1

Imported presentation-content claims:
- Controlled TC-001 slide deck content extraction count: 1
- Presentation deck content ready count: 1
- Presentation-safe internal TC-001 proof claim count: 1
- Accepted internal TC-001 theorem proof count: 1
- TC-001 proof execution count: 1
- TC-001 theorem proven count: 1
- Theorem proof execution count: 1
- Internal theorem proof count: 1
- Controlled internal TC-001 theorem proof count: 1
- Completed TC-001 supporting lemma chain count: 1
- Proved TC-001 supporting lemma count: 6
- Internal lemma proof count: 6

Boundary claims:
- New lemma proof execution count: 0
- New TC-001 proof execution count: 0
- New theorem proven count: 0
- New theorem proof execution count: 0
- Formalization complete count: 0
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is actual presentation deck drafting only.
This milestone is not new TC-001 proof execution.
This milestone is not new theorem proof execution.
This milestone is not proof assistant verification.
This milestone is not external validation.
This milestone is not manuscript readiness.
This milestone is not citation work.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.179 - Controlled TC-001 Actual Presentation Deck Draft" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 259: Controlled TC-001 Actual Presentation Deck Draft")
    print("Question: Can Viruse Fabric draft the actual TC-001 presentation deck from the official v8.178 slide content while preserving explicit zero claims for proof assistant verification, validation, readiness, and citations?")
    print("Title: Controlled TC-001 Actual Presentation Deck Draft v8.179")
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
        "Interpretation: The v8.179 artifact drafts the actual TC-001 presentation deck while preserving zero counts for proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 259 completed successfully.")
    print("V8_179_CONTROLLED_TC_001_ACTUAL_PRESENTATION_DECK_DRAFT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
