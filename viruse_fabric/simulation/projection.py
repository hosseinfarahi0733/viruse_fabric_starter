from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from viruse_fabric.core.fabric import Fabric


@dataclass
class ProjectedEvent:
    node_id: str
    label: str
    perceived_time: float
    kind: str


@dataclass
class ObserverProjection:
    """Compresses t1,t2,t3 into a single perceived time axis."""

    axis: tuple[float, float, float] = (0.70, 0.20, 0.10)

    def project_time(self, time_vec: np.ndarray) -> float:
        axis = np.asarray(self.axis, dtype=float)
        axis = axis / max(np.linalg.norm(axis), 1e-9)
        return float(np.dot(axis, time_vec))

    def project(self, fabric: Fabric) -> list[ProjectedEvent]:
        events = []
        for node in fabric.nodes.values():
            events.append(
                ProjectedEvent(
                    node_id=node.node_id,
                    label=node.label,
                    perceived_time=self.project_time(node.coord.time),
                    kind=node.kind,
                )
            )
        return sorted(events, key=lambda e: e.perceived_time)
