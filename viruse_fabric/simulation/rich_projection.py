from __future__ import annotations

from dataclasses import dataclass
import math

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.core.node import EventNode


@dataclass
class RichProjectedEvent:
    node_id: str
    event: str
    kind: str

    perceived_time: float
    local_tension: float
    perceived_intensity: float
    fabric_pressure: float
    curvature_hint: float
    degree: int


class RichObserverProjection:
    """Observer projection that sees more than event order.

    The old projection compressed the fabric into a simple perceived timeline.
    This one keeps hints of hidden fabric change:
    - local tension
    - perceived intensity
    - fabric pressure
    - curvature hint

    Translation: the observer finally gets more than a glorified to-do list.
    """

    def __init__(self, axis: tuple[float, float, float] = (0.70, 0.20, 0.10)) -> None:
        self.axis = axis

    def perceived_time(self, node: EventNode) -> float:
        return (
            self.axis[0] * node.coord.t1
            + self.axis[1] * node.coord.t2
            + self.axis[2] * node.coord.t3
        )

    def _constraint_penalty(self, fabric: Fabric, constraint) -> float:
        source = fabric.nodes[constraint.source]
        target = fabric.nodes[constraint.target]

        penalty_fn = getattr(constraint, "penalty", None)

        if callable(penalty_fn):
            return float(penalty_fn(source, target))

        return 0.0

    def node_tension_map(self, fabric: Fabric) -> dict[str, float]:
        tension = {node_id: 0.0 for node_id in fabric.nodes}

        for constraint in fabric.constraints:
            if constraint.source not in fabric.nodes or constraint.target not in fabric.nodes:
                continue

            penalty = self._constraint_penalty(fabric, constraint)

            # Split relation tension across the two touched nodes.
            tension[constraint.source] += penalty / 2.0
            tension[constraint.target] += penalty / 2.0

        return tension

    def node_degree_map(self, fabric: Fabric) -> dict[str, int]:
        degree = {node_id: 0 for node_id in fabric.nodes}

        for constraint in fabric.constraints:
            if constraint.source in degree:
                degree[constraint.source] += 1
            if constraint.target in degree:
                degree[constraint.target] += 1

        return degree

    def project(self, fabric: Fabric) -> list[RichProjectedEvent]:
        tension = self.node_tension_map(fabric)
        degree = self.node_degree_map(fabric)

        total_tension = sum(tension.values())
        max_tension = max(tension.values()) if tension else 0.0

        events: list[RichProjectedEvent] = []

        for node_id, node in fabric.nodes.items():
            local_tension = tension[node_id]
            node_degree = degree[node_id]

            if max_tension > 0:
                normalized_tension = local_tension / max_tension
            else:
                normalized_tension = 0.0

            perceived_intensity = math.log1p(local_tension) * (1.0 + 0.15 * node_degree)

            if total_tension > 0:
                fabric_pressure = local_tension / total_tension
            else:
                fabric_pressure = 0.0

            curvature_hint = normalized_tension * math.log1p(node_degree)

            events.append(
                RichProjectedEvent(
                    node_id=node_id,
                    event=str(node.state.get("event", "")),
                    kind=str(node.state.get("kind", "")),
                    perceived_time=self.perceived_time(node),
                    local_tension=local_tension,
                    perceived_intensity=perceived_intensity,
                    fabric_pressure=fabric_pressure,
                    curvature_hint=curvature_hint,
                    degree=node_degree,
                )
            )

        return sorted(events, key=lambda event: event.perceived_time)


def rich_projection_distance(
    base: list[RichProjectedEvent],
    new: list[RichProjectedEvent],
) -> float:
    """Compare two rich projections.

    This catches hidden changes that simple order distance misses.
    """

    base_map = {event.node_id: event for event in base}
    new_map = {event.node_id: event for event in new}

    common = sorted(set(base_map) & set(new_map))

    if not common:
        return 1.0

    total = 0.0

    for node_id in common:
        a = base_map[node_id]
        b = new_map[node_id]

        intensity_delta = abs(a.perceived_intensity - b.perceived_intensity)
        pressure_delta = abs(a.fabric_pressure - b.fabric_pressure)
        curvature_delta = abs(a.curvature_hint - b.curvature_hint)
        tension_delta = abs(a.local_tension - b.local_tension)

        # Normalized-ish, readable, not pretending to be holy scripture.
        total += (
            0.25 * math.log1p(tension_delta)
            + 0.35 * intensity_delta
            + 2.0 * pressure_delta
            + 0.75 * curvature_delta
        )

    missing_penalty = len(set(base_map) ^ set(new_map)) / max(len(base_map), 1)

    return (total / len(common)) + missing_penalty
