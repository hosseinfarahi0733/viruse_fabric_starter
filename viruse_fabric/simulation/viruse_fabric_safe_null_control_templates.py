"""Safe abstract toy null-control templates for the non-executing harness.

This module defines null-control templates and planned cell-control pairings.
It does not execute the harness, does not execute the engine, and does not run
a sweep. The templates are abstract toy controls only.

No real biological data, pathogen model, receptor parameter, host targeting,
wet-lab protocol, infectivity optimization, immune evasion optimization, or
host range prediction is introduced.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Tuple

from viruse_fabric.simulation.viruse_fabric_safe_sweep_execution_harness import (
    HARNESS_VERSION,
    build_safe_sweep_execution_harness_manifest_v1,
)


NULL_CONTROL_TEMPLATE_VERSION = "SAFE_NULL_CONTROL_TEMPLATES_V1"
NULL_CONTROL_TEMPLATE_SCOPE = "safe-null-control-templates-no-sweep-execution"


@dataclass(frozen=True)
class SafeNullControlTemplate:
    """A declarative null-control template for future safe toy harness checks."""

    template_id: str
    control_family: str
    allowed_abstract_transformation: str
    expected_abstract_leak_count: int
    forbidden_interpretation: str
    execution_enabled_now: bool = False
    engine_execution_enabled_now: bool = False
    sweep_execution_enabled_now: bool = False
    claim_expansion_allowed: bool = False
    real_biological_semantics_allowed: bool = False

    def validate(self) -> None:
        if not self.template_id.startswith("SAFE-NULL-"):
            raise ValueError(f"Unexpected null-control template id: {self.template_id}")
        if not self.control_family:
            raise ValueError(f"{self.template_id}: control_family must be non-empty.")
        if "abstract" not in self.allowed_abstract_transformation.lower():
            raise ValueError(
                f"{self.template_id}: transformation must remain explicitly abstract."
            )
        if self.expected_abstract_leak_count != 0:
            raise ValueError(
                f"{self.template_id}: expected_abstract_leak_count must be zero."
            )
        if "biological" not in self.forbidden_interpretation.lower():
            raise ValueError(
                f"{self.template_id}: forbidden interpretation must reject biological meaning."
            )

        must_be_false = {
            "execution_enabled_now": self.execution_enabled_now,
            "engine_execution_enabled_now": self.engine_execution_enabled_now,
            "sweep_execution_enabled_now": self.sweep_execution_enabled_now,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
        }
        bad = {key: value for key, value in must_be_false.items() if value is not False}
        if bad:
            raise ValueError(f"{self.template_id}: forbidden True flags: {bad}")

    def to_dict(self) -> Dict[str, Any]:
        self.validate()
        return {
            "template_id": self.template_id,
            "control_family": self.control_family,
            "allowed_abstract_transformation": self.allowed_abstract_transformation,
            "expected_abstract_leak_count": self.expected_abstract_leak_count,
            "forbidden_interpretation": self.forbidden_interpretation,
            "execution_enabled_now": self.execution_enabled_now,
            "engine_execution_enabled_now": self.engine_execution_enabled_now,
            "sweep_execution_enabled_now": self.sweep_execution_enabled_now,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
        }


def build_safe_null_control_templates_v1() -> Tuple[SafeNullControlTemplate, ...]:
    """Build the v1 declarative null-control template registry."""

    templates = (
        SafeNullControlTemplate(
            template_id="SAFE-NULL-LEDGER-DISABLED",
            control_family="abstract-ledger-ablation",
            allowed_abstract_transformation="abstract removal of memory-ledger contribution from future toy scoring",
            expected_abstract_leak_count=0,
            forbidden_interpretation="not a biological pathway, immune mechanism, pathogen feature, or host response",
        ),
        SafeNullControlTemplate(
            template_id="SAFE-NULL-ROUTE-LABEL-SHUFFLE",
            control_family="abstract-route-label-randomization",
            allowed_abstract_transformation="abstract shuffle of route labels before future toy scoring",
            expected_abstract_leak_count=0,
            forbidden_interpretation="not a biological transmission route, exposure route, or host-targeting route",
        ),
        SafeNullControlTemplate(
            template_id="SAFE-NULL-SYMBOLIC-DRIFT-FROZEN",
            control_family="abstract-symbolic-drift-freeze",
            allowed_abstract_transformation="abstract freeze of symbolic drift field before future toy scoring",
            expected_abstract_leak_count=0,
            forbidden_interpretation="not biological antigenic drift, biological mutation, immune evasion, viral adaptation, or any biological process",
        ),
        SafeNullControlTemplate(
            template_id="SAFE-NULL-PACKET-ORDER-PERMUTED",
            control_family="abstract-packet-order-permutation",
            allowed_abstract_transformation="abstract permutation of packet order before future toy scoring",
            expected_abstract_leak_count=0,
            forbidden_interpretation="not viral load, dose order, biological exposure sequence, or pathogen process",
        ),
    )

    for template in templates:
        template.validate()

    return templates


def build_safe_null_control_manifest_v1(preview_pair_count: int = 16) -> Dict[str, Any]:
    """Build a non-executing null-control manifest for future safe harness use."""

    harness_manifest = build_safe_sweep_execution_harness_manifest_v1(
        preview_cell_count=64
    )
    templates = build_safe_null_control_templates_v1()

    pair_records: List[Dict[str, Any]] = []
    index = 0

    for cell in harness_manifest["preview_cells"]:
        for template in templates:
            index += 1
            pair_records.append(
                {
                    "pair_id": f"SAFE-NULL-PAIR-{index:04d}",
                    "cell_id": cell["cell_id"],
                    "template_id": template.template_id,
                    "cell_validation_route": cell["validation_route"],
                    "planned_only": True,
                    "execution_enabled_now": False,
                    "engine_execution_enabled_now": False,
                    "sweep_execution_enabled_now": False,
                    "expected_abstract_leak_count": template.expected_abstract_leak_count,
                    "claim_expansion_allowed": False,
                    "real_biological_semantics_allowed": False,
                }
            )

    manifest = {
        "template_version": NULL_CONTROL_TEMPLATE_VERSION,
        "scope": NULL_CONTROL_TEMPLATE_SCOPE,
        "harness_version": HARNESS_VERSION,
        "harness_cell_count": harness_manifest["cell_count"],
        "template_count": len(templates),
        "planned_pair_count": len(pair_records),
        "preview_pair_count": min(preview_pair_count, len(pair_records)),
        "templates": [template.to_dict() for template in templates],
        "preview_pairs": pair_records[:preview_pair_count],
        "planned_expected_total_abstract_leak_count": sum(
            pair["expected_abstract_leak_count"] for pair in pair_records
        ),
        "execution_enabled_now": False,
        "engine_execution_enabled_now": False,
        "sweep_execution_enabled_now": False,
        "claim_expansion_allowed": False,
        "real_biological_semantics_allowed": False,
        "safe_abstract_toy_only": True,
        "interpretation_boundary": "planned_null_controls_only_no_execution",
    }

    validate_safe_null_control_manifest_v1(manifest)
    return manifest


def validate_safe_null_control_manifest_v1(manifest: Mapping[str, Any]) -> None:
    if manifest["template_version"] != NULL_CONTROL_TEMPLATE_VERSION:
        raise ValueError("Unexpected null-control template version.")
    if manifest["scope"] != NULL_CONTROL_TEMPLATE_SCOPE:
        raise ValueError("Unexpected null-control template scope.")
    if manifest["harness_version"] != "SAFE_SWEEP_EXECUTION_HARNESS_V1":
        raise ValueError("Unexpected harness version.")
    if manifest["harness_cell_count"] != 64:
        raise ValueError("Expected 64 harness cells.")
    if manifest["template_count"] != 4:
        raise ValueError("Expected 4 null-control templates.")
    if manifest["planned_pair_count"] != 64 * 4:
        raise ValueError("Expected 256 planned null-control pairs.")
    if manifest["planned_expected_total_abstract_leak_count"] != 0:
        raise ValueError("Expected planned leak count must be zero.")

    must_be_false = [
        "execution_enabled_now",
        "engine_execution_enabled_now",
        "sweep_execution_enabled_now",
        "claim_expansion_allowed",
        "real_biological_semantics_allowed",
    ]
    for key in must_be_false:
        if manifest[key] is not False:
            raise ValueError(f"{key} must be False.")

    if manifest["safe_abstract_toy_only"] is not True:
        raise ValueError("safe_abstract_toy_only must be True.")


__all__ = [
    "NULL_CONTROL_TEMPLATE_VERSION",
    "NULL_CONTROL_TEMPLATE_SCOPE",
    "SafeNullControlTemplate",
    "build_safe_null_control_templates_v1",
    "build_safe_null_control_manifest_v1",
    "validate_safe_null_control_manifest_v1",
]
