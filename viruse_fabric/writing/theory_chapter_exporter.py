from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from viruse_fabric.biology.apparent_targeting import ApparentTargetingAnalyzer
from viruse_fabric.biology.scenario_auditor import ScenarioSafetyConsistencyAuditor
from viruse_fabric.biology.viral_scenarios import (
    ViralPatternScenario,
    build_viral_pattern_scenarios,
)
from viruse_fabric.geometry.attractor_classifier import AttractorTypeClassifier
from viruse_fabric.simulation.intention_correction import IntentionCorrectionEngine
from viruse_fabric.simulation.observer_misreading import ObserverMisreadingEngine


@dataclass
class ChapterExportResult:
    output_path: Path
    title: str
    scenario_count: int
    safety_status: str
    total_findings: int
    word_count: int

    @property
    def interpretation(self) -> str:
        if self.safety_status == "pass":
            return "chapter export completed with safe conceptual boundary"
        if self.safety_status == "warning":
            return "chapter export completed but contains warnings"
        return "chapter export should be reviewed before use"


class TheoryChapterExporter:
    """Export a theory chapter from the simulator.

    This converts model outputs into a readable theoretical chapter.

    It does not claim biological operational validity.
    It does not describe real pathogens.
    It does not give protocols.

    It just makes the theory readable, because apparently humans insist on prose.
    """

    def __init__(self) -> None:
        self.targeting_analyzer = ApparentTargetingAnalyzer()
        self.classifier = AttractorTypeClassifier()
        self.misreading_engine = ObserverMisreadingEngine()
        self.correction_engine = IntentionCorrectionEngine()
        self.auditor = ScenarioSafetyConsistencyAuditor()

    def export(
        self,
        *,
        output_path: str | Path = "outputs/theory_chapter_v1_7.md",
        title: str = "Apparent Targeting Without Intention",
    ) -> ChapterExportResult:
        scenarios = build_viral_pattern_scenarios()
        audit_report = self.auditor.audit(scenarios)

        chapter = self._build_chapter(
            title=title,
            scenarios=scenarios,
            safety_status=audit_report.status,
            total_findings=audit_report.total_findings,
            safety_interpretation=audit_report.interpretation,
        )

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(chapter, encoding="utf-8")

        word_count = len(chapter.split())

        return ChapterExportResult(
            output_path=path,
            title=title,
            scenario_count=len(scenarios),
            safety_status=audit_report.status,
            total_findings=audit_report.total_findings,
            word_count=word_count,
        )

    def _build_chapter(
        self,
        *,
        title: str,
        scenarios: list[ViralPatternScenario],
        safety_status: str,
        total_findings: int,
        safety_interpretation: str,
    ) -> str:
        parts: list[str] = []

        parts.append(self._front_matter(title))
        parts.append(self._problem_section())
        parts.append(self._model_section())
        parts.append(self._scenario_table_section(scenarios))
        parts.append(self._results_section(scenarios))
        parts.append(self._observer_error_section(scenarios))
        parts.append(self._correction_section(scenarios))
        parts.append(
            self._safety_section(
                safety_status=safety_status,
                total_findings=total_findings,
                safety_interpretation=safety_interpretation,
            )
        )
        parts.append(self._closing_section())

        return "\n\n".join(parts).strip() + "\n"

    def _front_matter(self, title: str) -> str:
        return dedent(
            f"""
            # {title}

            **Project:** Viruse Fabric  
            **Chapter type:** computational-theoretical draft  
            **Core claim:** Causality is not a chain; it is a geometry of constraints.

            > هدفمندی ظاهری، قصد نیست؛ نتیجه‌ی هم‌راستایی مسیر، جاذب‌های سازنده و فیلترهای بافت است.
            """
        ).strip()

    def _problem_section(self) -> str:
        return dedent(
            """
            ## 1. Problem

            Some biological patterns appear target-like. A viral pattern may seem to select a host,
            a tissue, a cell state, or an outcome. The ordinary observer often compresses this into
            a simple story: the pattern wanted the endpoint.

            This project rejects that shortcut.

            In this model, intention is not placed inside the viral pattern. Instead, apparent
            targeting is treated as an observer-visible effect of route coherence inside a fabric of
            constraints. A route may look selected when it is stable, efficient, supported by
            constructive attractors, and filtered away from tension wells.

            The question is therefore not:

            **What does the virus intend?**

            The question is:

            **What kind of causal fabric makes a route appear intentional to an observer?**
            """
        ).strip()

    def _model_section(self) -> str:
        return dedent(
            """
            ## 2. Model

            The model represents events as nodes inside a causal fabric. The fabric contains
            constraints, tensions, space-time couplings, causal curvature, geodesic-like routes,
            and observer projections.

            The key computational layers are:

            1. **Causal curvature:** identifies nodes that concentrate tension, pressure, and connectivity.
            2. **Causal geodesic:** finds low-cost routes through the fabric.
            3. **Attractor classification:** separates constructive attractors from tension wells.
            4. **Apparent Targeting Index:** estimates how target-like a route appears.
            5. **Observer Misreading Engine:** estimates when route coherence is mistaken for intention.
            6. **Intention Correction Report:** rewrites the observer's mistaken story into a constraint-based explanation.

            The model deliberately remains abstract. It does not encode real pathogens, hosts,
            receptors, doses, protocols, or interventions.
            """
        ).strip()

    def _scenario_table_section(self, scenarios: list[ViralPatternScenario]) -> str:
        lines = [
            "## 3. Safe Viral-Pattern Scenario Layer",
            "",
            "The abstract nodes are translated into safe biological-facing language:",
            "",
            "| Node | Biological-facing role | Safe abstraction |",
            "|---|---|---|",
        ]

        first = scenarios[0].fabric
        for node_id in ["A", "B", "C", "D", "E"]:
            node = first.nodes[node_id]
            role = str(node.state.get("biological_role", ""))
            safe = str(node.state.get("safe_abstraction", ""))
            lines.append(f"| {node_id} | {role} | {safe} |")

        lines.extend(
            [
                "",
                "The tested scenarios are:",
                "",
                "| Scenario | Reading | Expected mechanism |",
                "|---|---|---|",
            ]
        )

        for scenario in scenarios:
            lines.append(
                f"| {scenario.name} | {scenario.biological_reading} | {scenario.expected_mechanism} |"
            )

        return "\n".join(lines)

    def _results_section(self, scenarios: list[ViralPatternScenario]) -> str:
        lines = [
            "## 4. Results: Apparent Targeting and Attractor Roles",
            "",
            "| Scenario | Path | Targeting score | Constructive nodes | Tension wells | Strained gateways | Interpretation |",
            "|---|---:|---:|---|---|---|---|",
        ]

        for scenario in scenarios:
            targeting = self.targeting_analyzer.analyze(
                scenario.fabric,
                case_name=scenario.name,
            )
            classification = self.classifier.classify(
                scenario.fabric,
                case_name=scenario.name,
            )

            lines.append(
                "| "
                f"{scenario.name} | "
                f"{' → '.join(targeting.path)} | "
                f"{targeting.score:.2f} | "
                f"{', '.join(classification.constructive_nodes) or 'none'} | "
                f"{', '.join(classification.tension_wells) or 'none'} | "
                f"{', '.join(classification.strained_gateways) or 'none'} | "
                f"{targeting.interpretation} |"
            )

        lines.append(
            dedent(
                """

                The coherent viral-pattern scenario produces high apparent targeting because the route
                is complete, efficient, and supported by a constructive attractor. The disrupted
                scenarios collapse into low apparent targeting because their dominant attractors become
                tension wells rather than stable route organizers.
                """
            ).strip()
        )

        return "\n".join(lines)

    def _observer_error_section(self, scenarios: list[ViralPatternScenario]) -> str:
        lines = [
            "## 5. Observer Misreading",
            "",
            "| Scenario | Targeting score | Misreading score | Main risk |",
            "|---|---:|---:|---|",
        ]

        for scenario in scenarios:
            misreading = self.misreading_engine.analyze(
                scenario.fabric,
                case_name=scenario.name,
            )

            lines.append(
                "| "
                f"{scenario.name} | "
                f"{misreading.apparent_targeting_score:.2f} | "
                f"{misreading.misreading_score:.2f} | "
                f"{misreading.interpretation} |"
            )

        lines.append(
            dedent(
                """

                Observer misreading occurs when route coherence, endpoint visibility, and dominant
                attractors are compressed into a story of intention. This is a reading error, not a
                property of the route itself.
                """
            ).strip()
        )

        return "\n".join(lines)

    def _correction_section(self, scenarios: list[ViralPatternScenario]) -> str:
        lines = [
            "## 6. Correcting the Intention Story",
            "",
        ]

        for scenario in scenarios:
            correction = self.correction_engine.generate(
                scenario.fabric,
                case_name=scenario.name,
            )

            lines.extend(
                [
                    f"### {scenario.name}",
                    "",
                    f"**Mistaken story:** {correction.mistaken_story}",
                    "",
                    f"**Corrected story:** {correction.corrected_story}",
                    "",
                    f"**Correction principle:** {correction.correction_principle}",
                    "",
                    f"**Book paragraph:** {correction.book_paragraph}",
                    "",
                ]
            )

        return "\n".join(lines).strip()

    def _safety_section(
        self,
        *,
        safety_status: str,
        total_findings: int,
        safety_interpretation: str,
    ) -> str:
        return dedent(
            f"""
            ## 7. Safety and Abstraction Boundary

            The scenario layer was audited before export.

            - Audit status: **{safety_status}**
            - Total findings: **{total_findings}**
            - Interpretation: **{safety_interpretation}**

            This chapter is non-operational. It does not describe real pathogens, hosts, doses,
            receptors, protocols, laboratory procedures, or interventions.

            The purpose of the scenario layer is explanatory: it translates abstract causal roles
            into safe biological-facing language without turning the model into an actionable
            biological system.
            """
        ).strip()

    def _closing_section(self) -> str:
        return dedent(
            """
            ## 8. Closing Claim

            Apparent targeting does not require intention. A route can look target-like when a
            constraint fabric makes it coherent, efficient, and visible. The observer then compresses
            this route into a story of selection or purpose.

            The corrected reading is:

            **Intention is not a property of the path. It is an observer's compressed interpretation
            of a coherent route through a fabric of constraints.**

            In Persian:

            **قصد، ویژگی مسیر نیست؛ قصد، خوانش فشرده و اشتباه مشاهده‌گر از مسیرهای هم‌راستا و پرجاذبه است.**
            """
        ).strip()
