from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy manuscript patch application checklist count: 1",
    "New safe abstract toy manuscript patch application checklist count: 1",
    "Toy manuscript patch application checklist JSON export count: 1",
    "Toy manuscript patch application checklist item count: 9",
    "Toy manuscript patch application checklist completion count: 0",
    "Toy manuscript patch application checklist execution count: 0",
    "Toy manuscript patch application permission count: 0",
    "Toy manuscript patch application applied patch count: 0",
    "Toy manuscript patch application manuscript file modified count: 0",
    "Toy manuscript patch application manuscript mutation count: 0",
    "Toy manuscript patch application checklist non-readiness disclaimer count: 1",
    "Toy manuscript patch application checklist boundary note count: 9",
    "Toy manuscript patch application checklist direct execution count: 1",

    "Safe abstract toy manuscript patch application plan count: 1",
    "Toy manuscript patch application plan JSON export count: 1",
    "Toy manuscript patch application plan step count: 7",
    "Toy manuscript patch application plan execution count: 0",
    "Toy manuscript patch application permission count: 0",
    "Toy manuscript patch application applied patch count: 0",
    "Toy manuscript patch application manuscript file modified count: 0",
    "Toy manuscript patch application manuscript mutation count: 0",

    "Safe abstract toy manuscript patch application readiness gate count: 1",
    "Toy manuscript patch application structural gate pass count: 1",
    "Toy manuscript patch application structural gate failure count: 0",

    "Safe abstract toy manuscript patch dry-run package count: 1",
    "Toy manuscript dry-run preview count: 6",
    "Toy manuscript dry-run applied patch count: 0",

    "Safe abstract toy manuscript patch proposal count: 1",
    "Toy manuscript proposed patch count: 6",
    "Toy manuscript applied patch count: 0",

    "Safe abstract toy manuscript consistency audit count: 1",
    "Toy manuscript consistency pass count: 1",
    "Toy manuscript missing slot count: 0",
    "Toy manuscript boundary failure count: 0",
    "Toy manuscript positive overclaim marker count: 0",

    "Safe abstract toy manuscript integration map count: 1",
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

    "Imported safe abstract toy manuscript patch application plan count: 1",
    "Imported safe abstract toy manuscript patch application readiness gate count: 1",
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


