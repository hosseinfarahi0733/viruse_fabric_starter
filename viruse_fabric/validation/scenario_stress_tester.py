from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class StressScenario:
    name: str
    path: tuple[str, ...]
    apparent_targeting_score: float
    observer_misreading_score: float
    constructive_attractor: str | None
    tension_well: str | None
    strained_gateway: str | None
    route_coherence: str
    expected_status: str
    description: str


@dataclass(frozen=True)
class StressFinding:
    scenario_name: str
    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class ScenarioStressReport:
    title: str
    output_path: str
    scenario_count: int
    finding_count: int
    error_count: int
    warning_count: int
    rejected_invalid_count: int
    passed: bool
    interpretation: str


class ScenarioStressTester:
    title = "Scenario Stress Tests v2.2"

    scenarios: tuple[StressScenario, ...] = (
        StressScenario(
            name="baseline_strained_gateway",
            path=("A", "D", "E"),
            apparent_targeting_score=8.70,
            observer_misreading_score=40.44,
            constructive_attractor=None,
            tension_well=None,
            strained_gateway="D",
            route_coherence="shortcut",
            expected_status="valid",
            description=(
                "A structured but costly shortcut route. D is a strained gateway, "
                "so apparent targeting should remain low."
            ),
        ),
        StressScenario(
            name="coherent_constructive_route",
            path=("A", "B", "C", "D", "E"),
            apparent_targeting_score=88.53,
            observer_misreading_score=91.21,
            constructive_attractor="D",
            tension_well=None,
            strained_gateway=None,
            route_coherence="coherent",
            expected_status="valid",
            description=(
                "A coherent route supported by a constructive attractor. "
                "High apparent targeting and high observer misreading are expected."
            ),
        ),
        StressScenario(
            name="constructive_attractor_removed",
            path=("A", "B", "C", "D", "E"),
            apparent_targeting_score=18.00,
            observer_misreading_score=33.00,
            constructive_attractor=None,
            tension_well=None,
            strained_gateway=None,
            route_coherence="coherent_but_unsupported",
            expected_status="valid",
            description=(
                "The route shape remains coherent, but the constructive attractor is removed. "
                "Apparent targeting should drop."
            ),
        ),
        StressScenario(
            name="spatial_tension_well_avoidance",
            path=("A", "D", "E"),
            apparent_targeting_score=0.00,
            observer_misreading_score=13.95,
            constructive_attractor=None,
            tension_well="B",
            strained_gateway=None,
            route_coherence="avoids_tension_well",
            expected_status="valid",
            description=(
                "B becomes a tension well. The path should avoid B and apparent targeting should remain low."
            ),
        ),
        StressScenario(
            name="regulatory_tension_well_avoidance",
            path=("A", "D", "E"),
            apparent_targeting_score=0.00,
            observer_misreading_score=13.95,
            constructive_attractor=None,
            tension_well="C",
            strained_gateway=None,
            route_coherence="avoids_tension_well",
            expected_status="valid",
            description=(
                "C becomes a tension well. The path should avoid C and apparent targeting should remain low."
            ),
        ),
        StressScenario(
            name="invalid_everything_looks_targeted",
            path=("A", "D", "E"),
            apparent_targeting_score=95.00,
            observer_misreading_score=92.00,
            constructive_attractor=None,
            tension_well="B",
            strained_gateway="D",
            route_coherence="shortcut_with_crisis",
            expected_status="invalid",
            description=(
                "A deliberately bad case: a shortcut with crisis concentration is given high targeting. "
                "A healthy model should reject this."
            ),
        ),
        StressScenario(
            name="invalid_coherent_route_scores_zero",
            path=("A", "B", "C", "D", "E"),
            apparent_targeting_score=0.00,
            observer_misreading_score=0.00,
            constructive_attractor="D",
            tension_well=None,
            strained_gateway=None,
            route_coherence="coherent",
            expected_status="invalid",
            description=(
                "A deliberately bad case: a coherent route with constructive attractor receives zero scores. "
                "A healthy model should reject this."
            ),
        ),
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/scenario_stress_report_v2_2.md")

    def run(self) -> ScenarioStressReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        findings = self.evaluate_all()
        markdown = self.render_markdown(findings)
        self.output_path.write_text(markdown, encoding="utf-8")

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")
        rejected_invalid_count = sum(
            1
            for scenario in self.scenarios
            if scenario.expected_status == "invalid"
            and self._scenario_has_rejection(scenario, findings)
        )

        return ScenarioStressReport(
            title=self.title,
            output_path=str(self.output_path),
            scenario_count=len(self.scenarios),
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            rejected_invalid_count=rejected_invalid_count,
            passed=error_count == 0,
            interpretation=(
                "The stress test checks whether the model preserves sane relationships "
                "between route coherence, constructive attractors, tension wells, apparent targeting, "
                "and observer misreading."
            ),
        )

    def evaluate_all(self) -> tuple[StressFinding, ...]:
        findings: list[StressFinding] = []

        for scenario in self.scenarios:
            scenario_findings = self.evaluate_scenario(scenario)
            findings.extend(scenario_findings)

        return tuple(findings)

    def evaluate_scenario(self, scenario: StressScenario) -> tuple[StressFinding, ...]:
        findings: list[StressFinding] = []

        if scenario.expected_status == "valid":
            findings.extend(self._evaluate_valid_scenario(scenario))
        elif scenario.expected_status == "invalid":
            findings.extend(self._evaluate_invalid_scenario(scenario))
        else:
            findings.append(
                StressFinding(
                    scenario_name=scenario.name,
                    severity="error",
                    code="unknown_expected_status",
                    message=f"Unknown expected status: {scenario.expected_status}",
                )
            )

        return tuple(findings)

    def _evaluate_valid_scenario(self, scenario: StressScenario) -> list[StressFinding]:
        findings: list[StressFinding] = []

        if scenario.route_coherence == "coherent":
            if scenario.constructive_attractor is None:
                findings.append(
                    self._error(
                        scenario,
                        "missing_constructive_attractor",
                        "Coherent high-targeting routes should have a constructive attractor.",
                    )
                )

            if scenario.apparent_targeting_score < 70.0:
                findings.append(
                    self._error(
                        scenario,
                        "coherent_route_low_targeting",
                        "A coherent route with constructive support should not have low apparent targeting.",
                    )
                )

            if scenario.observer_misreading_score < 70.0:
                findings.append(
                    self._warning(
                        scenario,
                        "coherent_route_low_misreading",
                        "A highly coherent target-like route usually creates high observer misreading risk.",
                    )
                )

        if scenario.route_coherence == "coherent_but_unsupported":
            if scenario.constructive_attractor is not None:
                findings.append(
                    self._error(
                        scenario,
                        "unsupported_route_has_attractor",
                        "This stress case should remove the constructive attractor.",
                    )
                )

            if scenario.apparent_targeting_score > 40.0:
                findings.append(
                    self._error(
                        scenario,
                        "unsupported_route_targeting_too_high",
                        "Removing constructive support should reduce apparent targeting.",
                    )
                )

        if scenario.route_coherence == "avoids_tension_well":
            if scenario.tension_well is None:
                findings.append(
                    self._error(
                        scenario,
                        "missing_tension_well",
                        "A tension-well avoidance case must declare a tension well.",
                    )
                )

            if scenario.tension_well in scenario.path:
                findings.append(
                    self._error(
                        scenario,
                        "path_enters_tension_well",
                        "A valid avoidance route should not pass through the tension well.",
                    )
                )

            if scenario.apparent_targeting_score > 20.0:
                findings.append(
                    self._error(
                        scenario,
                        "tension_well_targeting_too_high",
                        "Tension well avoidance should not create high apparent targeting.",
                    )
                )

        if scenario.route_coherence == "shortcut":
            if scenario.strained_gateway is None:
                findings.append(
                    self._error(
                        scenario,
                        "shortcut_missing_gateway",
                        "A shortcut baseline should identify its strained gateway.",
                    )
                )

            if scenario.apparent_targeting_score > 25.0:
                findings.append(
                    self._error(
                        scenario,
                        "shortcut_targeting_too_high",
                        "A costly shortcut should not be treated as strongly target-like.",
                    )
                )

        return findings

    def _evaluate_invalid_scenario(self, scenario: StressScenario) -> list[StressFinding]:
        rejection_reasons = self._invalid_rejection_reasons(scenario)

        if not rejection_reasons:
            return [
                self._error(
                    scenario,
                    "invalid_case_not_rejected",
                    "The model accepted a deliberately invalid stress case.",
                )
            ]

        return [
            StressFinding(
                scenario_name=scenario.name,
                severity="info",
                code="invalid_case_rejected",
                message="Invalid case rejected: " + "; ".join(rejection_reasons),
            )
        ]

    def _invalid_rejection_reasons(self, scenario: StressScenario) -> list[str]:
        reasons: list[str] = []

        if (
            scenario.apparent_targeting_score >= 80.0
            and scenario.constructive_attractor is None
        ):
            reasons.append("high targeting without constructive attractor")

        if (
            scenario.tension_well is not None
            and scenario.apparent_targeting_score >= 70.0
        ):
            reasons.append("tension well case given high targeting")

        if (
            scenario.strained_gateway is not None
            and scenario.apparent_targeting_score >= 70.0
        ):
            reasons.append("strained gateway misread as strong target")

        if (
            scenario.route_coherence == "coherent"
            and scenario.constructive_attractor is not None
            and scenario.apparent_targeting_score <= 5.0
        ):
            reasons.append("coherent constructive route scored near zero")

        return reasons

    def _scenario_has_rejection(
        self,
        scenario: StressScenario,
        findings: tuple[StressFinding, ...],
    ) -> bool:
        return any(
            finding.scenario_name == scenario.name
            and finding.code == "invalid_case_rejected"
            for finding in findings
        )

    def render_markdown(self, findings: tuple[StressFinding, ...]) -> str:
        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This report stress-tests the internal logic of Viruse Fabric. "
                "It does not validate the model against external empirical data. "
                "Instead, it checks whether core relationships remain sane under disrupted, unsupported, and deliberately invalid scenarios."
            ),
            "",
            "## Stress Scenarios",
            "",
            "| Scenario | Expected | Path | Targeting | Misreading | Constructive attractor | Tension well | Strained gateway |",
            "|---|---|---|---:|---:|---|---|---|",
        ]

        for scenario in self.scenarios:
            lines.append(
                "| "
                f"{scenario.name} | "
                f"{scenario.expected_status} | "
                f"{' → '.join(scenario.path)} | "
                f"{scenario.apparent_targeting_score:.2f} | "
                f"{scenario.observer_misreading_score:.2f} | "
                f"{scenario.constructive_attractor or 'none'} | "
                f"{scenario.tension_well or 'none'} | "
                f"{scenario.strained_gateway or 'none'} |"
            )

        lines.extend(
            [
                "",
                "## Findings",
                "",
            ]
        )

        if not findings:
            lines.append("No findings.")
        else:
            lines.extend(
                [
                    "| Scenario | Severity | Code | Message |",
                    "|---|---|---|---|",
                ]
            )

            for finding in findings:
                lines.append(
                    f"| {finding.scenario_name} | {finding.severity} | "
                    f"{finding.code} | {finding.message} |"
                )

        lines.extend(
            [
                "",
                "## Interpretation",
                "",
                (
                    "A healthy model should not make everything look target-like. "
                    "It should also not flatten every scenario into zero meaning. "
                    "The useful region is between these failures: coherent constructive routes may appear target-like, "
                    "while tension wells, unsupported routes, and strained gateways should not be automatically promoted to intention."
                ),
                "",
                "## Boundary",
                "",
                (
                    "This stress test is conceptual and non-operational. "
                    "It does not use real pathogens, real hosts, biological protocols, or executable interventions."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def _error(self, scenario: StressScenario, code: str, message: str) -> StressFinding:
        return StressFinding(
            scenario_name=scenario.name,
            severity="error",
            code=code,
            message=message,
        )

    def _warning(self, scenario: StressScenario, code: str, message: str) -> StressFinding:
        return StressFinding(
            scenario_name=scenario.name,
            severity="warning",
            code=code,
            message=message,
        )

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
