from __future__ import annotations

from pathlib import Path

from viruse_fabric.safety.toy_simulation_safety_guard import (
    assert_text_safe,
    build_safe_toy_fixture,
    check_fixture_safety,
    check_text_safety,
)
from viruse_fabric.writing.safe_toy_simulation_safety_guard_module import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_toy_simulation_safety_test_scaffolding_v8_185.md")
OUTPUT_PATH = Path("outputs/safe_toy_simulation_safety_guard_module_v8_186.md")
NOTE_PATH = Path("notes/theory_log.md")


def run_guard_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    safe_text = "toy synthetic abstract unitless non-operational fixture"
    safe_result = check_text_safety(safe_text)
    if not safe_result.passed:
        errors.append(f"Expected safe text to pass, got: {safe_result}")

    fixture = build_safe_toy_fixture()
    fixture_result = check_fixture_safety(fixture)
    if not fixture_result.passed:
        errors.append(f"Expected safe toy fixture to pass, got: {fixture_result}")

    blocked_samples = [
        "real_pathogen_identity toy synthetic abstract unitless non-operational",
        "real_receptor_parameter toy synthetic abstract unitless non-operational",
        "operational_host_targeting toy synthetic abstract unitless non-operational",
        "wet_lab_protocol toy synthetic abstract unitless non-operational",
        "actionable_biosafety_risk_instruction toy synthetic abstract unitless non-operational",
        "real_world_infectivity_optimization toy synthetic abstract unitless non-operational",
        "immune_evasion_optimization toy synthetic abstract unitless non-operational",
        "real_host_range_prediction toy synthetic abstract unitless non-operational",
    ]

    for sample in blocked_samples:
        blocked_result = check_text_safety(sample)
        if blocked_result.passed:
            errors.append(f"Expected blocked sample to fail: {sample}")

    try:
        assert_text_safe("toy synthetic abstract unitless non-operational content")
    except ValueError as exc:
        errors.append(f"assert_text_safe rejected allowed content: {exc}")

    try:
        assert_text_safe("operational_host_targeting toy synthetic abstract unitless non-operational")
        errors.append("assert_text_safe accepted blocked content.")
    except ValueError:
        pass

    return errors, warnings


def append_note() -> None:
    note = """
## v8.186 - Safe Toy Simulation Safety Guard Module

Status: main safety guard module completed on branch `v8-186-safe-toy-simulation-safety-guard-module`.

This milestone implements a concrete safety guard module and test harness before simulator implementation.

Positive guard claims:
- Safe toy simulation safety guard module count: 1
- New safe toy simulation safety guard module count: 1
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

Imported scaffolding claims:
- Safe toy simulation safety test scaffolding count: 1
- Safety guard scaffold count: 1
- Prohibited category checklist count: 1
- Safe toy fixture checklist count: 1
- Abstract-only enforcement checklist count: 1
- Non-operational boundary guard count: 1
- Pre-implementation safety gate count: 1
- Toy simulator safety test plan count: 1
- Blocked operational category count: 8

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

This milestone implements only the safety guard module.
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
    if "## v8.186 - Safe Toy Simulation Safety Guard Module" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 266: Safe Toy Simulation Safety Guard Module")
    print("Question: Can Viruse Fabric implement a safety guard module and test harness while preserving zero claims for simulator implementation, dynamics, real biological data, real pathogen simulation, real receptor parameters, host targeting, wet-lab content, verification, validation, readiness, and citations?")
    print("Title: Safe Toy Simulation Safety Guard Module v8.186")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")

    errors: list[str] = []
    warnings: list[str] = []

    guard_errors, guard_warnings = run_guard_tests()
    errors.extend(guard_errors)
    warnings.extend(guard_warnings)

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
        "Interpretation: The v8.186 artifact implements a safety guard module and test harness before simulator implementation while preserving zero counts for simulator implementation, dynamics implementation, executable toy simulator, real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 266 completed successfully.")
    print("V8_186_SAFE_TOY_SIMULATION_SAFETY_GUARD_MODULE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
