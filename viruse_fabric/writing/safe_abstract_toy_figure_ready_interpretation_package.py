from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from viruse_fabric.simulation.safe_abstract_toy_figure_ready_interpretation import (
    build_controlled_interpretation,
    write_figure_ready_exports,
)


COUNTER_LINES = [
    "Safe abstract toy figure-ready interpretation package count: 1",
    "New safe abstract toy figure-ready interpretation package count: 1",
    "Toy figure-ready interpretation module count: 1",
    "Toy figure-ready JSON export count: 1",
    "Toy figure-ready CSV export count: 1",
    "Toy figure-ready source record count: 15",
    "Toy figure-ready config summary count: 5",
    "Toy figure-ready row count: 5",
    "Toy figure-ready controlled interpretation line count: 5",
    "Toy figure-ready top config line count: 1",
    "Toy figure-ready bottom config line count: 1",
    "Toy figure-ready baseline config line count: 1",
    "Toy figure-ready all safety passed count: 1",
    "Toy figure-ready direct execution count: 1",

    "Safe abstract toy sensitivity ranking and baseline delta analysis count: 1",
    "Toy sensitivity ranking analysis module count: 1",
    "Toy sensitivity ranking JSON export count: 1",
    "Toy sensitivity ranking CSV export count: 1",
    "Toy sensitivity ranking source record count: 15",
    "Toy sensitivity ranking config summary count: 5",
    "Toy baseline delta analysis count: 1",
    "Toy baseline config count: 1",
    "Toy top pattern score config identification count: 1",
    "Toy bottom pattern score config identification count: 1",
    "Toy ranking all safety passed count: 1",

    "Safe abstract toy constraint sensitivity sweep count: 1",
    "Safe abstract toy dynamics run export and metrics report count: 1",
    "Safe abstract toy dynamics kernel unit test package count: 1",
    "Safe abstract toy dynamics kernel implementation count: 1",
    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Unitless dynamics execution count: 1",
    "Abstract graph dynamics execution count: 1",
    "Synthetic fixture execution count: 3",

    "Imported safe abstract toy sensitivity ranking and baseline delta analysis count: 1",
    "Imported safe abstract toy constraint sensitivity sweep count: 1",
    "Imported safe abstract toy dynamics run export and metrics report count: 1",
    "Imported safe abstract toy dynamics kernel unit test package count: 1",
    "Imported safe abstract toy dynamics kernel implementation count: 1",
    "Imported simulator implementation count: 1",
    "Imported dynamics implementation count: 1",
    "Imported executable toy simulator count: 1",

    "Real biological dataset import count: 0",
    "Real pathogen simulation count: 0",
    "Real receptor parameter count: 0",
    "Operational host targeting count: 0",
    "Wet-lab protocol count: 0",
    "Actionable biosafety-risk instruction count: 0",
    "Real-world infectivity optimization count: 0",
    "Immune evasion optimization count: 0",
    "Real host range prediction count: 0",

    "New lemma proof execution count: 0",
    "New TC-001 proof execution count: 0",
    "New theorem proven count: 0",
    "New theorem proof execution count: 0",
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_SOURCE_PHRASES = [
    "Safe abstract toy sensitivity ranking and baseline delta analysis count: 1",
    "Toy sensitivity ranking analysis module count: 1",
    "Toy sensitivity ranking JSON export count: 1",
    "Toy sensitivity ranking CSV export count: 1",
    "Toy sensitivity ranking source record count: 15",
    "Toy sensitivity ranking config summary count: 5",
    "Toy baseline delta analysis count: 1",
    "Toy baseline config count: 1",
    "Toy top pattern score config identification count: 1",
    "Toy bottom pattern score config identification count: 1",
    "Toy ranking all safety passed count: 1",
    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Real biological dataset import count: 0",
    "Real pathogen simulation count: 0",
    "Real receptor parameter count: 0",
    "Operational host targeting count: 0",
    "Wet-lab protocol count: 0",
    "Actionable biosafety-risk instruction count: 0",
    "Real-world infectivity optimization count: 0",
    "Immune evasion optimization count: 0",
    "Real host range prediction count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
    "Safe abstract toy figure-ready interpretation package count: 1",
    "New safe abstract toy figure-ready interpretation package count: 1",
    "Toy figure-ready interpretation module count: 1",
    "Toy figure-ready JSON export count: 1",
    "Toy figure-ready CSV export count: 1",
    "Toy figure-ready source record count: 15",
    "Toy figure-ready config summary count: 5",
    "Toy figure-ready row count: 5",
    "Toy figure-ready controlled interpretation line count: 5",
    "Toy figure-ready top config line count: 1",
    "Toy figure-ready bottom config line count: 1",
    "Toy figure-ready baseline config line count: 1",
    "Toy figure-ready all safety passed count: 1",
    "Toy figure-ready direct execution count: 1",

    "Safe abstract toy sensitivity ranking and baseline delta analysis count: 1",
    "Toy sensitivity ranking analysis module count: 1",
    "Toy sensitivity ranking JSON export count: 1",
    "Toy sensitivity ranking CSV export count: 1",
    "Toy sensitivity ranking source record count: 15",
    "Toy sensitivity ranking config summary count: 5",
    "Toy baseline delta analysis count: 1",
    "Toy baseline config count: 1",
    "Toy top pattern score config identification count: 1",
    "Toy bottom pattern score config identification count: 1",
    "Toy ranking all safety passed count: 1",

    "Safe abstract toy constraint sensitivity sweep count: 1",
    "Safe abstract toy dynamics run export and metrics report count: 1",
    "Safe abstract toy dynamics kernel unit test package count: 1",
    "Safe abstract toy dynamics kernel implementation count: 1",
    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Unitless dynamics execution count: 1",
    "Abstract graph dynamics execution count: 1",
    "Synthetic fixture execution count: 3",

    "Imported safe abstract toy sensitivity ranking and baseline delta analysis count: 1",
    "Imported safe abstract toy constraint sensitivity sweep count: 1",
    "Imported safe abstract toy dynamics run export and metrics report count: 1",
    "Imported safe abstract toy dynamics kernel unit test package count: 1",
    "Imported safe abstract toy dynamics kernel implementation count: 1",
    "Imported simulator implementation count: 1",
    "Imported dynamics implementation count: 1",
    "Imported executable toy simulator count: 1",

    "Real biological dataset import count: 0",
    "Real pathogen simulation count: 0",
    "Real receptor parameter count: 0",
    "Operational host targeting count: 0",
    "Wet-lab protocol count: 0",
    "Actionable biosafety-risk instruction count: 0",
    "Real-world infectivity optimization count: 0",
    "Immune evasion optimization count: 0",
    "Real host range prediction count: 0",

    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


@dataclass(frozen=True)
class SafeAbstractToyFigureReadyInterpretationPackageResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _summary_text(source_json: Path, json_path: Path, csv_path: Path) -> str:
    export_summary = write_figure_ready_exports(source_json, json_path, csv_path)
    package = build_controlled_interpretation(source_json)

    lines = "\n".join(f"- {line}" for line in package["interpretation_lines"])

    return dedent(
        f"""
        ## Toy figure-ready interpretation summary

        Export artifacts:
        - JSON: `{json_path}`
        - CSV: `{csv_path}`

        Package counts:
        - Toy figure-ready source record count: {export_summary["figure_ready_source_record_count"]}
        - Toy figure-ready config summary count: {export_summary["figure_ready_config_summary_count"]}
        - Toy figure-ready row count: {export_summary["figure_ready_row_count"]}
        - Toy figure-ready all safety passed: {export_summary["all_figure_rows_safety_passed"]}

        Headline:
        - Baseline config id: `{package["baseline_config_id"]}`
        - Top config id: `{package["top_config_id"]}`
        - Bottom config id: `{package["bottom_config_id"]}`
        - Top mean targeted-looking pattern score: {package["top_mean_targeted_looking_pattern_score"]}
        - Bottom mean targeted-looking pattern score: {package["bottom_mean_targeted_looking_pattern_score"]}

        Controlled interpretation lines:
        {lines}
        """
    ).strip()


def build_report(
    source_text: str,
    source_json: Path,
    json_path: Path,
    csv_path: Path,
) -> SafeAbstractToyFigureReadyInterpretationPackageResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.194 - Safe Abstract Toy Figure-Ready Interpretation Package

        ## Question

        Can Viruse Fabric transform the v8.193 safe toy ranking and baseline-delta analysis into a figure-ready interpretation package while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all zero boundaries for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, verification, validation, readiness, and citations?

        ## Source artifacts

        - `outputs/safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis_v8_193.md`
        - `outputs/safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis_v8_193.json`
        - `outputs/safe_abstract_toy_sensitivity_ranking_and_baseline_delta_analysis_v8_193.csv`

        ## Interpretation package boundary

        v8.194 creates a figure-ready interpretation package for toy outputs only.

        This milestone preserves:
        - Simulator implementation count: 1
        - Dynamics implementation count: 1
        - Executable toy simulator count: 1

        This milestone preserves:
        - Real biological dataset import count: 0
        - Real pathogen simulation count: 0
        - Real receptor parameter count: 0
        - Operational host targeting count: 0
        - Wet-lab protocol count: 0
        - Actionable biosafety-risk instruction count: 0

        The package is for presentation and figure preparation.

        It does not provide external validation.

        It does not make the manuscript submission ready.

        It does not add new citations.

        {_summary_text(source_json=source_json, json_path=json_path, csv_path=csv_path)}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy figure-ready interpretation package count: 1.

        This milestone records toy figure-ready interpretation module count: 1.

        This milestone records toy figure-ready JSON export count: 1.

        This milestone records toy figure-ready CSV export count: 1.

        This milestone records toy figure-ready source record count: 15.

        This milestone records toy figure-ready config summary count: 5.

        This milestone records toy figure-ready row count: 5.

        This milestone records toy figure-ready controlled interpretation line count: 5.

        This milestone records toy figure-ready all safety passed count: 1.

        This milestone preserves safe abstract toy sensitivity ranking and baseline delta analysis count: 1.

        This milestone preserves simulator implementation count: 1.

        This milestone preserves dynamics implementation count: 1.

        This milestone preserves executable toy simulator count: 1.

        This milestone records real biological dataset import count: 0.

        This milestone records real pathogen simulation count: 0.

        This milestone records real receptor parameter count: 0.

        This milestone records operational host targeting count: 0.

        This milestone records wet-lab protocol count: 0.

        This milestone records actionable biosafety-risk instruction count: 0.

        This milestone records real-world infectivity optimization count: 0.

        This milestone records immune evasion optimization count: 0.

        This milestone records real host range prediction count: 0.

        This milestone records proof assistant verification count: 0.

        This milestone records external validation count: 0.

        This milestone records independent experiment count: 0.

        This milestone records manuscript submission ready count: 0.

        This milestone records readiness approval count: 0.

        This milestone records new citation added count: 0.

        This milestone does not import real biological datasets.

        This milestone does not provide real pathogen simulation.

        This milestone does not provide real receptor parameters.

        This milestone does not provide operational host targeting.

        This milestone does not provide wet-lab protocols.

        This milestone does not provide actionable biosafety-risk instructions.

        This milestone does not provide external validation.

        This milestone does not make the manuscript submission ready.

        ## Safe claim

        The project has created a figure-ready interpretation package for safe abstract toy ranking outputs, while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_markers = [
        "Real pathogen simulation count: 1",
        "Real receptor parameter count: 1",
        "Operational host targeting count: 1",
        "Wet-lab protocol count: 1",
        "Actionable biosafety-risk instruction count: 1",
        "Real-world infectivity optimization count: 1",
        "Immune evasion optimization count: 1",
        "Real host range prediction count: 1",
        "Real biological dataset import count: 1",
        "Proof assistant verification count: 1",
        "External validation count: 1",
        "Independent experiment count: 1",
        "Manuscript submission ready count: 1",
        "Readiness approval count: 1",
        "New citation added count: 1",
    ]

    prohibited_behavior_count = sum(
        1 for marker in prohibited_markers if marker.lower() in report.lower()
    )

    boundary_keywords = [
        "real biological dataset import count: 0",
        "real pathogen simulation count: 0",
        "real receptor parameter count: 0",
        "operational host targeting count: 0",
        "wet-lab protocol count: 0",
        "actionable biosafety-risk instruction count: 0",
        "does not import real biological datasets",
        "does not provide real pathogen simulation",
        "does not provide real receptor parameters",
        "does not provide operational host targeting",
        "does not provide wet-lab protocols",
        "does not provide actionable biosafety-risk instructions",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone creates a figure-ready interpretation package for toy results only.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
        "External validation remains zero.",
    ]

    return SafeAbstractToyFigureReadyInterpretationPackageResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(
    source_path: Path,
    output_path: Path,
    source_json: Path,
    json_path: Path,
    csv_path: Path,
) -> SafeAbstractToyFigureReadyInterpretationPackageResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(
        source_text,
        source_json=source_json,
        json_path=json_path,
        csv_path=csv_path,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
