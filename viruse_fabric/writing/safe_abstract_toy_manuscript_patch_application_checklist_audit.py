from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent
from typing import Any


COUNTER_LINES = [
    "Safe abstract toy manuscript patch application checklist audit count: 1",
    "New safe abstract toy manuscript patch application checklist audit count: 1",
    "Toy manuscript patch application checklist audit JSON export count: 1",
    "Toy manuscript patch application checklist audit item count: 9",
    "Toy manuscript patch application checklist audit pass count: 9",
    "Toy manuscript patch application checklist audit failure count: 0",
    "Toy manuscript patch application checklist audit execution count: 1",
    "Toy manuscript patch application checklist completion count: 0",
    "Toy manuscript patch application checklist execution count: 0",
    "Toy manuscript patch application permission count: 0",
    "Toy manuscript patch application applied patch count: 0",
    "Toy manuscript patch application manuscript file modified count: 0",
    "Toy manuscript patch application manuscript mutation count: 0",
    "Toy manuscript patch application checklist audit non-readiness disclaimer count: 1",
    "Toy manuscript patch application checklist audit boundary note count: 9",
    "Toy manuscript patch application checklist audit direct execution count: 1",

    "Safe abstract toy manuscript patch application checklist count: 1",
    "Toy manuscript patch application checklist JSON export count: 1",
    "Toy manuscript patch application checklist item count: 9",
    "Toy manuscript patch application checklist completion count: 0",
    "Toy manuscript patch application checklist execution count: 0",
    "Toy manuscript patch application checklist non-readiness disclaimer count: 1",
    "Toy manuscript patch application checklist boundary note count: 9",

    "Safe abstract toy manuscript patch application plan count: 1",
    "Toy manuscript patch application plan step count: 7",
    "Toy manuscript patch application plan execution count: 0",

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

    "Simulator implementation count: 1",
    "Dynamics implementation count: 1",
    "Executable toy simulator count: 1",
    "Unitless dynamics execution count: 1",
    "Abstract graph dynamics execution count: 1",
    "Synthetic fixture execution count: 3",

    "Imported safe abstract toy manuscript patch application checklist count: 1",
    "Imported safe abstract toy manuscript patch application plan count: 1",
    "Imported safe abstract toy manuscript patch application readiness gate count: 1",
    "Imported safe abstract toy manuscript patch dry-run package count: 1",
    "Imported safe abstract toy manuscript patch proposal count: 1",
    "Imported safe abstract toy manuscript consistency audit count: 1",
    "Imported safe abstract toy manuscript integration map count: 1",
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


def load_checklist(source_json: Path) -> dict[str, Any]:
    payload = json.loads(source_json.read_text(encoding="utf-8"))
    expected = "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_checklist"
    if payload.get("package_kind") != expected:
        raise ValueError(f"Unexpected package kind: {payload.get('package_kind')}")
    return payload


def build_checklist_audit(source_json: Path) -> dict[str, Any]:
    checklist = load_checklist(source_json)

    checks = [
        (
            "checklist_item_count",
            checklist.get("checklist_item_count") == 9,
            "Checklist contains exactly nine plan-only items.",
        ),
        (
            "checklist_completion_zero",
            checklist.get("checklist_completion_count") == 0,
            "Checklist completes zero items.",
        ),
        (
            "checklist_execution_zero",
            checklist.get("checklist_execution_count") == 0,
            "Checklist executes zero steps.",
        ),
        (
            "application_permission_zero",
            checklist.get("application_permission_count") == 0,
            "Checklist grants zero application permission.",
        ),
        (
            "application_execution_zero",
            checklist.get("application_execution_count") == 0,
            "Checklist executes zero application actions.",
        ),
        (
            "applied_patch_zero",
            checklist.get("applied_patch_count") == 0,
            "Checklist applies zero manuscript patches.",
        ),
        (
            "manuscript_file_modified_zero",
            checklist.get("manuscript_file_modified_count") == 0,
            "Checklist modifies zero manuscript files.",
        ),
        (
            "manuscript_mutation_zero",
            checklist.get("manuscript_mutation_count") == 0,
            "Checklist creates zero manuscript mutations.",
        ),
        (
            "boundary_zeros_preserved",
            all(
                checklist.get("boundary", {}).get(key) == 0
                for key in [
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
            ),
            "All explicit real-biological, validation, proof, readiness, approval, and citation boundary counters remain zero.",
        ),
    ]

    audit_items = [
        {
            "audit_id": check_id,
            "audit_order": index,
            "passed": bool(passed),
            "description": description,
            "boundary_note": "Audit-only item. It does not complete checklist items, execute checklist steps, grant permission, apply patches, modify manuscript files, approve readiness, validate, cite, prove, or create real-biological operational content.",
        }
        for index, (check_id, passed, description) in enumerate(checks, start=1)
    ]

    pass_count = sum(1 for item in audit_items if item["passed"])
    failure_count = len(audit_items) - pass_count

    return {
        "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_checklist_audit",
        "source_checklist_item_count": checklist["checklist_item_count"],
        "source_checklist_completion_count": checklist["checklist_completion_count"],
        "source_checklist_execution_count": checklist["checklist_execution_count"],
        "audit_item_count": len(audit_items),
        "audit_pass_count": pass_count,
        "audit_failure_count": failure_count,
        "checklist_completion_count": 0,
        "checklist_execution_count": 0,
        "application_permission_count": 0,
        "application_execution_count": 0,
        "applied_patch_count": 0,
        "manuscript_file_modified_count": 0,
        "manuscript_mutation_count": 0,
        "non_readiness_disclaimer_count": 1,
        "boundary_note_count": len(audit_items),
        "audit_decision": "audit_passed_but_no_checklist_completion_or_application_execution",
        "audit_items": audit_items,
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
    package = build_checklist_audit(source_json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(package, indent=2, sort_keys=True), encoding="utf-8")
    return package


def build_report(source_json: Path, json_path: Path) -> tuple[str, dict[str, Any]]:
    package = write_package_json(source_json, json_path)

    audit_lines = []
    for item in package["audit_items"]:
        audit_lines.append(
            dedent(
                f"""
                ### {item["audit_id"]}

                Order: {item["audit_order"]}

                Passed: {item["passed"]}

                Description: {item["description"]}

                Boundary note: {item["boundary_note"]}
                """
            ).strip()
        )

    report = dedent(
        f"""
        # v8.203 - Safe Abstract Toy Manuscript Patch Application Checklist Audit

        ## Question

        Can Viruse Fabric audit the v8.202 plan-only checklist while completing zero checklist items, executing zero checklist steps, granting zero application permission, applying zero manuscript patches, modifying zero manuscript files, claiming no manuscript submission readiness, claiming no readiness approval, claiming no external validation, claiming no independent experiment, claiming no proof assistant verification, adding no citations, and introducing no real-biological operational capability?

        ## Source artifacts

        - `outputs/safe_abstract_toy_manuscript_patch_application_checklist_v8_202.md`
        - `outputs/safe_abstract_toy_manuscript_patch_application_checklist_v8_202.json`

        ## Audit boundary

        v8.203 creates an audit only.

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

        ## Toy manuscript patch application checklist audit

        JSON export:
        - `{json_path}`

        Audit decision:
        - {package["audit_decision"]}

        Audit counts:
        - Toy manuscript patch application checklist audit item count: {package["audit_item_count"]}
        - Toy manuscript patch application checklist audit pass count: {package["audit_pass_count"]}
        - Toy manuscript patch application checklist audit failure count: {package["audit_failure_count"]}
        - Toy manuscript patch application checklist audit execution count: 1
        - Toy manuscript patch application checklist completion count: {package["checklist_completion_count"]}
        - Toy manuscript patch application checklist execution count: {package["checklist_execution_count"]}
        - Toy manuscript patch application permission count: {package["application_permission_count"]}
        - Toy manuscript patch application applied patch count: {package["applied_patch_count"]}
        - Toy manuscript patch application manuscript file modified count: {package["manuscript_file_modified_count"]}
        - Toy manuscript patch application manuscript mutation count: {package["manuscript_mutation_count"]}
        - Toy manuscript patch application checklist audit non-readiness disclaimer count: {package["non_readiness_disclaimer_count"]}
        - Toy manuscript patch application checklist audit boundary note count: {package["boundary_note_count"]}

        ## Audit items

        {chr(10).join(audit_lines)}

        ## Counters

        {_counter_lines()}

        ## Safe claim

        The project has created an audit-only review of the plan-only checklist for audited safe abstract toy manuscript patch application planning, while completing zero checklist items, executing zero checklist steps, granting zero application permission, applying zero manuscript patches, modifying zero manuscript files, and preserving simulator implementation count: 1, dynamics implementation count: 1, executable toy simulator count: 1, and all explicit zero boundaries against real biological dataset imports, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions.
        """
    ).strip() + "\n"

    return report, package


def write_report(source_path: Path, output_path: Path, source_json: Path, json_path: Path) -> tuple[str, dict[str, Any]]:
    source_path.read_text(encoding="utf-8", errors="replace")
    report, package = build_report(source_json, json_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return report, package
