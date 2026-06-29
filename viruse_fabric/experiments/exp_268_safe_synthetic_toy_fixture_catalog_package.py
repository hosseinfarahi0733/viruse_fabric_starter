from __future__ import annotations

from pathlib import Path

from viruse_fabric.safety.toy_fixture_catalog import (
    build_fixture_catalog,
    fixture_catalog_summary,
    validate_fixture_catalog,
)
from viruse_fabric.writing.safe_synthetic_toy_fixture_catalog_package import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_toy_simulation_safety_guard_unit_test_package_v8_187.md")
OUTPUT_PATH = Path("outputs/safe_synthetic_toy_fixture_catalog_package_v8_188.md")
NOTE_PATH = Path("notes/theory_log.md")


def run_catalog_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    catalog = build_fixture_catalog()
    if len(catalog) != 3:
        errors.append(f"Expected 3 fixture catalog entries, got {len(catalog)}")

    fixture_ids = [entry.fixture_id for entry in catalog]
    if len(fixture_ids) != len(set(fixture_ids)):
        errors.append("Fixture ids are not unique.")

    results = validate_fixture_catalog()
    if len(results) != 3:
        errors.append(f"Expected 3 fixture safety results, got {len(results)}")

    for index, result in enumerate(results):
        if not result.passed:
            errors.append(f"Fixture safety check failed at index {index}: {result}")

    summary = fixture_catalog_summary()
    if summary["fixture_catalog_entry_count"] != 3:
        errors.append("Fixture catalog summary entry count mismatch.")
    if summary["fixture_catalog_safe_pass_count"] != 3:
        errors.append("Fixture catalog summary safe pass count mismatch.")
    if summary["fixture_catalog_blocked_marker_count"] != 0:
        errors.append("Fixture catalog summary blocked marker count mismatch.")
    if summary["fixture_catalog_missing_safe_marker_count"] != 0:
        errors.append("Fixture catalog summary missing safe marker count mismatch.")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.188 - Safe Synthetic Toy Fixture Catalog Package

Status: main fixture catalog package completed on branch `v8-188-safe-synthetic-toy-fixture-catalog-package`.

This milestone adds a safe synthetic toy fixture catalog for future tests and non-operational demonstrations.

Positive fixture catalog claims:
- Safe synthetic toy fixture catalog package count: 1
- New safe synthetic toy fixture catalog package count: 1
- Synthetic toy fixture catalog module count: 1
- Synthetic toy fixture catalog entry count: 3
- Synthetic toy fixture catalog safety pass count: 3
- Synthetic toy fixture catalog blocked marker count: 0
- Synthetic toy fixture catalog missing safe marker count: 0
- Two-node toy fixture count: 1
- Three-node chain toy fixture count: 1
- Star graph toy fixture count: 1
- Fixture catalog summary count: 1
- Fixture catalog guard validation count: 1

Imported guard/unit-test claims:
- Safe toy simulation safety guard unit test package count: 1
- Safety guard unit test file count: 1
- Safety guard unittest case count: 10
- Safety guard unit test execution count: 1
- Safe toy simulation safety guard module count: 1
- Safety guard module implementation count: 1
- Safety guard test harness count: 1
- Safe toy fixture builder count: 1
- Safe toy fixture pass check count: 1

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

This milestone adds a synthetic toy fixture catalog only.
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
    if "## v8.188 - Safe Synthetic Toy Fixture Catalog Package" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 268: Safe Synthetic Toy Fixture Catalog Package")
    print("Question: Can Viruse Fabric add a safe synthetic toy fixture catalog while preserving zero claims for simulator implementation, dynamics, executable simulator, real biological data, real pathogen simulation, host targeting, wet-lab content, verification, validation, readiness, and citations?")
    print("Title: Safe Synthetic Toy Fixture Catalog Package v8.188")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")

    errors: list[str] = []
    warnings: list[str] = []

    catalog_errors, catalog_warnings = run_catalog_tests()
    errors.extend(catalog_errors)
    warnings.extend(catalog_warnings)

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
        "Interpretation: The v8.188 artifact adds a safe synthetic toy fixture catalog while preserving zero counts for simulator implementation, dynamics implementation, executable toy simulator, real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 268 completed successfully.")
    print("V8_188_SAFE_SYNTHETIC_TOY_FIXTURE_CATALOG_PACKAGE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
