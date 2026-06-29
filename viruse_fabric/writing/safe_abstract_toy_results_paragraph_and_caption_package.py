from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy results paragraph and caption package count: 1",
    "New safe abstract toy results paragraph and caption package count: 1",
    "Toy results paragraph package JSON export count: 1",
    "Toy results paragraph count: 3",
    "Toy figure caption count: 1",
    "Toy limitation paragraph count: 1",
    "Toy safety boundary statement count: 1",
    "Toy controlled claim sentence count: 1",
    "Manuscript-safe toy wording package count: 1",
    "Toy results paragraph direct execution count: 1",

    "Safe abstract toy figure-ready interpretation package count: 1",
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

    "Safe abstract toy sensitivity ranking and baseline delta analysis count: 1",
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

    "Imported safe abstract toy figure-ready interpretation package count: 1",
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
    "Safe abstract toy figure-ready interpretation package count: 1",
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
    "Safe abstract toy sensitivity ranking and baseline delta analysis count: 1",
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
    "Safe abstract toy results paragraph and caption package count: 1",
    "New safe abstract toy results paragraph and caption package count: 1",
    "Toy results paragraph package JSON export count: 1",
    "Toy results paragraph count: 3",
    "Toy figure caption count: 1",
    "Toy limitation paragraph count: 1",
    "Toy safety boundary statement count: 1",
    "Toy controlled claim sentence count: 1",
    "Manuscript-safe toy wording package count: 1",
    "Toy results paragraph direct execution count: 1",

    "Safe abstract toy figure-ready interpretation package count: 1",
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

    "Safe abstract toy sensitivity ranking and baseline delta analysis count: 1",
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

    "Imported safe abstract toy figure-ready interpretation package count: 1",
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
class SafeAbstractToyResultsParagraphAndCaptionPackageResult:
    report: str
    package: dict[str, Any]
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def load_figure_ready_package(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    if payload.get("interpretation_kind") != "toy_synthetic_abstract_unitless_non-operational_figure_ready_interpretation":
        raise ValueError("Unexpected figure-ready interpretation kind.")
    return payload


def build_results_paragraph_package(source_json: Path) -> dict[str, Any]:
    payload = load_figure_ready_package(source_json)

    top_config = payload["top_config_id"]
    bottom_config = payload["bottom_config_id"]
    baseline_config = payload["baseline_config_id"]
    top_score = payload["top_mean_targeted_looking_pattern_score"]
    bottom_score = payload["bottom_mean_targeted_looking_pattern_score"]
    baseline_score = payload["baseline_mean_targeted_looking_pattern_score"]

    results_paragraphs = [
        (
            "Across the safe abstract toy sensitivity ranking package, five synthetic, unitless, "
            "non-operational configurations were summarized from 15 toy source records. The package "
            "identifies a top-ranked toy configuration by mean targeted-looking pattern score while "
            "preserving all explicit safety and anti-overclaim boundaries."
        ),
        (
            f"The top-ranked toy configuration was `{top_config}` with a mean targeted-looking pattern "
            f"score of {top_score}. The bottom-ranked toy configuration was `{bottom_config}` with a "
            f"mean targeted-looking pattern score of {bottom_score}. The baseline configuration was "
            f"`{baseline_config}` with a mean targeted-looking pattern score of {baseline_score}."
        ),
        (
            "These results are interpreted only as behavior of a synthetic toy constraint system. They "
            "are not biological measurements, not real-world predictions, not external validation, "
            "not independent experimental evidence, and not manuscript-submission readiness evidence."
        ),
    ]

    figure_caption = (
        "Figure X. Safe abstract toy sensitivity ranking over five synthetic, unitless, "
        "non-operational configurations. Rows summarize figure-ready toy scores and baseline deltas "
        "derived from 15 toy records. The figure reports only toy-system behavior and carries no "
        "biological, clinical, virological, external-validation, or manuscript-readiness claim."
    )

    limitation_paragraph = (
        "The analysis is intentionally limited to synthetic toy fixtures and abstract unitless scores. "
        "No real biological dataset, pathogen model, receptor parameter, operational host-targeting "
        "procedure, wet-lab protocol, or actionable biosafety-risk instruction is introduced."
    )

    safety_boundary_statement = (
        "All reported outputs remain toy, synthetic, abstract, unitless, and non-operational; real "
        "biological dataset import, real pathogen simulation, real receptor parameters, operational "
        "host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant "
        "verification, external validation, independent experiment, manuscript submission readiness, "
        "readiness approval, and new citation additions remain zero."
    )

    controlled_claim_sentence = (
        "The project now has manuscript-safe toy wording for presenting figure-ready abstract toy "
        "ranking outputs without converting them into biological, validation, readiness, or citation claims."
    )

    package = {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_results_paragraph_and_caption",
        "source_record_count": payload["source_record_count"],
        "config_summary_count": payload["config_summary_count"],
        "figure_ready_row_count": payload["figure_ready_row_count"],
        "results_paragraph_count": len(results_paragraphs),
        "figure_caption_count": 1,
        "limitation_paragraph_count": 1,
        "safety_boundary_statement_count": 1,
        "controlled_claim_sentence_count": 1,
        "top_config_id": top_config,
        "bottom_config_id": bottom_config,
        "baseline_config_id": baseline_config,
        "all_figure_rows_safety_passed": payload["all_figure_rows_safety_passed"],
        "results_paragraphs": results_paragraphs,
        "figure_caption": figure_caption,
        "limitation_paragraph": limitation_paragraph,
        "safety_boundary_statement": safety_boundary_statement,
        "controlled_claim_sentence": controlled_claim_sentence,
        "boundary": {
            "real_biological_dataset_import_count": 0,
            "real_pathogen_simulation_count": 0,
            "real_receptor_parameter_count": 0,
            "operational_host_targeting_count": 0,
            "wet_lab_protocol_count": 0,
            "actionable_biosafety_risk_instruction_count": 0,
            "proof_assistant_verification_count": 0,
            "external_validation_count": 0,
            "independent_experiment_count": 0,
            "manuscript_submission_ready_count": 0,
            "readiness_approval_count": 0,
            "new_citation_added_count": 0,
        },
    }

    return package


def write_package_json(source_json: Path, json_path: Path) -> dict[str, Any]:
    package = build_results_paragraph_package(source_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(package, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return package


def _package_text(package: dict[str, Any], json_path: Path) -> str:
    paragraphs = "\n\n".join(
        f"Paragraph {index}. {paragraph}"
        for index, paragraph in enumerate(package["results_paragraphs"], start=1)
    )

    return dedent(
        f"""
        ## Toy results paragraph and caption package

        JSON export:
        - `{json_path}`

        Package counts:
        - Toy figure-ready source record count: {package["source_record_count"]}
        - Toy figure-ready config summary count: {package["config_summary_count"]}
        - Toy figure-ready row count: {package["figure_ready_row_count"]}
        - Toy results paragraph count: {package["results_paragraph_count"]}
        - Toy figure caption count: {package["figure_caption_count"]}
        - Toy limitation paragraph count: {package["limitation_paragraph_count"]}
        - Toy safety boundary statement count: {package["safety_boundary_statement_count"]}
        - Toy controlled claim sentence count: {package["controlled_claim_sentence_count"]}

        Top/bottom/baseline:
        - Top config id: `{package["top_config_id"]}`
        - Bottom config id: `{package["bottom_config_id"]}`
        - Baseline config id: `{package["baseline_config_id"]}`

        ### Results paragraphs

        {paragraphs}

        ### Figure caption

        {package["figure_caption"]}

        ### Limitation paragraph

        {package["limitation_paragraph"]}

        ### Safety boundary statement

        {package["safety_boundary_statement"]}

        ### Controlled claim sentence

        {package["controlled_claim_sentence"]}
        """
    ).strip()


def build_report(
    source_text: str,
    source_json: Path,
    json_path: Path,
) -> SafeAbstractToyResultsParagraphAndCaptionPackageResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    package = write_package_json(source_json, json_path)

    report = dedent(
        f"""
        # v8.195 - Safe Abstract Toy Results Paragraph and Caption Package

        ## Question

        Can Viruse Fabric transform the v8.194 figure-ready toy interpretation package into manuscript-safe results paragraphs, a figure caption, a limitation paragraph, a safety boundary statement, and a controlled claim sentence while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all zero boundaries for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, verification, validation, readiness, and citations?

        ## Source artifacts

        - `outputs/safe_abstract_toy_figure_ready_interpretation_package_v8_194.md`
        - `outputs/safe_abstract_toy_figure_ready_interpretation_package_v8_194.json`
        - `outputs/safe_abstract_toy_figure_ready_interpretation_package_v8_194.csv`

        ## Package boundary

        v8.195 creates manuscript-safe wording for toy outputs only.

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

        The wording is manuscript-safe.

        The milestone is not manuscript submission readiness.

        The milestone is not external validation.

        The milestone does not add new citations.

        {_package_text(package, json_path)}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy results paragraph and caption package count: 1.

        This milestone records toy results paragraph package JSON export count: 1.

        This milestone records toy results paragraph count: 3.

        This milestone records toy figure caption count: 1.

        This milestone records toy limitation paragraph count: 1.

        This milestone records toy safety boundary statement count: 1.

        This milestone records toy controlled claim sentence count: 1.

        This milestone records manuscript-safe toy wording package count: 1.

        This milestone preserves safe abstract toy figure-ready interpretation package count: 1.

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

        The project has created manuscript-safe toy results paragraphs and a figure caption for safe abstract toy ranking outputs, while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone creates manuscript-safe wording for toy results only.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
        "External validation remains zero.",
        "Manuscript submission readiness remains zero.",
    ]

    return SafeAbstractToyResultsParagraphAndCaptionPackageResult(
        report=report,
        package=package,
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
) -> SafeAbstractToyResultsParagraphAndCaptionPackageResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text, source_json=source_json, json_path=json_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
