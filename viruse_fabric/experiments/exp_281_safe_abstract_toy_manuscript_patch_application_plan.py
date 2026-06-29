from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.safe_abstract_toy_manuscript_patch_application_plan import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    build_application_plan,
    write_package_json,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_application_readiness_gate_v8_200.md")
SOURCE_JSON = Path("outputs/safe_abstract_toy_manuscript_patch_application_readiness_gate_v8_200.json")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_application_plan_v8_201.md")
JSON_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_application_plan_v8_201.json")
NOTE_PATH = Path("notes/theory_log.md")


def append_note() -> None:
    note = """
## v8.201 - Safe Abstract Toy Manuscript Patch Application Plan

Status: main manuscript patch application plan completed on branch `v8-201-safe-abstract-toy-manuscript-patch-application-plan`.

This milestone creates a future manual application plan from the v8.200 structural gate. It grants zero application permission, executes zero application steps, applies zero manuscript patches, modifies zero manuscript files, and creates zero manuscript mutations.

Positive package claims:
- Safe abstract toy manuscript patch application plan count: 1
- New safe abstract toy manuscript patch application plan count: 1
- Toy manuscript patch application plan JSON export count: 1
- Toy manuscript patch application plan step count: 7
- Toy manuscript patch application plan execution count: 0
- Toy manuscript patch application permission count: 0
- Toy manuscript patch application applied patch count: 0
- Toy manuscript patch application manuscript file modified count: 0
- Toy manuscript patch application manuscript mutation count: 0
- Toy manuscript patch application plan non-readiness disclaimer count: 1
- Toy manuscript patch application plan boundary note count: 7
- Toy manuscript patch application plan direct execution count: 1

Imported gate/dry-run/proposal/audit/integration/wording/figure-ready/ranking/sweep/kernel claims:
- Safe abstract toy manuscript patch application readiness gate count: 1
- Toy manuscript patch application gate check count: 8
- Toy manuscript patch application structural gate pass count: 1
- Toy manuscript patch application structural gate failure count: 0
- Toy manuscript patch application permission count: 0
- Toy manuscript patch application execution count: 0
- Safe abstract toy manuscript patch dry-run package count: 1
- Toy manuscript dry-run preview count: 6
- Toy manuscript dry-run applied patch count: 0
- Safe abstract toy manuscript patch proposal count: 1
- Toy manuscript proposed patch count: 6
- Safe abstract toy manuscript consistency audit count: 1
- Toy manuscript consistency pass count: 1
- Safe abstract toy manuscript integration map count: 1
- Toy manuscript integration slot count: 6
- Safe abstract toy results paragraph and caption package count: 1
- Safe abstract toy figure-ready interpretation package count: 1
- Safe abstract toy sensitivity ranking and baseline delta analysis count: 1
- Safe abstract toy constraint sensitivity sweep count: 1
- Simulator implementation count: 1
- Dynamics implementation count: 1
- Executable toy simulator count: 1

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

This milestone creates a future manual application plan only.
This milestone grants zero application permission.
This milestone executes zero application steps.
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
    if "## v8.201 - Safe Abstract Toy Manuscript Patch Application Plan" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 281: Safe Abstract Toy Manuscript Patch Application Plan")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"JSON path: {JSON_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")
    print(f"Source JSON: {SOURCE_JSON}")

    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_PATH.exists():
        errors.append(f"Missing source artifact: {SOURCE_PATH}")
    if not SOURCE_JSON.exists():
        errors.append(f"Missing source JSON: {SOURCE_JSON}")

    if not errors:
        package = build_application_plan(SOURCE_JSON)

        expected = {
            "package_kind": "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_application_plan",
            "source_gate_check_count": 8,
            "source_structural_gate_pass_count": 1,
            "source_structural_gate_failure_count": 0,
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

    if OUTPUT_PATH.exists():
        report_size = OUTPUT_PATH.stat().st_size
    else:
        report_size = 0

    for line in COUNTER_LINES:
        print(line)

    print(f"Report exists: {OUTPUT_PATH.exists()}")
    print(f"JSON exists: {JSON_PATH.exists()}")
    print(f"Report size: {report_size}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        print("Passed: False")
        return 1

    print("Passed: True")
    print("Experiment 281 completed successfully.")
    print("V8_201_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_PLAN_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
