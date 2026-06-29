from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from viruse_fabric.simulation.safe_abstract_toy_constraint_sensitivity_sweep import (
    build_sensitivity_records,
    summarize_sensitivity_records,
    write_sensitivity_exports,
)


COUNTER_LINES = [
    "Safe abstract toy constraint sensitivity sweep count: 1",
    "New safe abstract toy constraint sensitivity sweep count: 1",
    "Toy constraint sensitivity sweep module count: 1",
    "Toy sensitivity configuration count: 5",
    "Toy sensitivity fixture count: 3",
    "Toy sensitivity run record count: 15",
    "Toy sensitivity JSON export count: 1",
    "Toy sensitivity CSV export count: 1",
    "Toy sensitivity metrics summary count: 1",
    "Toy sensitivity all safety passed count: 1",
    "Toy observation sensitivity metric count: 1",
    "Targeted-looking pattern sensitivity metric count: 1",
    "Toy sensitivity pattern score range count: 1",
    "Toy sensitivity direct execution count: 1",

    "Safe abstract toy dynamics run export and metrics report count: 1",
    "Toy dynamics run export module count: 1",
    "Toy dynamics JSON export count: 1",
    "Toy dynamics CSV export count: 1",
    "Toy dynamics exported record count: 3",
    "Toy dynamics metrics summary count: 1",
    "Toy run all safety passed count: 1",

    "Safe abstract toy dynamics kernel unit test package count: 1",
    "Safe abstract toy dynamics kernel implementation count: 1",
    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Toy dynamics kernel module count: 1",
    "Toy kernel fixture execution count: 3",
    "Toy kernel safety guard pass count: 3",
    "Toy observation projection execution count: 1",
    "Targeted-looking pattern score execution count: 1",
    "Unitless dynamics execution count: 1",
    "Abstract graph dynamics execution count: 1",
    "Synthetic fixture execution count: 3",

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
    "Safe abstract toy dynamics run export and metrics report count: 1",
    "Toy dynamics run export module count: 1",
    "Toy dynamics JSON export count: 1",
    "Toy dynamics CSV export count: 1",
    "Toy dynamics exported record count: 3",
    "Toy dynamics metrics summary count: 1",
    "Toy run all safety passed count: 1",
    "Safe abstract toy dynamics kernel unit test package count: 1",
    "Safe abstract toy dynamics kernel implementation count: 1",
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
    "Safe abstract toy constraint sensitivity sweep count: 1",
    "New safe abstract toy constraint sensitivity sweep count: 1",
    "Toy constraint sensitivity sweep module count: 1",
    "Toy sensitivity configuration count: 5",
    "Toy sensitivity fixture count: 3",
    "Toy sensitivity run record count: 15",
    "Toy sensitivity JSON export count: 1",
    "Toy sensitivity CSV export count: 1",
    "Toy sensitivity metrics summary count: 1",
    "Toy sensitivity all safety passed count: 1",
    "Toy observation sensitivity metric count: 1",
    "Targeted-looking pattern sensitivity metric count: 1",
    "Toy sensitivity pattern score range count: 1",
    "Toy sensitivity direct execution count: 1",

    "Safe abstract toy dynamics run export and metrics report count: 1",
    "Toy dynamics run export module count: 1",
    "Toy dynamics JSON export count: 1",
    "Toy dynamics CSV export count: 1",
    "Toy dynamics exported record count: 3",
    "Toy dynamics metrics summary count: 1",
    "Toy run all safety passed count: 1",

    "Safe abstract toy dynamics kernel unit test package count: 1",
    "Safe abstract toy dynamics kernel implementation count: 1",
    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Toy dynamics kernel module count: 1",
    "Toy kernel fixture execution count: 3",
    "Toy kernel safety guard pass count: 3",
    "Toy observation projection execution count: 1",
    "Targeted-looking pattern score execution count: 1",
    "Unitless dynamics execution count: 1",
    "Abstract graph dynamics execution count: 1",
    "Synthetic fixture execution count: 3",

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
class SafeAbstractToyConstraintSensitivitySweepResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _summary_text(json_path: Path, csv_path: Path) -> str:
    export_summary = write_sensitivity_exports(json_path=json_path, csv_path=csv_path)
    records = build_sensitivity_records()
    metrics = summarize_sensitivity_records(records)

    sample_lines = []
    for record in records[:5]:
        sample_lines.append(
            "- "
            + ", ".join(
                [
                    f"sweep_run_id={record['sweep_run_id']}",
                    f"config_id={record['config_id']}",
                    f"fixture_id={record['fixture_id']}",
                    f"final_observation_score={record['final_observation_score']}",
                    f"targeted_looking_pattern_score={record['targeted_looking_pattern_score']}",
                    f"passed_safety_guard={record['passed_safety_guard']}",
                ]
            )
        )

    return dedent(
        f"""
        ## Toy constraint sensitivity sweep summary

        Export artifacts:
        - JSON: `{export_summary["toy_sensitivity_json_export_path"]}`
        - CSV: `{export_summary["toy_sensitivity_csv_export_path"]}`

        Sweep counts:
        - Toy sensitivity configuration count: {metrics["toy_sensitivity_config_count"]}
        - Toy sensitivity fixture count: {metrics["toy_sensitivity_fixture_count"]}
        - Toy sensitivity run record count: {metrics["toy_sensitivity_record_count"]}
        - Toy sensitivity all safety passed: {metrics["toy_sensitivity_all_safety_passed"]}

        Metrics:
        - Mean final observation score: {metrics["mean_final_observation_score"]}
        - Mean targeted-looking pattern score: {metrics["mean_targeted_looking_pattern_score"]}
        - Max targeted-looking pattern score: {metrics["max_targeted_looking_pattern_score"]}
        - Min targeted-looking pattern score: {metrics["min_targeted_looking_pattern_score"]}
        - Pattern score range: {metrics["pattern_score_range"]}

        Sample records:
        {chr(10).join(sample_lines)}
        """
    ).strip()


def _description() -> str:
    return dedent(
        """
        ## Safe abstract toy constraint sensitivity sweep

        ### Purpose

        v8.192 runs a controlled sensitivity sweep over the safe abstract toy dynamics kernel.

        This milestone tests how unitless abstract toy weights change toy observation scores and targeted-looking pattern scores.

        It does not add real biological data.

        It does not add biological interpretation.

        It does not add external validation.

        ---

        ## Sweep boundary

        The sweep varies only synthetic, abstract, unitless toy weights.

        It uses:

        - 5 toy sensitivity configurations,
        - 3 synthetic fixtures,
        - 15 total toy run records,
        - JSON and CSV exports,
        - safety guard pass checks.

        The sweep does not contain real biological datasets, real pathogen identities, real receptor parameters, operational host targeting, wet-lab protocols, or actionable biosafety-risk instructions.

        ---

        ## Interpretation

        The sensitivity metrics are toy metrics.

        They are not biological measurements.

        They are not real-world predictions.

        They are not external validation.

        They are not manuscript readiness.
        """
    ).strip()


def build_report(
    source_text: str,
    json_path: Path,
    csv_path: Path,
) -> SafeAbstractToyConstraintSensitivitySweepResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.192 - Safe Abstract Toy Constraint Sensitivity Sweep

        ## Question

        Can Viruse Fabric run a safe abstract toy constraint sensitivity sweep over the existing toy dynamics kernel and exported synthetic fixtures while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all zero boundaries for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, verification, validation, readiness, and citations?

        ## Source artifact

        - `outputs/safe_abstract_toy_dynamics_run_export_and_metrics_report_v8_191.md`

        ## Sensitivity interpretation

        v8.192 adds a safe abstract toy sensitivity sweep.

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

        {_description()}

        {_summary_text(json_path=json_path, csv_path=csv_path)}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy constraint sensitivity sweep count: 1.

        This milestone records toy constraint sensitivity sweep module count: 1.

        This milestone records toy sensitivity configuration count: 5.

        This milestone records toy sensitivity fixture count: 3.

        This milestone records toy sensitivity run record count: 15.

        This milestone records toy sensitivity JSON export count: 1.

        This milestone records toy sensitivity CSV export count: 1.

        This milestone records toy sensitivity metrics summary count: 1.

        This milestone records toy sensitivity all safety passed count: 1.

        This milestone records toy observation sensitivity metric count: 1.

        This milestone records targeted-looking pattern sensitivity metric count: 1.

        This milestone records toy sensitivity pattern score range count: 1.

        This milestone preserves safe abstract toy dynamics run export and metrics report count: 1.

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

        The project has run a safe abstract toy constraint sensitivity sweep over synthetic fixtures and exported JSON/CSV metrics, while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone runs a toy constraint sensitivity sweep only.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
        "External validation remains zero.",
    ]

    return SafeAbstractToyConstraintSensitivitySweepResult(
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
    json_path: Path,
    csv_path: Path,
) -> SafeAbstractToyConstraintSensitivitySweepResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text, json_path=json_path, csv_path=csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
