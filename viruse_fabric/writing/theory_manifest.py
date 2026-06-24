from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
import re


@dataclass(frozen=True)
class ManifestSection:
    title: str
    body: str


@dataclass(frozen=True)
class TheoryManifestExportResult:
    title: str
    output_path: str
    section_count: int
    claim_count: int
    weak_point_count: int
    word_count: int
    interpretation: str


class TheoryManifestExporter:
    title = "Viruse Fabric Theory Manifest v2.0"

    core_claim = (
        "Causality is not a chain; it is a geometry of constraints."
    )

    central_persian_claim = (
        "علیت زنجیره نیست؛ هندسه‌ی قیود است."
    )

    claims: tuple[str, ...] = (
        "A cause is not merely a prior event; it is a local deformation in a constraint fabric.",
        "An observed path may look selected without being intended.",
        "Apparent targeting can emerge from route coherence, constructive attractors, and observer projection.",
        "A crisis node can be highly salient without being a true organizing target.",
        "Observer-facing narratives compress path structure into stories of intention.",
    )

    weak_points: tuple[tuple[str, str, str], ...] = (
        (
            "No external empirical validation yet",
            "The simulator has internal coherence, but it has not yet been tested against independent datasets or competing models.",
            "Treat current results as conceptual-computational evidence, not empirical proof.",
        ),
        (
            "Parameter sensitivity is still underdeveloped",
            "Several scores depend on formulas and weights that need systematic sensitivity analysis.",
            "Add parameter sweeps, ablation tests, and robustness reports in later versions.",
        ),
        (
            "The biological layer is intentionally abstract",
            "This protects safety, but also limits direct biological interpretation.",
            "Keep the layer non-operational and describe it as conceptual translation, not biological prediction.",
        ),
        (
            "Observer misreading is modeled, not measured",
            "The current observer error score is a theoretical construct rather than a validated psychological measure.",
            "Use it as an explanatory index until richer observer models are built.",
        ),
        (
            "The theory risks sounding metaphorical",
            "Terms such as curvature, fabric, and geodesic can look like metaphors if they are not tied to computations.",
            "Every theoretical term must stay connected to a defined score, path, classifier, or audit result.",
        ),
    )

    computational_evidence_rows: tuple[tuple[str, str, str], ...] = (
        (
            "v0.9",
            "Causal Curvature",
            "Showed how local tension, pressure, and connectivity can produce a curvature-like causal score.",
        ),
        (
            "v1.0",
            "Causal Geodesic",
            "Showed that changing spatial or temporal context can reroute the lowest-cost causal path.",
        ),
        (
            "v1.1",
            "Attractor Classifier",
            "Separated constructive attractors, tension wells, and strained gateways.",
        ),
        (
            "v1.2",
            "Apparent Targeting Index",
            "Measured when a coherent route appears target-like without assigning intention.",
        ),
        (
            "v1.3",
            "Abstract Viral Scenario Layer",
            "Mapped causal roles into a safe, non-operational biological vocabulary.",
        ),
        (
            "v1.4",
            "Scenario Auditor",
            "Checked the scenario layer for safety and internal consistency.",
        ),
        (
            "v1.5",
            "Observer Misreading",
            "Estimated when coherent paths are likely to be misread as intentional selection.",
        ),
        (
            "v1.6",
            "Intention Correction",
            "Converted intention-heavy narratives into constraint-based interpretations.",
        ),
        (
            "v1.7",
            "English Theory Chapter Exporter",
            "Generated a manuscript-facing English theory chapter from computational outputs.",
        ),
        (
            "v1.8",
            "Persian Theory Chapter Exporter",
            "Generated a Persian theory chapter with a safe conceptual boundary.",
        ),
        (
            "v1.9",
            "Bilingual Quality Audit",
            "Added a bilingual glossary and an automated quality gate for manuscript outputs.",
        ),
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/theory_manifest_v2_0.md")

    def export(self) -> TheoryManifestExportResult:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render_markdown()
        self.output_path.write_text(markdown, encoding="utf-8")

        return TheoryManifestExportResult(
            title=self.title,
            output_path=str(self.output_path),
            section_count=len(self.sections()),
            claim_count=len(self.claims),
            weak_point_count=len(self.weak_points),
            word_count=self._word_count(markdown),
            interpretation=(
                "The project now has a direct theory manifest that states its claims, "
                "boundaries, evidence, and unresolved weaknesses."
            ),
        )

    def sections(self) -> tuple[ManifestSection, ...]:
        return (
            ManifestSection("Core Claim", self._core_claim()),
            ManifestSection("What the Project Explains", self._what_it_explains()),
            ManifestSection("What the Project Does Not Claim", self._what_it_does_not_claim()),
            ManifestSection("Computational Evidence So Far", self._computational_evidence()),
            ManifestSection("Conceptual Boundary", self._conceptual_boundary()),
            ManifestSection("Biological Safety Boundary", self._biological_safety_boundary()),
            ManifestSection("Why This Is Not Just Metaphor", self._not_just_metaphor()),
            ManifestSection("Open Weak Points", self._open_weak_points()),
            ManifestSection("Next Research Questions", self._next_research_questions()),
        )

    def render_markdown(self) -> str:
        lines = [
            f"# {self.title}",
            "",
            f"**Core claim:** {self.core_claim}",
            "",
            f"**Persian formulation:** {self.central_persian_claim}",
            "",
            "> This manifest is not a declaration of proof. It is a boundary document: it states what the project currently claims, what it does not claim, what it has computed, and where it remains weak.",
            "",
        ]

        for section in self.sections():
            lines.extend(
                [
                    f"## {section.title}",
                    "",
                    section.body.strip(),
                    "",
                ]
            )

        markdown = "\n".join(lines)
        return self._clean_markdown(markdown)

    def _clean_markdown(self, markdown: str) -> str:
        cleaned_lines = []
        for line in markdown.splitlines():
            if line.startswith("            "):
                cleaned_lines.append(line[12:])
            else:
                cleaned_lines.append(line)
        return "\n".join(cleaned_lines) + "\n"

    def _core_claim(self) -> str:
        claim_lines = "\n".join(f"- {claim}" for claim in self.claims)

        return dedent(
            f"""
            Viruse Fabric starts from a simple reversal:

            **{self.core_claim}**

            In the usual chain view, explanation moves from one event to the next: A causes B, B causes C, and so on.
            In Viruse Fabric, explanation is not reduced to a sequence of arrows. Events are embedded in a fabric of constraints.
            A path becomes likely, stable, cheap, visible, or misleading because of the surrounding geometry of that fabric.

            The current claims are:

            {claim_lines}
            """
        )

    def _what_it_explains(self) -> str:
        return dedent(
            """
            The project explains a narrow but important class of patterns:

            - why some paths look inevitable after they occur;
            - why an outcome can appear target-like without requiring intention;
            - why the most salient node is not always the true organizing node;
            - why changing spatial or temporal context can reroute a causal path;
            - why observers compress route coherence into stories of purpose;
            - why some biological-looking patterns should be read as abstract constraint alignments rather than goal-directed agency.

            The strongest current example is the abstract viral pattern layer. In the coherent pattern scenario, the route
            A → B → C → D → E receives a high apparent targeting score because the path is coherent and supported by a constructive attractor.
            The model does not say that the pattern intends the endpoint. It says the endpoint becomes target-like to the observer because the route is stabilized by the fabric.
            """
        )

    def _what_it_does_not_claim(self) -> str:
        return dedent(
            """
            The project does not currently claim empirical proof.

            It also does not claim:

            - that all causality can be reduced to the current formulas;
            - that biological systems literally follow the simplified toy scenarios;
            - that viruses, pathogens, or abstract agents possess intention;
            - that apparent targeting is the same as real goal-directed planning;
            - that causal curvature is identical to physical spacetime curvature;
            - that the model predicts real-world biological outcomes;
            - that a safe conceptual scenario can be converted into an operational biological protocol.

            These limits are not cosmetic. They are part of the theory. If the model starts claiming more than it computes, it becomes decorative metaphysics with a Python folder. Humanity has produced enough of those.
            """
        )

    def _computational_evidence(self) -> str:
        rows = [
            "| Version | Layer | Evidence contributed |",
            "|---|---|---|",
        ]

        for version, layer, evidence in self.computational_evidence_rows:
            rows.append(f"| {version} | {layer} | {evidence} |")

        rows_text = "\n".join(rows)

        return dedent(
            f"""
            The project has accumulated evidence through staged computational layers.

            {rows_text}

            The evidence is internal and structural. It shows that the concepts are not merely verbal decorations:
            they correspond to route costs, classifications, scores, scenario audits, observer-error estimates, and generated theory outputs.
            """
        )

    def _conceptual_boundary(self) -> str:
        return dedent(
            """
            Viruse Fabric is a theory-building simulator.

            Its current role is to connect four layers:

            1. formal toy structures;
            2. causal geometry scores;
            3. observer-facing interpretations;
            4. manuscript-facing theoretical explanation.

            The model should be judged by whether these layers stay connected.
            A good result is not a dramatic sentence. A good result is a sentence that can be traced back to a path, score, classifier, scenario, or audit.
            """
        )

    def _biological_safety_boundary(self) -> str:
        return dedent(
            """
            The biological layer is intentionally non-operational.

            It does not contain real pathogens, real hosts, doses, receptors, laboratory protocols, experimental instructions, or deployable interventions.
            Biological language is used only as a safe translation layer for abstract causal roles.

            The safe reading is:

            - contact-like role, not real exposure design;
            - compatibility-like transition, not receptor modeling;
            - regulatory-context shift, not molecular protocol;
            - persistence-like stabilization, not replication mechanism;
            - visible endpoint, not biological endpoint prediction.

            If a future version starts producing actionable biological procedures, that version should be rejected or redesigned.
            """
        )

    def _not_just_metaphor(self) -> str:
        return dedent(
            """
            The project uses words such as fabric, curvature, geodesic, attractor, and projection.
            These words can become empty metaphors if they float away from computation.

            In this project, each term is tied to an operational role:

            - causal curvature is computed from local tension, fabric pressure, and degree;
            - causal geodesic refers to a lowest-cost route through the fabric;
            - constructive attractor, tension well, and strained gateway are classifier outputs;
            - apparent targeting is an index built from route support, path coverage, gravity alignment, and penalties;
            - observer misreading is an explicit score for the risk of intention-based interpretation;
            - intention correction rewrites observer stories into constraint-based explanations.

            The theory remains worth developing only while this connection stays intact.
            """
        )

    def _open_weak_points(self) -> str:
        rows = [
            "| Weak point | Why it matters | Current response |",
            "|---|---|---|",
        ]

        for weak_point, why_it_matters, response in self.weak_points:
            rows.append(f"| {weak_point} | {why_it_matters} | {response} |")

        return "\n".join(rows)

    def _next_research_questions(self) -> str:
        return dedent(
            """
            The next useful questions are not cosmetic. They should stress the theory.

            1. Can the same causal fabric produce different observer narratives under different projections?
            2. How sensitive are apparent targeting scores to parameter changes?
            3. Can the model distinguish a constructive attractor from a merely dramatic crisis node across many generated scenarios?
            4. Can English and Persian theory outputs remain conceptually aligned without hand-polishing?
            5. Can the manifest itself be audited by the chapter quality system?
            6. What would count as a failed prediction or failed explanation for Viruse Fabric?

            The last question is the most important. A theory that cannot say how it might fail is not a theory yet. It is just confidence wearing a lab coat.
            """
        )

    def _word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
