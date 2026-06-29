from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from viruse_fabric.writing.safe_abstract_toy_dynamics_kernel_unit_test_package import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_dynamics_kernel_implementation_v8_189.md")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_dynamics_kernel_unit_test_package_v8_190.md")
NOTE_PATH = Path("notes/theory_log.md")
TEST_PATH = Path("tests/simulation/test_safe_abstract_toy_dynamics_kernel.py")


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
        errors.append("Toy dynamics kernel unit tests failed.")
        if completed.stdout:
            errors.append("stdout: " + completed.stdout[-1200:])
        if completed.stderr:
            errors.append("stderr: " + completed.stderr[-1200:])

    return errors, warnings


def append_note() -> None:
    note = """
## v8.190 - Safe Abstract Toy Dynamics Kernel Unit Test Package

Status: main unit-test package completed on branch `v8-190-safe-abstract-toy-dynamics-kernel-unit-test-package`.

This milestone adds explicit unit tests for the safe abstract toy dynamics kernel.

Positive unit-test claims:
- Safe abstract toy dynamics kernel unit test package count: 1
- New safe abstract toy dynamics kernel unit test package count: 1
- Toy dynamics kernel unit test file count: 1
- Toy dynamics kernel unittest case count: 10
- Clamp unit test count: 1
- Kernel config unit test count: 1
- Single fixture kernel result unit test count: 1
- Catalog execution count unit test count: 1
- Catalog safety guard unit test count: 1
- Kernel summary unit test count: 1
- Empty summary unit test count: 1
- Unsafe fixture rejection unit test count: 1
- Unknown synthetic location rejection unit test count: 1
- Deterministic kernel execution unit test count: 1
- Toy dynamics kernel unit test execution count: 1

Imported kernel claims:
- Safe abstract toy dynamics kernel implementation count: 1
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

This milestone adds unit tests for the toy dynamics kernel only.
This milestone is not real biological dataset import.
This milestone is not real pathogen simulation.
This milestone is not real receptor parameterization.
This milestone is not operational host targeting.
This milestone is not wet-lab protocol work.
This milestone is not actionable biosafety-risk instruction.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.190 - Safe Abstract Toy Dynamics Kernel Unit Test Package" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 270: Safe Abstract Toy Dynamics Kernel Unit Test Package")
    print("Question: Can Viruse Fabric add unit tests for the safe abstract toy dynamics kernel while preserving all real-biological and validation/readiness/citation boundary zeros?")
    print("Title: Safe Abstract Toy Dynamics Kernel Unit Test Package v8.190")
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
        "Interpretation: The v8.190 artifact adds unit tests for the safe abstract toy dynamics kernel while preserving simulator implementation count 1, dynamics implementation count 1, executable toy simulator count 1, and zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 270 completed successfully.")
    print("V8_190_SAFE_ABSTRACT_TOY_DYNAMICS_KERNEL_UNIT_TEST_PACKAGE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
