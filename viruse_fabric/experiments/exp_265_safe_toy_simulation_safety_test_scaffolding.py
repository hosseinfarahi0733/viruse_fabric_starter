from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.safe_toy_simulation_safety_test_scaffolding import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_toy_simulation_architecture_specification_v8_184.md")
OUTPUT_PATH = Path("outputs/safe_toy_simulation_safety_test_scaffolding_v8_185.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.185 - Safe Toy Simulation Safety Test Scaffolding

Status: main safety-test scaffolding completed on branch `v8-185-safe-toy-simulation-safety-test-scaffolding`.

This milestone defines safety-test scaffolding before simulator implementation.

Positive scaffolding claims:
- Safe toy simulation safety test scaffolding count: 1
- New safe toy simulation safety test scaffolding count: 1
- Safety guard scaffold count: 1
- Prohibited category checklist count: 1
- Safe toy fixture checklist count: 1
- Abstract-only enforcement checklist count: 1
- Non-operational boundary guard count: 1
- Pre-implementation safety gate count: 1
- Toy simulator safety test plan count: 1
- Synthetic fixture safety test count: 1
- Unitless variable safety test count: 1
- Abstract graph safety test count: 1
- Observation projection safety test count: 1
- Blocked operational category count: 8

Imported architecture claims:
- Safe toy simulation architecture specification count: 1
- Toy simulator entity specification count: 1
- Synthetic compartment graph specification count: 1
- Unitless state variable specification count: 1
- Abstract update rule specification count: 1
- Observation projection specification count: 1
- Safety test specification count: 1
- Non-operational model boundary count: 1

Safety boundary claims:
- Real pathogen simulation count: 0
- Real receptor parameter count: 0
- Operational host targeting count: 0
- Wet-lab protocol count: 0
- Actionable biosafety-risk instruction count: 0
- Real-world infectivity optimization count: 0
- Immune evasion optimization count: 0
- Real host range prediction count: 0
- Simulator implementation count: 0
- Dynamics implementation count: 0
- Executable toy simulator count: 0
- Real biological dataset import count: 0

Research boundary claims:
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is safety-test scaffolding only.
This milestone is not simulator implementation.
This milestone is not dynamics implementation.
This milestone is not an executable toy simulator.
This milestone is not real pathogen simulation.
This milestone is not real receptor parameterization.
This milestone is not operational host targeting.
This milestone is not wet-lab protocol work.
This milestone is not actionable biosafety-risk instruction.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.185 - Safe Toy Simulation Safety Test Scaffolding" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 265: Safe Toy Simulation Safety Test Scaffolding")
    print("Question: Can Viruse Fabric define safety-test scaffolding before simulator implementation while preserving non-operational biological safety boundaries and zero claims for implementation, verification, validation, readiness, and citations?")
    print("Title: Safe Toy Simulation Safety Test Scaffolding v8.185")
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

        if result.boundary_phrase_count < 14:
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
        "Interpretation: The v8.185 artifact defines safety-test scaffolding before simulator implementation while preserving zero counts for simulator implementation, dynamics implementation, executable toy simulator, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 265 completed successfully.")
    print("V8_185_SAFE_TOY_SIMULATION_SAFETY_TEST_SCAFFOLDING_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
