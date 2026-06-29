from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.safe_abstract_toy_manuscript_patch_application_checklist import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    build_application_checklist,
    write_package_json,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_application_plan_v8_201.md")
SOURCE_JSON = Path("outputs/safe_abstract_toy_manuscript_patch_application_plan_v8_201.json")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_application_checklist_v8_202.md")
JSON_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_application_checklist_v8_202.json")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.202 - Safe Abstract Toy Manuscript Patch Application Checklist

Status: main manuscript patch application checklist completed on branch `v8-202-safe-abstract-toy-manuscript-patch-application-checklist`.

This milestone creates a plan-only checklist from the v8.201 future manual application plan. It completes zero checklist items, executes zero checklist steps, grants zero application permission, applies zero manuscript patches, modifies zero manuscript files, and creates zero manuscript mutations.

Positive package claims:
- Safe abstract toy manuscript patch application checklist count: 1
- New safe abstract toy manuscript patch application checklist count: 1
- Toy manuscript patch application checklist JSON export count: 1
- Toy manuscript patch application checklist item count: 9
- Toy manuscript patch application checklist completion count: 0
- Toy manuscript patch application checklist execution count: 0
- Toy manuscript patch application permission count: 0
- Toy manuscript patch application applied patch count: 0
- Toy manuscript patch application manuscript file modified count: 0
- Toy manuscript patch application manuscript mutation count: 0
- Toy manuscript patch application checklist non-readiness disclaimer count: 1
- Toy manuscript patch application checklist boundary note count: 9
- Toy manuscript patch application checklist direct execution count: 1

Safety boundary claims:
- Real biological dataset import count: 0
- Real pathogen simulation count: 0
- Real receptor parameter count: 0
- Operational host targeting count: 0
- Wet-lab protocol count: 0
- Actionable biosafety-risk instruction count: 0
- Real-world infectivity optimization count: 0
- Immune evasion optimization count: 0
- Real host range prediction count: 0

Research boundary claims:
- Proof assistant verification count: 0
- External validation count: 0
- Independent experiment count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- New citation added count: 0

This milestone creates a checklist only.
This milestone completes zero checklist items.
This milestone executes zero checklist steps.
This milestone grants zero application permission.
This milestone applies zero manuscript patches.
This milestone modifies zero manuscript files.
This milestone creates zero manuscript mutations.
This milestone is not manuscript submission readiness.
This milestone is not readiness approval.
This milestone is not real biological dataset import.
This milestone is not real pathogen simulation.
This milestone is not real receptor parameterization.
This milestone is not operational host targeting.
This milestone is not wet-lab protocol work.
This milestone is not actionable biosafety-risk instruction.
This milestone is not external validation.
This milestone is not independent experiment evidence.
This milestone does not add citations.
"""
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.202 - Safe Abstract Toy Manuscript Patch Application Checklist" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 282: Safe Abstract Toy Manuscript Patch Application Checklist")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"JSON path: {JSON_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")
    print(f"Source JSON: {SOURCE_JSON}")

    errors: list[str] = []

    if not SOURCE_PATH.exists():
        errors.append(f"Missing source artifact: {SOURCE_PATH}")
    if not SOURCE_JSON.exists():
        errors.append(f"Missing source JSON: {SOURCE_JSON}")

    if not errors:
        package = build_application_checklist(SOURCE_JSON)

        expected = {
            "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_checklist",
            "source_plan_step_count": 7,
            "source_application_plan_execution_count": 0,
            "checklist_item_count": 9,
            "checklist_completion_count": 0,
            "checklist_execution_count": 0,
            "application_permission_count": 0,
            "application_execution_count": 0,
            "applied_patch_count": 0,
            "manuscript_file_modified_count": 0,
            "manuscript_mutation_count": 0,
            "non_readiness_disclaimer_count": 1,
            "boundary_note_count": 9,
            "checklist_decision": "checklist_created_but_not_completed_or_executed",
        }

        for key, value in expected.items():
            if package.get(key) != value:
                errors.append(f"{key} mismatch: expected {value!r}, got {package.get(key)!r}")

        write_package_json(SOURCE_JSON, JSON_PATH)
        report, package = write_report(SOURCE_PATH, OUTPUT_PATH, SOURCE_JSON, JSON_PATH)

        for phrase in REQUIRED_REPORT_PHRASES:
            if phrase not in report:
                errors.append(f"Missing required report phrase: {phrase}")

        payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        boundary = payload["boundary"]
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
        ]:
            if boundary.get(key) != 0:
                errors.append(f"Boundary mismatch: {key}")

    append_note()

    report_size = OUTPUT_PATH.stat().st_size if OUTPUT_PATH.exists() else 0

    for line in COUNTER_LINES:
        print(line)

    print(f"Report exists: {OUTPUT_PATH.exists()}")
    print(f"JSON exists: {JSON_PATH.exists()}")
    print(f"Report size: {report_size}")
    print(f"Errors: {len(errors)}")
    print("Warnings: 0")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        print("Passed: False")
        return 1

    print("Passed: True")
    print("Experiment 282 completed successfully.")
    print("V8_202_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_CHECKLIST_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
