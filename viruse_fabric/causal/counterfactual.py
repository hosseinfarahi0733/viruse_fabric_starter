from __future__ import annotations

from dataclasses import dataclass

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.simulation.projection import ObserverProjection


@dataclass
class CounterfactualDeletionResult:
    deleted_node: str
    base_energy: float
    new_energy: float
    energy_delta: float
    base_order: list[str]
    new_order: list[str]
    missing_nodes: list[str]
    order_distance: float

    @property
    def interpretation(self) -> str:
        if self.energy_delta > 5 and self.order_distance > 0.5:
            return "high fabric and projection impact"
        if self.energy_delta > 2:
            return "high fabric impact"
        if self.order_distance > 0.5:
            return "high projection impact"
        if self.energy_delta < 0:
            return "removing this node reduces tension"
        return "low to moderate impact"


def _projection_order(fabric: Fabric, axis: tuple[float, float, float]) -> list[str]:
    projected = ObserverProjection(axis=axis).project(fabric)
    return [event.node_id for event in projected]


def _rank_distance(base: list[str], new: list[str]) -> float:
    """Simple normalized distance between two projected orders.

    This is intentionally small and explainable, because the theory is already
    weird enough without hiding it behind a mathematical fog machine.
    """
    common = [node for node in base if node in new]
    if len(common) <= 1:
        return 1.0

    base_rank = {node: i for i, node in enumerate(base)}
    new_rank = {node: i for i, node in enumerate(new)}

    total = 0.0
    max_possible = max(len(common) - 1, 1)

    for node in common:
        total += abs(base_rank[node] - new_rank[node])

    return total / (len(common) * max_possible)


def counterfactual_delete(
    fabric: Fabric,
    node_id: str,
    axis: tuple[float, float, float] = (0.70, 0.20, 0.10),
) -> CounterfactualDeletionResult:
    if node_id not in fabric.nodes:
        raise KeyError(f"Unknown node: {node_id}")

    base_energy = fabric.energy()
    reduced = fabric.without_node(node_id)
    new_energy = reduced.energy()

    base_order = _projection_order(fabric, axis)
    new_order = _projection_order(reduced, axis)

    return CounterfactualDeletionResult(
        deleted_node=node_id,
        base_energy=base_energy,
        new_energy=new_energy,
        energy_delta=new_energy - base_energy,
        base_order=base_order,
        new_order=new_order,
        missing_nodes=[node_id],
        order_distance=_rank_distance(base_order, new_order),
    )
