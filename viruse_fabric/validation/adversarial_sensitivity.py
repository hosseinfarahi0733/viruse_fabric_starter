from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import re


@dataclass(frozen=True)
class AdversarialCase:
    name: str
    constructive_support: float
    path_coverage: float
    gravity_alignment: float
    cost_efficiency: float
    observer_salience: float
    tension_well_penalty: float
    strained_gateway_penalty: float
    expected_role: str


@dataclass(frozen=True)
class AdversarialWeightProfile:
    name: str
    constructive_weight: float
    path_weight: float
    gravity_weight: float
    cost_weight: float
    salience_weight: float
    tension_penalty_weight: float
    gateway_penalty_weight: float


@dataclass(frozen=True)
class AdversarialRun:
    profile_name: str
    top_case: str
    supported_score: float
    strongest_rival_score: float
    supported_margin: float
    stable: bool
    failure_reason: str | None
    scores: dict[str, float]


@dataclass(frozen=True)
class AdversarialFinding:
    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class AdversarialSensitivityReport:
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


class AdversarialSensitivitySweeper:
    title = "Adversarial Sensitivity Sweep v2.7"

    minimum_stability_rate = 0.70
    minimum_supported_margin = 10.0

    maximum_ablated_score = 65.0
    maximum_shortcut_score = 50.0
    maximum_tension_well_score = 40.0

    cases: tuple[AdversarialCase, ...] = (
        AdversarialCase(
            name="supported_constructive_route",
            constructive_support=0.95,
            path_coverage=0.98,
            gravity_alignment=0.90,
            cost_efficiency=0.85,
            observer_salience=0.90,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_role="should usually remain highest with a clear margin",
        ),
        AdversarialCase(
            name="ablated_route",
            constructive_support=0.05,
            path_coverage=0.98,
            gravity_alignment=0.15,
            cost_efficiency=0.35,
            observer_salience=0.30,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_role="should not become strongly target-like",
        ),
        AdversarialCase(
            name="shortcut_gateway_route",
            constructive_support=0.10,
            path_coverage=0.55,
            gravity_alignment=0.30,
            cost_efficiency=0.30,
            observer_salience=0.40,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.60,
            expected_role="should remain low unless gateway penalties are aggressively weakened",
        ),
        AdversarialCase(
            name="tension_well_route",
            constructive_support=0.05,
            path_coverage=0.40,
            gravity_alignment=0.10,
            cost_efficiency=0.20,
            observer_salience=0.35,
            tension_well_penalty=0.80,
            strained_gateway_penalty=0.00,
            expected_role="should never become top-ranked",
        ),
        AdversarialCase(
            name="high_salience_ablated_decoy",
            constructive_support=0.04,
            path_coverage=0.92,
            gravity_alignment=0.28,
            cost_efficiency=0.55,
            observer_salience=0.98,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_role="tests whether observer salience can fake targeting",
        ),
        AdversarialCase(
            name="high_path_shortcut_decoy",
            constructive_support=0.12,
            path_coverage=0.92,
            gravity_alignment=0.50,
            cost_efficiency=0.62,
            observer_salience=0.72,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.18,
            expected_role="tests whether a visually efficient shortcut can fool the ranking",
        ),
        AdversarialCase(
            name="low_penalty_tension_decoy",
            constructive_support=0.05,
            path_coverage=0.74,
            gravity_alignment=0.55,
            cost_efficiency=0.62,
            observer_salience=0.80,
            tension_well_penalty=0.25,
            strained_gateway_penalty=0.00,
            expected_role="tests whether weakened tension penalties create false attractors",
        ),
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/adversarial_sensitivity_v2_7.md")

    def run(self) -> AdversarialSensitivityReport:
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

        return AdversarialSensitivityReport(
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
                "The adversarial sweep tests whether the model remains usable when scoring weights and decoy cases "
                "are pushed toward hostile but still interpretable configurations."
            ),
        )

    def weight_profiles(self) -> tuple[AdversarialWeightProfile, ...]:
        constructive_multipliers = (0.10, 0.25, 0.60, 1.00, 1.40)
        path_multipliers = (0.70, 1.00, 1.50, 2.20)
        gravity_multipliers = (0.35, 1.00, 1.80)
        cost_multipliers = (0.35, 1.00, 1.80)
        salience_multipliers = (0.35, 1.00, 2.50)
        tension_penalty_multipliers = (0.05, 0.25, 0.70, 1.40)
        gateway_penalty_multipliers = (0.05, 0.25, 0.70, 1.40)

        base = {
            "constructive": 30.0,
            "path": 25.0,
            "gravity": 20.0,
            "cost": 15.0,
            "salience": 10.0,
            "tension": 35.0,
            "gateway": 25.0,
        }

        profiles: list[AdversarialWeightProfile] = []

        for i, (c, p, g, cost, salience, tension_penalty, gateway_penalty) in enumerate(
            product(
                constructive_multipliers,
                path_multipliers,
                gravity_multipliers,
                cost_multipliers,
                salience_multipliers,
                tension_penalty_multipliers,
                gateway_penalty_multipliers,
            ),
            1,
        ):
            profiles.append(
                AdversarialWeightProfile(
                    name=f"adversarial_profile_{i:04d}",
                    constructive_weight=base["constructive"] * c,
                    path_weight=base["path"] * p,
                    gravity_weight=base["gravity"] * g,
                    cost_weight=base["cost"] * cost,
                    salience_weight=base["salience"] * salience,
                    tension_penalty_weight=base["tension"] * tension_penalty,
                    gateway_penalty_weight=base["gateway"] * gateway_penalty,
                )
            )

        return tuple(profiles)

    def evaluate_profile(self, profile: AdversarialWeightProfile) -> AdversarialRun:
        scores = {case.name: self.score_case(case, profile) for case in self.cases}
        top_case = max(scores, key=scores.get)

        supported_score = scores["supported_constructive_route"]
        strongest_rival_score = max(
            score for case_name, score in scores.items()
            if case_name != "supported_constructive_route"
        )
        supported_margin = supported_score - strongest_rival_score

        failure_reason = self.failure_reason(
            top_case=top_case,
            supported_margin=supported_margin,
            scores=scores,
        )

        return AdversarialRun(
            profile_name=profile.name,
            top_case=top_case,
            supported_score=supported_score,
            strongest_rival_score=strongest_rival_score,
            supported_margin=supported_margin,
            stable=failure_reason is None,
            failure_reason=failure_reason,
            scores=scores,
        )

    def failure_reason(
        self,
        top_case: str,
        supported_margin: float,
        scores: dict[str, float],
    ) -> str | None:
        if "tension" in top_case:
            return "tension-like case became top-ranked"

        if top_case != "supported_constructive_route":
            return f"{top_case} became top-ranked"

        if supported_margin < self.minimum_supported_margin:
            return "supported route won without enough margin"

        if scores["ablated_route"] > self.maximum_ablated_score:
            return "ablated route exceeded adversarial threshold"

        if scores["shortcut_gateway_route"] > self.maximum_shortcut_score:
            return "shortcut gateway route exceeded adversarial threshold"

        if scores["tension_well_route"] > self.maximum_tension_well_score:
            return "tension well route exceeded adversarial threshold"

        return None

    def score_case(self, case: AdversarialCase, profile: AdversarialWeightProfile) -> float:
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

    def evaluate_runs(self, runs: tuple[AdversarialRun, ...]) -> tuple[AdversarialFinding, ...]:
        findings: list[AdversarialFinding] = []

        stable_count = sum(1 for run in runs if run.stable)
        stability_rate = stable_count / len(runs) if runs else 0.0
        reason_counts = self.failure_reason_counts(runs)

        if stability_rate < self.minimum_stability_rate:
            findings.append(
                AdversarialFinding(
                    severity="error",
                    code="adversarial_stability_too_low",
                    message=(
                        f"Adversarial stability rate {stability_rate:.2%} is below required "
                        f"{self.minimum_stability_rate:.2%}."
                    ),
                )
            )

        tension_top_count = sum(
            1 for run in runs
            if "tension" in run.top_case and run.top_case != "supported_constructive_route"
        )
        if tension_top_count > 0:
            findings.append(
                AdversarialFinding(
                    severity="error",
                    code="tension_like_case_became_top",
                    message=f"A tension-like case became top-ranked in {tension_top_count} profiles.",
                )
            )

        for reason, count in reason_counts.items():
            findings.append(
                AdversarialFinding(
                    severity="warning",
                    code=self.reason_to_code(reason),
                    message=f"{reason}: {count} profiles.",
                )
            )

        if not findings:
            findings.append(
                AdversarialFinding(
                    severity="info",
                    code="adversarial_sensitivity_passed",
                    message="The model remained stable under adversarial weight perturbations and decoy pressure.",
                )
            )

        return tuple(findings)

    def render_markdown(
        self,
        runs: tuple[AdversarialRun, ...],
        findings: tuple[AdversarialFinding, ...],
        stability_rate: float,
    ) -> str:
        unstable_runs = [run for run in runs if not run.stable]
        margins = sorted(run.supported_margin for run in runs)
        top_counts = self.top_case_counts(runs)
        reason_counts = self.failure_reason_counts(runs)

        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This adversarial sensitivity sweep pushes scoring weights into hostile but interpretable configurations "
                "and adds decoy cases designed to mimic targeting without strong constructive support."
            ),
            "",
            "## Thresholds",
            "",
            f"- Minimum adversarial stability rate: {self.minimum_stability_rate:.2%}",
            f"- Minimum supported-route margin: {self.minimum_supported_margin:.2f}",
            f"- Maximum ablated route score: {self.maximum_ablated_score:.2f}",
            f"- Maximum shortcut route score: {self.maximum_shortcut_score:.2f}",
            f"- Maximum tension well route score: {self.maximum_tension_well_score:.2f}",
            "",
            "## Summary",
            "",
            f"- Cases tested: {len(self.cases)}",
            f"- Profiles tested: {len(runs)}",
            f"- Stable profiles: {sum(1 for run in runs if run.stable)}",
            f"- Unstable profiles: {len(unstable_runs)}",
            f"- Stability rate: {stability_rate:.2%}",
            f"- Minimum supported margin: {margins[0]:.2f}",
            f"- Median supported margin: {margins[len(margins) // 2]:.2f}",
            f"- Maximum supported margin: {margins[-1]:.2f}",
            "",
            "## Top-case counts",
            "",
            "| Case | Top count |",
            "|---|---:|",
        ]

        for case_name, count in top_counts.items():
            lines.append(f"| {case_name} | {count} |")

        lines.extend(
            [
                "",
                "## Failure reason counts",
                "",
                "| Reason | Count |",
                "|---|---:|",
            ]
        )

        if reason_counts:
            for reason, count in reason_counts.items():
                lines.append(f"| {reason} | {count} |")
        else:
            lines.append("| none | 0 |")

        lines.extend(
            [
                "",
                "## Closest adversarial runs",
                "",
                "| Profile | Top case | Supported | Strongest rival | Margin | Stable | Failure reason |",
                "|---|---|---:|---:|---:|---|---|",
            ]
        )

        closest_runs = sorted(runs, key=lambda run: run.supported_margin)[:15]
        for run in closest_runs:
            lines.append(
                f"| {run.profile_name} | {run.top_case} | "
                f"{run.supported_score:.2f} | {run.strongest_rival_score:.2f} | "
                f"{run.supported_margin:.2f} | {run.stable} | {run.failure_reason or 'none'} |"
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
                    "This test does not require perfect stability. It asks whether the model remains usable under hostile "
                    "weight settings, near-tie pressure, and decoy cases. Warnings identify fragile regions without "
                    "automatically invalidating the model."
                ),
                "",
                "## Boundary",
                "",
                (
                    "This adversarial sensitivity analysis is conceptual and non-operational. "
                    "It does not use real pathogens, real hosts, biological protocols, laboratory procedures, "
                    "or executable interventions."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def top_case_counts(self, runs: tuple[AdversarialRun, ...]) -> dict[str, int]:
        counts = {case.name: 0 for case in self.cases}
        for run in runs:
            counts[run.top_case] = counts.get(run.top_case, 0) + 1
        return counts

    def failure_reason_counts(self, runs: tuple[AdversarialRun, ...]) -> dict[str, int]:
        counts: dict[str, int] = {}
        for run in runs:
            if run.failure_reason is None:
                continue
            counts[run.failure_reason] = counts.get(run.failure_reason, 0) + 1
        return counts

    def reason_to_code(self, reason: str) -> str:
        return re.sub(r"[^a-z0-9]+", "_", reason.lower()).strip("_")

    def _clamp(self, value: float) -> float:
        return max(0.0, min(100.0, value))

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
