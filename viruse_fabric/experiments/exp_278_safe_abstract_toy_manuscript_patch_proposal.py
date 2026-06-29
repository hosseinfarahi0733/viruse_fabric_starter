from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.safe_abstract_toy_manuscript_patch_proposal import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    build_patch_proposal,
    write_package_json,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_manuscript_consistency_audit_v8_197.md")
SOURCE_AUDIT_JSON = Path("outputs/safe_abstract_toy_manuscript_consistency_audit_v8_197.json")
SOURCE_INTEGRATION_JSON = Path("outputs/safe_abstract_toy_manuscript_integration_map_v8_196.json")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_proposal_v8_198.md")
JSON_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_proposal_v8_198.json")
NOTE_PATH = Path("notes/theory_log.md")


def run_package_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_AUDIT_JSON.exists():
        errors.append(f"Missing source audit JSON: {SOURCE_AUDIT_JSON}")
        return errors, warnings

    if not SOURCE_INTEGRATION_JSON.exists():
        errors.append(f"Missing source integration JSON: {SOURCE_INTEGRATION_JSON}")
        return errors, warnings

    package = build_patch_proposal(
        audit_json=SOURCE_AUDIT_JSON,
        integration_json=SOURCE_INTEGRATION_JSON,
    )

    if package["package_kind"] != "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_proposal":
        errors.append("Unexpected manuscript patch proposal package kind.")

    if package["source_audit_pass_count"] != 1:
        errors.append("Expected imported audit pass count 1.")
    if package["source_slot_count"] != 6:
        errors.append("Expected source slot count 6.")
    if package["proposed_patch_count"] != 6:
        errors.append("Expected proposed patch count 6.")
    if package["applied_patch_count"] != 0:
        errors.append("Expected applied patch count 0.")
    if package["non_readiness_disclaimer_count"] != 1:
        errors.append("Expected non-readiness disclaimer count 1.")
    if package["boundary_note_count"] != 6:
        errors.append("Expected boundary note count 6.")
    if package["proposal_statuses"] != ["proposal_only_not_applied"]:
        errors.append(f"Unexpected proposal statuses: {package['proposal_statuses']}")

    for proposal in package["patch_proposals"]:
        if proposal["proposal_status"] != "proposal_only_not_applied":
            errors.append(f"Unexpected proposal status: {proposal}")
        if "not an applied manuscript patch" not in proposal["boundary_note"]:
            errors.append(f"Missing applied-patch boundary note: {proposal['patch_id']}")

    write_package_json(
        audit_json=SOURCE_AUDIT_JSON,
        integration_json=SOURCE_INTEGRATION_JSON,
        json_path=JSON_PATH,
    )

    if JSON_PATH.exists():
        payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        if payload["boundary"]["real_biological_dataset_import_count"] != 0:
            errors.append("JSON payload real biological dataset boundary mismatch.")
        if payload["boundary"]["real_pathogen_simulation_count"] != 0:
            errors.append("JSON payload real pathogen boundary mismatch.")
        if payload["boundary"]["proof_assistant_verification_count"] != 0:
            errors.append("JSON payload proof assistant boundary mismatch.")
        if payload["boundary"]["external_validation_count"] != 0:
            errors.append("JSON payload external validation boundary mismatch.")
        if payload["boundary"]["independent_experiment_count"] != 0:
            errors.append("JSON payload independent experiment boundary mismatch.")
        if payload["boundary"]["manuscript_submission_ready_count"] != 0:
            errors.append("JSON payload manuscript readiness boundary mismatch.")
        if payload["boundary"]["new_citation_added_count"] != 0:
            errors.append("JSON payload citation boundary mismatch.")
    else:
        errors.append("JSON patch proposal output missing.")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.198 - Safe Abstract Toy Manuscript Patch Proposal

Status: main manuscript patch proposal completed on branch `v8-198-safe-abstract-toy-manuscript-patch-proposal`.

