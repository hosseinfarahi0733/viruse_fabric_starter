"""Safe abstract toy sweep profile scaffold for Viruse Fabric.

This module defines bounded safe toy sweep profiles only. It does not run
real biological simulations, does not introduce pathogen models, and does not
encode receptor, host, wet-lab, infectivity, immune-evasion, or host-range
semantics.

The purpose is to separate safe abstract toy sweep declarations from the fixed
v9.1 default configuration boundary discovered by the v9.8 decision gate.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple


FORBIDDEN_BIOLOGICAL_SEMANTICS: Tuple[str, ...] = (
    "real biological dataset",
    "real pathogen model",
    "receptor parameter",
    "operational host targeting",
    "wet-lab protocol",
    "infectivity optimization",
    "immune evasion optimization",
    "host range prediction",
)


@dataclass(frozen=True)
class SafeToyParameterDefinition:
    """A single safe abstract toy sweep parameter definition."""

    name: str
    allowed_role: str
    must_not_mean: str
    values: Tuple[int, ...]
    requires_engine_support: bool

    def validate(self) -> None:
        if not self.name:
            raise ValueError("Safe toy parameter name must be non-empty.")
        if not self.allowed_role:
            raise ValueError(f"{self.name}: allowed_role must be non-empty.")
        if not self.must_not_mean:
            raise ValueError(f"{self.name}: must_not_mean must be non-empty.")
        if not self.values:
            raise ValueError(f"{self.name}: values must be non-empty.")
        if any(not isinstance(value, int) for value in self.values):
            raise TypeError(f"{self.name}: all values must be integers.")
        if any(value <= 0 for value in self.values):
            raise ValueError(f"{self.name}: all values must be positive.")
        if len(set(self.values)) != len(self.values):
            raise ValueError(f"{self.name}: values must be unique.")
        if "abstract" not in self.allowed_role.lower():
            raise ValueError(f"{self.name}: allowed_role must explicitly remain abstract.")
        forbidden_hint = self.must_not_mean.lower()
        if not any(token in forbidden_hint for token in ("biological", "host", "pathogen", "receptor", "wet-lab", "infectivity", "immune", "range", "viral")):
            raise ValueError(f"{self.name}: must_not_mean must explicitly prohibit biological interpretation.")


@dataclass(frozen=True)
class SafeToySweepProfile:
    """A bounded safe abstract toy sweep profile.

    The profile is intentionally declarative. It does not modify the existing
    engine and does not execute experiments. Future implementation work can
    adapt the engine to consume this profile.
    """

    profile_id: str
    scope: str
    parameters: Tuple[SafeToyParameterDefinition, ...]
    fixed_seed_fields: Mapping[str, Tuple[int, ...]] = field(default_factory=dict)
    forbidden_semantics: Tuple[str, ...] = FORBIDDEN_BIOLOGICAL_SEMANTICS
    claim_expansion_allowed: bool = False
    real_biological_semantics_allowed: bool = False

    def validate(self) -> None:
        if self.profile_id != "safe_toy_sweep_profile_v1":
            raise ValueError("Unexpected profile_id.")
        if self.scope != "safe-abstract-toy-sweep-profile-only":
            raise ValueError("Unexpected safe toy sweep profile scope.")
        if self.claim_expansion_allowed is not False:
            raise ValueError("claim_expansion_allowed must remain False.")
        if self.real_biological_semantics_allowed is not False:
            raise ValueError("real_biological_semantics_allowed must remain False.")
        if len(self.parameters) != 7:
            raise ValueError("Expected exactly 7 safe toy parameter definitions.")

        names = [param.name for param in self.parameters]
        if len(set(names)) != len(names):
            raise ValueError("Safe toy parameter names must be unique.")

        for param in self.parameters:
            param.validate()

        required_names = {
            "node_count",
            "packet_count",
            "step_count_limit",
            "graph_seed",
            "packet_seed",
            "transition_seed",
            "symbolic_drift_seed",
        }
        if set(names) != required_names:
            raise ValueError(f"Unexpected parameter registry: {names}")

        for forbidden in self.forbidden_semantics:
            if not forbidden:
                raise ValueError("Forbidden semantics entries must be non-empty.")

    def engine_supported_parameter_names(self) -> Tuple[str, ...]:
        return tuple(param.name for param in self.parameters if param.requires_engine_support)

    def seed_parameter_names(self) -> Tuple[str, ...]:
        return tuple(param.name for param in self.parameters if not param.requires_engine_support)

    def parameter_value_map(self) -> Dict[str, Tuple[int, ...]]:
        return {param.name: param.values for param in self.parameters}

    def materialize_grid_records(self, max_records: int | None = None) -> List[Dict[str, Any]]:
        """Return safe abstract toy sweep grid records.

        These are declarative records, not engine runs.
        """

        self.validate()

        value_map = self.parameter_value_map()
        ordered_names = tuple(value_map.keys())
        records: List[Dict[str, Any]] = []

        for index, values in enumerate(product(*(value_map[name] for name in ordered_names)), start=1):
            record = {
                "record_id": f"SAFE-SWEEP-CELL-{index:04d}",
                "scope": self.scope,
                "claim_expansion_allowed": False,
                "real_biological_semantics_allowed": False,
                "parameter_values": dict(zip(ordered_names, values)),
                "forbidden_semantics": list(self.forbidden_semantics),
            }
            records.append(record)
            if max_records is not None and len(records) >= max_records:
                break

        return records

    def summarize(self, preview_record_count: int = 8) -> Dict[str, Any]:
        self.validate()
        value_map = self.parameter_value_map()
        total_grid_cell_count = 1
        for values in value_map.values():
            total_grid_cell_count *= len(values)

        preview_records = self.materialize_grid_records(max_records=preview_record_count)

        return {
            "profile_id": self.profile_id,
            "scope": self.scope,
            "parameter_count": len(self.parameters),
            "engine_supported_parameter_count": len(self.engine_supported_parameter_names()),
            "seed_parameter_count": len(self.seed_parameter_names()),
            "total_grid_cell_count": total_grid_cell_count,
            "preview_record_count": len(preview_records),
            "preview_records": preview_records,
            "claim_expansion_allowed": self.claim_expansion_allowed,
            "real_biological_semantics_allowed": self.real_biological_semantics_allowed,
            "forbidden_semantics": list(self.forbidden_semantics),
        }


def build_safe_toy_sweep_profile_v1() -> SafeToySweepProfile:
    """Build the v1 safe abstract toy sweep profile."""

    profile = SafeToySweepProfile(
        profile_id="safe_toy_sweep_profile_v1",
        scope="safe-abstract-toy-sweep-profile-only",
        parameters=(
            SafeToyParameterDefinition(
                name="node_count",
                allowed_role="abstract toy graph size only",
                must_not_mean="host count, cell count, organism count, population count, or biological entity count",
                values=(12, 16, 20, 24),
                requires_engine_support=True,
            ),
            SafeToyParameterDefinition(
                name="packet_count",
                allowed_role="abstract toy packet volume only",
                must_not_mean="viral load, dose, infection count, particle count, or biological exposure",
                values=(24, 32, 40, 48),
                requires_engine_support=True,
            ),
            SafeToyParameterDefinition(
                name="step_count_limit",
                allowed_role="abstract discrete iteration count only",
                must_not_mean="incubation time, replication cycle, disease progression time, or biological time",
                values=(2, 3, 4, 5),
                requires_engine_support=True,
            ),
            SafeToyParameterDefinition(
                name="graph_seed",
                allowed_role="abstract randomization seed only",
                must_not_mean="environment, lineage, strain, host type, or empirical biological scenario",
                values=(101, 111, 121, 131),
                requires_engine_support=False,
            ),
            SafeToyParameterDefinition(
                name="packet_seed",
                allowed_role="abstract packet initialization seed only",
                must_not_mean="exposure route, sample source, patient group, or biological sampling",
                values=(202, 212, 222, 232),
                requires_engine_support=False,
            ),
            SafeToyParameterDefinition(
                name="transition_seed",
                allowed_role="abstract transition randomization seed only",
                must_not_mean="mutation process, transmission process, replication mechanism, or biological pathway",
                values=(303, 313, 323, 333),
                requires_engine_support=False,
            ),
            SafeToyParameterDefinition(
                name="symbolic_drift_seed",
                allowed_role="abstract symbolic drift randomization seed only",
                must_not_mean="immune evasion, antigenic drift, host adaptation, or biological mutation",
                values=(404, 414, 424, 434),
                requires_engine_support=False,
            ),
        ),
    )
    profile.validate()
    return profile


def build_profile_summary_v1(preview_record_count: int = 8) -> Dict[str, Any]:
    """Build a serializable profile summary for reporting."""

    profile = build_safe_toy_sweep_profile_v1()
    return profile.summarize(preview_record_count=preview_record_count)


__all__ = [
    "FORBIDDEN_BIOLOGICAL_SEMANTICS",
    "SafeToyParameterDefinition",
    "SafeToySweepProfile",
    "build_safe_toy_sweep_profile_v1",
    "build_profile_summary_v1",
]
