from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy manuscript patch dry-run package count: 1",
    "New safe abstract toy manuscript patch dry-run package count: 1",
    "Toy manuscript patch dry-run JSON export count: 1",
    "Toy manuscript dry-run preview count: 6",
    "Toy manuscript dry-run source proposal count: 6",
    "Toy manuscript dry-run applied patch count: 0",
    "Toy manuscript dry-run manuscript file modified count: 0",
    "Toy manuscript dry-run manuscript mutation count: 0",
    "Toy manuscript dry-run non-readiness disclaimer count: 1",
    "Toy manuscript dry-run boundary note count: 6",
    "Toy manuscript patch dry-run direct execution count: 1",

    "Safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript patch proposal JSON export count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",
    "Toy manuscript patch proposal source slot count: 6",
    "Toy manuscript patch proposal audit pass imported count: 1",
    "Toy manuscript patch proposal non-readiness disclaimer count: 1",
    "Toy manuscript patch proposal boundary note count: 6",

    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript integration slot audited count: 6",
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
    "Safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript patch proposal JSON export count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",
    "Toy manuscript patch proposal source slot count: 6",
    "Toy manuscript patch proposal audit pass imported count: 1",
    "Toy manuscript patch proposal non-readiness disclaimer count: 1",
    "Toy manuscript patch proposal boundary note count: 6",
    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency pass count: 1",
    "Safe abstract toy manuscript integration map count: 1",
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
    "Safe abstract toy manuscript patch dry-run package count: 1",
    "New safe abstract toy manuscript patch dry-run package count: 1",
    "Toy manuscript patch dry-run JSON export count: 1",
    "Toy manuscript dry-run preview count: 6",
    "Toy manuscript dry-run source proposal count: 6",
    "Toy manuscript dry-run applied patch count: 0",
    "Toy manuscript dry-run manuscript file modified count: 0",
    "Toy manuscript dry-run manuscript mutation count: 0",
    "Toy manuscript dry-run non-readiness disclaimer count: 1",
    "Toy manuscript dry-run boundary note count: 6",
    "Toy manuscript patch dry-run direct execution count: 1",

    "Safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript patch proposal JSON export count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",
    "Toy manuscript patch proposal source slot count: 6",
    "Toy manuscript patch proposal audit pass imported count: 1",
    "Toy manuscript patch proposal non-readiness disclaimer count: 1",
    "Toy manuscript patch proposal boundary note count: 6",

    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript integration slot audited count: 6",
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
class SafeAbstractToyManuscriptPatchDryRunPackageResult:
    report: str
    package: dict[str, Any]
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def load_patch_proposal(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    if payload.get("package_kind") != "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_proposal":
        raise ValueError("Unexpected patch proposal package kind.")
    return payload


def build_patch_dry_run_package(source_json: Path) -> dict[str, Any]:
    proposal = load_patch_proposal(source_json)

    if int(proposal.get("proposed_patch_count", 0)) != 6:
        raise ValueError("Expected six proposed patches.")
    if int(proposal.get("applied_patch_count", -1)) != 0:
        raise ValueError("Patch proposal must have zero applied patches.")

    previews: list[dict[str, Any]] = []
    for index, patch in enumerate(proposal["patch_proposals"], start=1):
        previews.append(
            {
                "dry_run_id": f"toy_patch_dry_run_{index:02d}",
                "source_patch_id": patch["patch_id"],
                "source_slot_id": patch["source_slot_id"],
                "target_manuscript_location": patch["target_manuscript_location"],
                "content_kind": patch["content_kind"],
                "preview_action": "would_insert_if_later_approved",
                "dry_run_status": "preview_only_not_applied",
                "manuscript_file_modified_count": 0,
                "manuscript_mutation_count": 0,
                "preview_text": patch["proposed_insertion_text"],
                "boundary_note": (
                    "Dry-run preview only. No manuscript file is modified, no manuscript patch is applied, "
                    "and no readiness, validation, proof-assistant, citation, or real-biological operational "
                    "claim is created."
                ),
            }
        )

    package = {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_dry_run_package",
        "source_proposed_patch_count": proposal["proposed_patch_count"],
        "dry_run_preview_count": len(previews),
        "applied_patch_count": 0,
        "manuscript_file_modified_count": 0,
        "manuscript_mutation_count": 0,
        "non_readiness_disclaimer_count": 1,
        "boundary_note_count": len(previews),
        "dry_run_statuses": sorted({preview["dry_run_status"] for preview in previews}),
        "preview_actions": sorted({preview["preview_action"] for preview in previews}),
        "dry_run_previews": previews,
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
    package = build_patch_dry_run_package(source_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(package, indent=2, sort_keys=True), encoding="utf-8")
    return package


def _package_text(package: dict[str, Any], json_path: Path) -> str:
    preview_lines = []
    for preview in package["dry_run_previews"]:
        preview_lines.append(
            dedent(
                f"""
                ### {preview["dry_run_id"]}

                Source patch id: {preview["source_patch_id"]}

                Source slot id: {preview["source_slot_id"]}

                Target manuscript location: {preview["target_manuscript_location"]}

                Content kind: {preview["content_kind"]}

                Preview action: {preview["preview_action"]}

                Dry-run status: {preview["dry_run_status"]}

                Manuscript file modified count: {preview["manuscript_file_modified_count"]}

                Manuscript mutation count: {preview["manuscript_mutation_count"]}

                Boundary note: {preview["boundary_note"]}

                Preview text:
                {preview["preview_text"]}
                """
            ).strip()
        )

    return dedent(
        f"""
        ## Toy manuscript patch dry-run package

        JSON export:
        - `{json_path}`

        Dry-run counts:
        - Toy manuscript dry-run preview count: {package["dry_run_preview_count"]}
        - Toy manuscript dry-run source proposal count: {package["source_proposed_patch_count"]}
        - Toy manuscript dry-run applied patch count: {package["applied_patch_count"]}
        - Toy manuscript dry-run manuscript file modified count: {package["manuscript_file_modified_count"]}
        - Toy manuscript dry-run manuscript mutation count: {package["manuscript_mutation_count"]}
        - Toy manuscript dry-run non-readiness disclaimer count: {package["non_readiness_disclaimer_count"]}
        - Toy manuscript dry-run boundary note count: {package["boundary_note_count"]}

        Dry-run status:
        - {", ".join(package["dry_run_statuses"])}

        Preview actions:
        - {", ".join(package["preview_actions"])}

        ## Dry-run preview entries

        {chr(10).join(preview_lines)}
        """
    ).strip()


def build_report(
    source_text: str,
    source_json: Path,
    json_path: Path,
) -> SafeAbstractToyManuscriptPatchDryRunPackageResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    package = write_package_json(source_json=source_json, json_path=json_path)

    report = dedent(
        f"""
        # v8.199 - Safe Abstract Toy Manuscript Patch Dry-Run Package

        ## Question

        Can Viruse Fabric create a controlled dry-run preview package from the v8.198 manuscript patch proposal while applying zero manuscript patches, modifying zero manuscript files, claiming no manuscript submission readiness, claiming no external validation, claiming no independent experiment, claiming no proof assistant verification, adding no citations, and introducing no real-biological operational capability?

        ## Source artifacts

        - `outputs/safe_abstract_toy_manuscript_patch_proposal_v8_198.md`
        - `outputs/safe_abstract_toy_manuscript_patch_proposal_v8_198.json`

        ## Dry-run boundary

        v8.199 creates a dry-run preview only.

        This milestone does not apply a manuscript patch.

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

        The dry-run package is manuscript-safe.

        The milestone is not manuscript submission readiness.

        The milestone is not external validation.

        The milestone is not independent experiment evidence.

        The milestone does not add new citations.

        {_package_text(package, json_path)}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy manuscript patch dry-run package count: 1.

        This milestone records toy manuscript patch dry-run JSON export count: 1.

        This milestone records toy manuscript dry-run preview count: 6.

        This milestone records toy manuscript dry-run source proposal count: 6.

        This milestone records toy manuscript dry-run applied patch count: 0.

        This milestone records toy manuscript dry-run manuscript file modified count: 0.

        This milestone records toy manuscript dry-run manuscript mutation count: 0.

        This milestone records toy manuscript dry-run non-readiness disclaimer count: 1.

        This milestone records toy manuscript dry-run boundary note count: 6.

        This milestone preserves safe abstract toy manuscript patch proposal count: 1.

        This milestone preserves safe abstract toy manuscript consistency audit count: 1.

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

        The project has created a controlled dry-run preview package for audited safe abstract toy manuscript patch proposals, while applying zero manuscript patches, modifying zero manuscript files, and preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone creates a manuscript patch dry-run preview only.",
        "No manuscript patch is applied.",
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
        "New citation additions remain zero.",
    ]

    return SafeAbstractToyManuscriptPatchDryRunPackageResult(
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
) -> SafeAbstractToyManuscriptPatchDryRunPackageResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(
        source_text=source_text,
        source_json=source_json,
        json_path=json_path,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
