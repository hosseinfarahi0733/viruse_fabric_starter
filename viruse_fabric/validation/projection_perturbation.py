from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class ProjectionCase:
    name: str
    constructive_support: float
    path_coverage: float
    gravity_alignment: float
    cost_efficiency: float
    observer_salience: float
    narrative_smoothness: float
    tension_well_penalty: float
    strained_gateway_penalty: float
    expected_label: str
    expected_role: str


@dataclass(frozen=True)
class ProjectionProfile:
    name: str
    salience_bias: float
    path_bias: float
    smoothness_bias: float
    penalty_blindness: float
    constructive_visibility: float
    correction_strength: float
    expected_effect: str


@dataclass(frozen=True)
class ProjectionRun:
    case_name: str
    profile_name: str
    intrinsic_score: float
    observer_misreading_score: float
    corrected_misreading_score: float
    false_intention: bool
    corrected_false_intention: bool


@dataclass(frozen=True)
class ProjectionFinding:
    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class ProjectionPerturbationReport:
    title: str
    output_path: str
    case_count: int
    projection_count: int
    run_count: int
    intrinsic_false_positive_count: int
    observer_false_intention_count: int
    corrected_false_intention_count: int
    correction_drop_percent: float
    supported_intrinsic_margin: float
    finding_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class ProjectionPerturbationTester:
    title = "Projection Perturbation v2.9"

    target_like_threshold = 60.0
    false_intention_threshold = 60.0
    minimum_supported_intrinsic_margin = 25.0
    minimum_observer_false_intention_count = 4
    maximum_corrected_false_intention_count = 6
    minimum_correction_drop_percent = 50.0

    cases: tuple[ProjectionCase, ...] = (
        ProjectionCase(
            name="supported_constructive_route",
            constructive_support=0.95,
            path_coverage=0.98,
            gravity_alignment=0.90,
            cost_efficiency=0.85,
            observer_salience=0.90,
            narrative_smoothness=0.92,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_label="target_like",
            expected_role="should remain intrinsically target-like",
        ),
        ProjectionCase(
            name="ablated_same_shape_route",
            constructive_support=0.05,
            path_coverage=0.98,
            gravity_alignment=0.15,
            cost_efficiency=0.35,
            observer_salience=0.42,
            narrative_smoothness=0.82,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_label="negative_control",
            expected_role="same shape without constructive support should not be intrinsically target-like",
        ),
        ProjectionCase(
            name="high_salience_decoy",
            constructive_support=0.04,
            path_coverage=0.88,
            gravity_alignment=0.25,
            cost_efficiency=0.55,
            observer_salience=0.98,
            narrative_smoothness=0.90,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_label="projection_trap",
            expected_role="should trigger observer misreading under salience-biased projections",
        ),
        ProjectionCase(
            name="smooth_story_shortcut",
            constructive_support=0.12,
            path_coverage=0.90,
            gravity_alignment=0.45,
            cost_efficiency=0.62,
            observer_salience=0.72,
            narrative_smoothness=0.96,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.28,
            expected_label="projection_trap",
            expected_role="should test narrative smoothness as a false-intention source",
        ),
        ProjectionCase(
            name="tension_well_decoy",
            constructive_support=0.05,
            path_coverage=0.72,
            gravity_alignment=0.50,
            cost_efficiency=0.62,
            observer_salience=0.82,
            narrative_smoothness=0.75,
            tension_well_penalty=0.35,
            strained_gateway_penalty=0.00,
            expected_label="projection_trap",
            expected_role="should test whether penalty blindness creates false attractors",
        ),
        ProjectionCase(
            name="strained_gateway_shortcut",
            constructive_support=0.10,
            path_coverage=0.60,
            gravity_alignment=0.30,
            cost_efficiency=0.30,
            observer_salience=0.40,
            narrative_smoothness=0.45,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.70,
            expected_label="negative_control",
            expected_role="should stay low even under perturbed projection",
        ),
    )

    profiles: tuple[ProjectionProfile, ...] = (
        ProjectionProfile(
            name="balanced_observer",
            salience_bias=1.00,
            path_bias=1.00,
            smoothness_bias=1.00,
            penalty_blindness=0.00,
            constructive_visibility=1.00,
            correction_strength=0.80,
            expected_effect="moderate observer reading with visible constructive support",
        ),
        ProjectionProfile(
            name="salience_biased_observer",
            salience_bias=2.20,
            path_bias=0.85,
            smoothness_bias=1.10,
            penalty_blindness=0.25,
            constructive_visibility=0.60,
            correction_strength=0.75,
            expected_effect="inflates high-salience decoys",
        ),
        ProjectionProfile(
            name="shape_biased_observer",
            salience_bias=0.80,
            path_bias=2.10,
            smoothness_bias=1.20,
            penalty_blindness=0.20,
            constructive_visibility=0.55,
            correction_strength=0.75,
            expected_effect="inflates routes that look complete or efficient",
        ),
        ProjectionProfile(
            name="story_biased_observer",
            salience_bias=1.20,
            path_bias=0.90,
            smoothness_bias=2.30,
            penalty_blindness=0.15,
            constructive_visibility=0.50,
            correction_strength=0.70,
            expected_effect="inflates narrative smoothness",
        ),
        ProjectionProfile(
            name="penalty_blind_observer",
            salience_bias=1.35,
            path_bias=1.20,
            smoothness_bias=1.10,
            penalty_blindness=0.85,
            constructive_visibility=0.45,
            correction_strength=0.85,
            expected_effect="underreads tension wells and strained gateways",
        ),
        ProjectionProfile(
            name="constructive_blind_observer",
            salience_bias=1.40,
            path_bias=1.35,
            smoothness_bias=1.35,
            penalty_blindness=0.45,
            constructive_visibility=0.10,
            correction_strength=0.90,
            expected_effect="mostly misses constructive support and overreads surface cues",
        ),
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/projection_perturbation_v2_9.md")

    def run(self) -> ProjectionPerturbationReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        runs = tuple(
            self.evaluate_run(case, profile)
            for case in self.cases
            for profile in self.profiles
        )

        findings = self.evaluate_runs(runs)
        markdown = self.render_markdown(runs, findings)
        self.output_path.write_text(markdown, encoding="utf-8")

        intrinsic_false_positive_count = self.intrinsic_false_positive_count()
        observer_false_intention_count = sum(1 for run in runs if run.false_intention)
        corrected_false_intention_count = sum(1 for run in runs if run.corrected_false_intention)
        correction_drop_percent = self.drop_percent(
            observer_false_intention_count,
            corrected_false_intention_count,
        )
        supported_intrinsic_margin = self.supported_intrinsic_margin()

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")

        return ProjectionPerturbationReport(
            title=self.title,
            output_path=str(self.output_path),
            case_count=len(self.cases),
            projection_count=len(self.profiles),
            run_count=len(runs),
            intrinsic_false_positive_count=intrinsic_false_positive_count,
            observer_false_intention_count=observer_false_intention_count,
            corrected_false_intention_count=corrected_false_intention_count,
            correction_drop_percent=correction_drop_percent,
            supported_intrinsic_margin=supported_intrinsic_margin,
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            passed=error_count == 0,
            interpretation=(
                "The projection perturbation test checks whether observer misreading changes under projection shifts "
                "while intrinsic fabric scoring remains discriminative."
            ),
        )

    def evaluate_run(
        self,
        case: ProjectionCase,
        profile: ProjectionProfile,
    ) -> ProjectionRun:
        intrinsic_score = self.intrinsic_score(case)
        observer_misreading_score = self.observer_misreading_score(case, profile)
        corrected_misreading_score = self.corrected_misreading_score(
            case=case,
            profile=profile,
            observer_misreading_score=observer_misreading_score,
        )

        false_intention = (
            case.expected_label != "target_like"
            and observer_misreading_score >= self.false_intention_threshold
            and intrinsic_score < self.target_like_threshold
        )

        corrected_false_intention = (
            case.expected_label != "target_like"
            and corrected_misreading_score >= self.false_intention_threshold
            and intrinsic_score < self.target_like_threshold
        )

        return ProjectionRun(
            case_name=case.name,
            profile_name=profile.name,
            intrinsic_score=intrinsic_score,
            observer_misreading_score=observer_misreading_score,
            corrected_misreading_score=corrected_misreading_score,
            false_intention=false_intention,
            corrected_false_intention=corrected_false_intention,
        )

    def intrinsic_score(self, case: ProjectionCase) -> float:
        raw = (
            30.0 * case.constructive_support
            + 25.0 * case.path_coverage
            + 20.0 * case.gravity_alignment
            + 15.0 * case.cost_efficiency
            + 10.0 * case.observer_salience
            - 35.0 * case.tension_well_penalty
            - 25.0 * case.strained_gateway_penalty
        )
        return self._clamp(raw)

    def observer_misreading_score(
        self,
        case: ProjectionCase,
        profile: ProjectionProfile,
    ) -> float:
        visible_constructive = case.constructive_support * profile.constructive_visibility
        visible_penalty = (
            1.0 - profile.penalty_blindness
        ) * (
            0.70 * case.tension_well_penalty
            + 0.55 * case.strained_gateway_penalty
        )

        raw = (
            26.0 * profile.salience_bias * case.observer_salience
            + 22.0 * profile.path_bias * case.path_coverage
            + 22.0 * profile.smoothness_bias * case.narrative_smoothness
            + 12.0 * case.cost_efficiency
            + 18.0 * visible_constructive
            - 35.0 * visible_penalty
        )

        return self._clamp(raw)

    def corrected_misreading_score(
        self,
        case: ProjectionCase,
        profile: ProjectionProfile,
        observer_misreading_score: float,
    ) -> float:
        missing_constructive_penalty = (
            1.0 - case.constructive_support
        ) * profile.correction_strength * 45.0

        hidden_penalty_recovery = (
            case.tension_well_penalty + case.strained_gateway_penalty
        ) * profile.correction_strength * 18.0

        corrected = (
            observer_misreading_score
            - missing_constructive_penalty
            - hidden_penalty_recovery
        )

        return self._clamp(corrected)

    def evaluate_runs(
        self,
        runs: tuple[ProjectionRun, ...],
    ) -> tuple[ProjectionFinding, ...]:
        findings: list[ProjectionFinding] = []

        intrinsic_false_positive_count = self.intrinsic_false_positive_count()
        observer_false_intention_count = sum(1 for run in runs if run.false_intention)
        corrected_false_intention_count = sum(1 for run in runs if run.corrected_false_intention)
        correction_drop_percent = self.drop_percent(
            observer_false_intention_count,
            corrected_false_intention_count,
        )
        supported_margin = self.supported_intrinsic_margin()

        if intrinsic_false_positive_count > 0:
            findings.append(
                ProjectionFinding(
                    severity="error",
                    code="intrinsic_false_positive",
                    message=f"Intrinsic fabric scoring produced {intrinsic_false_positive_count} false positives.",
                )
            )

        if supported_margin < self.minimum_supported_intrinsic_margin:
            findings.append(
                ProjectionFinding(
                    severity="error",
                    code="supported_margin_too_low",
                    message=(
                        f"Supported intrinsic margin {supported_margin:.2f} is below required "
                        f"{self.minimum_supported_intrinsic_margin:.2f}."
                    ),
                )
            )

        if observer_false_intention_count < self.minimum_observer_false_intention_count:
            findings.append(
                ProjectionFinding(
                    severity="error",
                    code="projection_did_not_perturb_observer",
                    message=(
                        f"Only {observer_false_intention_count} observer false-intention events were produced; "
                        f"required at least {self.minimum_observer_false_intention_count}."
                    ),
                )
            )

        if corrected_false_intention_count > self.maximum_corrected_false_intention_count:
            findings.append(
                ProjectionFinding(
                    severity="error",
                    code="correction_left_too_many_false_intentions",
                    message=(
                        f"Correction left {corrected_false_intention_count} false-intention events; "
                        f"maximum allowed is {self.maximum_corrected_false_intention_count}."
                    ),
                )
            )

        if correction_drop_percent < self.minimum_correction_drop_percent:
            findings.append(
                ProjectionFinding(
                    severity="error",
                    code="correction_drop_too_low",
                    message=(
                        f"Correction drop {correction_drop_percent:.2f}% is below required "
                        f"{self.minimum_correction_drop_percent:.2f}%."
                    ),
                )
            )

        if observer_false_intention_count > 0:
            findings.append(
                ProjectionFinding(
                    severity="warning",
                    code="observer_false_intention_detected",
                    message=(
                        f"Projection perturbation produced {observer_false_intention_count} observer false-intention events."
                    ),
                )
            )

        if corrected_false_intention_count > 0:
            findings.append(
                ProjectionFinding(
                    severity="warning",
                    code="residual_false_intention_after_correction",
                    message=(
                        f"Correction left {corrected_false_intention_count} residual false-intention events."
                    ),
                )
            )

        if not findings:
            findings.append(
                ProjectionFinding(
                    severity="info",
                    code="projection_perturbation_passed",
                    message="Projection perturbation separated observer misreading from intrinsic fabric scoring.",
                )
            )

        return tuple(findings)

    def intrinsic_false_positive_count(self) -> int:
        return sum(
            1 for case in self.cases
            if case.expected_label != "target_like"
            and self.intrinsic_score(case) >= self.target_like_threshold
        )

    def supported_intrinsic_margin(self) -> float:
        supported_score = self.intrinsic_score(self.case_by_name("supported_constructive_route"))
        strongest_rival = max(
            self.intrinsic_score(case)
            for case in self.cases
            if case.name != "supported_constructive_route"
        )
        return supported_score - strongest_rival

    def case_by_name(self, name: str) -> ProjectionCase:
        for case in self.cases:
            if case.name == name:
                return case
        raise ValueError(f"Missing case: {name}")

    def drop_percent(self, before: int, after: int) -> float:
        if before <= 0:
            return 0.0
        return ((before - after) / before) * 100.0

    def render_markdown(
        self,
        runs: tuple[ProjectionRun, ...],
        findings: tuple[ProjectionFinding, ...],
    ) -> str:
        observer_false_intention_count = sum(1 for run in runs if run.false_intention)
        corrected_false_intention_count = sum(1 for run in runs if run.corrected_false_intention)
        correction_drop_percent = self.drop_percent(
            observer_false_intention_count,
            corrected_false_intention_count,
        )

        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This projection perturbation test changes observer projection profiles while keeping intrinsic fabric "
                "scoring fixed. It tests whether apparent targeting and observer misreading remain distinguishable."
            ),
            "",
            "## Decision rule",
            "",
            f"- Target-like threshold: {self.target_like_threshold:.2f}",
            f"- False-intention threshold: {self.false_intention_threshold:.2f}",
            f"- Minimum supported intrinsic margin: {self.minimum_supported_intrinsic_margin:.2f}",
            f"- Minimum observer false-intention events: {self.minimum_observer_false_intention_count}",
            f"- Maximum corrected false-intention events: {self.maximum_corrected_false_intention_count}",
            f"- Minimum correction drop percent: {self.minimum_correction_drop_percent:.2f}%",
            "",
            "## Summary",
            "",
            f"- Cases tested: {len(self.cases)}",
            f"- Projection profiles tested: {len(self.profiles)}",
            f"- Runs tested: {len(runs)}",
            f"- Intrinsic false positives: {self.intrinsic_false_positive_count()}",
            f"- Observer false-intention events: {observer_false_intention_count}",
            f"- Corrected false-intention events: {corrected_false_intention_count}",
            f"- Correction drop percent: {correction_drop_percent:.2f}%",
            f"- Supported intrinsic margin: {self.supported_intrinsic_margin():.2f}",
            "",
            "## Case-level intrinsic scores",
            "",
            "| Case | Expected label | Intrinsic score | Expected role |",
            "|---|---|---:|---|",
        ]

        for case in self.cases:
            lines.append(
                f"| {case.name} | {case.expected_label} | "
                f"{self.intrinsic_score(case):.2f} | {case.expected_role} |"
            )

        lines.extend(
            [
                "",
                "## Projection runs",
                "",
                "| Case | Projection profile | Intrinsic | Observer misreading | Corrected misreading | False intention | Corrected false intention |",
                "|---|---|---:|---:|---:|---|---|",
            ]
        )

        for run in runs:
            lines.append(
                f"| {run.case_name} | {run.profile_name} | "
                f"{run.intrinsic_score:.2f} | {run.observer_misreading_score:.2f} | "
                f"{run.corrected_misreading_score:.2f} | {run.false_intention} | "
                f"{run.corrected_false_intention} |"
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
                    "The test passes only if intrinsic fabric scoring avoids false positives while projection shifts can still "
                    "produce observer false-intention events. The correction layer should then reduce those false readings."
                ),
                "",
                "## Boundary",
                "",
                (
                    "This projection perturbation analysis is conceptual and non-operational. "
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
