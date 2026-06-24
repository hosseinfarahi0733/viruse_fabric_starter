from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class BaselineCase:
    name: str
    constructive_support: float
    path_coverage: float
    gravity_alignment: float
    cost_efficiency: float
    observer_salience: float
    tension_well_penalty: float
    strained_gateway_penalty: float
    expected_label: str
    expected_role: str


@dataclass(frozen=True)
class ModelResult:
    model_name: str
    top_case: str
    supported_score: float
    strongest_rival_score: float
    separation_margin: float
    false_positive_count: int
    score_by_case: dict[str, float]
    passed_discrimination: bool


@dataclass(frozen=True)
class BaselineFinding:
    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class BaselineComparisonReport:
    title: str
    output_path: str
    case_count: int
    model_count: int
    baseline_count: int
    baseline_failure_count: int
    fabric_margin: float
    fabric_false_positive_count: int
    finding_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class BaselineComparator:
    title = "Baseline Comparison v2.8"

    target_like_threshold = 60.0
    minimum_fabric_margin = 25.0
    minimum_baseline_failure_count = 2

    cases: tuple[BaselineCase, ...] = (
        BaselineCase(
            name="supported_constructive_route",
            constructive_support=0.95,
            path_coverage=0.98,
            gravity_alignment=0.90,
            cost_efficiency=0.85,
            observer_salience=0.90,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_label="target_like",
            expected_role="should rank highest",
        ),
        BaselineCase(
            name="ablated_route",
            constructive_support=0.05,
            path_coverage=0.98,
            gravity_alignment=0.15,
            cost_efficiency=0.35,
            observer_salience=0.30,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_label="negative_control",
            expected_role="same route shape without constructive support should not look strongly target-like",
        ),
        BaselineCase(
            name="shortcut_gateway_route",
            constructive_support=0.10,
            path_coverage=0.55,
            gravity_alignment=0.30,
            cost_efficiency=0.30,
            observer_salience=0.40,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.60,
            expected_label="negative_control",
            expected_role="shortcut through a strained gateway should remain low",
        ),
        BaselineCase(
            name="tension_well_route",
            constructive_support=0.05,
            path_coverage=0.40,
            gravity_alignment=0.10,
            cost_efficiency=0.20,
            observer_salience=0.35,
            tension_well_penalty=0.80,
            strained_gateway_penalty=0.00,
            expected_label="negative_control",
            expected_role="tension well should not become target-like",
        ),
        BaselineCase(
            name="high_salience_ablated_decoy",
            constructive_support=0.04,
            path_coverage=0.92,
            gravity_alignment=0.28,
            cost_efficiency=0.55,
            observer_salience=0.98,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.00,
            expected_label="negative_control",
            expected_role="observer salience alone should not fake targeting",
        ),
        BaselineCase(
            name="high_path_shortcut_decoy",
            constructive_support=0.12,
            path_coverage=0.92,
            gravity_alignment=0.50,
            cost_efficiency=0.62,
            observer_salience=0.72,
            tension_well_penalty=0.00,
            strained_gateway_penalty=0.18,
            expected_label="negative_control",
            expected_role="efficient-looking shortcut should not beat constructive support",
        ),
        BaselineCase(
            name="low_penalty_tension_decoy",
            constructive_support=0.05,
            path_coverage=0.74,
            gravity_alignment=0.55,
            cost_efficiency=0.62,
            observer_salience=0.80,
            tension_well_penalty=0.25,
            strained_gateway_penalty=0.00,
            expected_label="negative_control",
            expected_role="weakened tension penalty should not create a false attractor",
        ),
    )

    model_names: tuple[str, ...] = (
        "viruse_fabric",
        "route_shape_baseline",
        "observer_salience_baseline",
        "efficiency_baseline",
        "reduced_linear_baseline",
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/baseline_comparison_v2_8.md")

    def run(self) -> BaselineComparisonReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        results = tuple(self.evaluate_model(model_name) for model_name in self.model_names)
        findings = self.evaluate_results(results)
        markdown = self.render_markdown(results, findings)
        self.output_path.write_text(markdown, encoding="utf-8")

        fabric_result = self.result_by_name(results, "viruse_fabric")
        baseline_results = [result for result in results if result.model_name != "viruse_fabric"]
        baseline_failure_count = sum(
            1 for result in baseline_results
            if not result.passed_discrimination
        )

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")

        return BaselineComparisonReport(
            title=self.title,
            output_path=str(self.output_path),
            case_count=len(self.cases),
            model_count=len(results),
            baseline_count=len(baseline_results),
            baseline_failure_count=baseline_failure_count,
            fabric_margin=fabric_result.separation_margin,
            fabric_false_positive_count=fabric_result.false_positive_count,
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            passed=error_count == 0,
            interpretation=(
                "The baseline comparison checks whether Viruse Fabric explains the target-like case better "
                "than simpler route-shape, observer-salience, and efficiency baselines."
            ),
        )

    def evaluate_model(self, model_name: str) -> ModelResult:
        score_by_case = {
            case.name: self.score_case(case, model_name)
            for case in self.cases
        }

        top_case = max(score_by_case, key=score_by_case.get)
        supported_score = score_by_case["supported_constructive_route"]
        strongest_rival_score = max(
            score for case_name, score in score_by_case.items()
            if case_name != "supported_constructive_route"
        )
        separation_margin = supported_score - strongest_rival_score
        false_positive_count = sum(
            1 for case in self.cases
            if case.expected_label == "negative_control"
            and score_by_case[case.name] >= self.target_like_threshold
        )

        passed_discrimination = (
            top_case == "supported_constructive_route"
            and false_positive_count == 0
            and separation_margin >= self.minimum_fabric_margin
        )

        return ModelResult(
            model_name=model_name,
            top_case=top_case,
            supported_score=supported_score,
            strongest_rival_score=strongest_rival_score,
            separation_margin=separation_margin,
            false_positive_count=false_positive_count,
            score_by_case=score_by_case,
            passed_discrimination=passed_discrimination,
        )

    def score_case(self, case: BaselineCase, model_name: str) -> float:
        if model_name == "viruse_fabric":
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

        if model_name == "route_shape_baseline":
            raw = 70.0 * case.path_coverage + 30.0 * case.cost_efficiency
            return self._clamp(raw)

        if model_name == "observer_salience_baseline":
            raw = 70.0 * case.observer_salience + 30.0 * case.path_coverage
            return self._clamp(raw)

        if model_name == "efficiency_baseline":
            raw = 50.0 * case.path_coverage + 50.0 * case.cost_efficiency
            return self._clamp(raw)

        if model_name == "reduced_linear_baseline":
            raw = (
                25.0 * case.path_coverage
                + 20.0 * case.gravity_alignment
                + 15.0 * case.cost_efficiency
                + 10.0 * case.observer_salience
            )
            return self._clamp(raw)

        raise ValueError(f"Unknown model name: {model_name}")

    def evaluate_results(self, results: tuple[ModelResult, ...]) -> tuple[BaselineFinding, ...]:
        findings: list[BaselineFinding] = []
        fabric_result = self.result_by_name(results, "viruse_fabric")
        baseline_results = [result for result in results if result.model_name != "viruse_fabric"]

        if fabric_result.top_case != "supported_constructive_route":
            findings.append(
                BaselineFinding(
                    severity="error",
                    code="fabric_top_case_failure",
                    message=f"Viruse Fabric ranked {fabric_result.top_case} above the supported constructive route.",
                )
            )

        if fabric_result.false_positive_count > 0:
            findings.append(
                BaselineFinding(
                    severity="error",
                    code="fabric_false_positive_controls",
                    message=f"Viruse Fabric produced {fabric_result.false_positive_count} false positive negative controls.",
                )
            )

        if fabric_result.separation_margin < self.minimum_fabric_margin:
            findings.append(
                BaselineFinding(
                    severity="error",
                    code="fabric_margin_too_low",
                    message=(
                        f"Viruse Fabric separation margin {fabric_result.separation_margin:.2f} is below "
                        f"required {self.minimum_fabric_margin:.2f}."
                    ),
                )
            )

        baseline_failure_count = 0
        for result in baseline_results:
            if result.passed_discrimination:
                continue

            baseline_failure_count += 1
            findings.append(
                BaselineFinding(
                    severity="warning",
                    code=f"{result.model_name}_weaker_than_fabric",
                    message=(
                        f"{result.model_name} failed discrimination: top={result.top_case}, "
                        f"false positives={result.false_positive_count}, "
                        f"margin={result.separation_margin:.2f}."
                    ),
                )
            )

        if baseline_failure_count < self.minimum_baseline_failure_count:
            findings.append(
                BaselineFinding(
                    severity="error",
                    code="baselines_not_sufficiently_weaker",
                    message=(
                        f"Only {baseline_failure_count} baselines failed discrimination; "
                        f"required at least {self.minimum_baseline_failure_count}."
                    ),
                )
            )

        if not findings:
            findings.append(
                BaselineFinding(
                    severity="info",
                    code="baseline_comparison_passed",
                    message="Viruse Fabric outperformed the tested simple baselines.",
                )
            )

        return tuple(findings)

    def render_markdown(
        self,
        results: tuple[ModelResult, ...],
        findings: tuple[BaselineFinding, ...],
    ) -> str:
        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This baseline comparison asks whether Viruse Fabric does more explanatory work than a simple "
                "route-shape baseline, observer-salience baseline, efficiency baseline, or reduced linear baseline."
            ),
            "",
            "## Decision rule",
            "",
            f"- Target-like threshold: {self.target_like_threshold:.2f}",
            f"- Minimum Viruse Fabric separation margin: {self.minimum_fabric_margin:.2f}",
            f"- Minimum weaker-baseline count: {self.minimum_baseline_failure_count}",
            "- Negative controls should not cross the target-like threshold.",
            "",
            "## Model summary",
            "",
            "| Model | Top case | Supported score | Strongest rival | Separation margin | False positive count | Passed discrimination |",
            "|---|---|---:|---:|---:|---:|---|",
        ]

        for result in results:
            lines.append(
                f"| {result.model_name} | {result.top_case} | "
                f"{result.supported_score:.2f} | {result.strongest_rival_score:.2f} | "
                f"{result.separation_margin:.2f} | {result.false_positive_count} | "
                f"{result.passed_discrimination} |"
            )

        lines.extend(
            [
                "",
                "## Case scores",
                "",
                "| Case | Expected label | Viruse Fabric | Route-shape baseline | Observer-salience baseline | Efficiency baseline | Reduced linear baseline |",
                "|---|---|---:|---:|---:|---:|---:|",
            ]
        )

        for case in self.cases:
            lines.append(
                f"| {case.name} | {case.expected_label} | "
                f"{self.result_by_name(results, 'viruse_fabric').score_by_case[case.name]:.2f} | "
                f"{self.result_by_name(results, 'route_shape_baseline').score_by_case[case.name]:.2f} | "
                f"{self.result_by_name(results, 'observer_salience_baseline').score_by_case[case.name]:.2f} | "
                f"{self.result_by_name(results, 'efficiency_baseline').score_by_case[case.name]:.2f} | "
                f"{self.result_by_name(results, 'reduced_linear_baseline').score_by_case[case.name]:.2f} |"
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
                    "Viruse Fabric passes this comparison only if it ranks the supported constructive route highest, "
                    "keeps negative controls below the target-like threshold, and preserves a clear separation margin. "
                    "A useful baseline test should expose false positive behavior in simpler models."
                ),
                "",
                "## Boundary",
                "",
                (
                    "This baseline comparison is conceptual and non-operational. "
                    "It does not use real pathogens, real hosts, biological protocols, laboratory procedures, "
                    "or executable interventions."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def result_by_name(
        self,
        results: tuple[ModelResult, ...],
        model_name: str,
    ) -> ModelResult:
        for result in results:
            if result.model_name == model_name:
                return result
        raise ValueError(f"Missing model result: {model_name}")

    def _clamp(self, value: float) -> float:
        return max(0.0, min(100.0, value))

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
