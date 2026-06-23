from __future__ import annotations

from dataclasses import dataclass

from viruse_fabric.core.fabric import Fabric
from viruse_fabric.simulation.observer_misreading import ObserverMisreadingEngine
from viruse_fabric.biology.apparent_targeting import ApparentTargetingAnalyzer
from viruse_fabric.geometry.attractor_classifier import AttractorTypeClassifier


@dataclass
class IntentionCorrectionReport:
    case_name: str
    path: list[str]

    apparent_targeting_score: float
    misreading_score: float

    mistaken_story: str
    corrected_story: str
    correction_principle: str
    book_paragraph: str

    main_error_source: str
    confidence: str


class IntentionCorrectionEngine:
    """Generate a corrected explanation for apparent intention.

    The goal is not to deny pattern.
    The goal is to prevent pattern from being lazily upgraded into intention.

    Because apparently the human mind sees a route and immediately invents a driver.
    """

    def __init__(self) -> None:
        self.misreading_engine = ObserverMisreadingEngine()
        self.targeting_analyzer = ApparentTargetingAnalyzer()
        self.classifier = AttractorTypeClassifier()

    def generate(
        self,
        fabric: Fabric,
        *,
        case_name: str,
        source: str = "A",
        target: str = "E",
    ) -> IntentionCorrectionReport:
        misreading = self.misreading_engine.analyze(
            fabric,
            case_name=case_name,
            source=source,
            target=target,
        )
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

        main_error_source = self._main_error_source(
            misreading_score=misreading.misreading_score,
            targeting_score=targeting.score,
            tension_wells=classification.tension_wells,
            strained_gateways=classification.strained_gateways,
            constructive_nodes=classification.constructive_nodes,
        )

        mistaken_story = self._mistaken_story(
            case_name=case_name,
            path=misreading.path,
            targeting_score=targeting.score,
            misreading_score=misreading.misreading_score,
            tension_wells=classification.tension_wells,
            strained_gateways=classification.strained_gateways,
        )

        corrected_story = self._corrected_story(
            path=misreading.path,
            constructive_nodes=classification.constructive_nodes,
            tension_wells=classification.tension_wells,
            strained_gateways=classification.strained_gateways,
        )

        correction_principle = self._correction_principle(
            constructive_nodes=classification.constructive_nodes,
            tension_wells=classification.tension_wells,
            strained_gateways=classification.strained_gateways,
        )

        book_paragraph = self._book_paragraph(
            case_name=case_name,
            path=misreading.path,
            targeting_score=targeting.score,
            misreading_score=misreading.misreading_score,
            main_error_source=main_error_source,
            corrected_story=corrected_story,
        )

        return IntentionCorrectionReport(
            case_name=case_name,
            path=misreading.path,
            apparent_targeting_score=targeting.score,
            misreading_score=misreading.misreading_score,
            mistaken_story=mistaken_story,
            corrected_story=corrected_story,
            correction_principle=correction_principle,
            book_paragraph=book_paragraph,
            main_error_source=main_error_source,
            confidence=self._confidence(misreading.misreading_score, targeting.score),
        )

    def _main_error_source(
        self,
        *,
        misreading_score: float,
        targeting_score: float,
        tension_wells: list[str],
        strained_gateways: list[str],
        constructive_nodes: list[str],
    ) -> str:
        if tension_wells:
            return "crisis concentration confused with causal intention"

        if strained_gateways:
            return "forced progression confused with directed intention"

        if constructive_nodes and targeting_score >= 70 and misreading_score >= 70:
            return "route coherence compressed into intentional selection"

        if targeting_score < 30:
            return "weak structure overinterpreted as direction"

        return "partial route coherence overread as purpose"

    def _mistaken_story(
        self,
        *,
        case_name: str,
        path: list[str],
        targeting_score: float,
        misreading_score: float,
        tension_wells: list[str],
        strained_gateways: list[str],
    ) -> str:
        path_label = " → ".join(path)

        if misreading_score >= 75:
            return (
                f"In {case_name}, an observer may see the route {path_label} "
                f"and infer that the pattern intentionally selected the endpoint."
            )

        if tension_wells:
            return (
                f"In {case_name}, an observer may treat the tension well "
                f"{', '.join(tension_wells)} as the hidden cause or target."
            )

        if strained_gateways:
            return (
                f"In {case_name}, an observer may see the forced route through "
                f"{', '.join(strained_gateways)} as directed progression."
            )

        if targeting_score < 30:
            return (
                f"In {case_name}, the observer has little reason to infer targeting, "
                "but may still overread a visible endpoint as purpose."
            )

        return (
            f"In {case_name}, partial route coherence may be mistaken for purpose."
        )

    def _corrected_story(
        self,
        *,
        path: list[str],
        constructive_nodes: list[str],
        tension_wells: list[str],
        strained_gateways: list[str],
    ) -> str:
        path_label = " → ".join(path)

        if tension_wells:
            return (
                f"The route {path_label} does not show intention. "
                f"It avoids high-tension wells: {', '.join(tension_wells)}. "
                "The dominant attractor is a crisis concentration, not a chosen target."
            )

        if strained_gateways:
            return (
                f"The route {path_label} is structured but costly. "
                f"The strained gateway {', '.join(strained_gateways)} shows constraint pressure, "
                "not intentional direction."
            )

        if constructive_nodes:
            nodes = ", ".join(constructive_nodes)

            if len(constructive_nodes) == 1:
                return (
                    f"The route {path_label} looks target-like because the constructive "
                    f"attractor {nodes} stabilizes the path. "
                    "This is route coherence, not intention."
                )

            return (
                f"The route {path_label} looks target-like because constructive "
                f"attractors {nodes} stabilize the path. "
                "This is route coherence, not intention."
            )

        return (
            f"The route {path_label} reflects weak constraint filtering. "
            "No strong intentional reading is justified."
        )

    def _correction_principle(
        self,
        *,
        constructive_nodes: list[str],
        tension_wells: list[str],
        strained_gateways: list[str],
    ) -> str:
        if tension_wells:
            return (
                "Do not confuse a high-gravity crisis point with a selected target."
            )

        if strained_gateways:
            return (
                "Do not confuse costly forced passage with intentional direction."
            )

        if constructive_nodes:
            return (
                "Read target-like behavior as coherence produced by constructive attractors."
            )

        return (
            "Read weak apparent direction as projection by the observer, not as intention."
        )

    def _book_paragraph(
        self,
        *,
        case_name: str,
        path: list[str],
        targeting_score: float,
        misreading_score: float,
        main_error_source: str,
        corrected_story: str,
    ) -> str:
        path_label = " → ".join(path)

        return (
            f"In the {case_name} scenario, the visible route is {path_label}. "
            f"The apparent targeting score is {targeting_score:.2f}, while the observer "
            f"misreading score is {misreading_score:.2f}. "
            f"The main interpretive error is {main_error_source}. "
            f"{corrected_story}"
        )

    def _confidence(self, misreading_score: float, targeting_score: float) -> str:
        gap = abs(misreading_score - targeting_score)

        if gap <= 15:
            return "high"
        if gap <= 35:
            return "medium"
        return "low"
