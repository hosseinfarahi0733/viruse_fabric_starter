from __future__ import annotations

from dataclasses import dataclass
from typing import Literal
import math

from viruse_fabric.core.node import EventNode
from viruse_fabric.geometry.metric import causal_interval, orientation

ConstraintKind = Literal["compatibility", "necessity", "tension", "projection"]


@dataclass
class Constraint:
    """A relation that tries to hold two nodes together in the fabric.

    weight: importance of the constraint.
    preferred_interval: ideal causal interval between the nodes.
    tolerance: how much mismatch is tolerated before penalty rises.
    """

    source: str
    target: str
    kind: ConstraintKind
    weight: float = 1.0
    preferred_interval: float = 1.0
    tolerance: float = 1.0
    omega: tuple[float, float, float] = (1.0, 1.0, 1.0)

    def penalty(self, a: EventNode, b: EventNode) -> float:
        interval = causal_interval(a.coord, b.coord)
        mismatch = abs(interval - self.preferred_interval)
        direction = orientation(a.coord, b.coord, self.omega)

        # Direction penalty prevents everything from influencing everything else.
        direction_penalty = 0.0 if direction > 0 else abs(direction) + 1.0
        smooth_penalty = math.log1p((mismatch / max(self.tolerance, 1e-9)) ** 2)
        return self.weight * (smooth_penalty + direction_penalty)
