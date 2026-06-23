from __future__ import annotations

from dataclasses import dataclass
import heapq
import math
from typing import Any

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.geometry.causal_curvature import CausalCurvatureAnalyzer


@dataclass
class GeodesicEdge:
    source: str
    target: str
    kind: str
    raw_penalty: float
    source_gravity: float
    target_gravity: float
    gravity_pull: float
    final_cost: float


@dataclass
class CausalGeodesic:
    source: str
    target: str
    path: list[str]
    total_cost: float
    total_raw_penalty: float
    total_gravity_pull: float
    edges: list[GeodesicEdge]

    @property
    def path_label(self) -> str:
        return " → ".join(self.path)

    @property
    def interpretation(self) -> str:
        if not self.path:
            return "no causal path found"
        if self.total_gravity_pull >= self.total_raw_penalty:
            return "path strongly shaped by causal gravity"
        if self.total_gravity_pull >= 0.35 * self.total_raw_penalty:
            return "path moderately bent by causal gravity"
        return "path mostly determined by raw constraint cost"


@dataclass
class GeodesicComparison:
    name: str
    geodesic: CausalGeodesic
    dominant_attractors: list[str]
    total_curvature: float
    curvature_entropy: float


class CausalGeodesicAnalyzer:
    """Find low-cost causal paths through the fabric.

    A causal geodesic is not just the shortest graph path.
    It is a path where raw constraint cost is reduced by nearby causal gravity.

    In this toy model:
    - high penalty makes an edge harder to travel
    - high causal gravity near the edge pulls the path inward
    - the best path is the path with lowest final cost

    Translation: the model stops pretending that cause is a straight arrow.
    Finally, some manners.
    """

    def __init__(self, attraction_strength: float = 0.65) -> None:
        self.attraction_strength = attraction_strength
        self.curvature_analyzer = CausalCurvatureAnalyzer()

    def analyze_path(self, fabric: Fabric, source: str, target: str) -> CausalGeodesic:
        if source not in fabric.nodes:
            raise KeyError(f"Unknown source node: {source}")
        if target not in fabric.nodes:
            raise KeyError(f"Unknown target node: {target}")

        curvature_report = self.curvature_analyzer.analyze(fabric)
        gravity = {
            node.node_id: node.causal_gravity
            for node in curvature_report.nodes
        }
        max_gravity = max(gravity.values(), default=1.0)

        adjacency: dict[str, list[tuple[str, GeodesicEdge]]] = {
            node_id: []
            for node_id in fabric.nodes
        }

        for constraint in fabric.constraints:
            if constraint.source not in fabric.nodes or constraint.target not in fabric.nodes:
                continue

            edge = self._edge_from_constraint(
                fabric=fabric,
                constraint=constraint,
                gravity=gravity,
                max_gravity=max_gravity,
            )
            adjacency[edge.source].append((edge.target, edge))

        distances: dict[str, float] = {node_id: math.inf for node_id in fabric.nodes}
        previous: dict[str, tuple[str, GeodesicEdge] | None] = {
            node_id: None
            for node_id in fabric.nodes
        }

        distances[source] = 0.0
        heap: list[tuple[float, str]] = [(0.0, source)]

        while heap:
            current_distance, node_id = heapq.heappop(heap)

            if current_distance > distances[node_id]:
                continue

            if node_id == target:
                break

            for next_node, edge in adjacency.get(node_id, []):
                candidate = current_distance + edge.final_cost

                if candidate < distances[next_node]:
                    distances[next_node] = candidate
                    previous[next_node] = (node_id, edge)
                    heapq.heappush(heap, (candidate, next_node))

        if math.isinf(distances[target]):
            return CausalGeodesic(
                source=source,
                target=target,
                path=[],
                total_cost=math.inf,
                total_raw_penalty=math.inf,
                total_gravity_pull=0.0,
                edges=[],
            )

        path: list[str] = []
        edges: list[GeodesicEdge] = []

        current = target
        while current is not None:
            path.append(current)
            prev = previous[current]
            if prev is None:
                break
            prev_node, edge = prev
            edges.append(edge)
            current = prev_node

        path.reverse()
        edges.reverse()

        return CausalGeodesic(
            source=source,
            target=target,
            path=path,
            total_cost=distances[target],
            total_raw_penalty=sum(edge.raw_penalty for edge in edges),
            total_gravity_pull=sum(edge.gravity_pull for edge in edges),
            edges=edges,
        )

    def compare(self, name: str, fabric: Fabric, source: str = "A", target: str = "E") -> GeodesicComparison:
        curvature_report = self.curvature_analyzer.analyze(fabric)
        geodesic = self.analyze_path(fabric, source, target)

        return GeodesicComparison(
            name=name,
            geodesic=geodesic,
            dominant_attractors=[node.node_id for node in curvature_report.dominant_nodes],
            total_curvature=curvature_report.total_curvature,
            curvature_entropy=curvature_report.curvature_entropy,
        )

    def _edge_from_constraint(
        self,
        *,
        fabric: Fabric,
        constraint: Any,
        gravity: dict[str, float],
        max_gravity: float,
    ) -> GeodesicEdge:
        source = fabric.nodes[constraint.source]
        target = fabric.nodes[constraint.target]

        penalty_fn = getattr(constraint, "penalty", None)
        if callable(penalty_fn):
            raw_penalty = float(penalty_fn(source, target))
        else:
            raw_penalty = float(getattr(constraint, "weight", 1.0))

        source_gravity = gravity.get(constraint.source, 0.0)
        target_gravity = gravity.get(constraint.target, 0.0)

        normalized_gravity = (
            (source_gravity + target_gravity)
            / max(2.0 * max_gravity, 1e-9)
        )

        gravity_pull = self.attraction_strength * normalized_gravity

        kind = str(getattr(constraint, "kind", "abstract"))
        kind_multiplier = {
            "compatibility": 0.95,
            "necessity": 1.00,
            "projection": 1.05,
            "spacetime": 0.90,
            "tension": 1.35,
        }.get(kind, 1.0)

        # Pull reduces the path cost, but never lets it become zero or negative.
        final_cost = max(
            0.05,
            kind_multiplier * raw_penalty / (1.0 + gravity_pull),
        )

        return GeodesicEdge(
            source=constraint.source,
            target=constraint.target,
            kind=kind,
            raw_penalty=raw_penalty,
            source_gravity=source_gravity,
            target_gravity=target_gravity,
            gravity_pull=gravity_pull,
            final_cost=final_cost,
        )
