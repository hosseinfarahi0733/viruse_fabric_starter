from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


PROHIBITED_CATEGORY_MARKERS: tuple[str, ...] = (
    "real_pathogen_identity",
    "real_pathogen_parameter",
    "real_receptor_identity",
    "real_receptor_parameter",
    "operational_host_targeting",
    "wet_lab_protocol",
    "actionable_biosafety_risk_instruction",
    "real_world_infectivity_optimization",
    "immune_evasion_optimization",
    "real_host_range_prediction",
    "real_biological_dataset_import",
)

PROHIBITED_PHRASE_MARKERS: tuple[str, ...] = (
    "host-targeting objective enabled",
    "operational host targeting recipe",
    "specific pathogen optimization",
    "wet-lab protocol steps",
    "increase real-world infectivity",
    "evade real-world immunity",
    "real receptor parameterization enabled",
    "real biological dataset import enabled",
)

REQUIRED_SAFE_MARKERS: tuple[str, ...] = (
    "toy",
    "synthetic",
    "abstract",
    "unitless",
    "non-operational",
)


@dataclass(frozen=True)
class SafetyGuardResult:
    passed: bool
    blocked_markers: tuple[str, ...]
    missing_safe_markers: tuple[str, ...]
    checked_text_length: int


def normalize_text(text: str) -> str:
    return " ".join(text.lower().replace("_", " ").split())


def _contains_marker(normalized_text: str, marker: str) -> bool:
    normalized_marker = normalize_text(marker)
    return normalized_marker in normalized_text


def check_text_safety(text: str, require_safe_markers: bool = True) -> SafetyGuardResult:
    normalized = normalize_text(text)

    blocked: list[str] = []
    for marker in PROHIBITED_CATEGORY_MARKERS + PROHIBITED_PHRASE_MARKERS:
        if _contains_marker(normalized, marker):
            blocked.append(marker)

    missing_safe: list[str] = []
    if require_safe_markers:
        for marker in REQUIRED_SAFE_MARKERS:
            if marker not in normalized:
                missing_safe.append(marker)

    return SafetyGuardResult(
        passed=(not blocked and not missing_safe),
        blocked_markers=tuple(blocked),
        missing_safe_markers=tuple(missing_safe),
        checked_text_length=len(text),
    )


def assert_text_safe(text: str, require_safe_markers: bool = True) -> None:
    result = check_text_safety(text, require_safe_markers=require_safe_markers)
    if not result.passed:
        details = {
            "blocked_markers": result.blocked_markers,
            "missing_safe_markers": result.missing_safe_markers,
        }
        raise ValueError(f"Unsafe toy simulation text rejected: {details}")


def build_safe_toy_fixture() -> dict[str, object]:
    return {
        "fixture_kind": "toy_synthetic_abstract_unitless_non-operational",
        "seed": 184185186,
        "nodes": [
            {
                "node_id": "node_alpha",
                "compatibility": 0.25,
                "defense": 0.65,
                "transport_resistance": 0.40,
            },
            {
                "node_id": "node_beta",
                "compatibility": 0.70,
                "defense": 0.20,
                "transport_resistance": 0.55,
            },
        ],
        "edges": [
            {
                "source": "node_alpha",
                "target": "node_beta",
                "edge_weight": 0.50,
            }
        ],
        "agents": [
            {
                "agent_id": "toy_agent_001",
                "activity": 0.10,
                "location": "node_alpha",
            }
        ],
        "boundary": "toy synthetic abstract unitless non-operational only",
    }


def check_fixture_safety(fixture: dict[str, object]) -> SafetyGuardResult:
    return check_text_safety(repr(fixture), require_safe_markers=True)


def collect_guard_summary() -> dict[str, object]:
    fixture = build_safe_toy_fixture()
    result = check_fixture_safety(fixture)
    return {
        "guard_module": "viruse_fabric.safety.toy_simulation_safety_guard",
        "prohibited_category_marker_count": len(PROHIBITED_CATEGORY_MARKERS),
        "prohibited_phrase_marker_count": len(PROHIBITED_PHRASE_MARKERS),
        "required_safe_marker_count": len(REQUIRED_SAFE_MARKERS),
        "safe_fixture_passed": result.passed,
        "safe_fixture_blocked_markers": result.blocked_markers,
        "safe_fixture_missing_safe_markers": result.missing_safe_markers,
    }
