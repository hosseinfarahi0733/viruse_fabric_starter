from __future__ import annotations

from dataclasses import dataclass

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.geometry.attractor_classifier import (
    AttractorTypeClassifier,
    AttractorClassificationReport,
)
from viruse_fabric.geometry.causal_geodesic import CausalGeodesicAnalyzer


@dataclass
class ApparentTargetingResult:
    case_name: str
    path: list[str]

    score: float
    constructive_support: float
    path_coverage: float
    gravity_alignment: float
    cost_efficiency: float
    tension_well_penalty: float
    strained_gateway_penalty: float

    constructive_nodes: list[str]
    tension_wells: list[str]
    strained_gateways: list[str]

    interpretation: str
    explanation: str


class ApparentTargetingAnalyzer:
    """Estimate how target-like a causal path appears.

    This does NOT mean the virus has intention.
    It means the observer sees a stable, coherent, low-cost path through the fabric
    and mistakes constraint filtering for targeting, because apparently narratives
    are addictive to primate brains.
    """

    def __init__(self) -> None:
        self.classifier = AttractorTypeClassifier()
        self.geodesic_analyzer = CausalGeodesicAnalyzer()

    def analyze(
        self,
        fabric: Fabric,
        *,
        case_name: str,
        source: str = "A",
        target: str = "E",
    ) -> ApparentTargetingResult:
        classification = self.classifier.classify(
            fabric,
            case_name=case_name,
            source=source,
            target=target,
        )
        geodesic = self.geodesic_analyzer.analyze_path(fabric, source, target)

        node_count = max(len(fabric.nodes), 1)
        path_coverage = min(1.0, len(geodesic.path) / node_count)

        constructive_support = self._constructive_support(classification)
        tension_well_penalty = self._tension_well_penalty(classification)
        strained_gateway_penalty = self._strained_gateway_penalty(classification)

        if geodesic.total_raw_penalty in (0.0, float("inf")):
            gravity_alignment = 0.0
        else:
            gravity_alignment = min(
                1.0,
                geodesic.total_gravity_pull / max(geodesic.total_raw_penalty, 1e-9),
            )

        cost_efficiency = 1.0 / (1.0 + max(geodesic.total_cost, 0.0))

        raw_score = (
            35.0 * constructive_support
            + 20.0 * path_coverage
            + 20.0 * gravity_alignment
            + 25.0 * cost_efficiency
            - 30.0 * tension_well_penalty
            - 18.0 * strained_gateway_penalty
        )

        score = max(0.0, min(100.0, raw_score))

        interpretation = self._interpret_score(score)
        explanation = self._explain(
            score=score,
            constructive_support=constructive_support,
            path_coverage=path_coverage,
            gravity_alignment=gravity_alignment,
            cost_efficiency=cost_efficiency,
            tension_well_penalty=tension_well_penalty,
            strained_gateway_penalty=strained_gateway_penalty,
        )

        return ApparentTargetingResult(
            case_name=case_name,
            path=geodesic.path,
            score=score,
            constructive_support=constructive_support,
            path_coverage=path_coverage,
            gravity_alignment=gravity_alignment,
            cost_efficiency=cost_efficiency,
            tension_well_penalty=tension_well_penalty,
            strained_gateway_penalty=strained_gateway_penalty,
            constructive_nodes=classification.constructive_nodes,
            tension_wells=classification.tension_wells,
            strained_gateways=classification.strained_gateways,
            interpretation=interpretation,
            explanation=explanation,
        )

    def _constructive_support(self, report: AttractorClassificationReport) -> float:
        value = 0.0

        for item in report.classifications:
            if item.attractor_type == "constructive_attractor":
                value += item.gravity_ratio
            elif item.attractor_type == "passive_corridor" and item.in_geodesic:
                value += 0.15 * item.gravity_ratio

        return min(1.0, value)

    def _tension_well_penalty(self, report: AttractorClassificationReport) -> float:
        value = 0.0

        for item in report.classifications:
            if item.attractor_type == "tension_well":
                value += item.gravity_ratio

        return min(1.5, value)

    def _strained_gateway_penalty(self, report: AttractorClassificationReport) -> float:
        value = 0.0

        for item in report.classifications:
            if item.attractor_type == "strained_gateway":
                # A gateway is still on the path, so it is not as bad as a tension well.
                value += 0.65 * item.gravity_ratio

        return min(1.5, value)

    def _interpret_score(self, score: float) -> str:
        if score >= 75:
            return "high apparent targeting"
        if score >= 50:
            return "moderate apparent targeting"
        if score >= 30:
            return "weak apparent targeting"
        return "low apparent targeting"

    def _explain(
        self,
        *,
        score: float,
        constructive_support: float,
        path_coverage: float,
        gravity_alignment: float,
        cost_efficiency: float,
        tension_well_penalty: float,
        strained_gateway_penalty: float,
    ) -> str:
        if score >= 75:
            return (
                "The path looks target-like because it is coherent, efficient, "
                "and supported by constructive attractors."
            )

        if tension_well_penalty > 0.6:
            return (
                "The path avoids high-gravity tension wells. This reduces apparent targeting "
                "because the fabric looks crisis-dominated rather than route-coherent."
            )

        if strained_gateway_penalty > 0.4:
            return (
                "The path passes through a costly gateway. It has structure, but the route is strained."
            )

        if constructive_support < 0.3:
            return (
                "The path lacks strong constructive attractor support, so targeting appears weak."
            )

        return (
            "The path shows partial route coherence, but not enough to look strongly target-like."
        )
