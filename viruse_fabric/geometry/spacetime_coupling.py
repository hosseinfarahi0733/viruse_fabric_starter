from __future__ import annotations

from dataclasses import dataclass
import copy
import math

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.core.node import EventNode
from viruse_fabric.geometry.metric import spatial_distance2, orientation


@dataclass
class SpaceTimeCouplingConstraint:
    """A biological space-time coupling relation.

    The original MVP made space too weak.
    This constraint makes spatial separation matter when two events are
    biologically connected.

    Example:
    A physical contact event and a cell-state transition should not be
    allowed to drift apart in space without cost.
    """

    source: str
    target: str
    kind: str = "spacetime"
    weight: float = 1.0

    preferred_space: float = 1.0
    space_tolerance: float = 0.5

    omega: tuple[float, float, float] = (1.0, 0.0, 0.0)
    min_orientation: float = 0.0
    orientation_weight: float = 0.5

    def penalty(self, a: EventNode, b: EventNode) -> float:
        spatial_distance = math.sqrt(spatial_distance2(a.coord, b.coord))
        spatial_mismatch = abs(spatial_distance - self.preferred_space)

        spatial_penalty = math.log1p(
            (spatial_mismatch / max(self.space_tolerance, 1e-9)) ** 2
        )

        flow = orientation(a.coord, b.coord, self.omega)
        if flow >= self.min_orientation:
            orientation_penalty = 0.0
        else:
            orientation_penalty = self.orientation_weight * abs(
                self.min_orientation - flow
            )

        return self.weight * (spatial_penalty + orientation_penalty)


def add_biological_spacetime_couplings(fabric: Fabric) -> Fabric:
    """Return a copy of the fabric with explicit biological space-time couplings.

    This is version 0.6's correction to the Critical Engine warning:
    INT-WEAK-SPACE-COUPLING.

    We do not replace the old constraints.
    We add a second layer that says:
    biologically connected events must also remain spatially coherent.
    """

    f = copy.deepcopy(fabric)

    couplings = [
        SpaceTimeCouplingConstraint(
            source="A",
            target="B",
            weight=4.0,
            preferred_space=1.0,
            space_tolerance=0.35,
            omega=(0.7, 0.2, 0.1),
        ),
        SpaceTimeCouplingConstraint(
            source="B",
            target="C",
            weight=3.5,
            preferred_space=1.0,
            space_tolerance=0.45,
            omega=(0.2, 0.7, 0.1),
        ),
        SpaceTimeCouplingConstraint(
            source="C",
            target="D",
            weight=2.5,
            preferred_space=1.414,
            space_tolerance=0.70,
            omega=(0.1, 0.2, 0.7),
        ),
        SpaceTimeCouplingConstraint(
            source="D",
            target="E",
            weight=1.8,
            preferred_space=1.414,
            space_tolerance=0.80,
            omega=(0.4, 0.2, 0.4),
        ),
    ]

    for coupling in couplings:
        f.add_constraint(coupling)

    return f
