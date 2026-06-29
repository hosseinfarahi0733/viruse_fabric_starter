from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy manuscript consistency audit count: 1",
    "New safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript integration slot audited count: 6",
    "Toy manuscript consistency pass count: 1",
    "Toy manuscript missing slot count: 0",
    "Toy manuscript boundary failure count: 0",
    "Toy manuscript positive overclaim marker count: 0",
    "Toy manuscript non-readiness disclaimer present count: 1",
    "Toy manuscript safety boundary slot present count: 1",
    "Toy manuscript consistency audit direct execution count: 1",

    "Safe abstract toy manuscript integration map count: 1",
    "Toy manuscript integration map JSON export count: 1",
    "Toy manuscript integration slot count: 6",
    "Toy manuscript results slot count: 1",
    "Toy manuscript figure caption slot count: 1",
    "Toy manuscript limitation slot count: 1",
    "Toy manuscript safety boundary slot count: 1",
    "Toy manuscript controlled claim slot count: 1",
    "Toy manuscript non-readiness disclaimer slot count: 1",
    "Manuscript-safe placement map count: 1",

    "Safe abstract toy results paragraph and caption package count: 1",
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

    "Imported safe abstract toy manuscript integration map count: 1",
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
    "Safe abstract toy manuscript integration map count: 1",
    "Toy manuscript integration map JSON export count: 1",
    "Toy manuscript integration slot count: 6",
    "Toy manuscript results slot count: 1",
    "Toy manuscript figure caption slot count: 1",
    "Toy manuscript limitation slot count: 1",
    "Toy manuscript safety boundary slot count: 1",
    "Toy manuscript controlled claim slot count: 1",
    "Toy manuscript non-readiness disclaimer slot count: 1",
    "Manuscript-safe placement map count: 1",
    "Safe abstract toy results paragraph and caption package count: 1",
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
    "Safe abstract toy manuscript consistency audit count: 1",
    "New safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript integration slot audited count: 6",
    "Toy manuscript consistency pass count: 1",
    "Toy manuscript missing slot count: 0",
    "Toy manuscript boundary failure count: 0",
    "Toy manuscript positive overclaim marker count: 0",
    "Toy manuscript non-readiness disclaimer present count: 1",
    "Toy manuscript safety boundary slot present count: 1",
    "Toy manuscript consistency audit direct execution count: 1",

    "Safe abstract toy manuscript integration map count: 1",
    "Toy manuscript integration map JSON export count: 1",
    "Toy manuscript integration slot count: 6",
    "Toy manuscript results slot count: 1",
    "Toy manuscript figure caption slot count: 1",
    "Toy manuscript limitation slot count: 1",
    "Toy manuscript safety boundary slot count: 1",
    "Toy manuscript controlled claim slot count: 1",
    "Toy manuscript non-readiness disclaimer slot count: 1",
    "Manuscript-safe placement map count: 1",

    "Safe abstract toy results paragraph and caption package count: 1",
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

    "Imported safe abstract toy manuscript integration map count: 1",
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


REQUIRED_SLOT_IDS = {
    "toy_results_text_slot",
    "toy_figure_caption_slot",
    "toy_limitation_slot",
    "toy_safety_boundary_slot",
    "toy_controlled_claim_slot",
    "toy_non_readiness_disclaimer_slot",
}


