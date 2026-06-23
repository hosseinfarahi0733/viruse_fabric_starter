from __future__ import annotations

from dataclasses import dataclass

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.simulation.projection import ObserverProjection


@dataclass
class CounterfactualDeletionResult:
    deleted_node: str

    base_energy: float
    new_energy: float
    raw_energy_delta: float

    structural_loss: float
    projection_distance: float
    counterfactual_impact: float

    base_order: list[str]
    new_order: list[str]
    removed_constraints: int

    @property
    def interpretation(self) -> str:
        if self.counterfactual_impact >= 7:
            return "high counterfactual importance"
        if self.counterfactual_impact >= 4:
            return "moderate counterfactual importance"
        if self.raw_energy_delta < 0 and self.structural_loss < 2:
            return "mostly tension/noise removing"
        return "low counterfactual importance"


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

    # Missing node also matters. Otherwise deleting the final phenotype looks too harmless.
    missing_penalty = len(set(base) - set(new)) / max(len(base), 1)

    return (total / (len(common) * max_possible)) + missing_penalty


def _structural_loss(fabric: Fabric, node_id: str) -> tuple[float, int]:
    touched = [
        c for c in fabric.constraints
        if c.source == node_id or c.target == node_id
    ]

    # Necessity constraints should matter more than ordinary compatibility.
    kind_multiplier = {
        "compatibility": 1.0,
        "necessity": 1.8,
        "tension": 1.2,
        "projection": 1.4,
    }

    loss = 0.0
    for c in touched:
        loss += c.weight * kind_multiplier.get(c.kind, 1.0)

    return loss, len(touched)


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
    raw_energy_delta = new_energy - base_energy

    base_order = _projection_order(fabric, axis)
    new_order = _projection_order(reduced, axis)

    projection_distance = _rank_distance(base_order, new_order)
    structural_loss, removed_constraints = _structural_loss(fabric, node_id)

    # Raw energy can drop simply because constraints vanished.
    # So the actual counterfactual impact must include lost structure.
    counterfactual_impact = (
        structural_loss
        + 4.0 * projection_distance
        + max(raw_energy_delta, 0.0)
    )

    return CounterfactualDeletionResult(
        deleted_node=node_id,
        base_energy=base_energy,
        new_energy=new_energy,
        raw_energy_delta=raw_energy_delta,
        structural_loss=structural_loss,
        projection_distance=projection_distance,
        counterfactual_impact=counterfactual_impact,
        base_order=base_order,
        new_order=new_order,
        removed_constraints=removed_constraints,
    )
