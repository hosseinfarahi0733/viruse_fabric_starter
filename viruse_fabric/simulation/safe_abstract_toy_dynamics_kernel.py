from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from viruse_fabric.safety.toy_simulation_safety_guard import (
    assert_text_safe,
    check_fixture_safety,
)


@dataclass(frozen=True)
class ToyKernelConfig:
    step_count: int = 4
    compatibility_weight: float = 0.35
    transport_weight: float = 0.25
    capacity_weight: float = 0.20
    defense_weight: float = 0.30
    memory_weight: float = 0.10
    activity_decay: float = 0.03


@dataclass(frozen=True)
class ToyKernelResult:
    fixture_id: str
    step_count: int
    node_count: int
    edge_count: int
    agent_count: int
    final_activity_sum: float
    final_observation_score: float
    targeted_looking_pattern_score: float
    passed_safety_guard: bool


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def _require_safe_fixture(fixture: dict[str, Any]) -> None:
    result = check_fixture_safety(fixture)
    if not result.passed:
        raise ValueError(f"Unsafe fixture rejected by toy kernel: {result}")

    assert_text_safe(
        "toy synthetic abstract unitless non-operational dynamics kernel",
        require_safe_markers=True,
    )


def _node_by_id(fixture: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(node["node_id"]): node for node in fixture.get("nodes", [])}


def _toy_node_drive(node: dict[str, Any], config: ToyKernelConfig) -> float:
    compatibility = float(node.get("compatibility", 0.0))
    defense = float(node.get("defense", 0.0))
    transport_resistance = float(node.get("transport_resistance", 0.0))
    capacity = float(node.get("capacity", 0.0))

    transport_score = 1.0 - transport_resistance

    drive = (
        config.compatibility_weight * compatibility
        + config.transport_weight * transport_score
        + config.capacity_weight * capacity
        - config.defense_weight * defense
    )
    return drive


def _toy_next_activity(
    current_activity: float,
    node: dict[str, Any],
    memory: float,
    config: ToyKernelConfig,
) -> float:
    drive = _toy_node_drive(node, config)
    next_activity = (
        current_activity
        + drive
        + config.memory_weight * memory
        - config.activity_decay
    )
    return clamp01(next_activity)


def _toy_move_location(
    current_location: str,
    fixture: dict[str, Any],
) -> str:
    edges = fixture.get("edges", [])
    outgoing = [
        edge for edge in edges if str(edge.get("source")) == str(current_location)
    ]
    if not outgoing:
        return current_location

    best_edge = max(outgoing, key=lambda edge: float(edge.get("edge_weight", 0.0)))
    return str(best_edge.get("target", current_location))


def run_toy_kernel(
    fixture: dict[str, Any],
    config: ToyKernelConfig | None = None,
) -> ToyKernelResult:
    config = config or ToyKernelConfig()
    _require_safe_fixture(fixture)

    working = deepcopy(fixture)
    nodes = _node_by_id(working)
    agents = working.get("agents", [])
    memory = 0.0

    for _ in range(config.step_count):
        activity_values: list[float] = []

        for agent in agents:
            location = str(agent.get("location"))
            node = nodes.get(location)
            if node is None:
                raise ValueError(f"Toy agent has unknown synthetic location: {location}")

            current_activity = float(agent.get("activity", 0.0))
            next_activity = _toy_next_activity(
                current_activity=current_activity,
                node=node,
                memory=memory,
                config=config,
            )
            agent["activity"] = next_activity
            agent["location"] = _toy_move_location(location, working)
            activity_values.append(next_activity)

        if activity_values:
            memory = clamp01(sum(activity_values) / len(activity_values))

    final_activities = [float(agent.get("activity", 0.0)) for agent in agents]
    final_activity_sum = sum(final_activities)
    final_observation_score = clamp01(
        final_activity_sum / max(1, len(agents))
    )

    node_scores = [
        _toy_node_drive(node, config)
        for node in working.get("nodes", [])
    ]
    if node_scores:
        targeted_looking_pattern_score = clamp01(
            (max(node_scores) - min(node_scores) + final_observation_score) / 2.0
        )
    else:
        targeted_looking_pattern_score = 0.0

    return ToyKernelResult(
        fixture_id=str(working.get("fixture_id", "unknown_toy_fixture")),
        step_count=config.step_count,
        node_count=len(working.get("nodes", [])),
        edge_count=len(working.get("edges", [])),
        agent_count=len(agents),
        final_activity_sum=round(final_activity_sum, 6),
        final_observation_score=round(final_observation_score, 6),
        targeted_looking_pattern_score=round(targeted_looking_pattern_score, 6),
        passed_safety_guard=True,
    )


def run_toy_kernel_catalog(
    fixtures: tuple[dict[str, Any], ...],
    config: ToyKernelConfig | None = None,
) -> tuple[ToyKernelResult, ...]:
    return tuple(run_toy_kernel(fixture, config=config) for fixture in fixtures)


def summarize_kernel_results(results: tuple[ToyKernelResult, ...]) -> dict[str, Any]:
    if not results:
        return {
            "toy_kernel_result_count": 0,
            "toy_kernel_all_safety_passed": False,
            "toy_kernel_mean_observation_score": 0.0,
            "toy_kernel_mean_targeted_looking_pattern_score": 0.0,
        }

    return {
        "toy_kernel_result_count": len(results),
        "toy_kernel_all_safety_passed": all(result.passed_safety_guard for result in results),
        "toy_kernel_mean_observation_score": round(
            sum(result.final_observation_score for result in results) / len(results),
            6,
        ),
        "toy_kernel_mean_targeted_looking_pattern_score": round(
            sum(result.targeted_looking_pattern_score for result in results) / len(results),
            6,
        ),
    }
