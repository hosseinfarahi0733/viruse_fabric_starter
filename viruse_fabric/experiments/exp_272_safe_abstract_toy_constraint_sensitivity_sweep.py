from __future__ import annotations

import csv
import json
from pathlib import Path

from viruse_fabric.simulation.safe_abstract_toy_constraint_sensitivity_sweep import (
    build_sensitivity_records,
    summarize_sensitivity_records,
    write_sensitivity_exports,
)
from viruse_fabric.writing.safe_abstract_toy_constraint_sensitivity_sweep import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_dynamics_run_export_and_metrics_report_v8_191.md")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_constraint_sensitivity_sweep_v8_192.md")
JSON_PATH = Path("outputs/safe_abstract_toy_constraint_sensitivity_sweep_v8_192.json")
CSV_PATH = Path("outputs/safe_abstract_toy_constraint_sensitivity_sweep_v8_192.csv")
NOTE_PATH = Path("notes/theory_log.md")


def run_sweep_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    summary = write_sensitivity_exports(JSON_PATH, CSV_PATH)
    if summary["toy_sensitivity_record_count"] != 15:
        errors.append("Expected 15 toy sensitivity records.")
    if summary["toy_sensitivity_config_count"] != 5:
        errors.append("Expected 5 toy sensitivity configurations.")
    if summary["toy_sensitivity_fixture_count"] != 3:
        errors.append("Expected 3 toy fixtures.")
    if summary["toy_sensitivity_all_safety_passed"] is not True:
        errors.append("Expected all toy sensitivity records to pass safety guard.")
    if not JSON_PATH.exists():
        errors.append("Sensitivity JSON export missing.")
    if not CSV_PATH.exists():
        errors.append("Sensitivity CSV export missing.")

    records = build_sensitivity_records()
    metrics = summarize_sensitivity_records(records)
    if metrics["toy_sensitivity_record_count"] != 15:
        errors.append("Sensitivity metrics record count mismatch.")
    if not (0.0 <= metrics["mean_final_observation_score"] <= 1.0):
        errors.append("Mean observation score out of range.")
    if not (0.0 <= metrics["mean_targeted_looking_pattern_score"] <= 1.0):
        errors.append("Mean pattern score out of range.")
    if metrics["pattern_score_range"] < 0.0:
        errors.append("Pattern score range cannot be negative.")

    if JSON_PATH.exists():
        payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        if payload["metrics_summary"]["toy_sensitivity_record_count"] != 15:
            errors.append("JSON payload sensitivity record count mismatch.")
        if payload["boundary"]["real_pathogen_simulation_count"] != 0:
            errors.append("JSON payload safety boundary mismatch.")

    if CSV_PATH.exists():
        with CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != 15:
            errors.append(f"Expected 15 CSV rows, got {len(rows)}")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.192 - Safe Abstract Toy Constraint Sensitivity Sweep

Status: main sensitivity sweep completed on branch `v8-192-safe-abstract-toy-constraint-sensitivity-sweep`.

This milestone runs a safe abstract toy constraint sensitivity sweep over the existing toy dynamics kernel and synthetic fixtures.

Positive sensitivity claims:
- Safe abstract toy constraint sensitivity sweep count: 1
- New safe abstract toy constraint sensitivity sweep count: 1
- Toy constraint sensitivity sweep module count: 1
- Toy sensitivity configuration count: 5
- Toy sensitivity fixture count: 3
- Toy sensitivity run record count: 15
- Toy sensitivity JSON export count: 1
- Toy sensitivity CSV export count: 1
- Toy sensitivity metrics summary count: 1
- Toy sensitivity all safety passed count: 1
- Toy observation sensitivity metric count: 1
- Targeted-looking pattern sensitivity metric count: 1
- Toy sensitivity pattern score range count: 1
- Toy sensitivity direct execution count: 1

Imported run/kernel claims:
- Safe abstract toy dynamics run export and metrics report count: 1
- Toy dynamics run export module count: 1
- Toy dynamics JSON export count: 1
- Toy dynamics CSV export count: 1
- Toy dynamics exported record count: 3
- Toy dynamics metrics summary count: 1
- Toy run all safety passed count: 1
- Safe abstract toy dynamics kernel unit test package count: 1
- Safe abstract toy dynamics kernel implementation count: 1
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

This milestone runs a toy sensitivity sweep only.
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
    if "## v8.192 - Safe Abstract Toy Constraint Sensitivity Sweep" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 272: Safe Abstract Toy Constraint Sensitivity Sweep")
    print("Question: Can Viruse Fabric run a safe toy constraint sensitivity sweep while preserving all real-biological and validation/readiness/citation boundary zeros?")
    print("Title: Safe Abstract Toy Constraint Sensitivity Sweep v8.192")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"JSON path: {JSON_PATH}")
    print(f"CSV path: {CSV_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")

    errors: list[str] = []
    warnings: list[str] = []

    sweep_errors, sweep_warnings = run_sweep_tests()
    errors.extend(sweep_errors)
    warnings.extend(sweep_warnings)

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
        "Interpretation: The v8.192 artifact runs a safe abstract toy constraint sensitivity sweep with 5 configurations and 15 synthetic toy records while preserving simulator implementation count 1, dynamics implementation count 1, executable toy simulator count 1, and zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 272 completed successfully.")
    print("V8_192_SAFE_ABSTRACT_TOY_CONSTRAINT_SENSITIVITY_SWEEP_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
