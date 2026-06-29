from __future__ import annotations

import json
from pathlib import Path

from viruse_fabric.writing.safe_abstract_toy_manuscript_consistency_audit import (
    COUNTER_LINES,
    REQUIRED_REPORT_PHRASES,
    build_manuscript_consistency_audit,
    write_package_json,
    write_report,
)


SOURCE_PATH = Path("outputs/safe_abstract_toy_manuscript_integration_map_v8_196.md")
SOURCE_JSON = Path("outputs/safe_abstract_toy_manuscript_integration_map_v8_196.json")
OUTPUT_PATH = Path("outputs/safe_abstract_toy_manuscript_consistency_audit_v8_197.md")
JSON_PATH = Path("outputs/safe_abstract_toy_manuscript_consistency_audit_v8_197.json")
NOTE_PATH = Path("notes/theory_log.md")


def run_package_tests() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not SOURCE_JSON.exists():
        errors.append(f"Missing source JSON: {SOURCE_JSON}")
        return errors, warnings

    package = build_manuscript_consistency_audit(SOURCE_JSON)

    if package["package_kind"] != "toy_synthetic_abstract_unitless_non-operational_manuscript_consistency_audit":
        errors.append("Unexpected manuscript consistency audit package kind.")

    if package["source_integration_slot_count"] != 6:
        errors.append("Expected 6 source integration slots.")
    if package["audited_slot_count"] != 6:
        errors.append("Expected 6 audited slots.")
    if package["missing_slot_count"] != 0:
        errors.append("Expected zero missing slots.")
    if package["boundary_failure_count"] != 0:
        errors.append("Expected zero boundary failures.")
    if package["positive_overclaim_marker_count"] != 0:
        errors.append("Expected zero positive overclaim markers.")
    if package["non_readiness_disclaimer_present_count"] != 1:
        errors.append("Expected non-readiness disclaimer present count 1.")
    if package["safety_boundary_slot_present_count"] != 1:
        errors.append("Expected safety boundary slot present count 1.")
    if package["consistency_pass_count"] != 1:
        errors.append("Expected consistency pass count 1.")

    if not all(check["passed"] for check in package["audit_checks"]):
        errors.append("Expected all audit checks to pass.")

    write_package_json(SOURCE_JSON, JSON_PATH)

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
        errors.append("JSON consistency audit output missing.")

    return errors, warnings


def append_note() -> None:
    note = """
## v8.197 - Safe Abstract Toy Manuscript Consistency Audit

Status: main manuscript consistency audit completed on branch `v8-197-safe-abstract-toy-manuscript-consistency-audit`.

This milestone audits the v8.196 manuscript integration map for slot completeness, boundary preservation, non-readiness disclaimer presence, safety boundary presence, and absence of positive overclaim markers.

Positive audit claims:
- Safe abstract toy manuscript consistency audit count: 1
- New safe abstract toy manuscript consistency audit count: 1
- Toy manuscript consistency audit JSON export count: 1
- Toy manuscript integration slot audited count: 6
- Toy manuscript consistency pass count: 1
- Toy manuscript missing slot count: 0
- Toy manuscript boundary failure count: 0
- Toy manuscript positive overclaim marker count: 0
- Toy manuscript non-readiness disclaimer present count: 1
- Toy manuscript safety boundary slot present count: 1
- Toy manuscript consistency audit direct execution count: 1

Imported integration/wording/figure-ready/ranking/sweep/kernel claims:
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

This milestone creates a consistency audit for toy manuscript wording only.
This milestone is not real biological dataset import.
This milestone is not real pathogen simulation.
This milestone is not real receptor parameterization.
This milestone is not operational host targeting.
This milestone is not wet-lab protocol work.
This milestone is not actionable biosafety-risk instruction.
This milestone is not external validation.
This milestone is not independent experiment evidence.
This milestone is not manuscript submission readiness.
This milestone does not add citations.
"""
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = NOTE_PATH.read_text(encoding="utf-8", errors="replace") if NOTE_PATH.exists() else ""
    if "## v8.197 - Safe Abstract Toy Manuscript Consistency Audit" not in existing:
        NOTE_PATH.write_text(existing.rstrip() + "\n\n" + note.strip() + "\n", encoding="utf-8")


def main() -> int:
    print("Experiment 277: Safe Abstract Toy Manuscript Consistency Audit")
    print("Question: Can Viruse Fabric audit the toy manuscript integration map while preserving all real-biological and validation/readiness/citation boundary zeros?")
    print("Title: Safe Abstract Toy Manuscript Consistency Audit v8.197")
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
            SOURCE_PATH,
            OUTPUT_PATH,
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
        "Interpretation: The v8.197 artifact audits the safe abstract toy manuscript integration map while preserving simulator implementation count 1, dynamics implementation count 1, executable toy simulator count 1, and zero counts for real biological dataset import, real pathogen simulation, real receptor parameters, operational host targeting, wet-lab protocols, actionable biosafety-risk instructions, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions."
    )
    print("Experiment 277 completed successfully.")
    print("V8_197_SAFE_ABSTRACT_TOY_MANUSCRIPT_CONSISTENCY_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
