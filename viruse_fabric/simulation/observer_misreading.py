from __future__ import annotations

from dataclasses import dataclass

from viruse_fabric.biology.apparent_targeting import ApparentTargetingAnalyzer
from viruse_fabric.core.fabric import Fabric
from viruse_fabric.geometry.attractor_classifier import AttractorTypeClassifier
from viruse_fabric.geometry.causal_curvature import CausalCurvatureAnalyzer
from viruse_fabric.geometry.causal_geodesic import CausalGeodesicAnalyzer


@dataclass
class ObserverMisreadingResult:
    case_name: str
    path: list[str]

    apparent_targeting_score: float
    misreading_score: float

    pathway_visibility: float
    narrative_compression: float
    dominant_attractor_bias: float
    intention_projection: float
    crisis_confusion_penalty: float
    strained_route_penalty: float

    inferred_story: str
    corrected_reading: str
    interpretation: str


class ObserverMisreadingEngine:
    """Estimate how strongly an observer may misread causal structure as intention.

    This does not model real psychology.
    It models a structural observer error:

    coherent path + visible endpoint + dominant attractor
    becomes
    "it was targeting that endpoint"

    Humanity then applauds itself for discovering a story it projected.
    """

    def __init__(self) -> None:
        self.targeting_analyzer = ApparentTargetingAnalyzer()
        self.classifier = AttractorTypeClassifier()
        self.curvature_analyzer = CausalCurvatureAnalyzer()
        self.geodesic_analyzer = CausalGeodesicAnalyzer()

    def analyze(
        self,
        fabric: Fabric,
        *,
        case_name: str,
        source: str = "A",
        target: str = "E",
    ) -> ObserverMisreadingResult:
        targeting = self.targeting_analyzer.analyze(
            fabric,
            case_name=case_name,
            source=source,
            target=target,
        )
        classification = self.classifier.classify(
            fabric,
            case_name=case_name,
            source=source,
            target=target,
        )
        curvature = self.curvature_analyzer.analyze(fabric)
        geodesic = self.geodesic_analyzer.analyze_path(fabric, source, target)

        node_count = max(len(fabric.nodes), 1)
        pathway_visibility = min(1.0, len(geodesic.path) / node_count)

        # A shorter clean story is easier for an observer to overinterpret.
        if len(geodesic.path) <= 1:
            narrative_compression = 0.0
        else:
            narrative_compression = 1.0 / len(geodesic.path)

        dominant_attractor_bias = 0.0
        if curvature.dominant_nodes:
            dominant_ids = {node.node_id for node in curvature.dominant_nodes}
            path_ids = set(geodesic.path)
            if dominant_ids & path_ids:
                dominant_attractor_bias = 1.0
            else:
                dominant_attractor_bias = 0.55

        crisis_confusion_penalty = min(1.0, len(classification.tension_wells) * 0.65)
        strained_route_penalty = min(1.0, len(classification.strained_gateways) * 0.45)

        intention_projection = min(
            1.0,
            (
                0.45 * (targeting.score / 100.0)
                + 0.25 * pathway_visibility
                + 0.20 * dominant_attractor_bias
                + 0.10 * narrative_compression
            ),
        )

        raw_misreading = (
            45.0 * intention_projection
            + 25.0 * (targeting.score / 100.0)
            + 20.0 * dominant_attractor_bias
            + 10.0 * pathway_visibility
            - 25.0 * crisis_confusion_penalty
            - 15.0 * strained_route_penalty
        )

        misreading_score = max(0.0, min(100.0, raw_misreading))

        return ObserverMisreadingResult(
            case_name=case_name,
            path=geodesic.path,
            apparent_targeting_score=targeting.score,
            misreading_score=misreading_score,
            pathway_visibility=pathway_visibility,
            narrative_compression=narrative_compression,
            dominant_attractor_bias=dominant_attractor_bias,
            intention_projection=intention_projection,
            crisis_confusion_penalty=crisis_confusion_penalty,
            strained_route_penalty=strained_route_penalty,
            inferred_story=self._inferred_story(
                targeting_score=targeting.score,
                misreading_score=misreading_score,
                tension_wells=classification.tension_wells,
                strained_gateways=classification.strained_gateways,
            ),
            corrected_reading=self._corrected_reading(
                tension_wells=classification.tension_wells,
                strained_gateways=classification.strained_gateways,
                constructive_nodes=classification.constructive_nodes,
            ),
            interpretation=self._interpret_score(misreading_score),
        )

    def _interpret_score(self, score: float) -> str:
        if score >= 75:
            return "high risk of intentionality misreading"
        if score >= 50:
            return "moderate risk of intentionality misreading"
        if score >= 30:
            return "weak risk of intentionality misreading"
        return "low risk of intentionality misreading"

    def _inferred_story(
        self,
        *,
        targeting_score: float,
        misreading_score: float,
        tension_wells: list[str],
        strained_gateways: list[str],
    ) -> str:
        if misreading_score >= 75 and targeting_score >= 70:
            return "observer may infer that the pattern selected the endpoint intentionally"

        if tension_wells:
            return "observer may notice disruption, but could still mistake crisis concentration for a cause"

        if strained_gateways:
            return "observer may see a forced route and overread it as directed progression"

        return "observer has limited evidence for intentional targeting"

    def _corrected_reading(
        self,
        *,
        tension_wells: list[str],
        strained_gateways: list[str],
        constructive_nodes: list[str],
    ) -> str:
        if tension_wells:
            return (
                "the dominant attractor is better read as a tension well, "
                "not as intentional selection"
            )

        if strained_gateways:
            return (
                "the path is structured but costly; apparent direction comes from constraint pressure"
            )

        if constructive_nodes:
            return (
                "the path is coherent because constructive attractors support it, "
                "not because the pattern intends the endpoint"
            )

        return "the pattern should be read as weakly organized constraint filtering"
