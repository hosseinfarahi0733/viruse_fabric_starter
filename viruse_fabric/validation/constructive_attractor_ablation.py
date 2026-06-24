from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class AblationCase:
    name: str
    path: tuple[str, ...]
    constructive_support: float
    path_coverage: float
    gravity_alignment: float
    cost_efficiency: float
    observer_salience: float
    tension_well_penalty: float
    strained_gateway_penalty: float
    expected_role: str
    description: str


@dataclass(frozen=True)
class AblationScore:
    case_name: str
    apparent_targeting: float
    observer_misreading: float


@dataclass(frozen=True)
class AblationFinding:
    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class ConstructiveAttractorAblationReport:
    title: str
    output_path: str
    case_count: int
    finding_count: int
    error_count: int
    warning_count: int
    targeting_drop_percent: float
    misreading_drop_percent: float
    passed: bool
    interpretation: str


class ConstructiveAttractorAblationTester:
    title = "Constructive Attractor Ablation v2.5"

    minimum_targeting_drop_percent = 50.0
    minimum_misreading_drop_percent = 40.0
    maximum_unsupported_targeting = 45.0
    maximum_shortcut_targeting = 25.0
    maximum_tension_well_targeting = 20.0

    cases: tuple[AblationCase, ...] = (
        AblationCase(
            name="coherent_with_constructive_attractor",
            path=("A", "B", "C", "D", "E"),
            constructive_support=0.95,
            path_coverage=0.98,
            gravity_alignment=0.90,
            cost_efficiency=0.85,
            observer_salience=0.90,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_role="positive control",
            description=(
                "A coherent route with D acting as a constructive attractor. "
                "This case should produce high apparent targeting."
            ),
        ),
        AblationCase(
            name="coherent_without_constructive_attractor",
            path=("A", "B", "C", "D", "E"),
            constructive_support=0.05,
            path_coverage=0.98,
            gravity_alignment=0.15,
            cost_efficiency=0.35,
            observer_salience=0.30,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_role="ablation case",
            description=(
                "The route shape is preserved, but constructive support is removed. "
                "Apparent targeting and observer misreading should drop."
            ),
        ),
        AblationCase(
            name="shortcut_with_strained_gateway",
            path=("A", "D", "E"),
            constructive_support=0.10,
            path_coverage=0.55,
            gravity_alignment=0.30,
            cost_efficiency=0.30,
            observer_salience=0.40,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.60,
            expected_role="gateway control",
            description=(
                "A shortcut route through a strained gateway. "
                "It should not be treated as strongly target-like."
            ),
        ),
        AblationCase(
            name="tension_well_injected",
            path=("A", "D", "E"),
            constructive_support=0.05,
            path_coverage=0.40,
            gravity_alignment=0.10,
            cost_efficiency=0.20,
            observer_salience=0.35,
            tension_well_penalty=0.80,
            strained_gateway_penalty=0.00,
            expected_role="negative control",
            description=(
                "A crisis-concentration case with a strong tension well. "
                "The model should not promote it into target-like explanation."
            ),
        ),
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/constructive_attractor_ablation_v2_5.md")

    def run(self) -> ConstructiveAttractorAblationReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        scores = tuple(self.score_case(case) for case in self.cases)
        findings = self.evaluate(scores)

        supported = self._score_by_name(scores, "coherent_with_constructive_attractor")
        ablated = self._score_by_name(scores, "coherent_without_constructive_attractor")

        targeting_drop = self.percent_drop(
            supported.apparent_targeting,
            ablated.apparent_targeting,
        )
        misreading_drop = self.percent_drop(
            supported.observer_misreading,
            ablated.observer_misreading,
        )

        markdown = self.render_markdown(scores, findings, targeting_drop, misreading_drop)
        self.output_path.write_text(markdown, encoding="utf-8")

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")

        return ConstructiveAttractorAblationReport(
            title=self.title,
            output_path=str(self.output_path),
            case_count=len(self.cases),
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            targeting_drop_percent=targeting_drop,
            misreading_drop_percent=misreading_drop,
            passed=error_count == 0,
            interpretation=(
                "The ablation test checks whether constructive attractor support is necessary "
                "for high apparent targeting and observer misreading."
            ),
        )

    def score_case(self, case: AblationCase) -> AblationScore:
        targeting_raw = (
            30.0 * case.constructive_support
            + 25.0 * case.path_coverage
            + 20.0 * case.gravity_alignment
            + 15.0 * case.cost_efficiency
            + 10.0 * case.observer_salience
            - 35.0 * case.tension_well_penalty
            - 25.0 * case.strained_gateway_penalty
        )

        apparent_targeting = self._clamp(targeting_raw)

        misreading_raw = (
            0.60 * apparent_targeting
            + 25.0 * case.observer_salience
            + 10.0 * case.constructive_support
            - 15.0 * case.tension_well_penalty
            - 10.0 * case.strained_gateway_penalty
        )

        observer_misreading = self._clamp(misreading_raw)

        return AblationScore(
            case_name=case.name,
            apparent_targeting=apparent_targeting,
            observer_misreading=observer_misreading,
        )

    def evaluate(self, scores: tuple[AblationScore, ...]) -> tuple[AblationFinding, ...]:
        findings: list[AblationFinding] = []

        supported = self._score_by_name(scores, "coherent_with_constructive_attractor")
        ablated = self._score_by_name(scores, "coherent_without_constructive_attractor")
        shortcut = self._score_by_name(scores, "shortcut_with_strained_gateway")
        tension = self._score_by_name(scores, "tension_well_injected")

        targeting_drop = self.percent_drop(
            supported.apparent_targeting,
            ablated.apparent_targeting,
        )
        misreading_drop = self.percent_drop(
            supported.observer_misreading,
            ablated.observer_misreading,
        )

        if supported.apparent_targeting < 70.0:
            findings.append(
                self._error(
                    "positive_control_too_weak",
                    "The supported coherent route should have high apparent targeting.",
                )
            )

        if targeting_drop < self.minimum_targeting_drop_percent:
            findings.append(
                self._error(
                    "targeting_drop_too_small",
                    (
                        "Removing the constructive attractor did not reduce apparent targeting enough. "
                        f"Observed drop: {targeting_drop:.2f}%."
                    ),
                )
            )

        if misreading_drop < self.minimum_misreading_drop_percent:
            findings.append(
                self._error(
                    "misreading_drop_too_small",
                    (
                        "Removing the constructive attractor did not reduce observer misreading enough. "
                        f"Observed drop: {misreading_drop:.2f}%."
                    ),
                )
            )

        if ablated.apparent_targeting > self.maximum_unsupported_targeting:
            findings.append(
                self._error(
                    "unsupported_route_targeting_too_high",
                    "The unsupported coherent route remained too target-like after ablation.",
                )
            )

        if shortcut.apparent_targeting > self.maximum_shortcut_targeting:
            findings.append(
                self._error(
                    "shortcut_gateway_targeting_too_high",
                    "A strained gateway shortcut was misread as strongly target-like.",
                )
            )

        if tension.apparent_targeting > self.maximum_tension_well_targeting:
            findings.append(
                self._error(
                    "tension_well_targeting_too_high",
                    "A tension well case was promoted into target-like explanation.",
                )
            )

        if not findings:
            findings.append(
                AblationFinding(
                    severity="info",
                    code="ablation_passed",
                    message=(
                        "Constructive attractor removal reduced both apparent targeting "
                        "and observer misreading beyond the required thresholds."
                    ),
                )
            )

        return tuple(findings)

    def render_markdown(
        self,
        scores: tuple[AblationScore, ...],
        findings: tuple[AblationFinding, ...],
        targeting_drop: float,
        misreading_drop: float,
    ) -> str:
        score_by_name = {score.case_name: score for score in scores}

        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This ablation test asks whether the constructive attractor is doing real explanatory work. "
                "If removing constructive support does not reduce apparent targeting, the model is too flexible."
            ),
            "",
            "## Thresholds",
            "",
            f"- Minimum targeting drop: {self.minimum_targeting_drop_percent:.2f}%",
            f"- Minimum observer misreading drop: {self.minimum_misreading_drop_percent:.2f}%",
            f"- Maximum unsupported targeting: {self.maximum_unsupported_targeting:.2f}",
            f"- Maximum shortcut targeting: {self.maximum_shortcut_targeting:.2f}",
            f"- Maximum tension well targeting: {self.maximum_tension_well_targeting:.2f}",
            "",
            "## Cases",
            "",
            "| Case | Role | Path | Constructive support | Tension penalty | Gateway penalty | Targeting | Misreading |",
            "|---|---|---|---:|---:|---:|---:|---:|",
        ]

        for case in self.cases:
            score = score_by_name[case.name]
            lines.append(
                "| "
                f"{case.name} | "
                f"{case.expected_role} | "
                f"{' → '.join(case.path)} | "
                f"{case.constructive_support:.2f} | "
                f"{case.tension_well_penalty:.2f} | "
                f"{case.strained_gateway_penalty:.2f} | "
                f"{score.apparent_targeting:.2f} | "
                f"{score.observer_misreading:.2f} |"
            )

        lines.extend(
            [
                "",
                "## Ablation result",
                "",
                f"- Apparent targeting drop after removing constructive attractor: {targeting_drop:.2f}%",
                f"- Observer misreading drop after removing constructive attractor: {misreading_drop:.2f}%",
                "",
                "## Findings",
                "",
                "| Severity | Code | Message |",
                "|---|---|---|",
            ]
        )

        for finding in findings:
            lines.append(f"| {finding.severity} | {finding.code} | {finding.message} |")

        lines.extend(
            [
                "",
                "## Interpretation",
                "",
                (
                    "The constructive attractor passes this ablation test only if removing it causes "
                    "a large drop in apparent targeting and observer misreading. "
                    "This prevents the model from treating route shape alone as sufficient evidence of target-like organization."
                ),
                "",
                "## Boundary",
                "",
                (
                    "This ablation test is conceptual and non-operational. "
                    "It does not use real pathogens, real hosts, biological protocols, laboratory procedures, "
                    "or executable interventions."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def _score_by_name(
        self,
        scores: tuple[AblationScore, ...],
        name: str,
    ) -> AblationScore:
        for score in scores:
            if score.case_name == name:
                return score
        raise KeyError(name)

    def percent_drop(self, before: float, after: float) -> float:
        if before <= 0:
            return 0.0
        return max(0.0, ((before - after) / before) * 100.0)

    def _clamp(self, value: float) -> float:
        return max(0.0, min(100.0, value))

    def _error(self, code: str, message: str) -> AblationFinding:
        return AblationFinding(
            severity="error",
            code=code,
            message=message,
        )

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