This milestone creates a controlled manuscript patch proposal from the audited toy manuscript integration map. It proposes placements only and applies zero manuscript patches.

Positive package claims:
- Safe abstract toy manuscript patch proposal count: 1
- New safe abstract toy manuscript patch proposal count: 1
- Toy manuscript patch proposal JSON export count: 1
- Toy manuscript proposed patch count: 6
- Toy manuscript applied patch count: 0
- Toy manuscript patch proposal source slot count: 6
- Toy manuscript patch proposal audit pass imported count: 1
- Toy manuscript patch proposal non-readiness disclaimer count: 1
- Toy manuscript patch proposal boundary note count: 6
- Toy manuscript patch proposal direct execution count: 1

Imported audit/integration/wording/figure-ready/ranking/sweep/kernel claims:
- Safe abstract toy manuscript consistency audit count: 1
- Toy manuscript consistency pass count: 1
- Toy manuscript missing slot count: 0
- Toy manuscript boundary failure count: 0
- Toy manuscript positive overclaim marker count: 0
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

This milestone creates a manuscript patch proposal only.
This milestone applies zero manuscript patches.
This milestone is not manuscript submission readiness.
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
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.198 - Safe Abstract Toy Manuscript Patch Proposal" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 278: Safe Abstract Toy Manuscript Patch Proposal")
    print("Question: Can Viruse Fabric create a controlled toy manuscript patch proposal while applying zero manuscript patches and preserving all real-biological and validation/readiness/citation boundary zeros?")
    print("Title: Safe Abstract Toy Manuscript Patch Proposal v8.198")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"JSON path: {JSON_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")
    print(f"Source audit JSON: {SOURCE_AUDIT_JSON}")
    print(f"Source integration JSON: {SOURCE_INTEGRATION_JSON}")

    errors: list[str] = []
    warnings: list[str] = []

    package_errors, package_warnings = run_package_tests()
    errors.extend(package_errors)
    warnings.extend(package_warnings)

    if not SOURCE_PATH.exists():
        errors.append(f"Missing source artifact: {SOURCE_PATH}")
    else:
        result = write_report(
            source_path=SOURCE_PATH,
            output_path=OUTPUT_PATH,
            audit_json=SOURCE_AUDIT_JSON,
            integration_json=SOURCE_INTEGRATION_JSON,
            json_path=JSON_PATH,
        )

        for phrase in result.missing_source_phrases:
            errors.append(f"Missing required source phrase: {phrase}")

        for phrase in result.missing_report_phrases:
            errors.append(f"Missing required report phrase: {phrase}")

        if result.prohibited_behavior_count != 0:
            errors.append(f"Prohibited behavior count must be 0, got {result.prohibited_behavior_count}")

        if result.boundary_phrase_count < 12:
            warnings.append(f"Boundary phrase count is low: {result.boundary_phrase_count}")

        warnings.extend(result.warning_messages)

    if OUTPUT_PATH.exists():
        report_text = OUTPUT_PATH.read_text(encoding="utf-8", errors="replace")
        report_size = OUTPUT_PATH.stat().st_size
    else:
        report_text = ""
        report_size = 0

    missing_required_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report_text
    ]

    if missing_required_report_phrases:
        for phrase in missing_required_report_phrases:
            errors.append(f"Missing required report phrase after write: {phrase}")

    append_note()

    for line in COUNTER_LINES:
        print(line)

    print(f"Report exists: {OUTPUT_PATH.exists()}")
    print(f"JSON exists: {JSON_PATH.exists()}")
    print(f"Report size: {report_size}")
    print(f"Missing required report phrases: {len(missing_required_report_phrases)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        print("Passed: False")
        return 1

    print("Passed: True")
    print(
        "Interpretation: The v8.198 artifact creates a controlled manuscript patch proposal for audited safe abstract toy wording while applying zero manuscript patches and preserving simulator implementation count 1, dynamics implementation count 1, executable toy simulator count 1, and zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 278 completed successfully.")
    print("V8_198_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_PROPOSAL_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
