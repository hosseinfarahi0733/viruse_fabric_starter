from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from viruse_fabric.safety.toy_simulation_safety_guard import (
    SafetyGuardResult,
    check_fixture_safety,
)


@dataclass(frozen=True)
class ToyFixtureCatalogEntry:
    fixture_id: str
    purpose: str
    fixture: dict[str, Any]


def _fixture_alpha_two_node() -> ToyFixtureCatalogEntry:
    return ToyFixtureCatalogEntry(
        fixture_id="toy_fixture_alpha_two_node",
        purpose="toy synthetic abstract unitless non-operational two-node graph fixture",
        fixture={
            "fixture_kind": "toy_synthetic_abstract_unitless_non-operational",
            "fixture_id": "toy_fixture_alpha_two_node",
            "seed": 188001,
            "nodes": [
                {
                    "node_id": "toy_node_alpha",
                    "compatibility": 0.20,
                    "defense": 0.70,
                    "transport_resistance": 0.40,
                    "capacity": 0.80,
                },
                {
                    "node_id": "toy_node_beta",
                    "compatibility": 0.65,
                    "defense": 0.30,
                    "transport_resistance": 0.55,
                    "capacity": 0.60,
                },
            ],
            "edges": [
                {
                    "source": "toy_node_alpha",
                    "target": "toy_node_beta",
                    "edge_weight": 0.50,
                }
            ],
            "agents": [
                {
                    "agent_id": "toy_agent_alpha",
                    "activity": 0.10,
                    "location": "toy_node_alpha",
                }
            ],
            "boundary": "toy synthetic abstract unitless non-operational only",
        },
    )


def _fixture_beta_three_node_chain() -> ToyFixtureCatalogEntry:
    return ToyFixtureCatalogEntry(
        fixture_id="toy_fixture_beta_three_node_chain",
        purpose="toy synthetic abstract unitless non-operational three-node chain fixture",
        fixture={
            "fixture_kind": "toy_synthetic_abstract_unitless_non-operational",
            "fixture_id": "toy_fixture_beta_three_node_chain",
            "seed": 188002,
            "nodes": [
                {
                    "node_id": "toy_node_1",
                    "compatibility": 0.30,
                    "defense": 0.60,
                    "transport_resistance": 0.20,
                    "capacity": 0.75,
                },
                {
                    "node_id": "toy_node_2",
                    "compatibility": 0.55,
                    "defense": 0.40,
                    "transport_resistance": 0.50,
                    "capacity": 0.65,
                },
                {
                    "node_id": "toy_node_3",
                    "compatibility": 0.80,
                    "defense": 0.25,
                    "transport_resistance": 0.70,
                    "capacity": 0.50,
                },
            ],
            "edges": [
                {
                    "source": "toy_node_1",
                    "target": "toy_node_2",
                    "edge_weight": 0.45,
                },
                {
                    "source": "toy_node_2",
                    "target": "toy_node_3",
                    "edge_weight": 0.35,
                },
            ],
            "agents": [
                {
                    "agent_id": "toy_agent_beta",
                    "activity": 0.15,
                    "location": "toy_node_1",
                }
            ],
            "boundary": "toy synthetic abstract unitless non-operational only",
        },
    )


def _fixture_gamma_star() -> ToyFixtureCatalogEntry:
    return ToyFixtureCatalogEntry(
        fixture_id="toy_fixture_gamma_star",
        purpose="toy synthetic abstract unitless non-operational star graph fixture",
        fixture={
            "fixture_kind": "toy_synthetic_abstract_unitless_non-operational",
            "fixture_id": "toy_fixture_gamma_star",
            "seed": 188003,
            "nodes": [
                {
                    "node_id": "toy_center",
                    "compatibility": 0.50,
                    "defense": 0.50,
                    "transport_resistance": 0.30,
                    "capacity": 0.70,
                },
                {
                    "node_id": "toy_leaf_a",
                    "compatibility": 0.25,
                    "defense": 0.75,
                    "transport_resistance": 0.65,
                    "capacity": 0.55,
                },
                {
                    "node_id": "toy_leaf_b",
                    "compatibility": 0.75,
                    "defense": 0.35,
                    "transport_resistance": 0.45,
                    "capacity": 0.60,
                },
            ],
            "edges": [
                {
                    "source": "toy_center",
                    "target": "toy_leaf_a",
                    "edge_weight": 0.40,
                },
                {
                    "source": "toy_center",
                    "target": "toy_leaf_b",
                    "edge_weight": 0.60,
                },
            ],
            "agents": [
                {
                    "agent_id": "toy_agent_gamma",
                    "activity": 0.20,
                    "location": "toy_center",
                }
            ],
            "boundary": "toy synthetic abstract unitless non-operational only",
        },
    )


def build_fixture_catalog() -> tuple[ToyFixtureCatalogEntry, ...]:
    return (
        _fixture_alpha_two_node(),
        _fixture_beta_three_node_chain(),
        _fixture_gamma_star(),
    )


def get_fixture_catalog_payloads() -> tuple[dict[str, Any], ...]:
    return tuple(deepcopy(entry.fixture) for entry in build_fixture_catalog())


def validate_fixture_catalog() -> tuple[SafetyGuardResult, ...]:
    return tuple(check_fixture_safety(entry.fixture) for entry in build_fixture_catalog())


def fixture_catalog_summary() -> dict[str, Any]:
    catalog = build_fixture_catalog()
    results = validate_fixture_catalog()
    return {
        "fixture_catalog_module": "viruse_fabric.safety.toy_fixture_catalog",
        "fixture_catalog_entry_count": len(catalog),
        "fixture_catalog_safe_pass_count": sum(1 for result in results if result.passed),
        "fixture_catalog_blocked_marker_count": sum(len(result.blocked_markers) for result in results),
        "fixture_catalog_missing_safe_marker_count": sum(len(result.missing_safe_markers) for result in results),
        "fixture_ids": tuple(entry.fixture_id for entry in catalog),
    }
