from __future__ import annotations

from dataclasses import dataclass

from viruse_fabric.core.fabric import Fabric


@dataclass
class CausalMassReport:
    base_energy: float
    masses: dict[str, float]

    def sorted(self) -> list[tuple[str, float]]:
        return sorted(self.masses.items(), key=lambda item: item[1], reverse=True)


def compute_causal_mass(fabric: Fabric) -> CausalMassReport:
    """Causal mass = how costly it is to remove a node from the constraint fabric.

    In a pure graph deletion, removing a node also removes its constraints, which always
    makes the remaining energy look smaller. That is the wrong intuition for this theory.
    Here we model deletion as *severing* the node from the fabric: every broken constraint
    creates a severance cost, reduced by the amount of tension that constraint already had.

    High positive mass means: the node holds many coherent constraints together.
    Low or negative mass means: the node mostly contributes tension/noise.
    """

    base = fabric.energy()
    masses: dict[str, float] = {}
    for node_id in fabric.nodes:
        mass = 0.0
        for c in fabric.constraints:
            if c.source == node_id or c.target == node_id:
                a = fabric.nodes[c.source]
                b = fabric.nodes[c.target]
                current_penalty = c.penalty(a, b)
                severance_cost = c.weight * 4.0
                mass += severance_cost - current_penalty
        masses[node_id] = mass
    return CausalMassReport(base_energy=base, masses=masses)
