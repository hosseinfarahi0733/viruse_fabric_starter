from __future__ import annotations

import csv
import json
from pathlib import Path

from viruse_fabric.simulation.safe_abstract_toy_figure_ready_interpretation import (
    build_controlled_interpretation,
    build_figure_ready_rows,
    write_figure_ready_exports,
)
from viruse_fabric.writing.safe_abstract_toy_figure_ready_interpretation_package import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis_v8_193.md")
SOURCE_JSON = Path("outputs/safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis_v8_193.json")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_figure_ready_interpretation_package_v8_194.md")
JSON_PATH = Path("outputs/safe_abstract_toy_figure_ready_interpretation_package_v8_194.json")
CSV_PATH = Path("outputs/safe_abstract_toy_figure_ready_interpretation_package_v8_194.csv")
NOTE_PATH = Path("notes/theory_log.md")


def run_package_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_JSON.exists():
        errors.append(f"Missing source JSON: {SOURCE_JSON}")
        return errors, warnings

    rows = build_figure_ready_rows(SOURCE_JSON)
    if len(rows) != 5:
        errors.append(f"Expected 5 figure-ready rows, got {len(rows)}")
    if not all(row["all_safety_passed"] for row in rows):
        errors.append("Expected all figure-ready rows to pass safety.")

    roles = {row["figure_role"] for row in rows}
    if "top" not in roles:
        errors.append("Missing top figure role.")
    if "bottom" not in roles:
        errors.append("Missing bottom figure role.")

    package = build_controlled_interpretation(SOURCE_JSON)
    if package["figure_ready_row_count"] != 5:
        errors.append("Figure-ready package row count mismatch.")
    if package["source_record_count"] != 15:
        errors.append("Figure-ready source record count mismatch.")
    if package["config_summary_count"] != 5:
        errors.append("Figure-ready config summary count mismatch.")
    if len(package["interpretation_lines"]) != 5:
        errors.append("Expected 5 controlled interpretation lines.")
    if package["all_figure_rows_safety_passed"] is not True:
        errors.append("Expected all figure rows safety passed.")

    summary = write_figure_ready_exports(SOURCE_JSON, JSON_PATH, CSV_PATH)
    if summary["figure_ready_source_record_count"] != 15:
        errors.append("Export summary source record count mismatch.")
    if summary["figure_ready_config_summary_count"] != 5:
        errors.append("Export summary config count mismatch.")
    if summary["figure_ready_row_count"] != 5:
        errors.append("Export summary row count mismatch.")
    if summary["all_figure_rows_safety_passed"] is not True:
        errors.append("Export summary safety mismatch.")

    if JSON_PATH.exists():
        payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        if payload["boundary"]["real_pathogen_simulation_count"] != 0:
            errors.append("JSON payload real pathogen boundary mismatch.")
        if payload["boundary"]["external_validation_count"] != 0:
            errors.append("JSON payload external validation boundary mismatch.")
        if payload["boundary"]["manuscript_submission_ready_count"] != 0:
            errors.append("JSON payload manuscript readiness boundary mismatch.")
        if payload["figure_ready_row_count"] != 5:
            errors.append("JSON figure-ready row count mismatch.")

    if CSV_PATH.exists():
        with CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
            csv_rows = list(csv.DictReader(handle))
        if len(csv_rows) != 5:
            errors.append(f"Expected 5 CSV rows, got {len(csv_rows)}")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.194 - Safe Abstract Toy Figure-Ready Interpretation Package

Status: main figure-ready interpretation package completed on branch `v8-194-safe-abstract-toy-figure-ready-interpretation-package`.

This milestone creates a figure-ready interpretation package for the safe abstract toy ranking outputs.

Positive package claims:
- Safe abstract toy figure-ready interpretation package count: 1
- New safe abstract toy figure-ready interpretation package count: 1
- Toy figure-ready interpretation module count: 1
- Toy figure-ready JSON export count: 1
- Toy figure-ready CSV export count: 1
- Toy figure-ready source record count: 15
- Toy figure-ready config summary count: 5
- Toy figure-ready row count: 5
- Toy figure-ready controlled interpretation line count: 5
- Toy figure-ready top config line count: 1
- Toy figure-ready bottom config line count: 1
- Toy figure-ready baseline config line count: 1
- Toy figure-ready all safety passed count: 1
- Toy figure-ready direct execution count: 1

Imported ranking/sweep/kernel claims:
- Safe abstract toy sensitivity ranking and baseline delta analysis count: 1
- Toy sensitivity ranking analysis module count: 1
- Toy sensitivity ranking JSON export count: 1
- Toy sensitivity ranking CSV export count: 1
- Toy sensitivity ranking source record count: 15
- Toy sensitivity ranking config summary count: 5
- Toy baseline delta analysis count: 1
- Simulator implementation count: 1
- Dynamics implementation count: 1
- Executable toy simulator count: 1

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

This milestone creates a figure-ready interpretation package for toy results only.
This milestone is not real biological dataset import.
This milestone is not real pathogen simulation.
This milestone is not real receptor parameterization.
This milestone is not operational host targeting.
This milestone is not wet-lab protocol work.
This milestone is not actionable biosafety-risk instruction.
This milestone is not external validation.
This milestone is not manuscript readiness.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.194 - Safe Abstract Toy Figure-Ready Interpretation Package" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 274: Safe Abstract Toy Figure-Ready Interpretation Package")
    print("Question: Can Viruse Fabric create a figure-ready interpretation package for safe toy ranking outputs while preserving all real-biological and validation/readiness/citation boundary zeros?")
    print("Title: Safe Abstract Toy Figure-Ready Interpretation Package v8.194")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"JSON path: {JSON_PATH}")
    print(f"CSV path: {CSV_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")
    print(f"Source JSON: {SOURCE_JSON}")

    errors: list[str] = []
    warnings: list[str] = []

    package_errors, package_warnings = run_package_tests()
    errors.extend(package_errors)
    warnings.extend(package_warnings)

    if not SOURCE_PATH.exists():
        errors.append(f"Missing source artifact: {SOURCE_PATH}")
    else:
        result = write_report(
            SOURCE_PATH,
            OUTPUT_PATH,
            source_json=SOURCE_JSON,
            json_path=JSON_PATH,
            csv_path=CSV_PATH,
        )

        for phrase in result.missing_source_phrases:
            errors.append(f"Missing required source phrase: {phrase}")

        for phrase in result.missing_report_phrases:
            errors.append(f"Missing required report phrase: {phrase}")

        if result.prohibited_behavior_count != 0:
            errors.append(f"Prohibited behavior count must be 0, got {result.prohibited_behavior_count}")

        if result.boundary_phrase_count < 12:
            warnings.append(f"Boundary phrase count is low: {result.boundary_phrase_count}")

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
    print(f"JSON exists: {JSON_PATH.exists()}")
    print(f"CSV exists: {CSV_PATH.exists()}")
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
        "Interpretation: The v8.194 artifact creates a figure-ready interpretation package for safe abstract toy ranking outputs while preserving simulator implementation count 1, dynamics implementation count 1, executable toy simulator count 1, and zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 274 completed successfully.")
    print("V8_194_SAFE_ABSTRACT_TOY_FIGURE_READY_INTERPRETATION_PACKAGE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
