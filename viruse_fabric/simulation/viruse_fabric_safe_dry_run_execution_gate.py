"""Safe dry-run execution gate.

This module prepares a gate for a future dry-run, but does not authorize or
execute the dry-run now. It does not execute the engine, does not run a sweep,
and does not execute null controls.

No real biological dataset, pathogen model, receptor parameter, host targeting,
wet-lab protocol, infectivity optimization, immune evasion optimization, or
host range prediction is introduced.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping

from viruse_fabric.simulation.viruse_fabric_safe_dry_run_manifest_builder import (
    SAFE_DRY_RUN_MANIFEST_BUILDER_VERSION,
    build_safe_dry_run_manifest_v1,
)


SAFE_DRY_RUN_EXECUTION_GATE_VERSION = "SAFE_DRY_RUN_EXECUTION_GATE_V1"
SAFE_DRY_RUN_EXECUTION_GATE_SCOPE = (
    "safe-dry-run-execution-gate-only-no-dry-run-engine-or-sweep-execution"
)


@dataclass(frozen=True)
class SafeDryRunExecutionGate:
    """Gate metadata only. It does not execute anything."""

    gate_id: str = "safe_dry_run_execution_gate_v1"
    dry_run_allowed_now: bool = False
    dry_run_execution_enabled: bool = False
    engine_execution_enabled: bool = False
    sweep_execution_enabled: bool = False
    null_control_execution_enabled: bool = False
    claim_expansion_allowed: bool = False
    evidence_interpretation_allowed: bool = False
    real_biological_semantics_allowed: bool = False

    def validate_static_safety(self) -> None:
        if self.gate_id != "safe_dry_run_execution_gate_v1":
            raise ValueError("Unexpected safe dry-run execution gate id.")

        must_be_false = {
            "dry_run_allowed_now": self.dry_run_allowed_now,
            "dry_run_execution_enabled": self.dry_run_execution_enabled,
            "engine_execution_enabled": self.engine_execution_enabled,
            "sweep_execution_enabled": self.sweep_execution_enabled,
            "null_control_execution_enabled": self.null_control_execution_enabled,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "evidence_interpretation_allowed": self.evidence_interpretation_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
        }

        bad = {key: value for key, value in must_be_false.items() if value is not False}
        if bad:
            raise ValueError(f"Forbidden enabled flags in execution gate: {bad}")

    def build_gate(self) -> Dict[str, Any]:
        self.validate_static_safety()

        manifest = build_safe_dry_run_manifest_v1(
            preview_cell_count=12,
            preview_pair_count=16,
        )

        gate_checks = build_safe_dry_run_execution_gate_checks_v1()

        gate = {
            "gate_version": SAFE_DRY_RUN_EXECUTION_GATE_VERSION,
            "scope": SAFE_DRY_RUN_EXECUTION_GATE_SCOPE,
            "gate_id": self.gate_id,
            "manifest_builder_version": SAFE_DRY_RUN_MANIFEST_BUILDER_VERSION,
            "manifest_cell_count": manifest["cell_count"],
            "manifest_template_count": manifest["template_count"],
            "manifest_planned_null_control_pair_count": manifest[
                "planned_null_control_pair_count"
            ],
            "manifest_planned_expected_total_abstract_leak_count": manifest[
                "planned_expected_total_abstract_leak_count"
            ],
            "manifest_route_counts": manifest["route_counts"],
            "gate_check_count": len(gate_checks),
            "gate_checks": gate_checks,
            "dry_run_allowed_now": self.dry_run_allowed_now,
            "dry_run_execution_enabled": self.dry_run_execution_enabled,
            "engine_execution_enabled": self.engine_execution_enabled,
            "sweep_execution_enabled": self.sweep_execution_enabled,
            "null_control_execution_enabled": self.null_control_execution_enabled,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "evidence_interpretation_allowed": self.evidence_interpretation_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
            "safe_abstract_toy_only": True,
            "interpretation_boundary": "execution_gate_metadata_only_not_authorization",
            "authorization_status": "not_authorized",
            "failure_mode": "stop_before_dry_run_if_any_gate_check_fails",
        }

        validate_safe_dry_run_execution_gate_v1(gate)
        return gate


def build_safe_dry_run_execution_gate_checks_v1() -> List[Dict[str, Any]]:
    return [
        {
            "gate_check_id": "SAFE-DRY-RUN-GATE-001",
            "title": "Manifest exists and remains metadata-only",
            "required": True,
            "passes_now": True,
            "authorizes_execution": False,
            "blocks_engine_execution": True,
            "blocks_sweep_execution": True,
            "blocks_null_control_execution": True,
            "blocks_claim_expansion": True,
            "failure_response": "stop_before_dry_run",
        },
        {
            "gate_check_id": "SAFE-DRY-RUN-GATE-002",
            "title": "Dry-run execution remains disabled",
            "required": True,
            "passes_now": True,
            "authorizes_execution": False,
            "blocks_engine_execution": True,
            "blocks_sweep_execution": True,
            "blocks_null_control_execution": True,
            "blocks_claim_expansion": True,
            "failure_response": "reject_if_dry_run_execution_flag_is_true",
        },
        {
            "gate_check_id": "SAFE-DRY-RUN-GATE-003",
            "title": "Engine and sweep execution remain disabled",
            "required": True,
            "passes_now": True,
            "authorizes_execution": False,
            "blocks_engine_execution": True,
            "blocks_sweep_execution": True,
            "blocks_null_control_execution": True,
            "blocks_claim_expansion": True,
            "failure_response": "reject_if_engine_or_sweep_execution_flag_is_true",
        },
        {
            "gate_check_id": "SAFE-DRY-RUN-GATE-004",
            "title": "Null-control execution remains disabled",
            "required": True,
            "passes_now": True,
            "authorizes_execution": False,
            "blocks_engine_execution": True,
            "blocks_sweep_execution": True,
            "blocks_null_control_execution": True,
            "blocks_claim_expansion": True,
            "failure_response": "reject_if_null_control_execution_flag_is_true",
        },
        {
            "gate_check_id": "SAFE-DRY-RUN-GATE-005",
            "title": "Biological and operational semantics remain forbidden",
            "required": True,
            "passes_now": True,
            "authorizes_execution": False,
            "blocks_engine_execution": True,
            "blocks_sweep_execution": True,
            "blocks_null_control_execution": True,
            "blocks_claim_expansion": True,
            "failure_response": "reject_if_biological_or_operational_semantics_appear",
        },
        {
            "gate_check_id": "SAFE-DRY-RUN-GATE-006",
            "title": "Validation, readiness, citation, and evidence claims remain forbidden",
            "required": True,
            "passes_now": True,
            "authorizes_execution": False,
            "blocks_engine_execution": True,
            "blocks_sweep_execution": True,
            "blocks_null_control_execution": True,
            "blocks_claim_expansion": True,
            "failure_response": "reject_if_claim_or_readiness_language_appears",
        },
    ]


def build_safe_dry_run_execution_gate_v1() -> Dict[str, Any]:
    gate = SafeDryRunExecutionGate()
    return gate.build_gate()


def validate_safe_dry_run_execution_gate_v1(gate: Mapping[str, Any]) -> None:
    if gate["gate_version"] != SAFE_DRY_RUN_EXECUTION_GATE_VERSION:
        raise ValueError("Unexpected safe dry-run execution gate version.")
    if gate["scope"] != SAFE_DRY_RUN_EXECUTION_GATE_SCOPE:
        raise ValueError("Unexpected safe dry-run execution gate scope.")
    if gate["manifest_builder_version"] != "SAFE_DRY_RUN_MANIFEST_BUILDER_V1":
        raise ValueError("Unexpected manifest builder version.")
    if gate["manifest_cell_count"] != 64:
        raise ValueError("Expected 64 manifest cells.")
    if gate["manifest_template_count"] != 4:
        raise ValueError("Expected 4 null-control templates.")
    if gate["manifest_planned_null_control_pair_count"] != 256:
        raise ValueError("Expected 256 planned null-control pairs.")
    if gate["manifest_planned_expected_total_abstract_leak_count"] != 0:
        raise ValueError("Expected planned abstract leak count to be zero.")
    if gate["manifest_route_counts"] != {
        "current_engine_default_boundary": 1,
        "safe_sweep_profile_validation": 63,
        "outside_safe_sweep_profile": 0,
    }:
        raise ValueError(f"Unexpected manifest route counts: {gate['manifest_route_counts']}")
    if gate["gate_check_count"] != 6:
        raise ValueError("Expected 6 execution gate checks.")

    must_be_false = [
        "dry_run_allowed_now",
        "dry_run_execution_enabled",
        "engine_execution_enabled",
        "sweep_execution_enabled",
        "null_control_execution_enabled",
        "claim_expansion_allowed",
        "evidence_interpretation_allowed",
        "real_biological_semantics_allowed",
    ]

    for key in must_be_false:
        if gate[key] is not False:
            raise ValueError(f"{key} must be False.")

    if gate["safe_abstract_toy_only"] is not True:
        raise ValueError("safe_abstract_toy_only must be True.")
    if gate["interpretation_boundary"] != "execution_gate_metadata_only_not_authorization":
        raise ValueError("Unexpected interpretation boundary.")
    if gate["authorization_status"] != "not_authorized":
        raise ValueError("Execution gate must not authorize dry-run execution.")

    for check in gate["gate_checks"]:
        if check["required"] is not True:
            raise ValueError(f"Gate check must be required: {check}")
        if check["passes_now"] is not True:
            raise ValueError(f"Gate check must pass as metadata check: {check}")
        if check["authorizes_execution"] is not False:
            raise ValueError(f"Gate check must not authorize execution: {check}")
        if check["blocks_engine_execution"] is not True:
            raise ValueError(f"Gate check must block engine execution: {check}")
        if check["blocks_sweep_execution"] is not True:
            raise ValueError(f"Gate check must block sweep execution: {check}")
        if check["blocks_null_control_execution"] is not True:
            raise ValueError(f"Gate check must block null-control execution: {check}")
        if check["blocks_claim_expansion"] is not True:
            raise ValueError(f"Gate check must block claim expansion: {check}")


__all__ = [
    "SAFE_DRY_RUN_EXECUTION_GATE_VERSION",
    "SAFE_DRY_RUN_EXECUTION_GATE_SCOPE",
    "SafeDryRunExecutionGate",
    "build_safe_dry_run_execution_gate_checks_v1",
    "build_safe_dry_run_execution_gate_v1",
    "validate_safe_dry_run_execution_gate_v1",
]
