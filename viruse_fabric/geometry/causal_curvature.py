from __future__ import annotations

from dataclasses import dataclass
import math

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.simulation.rich_projection import RichObserverProjection


@dataclass
class NodeCurvature:
    node_id: str
    kind: str
    degree: int
    local_tension: float
    fabric_pressure: float
    curvature: float
    causal_gravity: float

    @property
    def interpretation(self) -> str:
        if self.causal_gravity >= 3.0:
            return "high causal attractor"
        if self.causal_gravity >= 1.5:
            return "moderate causal attractor"
        if self.causal_gravity >= 0.5:
            return "weak causal attractor"
        return "low curvature node"


@dataclass
class FabricCurvatureReport:
    total_curvature: float
    max_curvature: float
    curvature_entropy: float
    nodes: list[NodeCurvature]

    @property
    def dominant_nodes(self) -> list[NodeCurvature]:
        if not self.nodes:
            return []

        threshold = 0.75 * max(node.causal_gravity for node in self.nodes)
        return [
            node for node in self.nodes
            if node.causal_gravity >= threshold and node.causal_gravity > 0
        ]

    @property
    def interpretation(self) -> str:
        if self.total_curvature >= 8 and self.curvature_entropy < 1.2:
            return "curvature concentrated in a few causal attractors"
        if self.total_curvature >= 8:
            return "high distributed causal curvature"
        if self.total_curvature >= 3:
            return "moderate causal curvature"
        return "low causal curvature"


class CausalCurvatureAnalyzer:
    """Estimate causal curvature in the fabric.

    This is not claiming physical general relativity.
    Calm down, imaginary reviewer.

    Here, curvature means:
    a node's ability to concentrate tension, pressure, and connectivity
    so that nearby causal paths become biased around it.
    """

    def __init__(self) -> None:
        self.projector = RichObserverProjection()

    def analyze(self, fabric: Fabric) -> FabricCurvatureReport:
        projected = self.projector.project(fabric)

        nodes: list[NodeCurvature] = []

        for event in projected:
            # Curvature-like local concentration:
            # tension matters, but pressure and degree decide whether it bends the surrounding fabric.
            curvature = (
                math.log1p(event.local_tension)
                * (1.0 + event.fabric_pressure)
                * math.log1p(event.degree)
            )

            # Causal gravity is curvature with a pressure boost.
            causal_gravity = curvature * (1.0 + 2.0 * event.fabric_pressure)

            nodes.append(
                NodeCurvature(
                    node_id=event.node_id,
                    kind=event.kind,
                    degree=event.degree,
                    local_tension=event.local_tension,
                    fabric_pressure=event.fabric_pressure,
                    curvature=curvature,
                    causal_gravity=causal_gravity,
                )
            )

        total_curvature = sum(node.curvature for node in nodes)
        max_curvature = max((node.curvature for node in nodes), default=0.0)
        entropy = self._curvature_entropy(nodes)

        return FabricCurvatureReport(
            total_curvature=total_curvature,
            max_curvature=max_curvature,
            curvature_entropy=entropy,
            nodes=sorted(nodes, key=lambda node: node.causal_gravity, reverse=True),
        )

    def _curvature_entropy(self, nodes: list[NodeCurvature]) -> float:
        total = sum(node.curvature for node in nodes)

        if total <= 0:
            return 0.0

        entropy = 0.0

        for node in nodes:
            p = node.curvature / total
            if p > 0:
                entropy -= p * math.log(p)

        return entropy
