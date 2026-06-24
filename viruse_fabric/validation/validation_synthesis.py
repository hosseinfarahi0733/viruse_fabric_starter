from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class ValidationMilestone:
    version: str
    title: str
    report_path: str
    status: str
    errors: int
    warnings: int
    core_result: str
    validation_role: str
    claim_supported: str
    limitation: str


@dataclass(frozen=True)
class ReadinessScore:
    category: str
    score: int
    rationale: str


@dataclass(frozen=True)
class ValidationSynthesisFinding:
    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class ValidationSynthesisReport:
    title: str
    output_path: str
    milestone_count: int
    implemented_validation_count: int
    passed_validation_count: int
    total_errors: int
    total_warnings: int
    missing_report_count: int
    readiness_score: int
    research_status: str
    finding_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class ValidationSynthesisBuilder:
    title = "Validation Synthesis and Research Readiness v3.0"

    research_status = "research prototype with internal validation"
    minimum_milestones = 6
    minimum_implemented_validations = 5
    minimum_readiness_score = 65

    milestones: tuple[ValidationMilestone, ...] = (
        ValidationMilestone(
            version="v2.4.0",
            title="Validation Protocol",
            report_path="outputs/validation_protocol_v2_4.md",
            status="passed",
            errors=0,
            warnings=0,
            core_result="Defined the validation program and kept the project at research prototype status.",
            validation_role="Protocol layer",
            claim_supported="The project has an explicit validation roadmap before stronger presentation claims.",
            limitation="The protocol itself does not validate the model; it only defines what must be tested.",
        ),
        ValidationMilestone(
            version="v2.5.0",
            title="Constructive Attractor Ablation",
            report_path="outputs/constructive_attractor_ablation_v2_5.md",
            status="passed",
            errors=0,
            warnings=0,
            core_result="Removing constructive attractor support reduced apparent targeting by 59.84% and observer misreading by 65.37%.",
            validation_role="Necessity test",
            claim_supported="Constructive attractor support does real explanatory work in the model.",
            limitation="The test is internal and conceptual; it does not establish external biological validity.",
        ),
        ValidationMilestone(
            version="v2.6.0",
            title="Parameter Sensitivity Sweep",
            report_path="outputs/parameter_sensitivity_v2_6.md",
            status="passed",
            errors=0,
            warnings=0,
            core_result="The model remained stable across 729 moderate weight profiles with 100.00% stability.",
            validation_role="Moderate robustness test",
            claim_supported="The result is not dependent on one fragile moderate weight setting.",
            limitation="Moderate perturbation is not the same as adversarial stress.",
        ),
        ValidationMilestone(
            version="v2.7.0",
            title="Adversarial Sensitivity Sweep",
            report_path="outputs/adversarial_sensitivity_v2_7.md",
            status="passed",
            errors=0,
            warnings=3,
            core_result="The model stayed above threshold under 8640 hostile profiles with 81.06% stability.",
            validation_role="Adversarial robustness test",
            claim_supported="The model remains usable under hostile but interpretable decoy pressure.",
            limitation="Fragile regions exist; the model is not perfectly robust.",
        ),
        ValidationMilestone(
            version="v2.8.0",
            title="Baseline Comparison",
            report_path="outputs/baseline_comparison_v2_8.md",
            status="passed",
            errors=0,
            warnings=4,
            core_result="Viruse Fabric beat four simple baselines with margin 44.15 and zero false positives.",
            validation_role="Baseline discrimination test",
            claim_supported="The model is not reducible to simple route-shape, salience, or efficiency scoring.",
            limitation="The tested baselines are still internal and simplified.",
        ),
        ValidationMilestone(
            version="v2.9.0",
            title="Projection Perturbation",
            report_path="outputs/projection_perturbation_v2_9.md",
            status="passed",
            errors=0,
            warnings=2,
            core_result="Projection shifts produced 22 observer false intentions; correction reduced them to 3 with 86.36% drop.",
            validation_role="Observer-misreading test",
            claim_supported="Observer misreading can vary while intrinsic fabric discrimination remains stable.",
            limitation="Projection profiles are synthetic and conceptual.",
        ),
    )

    readiness_scores: tuple[ReadinessScore, ...] = (
        ReadinessScore(
            category="Theoretical coherence",
            score=82,
            rationale="The theory has stable core claims, a manifest, and repeated validation-facing tests.",
        ),
        ReadinessScore(
            category="Internal validation",
            score=78,
            rationale="Five implemented validation tests passed, including ablation, sensitivity, baseline, and projection perturbation.",
        ),
        ReadinessScore(
            category="Robustness",
            score=72,
            rationale="The model survived moderate and adversarial perturbations, but adversarial warnings show fragile regions.",
        ),
        ReadinessScore(
            category="Baseline defense",
            score=76,
            rationale="The model outperformed simple baselines, but the baselines are still conceptual and should be expanded later.",
        ),
        ReadinessScore(
            category="Observer-model separation",
            score=80,
            rationale="Projection perturbation separated intrinsic scoring from observer false-intention effects.",
        ),
        ReadinessScore(
            category="External validity",
            score=35,
            rationale="No external validation has been performed; claims must remain conceptual and non-operational.",
        ),
        ReadinessScore(
            category="Manuscript readiness",
            score=62,
            rationale="The project has enough material for a serious manuscript skeleton, but not for final claims.",
        ),
        ReadinessScore(
            category="Public presentation readiness",
            score=58,
            rationale="The demo and visuals exist, but the project should still be framed cautiously.",
        ),
    )

    allowed_claims: tuple[str, ...] = (
        "Viruse Fabric is a conceptual-computational research prototype.",
        "The model internally supports the distinction between apparent targeting and observer misreading.",
        "Constructive attractor support appears necessary in the current internal setup.",
        "The model is more discriminative than the tested simple baselines.",
        "The current validation layer supports continued research and manuscript development.",
    )

    disallowed_claims: tuple[str, ...] = (
        "The model proves a new law of causality.",
        "The model predicts real biological infection or viral behavior.",
        "The model is experimentally validated in real organisms or pathogens.",
        "The model supports operational biological intervention.",
        "The project is ready for strong public scientific claims without caveats.",
    )

    next_steps: tuple[str, ...] = (
        "Write a formal manuscript skeleton.",
        "Add a failure taxonomy for fragile regions found in adversarial tests.",
        "Expand baseline comparisons with more neutral and adversarial baselines.",
        "Build a validation dashboard or summary table for public-facing review.",
        "Define external validation boundaries without using real biological operational details.",
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/validation_synthesis_v3_0.md")

    def run(self) -> ValidationSynthesisReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        findings = self.evaluate()
        markdown = self.render_markdown(findings)
        self.output_path.write_text(markdown, encoding="utf-8")

        total_errors = sum(milestone.errors for milestone in self.milestones)
        total_warnings = sum(milestone.warnings for milestone in self.milestones)
        missing_report_count = self.missing_report_count()
        implemented_validation_count = len(
            [m for m in self.milestones if m.version != "v2.4.0"]
        )
        passed_validation_count = len(
            [m for m in self.milestones if m.version != "v2.4.0" and m.status == "passed"]
        )
        readiness_score = self.overall_readiness_score()

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")

        return ValidationSynthesisReport(
            title=self.title,
            output_path=str(self.output_path),
            milestone_count=len(self.milestones),
            implemented_validation_count=implemented_validation_count,
            passed_validation_count=passed_validation_count,
            total_errors=total_errors,
            total_warnings=total_warnings,
            missing_report_count=missing_report_count,
            readiness_score=readiness_score,
            research_status=self.research_status,
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            passed=error_count == 0,
            interpretation=(
                "The synthesis report consolidates the validation sequence and defines what the project may "
                "and may not claim at the current research-readiness stage."
            ),
        )

    def evaluate(self) -> tuple[ValidationSynthesisFinding, ...]:
        findings: list[ValidationSynthesisFinding] = []

        if len(self.milestones) < self.minimum_milestones:
            findings.append(
                ValidationSynthesisFinding(
                    severity="error",
                    code="too_few_milestones",
                    message=f"Only {len(self.milestones)} milestones were summarized.",
                )
            )

        implemented_validation_count = len(
            [m for m in self.milestones if m.version != "v2.4.0"]
        )
        if implemented_validation_count < self.minimum_implemented_validations:
            findings.append(
                ValidationSynthesisFinding(
                    severity="error",
                    code="too_few_implemented_validations",
                    message=f"Only {implemented_validation_count} implemented validations were summarized.",
                )
            )

        if self.missing_report_count() > 0:
            findings.append(
                ValidationSynthesisFinding(
                    severity="error",
                    code="missing_validation_reports",
                    message=f"{self.missing_report_count()} validation report files are missing.",
                )
            )

        total_errors = sum(milestone.errors for milestone in self.milestones)
        if total_errors > 0:
            findings.append(
                ValidationSynthesisFinding(
                    severity="error",
                    code="validation_errors_present",
                    message=f"The summarized validation sequence contains {total_errors} errors.",
                )
            )

        readiness_score = self.overall_readiness_score()
        if readiness_score < self.minimum_readiness_score:
            findings.append(
                ValidationSynthesisFinding(
                    severity="error",
                    code="readiness_score_too_low",
                    message=f"Overall readiness score {readiness_score} is below required {self.minimum_readiness_score}.",
                )
            )

        if sum(milestone.warnings for milestone in self.milestones) > 0:
            findings.append(
                ValidationSynthesisFinding(
                    severity="warning",
                    code="validation_warnings_present",
                    message=(
                        f"The validation sequence contains {sum(m.warnings for m in self.milestones)} warnings. "
                        "These warnings should be preserved as limitations, not hidden."
                    ),
                )
            )

        findings.append(
            ValidationSynthesisFinding(
                severity="warning",
                code="external_validation_not_completed",
                message="External validation has not been completed; claims must remain conceptual and research-prototype level.",
            )
        )

        if not findings:
            findings.append(
                ValidationSynthesisFinding(
                    severity="info",
                    code="validation_synthesis_passed",
                    message="Validation synthesis passed without warnings.",
                )
            )

        return tuple(findings)

    def missing_report_count(self) -> int:
        return sum(1 for milestone in self.milestones if not Path(milestone.report_path).exists())

    def overall_readiness_score(self) -> int:
        if not self.readiness_scores:
            return 0
        return round(sum(score.score for score in self.readiness_scores) / len(self.readiness_scores))

    def render_markdown(
        self,
        findings: tuple[ValidationSynthesisFinding, ...],
    ) -> str:
        lines = [
            f"# {self.title}",
            "",
            "## Executive Summary",
            "",
            (
                "Viruse Fabric has moved beyond a purely conceptual sketch into a research prototype with an internal "
                "validation sequence. The current evidence supports continued research, manuscript development, and cautious "
                "technical presentation. It does not support strong external, biological, or operational claims."
            ),
            "",
            f"- Research status: {self.research_status}",
            f"- Overall readiness score: {self.overall_readiness_score()} / 100",
            f"- Milestones summarized: {len(self.milestones)}",
            f"- Implemented validation tests: {len([m for m in self.milestones if m.version != 'v2.4.0'])}",
            f"- Total validation warnings: {sum(m.warnings for m in self.milestones)}",
            f"- Total validation errors: {sum(m.errors for m in self.milestones)}",
            f"- Missing report files: {self.missing_report_count()}",
            "",
            "## Validation Milestones",
            "",
            "| Version | Title | Status | Errors | Warnings | Validation role | Core result |",
            "|---|---|---|---:|---:|---|---|",
        ]

        for milestone in self.milestones:
            lines.append(
                f"| {milestone.version} | {milestone.title} | {milestone.status} | "
                f"{milestone.errors} | {milestone.warnings} | {milestone.validation_role} | "
                f"{milestone.core_result} |"
            )

        lines.extend(
            [
                "",
                "## Claims Supported by the Current Evidence",
                "",
            ]
        )

        for claim in self.allowed_claims:
            lines.append(f"- {claim}")

        lines.extend(
            [
                "",
                "## Claims Not Supported Yet",
                "",
            ]
        )

        for claim in self.disallowed_claims:
            lines.append(f"- {claim}")

        lines.extend(
            [
                "",
                "## Milestone-Level Interpretation",
                "",
                "| Version | Claim supported | Limitation |",
                "|---|---|---|",
            ]
        )

        for milestone in self.milestones:
            lines.append(
                f"| {milestone.version} | {milestone.claim_supported} | {milestone.limitation} |"
            )

        lines.extend(
            [
                "",
                "## Readiness Scores",
                "",
                "| Category | Score | Rationale |",
                "|---|---:|---|",
            ]
        )

        for score in self.readiness_scores:
            lines.append(f"| {score.category} | {score.score} | {score.rationale} |")

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
                "## Next Steps",
                "",
            ]
        )

        for step in self.next_steps:
            lines.append(f"- {step}")

        lines.extend(
            [
                "",
                "## Research Boundary",
                "",
                (
                    "This synthesis is conceptual and non-operational. It does not use real pathogens, real hosts, "
                    "biological protocols, laboratory procedures, or executable interventions. The project should remain "
                    "framed as a research prototype until external validation and stronger peer critique are completed."
                ),
                "",
                "## Final Readiness Statement",
                "",
                (
                    "The project is ready for a structured manuscript draft and careful internal or technical review. "
                    "It is not yet ready for strong public claims, biological prediction claims, or operational use."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
