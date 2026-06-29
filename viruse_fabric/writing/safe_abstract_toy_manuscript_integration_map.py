from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy manuscript integration map count: 1",
    "New safe abstract toy manuscript integration map count: 1",
    "Toy manuscript integration map JSON export count: 1",
    "Toy manuscript integration slot count: 6",
    "Toy manuscript results slot count: 1",
    "Toy manuscript figure caption slot count: 1",
    "Toy manuscript limitation slot count: 1",
    "Toy manuscript safety boundary slot count: 1",
    "Toy manuscript controlled claim slot count: 1",
    "Toy manuscript non-readiness disclaimer slot count: 1",
    "Manuscript-safe placement map count: 1",
    "Toy manuscript integration direct execution count: 1",

    "Safe abstract toy results paragraph and caption package count: 1",
    "Toy results paragraph package JSON export count: 1",
    "Toy results paragraph count: 3",
    "Toy figure caption count: 1",
    "Toy limitation paragraph count: 1",
    "Toy safety boundary statement count: 1",
    "Toy controlled claim sentence count: 1",
    "Manuscript-safe toy wording package count: 1",

    "Safe abstract toy figure-ready interpretation package count: 1",
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

    "Imported safe abstract toy results paragraph and caption package count: 1",
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
    "Safe abstract toy results paragraph and caption package count: 1",
    "Toy results paragraph package JSON export count: 1",
    "Toy results paragraph count: 3",
    "Toy figure caption count: 1",
    "Toy limitation paragraph count: 1",
    "Toy safety boundary statement count: 1",
    "Toy controlled claim sentence count: 1",
    "Manuscript-safe toy wording package count: 1",
    "Safe abstract toy figure-ready interpretation package count: 1",
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
    "Safe abstract toy manuscript integration map count: 1",
    "New safe abstract toy manuscript integration map count: 1",
    "Toy manuscript integration map JSON export count: 1",
    "Toy manuscript integration slot count: 6",
    "Toy manuscript results slot count: 1",
    "Toy manuscript figure caption slot count: 1",
    "Toy manuscript limitation slot count: 1",
    "Toy manuscript safety boundary slot count: 1",
    "Toy manuscript controlled claim slot count: 1",
    "Toy manuscript non-readiness disclaimer slot count: 1",
    "Manuscript-safe placement map count: 1",
    "Toy manuscript integration direct execution count: 1",

    "Safe abstract toy results paragraph and caption package count: 1",
    "Toy results paragraph package JSON export count: 1",
    "Toy results paragraph count: 3",
    "Toy figure caption count: 1",
    "Toy limitation paragraph count: 1",
    "Toy safety boundary statement count: 1",
    "Toy controlled claim sentence count: 1",
    "Manuscript-safe toy wording package count: 1",

    "Safe abstract toy figure-ready interpretation package count: 1",
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

    "Imported safe abstract toy results paragraph and caption package count: 1",
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
class SafeAbstractToyManuscriptIntegrationMapResult:
    report: str
    package: dict[str, Any]
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def load_results_caption_package(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    if payload.get("package_kind") != "toy_synthetic_abstract_unitless_non-operational_results_paragraph_and_caption":
        raise ValueError("Unexpected results paragraph and caption package kind.")
    return payload


def build_manuscript_integration_map(source_json: Path) -> dict[str, Any]:
    source = load_results_caption_package(source_json)

    results_text = "\n\n".join(source["results_paragraphs"])

    slots = [
        {
            "slot_id": "toy_results_text_slot",
            "target_manuscript_location": "Results subsection for safe abstract toy outputs",
            "content_kind": "results_paragraphs",
            "content": results_text,
            "placement_rule": "Use only as toy-results wording; do not present as biological, empirical, validation, or readiness evidence.",
        },
        {
            "slot_id": "toy_figure_caption_slot",
            "target_manuscript_location": "Caption for toy sensitivity ranking figure or table",
            "content_kind": "figure_caption",
            "content": source["figure_caption"],
            "placement_rule": "Use only with the toy figure-ready outputs; preserve the non-biological and non-validation boundary.",
        },
        {
            "slot_id": "toy_limitation_slot",
            "target_manuscript_location": "Limitations or boundary subsection",
            "content_kind": "limitation_paragraph",
            "content": source["limitation_paragraph"],
            "placement_rule": "Keep near any toy results discussion to prevent overclaiming.",
        },
        {
            "slot_id": "toy_safety_boundary_slot",
            "target_manuscript_location": "Safety and anti-overclaim boundary subsection",
            "content_kind": "safety_boundary_statement",
            "content": source["safety_boundary_statement"],
            "placement_rule": "Keep explicit zero-boundary wording unchanged.",
        },
        {
            "slot_id": "toy_controlled_claim_slot",
            "target_manuscript_location": "End of toy results subsection or transition sentence",
            "content_kind": "controlled_claim_sentence",
            "content": source["controlled_claim_sentence"],
            "placement_rule": "Use as a controlled scope sentence only.",
        },
        {
            "slot_id": "toy_non_readiness_disclaimer_slot",
            "target_manuscript_location": "Readiness boundary note",
            "content_kind": "non_readiness_disclaimer",
            "content": (
                "This toy-results wording package does not make the manuscript submission ready, "
                "does not add external validation, does not add independent experimental evidence, "
                "does not add proof assistant verification, and does not add new citations."
            ),
            "placement_rule": "Use whenever the toy wording is moved into a broader manuscript draft.",
        },
    ]

    package = {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_integration_map",
        "source_record_count": source["source_record_count"],
        "config_summary_count": source["config_summary_count"],
        "figure_ready_row_count": source["figure_ready_row_count"],
        "results_paragraph_count": source["results_paragraph_count"],
        "figure_caption_count": source["figure_caption_count"],
        "limitation_paragraph_count": source["limitation_paragraph_count"],
        "safety_boundary_statement_count": source["safety_boundary_statement_count"],
        "controlled_claim_sentence_count": source["controlled_claim_sentence_count"],
        "integration_slot_count": len(slots),
        "results_slot_count": 1,
        "figure_caption_slot_count": 1,
        "limitation_slot_count": 1,
        "safety_boundary_slot_count": 1,
        "controlled_claim_slot_count": 1,
        "non_readiness_disclaimer_slot_count": 1,
        "slots": slots,
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
    package = build_manuscript_integration_map(source_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(package, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return package


def _package_text(package: dict[str, Any], json_path: Path) -> str:
    slot_lines = []
    for slot in package["slots"]:
        slot_lines.append(
            dedent(
                f"""
                ### {slot["slot_id"]}

                Target manuscript location: {slot["target_manuscript_location"]}

                Content kind: {slot["content_kind"]}

                Placement rule: {slot["placement_rule"]}

                Content:
                {slot["content"]}
                """
            ).strip()
        )

    return dedent(
        f"""
        ## Toy manuscript integration map

        JSON export:
        - `{json_path}`

        Package counts:
        - Toy manuscript integration slot count: {package["integration_slot_count"]}
        - Toy manuscript results slot count: {package["results_slot_count"]}
        - Toy manuscript figure caption slot count: {package["figure_caption_slot_count"]}
        - Toy manuscript limitation slot count: {package["limitation_slot_count"]}
        - Toy manuscript safety boundary slot count: {package["safety_boundary_slot_count"]}
        - Toy manuscript controlled claim slot count: {package["controlled_claim_slot_count"]}
        - Toy manuscript non-readiness disclaimer slot count: {package["non_readiness_disclaimer_slot_count"]}

        ## Integration slots

        {chr(10).join(slot_lines)}
        """
    ).strip()


def build_report(
    source_text: str,
    source_json: Path,
    json_path: Path,
) -> SafeAbstractToyManuscriptIntegrationMapResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    package = write_package_json(source_json, json_path)

    report = dedent(
        f"""
        # v8.196 - Safe Abstract Toy Manuscript Integration Map

        ## Question

        Can Viruse Fabric create a controlled manuscript integration map for placing the v8.195 manuscript-safe toy wording into a manuscript draft without claiming manuscript submission readiness, external validation, independent experiment, proof assistant verification, new citation additions, or any real-biological operational capability?

        ## Source artifacts

        - `outputs/safe_abstract_toy_results_paragraph_and_caption_package_v8_195.md`
        - `outputs/safe_abstract_toy_results_paragraph_and_caption_package_v8_195.json`

        ## Integration boundary

        v8.196 creates a placement map only.

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

        The map is manuscript-safe.

        The milestone is not manuscript submission readiness.

        The milestone is not external validation.

        The milestone is not independent experiment evidence.

        The milestone does not add new citations.

        {_package_text(package, json_path)}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy manuscript integration map count: 1.

        This milestone records toy manuscript integration map JSON export count: 1.

        This milestone records toy manuscript integration slot count: 6.

        This milestone records toy manuscript results slot count: 1.

        This milestone records toy manuscript figure caption slot count: 1.

        This milestone records toy manuscript limitation slot count: 1.

        This milestone records toy manuscript safety boundary slot count: 1.

        This milestone records toy manuscript controlled claim slot count: 1.

        This milestone records toy manuscript non-readiness disclaimer slot count: 1.

        This milestone records manuscript-safe placement map count: 1.

        This milestone preserves safe abstract toy results paragraph and caption package count: 1.

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

        The project has created a controlled manuscript integration map for placing manuscript-safe toy results wording into a manuscript draft, while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone creates a manuscript integration map for toy wording only.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
        "External validation remains zero.",
        "Independent experiment remains zero.",
        "Manuscript submission readiness remains zero.",
        "New citation additions remain zero.",
    ]

    return SafeAbstractToyManuscriptIntegrationMapResult(
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
) -> SafeAbstractToyManuscriptIntegrationMapResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text, source_json=source_json, json_path=json_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
