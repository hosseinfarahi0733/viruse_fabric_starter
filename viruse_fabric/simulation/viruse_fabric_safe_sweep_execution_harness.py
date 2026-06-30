"""Safe abstract toy sweep execution harness scaffold.

This module implements a future sweep harness structure while deliberately
refusing to execute the sweep. It prepares safe abstract toy cells, validates
them against SafeToySweepProfile, and keeps engine execution disabled.

No real biological data, pathogen model, receptor parameter, host targeting,
wet-lab protocol, infectivity optimization, immune evasion optimization, or
host range prediction is introduced.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Tuple

from viruse_fabric.simulation.viruse_fabric_minimal_safe_toy_simulation_engine import (
    SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_VERSION,
    classify_config_against_safe_sweep_profile,
)
from viruse_fabric.simulation.viruse_fabric_safe_toy_sweep_profile import (
    FORBIDDEN_BIOLOGICAL_SEMANTICS,
    SafeToySweepProfile,
    build_safe_toy_sweep_profile_v1,
)


HARNESS_VERSION = "SAFE_SWEEP_EXECUTION_HARNESS_V1"
HARNESS_SCOPE = "safe-sweep-execution-harness-implementation-no-sweep-execution"

ENGINE_VALIDATED_FIELDS: Tuple[str, ...] = (
    "node_count",
    "packet_count",
    "step_count_limit",
)


@dataclass(frozen=True)
class SafeSweepHarnessCell:
    """A declarative future sweep cell.

    The cell is a safe abstract toy execution declaration only. It is not an
    executed result.
    """

    cell_id: str
    config: Mapping[str, int]
    validation_route: str
    safe_sweep_profile_validation_passed: bool
    current_engine_default_compatible: bool
    engine_execution_allowed_now: bool = False
    sweep_execution_allowed_now: bool = False
    claim_expansion_allowed: bool = False
    real_biological_semantics_allowed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "cell_id": self.cell_id,
            "config": dict(self.config),
            "validation_route": self.validation_route,
            "safe_sweep_profile_validation_passed": self.safe_sweep_profile_validation_passed,
            "current_engine_default_compatible": self.current_engine_default_compatible,
            "engine_execution_allowed_now": self.engine_execution_allowed_now,
            "sweep_execution_allowed_now": self.sweep_execution_allowed_now,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
        }


@dataclass(frozen=True)
class SafeSweepExecutionHarness:
    """A non-executing safe sweep harness implementation."""

    harness_id: str
    profile: SafeToySweepProfile
    execution_enabled: bool = False
    engine_execution_enabled: bool = False
    sweep_execution_enabled: bool = False
    claim_expansion_allowed: bool = False
    real_biological_semantics_allowed: bool = False

    def validate_static_safety(self) -> None:
        if self.harness_id != "safe_sweep_execution_harness_v1":
            raise ValueError("Unexpected safe sweep harness id.")
        if self.execution_enabled is not False:
            raise ValueError("execution_enabled must remain False in v1.")
        if self.engine_execution_enabled is not False:
            raise ValueError("engine_execution_enabled must remain False in v1.")
        if self.sweep_execution_enabled is not False:
            raise ValueError("sweep_execution_enabled must remain False in v1.")
        if self.claim_expansion_allowed is not False:
            raise ValueError("claim_expansion_allowed must remain False.")
        if self.real_biological_semantics_allowed is not False:
            raise ValueError("real_biological_semantics_allowed must remain False.")

        self.profile.validate()

    def build_cells(self) -> List[SafeSweepHarnessCell]:
        """Build declarative future execution cells without running the engine."""

        self.validate_static_safety()
        value_map = self.profile.parameter_value_map()

        cells: List[SafeSweepHarnessCell] = []
        index = 0

        for node_count in value_map["node_count"]:
            for packet_count in value_map["packet_count"]:
                for step_count_limit in value_map["step_count_limit"]:
                    index += 1
                    config = {
                        "node_count": node_count,
                        "packet_count": packet_count,
                        "step_count_limit": step_count_limit,
                    }

                    route = classify_config_against_safe_sweep_profile(config)

                    if route["safe_sweep_profile_validation_passed"] is not True:
                        raise ValueError(f"Safe harness cell failed profile validation: {config}")
                    if route["validation_route"] not in {
                        "current_engine_default_boundary",
                        "safe_sweep_profile_validation",
                    }:
                        raise ValueError(f"Unexpected route for safe harness cell: {route}")

                    cells.append(
                        SafeSweepHarnessCell(
                            cell_id=f"SAFE-HARNESS-CELL-{index:04d}",
                            config=config,
                            validation_route=route["validation_route"],
                            safe_sweep_profile_validation_passed=route[
                                "safe_sweep_profile_validation_passed"
                            ],
                            current_engine_default_compatible=route[
                                "current_engine_default_compatible"
                            ],
                        )
                    )

        return cells

    def build_manifest(self, preview_cell_count: int = 12) -> Dict[str, Any]:
        """Build a non-executing harness manifest."""

        cells = self.build_cells()
        route_counts = {
            "current_engine_default_boundary": 0,
            "safe_sweep_profile_validation": 0,
            "outside_safe_sweep_profile": 0,
        }

        for cell in cells:
            route_counts[cell.validation_route] += 1

        manifest = {
            "harness_id": self.harness_id,
            "harness_version": HARNESS_VERSION,
            "scope": HARNESS_SCOPE,
            "validation_route_version": SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_VERSION,
            "profile_id": self.profile.profile_id,
            "engine_validated_field_count": len(ENGINE_VALIDATED_FIELDS),
            "cell_count": len(cells),
            "route_counts": route_counts,
            "preview_cell_count": min(preview_cell_count, len(cells)),
            "preview_cells": [
                cell.to_dict() for cell in cells[:preview_cell_count]
            ],
            "execution_enabled": self.execution_enabled,
            "engine_execution_enabled": self.engine_execution_enabled,
            "sweep_execution_enabled": self.sweep_execution_enabled,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
            "forbidden_semantics": list(FORBIDDEN_BIOLOGICAL_SEMANTICS),
            "safe_abstract_toy_only": True,
            "interpretation_boundary": "internal_toy_harness_manifest_only",
        }

        validate_harness_manifest(manifest)
        return manifest

    def run_sweep(self) -> None:
        """Explicitly refuse execution in v1."""

        raise RuntimeError(
            "SafeSweepExecutionHarness v1 is non-executing. "
            "Sweep execution is forbidden by this artifact."
        )


def build_safe_sweep_execution_harness_v1() -> SafeSweepExecutionHarness:
    profile = build_safe_toy_sweep_profile_v1()
    harness = SafeSweepExecutionHarness(
        harness_id="safe_sweep_execution_harness_v1",
        profile=profile,
    )
    harness.validate_static_safety()
    return harness


def build_safe_sweep_execution_harness_manifest_v1(
    preview_cell_count: int = 12,
) -> Dict[str, Any]:
    harness = build_safe_sweep_execution_harness_v1()
    return harness.build_manifest(preview_cell_count=preview_cell_count)


def validate_harness_manifest(manifest: Mapping[str, Any]) -> None:
    if manifest["harness_version"] != HARNESS_VERSION:
        raise ValueError("Unexpected harness version.")
    if manifest["scope"] != HARNESS_SCOPE:
        raise ValueError("Unexpected harness scope.")
    if manifest["validation_route_version"] != "SAFE_SWEEP_PROFILE_VALIDATION_ROUTE_V1":
        raise ValueError("Unexpected validation route version.")
    if manifest["cell_count"] != 64:
        raise ValueError("Expected 64 engine-validated safe harness cells.")
    if manifest["route_counts"] != {
        "current_engine_default_boundary": 1,
        "safe_sweep_profile_validation": 63,
        "outside_safe_sweep_profile": 0,
    }:
        raise ValueError(f"Unexpected route counts: {manifest['route_counts']}")

    must_be_false = [
        "execution_enabled",
        "engine_execution_enabled",
        "sweep_execution_enabled",
        "claim_expansion_allowed",
        "real_biological_semantics_allowed",
    ]
    for key in must_be_false:
        if manifest[key] is not False:
            raise ValueError(f"{key} must be False.")

    if manifest["safe_abstract_toy_only"] is not True:
        raise ValueError("safe_abstract_toy_only must be True.")


__all__ = [
    "HARNESS_VERSION",
    "HARNESS_SCOPE",
    "SafeSweepHarnessCell",
    "SafeSweepExecutionHarness",
    "build_safe_sweep_execution_harness_v1",
    "build_safe_sweep_execution_harness_manifest_v1",
    "validate_harness_manifest",
]
