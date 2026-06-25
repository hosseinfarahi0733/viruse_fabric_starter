from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class SourceArtifact:
    name: str
    path: str
    role: str


@dataclass(frozen=True)
class IntegrationStep:
    target_section: str
    source: str
    action: str
    rationale: str
    expected_effect: str


@dataclass(frozen=True)
class WarningAction:
    warning_code: str
    source_warning: str
    integration_response: str
    status_after_plan: str


@dataclass(frozen=True)
class ManuscriptIntegrationPlanReport:
    title: str
    output_path: str
    source_artifact_count: int
    missing_source_artifact_count: int
    integration_step_count: int
    warning_action_count: int
    boundary_count: int
    next_action_count: int
    word_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class ManuscriptIntegrationPlanBuilder:
    title = "Manuscript Integration Plan v3.6"

    minimum_source_artifact_count = 4
    minimum_integration_step_count = 10
    minimum_warning_action_count = 3
    minimum_word_count = 1200

    source_artifacts: tuple[SourceArtifact, ...] = (
        SourceArtifact(
            name="Full Manuscript Draft v3.2",
            path="outputs/full_manuscript_draft_v3_2.md",
            role="Base manuscript draft to be revised.",
        ),
        SourceArtifact(
            name="Manuscript Quality Audit v3.3",
            path="outputs/manuscript_quality_audit_v3_3.md",
            role="Quality gate that identifies remaining manuscript weaknesses.",
        ),
        SourceArtifact(
            name="Related Work and Positioning Scaffold v3.4",
            path="outputs/related_work_positioning_v3_4.md",
            role="Positioning material for related work, constraint clarification, and conceptual neighbors.",
        ),
        SourceArtifact(
            name="Formal Notation Scaffold v3.5",
            path="outputs/formal_notation_scaffold_v3_5.md",
            role="Symbolic vocabulary for the formal model section.",
        ),
    )

    integration_steps: tuple[IntegrationStep, ...] = (
        IntegrationStep(
            target_section="Abstract",
            source="v3.4 and v3.5",
            action=(
                "Add one sentence clarifying that constraints shape possible paths and one sentence stating that the notation is manuscript-facing rather than proof-level."
            ),
            rationale=(
                "The abstract currently needs to signal both conceptual clarity and formal caution before readers reach the body."
            ),
            expected_effect="Reduces risk of teleological or over-formal interpretation at the opening.",
        ),
        IntegrationStep(
            target_section="Introduction",
            source="v3.4",
            action=(
                "Insert a plain-language explanation of constraint geometry after the causal-chain contrast."
            ),
            rationale=(
                "Readers must understand constraint before they can understand apparent intentionality."
            ),
            expected_effect="Makes the core thesis easier to read without weakening its originality.",
        ),
        IntegrationStep(
            target_section="Related Work and Positioning",
            source="v3.4",
            action=(
                "Add a new manuscript section between Introduction and Core Thesis using the seven conceptual neighbor families."
            ),
            rationale=(
                "The v3.3 audit identified missing related work as a manuscript weakness."
            ),
            expected_effect="Addresses the related-work gap while avoiding fake citations.",
        ),
        IntegrationStep(
            target_section="Core Thesis",
            source="v3.4",
            action=(
                "Add a compact statement: apparent purpose can emerge when constraint-shaped paths are read through observer projection."
            ),
            rationale=(
                "The thesis needs a precise bridge between constraint geometry and apparent intentionality."
            ),
            expected_effect="Improves conceptual continuity between thesis and model.",
        ),
        IntegrationStep(
            target_section="Formal Model",
            source="v3.5",
            action=(
                "Insert the scaffold object F = (C, P, A, O), then define C, P, A, O before discussing validation."
            ),
            rationale=(
                "The manuscript needs symbolic structure before presenting technical claims."
            ),
            expected_effect="Addresses the formal-notation warning from v3.3.",
        ),
        IntegrationStep(
            target_section="Formal Model",
            source="v3.5",
            action=(
                "Add K(p, C), alpha(p, A), I_app, I_false, R(I_app), and Delta_R as working notation."
            ),
            rationale=(
                "The model needs explicit handles for compatibility, attractor concentration, observer projection, false intentionality, and correction."
            ),
            expected_effect="Makes later validation claims easier to connect to model terms.",
        ),
        IntegrationStep(
            target_section="Validation Sequence",
            source="v3.3 and v3.5",
            action=(
                "Add a short bridge explaining how the validation experiments map onto the formal symbols."
            ),
            rationale=(
                "The validation sequence should not feel disconnected from the new notation."
            ),
            expected_effect="Improves manuscript coherence between model and results.",
        ),
        IntegrationStep(
            target_section="Results",
            source="v3.3",
            action=(
                "Convert the validation outcomes into a compact table with milestone, metric, and interpretation columns."
            ),
            rationale=(
                "The quality audit recommended better readability for validation results."
            ),
            expected_effect="Makes the evidence easier to review and reduces narrative clutter.",
        ),
        IntegrationStep(
            target_section="Limitations",
            source="v3.3, v3.4, and v3.5",
            action=(
                "Preserve explicit boundaries: no external validation, no real pathogens, no real hosts, no biological protocols, no laboratory procedures, and no executable interventions."
            ),
            rationale=(
                "The manuscript must keep its safety and evidence limits visible."
            ),
            expected_effect="Keeps the project inside research-prototype boundaries.",
        ),
        IntegrationStep(
            target_section="Future Work",
            source="v3.4 and v3.5",
            action=(
                "Add three future tasks: real citation work, deeper formalization, and external validation design."
            ),
            rationale=(
                "The next steps should follow from current weaknesses rather than from ambition fog."
            ),
            expected_effect="Turns audit warnings into a concrete research path.",
        ),
        IntegrationStep(
            target_section="Conclusion",
            source="v3.3, v3.4, and v3.5",
            action=(
                "Restate the bounded claim: Viruse Fabric is a conceptual-computational prototype with internal validation and a first symbolic scaffold."
            ),
            rationale=(
                "The conclusion should end with defensible scope, not victory music."
            ),
            expected_effect="Prevents the final paragraph from overclaiming.",
        ),
    )

    warning_actions: tuple[WarningAction, ...] = (
        WarningAction(
            warning_code="needs_related_work",
            source_warning="The v3.3 quality audit identified missing related work.",
            integration_response="Use v3.4 as a Related Work and Positioning section scaffold.",
            status_after_plan="Addressed by planned manuscript insertion, but real citations remain pending.",
        ),
        WarningAction(
            warning_code="needs_formal_notation",
            source_warning="The v3.3 quality audit identified missing formal notation.",
            integration_response="Use v3.5 to revise the Formal Model section with F = (C, P, A, O) and related symbols.",
            status_after_plan="Addressed at scaffold level, but not yet proof-level.",
        ),
        WarningAction(
            warning_code="draft_not_submission_ready",
            source_warning="The v3.3 quality audit warned that the draft is not submission-ready.",
            integration_response="Keep submission readiness unresolved until related work, formal notation, and quality audit are integrated into a revised draft.",
            status_after_plan="Still open. The integration plan reduces risk but does not make the manuscript submission-ready.",
        ),
    )

    boundaries: tuple[str, ...] = (
        "This plan does not rewrite the full manuscript yet.",
        "This plan does not provide real citations.",
        "This plan does not establish peer review.",
        "This plan does not establish external validation.",
        "This plan does not model real pathogens or real hosts.",
        "This plan does not support biological protocols, laboratory procedures, or executable interventions.",
        "This plan does not support strong public claims.",
        "This plan is a manuscript revision map, not a final paper.",
    )

    next_actions: tuple[str, ...] = (
        "Create an integrated manuscript draft using v3.2 as the base.",
        "Insert the v3.4 related-work section with citation placeholders clearly marked.",
        "Insert the v3.5 formal notation into the Formal Model section.",
        "Convert validation results into a compact table.",
        "Run a new manuscript quality audit after integration.",
        "Keep the manuscript status as cautious technical review only.",
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/manuscript_integration_plan_v3_6.md")

    def run(self) -> ManuscriptIntegrationPlanReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render_markdown()
        self.output_path.write_text(markdown, encoding="utf-8")

        missing_sources = self.missing_source_artifacts()
        word_count = self.word_count(markdown)

        errors: list[str] = []
        warnings: list[str] = []

        if len(self.source_artifacts) < self.minimum_source_artifact_count:
            errors.append("too few source artifacts")

        if missing_sources:
            errors.append("one or more source artifacts are missing")

        if len(self.integration_steps) < self.minimum_integration_step_count:
            errors.append("too few integration steps")

        if len(self.warning_actions) < self.minimum_warning_action_count:
            errors.append("too few warning actions")

        if word_count < self.minimum_word_count:
            errors.append("integration plan is too short")

        required_phrases = (
            "Manuscript Integration Plan",
            "Source Artifact Inventory",
            "Integration Map",
            "Warning Reduction Plan",
            "F = (C, P, A, O)",
            "Related Work and Positioning",
            "Formal Model",
            "not submission-ready",
            "does not establish external validation",
            "does not support strong public claims",
        )

        for phrase in required_phrases:
            if phrase not in markdown:
                errors.append(f"missing required phrase: {phrase}")

        warnings.append("the integrated manuscript has not been generated yet")
        warnings.append("real citations remain pending")
        warnings.append("formal notation remains scaffold-level")

        return ManuscriptIntegrationPlanReport(
            title=self.title,
            output_path=str(self.output_path),
            source_artifact_count=len(self.source_artifacts),
            missing_source_artifact_count=len(missing_sources),
            integration_step_count=len(self.integration_steps),
            warning_action_count=len(self.warning_actions),
            boundary_count=len(self.boundaries),
            next_action_count=len(self.next_actions),
            word_count=word_count,
            error_count=len(errors),
            warning_count=len(warnings),
            passed=len(errors) == 0,
            interpretation=(
                "The manuscript integration plan maps the v3.4 positioning scaffold and v3.5 formal notation scaffold "
                "onto the v3.2 manuscript while responding to v3.3 audit warnings."
            ),
        )

    def missing_source_artifacts(self) -> tuple[str, ...]:
        missing = [
            artifact.path for artifact in self.source_artifacts
            if not Path(artifact.path).exists()
        ]
        return tuple(missing)

    def render_markdown(self) -> str:
        lines: list[str] = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This plan defines how the v3.4 Related Work and Positioning Scaffold and the v3.5 Formal Notation Scaffold should be integrated into the v3.2 full manuscript draft. "
                "It also responds to the v3.3 manuscript quality audit warnings. The goal is not to produce a final paper in this step. "
                "The goal is to create a controlled revision map so the manuscript can be improved without turning into a stitched-together academic creature with too many elbows."
            ),
            "",
            "## Source Artifact Inventory",
            "",
            "| Artifact | Path | Role | Present |",
            "|---|---|---|---|",
        ]

        for artifact in self.source_artifacts:
            present = Path(artifact.path).exists()
            lines.append(f"| {artifact.name} | `{artifact.path}` | {artifact.role} | {present} |")

        lines.extend(
            [
                "",
                "## Integration Map",
                "",
                "| Target manuscript section | Source | Action | Rationale | Expected effect |",
                "|---|---|---|---|---|",
            ]
        )

        for step in self.integration_steps:
            lines.append(
                f"| {step.target_section} | {step.source} | {step.action} | {step.rationale} | {step.expected_effect} |"
            )

        lines.extend(
            [
                "",
                "## Warning Reduction Plan",
                "",
                (
                    "The v3.3 audit produced three manuscript-level warnings. This plan does not pretend they disappear by being named, "
                    "which would be very human and very useless. Instead, each warning gets a concrete integration response."
                ),
                "",
                "| Warning code | Source warning | Integration response | Status after plan |",
                "|---|---|---|---|",
            ]
        )

        for action in self.warning_actions:
            lines.append(
                f"| {action.warning_code} | {action.source_warning} | {action.integration_response} | {action.status_after_plan} |"
            )

        lines.extend(
            [
                "",
                "## Formal Model Insertion",
                "",
                "The Formal Model section should introduce the scaffold object:",
                "",
                "```text",
                "F = (C, P, A, O)",
                "```",
                "",
                "where `C` is the constraint set, `P` is the path space, `A` is the constructive attractor set, and `O` is observer projection.",
                "",
                (
                    "This notation should be presented as a scaffold, not as a final proof. "
                    "The manuscript should explicitly say that compatibility `K(p, C)`, attractor concentration `alpha(p, A)`, apparent intentionality `I_app`, false intentionality `I_false`, and correction `R(I_app)` are working terms for technical review."
                ),
                "",
                "## Related Work Insertion",
                "",
                (
                    "The Related Work and Positioning section should use the seven families from v3.4: causal-chain models, network causality, dynamical systems, constraint-based explanation, observer-dependent interpretation, teleology and apparent purpose, and model validation frameworks."
                ),
                "",
                (
                    "Because the scaffold does not provide real citations, the manuscript must mark this section as a positioning scaffold until real sources are selected and read. "
                    "The point is to orient the manuscript, not to fake scholarship. Humanity has enough ways to do that already."
                ),
                "",
                "## Revision Order",
                "",
                "The safest revision order is:",
                "",
                "1. Preserve the v3.2 manuscript as the base.",
                "2. Insert Related Work and Positioning after the Introduction.",
                "3. Rewrite the Formal Model section using the v3.5 notation.",
                "4. Add a validation mapping paragraph that connects experiments to notation.",
                "5. Convert the Results section into a compact validation table.",
                "6. Strengthen Limitations and Research Boundary language.",
                "7. Update the Conclusion with the bounded v3.5 status.",
                "8. Run a new quality audit.",
                "",
                "## Manuscript Boundaries",
                "",
            ]
        )

        for boundary in self.boundaries:
            lines.append(f"- {boundary}")

        lines.extend(
            [
                "",
                "## Next Actions",
                "",
            ]
        )

        for action in self.next_actions:
            lines.append(f"- {action}")

        lines.extend(
            [
                "",
                "## Integration Status",
                "",
                (
                    "After this plan, the manuscript is better prepared for an integrated revision, but it is still not submission-ready. "
                    "The next milestone should generate an integrated manuscript draft and then rerun quality checks. "
                    "The proper status remains: research prototype with internal validation, manuscript-facing scaffolds, and no external validation."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
