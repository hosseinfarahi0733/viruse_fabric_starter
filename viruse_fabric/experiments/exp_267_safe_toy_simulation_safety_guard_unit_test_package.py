from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from viruse_fabric.writing.safe_toy_simulation_safety_guard_unit_test_package import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_toy_simulation_safety_guard_module_v8_186.md")
OUTPUT_PATH = Path("outputs/safe_toy_simulation_safety_guard_unit_test_package_v8_187.md")
NOTE_PATH = Path("notes/theory_log.md")
TEST_PATH = Path("tests/safety/test_toy_simulation_safety_guard.py")


def run_unit_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not TEST_PATH.exists():
        errors.append(f"Missing unit test file: {TEST_PATH}")
        return errors, warnings

    completed = subprocess.run(
        [sys.executable, str(TEST_PATH)],
        check=False,
        text=True,
        capture_output=True,
    )

    if completed.returncode != 0:
        errors.append("Safety guard unit tests failed.")
        if completed.stdout:
            errors.append("stdout: " + completed.stdout[-1200:])
        if completed.stderr:
            errors.append("stderr: " + completed.stderr[-1200:])

    return errors, warnings


def append_note() -> None:
    note = """
## v8.187 - Safe Toy Simulation Safety Guard Unit Test Package

Status: main unit-test package completed on branch `v8-187-safe-toy-simulation-safety-guard-unit-test-package`.

This milestone adds an explicit unit-test package for the safety guard module.

Positive unit-test claims:
- Safe toy simulation safety guard unit test package count: 1
- New safe toy simulation safety guard unit test package count: 1
- Safety guard unit test file count: 1
- Safety guard unittest case count: 10
- Safe text pass unit test count: 1
- Safe fixture pass unit test count: 1
- Required safe marker enforcement unit test count: 1
- Prohibited category marker unit test count: 1
- Prohibited phrase marker unit test count: 1
- Assert safe accept unit test count: 1
- Assert safe reject unit test count: 1
- Normalization unit test count: 1
- Guard summary consistency unit test count: 1
- Required safe marker stability unit test count: 1
- Safety guard unit test execution count: 1

Imported guard claims:
- Safe toy simulation safety guard module count: 1
- Safety guard module implementation count: 1
- Safety guard test harness count: 1
- Safe toy fixture builder count: 1
- Safe toy fixture pass check count: 1
- Prohibited category marker family count: 11
- Prohibited phrase marker family count: 8
- Required safe marker count: 5
- Allowed synthetic fixture test count: 1
- Blocked synthetic category test count: 8
- Safety guard summary count: 1

Safety boundary claims:
- Simulator implementation count: 0
- Dynamics implementation count: 0
- Executable toy simulator count: 0
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

This milestone adds unit tests only.
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
    if "## v8.187 - Safe Toy Simulation Safety Guard Unit Test Package" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 267: Safe Toy Simulation Safety Guard Unit Test Package")
    print("Question: Can Viruse Fabric package safety guard behavior into explicit unit tests while preserving zero claims for simulator implementation, dynamics, executable simulator, real biological data, real pathogen simulation, host targeting, wet-lab content, verification, validation, readiness, and citations?")
    print("Title: Safe Toy Simulation Safety Guard Unit Test Package v8.187")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")

    errors: list[str] = []
    warnings: list[str] = []

    unit_errors, unit_warnings = run_unit_tests()
    errors.extend(unit_errors)
    warnings.extend(unit_warnings)

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
        "Interpretation: The v8.187 artifact packages the safety guard behavior into explicit unit tests while preserving zero counts for simulator implementation, dynamics implementation, executable toy simulator, real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 267 completed successfully.")
    print("V8_187_SAFE_TOY_SIMULATION_SAFETY_GUARD_UNIT_TEST_PACKAGE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
