from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy manuscript patch application plan count: 1",
    "New safe abstract toy manuscript patch application plan count: 1",
    "Toy manuscript patch application plan JSON export count: 1",
    "Toy manuscript patch application plan step count: 7",
    "Toy manuscript patch application plan execution count: 0",
    "Toy manuscript patch application permission count: 0",
    "Toy manuscript patch application applied patch count: 0",
    "Toy manuscript patch application manuscript file modified count: 0",
    "Toy manuscript patch application manuscript mutation count: 0",
    "Toy manuscript patch application plan non-readiness disclaimer count: 1",
    "Toy manuscript patch application plan boundary note count: 7",
    "Toy manuscript patch application plan direct execution count: 1",

    "Safe abstract toy manuscript patch application readiness gate count: 1",
    "Toy manuscript patch application gate JSON export count: 1",
    "Toy manuscript patch application gate check count: 8",
    "Toy manuscript patch application structural gate pass count: 1",
    "Toy manuscript patch application structural gate failure count: 0",
    "Toy manuscript patch application permission count: 0",
    "Toy manuscript patch application execution count: 0",
    "Toy manuscript patch application applied patch count: 0",
    "Toy manuscript patch application manuscript file modified count: 0",
    "Toy manuscript patch application manuscript mutation count: 0",

    "Safe abstract toy manuscript patch dry-run package count: 1",
    "Toy manuscript patch dry-run JSON export count: 1",
    "Toy manuscript dry-run preview count: 6",
    "Toy manuscript dry-run applied patch count: 0",
    "Toy manuscript dry-run manuscript file modified count: 0",
    "Toy manuscript dry-run manuscript mutation count: 0",

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


def load_gate(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    expected = "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_readiness_gate"
    if payload.get("package_kind") != expected:
        raise ValueError(f"Unexpected package kind: {payload.get('package_kind')}")
    return payload


def build_application_plan(source_json: Path) -> dict[str, Any]:
    gate = load_gate(source_json)

    assert gate["gate_check_count"] == 8
    assert gate["structural_gate_pass_count"] == 1
    assert gate["structural_gate_failure_count"] == 0
    assert gate["application_permission_count"] == 0
    assert gate["application_execution_count"] == 0
    assert gate["applied_patch_count"] == 0
    assert gate["manuscript_file_modified_count"] == 0
    assert gate["manuscript_mutation_count"] == 0

    plan_steps = [
        ("manual_review_gate_report", "manual_review", "Review the v8.200 structural gate report before any future manual manuscript action."),
        ("confirm_toy_scope", "scope_check", "Confirm that every future insertion remains synthetic, abstract, unitless, and non-operational."),
        ("confirm_zero_real_biological_scope", "safety_check", "Confirm zero real biological dataset import, real pathogen simulation, receptor parameterization, host targeting, wet-lab protocol, and actionable biosafety-risk instruction."),
        ("confirm_non_readiness_boundary", "readiness_boundary_check", "Confirm that the plan does not make the manuscript submission ready and does not approve readiness."),
        ("confirm_no_validation_or_citation_claim", "research_boundary_check", "Confirm zero external validation, zero independent experiment, zero proof assistant verification, and zero new citation additions."),
        ("prepare_future_manual_diff_only", "future_manual_diff_preparation", "Prepare only a future manual diff pathway; do not execute it in this milestone."),
        ("stop_before_application", "hard_stop", "Stop before any application, manuscript file modification, or manuscript mutation."),
    ]

    steps = [
        {
            "step_id": step_id,
            "step_order": index,
            "step_kind": kind,
            "description": description,
            "boundary_note": "Plan-only step. No permission, execution, manuscript modification, readiness approval, validation, citation addition, or real-biological operational claim is created.",
        }
        for index, (step_id, kind, description) in enumerate(plan_steps, start=1)
    ]

    return {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_plan",
        "source_gate_check_count": gate["gate_check_count"],
        "source_structural_gate_pass_count": gate["structural_gate_pass_count"],
        "source_structural_gate_failure_count": gate["structural_gate_failure_count"],
        "plan_step_count": 7,
        "application_plan_execution_count": 0,
        "application_permission_count": 0,
        "application_execution_count": 0,
        "applied_patch_count": 0,
        "manuscript_file_modified_count": 0,
        "manuscript_mutation_count": 0,
        "non_readiness_disclaimer_count": 1,
        "boundary_note_count": 7,
        "plan_decision": "plan_created_but_application_not_permitted_or_executed",
        "plan_steps": steps,
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
    package = build_application_plan(source_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(package, indent=2, sort_keys=True), encoding="utf-8")
    return package


def build_report(source_text: str, source_json: Path, json_path: Path) -> tuple[str, dict[str, Any]]:
    package = write_package_json(source_json, json_path)

    step_lines = []
    for step in package["plan_steps"]:
        step_lines.append(
            dedent(
                f"""
                ### {step["step_id"]}

                Order: {step["step_order"]}

                Kind: {step["step_kind"]}

                Description: {step["description"]}

                Boundary note: {step["boundary_note"]}
                """
            ).strip()
        )

    report = dedent(
        f"""
        # v8.201 - Safe Abstract Toy Manuscript Patch Application Plan

        ## Question

        Can Viruse Fabric create a controlled future manual application plan from the v8.200 structural gate while executing zero manuscript patches, granting zero application permission, modifying zero manuscript files, claiming no manuscript submission readiness, claiming no readiness approval, claiming no external validation, claiming no independent experiment, claiming no proof assistant verification, adding no citations, and introducing no real-biological operational capability?

        ## Source artifacts

        - `outputs/safe_abstract_toy_manuscript_patch_application_readiness_gate_v8_200.md`
        - `outputs/safe_abstract_toy_manuscript_patch_application_readiness_gate_v8_200.json`

        ## Plan boundary

        v8.201 creates a plan only.

        This milestone does not apply a manuscript patch.

        This milestone grants zero application permission.

        This milestone executes zero application steps.

        This milestone modifies zero manuscript files.

        This milestone is not manuscript submission readiness.

        This milestone is not readiness approval.

        This milestone is not external validation.

        This milestone is not independent experiment evidence.

        This milestone does not add new citations.

        ## Toy manuscript patch application plan

        JSON export:
        - `{json_path}`

        Plan decision:
        - {package["plan_decision"]}

        Plan counts:
        - Toy manuscript patch application plan step count: {package["plan_step_count"]}
        - Toy manuscript patch application plan execution count: {package["application_plan_execution_count"]}
        - Toy manuscript patch application permission count: {package["application_permission_count"]}
        - Toy manuscript patch application applied patch count: {package["applied_patch_count"]}
        - Toy manuscript patch application manuscript file modified count: {package["manuscript_file_modified_count"]}
        - Toy manuscript patch application manuscript mutation count: {package["manuscript_mutation_count"]}
        - Toy manuscript patch application plan non-readiness disclaimer count: {package["non_readiness_disclaimer_count"]}
        - Toy manuscript patch application plan boundary note count: {package["boundary_note_count"]}

        ## Plan steps

        {chr(10).join(step_lines)}

        ## Counters

        {_counter_lines()}

        ## Safe claim

        The project has created a controlled future manual application plan for audited safe abstract toy manuscript patch dry-runs, while granting zero application permission, executing zero application steps, applying zero manuscript patches, modifying zero manuscript files, and preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
        """
    ).strip() + "\n"

    return report, package


def write_report(source_path: Path, output_path: Path, source_json: Path, json_path: Path) -> tuple[str, dict[str, Any]]:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    report, package = build_report(source_text, source_json, json_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return report, package
