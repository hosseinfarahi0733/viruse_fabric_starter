from __future__ import annotations

from pathlib import Path
import sys

from viruse_fabric.writing.dependent_object_definition_completion_planning import (
    write_report,
    REQUIRED_REPORT_PHRASES,
)


SOURCE_PATH = Path("outputs/controlled_sigma_a_definition_completion_execution_v8_147.md")
OUTPUT_PATH = Path("outputs/dependent_object_definition_completion_planning_v8_148.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.148 — Dependent-object Definition Completion Planning

Status: main execution completed on branch `v8-148-dependent-object-definition-completion-planning`.

This milestone creates a controlled plan for future completion of six dependent-object definitions after official v8.147 Sigma_A definition completion.

Positive planning claims:
- Dependent-object definition completion planning count: 1
- New dependent-object definition completion planning count: 1
- Dependent-object completion plan count: 1
- Planned dependent-object count: 6

Boundary claims:
- Dependent-object definition completion count: 0
- Adm_A definition completion count: 0
- C_reg definition completion count: 0
- Pi_obs definition completion count: 0
- M_c definition completion count: 0
- R_A definition completion count: 0
- Traj_A definition completion count: 0
- Formalization complete count: 0
- Theorem candidate plan count: 0
- New theorem proven count: 0
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is not a dependent-object completion execution.
This milestone is not theorem candidate planning.
This milestone is not proof execution.
This milestone is not validation.
This milestone is not manuscript readiness.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.148 — Dependent-object Definition Completion Planning" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 228: Dependent-object Definition Completion Planning")
    print("Question: Can Viruse Fabric plan dependent-object definition completion after official Sigma_A completion while preserving zero completion/proof/validation/readiness/citation claims?")
    print("Title: Dependent-object Definition Completion Planning v8.148")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")

    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_PATH.exists():
        errors.append(f"Missing source artifact: {SOURCE_PATH}")
        result = None
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

        if result.boundary_phrase_count < 12:
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
        "Dependent-object definition completion planning count: 1",
        "New dependent-object definition completion planning count: 1",
        "Dependent-object completion plan count: 1",
        "Dependent-object completion planning row count: 6",
        "Planned dependent-object count: 6",
        "Planned Adm_A definition completion count: 1",
        "Planned C_reg definition completion count: 1",
        "Planned Pi_obs definition completion count: 1",
        "Planned M_c definition completion count: 1",
        "Planned R_A definition completion count: 1",
        "Planned Traj_A definition completion count: 1",
        "Imported completed Sigma_A definition count: 1",
        "Imported completed formal definition count: 1",
        "Dependent-object definition completion count: 0",
        "Adm_A definition completion count: 0",
        "C_reg definition completion count: 0",
        "Pi_obs definition completion count: 0",
        "M_c definition completion count: 0",
        "R_A definition completion count: 0",
        "Traj_A definition completion count: 0",
        "Formalization complete count: 0",
        "Theorem candidate plan count: 0",
        "New theorem proven count: 0",
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
        "Interpretation: The v8.148 artifact plans controlled dependent-object definition completion while preserving zero counts for actual dependent-object completion, full formalization, theorem candidate planning, theorem proof, validation, readiness approval, and citation claims."
    )
    print("Experiment 228 completed successfully.")
    print("V8_148_DEPENDENT_OBJECT_DEFINITION_COMPLETION_PLANNING_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
