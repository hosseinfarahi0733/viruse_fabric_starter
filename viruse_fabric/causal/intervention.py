from __future__ import annotations

from dataclasses import dataclass, replace
import copy

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.simulation.projection import ObserverProjection


@dataclass
class InterventionComparison:
    name: str
    description: str
    base_energy: float
    new_energy: float
    energy_delta: float
    base_order: list[str]
    new_order: list[str]
    projection_distance: float

    @property
    def interpretation(self) -> str:
        if self.energy_delta > 3 and self.projection_distance > 0.35:
            return "strong fabric and projection effect"
        if self.energy_delta > 3:
            return "strong fabric effect"
        if self.projection_distance > 0.35:
            return "strong projection effect"
        if self.energy_delta < -3:
            return "stabilizing intervention"
        return "limited intervention effect"


def _projection_order(fabric: Fabric, axis: tuple[float, float, float]) -> list[str]:
    projected = ObserverProjection(axis=axis).project(fabric)
    return [event.node_id for event in projected]


def _rank_distance(base: list[str], new: list[str]) -> float:
    common = [node for node in base if node in new]

    if len(common) <= 1:
        return 1.0

    base_rank = {node: i for i, node in enumerate(base)}
    new_rank = {node: i for i, node in enumerate(new)}

    total = 0.0
    max_possible = max(len(base) - 1, 1)

    for node in common:
        total += abs(base_rank[node] - new_rank[node])

    missing_penalty = len(set(base) - set(new)) / max(len(base), 1)

    return (total / (len(common) * max_possible)) + missing_penalty


def shift_node_time(
    fabric: Fabric,
    node_id: str,
    *,
    dt1: float = 0.0,
    dt2: float = 0.0,
    dt3: float = 0.0,
) -> Fabric:
    """Move a node inside the 3-time structure without deleting it."""

    if node_id not in fabric.nodes:
        raise KeyError(f"Unknown node: {node_id}")

    f = copy.deepcopy(fabric)
    node = f.nodes[node_id]
    node.coord = replace(
        node.coord,
        t1=node.coord.t1 + dt1,
        t2=node.coord.t2 + dt2,
        t3=node.coord.t3 + dt3,
    )
    node.state["intervention"] = {
        "type": "shift_node_time",
        "dt1": dt1,
        "dt2": dt2,
        "dt3": dt3,
    }
    return f


def shift_node_space(
    fabric: Fabric,
    node_id: str,
    *,
    dx: float = 0.0,
    dy: float = 0.0,
    dz: float = 0.0,
) -> Fabric:
    """Move a node spatially without changing its three time coordinates."""

    if node_id not in fabric.nodes:
        raise KeyError(f"Unknown node: {node_id}")

    f = copy.deepcopy(fabric)
    node = f.nodes[node_id]
    node.coord = replace(
        node.coord,
        x=node.coord.x + dx,
        y=node.coord.y + dy,
        z=node.coord.z + dz,
    )
    node.state["intervention"] = {
        "type": "shift_node_space",
        "dx": dx,
        "dy": dy,
        "dz": dz,
    }
    return f


def scale_constraint_weight(
    fabric: Fabric,
    *,
    source: str | None = None,
    target: str | None = None,
    kind: str | None = None,
    factor: float = 1.0,
) -> Fabric:
    """Scale matching constraint weights.

    This lets us test whether a relation is truly central or merely decorative.
    Humanity invented decorative relations too, mostly in meetings.
    """

    f = copy.deepcopy(fabric)
    changed = 0

    for constraint in f.constraints:
        source_match = source is None or constraint.source == source
        target_match = target is None or constraint.target == target
        kind_match = kind is None or constraint.kind == kind

        if source_match and target_match and kind_match:
            constraint.weight *= factor
            changed += 1

    if changed == 0:
        raise ValueError("No constraints matched the intervention filter.")

    return f


def compare_intervention(
    *,
    name: str,
    description: str,
    base: Fabric,
    intervened: Fabric,
    axis: tuple[float, float, float] = (0.70, 0.20, 0.10),
) -> InterventionComparison:
    base_energy = base.energy()
    new_energy = intervened.energy()

    base_order = _projection_order(base, axis)
    new_order = _projection_order(intervened, axis)

    return InterventionComparison(
        name=name,
        description=description,
        base_energy=base_energy,
        new_energy=new_energy,
        energy_delta=new_energy - base_energy,
        base_order=base_order,
        new_order=new_order,
        projection_distance=_rank_distance(base_order, new_order),
    )
