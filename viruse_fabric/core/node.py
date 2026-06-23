from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
import numpy as np


@dataclass(frozen=True)
class Coord6D:
    """3 spatial coordinates + 3 real model-time coordinates."""

    x: float
    y: float
    z: float
    t1: float
    t2: float
    t3: float

    @property
    def space(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z], dtype=float)

    @property
    def time(self) -> np.ndarray:
        return np.array([self.t1, self.t2, self.t3], dtype=float)


@dataclass
class EventNode:
    """A visible node in the unified causal fabric."""

    node_id: str
    label: str
    coord: Coord6D
    kind: str = "abstract"
    state: dict[str, Any] = field(default_factory=dict)

    def __hash__(self) -> int:
        return hash(self.node_id)
