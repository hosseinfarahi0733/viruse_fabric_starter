from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.safe_abstract_toy_manuscript_patch_dry_run_package import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    build_patch_dry_run_package,
    write_package_json,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_proposal_v8_198.md")
SOURCE_JSON = Path("outputs/safe_abstract_toy_manuscript_patch_proposal_v8_198.json")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_dry_run_package_v8_199.md")
JSON_PATH = Path("outputs/safe_abstract_toy_manuscript_patch_dry_run_package_v8_199.json")
NOTE_PATH = Path("notes/theory_log.md")


def run_package_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_JSON.exists():
        errors.append(f"Missing source JSON: {SOURCE_JSON}")
        return errors, warnings

    package = build_patch_dry_run_package(SOURCE_JSON)

    if package["package_kind"] != "toy_synthetic_abstract_unitless_non-operational_manuscript_patch_dry_run_package":
        errors.append("Unexpected manuscript patch dry-run package kind.")

    if package["source_proposed_patch_count"] != 6:
        errors.append("Expected source proposed patch count 6.")
    if package["dry_run_preview_count"] != 6:
        errors.append("Expected dry-run preview count 6.")
    if package["applied_patch_count"] != 0:
        errors.append("Expected applied patch count 0.")
    if package["manuscript_file_modified_count"] != 0:
        errors.append("Expected manuscript file modified count 0.")
    if package["manuscript_mutation_count"] != 0:
        errors.append("Expected manuscript mutation count 0.")
    if package["non_readiness_disclaimer_count"] != 1:
        errors.append("Expected non-readiness disclaimer count 1.")
    if package["boundary_note_count"] != 6:
        errors.append("Expected boundary note count 6.")
    if package["dry_run_statuses"] != ["preview_only_not_applied"]:
        errors.append(f"Unexpected dry-run statuses: {package['dry_run_statuses']}")
    if package["preview_actions"] != ["would_insert_if_later_approved"]:
        errors.append(f"Unexpected preview actions: {package['preview_actions']}")

    for preview in package["dry_run_previews"]:
        if preview["dry_run_status"] != "preview_only_not_applied":
            errors.append(f"Unexpected dry-run status: {preview}")
        if preview["manuscript_file_modified_count"] != 0:
            errors.append(f"Dry-run modified manuscript file: {preview}")
        if preview["manuscript_mutation_count"] != 0:
            errors.append(f"Dry-run mutated manuscript: {preview}")
        if "No manuscript file is modified" not in preview["boundary_note"]:
            errors.append(f"Missing dry-run boundary note: {preview['dry_run_id']}")

    write_package_json(source_json=SOURCE_JSON, json_path=JSON_PATH)

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
        errors.append("JSON dry-run output missing.")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.199 - Safe Abstract Toy Manuscript Patch Dry-Run Package

Status: main manuscript patch dry-run package completed on branch `v8-199-safe-abstract-toy-manuscript-patch-dry-run-package`.

This milestone creates a controlled dry-run preview from the v8.198 manuscript patch proposal. It previews placements only, applies zero manuscript patches, and modifies zero manuscript files.

Positive package claims:
- Safe abstract toy manuscript patch dry-run package count: 1
- New safe abstract toy manuscript patch dry-run package count: 1
- Toy manuscript patch dry-run JSON export count: 1
- Toy manuscript dry-run preview count: 6
- Toy manuscript dry-run source proposal count: 6
- Toy manuscript dry-run applied patch count: 0
- Toy manuscript dry-run manuscript file modified count: 0
- Toy manuscript dry-run manuscript mutation count: 0
- Toy manuscript dry-run non-readiness disclaimer count: 1
- Toy manuscript dry-run boundary note count: 6
- Toy manuscript patch dry-run direct execution count: 1

Imported proposal/audit/integration/wording/figure-ready/ranking/sweep/kernel claims:
- Safe abstract toy manuscript patch proposal count: 1
- Toy manuscript proposed patch count: 6
- Toy manuscript applied patch count: 0
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

This milestone creates a manuscript patch dry-run preview only.
This milestone applies zero manuscript patches.
This milestone modifies zero manuscript files.
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
    if "## v8.199 - Safe Abstract Toy Manuscript Patch Dry-Run Package" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 279: Safe Abstract Toy Manuscript Patch Dry-Run Package")
    print("Question: Can Viruse Fabric create a controlled dry-run preview while applying zero manuscript patches, modifying zero manuscript files, and preserving all real-biological and validation/readiness/citation boundary zeros?")
    print("Title: Safe Abstract Toy Manuscript Patch Dry-Run Package v8.199")
    print(f"Output path: {OUTPUT_PATH}")
    print(f"JSON path: {JSON_PATH}")
    print(f"Source artifact: {SOURCE_PATH}")
    print(f"Source JSON: {SOURCE_JSON}")

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
            source_json=SOURCE_JSON,
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
        "Interpretation: The v8.199 artifact creates a controlled dry-run preview for audited safe abstract toy manuscript patch proposals while applying zero manuscript patches, modifying zero manuscript files, and preserving simulator implementation count 1, dynamics implementation count 1, executable toy simulator count 1, and zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 279 completed successfully.")
    print("V8_199_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_DRY_RUN_PACKAGE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
