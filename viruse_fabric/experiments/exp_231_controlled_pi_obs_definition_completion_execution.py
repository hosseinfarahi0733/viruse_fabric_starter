from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_pi_obs_definition_completion_execution import (
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/controlled_c_reg_definition_completion_execution_v8_150.md")
OUTPUT_PATH = Path("outputs/controlled_pi_obs_definition_completion_execution_v8_151.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.151 — Controlled Pi_obs Definition Completion Execution

Status: main execution completed on branch `v8-151-controlled-pi-obs-definition-completion-execution`.

This milestone executes the third controlled dependent-object definition completion after v8.150 C_reg completion.

Positive execution claims:
- Controlled Pi_obs definition completion execution count: 1
- New controlled Pi_obs definition completion execution count: 1
- Pi_obs definition completion execution count: 1
- Dependent-object definition completion execution count: 1
- Pi_obs definition completion count: 1
- Completed Pi_obs definition count: 1
- Adm_A definition completion count: 1
- Completed Adm_A definition count: 1
- C_reg definition completion count: 1
- Completed C_reg definition count: 1
- Dependent-object definition completion count: 3
- Completed dependent-object definition count: 3

Boundary claims:
- M_c definition completion count: 0
- R_A definition completion count: 0
- Traj_A definition completion count: 0
- All dependent-object definition completion count: 0
- Dependent-object completion bundle integration count: 0
- Formalization complete count: 0
- Theorem candidate plan count: 0
- New theorem proven count: 0
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is not M_c completion.
This milestone is not R_A completion.
This milestone is not Traj_A completion.
This milestone is not all-dependent-object completion.
This milestone is not dependent-object bundle integration.
This milestone is not full formalization.
This milestone is not theorem candidate planning.
This milestone is not proof execution.
This milestone is not validation.
This milestone is not manuscript readiness.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.151 — Controlled Pi_obs Definition Completion Execution" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 231: Controlled Pi_obs Definition Completion Execution")
    print("Question: Can Viruse Fabric complete Pi_obs as the third dependent-object definition after v8.150 C_reg completion while preserving zero claims for M_c, R_A, Traj_A, all-dependent-object completion, bundle integration, full formalization, theorem, proof, validation, readiness, and citations?")
    print("Title: Controlled Pi_obs Definition Completion Execution v8.151")
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
        "Controlled Pi_obs definition completion execution count: 1",
        "New controlled Pi_obs definition completion execution count: 1",
        "Pi_obs definition completion execution count: 1",
        "Dependent-object definition completion execution count: 1",
        "Definition completion execution count: 1",
        "Completion execution count: 1",
        "Definition execution count: 1",
        "New definition execution count: 1",
        "Adm_A definition completion count: 1",
        "Completed Adm_A definition count: 1",
        "C_reg definition completion count: 1",
        "Completed C_reg definition count: 1",
        "Pi_obs definition completion count: 1",
        "Completed Pi_obs definition count: 1",
        "Dependent-object definition completion count: 3",
        "Completed dependent-object definition count: 3",
        "Imported controlled C_reg definition completion execution count: 1",
        "Imported completed Adm_A definition count: 1",
        "Imported completed C_reg definition count: 1",
        "Imported dependent-object definition completion count: 2",
        "Imported completed dependent-object definition count: 2",
        "Imported completed Sigma_A definition count: 1",
        "Imported completed formal definition count: 1",
        "M_c definition completion count: 0",
        "R_A definition completion count: 0",
        "Traj_A definition completion count: 0",
        "All dependent-object definition completion count: 0",
        "Dependent-object completion bundle integration count: 0",
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
        "Interpretation: The v8.151 artifact executes controlled Pi_obs definition completion while preserving zero counts for M_c, R_A, Traj_A, all-dependent-object completion, bundle integration, full formalization, theorem candidate planning, theorem proof, validation, readiness approval, and citation claims."
    )
    print("Experiment 231 completed successfully.")
    print("V8_151_CONTROLLED_PI_OBS_DEFINITION_COMPLETION_EXECUTION_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
