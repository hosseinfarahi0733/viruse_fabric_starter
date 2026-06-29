from __future__ import annotations

import csv
import json
from pathlib import Path

from viruse_fabric.simulation.safe_abstract_toy_dynamics_run_export import (
    build_toy_run_records,
    build_toy_run_metrics_summary,
    write_toy_run_exports,
)
from viruse_fabric.writing.safe_abstract_toy_dynamics_run_export_and_metrics_report import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_dynamics_kernel_unit_test_package_v8_190.md")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_dynamics_run_export_and_metrics_report_v8_191.md")
JSON_PATH = Path("outputs/safe_abstract_toy_dynamics_run_export_v8_191.json")
CSV_PATH = Path("outputs/safe_abstract_toy_dynamics_run_export_v8_191.csv")
NOTE_PATH = Path("notes/theory_log.md")


def run_export_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    summary = write_toy_run_exports(JSON_PATH, CSV_PATH)
    if summary["toy_run_export_record_count"] != 3:
        errors.append("Expected 3 exported toy run records.")
    if summary["toy_run_all_safety_passed"] is not True:
        errors.append("Expected all exported toy runs to pass safety guard.")
    if not JSON_PATH.exists():
        errors.append("JSON export missing.")
    if not CSV_PATH.exists():
        errors.append("CSV export missing.")

    records = build_toy_run_records()
    metrics = build_toy_run_metrics_summary(records)
    if metrics["toy_run_record_count"] != 3:
        errors.append("Metrics summary record count mismatch.")
    if not (0.0 <= metrics["mean_final_observation_score"] <= 1.0):
        errors.append("Mean observation score out of range.")
    if not (0.0 <= metrics["mean_targeted_looking_pattern_score"] <= 1.0):
        errors.append("Mean pattern score out of range.")

    if JSON_PATH.exists():
        payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        if payload["metrics_summary"]["toy_run_record_count"] != 3:
            errors.append("JSON payload record count mismatch.")
        if payload["boundary"]["real_pathogen_simulation_count"] != 0:
            errors.append("JSON payload safety boundary mismatch.")

    if CSV_PATH.exists():
        with CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != 3:
            errors.append(f"Expected 3 CSV rows, got {len(rows)}")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.191 - Safe Abstract Toy Dynamics Run Export and Metrics Report

Status: main run export and metrics report completed on branch `v8-191-safe-abstract-toy-dynamics-run-export-and-metrics-report`.

This milestone exports safe abstract toy dynamics run results into JSON and CSV artifacts.

Positive export claims:
- Safe abstract toy dynamics run export and metrics report count: 1
- New safe abstract toy dynamics run export and metrics report count: 1
- Toy dynamics run export module count: 1
- Toy dynamics JSON export count: 1
- Toy dynamics CSV export count: 1
- Toy dynamics exported record count: 3
- Toy dynamics exported fixture result count: 3
- Toy dynamics metrics summary count: 1
- Toy observation metric row count: 3
- Targeted-looking pattern metric row count: 3
- Toy run all safety passed count: 1
- Toy run export direct execution count: 1

Imported kernel/test claims:
- Safe abstract toy dynamics kernel unit test package count: 1
- Toy dynamics kernel unit test file count: 1
- Toy dynamics kernel unittest case count: 10
- Toy dynamics kernel unit test execution count: 1
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

This milestone exports toy dynamics run metrics only.
This milestone is not real biological dataset import.
This milestone is not real pathogen simulation.
This milestone is not real receptor parameterization.
This milestone is not operational host targeting.
This milestone is not wet-lab protocol work.
This milestone is not actionable biosafety-risk instruction.
This milestone is not external validation.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.191 - Safe Abstract Toy Dynamics Run Export and Metrics Report" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 271: Safe Abstract Toy Dynamics Run Export and Metrics Report")
    print("Question: Can Viruse Fabric export safe toy dynamics run metrics while preserving all real-biological and validation/readiness/citation boundary zeros?")
    print("Title: Safe Abstract Toy Dynamics Run Export and Metrics Report v8.191")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"JSON path: {JSON_PATH}")
    print(f"CSV path: {CSV_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")

    errors: list[str] = []
    warnings: list[str] = []

    export_errors, export_warnings = run_export_tests()
    errors.extend(export_errors)
    warnings.extend(export_warnings)

    if not SOURCE_PATH.exists():
        errors.append(f"Missing source artifact: {SOURCE_PATH}")
    else:
        result = write_report(
            SOURCE_PATH,
            OUTPUT_PATH,
            json_path=JSON_PATH,
            csv_path=CSV_PATH,
        )

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
        "Interpretation: The v8.191 artifact exports safe abstract toy dynamics run results into JSON and CSV metrics artifacts while preserving simulator implementation count 1, dynamics implementation count 1, executable toy simulator count 1, and zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 271 completed successfully.")
    print("V8_191_SAFE_ABSTRACT_TOY_DYNAMICS_RUN_EXPORT_AND_METRICS_REPORT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
