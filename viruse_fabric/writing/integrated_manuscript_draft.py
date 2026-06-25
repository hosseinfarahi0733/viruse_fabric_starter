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
class ValidationRow:
    milestone: str
    metric: str
    interpretation: str


@dataclass(frozen=True)
class IntegratedManuscriptReport:
    title: str
    output_path: str
    source_artifact_count: int
    missing_source_artifact_count: int
    section_count: int
    related_family_count: int
    notation_count: int
    validation_row_count: int
    boundary_count: int
    word_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class IntegratedManuscriptDraftBuilder:
    title = "Integrated Manuscript Draft v3.7"

    minimum_source_artifact_count = 5
    minimum_section_count = 18
    minimum_related_family_count = 7
    minimum_notation_count = 10
    minimum_validation_row_count = 8
    minimum_word_count = 2600

    source_artifacts: tuple[SourceArtifact, ...] = (
        SourceArtifact(
            name="Full Manuscript Draft v3.2",
            path="outputs/full_manuscript_draft_v3_2.md",
            role="Base manuscript draft.",
        ),
        SourceArtifact(
            name="Manuscript Quality Audit v3.3",
            path="outputs/manuscript_quality_audit_v3_3.md",
            role="Quality gate and warning source.",
        ),
        SourceArtifact(
            name="Related Work and Positioning Scaffold v3.4",
            path="outputs/related_work_positioning_v3_4.md",
            role="Related work, constraint clarification, and positioning source.",
        ),
        SourceArtifact(
            name="Formal Notation Scaffold v3.5",
            path="outputs/formal_notation_scaffold_v3_5.md",
            role="Symbolic vocabulary and formal model source.",
        ),
        SourceArtifact(
            name="Manuscript Integration Plan v3.6",
            path="outputs/manuscript_integration_plan_v3_6.md",
            role="Revision map for integrating positioning and notation.",
        ),
    )

    related_families: tuple[str, ...] = (
        "Linear causal-chain models",
        "Network causality",
        "Dynamical systems",
        "Constraint-based explanation",
        "Observer-dependent interpretation",
        "Teleology and apparent purpose",
        "Model validation and stress testing",
    )

    notation_terms: tuple[tuple[str, str], ...] = (
        ("F", "the causal fabric as the top-level structure"),
        ("C", "the constraint set"),
        ("c_i", "an individual constraint"),
        ("P", "the path space"),
        ("p", "a candidate path"),
        ("K(p, C)", "path compatibility under constraints"),
        ("A", "the constructive attractor set"),
        ("alpha(p, A)", "attractor concentration"),
        ("O", "observer projection"),
        ("I_app(p, O)", "apparent intentionality under projection"),
        ("I_false", "false intentionality"),
        ("R(I_app)", "projection correction"),
        ("Delta_R", "correction drop"),
    )

    validation_rows: tuple[ValidationRow, ...] = (
        ValidationRow(
            milestone="v2.5 Constructive Attractor Ablation",
            metric="Targeting drop 59.84%; misreading drop 65.37%",
            interpretation="Constructive attractors materially affect path selection and observer misreading.",
        ),
        ValidationRow(
            milestone="v2.6 Parameter Sensitivity",
            metric="729 profiles; 100.00% stability",
            interpretation="The model remains stable under ordinary parameter perturbation.",
        ),
        ValidationRow(
            milestone="v2.7 Adversarial Sensitivity",
            metric="8640 profiles; 81.06% stability",
            interpretation="The model is robust but exposes fragile regions under adversarial pressure.",
        ),
        ValidationRow(
            milestone="v2.8 Baseline Comparison",
            metric="Fabric margin 44.15; zero false positives",
            interpretation="The fabric model outperforms simpler baseline interpretations in internal tests.",
        ),
        ValidationRow(
            milestone="v2.9 Projection Perturbation",
            metric="Observer false intentions 22; corrected false intentions 3; correction drop 86.36%",
            interpretation="Projection correction reduces observer-driven false intentionality.",
        ),
        ValidationRow(
            milestone="v3.0 Validation Synthesis",
            metric="Readiness score 68",
            interpretation="The project status is research prototype with internal validation.",
        ),
        ValidationRow(
            milestone="v3.3 Manuscript Quality Audit",
            metric="Overclaim count 0; weak phrase count 0; boundary phrase count 12",
            interpretation="The manuscript preserves claim boundaries and avoids hype language.",
        ),
        ValidationRow(
            milestone="v3.4 to v3.6 Manuscript Scaffolds",
            metric="Positioning, notation, and integration plan all passed",
            interpretation="The manuscript now has conceptual positioning, symbolic vocabulary, and a revision map.",
        ),
    )

    boundaries: tuple[str, ...] = (
        "This integrated draft is not a final paper.",
        "This integrated draft is not submission-ready.",
        "This integrated draft is not externally validated.",
        "This integrated draft does not establish peer review.",
        "This integrated draft does not model real pathogens or real hosts.",
        "This integrated draft does not support biological protocols, laboratory procedures, or executable interventions.",
        "This integrated draft does not support strong public claims.",
        "This integrated draft remains a research prototype with internal validation.",
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/integrated_manuscript_draft_v3_7.md")

    def run(self) -> IntegratedManuscriptReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render_markdown()
        self.output_path.write_text(markdown, encoding="utf-8")

        missing_sources = self.missing_source_artifacts()
        section_count = self.section_count(markdown)
        word_count = self.word_count(markdown)

        errors: list[str] = []
        warnings: list[str] = []

        if len(self.source_artifacts) < self.minimum_source_artifact_count:
            errors.append("too few source artifacts")

        if missing_sources:
            errors.append("one or more source artifacts are missing")

        if section_count < self.minimum_section_count:
            errors.append("too few manuscript sections")

        if len(self.related_families) < self.minimum_related_family_count:
            errors.append("too few related-work families")

        if len(self.notation_terms) < self.minimum_notation_count:
            errors.append("too few notation terms")

        if len(self.validation_rows) < self.minimum_validation_row_count:
            errors.append("too few validation rows")

        if word_count < self.minimum_word_count:
            errors.append("integrated manuscript draft is too short")

        required_phrases = (
            "Integrated Manuscript Draft",
            "Related Work and Positioning",
            "Formal Model",
            "F = (C, P, A, O)",
            "K(p, C)",
            "alpha(p, A)",
            "I_app",
            "I_false",
            "R(I_app)",
            "Delta_R",
            "research prototype with internal validation",
            "not submission-ready",
            "not externally validated",
            "does not support strong public claims",
            "real pathogens",
            "real hosts",
            "biological protocols",
            "laboratory procedures",
            "executable interventions",
            "Compact Validation Results",
        )

        for phrase in required_phrases:
            if phrase not in markdown:
                errors.append(f"missing required phrase: {phrase}")

        warnings.append("real citations are still pending")
        warnings.append("formal notation remains scaffold-level")
        warnings.append("external validation is still absent")

        return IntegratedManuscriptReport(
            title=self.title,
            output_path=str(self.output_path),
            source_artifact_count=len(self.source_artifacts),
            missing_source_artifact_count=len(missing_sources),
            section_count=section_count,
            related_family_count=len(self.related_families),
            notation_count=len(self.notation_terms),
            validation_row_count=len(self.validation_rows),
            boundary_count=len(self.boundaries),
            word_count=word_count,
            error_count=len(errors),
            warning_count=len(warnings),
            passed=len(errors) == 0,
            interpretation=(
                "The integrated manuscript draft combines the v3.2 manuscript base with v3.4 positioning, "
                "v3.5 formal notation, and v3.6 integration logic while preserving research boundaries."
            ),
        )

    def missing_source_artifacts(self) -> tuple[str, ...]:
        return tuple(
            artifact.path for artifact in self.source_artifacts
            if not Path(artifact.path).exists()
        )

    def render_markdown(self) -> str:
        lines: list[str] = [
            f"# {self.title}",
            "",
            "## Manuscript Status",
            "",
            (
                "This document is an integrated manuscript draft for cautious technical review. "
                "It combines the v3.2 full manuscript draft with the v3.4 related-work and positioning scaffold, "
                "the v3.5 formal notation scaffold, and the v3.6 manuscript integration plan. "
                "The status remains research prototype with internal validation. It is not submission-ready, "
                "not externally validated, and not a final paper."
            ),
            "",
            "## Integration Rationale",
            "",
            (
                "The purpose of this integrated draft is to join three manuscript-facing improvements without losing the boundaries that made the earlier draft defensible. "
                "The v3.4 positioning scaffold clarifies the conceptual neighborhood of the project and explains why constraint geometry is not simply another name for a causal chain, a network, or a teleological claim. "
                "The v3.5 formal notation scaffold gives the manuscript a first symbolic vocabulary so that terms such as constraint set, path compatibility, constructive attractor concentration, observer projection, false intentionality, and correction can be discussed without drifting into vague metaphor. "
                "The v3.6 integration plan defines where these additions belong so that the manuscript becomes more coherent rather than merely longer."
            ),
            "",
            (
                "This integration also changes the manuscript's argumentative shape. "
                "The earlier full draft established the central thesis and summarized internal validation. "
                "The integrated version now has to do more: it must introduce the reader to the meaning of constraints, place the project among neighboring conceptual families, define a symbolic scaffold, map validation results onto that scaffold, and preserve explicit research boundaries. "
                "In other words, the manuscript is moving from a readable prototype draft toward a technically organized review draft. "
                "That is progress, but not magic. It does not make the project externally validated, peer reviewed, or submission-ready."
            ),
            "",
            (
                "The main risk at this stage is over-integration. "
                "A manuscript can become worse when every useful artifact is inserted without hierarchy. "
                "This draft therefore treats related work, notation, validation mapping, limitations, and conclusion as separate functions. "
                "Related work positions the project. Formal notation clarifies the model. Validation mapping connects tests to terms. Limitations prevent overclaiming. "
                "The conclusion restates the bounded claim. Apparently even ideas need seating charts, otherwise they all rush the stage and call it synthesis."
            ),
            "",
            "## Working Title",
            "",
            "**Viruse Fabric: Constraint Geometry, Apparent Intentionality, and Observer Projection in a Causal Fabric**",
            "",
            "## Abstract",
            "",
            (
                "Viruse Fabric proposes that causality can be modeled not merely as a chain of events, but as a geometry of constraints. "
                "In this view, a causal system is shaped by abstract constraints, compatible paths, constructive attractors, and observer projection. "
                "The project studies how apparent intentionality can arise when paths shaped by constraints are interpreted as if they were goal-directed. "
                "The model does not assign real intention to non-intentional systems. Instead, it separates intrinsic fabric structure from observer-driven interpretation."
            ),
            "",
            (
                "This integrated draft adds conceptual positioning and a first symbolic notation to the earlier manuscript draft. "
                "The formal scaffold represents the fabric as `F = (C, P, A, O)`, where `C` is the constraint set, `P` is the path space, `A` is the constructive attractor set, and `O` is observer projection. "
                "Internal validation results support the prototype framing, including attractor ablation, parameter sensitivity, adversarial sensitivity, baseline comparison, and projection correction. "
                "The manuscript remains bounded: it does not establish external validation, real biological prediction, operational intervention, or strong public claims."
            ),
            "",
            "## Introduction",
            "",
            (
                "Many causal explanations are written as chains: one event leads to another, which leads to another. "
                "This is useful, but incomplete. A chain is a thin projection of a larger structure. "
                "Events occur inside fields of restriction, compatibility, pressure, and interpretation. "
                "Viruse Fabric starts from the claim that causality is not only a sequence of arrows; it is a geometry of constraints."
            ),
            "",
            (
                "The project asks why some paths appear directed even when no intention is present. "
                "A path may persist because it fits the available constraints. It may become prominent because it concentrates around constructive attractors. "
                "It may then be interpreted by an observer as if it had a purpose. "
                "This does not mean that purpose exists inside the path. It means that apparent purpose can emerge from the alignment of constraint geometry, attractor concentration, path compatibility, and observer projection."
            ),
            "",
            "## Plain-Language Constraint Clarification",
            "",
            (
                "A constraint is any abstract condition, pressure, relation, or filter that shapes the space of possible paths. "
                "A constraint is not necessarily a command, a force, a rule, or an intention. "
                "It may simply make one route easier, another route harder, one state more stable, and another state less likely. "
                "A slope constrains water, a wall constrains movement, a narrow channel constrains flow, and a compatibility condition constrains which paths remain coherent."
            ),
            "",
            (
                "Constraint geometry is the joint shape produced when many constraints operate together. "
                "The important point is that direction can appear without intention. "
                "A path may look as if it is aiming somewhere because the surrounding constraints repeatedly make that path more compatible than alternatives. "
                "Apparently this needs to be said out loud, because humans see a repeated pattern and immediately start hunting for a tiny manager inside it."
            ),
            "",
            "## Related Work and Positioning",
            "",
            (
                "This manuscript positions Viruse Fabric near several conceptual families while avoiding collapse into any one of them. "
                "The positioning is scaffold-level and does not yet include real citations. "
                "The purpose is to clarify the conceptual neighborhood before later citation work is added."
            ),
            "",
        ]

        for family in self.related_families:
            lines.append(f"- **{family}.** This family provides a neighboring reference point, but Viruse Fabric remains focused on constraint-shaped causality, apparent intentionality, and observer projection.")

        lines.extend(
            [
                "",
                (
                    "Linear causal-chain models are useful as a contrast case because they show what the project is moving beyond. "
                    "Network causality is closer, but connectivity alone does not capture pressure, compatibility, attractor concentration, or observer projection. "
                    "Dynamical systems provide useful intuitions about trajectories and attractors, but the present manuscript does not claim to be a complete dynamical-systems theory. "
                    "Constraint-based explanation is the closest conceptual neighbor because it explains outcomes by asking how the space of possibilities is shaped. "
                    "Observer-dependent interpretation and teleology are essential for preventing a common mistake: confusing apparent purpose with actual intention."
                ),
                "",
                "## Core Thesis",
                "",
                (
                    "The core thesis is: causality is not a chain; it is a geometry of constraints. "
                    "A causal fabric shapes possible paths before any observer narrates them as a linear sequence. "
                    "Some paths become more compatible with the fabric, some are suppressed, and some concentrate around constructive attractors. "
                    "When an observer interprets these structured paths, the result may be apparent intentionality."
                ),
                "",
                (
                    "The thesis is intentionally bounded. It does not claim that non-intentional systems possess real purpose. "
                    "It claims that purpose-like readings can arise when structured paths are projected through an observer model. "
                    "This distinction matters because the project is about the geometry that makes a path look directed, not about smuggling intention into systems that do not have it."
                ),
                "",
                "## Formal Model",
                "",
                "The integrated formal scaffold represents the fabric as:",
                "",
                "```text",
                "F = (C, P, A, O)",
                "```",
                "",
                "where:",
                "",
                "- `F` is the causal fabric.",
                "- `C` is the constraint set.",
                "- `P` is the path space.",
                "- `A` is the constructive attractor set.",
                "- `O` is observer projection.",
                "",
                "The working notation is:",
                "",
                "| Symbol | Meaning |",
                "|---|---|",
            ]
        )

        for symbol, meaning in self.notation_terms:
            lines.append(f"| `{symbol}` | {meaning} |")

        lines.extend(
            [
                "",
                (
                    "Path compatibility is represented as `K(p, C)`, the degree to which a candidate path `p` fits the active constraint set `C`. "
                    "Constructive attractor concentration is represented as `alpha(p, A)`, the degree to which the path concentrates around attractor regions. "
                    "Apparent intentionality is represented as `I_app(p, O)`, the purpose-like interpretation assigned under observer projection. "
                    "False intentionality, `I_false`, appears when projected purpose exceeds intrinsic structural support. "
                    "Correction is represented as `R(I_app)`, and correction drop is represented as `Delta_R`."
                ),
                "",
                "## Interpretive Flow",
                "",
                "The intended interpretive flow is:",
                "",
                "```text",
                "constraints -> compatible paths -> attractor concentration -> observer projection -> apparent intentionality",
                "```",
                "",
                (
                    "This flow is not a claim that paths possess goals. "
                    "It is a claim that constraints can shape path selection, attractors can concentrate compatible paths, and observers can then read the resulting structure as if it were intentional. "
                    "The difference between actual intention and apparent intentionality is one of the manuscript's central boundaries."
                ),
                "",
                "## Validation Mapping",
                "",
                (
                    "The validation sequence maps onto the formal scaffold as follows. "
                    "Attractor ablation tests whether `A` matters. Parameter sensitivity and adversarial sensitivity test whether the fabric is stable under changes in `C` and related weights. "
                    "Baseline comparison asks whether fabric-level interpretation outperforms simpler models. "
                    "Projection perturbation tests whether `O` can create false intentionality and whether `R(I_app)` can reduce it."
                ),
                "",
                (
                    "The validation evidence is internal. It supports a research-prototype interpretation, not a final theory. "
                    "The manuscript should therefore treat the validation sequence as a disciplined internal check rather than as proof of external biological applicability."
                ),
                "",
                "## Compact Validation Results",
                "",
                "| Milestone | Metric | Interpretation |",
                "|---|---|---|",
            ]
        )

        for row in self.validation_rows:
            lines.append(f"| {row.milestone} | {row.metric} | {row.interpretation} |")

        lines.extend(
            [
                "",
                "## Results Interpretation",
                "",
                (
                    "The internal results suggest that the fabric model captures distinctions that simpler baselines miss. "
                    "Constructive attractor ablation reduces targeting and observer misreading, which supports the role of attractor concentration. "
                    "Projection perturbation shows that observer projection can inflate intentional readings and that correction can reduce false intentionality. "
                    "The baseline comparison indicates that fabric-level interpretation provides a stronger internal account than simpler alternatives."
                ),
                "",
                (
                    "The results should not be overread. They show internal coherence and useful model behavior under designed scenarios. "
                    "They do not show external validation, real-world biological prediction, or operational applicability. "
                    "This is why the manuscript keeps repeating its boundary conditions like a tired adult explaining stove safety."
                ),
                "",
                "## Limitations",
                "",
                (
                    "The current model remains a conceptual-computational prototype. "
                    "The notation is scaffold-level rather than proof-level. "
                    "The related-work section is a positioning scaffold and does not yet include real citations. "
                    "The validation sequence is internal and scenario-based. "
                    "The manuscript is not submission-ready."
                ),
                "",
                (
                    "The project does not model real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions. "
                    "It does not establish external validation. It does not support strong public claims. "
                    "Its current value is in clarifying a research direction: apparent intentionality can be studied as a product of constraint-shaped paths and observer projection."
                ),
                "",
                "## Allowed and Disallowed Claims",
                "",
                "The current evidence supports these cautious claims:",
                "",
                "- Viruse Fabric is a research prototype with internal validation.",
                "- Constraint geometry can be used to model path compatibility and apparent intentionality.",
                "- Constructive attractors play a measurable role in internal ablation tests.",
                "- Observer projection can create false intentionality in the model.",
                "- Projection correction can reduce false intentionality in internal tests.",
                "",
                "The current evidence does not support these claims:",
                "",
                "- The theory is externally validated.",
                "- The model predicts real biological systems.",
                "- The manuscript is submission-ready.",
                "- The model supports operational intervention.",
                "- The model supports strong public claims.",
                "",
                "## Future Work",
                "",
                (
                    "The next technical step is to generate a revised integrated manuscript and rerun a manuscript quality audit. "
                    "The related-work scaffold should later be replaced with a citation-backed section based on real sources. "
                    "The formal notation should be refined into clearer definitions, explicit equations, and eventually testable model variants. "
                    "External validation would require a separate design process and must remain outside the current claim boundary."
                ),
                "",
                "## Human-AI Work Note",
                "",
                (
                    "This manuscript was developed through iterative human-AI collaboration. "
                    "The human role supplied direction, judgment, persistence, and conceptual pressure. "
                    "The AI role supplied drafting, structuring, checking, and annoying reminders that Git still wanted one more commit. "
                    "The collaboration does not replace review, critique, or validation. It is a workflow note, not an epistemic guarantee."
                ),
                "",
                "## Source Artifact Inventory",
                "",
                "| Artifact | Path | Role | Present |",
                "|---|---|---|---|",
            ]
        )

        for artifact in self.source_artifacts:
            present = Path(artifact.path).exists()
            lines.append(f"| {artifact.name} | `{artifact.path}` | {artifact.role} | {present} |")

        lines.extend(
            [
                "",
                "## Research Boundary",
                "",
            ]
        )

        for boundary in self.boundaries:
            lines.append(f"- {boundary}")

        lines.extend(
            [
                "",
                "Boundary checklist: this integrated draft is conceptual and non-operational. It does not use real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions. It is not externally validated and does not support strong public claims.",
                "",
                "## Conclusion",
                "",
                (
                    "Viruse Fabric now has a more complete manuscript-facing form. "
                    "The project includes a full manuscript draft, a manuscript quality audit, a related-work and positioning scaffold, a formal notation scaffold, and a manuscript integration plan. "
                    "This integrated draft brings those components together while preserving the central boundary: the project is a research prototype with internal validation."
                ),
                "",
                (
                    "The central claim remains cautious and focused. Apparent intentionality may emerge when constraint geometry, constructive attractor concentration, path compatibility, and observer projection align. "
                    "The model does not require real intention to explain the appearance of purpose. "
                    "That is the point: not that systems secretly want things, but that structured constraints can make paths look as if they do. "
                    "Tiny mercy: for once, the manuscript says what it means before pretending to be finished."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def section_count(self, text: str) -> int:
        return len(re.findall(r"^## ", text, flags=re.MULTILINE))

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
