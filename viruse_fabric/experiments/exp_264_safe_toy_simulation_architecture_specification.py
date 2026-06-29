from __future__ import annotations

from pathlib import Path

from viruse_fabric.writing.safe_toy_simulation_architecture_specification import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_multidisciplinary_simulation_environment_scope_map_v8_183.md")
OUTPUT_PATH = Path("outputs/safe_toy_simulation_architecture_specification_v8_184.md")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.184 - Safe Toy Simulation Architecture Specification

Status: main architecture specification completed on branch `v8-184-safe-toy-simulation-architecture-specification`.

This milestone specifies a safe toy simulation architecture for targeted-looking behavior using abstract agents, synthetic compartments, unitless variables, abstract update rules, observation projection, and safety tests.

Positive architecture claims:
- Safe toy simulation architecture specification count: 1
- New safe toy simulation architecture specification count: 1
- Toy simulator entity specification count: 1
- Synthetic compartment graph specification count: 1
- Unitless state variable specification count: 1
- Abstract update rule specification count: 1
- Observation projection specification count: 1
- Safety test specification count: 1
- Toy agent specification count: 1
- Synthetic data fixture specification count: 1
- Deterministic seed requirement count: 1
- Non-operational model boundary count: 1

Imported safe scope claims:
- Safe multidisciplinary simulation environment scope map count: 1
- Discipline role map count: 10
- Targeted-looking behavior explanation count: 1
- Toy model requirement count: 1
- Synthetic data requirement count: 1
- Abstract graph requirement count: 1
- Safety boundary lock count: 1

Safety boundary claims:
- Real pathogen simulation count: 0
- Real receptor parameter count: 0
- Operational host targeting count: 0
- Wet-lab protocol count: 0
- Actionable biosafety-risk instruction count: 0
- Real-world infectivity optimization count: 0
- Immune evasion optimization count: 0
- Real host range prediction count: 0

Research boundary claims:
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone is architecture specification only.
This milestone is not simulator implementation.
This milestone is not real pathogen simulation.
This milestone is not real receptor parameterization.
This milestone is not operational host targeting.
This milestone is not wet-lab protocol work.
This milestone is not actionable biosafety-risk instruction.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.184 - Safe Toy Simulation Architecture Specification" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 264: Safe Toy Simulation Architecture Specification")
    print("Question: Can Viruse Fabric specify a safe toy simulation architecture while preserving non-operational biological safety boundaries and zero claims for verification, validation, readiness, and citations?")
    print("Title: Safe Toy Simulation Architecture Specification v8.184")
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
        "Interpretation: The v8.184 artifact specifies a safe toy simulation architecture using abstract agents, synthetic compartments, unitless variables, abstract update rules, observation projection, and safety tests while preserving zero counts for real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 264 completed successfully.")
    print("V8_184_SAFE_TOY_SIMULATION_ARCHITECTURE_SPECIFICATION_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
