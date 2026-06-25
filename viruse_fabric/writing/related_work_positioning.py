from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class PositioningFamily:
    name: str
    relation: str
    distinction: str
    manuscript_use: str


@dataclass(frozen=True)
class RelatedWorkPositioningReport:
    title: str
    output_path: str
    family_count: int
    distinction_count: int
    glossary_count: int
    boundary_count: int
    recommendation_count: int
    word_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class RelatedWorkPositioningBuilder:
    title = "Related Work and Positioning Scaffold v3.4"

    minimum_family_count = 7
    minimum_glossary_count = 6
    minimum_word_count = 1200

    glossary: tuple[tuple[str, str], ...] = (
        (
            "Constraint",
            "Any abstract condition, pressure, relation, or filter that shapes the space of possible paths.",
        ),
        (
            "Constraint geometry",
            "The overall shape produced when many constraints jointly make some paths easier, harder, stable, unstable, visible, or suppressed.",
        ),
        (
            "Constructive attractor",
            "A region of the fabric where compatible paths, tensions, and relations concentrate without requiring intention.",
        ),
        (
            "Path compatibility",
            "The degree to which a possible path remains consistent with the constraints present in the fabric.",
        ),
        (
            "Observer projection",
            "The interpretation imposed by an observer when a structured path is read as if it had intention or purpose.",
        ),
        (
            "Apparent intentionality",
            "The appearance of purpose that emerges from constraint-shaped paths and observer projection, without requiring actual intention.",
        ),
    )

    families: tuple[PositioningFamily, ...] = (
        PositioningFamily(
            name="Linear causal-chain models",
            relation=(
                "These models explain events as ordered sequences where one event produces another."
            ),
            distinction=(
                "Viruse Fabric does not reject sequences, but treats a sequence as only one projection of a wider constraint fabric."
            ),
            manuscript_use=(
                "Use this family to explain why the project moves from arrows to constraint geometry."
            ),
        ),
        PositioningFamily(
            name="Network causality",
            relation=(
                "Network models represent events as nodes and relations as edges."
            ),
            distinction=(
                "Viruse Fabric uses relational structure, but emphasizes pressure, compatibility, attractor concentration, and observer projection rather than graph connectivity alone."
            ),
            manuscript_use=(
                "Use this family to show that the project is not merely a graph model with new vocabulary."
            ),
        ),
        PositioningFamily(
            name="Dynamical systems",
            relation=(
                "Dynamical systems study trajectories, attractors, stability, and state-space evolution."
            ),
            distinction=(
                "Viruse Fabric borrows the intuition of attractors and trajectories, but frames them as causal-interpretive structures inside a constraint fabric."
            ),
            manuscript_use=(
                "Use this family to position constructive attractors without claiming a complete dynamical formalism yet."
            ),
        ),
        PositioningFamily(
            name="Constraint-based explanation",
            relation=(
                "Constraint-based approaches explain outcomes by the conditions that limit what can occur."
            ),
            distinction=(
                "Viruse Fabric extends this into a manuscript-level account of apparent intentionality, observer error, and causal curvature."
            ),
            manuscript_use=(
                "Use this family as the closest conceptual neighbor."
            ),
        ),
        PositioningFamily(
            name="Observer-dependent interpretation",
            relation=(
                "These approaches examine how observers shape what is inferred from a system."
            ),
            distinction=(
                "Viruse Fabric separates intrinsic structure from observer projection and tests how false intention can be reduced."
            ),
            manuscript_use=(
                "Use this family to support the distinction between path structure and interpreted purpose."
            ),
        ),
        PositioningFamily(
            name="Teleology and apparent purpose",
            relation=(
                "Teleological explanations describe systems as if they act toward ends."
            ),
            distinction=(
                "Viruse Fabric avoids assigning real intention. It explains apparent purpose as an emergent reading of constraint-shaped paths."
            ),
            manuscript_use=(
                "Use this family to prevent readers from mistaking the project for a claim about real purpose in non-intentional systems."
            ),
        ),
        PositioningFamily(
            name="Model validation and stress testing",
            relation=(
                "Validation frameworks test whether a model remains stable, informative, and bounded under perturbation."
            ),
            distinction=(
                "Viruse Fabric currently has internal validation, sensitivity tests, baseline comparison, projection perturbation, and manuscript audit, but no external validation."
            ),
            manuscript_use=(
                "Use this family to keep the project in the category of research prototype rather than finished theory."
            ),
        ),
    )

    boundaries: tuple[str, ...] = (
        "The scaffold does not provide real citations.",
        "The scaffold does not claim peer review.",
        "The scaffold does not establish external validation.",
        "The scaffold does not connect the model to real pathogens or real hosts.",
        "The scaffold does not support biological protocols, laboratory procedures, or executable interventions.",
        "The scaffold is a positioning aid for a cautious manuscript draft.",
    )

    recommendations: tuple[str, ...] = (
        "Add real citations only after selecting target literatures and reading primary sources.",
        "Keep causal-chain models as the contrast case, not as a strawman.",
        "Position constraint-based explanation as the closest conceptual neighbor.",
        "Clarify that constructive attractors are not intentional agents.",
        "Use observer projection to separate apparent purpose from actual purpose.",
        "Add formal notation after the positioning scaffold is stable.",
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/related_work_positioning_v3_4.md")

    def run(self) -> RelatedWorkPositioningReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render_markdown()
        self.output_path.write_text(markdown, encoding="utf-8")

        family_count = len(self.families)
        distinction_count = sum(1 for family in self.families if family.distinction)
        glossary_count = len(self.glossary)
        boundary_count = len(self.boundaries)
        recommendation_count = len(self.recommendations)
        word_count = self.word_count(markdown)

        errors: list[str] = []
        warnings: list[str] = []

        if family_count < self.minimum_family_count:
            errors.append("too few related-work families")

        if glossary_count < self.minimum_glossary_count:
            errors.append("too few glossary entries")

        if word_count < self.minimum_word_count:
            errors.append("positioning scaffold is too short")

        if "A constraint is any abstract condition" not in markdown:
            errors.append("constraint definition is missing")

        if "apparent purpose" not in markdown.lower():
            errors.append("apparent purpose positioning is missing")

        if "does not provide real citations" not in markdown:
            errors.append("citation boundary is missing")

        if "external validation" not in markdown:
            errors.append("external validation boundary is missing")

        warnings.append("real citations still need to be added later")
        warnings.append("formal notation is still pending")

        return RelatedWorkPositioningReport(
            title=self.title,
            output_path=str(self.output_path),
            family_count=family_count,
            distinction_count=distinction_count,
            glossary_count=glossary_count,
            boundary_count=boundary_count,
            recommendation_count=recommendation_count,
            word_count=word_count,
            error_count=len(errors),
            warning_count=len(warnings),
            passed=len(errors) == 0,
            interpretation=(
                "The related-work scaffold positions Viruse Fabric against neighboring conceptual families "
                "while clarifying constraints, apparent intentionality, and validation boundaries."
            ),
        )

    def render_markdown(self) -> str:
        lines: list[str] = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This scaffold prepares a future Related Work and Positioning section for the Viruse Fabric manuscript. "
                "It does not provide real citations. It maps the conceptual neighborhood so that later citation work can be added without pretending the draft is already peer-reviewed."
            ),
            "",
            "## Plain-Language Clarification",
            "",
            (
                "A constraint is any abstract condition, pressure, relation, or filter that shapes the space of possible paths. "
                "A constraint does not need to be a command, a force, or an intention. It can simply make some paths easier, harder, more stable, less stable, more visible, or suppressed."
            ),
            "",
            (
                "Constraint geometry is the joint shape created by many such constraints. "
                "When paths become concentrated around constructive attractors, remain compatible with the fabric, and are then interpreted by an observer, they can appear purposeful without containing actual intention."
            ),
            "",
            "In short: apparent purpose can emerge when constraint-shaped paths are read through observer projection.",
            "",
            "## Why Constraints Matter",
            "",
            (
                "The word constraint is central because it allows the manuscript to describe direction without inventing intention. "
                "A system can produce directional-looking behavior even when no agent inside the system is choosing a goal. "
                "For example, a slope, a channel, a barrier, and a region of lower resistance can make water repeatedly move along a similar path. "
                "The water does not intend the destination. The destination becomes likely because the space of possible movement has been shaped."
            ),
            "",
            (
                "Viruse Fabric uses this idea at an abstract level. A constraint may be a relation, a pressure, a compatibility condition, "
                "a filter, or a stability condition. Each one removes some possible paths, weakens others, and makes some paths more coherent. "
                "When many constraints interact, they create a structured space rather than a simple chain. That structured space is what this project calls constraint geometry."
            ),
            "",
            (
                "This matters for apparent intentionality. If a path repeatedly survives filtering, remains compatible with the surrounding fabric, "
                "and concentrates near a constructive attractor, the path may look as if it was aiming at something. "
                "The project treats that appearance carefully: the apparent aim belongs to the interpreted pattern, not to a hidden intention inside the system."
            ),
            "",
            "## Positioning Logic",
            "",
            (
                "The related-work section should therefore position Viruse Fabric between several neighboring families without collapsing it into any one of them. "
                "It is not only a causal-chain account, because the model cares about the surrounding field of constraints. "
                "It is not only a network account, because connectivity alone does not explain pressure, compatibility, or projection. "
                "It is not yet a full dynamical-systems theory, because the present manuscript does not provide a complete formal state-space specification."
            ),
            "",
            (
                "The strongest current positioning is cautious: Viruse Fabric is a conceptual-computational prototype for studying how constraint-shaped paths can be misread as intentional. "
                "Its internal validation supports this framing, but it does not establish external validation, biological prediction, or operational use. "
                "This is why the manuscript must keep its boundaries visible. Without those boundaries, the theory would become louder than its evidence."
            ),
            "",
            "## Glossary for Positioning",
            "",
            "| Term | Working definition |",
            "|---|---|",
        ]

        for term, definition in self.glossary:
            lines.append(f"| {term} | {definition} |")

        lines.extend(
            [
                "",
                "## Conceptual Neighbor Families",
                "",
            ]
        )

        for index, family in enumerate(self.families, start=1):
            lines.extend(
                [
                    f"### {index}. {family.name}",
                    "",
                    f"**Relation.** {family.relation}",
                    "",
                    f"**Distinction.** {family.distinction}",
                    "",
                    f"**Manuscript use.** {family.manuscript_use}",
                    "",
                ]
            )

        lines.extend(
            [
                "## Positioning Statement",
                "",
                (
                    "Viruse Fabric should be positioned as a conceptual-computational research prototype about constraint-shaped causality and apparent intentionality. "
                    "It is closest to constraint-based explanation and dynamical-system intuitions, but it is not yet a complete formal dynamical theory. "
                    "It uses network-like relations, but it is not merely a network model. "
                    "It discusses apparent purpose, but it does not assign real intention to non-intentional systems."
                ),
                "",
                (
                    "The manuscript should therefore avoid claiming that the model proves a universal theory of causality. "
                    "Its current defensible claim is narrower: internal validation suggests that constraint geometry, constructive attractors, path compatibility, and observer projection can be modeled together to explain how apparent intentionality may arise."
                ),
                "",
                "## Boundaries",
                "",
            ]
        )

        for boundary in self.boundaries:
            lines.append(f"- {boundary}")

        lines.extend(
            [
                "",
                "## Recommendations",
                "",
            ]
        )

        for recommendation in self.recommendations:
            lines.append(f"- {recommendation}")

        lines.extend(
            [
                "",
                "## Next Manuscript Step",
                "",
                (
                    "After this scaffold, the next sensible manuscript step is formal notation. "
                    "The notation should define constraint sets, path compatibility, constructive attractor concentration, observer projection, and correction of false intentionality. "
                    "That comes after positioning because equations without conceptual boundaries are just decorative machinery, humanity's favorite way to make confusion look expensive."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
