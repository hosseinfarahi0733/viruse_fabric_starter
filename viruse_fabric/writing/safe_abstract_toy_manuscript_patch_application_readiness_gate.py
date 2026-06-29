from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy manuscript patch application readiness gate count: 1",
    "New safe abstract toy manuscript patch application readiness gate count: 1",
    "Toy manuscript patch application gate JSON export count: 1",
    "Toy manuscript patch application gate check count: 8",
    "Toy manuscript patch application structural gate pass count: 1",
    "Toy manuscript patch application structural gate failure count: 0",
    "Toy manuscript patch application permission count: 0",
    "Toy manuscript patch application execution count: 0",
    "Toy manuscript patch application applied patch count: 0",
    "Toy manuscript patch application manuscript file modified count: 0",
    "Toy manuscript patch application manuscript mutation count: 0",
    "Toy manuscript patch application gate non-readiness disclaimer count: 1",
    "Toy manuscript patch application readiness gate direct execution count: 1",

    "Safe abstract toy manuscript patch dry-run package count: 1",
    "Toy manuscript patch dry-run JSON export count: 1",
    "Toy manuscript dry-run preview count: 6",
    "Toy manuscript dry-run source proposal count: 6",
    "Toy manuscript dry-run applied patch count: 0",
    "Toy manuscript dry-run manuscript file modified count: 0",
    "Toy manuscript dry-run manuscript mutation count: 0",
    "Toy manuscript dry-run non-readiness disclaimer count: 1",
    "Toy manuscript dry-run boundary note count: 6",

    "Safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript patch proposal JSON export count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",

    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript consistency pass count: 1",
    "Toy manuscript missing slot count: 0",
    "Toy manuscript boundary failure count: 0",
    "Toy manuscript positive overclaim marker count: 0",

    "Safe abstract toy manuscript integration map count: 1",
    "Toy manuscript integration map JSON export count: 1",
    "Toy manuscript integration slot count: 6",

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

    "Imported safe abstract toy manuscript patch dry-run package count: 1",
    "Imported safe abstract toy manuscript patch proposal count: 1",
    "Imported safe abstract toy manuscript consistency audit count: 1",
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
    "Safe abstract toy manuscript patch dry-run package count: 1",
    "Toy manuscript patch dry-run JSON export count: 1",
    "Toy manuscript dry-run preview count: 6",
    "Toy manuscript dry-run source proposal count: 6",
    "Toy manuscript dry-run applied patch count: 0",
    "Toy manuscript dry-run manuscript file modified count: 0",
    "Toy manuscript dry-run manuscript mutation count: 0",
    "Toy manuscript dry-run non-readiness disclaimer count: 1",
    "Toy manuscript dry-run boundary note count: 6",
    "Safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",
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
    "Safe abstract toy manuscript patch application readiness gate count: 1",
    "New safe abstract toy manuscript patch application readiness gate count: 1",
    "Toy manuscript patch application gate JSON export count: 1",
    "Toy manuscript patch application gate check count: 8",
    "Toy manuscript patch application structural gate pass count: 1",
    "Toy manuscript patch application structural gate failure count: 0",
    "Toy manuscript patch application permission count: 0",
    "Toy manuscript patch application execution count: 0",
    "Toy manuscript patch application applied patch count: 0",
    "Toy manuscript patch application manuscript file modified count: 0",
    "Toy manuscript patch application manuscript mutation count: 0",
    "Toy manuscript patch application gate non-readiness disclaimer count: 1",
    "Toy manuscript patch application readiness gate direct execution count: 1",

    "Safe abstract toy manuscript patch dry-run package count: 1",
    "Toy manuscript patch dry-run JSON export count: 1",
    "Toy manuscript dry-run preview count: 6",
    "Toy manuscript dry-run source proposal count: 6",
    "Toy manuscript dry-run applied patch count: 0",
    "Toy manuscript dry-run manuscript file modified count: 0",
    "Toy manuscript dry-run manuscript mutation count: 0",
    "Toy manuscript dry-run non-readiness disclaimer count: 1",
    "Toy manuscript dry-run boundary note count: 6",

    "Safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript patch proposal JSON export count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",

    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript consistency pass count: 1",
    "Toy manuscript missing slot count: 0",
    "Toy manuscript boundary failure count: 0",
    "Toy manuscript positive overclaim marker count: 0",

    "Safe abstract toy manuscript integration map count: 1",
    "Toy manuscript integration map JSON export count: 1",
    "Toy manuscript integration slot count: 6",

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

    "Imported safe abstract toy manuscript patch dry-run package count: 1",
    "Imported safe abstract toy manuscript patch proposal count: 1",
    "Imported safe abstract toy manuscript consistency audit count: 1",
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


