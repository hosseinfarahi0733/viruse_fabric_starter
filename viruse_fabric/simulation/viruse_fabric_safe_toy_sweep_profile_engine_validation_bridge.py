"""Bridge SafeToySweepProfile declarations to current engine validation boundaries.

This module does not modify the engine and does not execute experiments. It
classifies SafeToySweepProfile values against the current v9.1-style fixed
default boundary so that a later checked commit can safely separate default
validation from sweep-profile validation.

Safe abstract toy only. No biological semantics are introduced.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Any, Dict, List, Mapping, Tuple

from viruse_fabric.simulation.viruse_fabric_safe_toy_sweep_profile import (
    FORBIDDEN_BIOLOGICAL_SEMANTICS,
    SafeToySweepProfile,
    build_safe_toy_sweep_profile_v1,
)


V9_1_DEFAULT_ENGINE_VALUES: Mapping[str, int] = {
    "node_count": 16,
    "packet_count": 32,
    "step_count_limit": 3,
}

ENGINE_VALIDATED_PARAMETER_NAMES: Tuple[str, ...] = (
    "node_count",
    "packet_count",
    "step_count_limit",
)


@dataclass(frozen=True)
class SafeProfileEngineValidationBridgeResult:
    """Serializable result for profile-to-engine validation bridge checks."""

    profile_id: str
    scope: str
    bridge_scope: str
    engine_modified: bool
    experiment_executed: bool
    claim_expansion_allowed: bool
    profile_parameter_count: int
    engine_validated_parameter_count: int
    baseline_compatible_cell_count: int
    sweep_profile_cell_count: int
    sweep_only_cell_count: int
    default_value_map: Dict[str, int]
    engine_validated_parameter_values: Dict[str, Tuple[int, ...]]
    sweep_only_values_by_parameter: Dict[str, Tuple[int, ...]]
    bridge_records_preview: List[Dict[str, Any]]
    forbidden_semantics: Tuple[str, ...]
    next_allowed_action: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "profile_id": self.profile_id,
            "scope": self.scope,
            "bridge_scope": self.bridge_scope,
            "engine_modified": self.engine_modified,
            "experiment_executed": self.experiment_executed,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "profile_parameter_count": self.profile_parameter_count,
            "engine_validated_parameter_count": self.engine_validated_parameter_count,
            "baseline_compatible_cell_count": self.baseline_compatible_cell_count,
            "sweep_profile_cell_count": self.sweep_profile_cell_count,
            "sweep_only_cell_count": self.sweep_only_cell_count,
            "default_value_map": dict(self.default_value_map),
            "engine_validated_parameter_values": {
                key: list(value) for key, value in self.engine_validated_parameter_values.items()
            },
            "sweep_only_values_by_parameter": {
                key: list(value) for key, value in self.sweep_only_values_by_parameter.items()
            },
            "bridge_records_preview": list(self.bridge_records_preview),
            "forbidden_semantics": list(self.forbidden_semantics),
            "next_allowed_action": self.next_allowed_action,
        }


def _parameter_value_map(profile: SafeToySweepProfile) -> Dict[str, Tuple[int, ...]]:
    return profile.parameter_value_map()


def _validate_default_values_present(profile: SafeToySweepProfile) -> None:
    value_map = _parameter_value_map(profile)

    for name, default_value in V9_1_DEFAULT_ENGINE_VALUES.items():
        if name not in value_map:
            raise ValueError(f"Missing engine validated parameter in profile: {name}")
        if default_value not in value_map[name]:
            raise ValueError(f"Default value {default_value} for {name} is absent from safe sweep profile.")


def _engine_parameter_grid(profile: SafeToySweepProfile) -> List[Dict[str, int]]:
    value_map = _parameter_value_map(profile)
    values = [value_map[name] for name in ENGINE_VALIDATED_PARAMETER_NAMES]

    records: List[Dict[str, int]] = []
    for combo in product(*values):
        records.append(dict(zip(ENGINE_VALIDATED_PARAMETER_NAMES, combo)))

    return records


def classify_profile_against_current_engine_boundary(
    profile: SafeToySweepProfile | None = None,
    preview_record_count: int = 12,
) -> SafeProfileEngineValidationBridgeResult:
    """Classify safe sweep profile cells against current fixed engine defaults.

    Baseline-compatible cells match the current v9.1 default boundary exactly.
    Sweep-only cells are safe abstract toy declarations that require a separate
    future validation path before they can be executed by the engine.
    """

    profile = profile or build_safe_toy_sweep_profile_v1()
    profile.validate()
    _validate_default_values_present(profile)

    value_map = _parameter_value_map(profile)
    engine_value_map = {
        name: value_map[name] for name in ENGINE_VALIDATED_PARAMETER_NAMES
    }

    sweep_only_values_by_parameter = {
        name: tuple(value for value in values if value != V9_1_DEFAULT_ENGINE_VALUES[name])
        for name, values in engine_value_map.items()
    }

    grid = _engine_parameter_grid(profile)
    bridge_records: List[Dict[str, Any]] = []

    baseline_compatible_cell_count = 0
    sweep_only_cell_count = 0

    for index, values in enumerate(grid, start=1):
        is_baseline_compatible = all(
            values[name] == V9_1_DEFAULT_ENGINE_VALUES[name]
            for name in ENGINE_VALIDATED_PARAMETER_NAMES
        )

        if is_baseline_compatible:
            baseline_compatible_cell_count += 1
            validation_route = "current_engine_default_boundary"
        else:
            sweep_only_cell_count += 1
            validation_route = "future_safe_sweep_profile_validation_required"

        bridge_records.append(
            {
                "record_id": f"ENGINE-BRIDGE-CELL-{index:04d}",
                "engine_parameter_values": values,
                "baseline_compatible": is_baseline_compatible,
                "validation_route": validation_route,
                "safe_abstract_toy_only": True,
                "claim_expansion_allowed": False,
                "real_biological_semantics_allowed": False,
            }
        )

    if baseline_compatible_cell_count != 1:
        raise ValueError("Expected exactly one baseline-compatible current-engine cell.")

    if sweep_only_cell_count <= 0:
        raise ValueError("Expected at least one sweep-only cell requiring future validation.")

    return SafeProfileEngineValidationBridgeResult(
        profile_id=profile.profile_id,
        scope=profile.scope,
        bridge_scope="safe-profile-to-current-engine-validation-boundary-bridge-only",
        engine_modified=False,
        experiment_executed=False,
        claim_expansion_allowed=False,
        profile_parameter_count=len(profile.parameters),
        engine_validated_parameter_count=len(ENGINE_VALIDATED_PARAMETER_NAMES),
        baseline_compatible_cell_count=baseline_compatible_cell_count,
        sweep_profile_cell_count=len(grid),
        sweep_only_cell_count=sweep_only_cell_count,
        default_value_map=dict(V9_1_DEFAULT_ENGINE_VALUES),
        engine_validated_parameter_values=engine_value_map,
        sweep_only_values_by_parameter=sweep_only_values_by_parameter,
        bridge_records_preview=bridge_records[:preview_record_count],
        forbidden_semantics=FORBIDDEN_BIOLOGICAL_SEMANTICS,
        next_allowed_action="modify_engine_validation_to_accept_safe_sweep_profile_on_separate_checked_commit",
    )


def build_validation_bridge_summary_v1(preview_record_count: int = 12) -> Dict[str, Any]:
    """Build a JSON-serializable validation bridge summary."""

    result = classify_profile_against_current_engine_boundary(
        preview_record_count=preview_record_count
    )
    return result.to_dict()


__all__ = [
    "V9_1_DEFAULT_ENGINE_VALUES",
    "ENGINE_VALIDATED_PARAMETER_NAMES",
    "SafeProfileEngineValidationBridgeResult",
    "classify_profile_against_current_engine_boundary",
    "build_validation_bridge_summary_v1",
]
