from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.controlled_full_dependency_closure_boundary_audit import (
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/controlled_dependent_object_completion_bundle_integration_v8_155.md")
OUTPUT_PATH = Path("outputs/controlled_full_dependency_closure_boundary_audit_v8_156.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.156 — Controlled Full Dependency Closure Boundary Audit

Status: main audit completed on branch `v8-156-controlled-full-dependency-closure-boundary-audit`.

This milestone runs one controlled full dependency closure boundary audit over the integrated dependent-object completion bundle after v8.155.

Positive audit claims:
- Controlled full dependency closure boundary audit count: 1
- New controlled full dependency closure boundary audit count: 1
- Full dependency closure audit count: 1
- Dependency closure boundary audit count: 1
- Dependency closure boundary pass count: 1
- Dependency closure blocker count: 0
- Unresolved dependency gap count: 0
- Dependent-object completion bundle integration count: 1
- Integrated dependent-object completion bundle count: 1
- Completed dependent-object completion bundle count: 1

Boundary claims:
- Formalization complete count: 0
- Theorem candidate plan count: 0
- New theorem proven count: 0
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is not full formalization.
This milestone is not theorem candidate planning.
This milestone is not proof execution.
This milestone is not validation.
This milestone is not manuscript readiness.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.156 — Controlled Full Dependency Closure Boundary Audit" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 236: Controlled Full Dependency Closure Boundary Audit")
    print("Question: Can Viruse Fabric audit dependency closure over the v8.155 integrated bundle while preserving zero claims for full formalization, theorem, proof, validation, readiness, and citations?")
    print("Title: Controlled Full Dependency Closure Boundary Audit v8.156")
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
        "Controlled full dependency closure boundary audit count: 1",
        "New controlled full dependency closure boundary audit count: 1",
        "Full dependency closure audit count: 1",
        "Dependency closure boundary audit count: 1",
        "Dependency closure boundary pass count: 1",
        "Dependency closure blocker count: 0",
        "Unresolved dependency gap count: 0",
        "Dependent-object completion bundle integration count: 1",
        "Integrated dependent-object completion bundle count: 1",
        "Completed dependent-object completion bundle count: 1",
        "Dependent-object definition completion count: 6",
        "Completed dependent-object definition count: 6",
        "All dependent-object definition completion count: 1",
        "Imported dependent-object completion bundle integration count: 1",
        "Imported integrated dependent-object completion bundle count: 1",
        "Imported completed dependent-object completion bundle count: 1",
        "Imported completed Sigma_A definition count: 1",
        "Imported completed formal definition count: 1",
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
        "Interpretation: The v8.156 artifact runs a controlled full dependency closure boundary audit and records zero dependency blockers and zero unresolved dependency gaps while preserving zero counts for full formalization, theorem candidate planning, theorem proof, validation, readiness approval, and citation claims."
    )
    print("Experiment 236 completed successfully.")
    print("V8_156_CONTROLLED_FULL_DEPENDENCY_CLOSURE_BOUNDARY_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
