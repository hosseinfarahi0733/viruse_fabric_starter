from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class ManuscriptSection:
    number: int
    title: str
    purpose: str
    key_points: tuple[str, ...]
    source_artifacts: tuple[str, ...]


@dataclass(frozen=True)
class ManuscriptSkeletonReport:
    title: str
    output_path: str
    section_count: int
    validation_section_count: int
    source_artifact_count: int
    allowed_claim_count: int
    disallowed_claim_count: int
    readiness_status: str
    word_count: int
    finding_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


@dataclass(frozen=True)
class ManuscriptFinding:
    severity: str
    code: str
    message: str


class ManuscriptSkeletonBuilder:
    title = "Viruse Fabric Manuscript Skeleton v3.1"

    readiness_status = "manuscript skeleton for cautious technical review"

    source_artifacts: tuple[str, ...] = (
        "outputs/theory_chapter_v1_7.md",
        "outputs/theory_chapter_fa_v1_8.md",
        "outputs/bilingual_quality_report_v1_9.md",
        "outputs/theory_manifest_v2_0.md",
        "outputs/visual_explanation_report_v2_1.md",
        "outputs/scenario_stress_report_v2_2.md",
        "outputs/public_demo_report_v2_3.md",
        "outputs/validation_protocol_v2_4.md",
        "outputs/constructive_attractor_ablation_v2_5.md",
        "outputs/parameter_sensitivity_v2_6.md",
        "outputs/adversarial_sensitivity_v2_7.md",
        "outputs/baseline_comparison_v2_8.md",
        "outputs/projection_perturbation_v2_9.md",
        "outputs/validation_synthesis_v3_0.md",
    )

    validation_artifacts: tuple[str, ...] = (
        "outputs/validation_protocol_v2_4.md",
        "outputs/constructive_attractor_ablation_v2_5.md",
        "outputs/parameter_sensitivity_v2_6.md",
        "outputs/adversarial_sensitivity_v2_7.md",
        "outputs/baseline_comparison_v2_8.md",
        "outputs/projection_perturbation_v2_9.md",
        "outputs/validation_synthesis_v3_0.md",
    )

    allowed_claims: tuple[str, ...] = (
        "Viruse Fabric is a conceptual-computational research prototype.",
        "The project internally models apparent targeting as a pattern emerging from constraint geometry.",
        "The implemented validation sequence supports the distinction between intrinsic fabric scoring and observer misreading.",
        "Constructive attractor support, penalty structure, and projection correction perform measurable work in the internal tests.",
        "The current state supports cautious manuscript development and technical review.",
    )

    disallowed_claims: tuple[str, ...] = (
        "The project proves a universal law of causality.",
        "The project predicts real biological infection, viral behavior, or host-pathogen outcomes.",
        "The project has external biological validation.",
        "The project supports laboratory procedures, biological protocols, or operational intervention.",
        "The project is ready for strong public claims without caveats.",
    )

    sections: tuple[ManuscriptSection, ...] = (
        ManuscriptSection(
            number=1,
            title="Abstract",
            purpose="State the central thesis and current evidence level without overclaiming.",
            key_points=(
                "Causality is modeled as a geometry of constraints rather than a linear chain.",
                "Apparent targeting is treated as an emergent projection of aligned constraints, not as literal intention.",
                "The project is currently a research prototype with internal validation.",
            ),
            source_artifacts=(
                "outputs/theory_manifest_v2_0.md",
                "outputs/validation_synthesis_v3_0.md",
            ),
        ),
        ManuscriptSection(
            number=2,
            title="Introduction",
            purpose="Explain why linear causal-chain language is insufficient for the target class of phenomena.",
            key_points=(
                "Motivate the need for a constraint-fabric view.",
                "Introduce the distinction between causal structure and observer interpretation.",
                "Frame the work as conceptual-computational, not operational biological modeling.",
            ),
            source_artifacts=(
                "outputs/theory_chapter_v1_7.md",
                "outputs/theory_chapter_fa_v1_8.md",
            ),
        ),
        ManuscriptSection(
            number=3,
            title="Core Thesis",
            purpose="Define the project’s central claim in precise language.",
            key_points=(
                "Causality is not a chain; it is a geometry of constraints.",
                "A cause is not merely an arrow but a deformation in a constraint fabric.",
                "Intention is not a property of the route; it is observer-side compression of aligned, salient, attractor-like structure.",
            ),
            source_artifacts=(
                "outputs/theory_manifest_v2_0.md",
                "notes/theory_log.md",
            ),
        ),
        ManuscriptSection(
            number=4,
            title="Formal Model",
            purpose="Describe the computational objects and scoring logic without pretending the model is externally validated.",
            key_points=(
                "Define nodes, constraints, paths, constructive attractors, penalties, and projection profiles.",
                "Explain intrinsic fabric scoring separately from observer misreading.",
                "Describe the correction layer as a way to reduce false-intention readings.",
            ),
            source_artifacts=(
                "viruse_fabric/core/fabric.py",
                "viruse_fabric/geometry/causal_curvature.py",
                "viruse_fabric/simulation/intention_correction.py",
            ),
        ),
        ManuscriptSection(
            number=5,
            title="Validation Protocol",
            purpose="Show that the validation sequence was defined before stronger claims were made.",
            key_points=(
                "Summarize the validation protocol from v2.4.",
                "Separate necessity tests, robustness tests, baseline comparisons, and projection perturbation.",
                "Keep the status at research prototype level.",
            ),
            source_artifacts=(
                "outputs/validation_protocol_v2_4.md",
            ),
        ),
        ManuscriptSection(
            number=6,
            title="Validation Results",
            purpose="Present the implemented validation sequence from v2.5 through v2.9.",
            key_points=(
                "Constructive attractor ablation reduced apparent targeting and observer misreading.",
                "Moderate and adversarial sensitivity sweeps tested robustness.",
                "Baseline comparison showed Viruse Fabric outperforming simple baselines.",
                "Projection perturbation separated observer false-intention from intrinsic scoring.",
            ),
            source_artifacts=(
                "outputs/constructive_attractor_ablation_v2_5.md",
                "outputs/parameter_sensitivity_v2_6.md",
                "outputs/adversarial_sensitivity_v2_7.md",
                "outputs/baseline_comparison_v2_8.md",
                "outputs/projection_perturbation_v2_9.md",
            ),
        ),
        ManuscriptSection(
            number=7,
            title="Research Readiness",
            purpose="Summarize what the internal validation sequence allows the project to responsibly claim.",
            key_points=(
                "The project has five passed implemented validation tests.",
                "The readiness score is 68, suitable for cautious technical review but not final scientific claims.",
                "Warnings and fragile regions should be preserved as limitations.",
            ),
            source_artifacts=(
                "outputs/validation_synthesis_v3_0.md",
            ),
        ),
        ManuscriptSection(
            number=8,
            title="Limitations",
            purpose="Prevent the manuscript from mutating into an overconfident brochure, humanity’s favorite genre.",
            key_points=(
                "No external validation has been completed.",
                "The tests are conceptual and internal.",
                "The model does not predict real biological behavior or support operational intervention.",
            ),
            source_artifacts=(
                "outputs/validation_synthesis_v3_0.md",
            ),
        ),
        ManuscriptSection(
            number=9,
            title="Allowed and Disallowed Claims",
            purpose="Make claim boundaries explicit.",
            key_points=(
                "List claims supported by the current internal validation sequence.",
                "List claims that remain unsupported.",
                "Use this section as a guardrail for papers, talks, demos, and public summaries.",
            ),
            source_artifacts=(
                "outputs/validation_synthesis_v3_0.md",
            ),
        ),
        ManuscriptSection(
            number=10,
            title="Future Work",
            purpose="Define the next serious steps without pretending they have already been done.",
            key_points=(
                "Develop failure taxonomy for fragile regions.",
                "Expand baselines and add external critique.",
                "Build a cautious public-facing technical narrative.",
                "Prepare a full manuscript draft from this skeleton.",
            ),
            source_artifacts=(
                "outputs/validation_synthesis_v3_0.md",
            ),
        ),
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/manuscript_skeleton_v3_1.md")

    def run(self) -> ManuscriptSkeletonReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        findings = self.evaluate()
        markdown = self.render_markdown(findings)
        self.output_path.write_text(markdown, encoding="utf-8")

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")

        return ManuscriptSkeletonReport(
            title=self.title,
            output_path=str(self.output_path),
            section_count=len(self.sections),
            validation_section_count=self.validation_section_count(),
            source_artifact_count=len(self.source_artifacts),
            allowed_claim_count=len(self.allowed_claims),
            disallowed_claim_count=len(self.disallowed_claims),
            readiness_status=self.readiness_status,
            word_count=self.word_count(markdown),
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            passed=error_count == 0,
            interpretation=(
                "The manuscript skeleton converts the validated research prototype into a cautious technical paper structure."
            ),
        )

    def evaluate(self) -> tuple[ManuscriptFinding, ...]:
        findings: list[ManuscriptFinding] = []

        if len(self.sections) < 10:
            findings.append(
                ManuscriptFinding(
                    severity="error",
                    code="too_few_sections",
                    message=f"Only {len(self.sections)} manuscript sections were defined.",
                )
            )

        if self.validation_section_count() < 3:
            findings.append(
                ManuscriptFinding(
                    severity="error",
                    code="validation_underrepresented",
                    message="Validation is underrepresented in the manuscript skeleton.",
                )
            )

        missing_artifacts = [
            artifact for artifact in self.source_artifacts
            if not Path(artifact).exists()
        ]

        if missing_artifacts:
            findings.append(
                ManuscriptFinding(
                    severity="error",
                    code="missing_source_artifacts",
                    message=f"{len(missing_artifacts)} source artifacts are missing.",
                )
            )

        if len(self.allowed_claims) < 5:
            findings.append(
                ManuscriptFinding(
                    severity="error",
                    code="too_few_allowed_claims",
                    message="Allowed claims are not sufficiently specified.",
                )
            )

        if len(self.disallowed_claims) < 5:
            findings.append(
                ManuscriptFinding(
                    severity="error",
                    code="too_few_disallowed_claims",
                    message="Disallowed claims are not sufficiently specified.",
                )
            )

        findings.append(
            ManuscriptFinding(
                severity="warning",
                code="manuscript_not_full_draft",
                message="This artifact is a manuscript skeleton, not a full paper draft.",
            )
        )

        findings.append(
            ManuscriptFinding(
                severity="warning",
                code="external_validation_boundary",
                message="External validation is still missing and must remain visible in the manuscript.",
            )
        )

        return tuple(findings)

    def validation_section_count(self) -> int:
        return sum(
            1 for section in self.sections
            if "validation" in section.title.lower()
            or "readiness" in section.title.lower()
            or "claims" in section.title.lower()
            or "limitations" in section.title.lower()
        )

    def render_markdown(
        self,
        findings: tuple[ManuscriptFinding, ...],
    ) -> str:
        lines = [
            f"# {self.title}",
            "",
            "## Manuscript Status",
            "",
            f"- Status: {self.readiness_status}",
            "- This is a manuscript skeleton, not a full paper draft.",
            "- The intended tone is technical, cautious, and explicit about limitations.",
            "- The manuscript must preserve the boundary between internal validation and external validation.",
            "",
            "## Working Title",
            "",
            "Viruse Fabric: A Constraint-Geometry Model of Apparent Targeting and Observer Misreading",
            "",
            "## Core Sentence",
            "",
            "Causality is not a chain; it is a geometry of constraints.",
            "",
            "## Human-AI Work Note",
            "",
            (
                "This manuscript skeleton records a collaborative construction process: computational structuring, validation "
                "discipline, and language organization were combined with human persistence, judgment, and direction. "
                "The result should be judged by the clarity of the model and the honesty of its validation boundaries, "
                "not by romantic claims about intelligence or authorship."
            ),
            "",
            "## Abstract Draft",
            "",
            (
                "This paper introduces Viruse Fabric, a conceptual-computational framework that models causality as a geometry "
                "of constraints rather than a chain of isolated causes. The framework is used to study apparent targeting: "
                "cases where routes through a constraint fabric appear intentional to an observer despite lacking literal intent. "
                "The model separates intrinsic fabric scoring from observer misreading and evaluates this distinction through "
                "an internal validation sequence including constructive attractor ablation, parameter sensitivity, adversarial "
                "sensitivity, baseline comparison, and projection perturbation. The current evidence supports cautious manuscript "
                "development and technical review, but not external biological prediction claims or operational use."
            ),
            "",
            "## Proposed Manuscript Structure",
            "",
        ]

        for section in self.sections:
            lines.extend(
                [
                    f"### {section.number}. {section.title}",
                    "",
                    f"**Purpose:** {section.purpose}",
                    "",
                    "**Key points:**",
                ]
            )

            for point in section.key_points:
                lines.append(f"- {point}")

            lines.extend(
                [
                    "",
                    "**Source artifacts:**",
                ]
            )

            for artifact in section.source_artifacts:
                lines.append(f"- `{artifact}`")

            lines.append("")

        lines.extend(
            [
                "## Allowed Claims",
                "",
            ]
        )

        for claim in self.allowed_claims:
            lines.append(f"- {claim}")

        lines.extend(
            [
                "",
                "## Disallowed Claims",
                "",
            ]
        )

        for claim in self.disallowed_claims:
            lines.append(f"- {claim}")

        lines.extend(
            [
                "",
                "## Source Artifact Inventory",
                "",
            ]
        )

        for artifact in self.source_artifacts:
            exists = Path(artifact).exists()
            lines.append(f"- `{artifact}` | exists: {exists}")

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
                "## Research Boundary",
                "",
                (
                    "This manuscript skeleton is conceptual and non-operational. It does not use real pathogens, real hosts, "
                    "biological protocols, laboratory procedures, or executable interventions. The manuscript must keep "
                    "Viruse Fabric framed as a research prototype with internal validation until external validation and "
                    "serious peer critique are completed."
                ),
                "",
                "## Next Writing Step",
                "",
                (
                    "The next step is to expand this skeleton into a full manuscript draft with an abstract, introduction, "
                    "formal model section, validation results, limitations, and claim-boundary discussion."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
