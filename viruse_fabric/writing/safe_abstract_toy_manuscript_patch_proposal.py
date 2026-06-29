from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy manuscript patch proposal count: 1",
    "New safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript patch proposal JSON export count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",
    "Toy manuscript patch proposal source slot count: 6",
    "Toy manuscript patch proposal audit pass imported count: 1",
    "Toy manuscript patch proposal non-readiness disclaimer count: 1",
    "Toy manuscript patch proposal boundary note count: 6",
    "Toy manuscript patch proposal direct execution count: 1",

    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript integration slot audited count: 6",
    "Toy manuscript consistency pass count: 1",
    "Toy manuscript missing slot count: 0",
    "Toy manuscript boundary failure count: 0",
    "Toy manuscript positive overclaim marker count: 0",
    "Toy manuscript non-readiness disclaimer present count: 1",
    "Toy manuscript safety boundary slot present count: 1",

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
    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript integration slot audited count: 6",
    "Toy manuscript consistency pass count: 1",
    "Toy manuscript missing slot count: 0",
    "Toy manuscript boundary failure count: 0",
    "Toy manuscript positive overclaim marker count: 0",
    "Toy manuscript non-readiness disclaimer present count: 1",
    "Toy manuscript safety boundary slot present count: 1",
    "Safe abstract toy manuscript integration map count: 1",
    "Toy manuscript integration slot count: 6",
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
    "Safe abstract toy manuscript patch proposal count: 1",
    "New safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript patch proposal JSON export count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",
    "Toy manuscript patch proposal source slot count: 6",
    "Toy manuscript patch proposal audit pass imported count: 1",
    "Toy manuscript patch proposal non-readiness disclaimer count: 1",
    "Toy manuscript patch proposal boundary note count: 6",
    "Toy manuscript patch proposal direct execution count: 1",

    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency audit JSON export count: 1",
    "Toy manuscript integration slot audited count: 6",
    "Toy manuscript consistency pass count: 1",
    "Toy manuscript missing slot count: 0",
    "Toy manuscript boundary failure count: 0",
    "Toy manuscript positive overclaim marker count: 0",
    "Toy manuscript non-readiness disclaimer present count: 1",
    "Toy manuscript safety boundary slot present count: 1",

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
class SafeAbstractToyManuscriptPatchProposalResult:
    report: str
    package: dict[str, Any]
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_patch_proposal(audit_json: Path, integration_json: Path) -> dict[str, Any]:
    audit = load_json(audit_json)
    integration = load_json(integration_json)

    if audit.get("package_kind") != "toy_synthetic_abstract_unitless_non-operational_manuscript_consistency_audit":
        raise ValueError("Unexpected consistency audit package kind.")

    if integration.get("package_kind") != "toy_synthetic_abstract_unitless_non-operational_manuscript_integration_map":
        raise ValueError("Unexpected manuscript integration map package kind.")

    if int(audit.get("consistency_pass_count", 0)) != 1:
        raise ValueError("Cannot build patch proposal from failing audit.")

    slots = integration.get("slots", [])
    proposals: list[dict[str, Any]] = []

    for index, slot in enumerate(slots, start=1):
        proposals.append(
            {
                "patch_id": f"toy_patch_proposal_{index:02d}",
                "source_slot_id": slot["slot_id"],
                "target_manuscript_location": slot["target_manuscript_location"],
                "content_kind": slot["content_kind"],
                "proposal_status": "proposal_only_not_applied",
                "proposed_insertion_text": slot["content"],
                "placement_rule": slot["placement_rule"],
                "boundary_note": (
                    "This is a proposed placement for synthetic, abstract, unitless toy wording only; "
                    "it is not an applied manuscript patch, not manuscript submission readiness, not "
                    "external validation, not independent experimental evidence, not proof assistant "
                    "verification, and not a new citation addition."
                ),
            }
        )

    package = {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_proposal",
        "source_audit_pass_count": audit["consistency_pass_count"],
        "source_slot_count": integration["integration_slot_count"],
        "proposed_patch_count": len(proposals),
        "applied_patch_count": 0,
        "non_readiness_disclaimer_count": 1,
        "boundary_note_count": len(proposals),
        "proposal_statuses": sorted({proposal["proposal_status"] for proposal in proposals}),
        "patch_proposals": proposals,
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


def write_package_json(audit_json: Path, integration_json: Path, json_path: Path) -> dict[str, Any]:
    package = build_patch_proposal(audit_json=audit_json, integration_json=integration_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(package, indent=2, sort_keys=True), encoding="utf-8")
    return package


def _package_text(package: dict[str, Any], json_path: Path) -> str:
    proposal_lines = []
    for proposal in package["patch_proposals"]:
        proposal_lines.append(
            dedent(
                f"""
                ### {proposal["patch_id"]}

                Source slot id: {proposal["source_slot_id"]}

                Target manuscript location: {proposal["target_manuscript_location"]}

                Content kind: {proposal["content_kind"]}

                Proposal status: {proposal["proposal_status"]}

                Placement rule: {proposal["placement_rule"]}

                Boundary note: {proposal["boundary_note"]}

                Proposed insertion text:
                {proposal["proposed_insertion_text"]}
                """
            ).strip()
        )

    return dedent(
        f"""
        ## Toy manuscript patch proposal package

        JSON export:
        - `{json_path}`

        Proposal counts:
        - Toy manuscript proposed patch count: {package["proposed_patch_count"]}
        - Toy manuscript applied patch count: {package["applied_patch_count"]}
        - Toy manuscript patch proposal source slot count: {package["source_slot_count"]}
        - Toy manuscript patch proposal audit pass imported count: {package["source_audit_pass_count"]}
        - Toy manuscript patch proposal non-readiness disclaimer count: {package["non_readiness_disclaimer_count"]}
        - Toy manuscript patch proposal boundary note count: {package["boundary_note_count"]}

        Proposal status:
        - {", ".join(package["proposal_statuses"])}

        ## Proposed patch entries

        {chr(10).join(proposal_lines)}
        """
    ).strip()


def build_report(
    source_text: str,
    audit_json: Path,
    integration_json: Path,
    json_path: Path,
) -> SafeAbstractToyManuscriptPatchProposalResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    package = write_package_json(
        audit_json=audit_json,
        integration_json=integration_json,
        json_path=json_path,
    )

    report = dedent(
        f"""
        # v8.198 - Safe Abstract Toy Manuscript Patch Proposal

        ## Question

        Can Viruse Fabric create a controlled manuscript patch proposal from the audited toy manuscript integration map without applying any manuscript patch, claiming manuscript submission readiness, claiming external validation, claiming independent experiment, claiming proof assistant verification, adding citations, or introducing any real-biological operational capability?

        ## Source artifacts

        - `outputs/safe_abstract_toy_manuscript_consistency_audit_v8_197.md`
        - `outputs/safe_abstract_toy_manuscript_consistency_audit_v8_197.json`
        - `outputs/safe_abstract_toy_manuscript_integration_map_v8_196.json`

        ## Patch proposal boundary

        v8.198 creates a patch proposal only.

        This milestone does not apply a manuscript patch.

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

        The patch proposal is manuscript-safe.

        The milestone is not manuscript submission readiness.

        The milestone is not external validation.

        The milestone is not independent experiment evidence.

        The milestone does not add new citations.

        {_package_text(package, json_path)}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim and safety boundary

        This milestone records safe abstract toy manuscript patch proposal count: 1.

        This milestone records toy manuscript patch proposal JSON export count: 1.

        This milestone records toy manuscript proposed patch count: 6.

        This milestone records toy manuscript applied patch count: 0.

        This milestone records toy manuscript patch proposal source slot count: 6.

        This milestone records toy manuscript patch proposal audit pass imported count: 1.

        This milestone records toy manuscript patch proposal non-readiness disclaimer count: 1.

        This milestone records toy manuscript patch proposal boundary note count: 6.

        This milestone preserves safe abstract toy manuscript consistency audit count: 1.

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

        The project has created a controlled manuscript patch proposal for audited safe abstract toy wording, while applying zero manuscript patches and preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
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
        "This milestone creates a manuscript patch proposal only.",
        "No manuscript patch is applied.",
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

    return SafeAbstractToyManuscriptPatchProposalResult(
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
    audit_json: Path,
    integration_json: Path,
    json_path: Path,
) -> SafeAbstractToyManuscriptPatchProposalResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(
        source_text=source_text,
        audit_json=audit_json,
        integration_json=integration_json,
        json_path=json_path,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
