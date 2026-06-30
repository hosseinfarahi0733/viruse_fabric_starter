"""Safe dry-run manifest builder.

This module builds a dry-run manifest for future safe abstract toy checks. It
does not execute a dry-run, does not execute the engine, does not run a sweep,
and does not execute null controls.

No real biological dataset, pathogen model, receptor parameter, host targeting,
wet-lab protocol, infectivity optimization, immune evasion optimization, or
host range prediction is introduced.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Tuple

from viruse_fabric.simulation.viruse_fabric_safe_null_control_templates import (
    NULL_CONTROL_TEMPLATE_VERSION,
    build_safe_null_control_manifest_v1,
)
from viruse_fabric.simulation.viruse_fabric_safe_sweep_execution_harness import (
    HARNESS_VERSION,
    build_safe_sweep_execution_harness_manifest_v1,
)


SAFE_DRY_RUN_MANIFEST_BUILDER_VERSION = "SAFE_DRY_RUN_MANIFEST_BUILDER_V1"
SAFE_DRY_RUN_MANIFEST_BUILDER_SCOPE = (
    "safe-dry-run-manifest-builder-no-engine-or-sweep-execution"
)


@dataclass(frozen=True)
class SafeDryRunManifestBuilder:
    """Builds dry-run metadata only."""

    builder_id: str = "safe_dry_run_manifest_builder_v1"
    dry_run_execution_enabled: bool = False
    engine_execution_enabled: bool = False
    sweep_execution_enabled: bool = False
    null_control_execution_enabled: bool = False
    claim_expansion_allowed: bool = False
    real_biological_semantics_allowed: bool = False

    def validate_static_safety(self) -> None:
        if self.builder_id != "safe_dry_run_manifest_builder_v1":
            raise ValueError("Unexpected builder id.")

        must_be_false = {
            "dry_run_execution_enabled": self.dry_run_execution_enabled,
            "engine_execution_enabled": self.engine_execution_enabled,
            "sweep_execution_enabled": self.sweep_execution_enabled,
            "null_control_execution_enabled": self.null_control_execution_enabled,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
        }

        bad = {key: value for key, value in must_be_false.items() if value is not False}
        if bad:
            raise ValueError(f"Forbidden enabled flags in manifest builder: {bad}")

    def build_manifest(self, preview_cell_count: int = 12, preview_pair_count: int = 16) -> Dict[str, Any]:
        """Build a dry-run manifest without executing anything."""

        self.validate_static_safety()

        harness_manifest = build_safe_sweep_execution_harness_manifest_v1(
            preview_cell_count=64
        )
        null_manifest = build_safe_null_control_manifest_v1(
            preview_pair_count=preview_pair_count
        )

        route_counts = harness_manifest["route_counts"]
        pair_template_ids = sorted(
            {pair["template_id"] for pair in null_manifest["preview_pairs"]}
        )

        manifest = {
            "builder_version": SAFE_DRY_RUN_MANIFEST_BUILDER_VERSION,
            "scope": SAFE_DRY_RUN_MANIFEST_BUILDER_SCOPE,
            "builder_id": self.builder_id,
            "harness_version": HARNESS_VERSION,
            "null_control_template_version": NULL_CONTROL_TEMPLATE_VERSION,
            "cell_count": harness_manifest["cell_count"],
            "route_counts": route_counts,
            "template_count": null_manifest["template_count"],
            "planned_null_control_pair_count": null_manifest["planned_pair_count"],
            "planned_expected_total_abstract_leak_count": null_manifest[
                "planned_expected_total_abstract_leak_count"
            ],
            "preview_cell_count": min(preview_cell_count, harness_manifest["cell_count"]),
            "preview_pair_count": null_manifest["preview_pair_count"],
            "preview_cells": harness_manifest["preview_cells"][:preview_cell_count],
            "preview_pairs": null_manifest["preview_pairs"][:preview_pair_count],
            "preview_pair_template_ids": pair_template_ids,
            "dry_run_execution_enabled": self.dry_run_execution_enabled,
            "engine_execution_enabled": self.engine_execution_enabled,
            "sweep_execution_enabled": self.sweep_execution_enabled,
            "null_control_execution_enabled": self.null_control_execution_enabled,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
            "safe_abstract_toy_only": True,
            "interpretation_boundary": "dry_run_manifest_metadata_only_not_evidence",
        }

        validate_safe_dry_run_manifest_v1(manifest)
        return manifest


def build_safe_dry_run_manifest_builder_v1() -> SafeDryRunManifestBuilder:
    builder = SafeDryRunManifestBuilder()
    builder.validate_static_safety()
    return builder


def build_safe_dry_run_manifest_v1(
    preview_cell_count: int = 12,
    preview_pair_count: int = 16,
) -> Dict[str, Any]:
    builder = build_safe_dry_run_manifest_builder_v1()
    return builder.build_manifest(
        preview_cell_count=preview_cell_count,
        preview_pair_count=preview_pair_count,
    )


def validate_safe_dry_run_manifest_v1(manifest: Mapping[str, Any]) -> None:
    if manifest["builder_version"] != SAFE_DRY_RUN_MANIFEST_BUILDER_VERSION:
        raise ValueError("Unexpected dry-run manifest builder version.")
    if manifest["scope"] != SAFE_DRY_RUN_MANIFEST_BUILDER_SCOPE:
        raise ValueError("Unexpected dry-run manifest builder scope.")
    if manifest["harness_version"] != "SAFE_SWEEP_EXECUTION_HARNESS_V1":
        raise ValueError("Unexpected harness version.")
    if manifest["null_control_template_version"] != "SAFE_NULL_CONTROL_TEMPLATES_V1":
        raise ValueError("Unexpected null-control template version.")
    if manifest["cell_count"] != 64:
        raise ValueError("Expected 64 dry-run manifest cells.")
    if manifest["template_count"] != 4:
        raise ValueError("Expected 4 null-control templates.")
    if manifest["planned_null_control_pair_count"] != 256:
        raise ValueError("Expected 256 planned null-control pairs.")
    if manifest["planned_expected_total_abstract_leak_count"] != 0:
        raise ValueError("Expected planned total abstract leak count to be zero.")
    if manifest["route_counts"] != {
        "current_engine_default_boundary": 1,
        "safe_sweep_profile_validation": 63,
        "outside_safe_sweep_profile": 0,
    }:
        raise ValueError(f"Unexpected route counts: {manifest['route_counts']}")

    must_be_false = [
        "dry_run_execution_enabled",
        "engine_execution_enabled",
        "sweep_execution_enabled",
        "null_control_execution_enabled",
        "claim_expansion_allowed",
        "real_biological_semantics_allowed",
    ]

    for key in must_be_false:
        if manifest[key] is not False:
            raise ValueError(f"{key} must be False.")

    if manifest["safe_abstract_toy_only"] is not True:
        raise ValueError("safe_abstract_toy_only must be True.")
    if manifest["interpretation_boundary"] != "dry_run_manifest_metadata_only_not_evidence":
        raise ValueError("Unexpected interpretation boundary.")


__all__ = [
    "SAFE_DRY_RUN_MANIFEST_BUILDER_VERSION",
    "SAFE_DRY_RUN_MANIFEST_BUILDER_SCOPE",
    "SafeDryRunManifestBuilder",
    "build_safe_dry_run_manifest_builder_v1",
    "build_safe_dry_run_manifest_v1",
    "validate_safe_dry_run_manifest_v1",
]