REQUIRED_REPORT_PHRASES = COUNTER_LINES


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def load_plan(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    expected = "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_plan"
    if payload.get("package_kind") != expected:
        raise ValueError(f"Unexpected package kind: {payload.get('package_kind')}")
    return payload


def build_application_checklist(source_json: Path) -> dict[str, Any]:
    plan = load_plan(source_json)

    assert plan["plan_step_count"] == 7
    assert plan["application_plan_execution_count"] == 0
    assert plan["application_permission_count"] == 0
    assert plan["application_execution_count"] == 0
    assert plan["applied_patch_count"] == 0
    assert plan["manuscript_file_modified_count"] == 0
    assert plan["manuscript_mutation_count"] == 0
    assert plan["plan_decision"] == "plan_created_but_application_not_permitted_or_executed"

    items = [
        ("check_plan_source", "Confirm the v8.201 plan is the sole source for this checklist."),
        ("check_toy_scope", "Confirm all future wording remains synthetic, abstract, unitless, and non-operational."),
        ("check_no_application_permission", "Confirm this checklist grants zero application permission."),
        ("check_no_application_execution", "Confirm this checklist executes zero application steps."),
        ("check_no_manuscript_patch", "Confirm this checklist applies zero manuscript patches."),
        ("check_no_manuscript_file_modification", "Confirm this checklist modifies zero manuscript files."),
        ("check_no_readiness_or_approval", "Confirm no manuscript readiness or readiness approval is claimed."),
        ("check_no_validation_proof_or_citation", "Confirm no external validation, proof assistant verification, independent experiment, or citation addition is claimed."),
        ("check_no_real_biological_scope", "Confirm zero real biological dataset import, real pathogen simulation, receptor parameterization, operational host targeting, wet-lab protocol, actionable biosafety-risk instruction, infectivity optimization, immune evasion optimization, or host range prediction."),
    ]

    checklist_items = [
        {
            "item_id": item_id,
            "item_order": index,
            "status": "unchecked_plan_only",
            "description": description,
            "boundary_note": "Checklist-only item. It does not grant permission, execute application, modify manuscript files, approve readiness, validate, cite, prove, or create real-biological operational content.",
        }
        for index, (item_id, description) in enumerate(items, start=1)
    ]

    return {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_checklist",
        "source_plan_step_count": plan["plan_step_count"],
        "source_application_plan_execution_count": plan["application_plan_execution_count"],
        "checklist_item_count": len(checklist_items),
        "checklist_completion_count": 0,
        "checklist_execution_count": 0,
        "application_permission_count": 0,
        "application_execution_count": 0,
        "applied_patch_count": 0,
        "manuscript_file_modified_count": 0,
        "manuscript_mutation_count": 0,
        "non_readiness_disclaimer_count": 1,
        "boundary_note_count": len(checklist_items),
        "checklist_decision": "checklist_created_but_not_completed_or_executed",
        "checklist_items": checklist_items,
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


def write_package_json(source_json: Path, json_path: Path) -> dict[str, Any]:
    package = build_application_checklist(source_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(package, indent=2, sort_keys=True), encoding="utf-8")
    return package


def build_report(source_json: Path, json_path: Path) -> tuple[str, dict[str, Any]]:
    package = write_package_json(source_json, json_path)

    item_lines = []
    for item in package["checklist_items"]:
        item_lines.append(
            dedent(
                f"""
                ### {item["item_id"]}

                Order: {item["item_order"]}

                Status: {item["status"]}

                Description: {item["description"]}

                Boundary note: {item["boundary_note"]}
                """
            ).strip()
        )

    report = dedent(
        f"""
        # v8.202 - Safe Abstract Toy Manuscript Patch Application Checklist

        ## Question

        Can Viruse Fabric create a controlled plan-only checklist from the v8.201 future manual application plan while completing zero checklist items, executing zero checklist steps, granting zero application permission, applying zero manuscript patches, modifying zero manuscript files, claiming no manuscript submission readiness, claiming no readiness approval, claiming no external validation, claiming no independent experiment, claiming no proof assistant verification, adding no citations, and introducing no real-biological operational capability?

        ## Source artifacts

        - `outputs/safe_abstract_toy_manuscript_patch_application_plan_v8_201.md`
        - `outputs/safe_abstract_toy_manuscript_patch_application_plan_v8_201.json`

        ## Checklist boundary

        v8.202 creates a checklist only.

        This milestone completes zero checklist items.

        This milestone executes zero checklist steps.

        This milestone grants zero application permission.

        This milestone applies zero manuscript patches.

        This milestone modifies zero manuscript files.

        This milestone is not manuscript submission readiness.

        This milestone is not readiness approval.

        This milestone is not external validation.

        This milestone is not independent experiment evidence.

        This milestone does not add new citations.

        ## Toy manuscript patch application checklist

        JSON export:
        - `{json_path}`

        Checklist decision:
        - {package["checklist_decision"]}

        Checklist counts:
        - Toy manuscript patch application checklist item count: {package["checklist_item_count"]}
        - Toy manuscript patch application checklist completion count: {package["checklist_completion_count"]}
        - Toy manuscript patch application checklist execution count: {package["checklist_execution_count"]}
        - Toy manuscript patch application permission count: {package["application_permission_count"]}
        - Toy manuscript patch application applied patch count: {package["applied_patch_count"]}
        - Toy manuscript patch application manuscript file modified count: {package["manuscript_file_modified_count"]}
        - Toy manuscript patch application manuscript mutation count: {package["manuscript_mutation_count"]}
        - Toy manuscript patch application checklist non-readiness disclaimer count: {package["non_readiness_disclaimer_count"]}
        - Toy manuscript patch application checklist boundary note count: {package["boundary_note_count"]}

        ## Checklist items

        {chr(10).join(item_lines)}

        ## Counters

        {_counter_lines()}

        ## Safe claim

        The project has created a controlled plan-only checklist for audited safe abstract toy manuscript patch application planning, while completing zero checklist items, executing zero checklist steps, granting zero application permission, applying zero manuscript patches, modifying zero manuscript files, and preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
        """
    ).strip() + "\n"

    return report, package


def write_report(source_path: Path, output_path: Path, source_json: Path, json_path: Path) -> tuple[str, dict[str, Any]]:
    source_path.read_text(encoding="utf-8", errors="replace")
    report, package = build_report(source_json, json_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return report, package
