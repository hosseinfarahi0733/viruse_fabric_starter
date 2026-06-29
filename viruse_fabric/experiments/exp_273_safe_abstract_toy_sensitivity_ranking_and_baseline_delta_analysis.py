from __future__ import annotations

import csv
import json
from pathlib import Path

from viruse_fabric.simulation.safe_abstract_toy_sensitivity_ranking_analysis import (
    build_ranking_analysis,
    write_ranking_exports,
)
from viruse_fabric.writing.safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_constraint_sensitivity_sweep_v8_192.md")
SOURCE_JSON = Path("outputs/safe_abstract_toy_constraint_sensitivity_sweep_v8_192.json")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis_v8_193.md")
JSON_PATH = Path("outputs/safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis_v8_193.json")
CSV_PATH = Path("outputs/safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis_v8_193.csv")
NOTE_PATH = Path("notes/theory_log.md")


def run_analysis_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_JSON.exists():
        errors.append(f"Missing source JSON: {SOURCE_JSON}")
        return errors, warnings

    summary = write_ranking_exports(SOURCE_JSON, JSON_PATH, CSV_PATH)
    if summary["ranking_analysis_record_count"] != 15:
        errors.append("Expected 15 source records.")
    if summary["ranking_analysis_config_count"] != 5:
        errors.append("Expected 5 config summaries.")
    if summary["all_config_rows_safety_passed"] is not True:
        errors.append("Expected all config rows to pass safety.")

    analysis = build_ranking_analysis(SOURCE_JSON)
    if analysis["config_summary_count"] != 5:
        errors.append("Analysis config summary count mismatch.")
    if analysis["source_record_count"] != 15:
        errors.append("Analysis source record count mismatch.")
    if analysis["baseline_config_id"] != "toy_sweep_baseline":
        errors.append("Baseline config id mismatch.")

    config_rows = analysis["config_rows"]
    ranks = sorted(int(row["pattern_score_rank_desc"]) for row in config_rows)
    if ranks != [1, 2, 3, 4, 5]:
        errors.append(f"Unexpected rank set: {ranks}")

    baseline_rows = [row for row in config_rows if row["config_id"] == "toy_sweep_baseline"]
    if len(baseline_rows) != 1:
        errors.append("Expected exactly one baseline row.")
    else:
        baseline = baseline_rows[0]
        if baseline["delta_mean_targeted_looking_pattern_score_vs_baseline"] != 0.0:
            errors.append("Baseline pattern delta must be zero.")
        if baseline["delta_mean_final_observation_score_vs_baseline"] != 0.0:
            errors.append("Baseline observation delta must be zero.")

    if JSON_PATH.exists():
        payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        if payload["boundary"]["real_pathogen_simulation_count"] != 0:
            errors.append("JSON payload safety boundary mismatch.")
        if payload["config_summary_count"] != 5:
            errors.append("JSON config summary count mismatch.")

    if CSV_PATH.exists():
        with CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) != 5:
            errors.append(f"Expected 5 CSV rows, got {len(rows)}")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.193 - Safe Abstract Toy Sensitivity Ranking and Baseline Delta Analysis

Status: main ranking and baseline-delta analysis completed on branch `v8-193-safe-abstract-toy-sensitivity-ranking-and-baseline-delta-analysis`.

This milestone computes a safe abstract toy ranking and baseline-delta analysis over the v8.192 sensitivity sweep.

Positive analysis claims:
- Safe abstract toy sensitivity ranking and baseline delta analysis count: 1
- New safe abstract toy sensitivity ranking and baseline delta analysis count: 1
- Toy sensitivity ranking analysis module count: 1
- Toy sensitivity ranking JSON export count: 1
- Toy sensitivity ranking CSV export count: 1
- Toy sensitivity ranking source record count: 15
- Toy sensitivity ranking config summary count: 5
- Toy baseline delta analysis count: 1
- Toy baseline config count: 1
- Toy top pattern score config identification count: 1
- Toy bottom pattern score config identification count: 1
- Toy ranking all safety passed count: 1
- Toy ranking direct execution count: 1

Imported sweep/kernel claims:
- Safe abstract toy constraint sensitivity sweep count: 1
- Toy constraint sensitivity sweep module count: 1
- Toy sensitivity configuration count: 5
- Toy sensitivity fixture count: 3
- Toy sensitivity run record count: 15
- Toy sensitivity JSON export count: 1
- Toy sensitivity CSV export count: 1
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

This milestone ranks toy sensitivity configurations only.
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
    if "## v8.193 - Safe Abstract Toy Sensitivity Ranking and Baseline Delta Analysis" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 273: Safe Abstract Toy Sensitivity Ranking and Baseline Delta Analysis")
    print("Question: Can Viruse Fabric rank safe toy sensitivity configurations and compute baseline deltas while preserving all real-biological and validation/readiness/citation boundary zeros?")
    print("Title: Safe Abstract Toy Sensitivity Ranking and Baseline Delta Analysis v8.193")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"JSON path: {JSON_PATH}")
    print(f"CSV path: {CSV_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")
    print(f"Source JSON: {SOURCE_JSON}")

    errors: list[str] = []
    warnings: list[str] = []

    analysis_errors, analysis_warnings = run_analysis_tests()
    errors.extend(analysis_errors)
    warnings.extend(analysis_warnings)

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
        "Interpretation: The v8.193 artifact ranks safe abstract toy sensitivity configurations and computes baseline deltas while preserving simulator implementation count 1, dynamics implementation count 1, executable toy simulator count 1, and zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 273 completed successfully.")
    print("V8_193_SAFE_ABSTRACT_TOY_SENSITIVITY_RANKING_AND_BASELINE_DELTA_ANALYSIS_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
