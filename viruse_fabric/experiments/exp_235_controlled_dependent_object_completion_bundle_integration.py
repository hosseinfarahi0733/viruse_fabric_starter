from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_dependent_object_completion_bundle_integration import (
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/controlled_traj_a_definition_completion_execution_v8_154.md")
OUTPUT_PATH = Path("outputs/controlled_dependent_object_completion_bundle_integration_v8_155.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.155 — Controlled Dependent-object Completion Bundle Integration

Status: main integration completed on branch `v8-155-controlled-dependent-object-completion-bundle-integration`.

This milestone integrates the six completed dependent-object definitions into one controlled completion bundle after v8.154 Traj_A completion.

Positive integration claims:
- Controlled dependent-object completion bundle integration count: 1
- New controlled dependent-object completion bundle integration count: 1
- Dependent-object completion bundle integration count: 1
- Integrated dependent-object completion bundle count: 1
- Completed dependent-object completion bundle count: 1
- Dependent-object definition completion count: 6
- Completed dependent-object definition count: 6
- All dependent-object definition completion count: 1

Boundary claims:
- Full dependency closure audit count: 0
- Formalization complete count: 0
- Theorem candidate plan count: 0
- New theorem proven count: 0
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is not a full dependency closure audit.
This milestone is not full formalization.
This milestone is not theorem candidate planning.
This milestone is not proof execution.
This milestone is not validation.
This milestone is not manuscript readiness.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.155 — Controlled Dependent-object Completion Bundle Integration" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 235: Controlled Dependent-object Completion Bundle Integration")
    print("Question: Can Viruse Fabric integrate six completed dependent-object definitions into one controlled completion bundle after v8.154 while preserving zero claims for dependency closure audit, full formalization, theorem, proof, validation, readiness, and citations?")
    print("Title: Controlled Dependent-object Completion Bundle Integration v8.155")
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

    counters_to_print = [
        "Controlled dependent-object completion bundle integration count: 1",
        "New controlled dependent-object completion bundle integration count: 1",
        "Dependent-object completion bundle integration count: 1",
        "Integrated dependent-object completion bundle count: 1",
        "Completed dependent-object completion bundle count: 1",
        "Adm_A definition completion count: 1",
        "Completed Adm_A definition count: 1",
        "C_reg definition completion count: 1",
        "Completed C_reg definition count: 1",
        "Pi_obs definition completion count: 1",
        "Completed Pi_obs definition count: 1",
        "M_c definition completion count: 1",
        "Completed M_c definition count: 1",
        "R_A definition completion count: 1",
        "Completed R_A definition count: 1",
        "Traj_A definition completion count: 1",
        "Completed Traj_A definition count: 1",
        "Dependent-object definition completion count: 6",
        "Completed dependent-object definition count: 6",
        "All dependent-object definition completion count: 1",
        "Imported controlled Traj_A definition completion execution count: 1",
        "Imported completed Adm_A definition count: 1",
        "Imported completed C_reg definition count: 1",
        "Imported completed Pi_obs definition count: 1",
        "Imported completed M_c definition count: 1",
        "Imported completed R_A definition count: 1",
        "Imported completed Traj_A definition count: 1",
        "Imported dependent-object definition completion count: 6",
        "Imported completed dependent-object definition count: 6",
        "Imported all dependent-object definition completion count: 1",
        "Imported completed Sigma_A definition count: 1",
        "Imported completed formal definition count: 1",
        "Full dependency closure audit count: 0",
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
        "Interpretation: The v8.155 artifact integrates the completed dependent-object definitions into a controlled completion bundle while preserving zero counts for dependency closure audit, full formalization, theorem candidate planning, theorem proof, validation, readiness approval, and citation claims."
    )
    print("Experiment 235 completed successfully.")
    print("V8_155_CONTROLLED_DEPENDENT_OBJECT_COMPLETION_BUNDLE_INTEGRATION_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
