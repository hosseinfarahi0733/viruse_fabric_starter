from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import re


@dataclass(frozen=True)
class SensitivityCase:
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


@dataclass(frozen=True)
class WeightProfile:
    name: str
    constructive_weight: float
    path_weight: float
    gravity_weight: float
    cost_weight: float
    salience_weight: float
    tension_penalty_weight: float
    gateway_penalty_weight: float


@dataclass(frozen=True)
class SensitivityRun:
    profile_name: str
    top_case: str
    supported_score: float
    ablated_score: float
    shortcut_score: float
    tension_well_score: float
    stable: bool


@dataclass(frozen=True)
class SensitivityFinding:
    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class ParameterSensitivityReport:
    title: str
    output_path: str
    case_count: int
    profile_count: int
    stable_count: int
    unstable_count: int
    stability_rate: float
    finding_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class ParameterSensitivitySweeper:
    title = "Parameter Sensitivity Sweep v2.6"

    minimum_stability_rate = 0.80
    maximum_ablated_score = 50.0
    maximum_shortcut_score = 35.0
    maximum_tension_well_score = 25.0

    cases: tuple[SensitivityCase, ...] = (
        SensitivityCase(
            name="supported_constructive_route",
            path=("A", "B", "C", "D", "E"),
            constructive_support=0.95,
            path_coverage=0.98,
            gravity_alignment=0.90,
            cost_efficiency=0.85,
            observer_salience=0.90,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_role="should remain highest",
        ),
        SensitivityCase(
            name="ablated_route",
            path=("A", "B", "C", "D", "E"),
            constructive_support=0.05,
            path_coverage=0.98,
            gravity_alignment=0.15,
            cost_efficiency=0.35,
            observer_salience=0.30,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_role="should remain below supported route",
        ),
        SensitivityCase(
            name="shortcut_gateway_route",
            path=("A", "D", "E"),
            constructive_support=0.10,
            path_coverage=0.55,
            gravity_alignment=0.30,
            cost_efficiency=0.30,
            observer_salience=0.40,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.60,
            expected_role="should remain low",
        ),
        SensitivityCase(
            name="tension_well_route",
            path=("A", "D", "E"),
            constructive_support=0.05,
            path_coverage=0.40,
            gravity_alignment=0.10,
            cost_efficiency=0.20,
            observer_salience=0.35,
            tension_well_penalty=0.80,
            strained_gateway_penalty=0.00,
            expected_role="should remain lowest",
        ),
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/parameter_sensitivity_v2_6.md")

    def run(self) -> ParameterSensitivityReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        profiles = self.weight_profiles()
        runs = tuple(self.evaluate_profile(profile) for profile in profiles)
        findings = self.evaluate_runs(runs)

        stable_count = sum(1 for run in runs if run.stable)
        unstable_count = len(runs) - stable_count
        stability_rate = stable_count / len(runs) if runs else 0.0

        markdown = self.render_markdown(runs, findings, stability_rate)
        self.output_path.write_text(markdown, encoding="utf-8")

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")

        return ParameterSensitivityReport(
            title=self.title,
            output_path=str(self.output_path),
            case_count=len(self.cases),
            profile_count=len(profiles),
            stable_count=stable_count,
            unstable_count=unstable_count,
            stability_rate=stability_rate,
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            passed=error_count == 0,
            interpretation=(
                "The sensitivity sweep checks whether the supported constructive route remains dominant "
                "under moderate scoring-weight perturbations."
            ),
        )

    def weight_profiles(self) -> tuple[WeightProfile, ...]:
        multipliers = (0.80, 1.00, 1.20)
        profiles: list[WeightProfile] = []

        base = {
            "constructive": 30.0,
            "path": 25.0,
            "gravity": 20.0,
            "cost": 15.0,
            "salience": 10.0,
            "tension": 35.0,
            "gateway": 25.0,
        }

        for i, (c, p, g, cost, salience, penalty) in enumerate(
            product(multipliers, multipliers, multipliers, multipliers, multipliers, multipliers),
            1,
        ):
            profiles.append(
                WeightProfile(
                    name=f"profile_{i:03d}",
                    constructive_weight=base["constructive"] * c,
                    path_weight=base["path"] * p,
                    gravity_weight=base["gravity"] * g,
                    cost_weight=base["cost"] * cost,
                    salience_weight=base["salience"] * salience,
                    tension_penalty_weight=base["tension"] * penalty,
                    gateway_penalty_weight=base["gateway"] * penalty,
                )
            )

        return tuple(profiles)

    def evaluate_profile(self, profile: WeightProfile) -> SensitivityRun:
        scores = {case.name: self.score_case(case, profile) for case in self.cases}
        top_case = max(scores, key=scores.get)

        supported = scores["supported_constructive_route"]
        ablated = scores["ablated_route"]
        shortcut = scores["shortcut_gateway_route"]
        tension = scores["tension_well_route"]

        stable = (
            top_case == "supported_constructive_route"
            and ablated <= self.maximum_ablated_score
            and shortcut <= self.maximum_shortcut_score
            and tension <= self.maximum_tension_well_score
        )

        return SensitivityRun(
            profile_name=profile.name,
            top_case=top_case,
            supported_score=supported,
            ablated_score=ablated,
            shortcut_score=shortcut,
            tension_well_score=tension,
            stable=stable,
        )

    def score_case(self, case: SensitivityCase, profile: WeightProfile) -> float:
        raw = (
            profile.constructive_weight * case.constructive_support
            + profile.path_weight * case.path_coverage
            + profile.gravity_weight * case.gravity_alignment
            + profile.cost_weight * case.cost_efficiency
            + profile.salience_weight * case.observer_salience
            - profile.tension_penalty_weight * case.tension_well_penalty
            - profile.gateway_penalty_weight * case.strained_gateway_penalty
        )
        return self._clamp(raw)

    def evaluate_runs(self, runs: tuple[SensitivityRun, ...]) -> tuple[SensitivityFinding, ...]:
        findings: list[SensitivityFinding] = []

        stable_count = sum(1 for run in runs if run.stable)
        stability_rate = stable_count / len(runs) if runs else 0.0

        if stability_rate < self.minimum_stability_rate:
            findings.append(
                SensitivityFinding(
                    severity="error",
                    code="stability_rate_too_low",
                    message=(
                        f"Stability rate {stability_rate:.2%} is below required "
                        f"{self.minimum_stability_rate:.2%}."
                    ),
                )
            )

        top_failures = [run for run in runs if run.top_case != "supported_constructive_route"]
        if top_failures:
            findings.append(
                SensitivityFinding(
                    severity="error",
                    code="supported_route_not_dominant",
                    message=f"Supported route failed to remain top in {len(top_failures)} profiles.",
                )
            )

        ablated_failures = [
            run for run in runs if run.ablated_score > self.maximum_ablated_score
        ]
        if ablated_failures:
            findings.append(
                SensitivityFinding(
                    severity="error",
                    code="ablated_route_too_high",
                    message=f"Ablated route exceeded threshold in {len(ablated_failures)} profiles.",
                )
            )

        shortcut_failures = [
            run for run in runs if run.shortcut_score > self.maximum_shortcut_score
        ]
        if shortcut_failures:
            findings.append(
                SensitivityFinding(
                    severity="error",
                    code="shortcut_route_too_high",
                    message=f"Shortcut route exceeded threshold in {len(shortcut_failures)} profiles.",
                )
            )

        tension_failures = [
            run for run in runs if run.tension_well_score > self.maximum_tension_well_score
        ]
        if tension_failures:
            findings.append(
                SensitivityFinding(
                    severity="error",
                    code="tension_well_route_too_high",
                    message=f"Tension well route exceeded threshold in {len(tension_failures)} profiles.",
                )
            )

        if not findings:
            findings.append(
                SensitivityFinding(
                    severity="info",
                    code="sensitivity_passed",
                    message=(
                        "The scenario ranking and key thresholds remained stable across all tested weight profiles."
                    ),
                )
            )

        return tuple(findings)

    def render_markdown(
        self,
        runs: tuple[SensitivityRun, ...],
        findings: tuple[SensitivityFinding, ...],
        stability_rate: float,
    ) -> str:
        unstable_runs = [run for run in runs if not run.stable]

        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This sensitivity sweep tests whether the main validation result depends on one fragile weight setting. "
                "A useful model should remain stable under moderate scoring-weight perturbations."
            ),
            "",
            "## Thresholds",
            "",
            f"- Minimum stability rate: {self.minimum_stability_rate:.2%}",
            f"- Maximum ablated route score: {self.maximum_ablated_score:.2f}",
            f"- Maximum shortcut route score: {self.maximum_shortcut_score:.2f}",
            f"- Maximum tension well route score: {self.maximum_tension_well_score:.2f}",
            "",
            "## Summary",
            "",
            f"- Profiles tested: {len(runs)}",
            f"- Stable profiles: {sum(1 for run in runs if run.stable)}",
            f"- Unstable profiles: {len(unstable_runs)}",
            f"- Stability rate: {stability_rate:.2%}",
            "",
            "## Representative stable runs",
            "",
            "| Profile | Top case | Supported | Ablated | Shortcut | Tension well | Stable |",
            "|---|---|---:|---:|---:|---:|---|",
        ]

        for run in runs[:12]:
            lines.append(
                f"| {run.profile_name} | {run.top_case} | "
                f"{run.supported_score:.2f} | {run.ablated_score:.2f} | "
                f"{run.shortcut_score:.2f} | {run.tension_well_score:.2f} | {run.stable} |"
            )

        lines.extend(
            [
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
                    "The sensitivity sweep passes only if the supported constructive route remains dominant "
                    "and disrupted or unsupported cases do not become strongly target-like under moderate perturbations."
                ),
                "",
                "## Boundary",
                "",
                (
                    "This sensitivity analysis is conceptual and non-operational. "
                    "It does not use real pathogens, real hosts, biological protocols, laboratory procedures, "
                    "or executable interventions."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def _clamp(self, value: float) -> float:
        return max(0.0, min(100.0, value))

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
