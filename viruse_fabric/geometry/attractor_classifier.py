from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.geometry.causal_curvature import CausalCurvatureAnalyzer
from viruse_fabric.geometry.causal_geodesic import CausalGeodesicAnalyzer


AttractorType = Literal[
    "constructive_attractor",
    "tension_well",
    "strained_gateway",
    "passive_corridor",
    "background_node",
]


@dataclass
class AttractorClassification:
    node_id: str
    kind: str
    attractor_type: AttractorType

    in_geodesic: bool
    path_index: int | None

    causal_gravity: float
    gravity_ratio: float
    curvature: float
    local_tension: float
    fabric_pressure: float
    degree: int

    incident_path_cost: float
    incident_raw_penalty: float
    incident_gravity_pull: float

    explanation: str
    recommendation: str


@dataclass
class AttractorClassificationReport:
    case_name: str
    geodesic_path: list[str]
    dominant_attractors: list[str]
    classifications: list[AttractorClassification]

    @property
    def constructive_nodes(self) -> list[str]:
        return [
            c.node_id for c in self.classifications
            if c.attractor_type == "constructive_attractor"
        ]

    @property
    def tension_wells(self) -> list[str]:
        return [
            c.node_id for c in self.classifications
            if c.attractor_type == "tension_well"
        ]

    @property
    def strained_gateways(self) -> list[str]:
        return [
            c.node_id for c in self.classifications
            if c.attractor_type == "strained_gateway"
        ]

    @property
    def interpretation(self) -> str:
        if self.tension_wells and self.constructive_nodes:
            return "mixed fabric: some attractors guide paths while others repel or concentrate crisis"
        if self.tension_wells:
            return "avoidance-dominated fabric: dominant attractors behave like tension wells"
        if self.constructive_nodes and self.strained_gateways:
            return "mixed constructive fabric: attractors support the path but some gateways remain strained"
        if self.constructive_nodes:
            return "constructive fabric: attractors support the geodesic path"
        if self.strained_gateways:
            return "strained fabric: attractors lie on the path but remain costly gateways"
        return "weakly organized fabric: no strong attractor role detected"


class AttractorTypeClassifier:
    """Classify causal attractors by their relation to geodesic paths.

    A node with high causal gravity can do two very different things:

    1. Constructive attractor:
       The path passes through it. It organizes the route.

    2. Tension well:
       The path avoids it. It concentrates stress but is not a stable route.

    This distinction matters because humans see a big bright causal object and
    immediately call it "the cause", because apparently restraint was not included
    in the default firmware.
    """

    def __init__(
        self,
        *,
        high_gravity_threshold: float = 0.72,
        moderate_gravity_threshold: float = 0.42,
        strained_cost_threshold: float = 1.25,
    ) -> None:
        self.high_gravity_threshold = high_gravity_threshold
        self.moderate_gravity_threshold = moderate_gravity_threshold
        self.strained_cost_threshold = strained_cost_threshold

        self.curvature_analyzer = CausalCurvatureAnalyzer()
        self.geodesic_analyzer = CausalGeodesicAnalyzer()

    def classify(
        self,
        fabric: Fabric,
        *,
        case_name: str,
        source: str = "A",
        target: str = "E",
    ) -> AttractorClassificationReport:
        curvature_report = self.curvature_analyzer.analyze(fabric)
        geodesic = self.geodesic_analyzer.analyze_path(fabric, source, target)

        max_gravity = max(
            (node.causal_gravity for node in curvature_report.nodes),
            default=1.0,
        )

        path_index = {
            node_id: index
            for index, node_id in enumerate(geodesic.path)
        }

        incident_cost = {node_id: 0.0 for node_id in fabric.nodes}
        incident_raw = {node_id: 0.0 for node_id in fabric.nodes}
        incident_pull = {node_id: 0.0 for node_id in fabric.nodes}

        for edge in geodesic.edges:
            for node_id in (edge.source, edge.target):
                incident_cost[node_id] += edge.final_cost
                incident_raw[node_id] += edge.raw_penalty
                incident_pull[node_id] += edge.gravity_pull

        classifications: list[AttractorClassification] = []

        for node in curvature_report.nodes:
            in_path = node.node_id in path_index
            gravity_ratio = node.causal_gravity / max(max_gravity, 1e-9)

            node_incident_cost = incident_cost.get(node.node_id, 0.0)

            attractor_type = self._classify_type(
                in_path=in_path,
                gravity_ratio=gravity_ratio,
                incident_cost=node_incident_cost,
            )

            explanation, recommendation = self._explain(
                attractor_type=attractor_type,
                node_id=node.node_id,
            )

            classifications.append(
                AttractorClassification(
                    node_id=node.node_id,
                    kind=node.kind,
                    attractor_type=attractor_type,
                    in_geodesic=in_path,
                    path_index=path_index.get(node.node_id),
                    causal_gravity=node.causal_gravity,
                    gravity_ratio=gravity_ratio,
                    curvature=node.curvature,
                    local_tension=node.local_tension,
                    fabric_pressure=node.fabric_pressure,
                    degree=node.degree,
                    incident_path_cost=node_incident_cost,
                    incident_raw_penalty=incident_raw.get(node.node_id, 0.0),
                    incident_gravity_pull=incident_pull.get(node.node_id, 0.0),
                    explanation=explanation,
                    recommendation=recommendation,
                )
            )

        return AttractorClassificationReport(
            case_name=case_name,
            geodesic_path=geodesic.path,
            dominant_attractors=[
                node.node_id for node in curvature_report.dominant_nodes
            ],
            classifications=sorted(
                classifications,
                key=lambda item: item.causal_gravity,
                reverse=True,
            ),
        )

    def _classify_type(
        self,
        *,
        in_path: bool,
        gravity_ratio: float,
        incident_cost: float,
    ) -> AttractorType:
        if in_path and gravity_ratio >= self.high_gravity_threshold:
            if incident_cost >= self.strained_cost_threshold:
                return "strained_gateway"
            return "constructive_attractor"

        if (not in_path) and gravity_ratio >= self.high_gravity_threshold:
            return "tension_well"

        if in_path and gravity_ratio >= self.moderate_gravity_threshold:
            return "passive_corridor"

        if in_path:
            return "passive_corridor"

        return "background_node"

    def _explain(
        self,
        *,
        attractor_type: AttractorType,
        node_id: str,
    ) -> tuple[str, str]:
        if attractor_type == "constructive_attractor":
            return (
                f"{node_id} has high causal gravity and lies on the geodesic path.",
                "Treat it as a route-organizing attractor, not merely an early event.",
            )

        if attractor_type == "tension_well":
            return (
                f"{node_id} has high causal gravity but is avoided by the geodesic path.",
                "Treat it as a crisis center or avoided basin, not as a stable route.",
            )

        if attractor_type == "strained_gateway":
            return (
                f"{node_id} lies on the geodesic and has high gravity, but the path cost around it remains high.",
                "Treat it as a necessary but stressed passage point.",
            )

        if attractor_type == "passive_corridor":
            return (
                f"{node_id} lies on the geodesic but does not dominate the fabric.",
                "Treat it as a corridor node in the route.",
            )

        return (
            f"{node_id} is outside the geodesic and does not dominate causal gravity.",
            "Treat it as background until stronger constraints justify a larger role.",
        )