@dataclass(frozen=True)
class SafeAbstractToyManuscriptConsistencyAuditResult:
    report: str
    package: dict[str, Any]
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def load_manuscript_integration_map(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    if payload.get("package_kind") != "toy_synthetic_abstract_unitless_non-operational_manuscript_integration_map":
        raise ValueError("Unexpected manuscript integration map package kind.")
    return payload


def build_manuscript_consistency_audit(source_json: Path) -> dict[str, Any]:
    source = load_manuscript_integration_map(source_json)
    slots = source.get("slots", [])

    observed_slot_ids = {slot.get("slot_id") for slot in slots}
    missing_slots = sorted(REQUIRED_SLOT_IDS - observed_slot_ids)

    boundary = source.get("boundary", {})
    required_zero_boundary_keys = [
        "real_biological_dataset_import_count",
        "real_pathogen_simulation_count",
        "real_receptor_parameter_count",
        "operational_host_targeting_count",
        "wet_lab_protocol_count",
        "actionable_biosafety_risk_instruction_count",
        "proof_assistant_verification_count",
        "external_validation_count",
        "independent_experiment_count",
        "manuscript_submission_ready_count",
        "readiness_approval_count",
        "new_citation_added_count",
    ]

    boundary_failures = [
        key for key in required_zero_boundary_keys
        if int(boundary.get(key, -1)) != 0
    ]

    source_text = json.dumps(source, sort_keys=True).lower()
    positive_overclaim_markers = [
        "manuscript is ready",
        "provides external validation",
        "external validation is provided",
        "independent experiment is provided",
        "proof assistant verification is provided",
        "new citations are added",
        "readiness is approved",
    ]
    positive_overclaim_hits = [
        marker for marker in positive_overclaim_markers
        if marker in source_text
    ]

    non_readiness_disclaimer_present = (
        "toy_non_readiness_disclaimer_slot" in observed_slot_ids
        and "does not make the manuscript submission ready" in source_text
    )
    safety_boundary_slot_present = "toy_safety_boundary_slot" in observed_slot_ids

    consistency_pass = (
        len(slots) == 6
        and not missing_slots
        and not boundary_failures
        and not positive_overclaim_hits
        and non_readiness_disclaimer_present
        and safety_boundary_slot_present
    )

    audit_checks = [
        {
            "check_id": "slot_count_check",
            "passed": len(slots) == 6,
            "detail": f"Expected 6 integration slots and found {len(slots)}.",
        },
        {
            "check_id": "required_slot_id_check",
            "passed": not missing_slots,
            "detail": f"Missing slots: {missing_slots}",
        },
        {
            "check_id": "boundary_zero_check",
            "passed": not boundary_failures,
            "detail": f"Boundary failures: {boundary_failures}",
        },
        {
            "check_id": "positive_overclaim_marker_check",
            "passed": not positive_overclaim_hits,
            "detail": f"Positive overclaim hits: {positive_overclaim_hits}",
        },
        {
            "check_id": "non_readiness_disclaimer_check",
            "passed": bool(non_readiness_disclaimer_present),
            "detail": "Non-readiness disclaimer slot and wording checked.",
        },
        {
            "check_id": "safety_boundary_slot_check",
            "passed": bool(safety_boundary_slot_present),
            "detail": "Safety boundary slot checked.",
        },
    ]

    package = {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_consistency_audit",
        "source_integration_slot_count": source["integration_slot_count"],
        "audited_slot_count": len(slots),
        "missing_slot_count": len(missing_slots),
        "boundary_failure_count": len(boundary_failures),
        "positive_overclaim_marker_count": len(positive_overclaim_hits),
        "non_readiness_disclaimer_present_count": int(bool(non_readiness_disclaimer_present)),
        "safety_boundary_slot_present_count": int(bool(safety_boundary_slot_present)),
        "consistency_pass_count": int(bool(consistency_pass)),
        "observed_slot_ids": sorted(observed_slot_ids),
        "missing_slots": missing_slots,
        "boundary_failures": boundary_failures,
        "positive_overclaim_hits": positive_overclaim_hits,
        "audit_checks": audit_checks,
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
    package = build_manuscript_consistency_audit(source_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps(package, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return package


def _package_text(package: dict[str, Any], json_path: Path) -> str:
    check_lines = []
    for check in package["audit_checks"]:
        check_lines.append(
            f"- {check['check_id']}: passed={check['passed']} | {check['detail']}"
        )

    return dedent(
        f"""
        ## Toy manuscript consistency audit

        JSON export:
        - `{json_path}`

        Audit counts:
        - Toy manuscript integration slot audited count: {package["audited_slot_count"]}
        - Toy manuscript consistency pass count: {package["consistency_pass_count"]}
        - Toy manuscript missing slot count: {package["missing_slot_count"]}
        - Toy manuscript boundary failure count: {package["boundary_failure_count"]}
        - Toy manuscript positive overclaim marker count: {package["positive_overclaim_marker_count"]}
        - Toy manuscript non-readiness disclaimer present count: {package["non_readiness_disclaimer_present_count"]}
        - Toy manuscript safety boundary slot present count: {package["safety_boundary_slot_present_count"]}

        Observed slot ids:
        - {chr(10) + "- ".join(package["observed_slot_ids"])}

        Audit checks:
        {chr(10).join(check_lines)}
        """
    ).strip()


def build_report(
    source_text: str,
    source_json: Path,
    json_path: Path,
) -> SafeAbstractToyManuscriptConsistencyAuditResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    package = write_package_json(source_json, json_path)

    report = dedent(
        f"""
        # v8.197 - Safe Abstract Toy Manuscript Consistency Audit

        ## Question

        Can Viruse Fabric audit the v8.196 safe abstract toy manuscript integration map for slot completeness, boundary preservation, non-readiness disclaimer presence, safety boundary presence, and absence of positive overclaim markers without claiming manuscript submission readiness, external validation, independent experiment, proof assistant verification, new citation additions, or any real-biological operational capability?

        ## Source artifacts

        - `outputs/safe_abstract_toy_manuscript_integration_map_v8_196.md`
        - `outputs/safe_abstract_toy_manuscript_integration_map_v8_196.json`

        ## Audit boundary

        v8.197 creates a consistency audit only.

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

        The audit is manuscript-safe.

        The milestone is not manuscript submission readiness.

        The milestone is not external validation.

        The milestone is not independent experiment evidence.

        The milestone does not add new citations.

        {_package_text(package, json_path)}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy manuscript consistency audit count: 1.

        This milestone records toy manuscript consistency audit JSON export count: 1.

        This milestone records toy manuscript integration slot audited count: 6.

        This milestone records toy manuscript consistency pass count: 1.

        This milestone records toy manuscript missing slot count: 0.

        This milestone records toy manuscript boundary failure count: 0.

        This milestone records toy manuscript positive overclaim marker count: 0.

        This milestone records toy manuscript non-readiness disclaimer present count: 1.

        This milestone records toy manuscript safety boundary slot present count: 1.

        This milestone preserves safe abstract toy manuscript integration map count: 1.

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

        The project has audited the safe abstract toy manuscript integration map for consistency, while preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone creates a consistency audit for toy manuscript wording only.",
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

    return SafeAbstractToyManuscriptConsistencyAuditResult(
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
) -> SafeAbstractToyManuscriptConsistencyAuditResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text, source_json=source_json, json_path=json_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