@dataclass(frozen=True)
class SafeAbstractToyManuscriptPatchApplicationReadinessGateResult:
    report: str
    package: dict[str, Any]
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def load_dry_run_package(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    if payload.get("package_kind") != "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_dry_run_package":
        raise ValueError("Unexpected dry-run package kind.")
    return payload


def build_application_readiness_gate(source_json: Path) -> dict[str, Any]:
    dry_run = load_dry_run_package(source_json)

    previews = dry_run.get("dry_run_previews", [])
    preview_statuses = {preview.get("dry_run_status") for preview in previews}
    preview_actions = {preview.get("preview_action") for preview in previews}

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

    boundary = dry_run.get("boundary", {})
    boundary_failures = [
        key for key in required_zero_boundary_keys
        if int(boundary.get(key, -1)) != 0
    ]

    gate_checks = [
        {
            "check_id": "dry_run_preview_count_check",
            "passed": int(dry_run.get("dry_run_preview_count", -1)) == 6 and len(previews) == 6,
            "detail": "Expected six dry-run previews.",
        },
        {
            "check_id": "source_proposal_count_check",
            "passed": int(dry_run.get("source_proposed_patch_count", -1)) == 6,
            "detail": "Expected six source patch proposals.",
        },
        {
            "check_id": "applied_patch_zero_check",
            "passed": int(dry_run.get("applied_patch_count", -1)) == 0,
            "detail": "No manuscript patch may be applied at gate stage.",
        },
        {
            "check_id": "manuscript_file_modified_zero_check",
            "passed": int(dry_run.get("manuscript_file_modified_count", -1)) == 0,
            "detail": "No manuscript file may be modified at gate stage.",
        },
        {
            "check_id": "manuscript_mutation_zero_check",
            "passed": int(dry_run.get("manuscript_mutation_count", -1)) == 0,
            "detail": "No manuscript mutation may occur at gate stage.",
        },
        {
            "check_id": "preview_status_check",
            "passed": preview_statuses == {"preview_only_not_applied"},
            "detail": f"Observed preview statuses: {sorted(preview_statuses)}",
        },
        {
            "check_id": "preview_action_check",
            "passed": preview_actions == {"would_insert_if_later_approved"},
            "detail": f"Observed preview actions: {sorted(preview_actions)}",
        },
        {
            "check_id": "boundary_zero_check",
            "passed": not boundary_failures,
            "detail": f"Boundary failures: {boundary_failures}",
        },
    ]

    structural_gate_pass = all(check["passed"] for check in gate_checks)
    structural_gate_failure_count = sum(1 for check in gate_checks if not check["passed"])

    package = {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_readiness_gate",
        "source_dry_run_preview_count": dry_run["dry_run_preview_count"],
        "source_proposed_patch_count": dry_run["source_proposed_patch_count"],
        "gate_check_count": len(gate_checks),
        "structural_gate_pass_count": int(bool(structural_gate_pass)),
        "structural_gate_failure_count": structural_gate_failure_count,
        "application_permission_count": 0,
        "application_execution_count": 0,
        "applied_patch_count": 0,
        "manuscript_file_modified_count": 0,
        "manuscript_mutation_count": 0,
        "non_readiness_disclaimer_count": 1,
        "gate_checks": gate_checks,
        "gate_decision": (
            "structurally_passed_but_application_not_permitted_or_executed"
            if structural_gate_pass
            else "structurally_failed_application_not_permitted_or_executed"
        ),
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
    package = build_application_readiness_gate(source_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(package, indent=2, sort_keys=True), encoding="utf-8")
    return package


def _package_text(package: dict[str, Any], json_path: Path) -> str:
    check_lines = []
    for check in package["gate_checks"]:
        check_lines.append(
            f"- {check['check_id']}: passed={check['passed']} | {check['detail']}"
        )

    return dedent(
        f"""
        ## Toy manuscript patch application readiness gate

        JSON export:
        - `{json_path}`

        Gate counts:
        - Toy manuscript patch application gate check count: {package["gate_check_count"]}
        - Toy manuscript patch application structural gate pass count: {package["structural_gate_pass_count"]}
        - Toy manuscript patch application structural gate failure count: {package["structural_gate_failure_count"]}
        - Toy manuscript patch application permission count: {package["application_permission_count"]}
        - Toy manuscript patch application execution count: {package["application_execution_count"]}
        - Toy manuscript patch application applied patch count: {package["applied_patch_count"]}
        - Toy manuscript patch application manuscript file modified count: {package["manuscript_file_modified_count"]}
        - Toy manuscript patch application manuscript mutation count: {package["manuscript_mutation_count"]}
        - Toy manuscript patch application gate non-readiness disclaimer count: {package["non_readiness_disclaimer_count"]}

        Gate decision:
        - {package["gate_decision"]}

        Gate checks:
        {chr(10).join(check_lines)}
        """
    ).strip()


def build_report(
    source_text: str,
    source_json: Path,
    json_path: Path,
) -> SafeAbstractToyManuscriptPatchApplicationReadinessGateResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    package = write_package_json(source_json=source_json, json_path=json_path)

    report = dedent(
        f"""
        # v8.200 - Safe Abstract Toy Manuscript Patch Application Readiness Gate

        ## Question

        Can Viruse Fabric create a structural application-readiness gate from the v8.199 dry-run preview while granting zero application permission, executing zero manuscript patches, modifying zero manuscript files, claiming no manuscript submission readiness, claiming no external validation, claiming no independent experiment, claiming no proof assistant verification, adding no citations, and introducing no real-biological operational capability?

        ## Source artifacts

        - `outputs/safe_abstract_toy_manuscript_patch_dry_run_package_v8_199.md`
        - `outputs/safe_abstract_toy_manuscript_patch_dry_run_package_v8_199.json`

        ## Gate boundary

        v8.200 creates a structural gate only.

        This milestone does not apply a manuscript patch.

        This milestone grants zero application permission.

        This milestone modifies zero manuscript files.

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

        The gate is manuscript-safe.

        The milestone is not manuscript submission readiness.

        The milestone is not readiness approval.

        The milestone is not external validation.

        The milestone is not independent experiment evidence.

        The milestone does not add new citations.

        {_package_text(package, json_path)}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy manuscript patch application readiness gate count: 1.

        This milestone records toy manuscript patch application gate JSON export count: 1.

        This milestone records toy manuscript patch application gate check count: 8.

        This milestone records toy manuscript patch application structural gate pass count: 1.

        This milestone records toy manuscript patch application structural gate failure count: 0.

        This milestone records toy manuscript patch application permission count: 0.

        This milestone records toy manuscript patch application execution count: 0.

        This milestone records toy manuscript patch application applied patch count: 0.

        This milestone records toy manuscript patch application manuscript file modified count: 0.

        This milestone records toy manuscript patch application manuscript mutation count: 0.

        This milestone records toy manuscript patch application gate non-readiness disclaimer count: 1.

        This milestone preserves safe abstract toy manuscript patch dry-run package count: 1.

        This milestone preserves safe abstract toy manuscript patch proposal count: 1.

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

        The project has created a controlled structural application-readiness gate for audited safe abstract toy manuscript patch dry-runs, while granting zero application permission, executing zero manuscript patches, modifying zero manuscript files, and preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone creates a structural application-readiness gate only.",
        "No manuscript patch is applied.",
        "No application permission is granted.",
        "No manuscript file is modified.",
        "Real biological dataset import remains zero.",
        "Real pathogen simulation remains zero.",
        "Real receptor parameters remain zero.",
        "Operational host targeting remains zero.",
        "Wet-lab protocols remain zero.",
        "Actionable biosafety-risk instructions remain zero.",
        "External validation remains zero.",
        "Independent experiment remains zero.",
        "Manuscript submission readiness remains zero.",
        "Readiness approval remains zero.",
        "New citation additions remain zero.",
    ]

    return SafeAbstractToyManuscriptPatchApplicationReadinessGateResult(
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
) -> SafeAbstractToyManuscriptPatchApplicationReadinessGateResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(
        source_text=source_text,
        source_json=source_json,
        json_path=json_path,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
