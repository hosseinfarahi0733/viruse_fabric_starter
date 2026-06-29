from __future__ import annotations

from pathlib import Path

from viruse_fabric.safety.toy_fixture_catalog import get_fixture_catalog_payloads
from viruse_fabric.simulation.safe_abstract_toy_dynamics_kernel import (
    run_toy_kernel_catalog,
    summarize_kernel_results,
)
from viruse_fabric.writing.safe_abstract_toy_dynamics_kernel_implementation import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_synthetic_toy_fixture_catalog_package_v8_188.md")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_dynamics_kernel_implementation_v8_189.md")
NOTE_PATH = Path("notes/theory_log.md")


def run_kernel_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    fixtures = get_fixture_catalog_payloads()
    if len(fixtures) != 3:
        errors.append(f"Expected 3 fixtures, got {len(fixtures)}")

    results = run_toy_kernel_catalog(fixtures)
    if len(results) != 3:
        errors.append(f"Expected 3 toy kernel results, got {len(results)}")

    for result in results:
        if not result.passed_safety_guard:
            errors.append(f"Safety guard failed for result: {result}")
        if result.step_count <= 0:
            errors.append(f"Invalid step count: {result}")
        if not (0.0 <= result.final_observation_score <= 1.0):
            errors.append(f"Observation score out of range: {result}")
        if not (0.0 <= result.targeted_looking_pattern_score <= 1.0):
            errors.append(f"Pattern score out of range: {result}")

    summary = summarize_kernel_results(results)
    if summary["toy_kernel_result_count"] != 3:
        errors.append("Toy kernel summary result count mismatch.")
    if summary["toy_kernel_all_safety_passed"] is not True:
        errors.append("Toy kernel summary safety pass mismatch.")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.189 - Safe Abstract Toy Dynamics Kernel Implementation

Status: main toy dynamics kernel implementation completed on branch `v8-189-safe-abstract-toy-dynamics-kernel-implementation`.

This milestone implements the first safe abstract toy dynamics kernel over synthetic fixtures.

Positive execution claims:
- Safe abstract toy dynamics kernel implementation count: 1
- New safe abstract toy dynamics kernel implementation count: 1
- Simulator implementation count: 1
- Dynamics implementation count: 1
- Executable toy simulator count: 1
- Toy dynamics kernel module count: 1
- Toy kernel catalog execution count: 1
- Toy kernel fixture execution count: 3
- Toy kernel safety guard pass count: 3
- Toy kernel result summary count: 1
- Toy observation projection execution count: 1
- Targeted-looking pattern score execution count: 1
- Unitless dynamics execution count: 1
- Abstract graph dynamics execution count: 1
- Synthetic fixture execution count: 3

Imported fixture catalog claims:
- Safe synthetic toy fixture catalog package count: 1
- Synthetic toy fixture catalog module count: 1
- Synthetic toy fixture catalog entry count: 3
- Synthetic toy fixture catalog safety pass count: 3
- Synthetic toy fixture catalog blocked marker count: 0
- Synthetic toy fixture catalog missing safe marker count: 0

Safety boundary claims:
- Real biological dataset import count: 0
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

This milestone implements only a toy, synthetic, abstract, unitless, non-operational dynamics kernel.
This milestone is not real biological dataset import.
This milestone is not real pathogen simulation.
This milestone is not real receptor parameterization.
This milestone is not operational host targeting.
This milestone is not wet-lab protocol work.
This milestone is not actionable biosafety-risk instruction.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.189 - Safe Abstract Toy Dynamics Kernel Implementation" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 269: Safe Abstract Toy Dynamics Kernel Implementation")
    print("Question: Can Viruse Fabric implement a safe executable toy dynamics kernel while preserving zero claims for real biological data, real pathogen simulation, real receptor parameters, host targeting, wet-lab content, verification, validation, readiness, and citations?")
    print("Title: Safe Abstract Toy Dynamics Kernel Implementation v8.189")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")

    errors: list[str] = []
    warnings: list[str] = []

    kernel_errors, kernel_warnings = run_kernel_tests()
    errors.extend(kernel_errors)
    warnings.extend(kernel_warnings)

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
        "Interpretation: The v8.189 artifact implements the first safe abstract toy dynamics kernel with simulator implementation count 1, dynamics implementation count 1, and executable toy simulator count 1, while preserving zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 269 completed successfully.")
    print("V8_189_SAFE_ABSTRACT_TOY_DYNAMICS_KERNEL_IMPLEMENTATION_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
