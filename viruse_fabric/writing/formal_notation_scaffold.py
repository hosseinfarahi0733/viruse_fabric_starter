from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class NotationEntry:
    symbol: str
    name: str
    meaning: str
    manuscript_use: str


@dataclass(frozen=True)
class FormalRelation:
    name: str
    expression: str
    explanation: str
    boundary: str


@dataclass(frozen=True)
class FormalNotationReport:
    title: str
    output_path: str
    notation_count: int
    relation_count: int
    definition_count: int
    boundary_count: int
    example_count: int
    word_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class FormalNotationScaffoldBuilder:
    title = "Formal Notation Scaffold v3.5"

    minimum_notation_count = 10
    minimum_relation_count = 7
    minimum_definition_count = 7
    minimum_word_count = 1200

    notation_entries: tuple[NotationEntry, ...] = (
        NotationEntry(
            symbol="F",
            name="Fabric",
            meaning="The abstract causal fabric containing constraints, paths, attractors, and observer projections.",
            manuscript_use="Use F as the top-level object of the model.",
        ),
        NotationEntry(
            symbol="C",
            name="Constraint set",
            meaning="The set of abstract conditions, pressures, relations, or filters that shape possible paths.",
            manuscript_use="Use C to avoid treating causality as a simple event chain.",
        ),
        NotationEntry(
            symbol="c_i",
            name="Individual constraint",
            meaning="A single constraint inside C, such as a pressure, relation, filter, or compatibility condition.",
            manuscript_use="Use c_i when discussing how local restrictions shape path behavior.",
        ),
        NotationEntry(
            symbol="P",
            name="Path space",
            meaning="The set of possible paths available inside the fabric before compatibility filtering.",
            manuscript_use="Use P to distinguish possible paths from selected or interpreted paths.",
        ),
        NotationEntry(
            symbol="p",
            name="Path",
            meaning="A candidate trajectory, sequence, or structured route through the fabric.",
            manuscript_use="Use p for the object whose compatibility and apparent intentionality are evaluated.",
        ),
        NotationEntry(
            symbol="K(p, C)",
            name="Compatibility score",
            meaning="A score describing how well path p fits the active constraint set C.",
            manuscript_use="Use K to explain why some paths remain stable while others are suppressed.",
        ),
        NotationEntry(
            symbol="A",
            name="Constructive attractor set",
            meaning="The set of regions where compatible paths, tensions, and relations concentrate.",
            manuscript_use="Use A to formalize constructive attractor concentration without implying intention.",
        ),
        NotationEntry(
            symbol="alpha(p, A)",
            name="Attractor concentration",
            meaning="A score describing how strongly path p concentrates around constructive attractors.",
            manuscript_use="Use alpha to connect path compatibility with attractor-centered structure.",
        ),
        NotationEntry(
            symbol="O",
            name="Observer projection",
            meaning="The interpretive mapping imposed by an observer on a structured path.",
            manuscript_use="Use O to separate intrinsic fabric structure from observer interpretation.",
        ),
        NotationEntry(
            symbol="I_app(p, O)",
            name="Apparent intentionality",
            meaning="The apparent purpose attributed to path p under observer projection O.",
            manuscript_use="Use I_app to discuss purpose-like readings without claiming real intention.",
        ),
        NotationEntry(
            symbol="I_false",
            name="False intentionality",
            meaning="Cases where observer projection assigns purpose beyond what intrinsic fabric structure supports.",
            manuscript_use="Use I_false to represent observer-driven misreading.",
        ),
        NotationEntry(
            symbol="R",
            name="Correction operator",
            meaning="A correction procedure that reduces false intentionality by separating projection from intrinsic structure.",
            manuscript_use="Use R to describe projection correction and reduction of observer error.",
        ),
    )

    relations: tuple[FormalRelation, ...] = (
        FormalRelation(
            name="Fabric composition",
            expression="F = (C, P, A, O)",
            explanation="The fabric is represented as constraints, possible paths, constructive attractors, and observer projection.",
            boundary="This is a scaffold definition, not a complete mathematical ontology.",
        ),
        FormalRelation(
            name="Constraint set",
            expression="C = {c_1, c_2, ..., c_n}",
            explanation="The constraint set contains the abstract conditions that shape which paths remain possible or stable.",
            boundary="The entries are abstract and do not represent biological protocols or operational interventions.",
        ),
        FormalRelation(
            name="Path compatibility",
            expression="K(p, C) -> [0, 1]",
            explanation="Compatibility maps a path and constraint set to a bounded score, where higher values mean better fit.",
            boundary="The scaffold does not specify a final scoring equation.",
        ),
        FormalRelation(
            name="Compatible path subset",
            expression="P_C = {p in P | K(p, C) >= theta_K}",
            explanation="The compatible path subset contains paths whose compatibility exceeds a chosen threshold.",
            boundary="The threshold is a modeling convention, not an externally validated biological constant.",
        ),
        FormalRelation(
            name="Constructive attractor concentration",
            expression="alpha(p, A) -> [0, 1]",
            explanation="Attractor concentration estimates how strongly a path gathers around constructive attractor regions.",
            boundary="A constructive attractor is not an intentional agent.",
        ),
        FormalRelation(
            name="Apparent intentionality",
            expression="I_app(p, O) = O(K(p, C), alpha(p, A), context)",
            explanation="Apparent intentionality is modeled as an observer projection over compatibility, attractor concentration, and context.",
            boundary="The expression describes apparent purpose, not actual intention.",
        ),
        FormalRelation(
            name="False intentionality",
            expression="I_false = I_app - I_intrinsic_support",
            explanation="False intentionality is the excess purpose-like interpretation beyond intrinsic structural support.",
            boundary="This is a conceptual difference, not a claim of directly measured mental intention.",
        ),
        FormalRelation(
            name="Projection correction",
            expression="R(I_app) -> I_corrected",
            explanation="The correction operator reduces observer-driven purpose attribution by re-weighting intrinsic support.",
            boundary="The current correction is internally validated only.",
        ),
        FormalRelation(
            name="Correction drop",
            expression="Delta_R = (I_false_before - I_false_after) / I_false_before",
            explanation="Correction drop measures the proportional reduction of false intentionality after projection correction.",
            boundary="The value is meaningful inside the model and does not establish external validation.",
        ),
    )

    definitions: tuple[str, ...] = (
        "A constraint is any abstract condition, pressure, relation, or filter that shapes the space of possible paths.",
        "Constraint geometry is the joint structure produced when constraints make some paths easier, harder, stable, unstable, visible, or suppressed.",
        "A path is a candidate route through the fabric, not necessarily a literal physical trajectory.",
        "Path compatibility describes how well a path fits the active constraint set.",
        "A constructive attractor is a region where compatible paths and tensions concentrate without requiring intention.",
        "Observer projection is the interpretive mapping that can make a structured path appear purposeful.",
        "Apparent intentionality is the appearance of purpose without a commitment to actual intention.",
        "False intentionality occurs when observer projection exceeds what intrinsic structure supports.",
        "Projection correction reduces false intentionality by separating observer interpretation from fabric structure.",
    )

    boundaries: tuple[str, ...] = (
        "This scaffold is not a formal proof.",
        "This scaffold is not a complete mathematical theory.",
        "This scaffold is not externally validated.",
        "This scaffold does not model real pathogens or real hosts.",
        "This scaffold does not support biological protocols, laboratory procedures, or executable interventions.",
        "This scaffold does not support strong public claims.",
        "The notation is intended to clarify the manuscript before deeper formalization.",
    )

    examples: tuple[str, ...] = (
        "If K(p, C) is high, the path is compatible with the constraint set.",
        "If alpha(p, A) is high, the path concentrates around constructive attractors.",
        "If I_app is high while intrinsic support is low, the observer may be producing false intentionality.",
        "If Delta_R is high, projection correction has reduced observer-driven misreading.",
    )

    recommendations: tuple[str, ...] = (
        "Convert the scaffold into a dedicated Formal Model section in the manuscript.",
        "Define the compatibility score more precisely in a later version.",
        "Separate intrinsic support from observer projection in all future validation reports.",
        "Avoid treating constructive attractors as agents.",
        "Keep the notation abstract until external validation exists.",
        "Use the notation to improve clarity, not to decorate uncertainty.",
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/formal_notation_scaffold_v3_5.md")

    def run(self) -> FormalNotationReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render_markdown()
        self.output_path.write_text(markdown, encoding="utf-8")

        notation_count = len(self.notation_entries)
        relation_count = len(self.relations)
        definition_count = len(self.definitions)
        boundary_count = len(self.boundaries)
        example_count = len(self.examples)
        word_count = self.word_count(markdown)

        errors: list[str] = []
        warnings: list[str] = []

        if notation_count < self.minimum_notation_count:
            errors.append("too few notation entries")

        if relation_count < self.minimum_relation_count:
            errors.append("too few formal relations")

        if definition_count < self.minimum_definition_count:
            errors.append("too few definitions")

        if word_count < self.minimum_word_count:
            errors.append("formal notation scaffold is too short")

        required_phrases = (
            "F = (C, P, A, O)",
            "K(p, C)",
            "alpha(p, A)",
            "I_app",
            "I_false",
            "R(I_app)",
            "Delta_R",
            "not a formal proof",
            "not externally validated",
            "does not support strong public claims",
        )

        for phrase in required_phrases:
            if phrase not in markdown:
                errors.append(f"missing required phrase: {phrase}")

        warnings.append("compatibility score still needs a final equation")
        warnings.append("formal notation still needs external critique")
        warnings.append("notation is manuscript-facing, not proof-level")

        return FormalNotationReport(
            title=self.title,
            output_path=str(self.output_path),
            notation_count=notation_count,
            relation_count=relation_count,
            definition_count=definition_count,
            boundary_count=boundary_count,
            example_count=example_count,
            word_count=word_count,
            error_count=len(errors),
            warning_count=len(warnings),
            passed=len(errors) == 0,
            interpretation=(
                "The formal notation scaffold gives Viruse Fabric a cautious symbolic vocabulary for constraints, "
                "paths, compatibility, constructive attractors, observer projection, false intentionality, and correction."
            ),
        )

    def render_markdown(self) -> str:
        lines: list[str] = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This scaffold introduces a cautious symbolic vocabulary for the Viruse Fabric manuscript. "
                "Its purpose is clarity, not proof. The notation helps the manuscript state what is being modeled: "
                "constraints, paths, compatibility, constructive attractors, observer projection, false intentionality, and correction."
            ),
            "",
            (
                "The scaffold should be read as a manuscript-facing bridge between conceptual explanation and later formalization. "
                "It is not a formal proof, not a complete mathematical theory, and not externally validated. "
                "Apparently even symbols need supervision, because otherwise humans start mistaking notation for truth."
            ),
            "",
            "## Core Formal Object",
            "",
            "The top-level scaffold is:",
            "",
            "```text",
            "F = (C, P, A, O)",
            "```",
            "",
            "Where:",
            "",
            "- `F` is the fabric.",
            "- `C` is the constraint set.",
            "- `P` is the path space.",
            "- `A` is the constructive attractor set.",
            "- `O` is observer projection.",
            "",
            "This says that Viruse Fabric is not a simple chain of events. It is a structured object containing constraints, possible paths, attractor regions, and interpretive projection.",
            "",
            "## Working Definitions",
            "",
        ]

        for definition in self.definitions:
            lines.append(f"- {definition}")

        lines.extend(
            [
                "",
                "## Notation Table",
                "",
                "| Symbol | Name | Meaning | Manuscript use |",
                "|---|---|---|---|",
            ]
        )

        for entry in self.notation_entries:
            lines.append(
                f"| `{entry.symbol}` | {entry.name} | {entry.meaning} | {entry.manuscript_use} |"
            )

        lines.extend(
            [
                "",
                "## Formal Relations",
                "",
            ]
        )

        for index, relation in enumerate(self.relations, start=1):
            lines.extend(
                [
                    f"### {index}. {relation.name}",
                    "",
                    "```text",
                    relation.expression,
                    "```",
                    "",
                    f"**Explanation.** {relation.explanation}",
                    "",
                    f"**Boundary.** {relation.boundary}",
                    "",
                ]
            )

        lines.extend(
            [
                "## Interpretive Flow",
                "",
                "The intended manuscript logic is:",
                "",
                "```text",
                "constraints -> compatible paths -> attractor concentration -> observer projection -> apparent intentionality",
                "```",
                "",
                (
                    "This flow does not claim that a path has real intention. "
                    "It claims that a path can become compatible, concentrated, and then interpreted as if it were directed toward an end."
                ),
                "",
                "A compact version is:",
                "",
                "```text",
                "C shapes P; K selects P_C; alpha highlights attractor concentration; O produces I_app.",
                "```",
                "",
                (
                    "False intentionality appears when `I_app` is stronger than the intrinsic structural support provided by compatibility and attractor concentration. "
                    "Projection correction then tries to reduce this gap."
                ),
                "",
                "## Minimal Example Logic",
                "",
            ]
        )

        for example in self.examples:
            lines.append(f"- {example}")

        lines.extend(
            [
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
                    "The next manuscript step after this scaffold is integration: the notation should be inserted into the Formal Model section of the manuscript draft, "
                    "then checked against the manuscript quality audit. The goal is not to make the paper look mathematical. "
                    "The goal is to make the conceptual commitments explicit enough that they can be criticized, tested, and improved."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
