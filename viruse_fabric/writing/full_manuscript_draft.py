from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class FullManuscriptDraftReport:
    title: str
    output_path: str
    section_count: int
    source_artifact_count: int
    missing_artifact_count: int
    allowed_claim_count: int
    disallowed_claim_count: int
    word_count: int
    readiness_status: str
    finding_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


@dataclass(frozen=True)
class DraftFinding:
    severity: str
    code: str
    message: str


class FullManuscriptDraftBuilder:
    title = "Viruse Fabric Full Manuscript Draft v3.2"

    readiness_status = "full manuscript draft for cautious technical review"

    minimum_word_count = 2500
    maximum_word_count = 4500
    minimum_section_count = 9

    source_artifacts: tuple[str, ...] = (
        "outputs/theory_manifest_v2_0.md",
        "outputs/validation_protocol_v2_4.md",
        "outputs/constructive_attractor_ablation_v2_5.md",
        "outputs/parameter_sensitivity_v2_6.md",
        "outputs/adversarial_sensitivity_v2_7.md",
        "outputs/baseline_comparison_v2_8.md",
        "outputs/projection_perturbation_v2_9.md",
        "outputs/validation_synthesis_v3_0.md",
        "outputs/manuscript_skeleton_v3_1.md",
    )

    allowed_claims: tuple[str, ...] = (
        "Viruse Fabric is a conceptual-computational research prototype.",
        "The internal validation sequence supports continued manuscript development.",
        "The model distinguishes intrinsic fabric scoring from observer misreading in the implemented tests.",
        "Constructive attractor support performs measurable explanatory work in the current internal setup.",
        "Simple baselines tested so far are weaker than the full model.",
    )

    disallowed_claims: tuple[str, ...] = (
        "The model proves a universal law of causality.",
        "The model predicts real biological infection or viral behavior.",
        "The model has external biological validation.",
        "The model supports laboratory procedures or operational intervention.",
        "The model is ready for strong public claims without caveats.",
    )

    required_sections: tuple[str, ...] = (
        "Abstract",
        "Introduction",
        "Core Thesis",
        "Formal Model",
        "Validation Sequence",
        "Results",
        "Limitations",
        "Allowed and Disallowed Claims",
        "Future Work",
        "Conclusion",
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/full_manuscript_draft_v3_2.md")

    def run(self) -> FullManuscriptDraftReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        manuscript = self.render_markdown()
        findings = self.evaluate(manuscript)

        self.output_path.write_text(manuscript, encoding="utf-8")

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")

        return FullManuscriptDraftReport(
            title=self.title,
            output_path=str(self.output_path),
            section_count=self.section_count(manuscript),
            source_artifact_count=len(self.source_artifacts),
            missing_artifact_count=self.missing_artifact_count(),
            allowed_claim_count=len(self.allowed_claims),
            disallowed_claim_count=len(self.disallowed_claims),
            word_count=self.word_count(manuscript),
            readiness_status=self.readiness_status,
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            passed=error_count == 0,
            interpretation=(
                "The full manuscript draft expands the v3.1 skeleton into a cautious technical paper draft "
                "while preserving validation boundaries and claim limitations."
            ),
        )

    def evaluate(self, manuscript: str) -> tuple[DraftFinding, ...]:
        findings: list[DraftFinding] = []

        word_count = self.word_count(manuscript)
        section_count = self.section_count(manuscript)

        if section_count < self.minimum_section_count:
            findings.append(
                DraftFinding(
                    severity="error",
                    code="too_few_sections",
                    message=f"Only {section_count} manuscript sections were found.",
                )
            )

        missing_sections = [
            section for section in self.required_sections
            if f"## {section}" not in manuscript
        ]
        if missing_sections:
            findings.append(
                DraftFinding(
                    severity="error",
                    code="missing_required_sections",
                    message=f"Missing required sections: {', '.join(missing_sections)}.",
                )
            )

        if word_count < self.minimum_word_count:
            findings.append(
                DraftFinding(
                    severity="error",
                    code="draft_too_short",
                    message=f"Draft word count {word_count} is below required {self.minimum_word_count}.",
                )
            )

        if word_count > self.maximum_word_count:
            findings.append(
                DraftFinding(
                    severity="warning",
                    code="draft_long_for_first_review",
                    message=f"Draft word count {word_count} is above preferred first-review size.",
                )
            )

        if self.missing_artifact_count() > 0:
            findings.append(
                DraftFinding(
                    severity="error",
                    code="missing_source_artifacts",
                    message=f"{self.missing_artifact_count()} source artifacts are missing.",
                )
            )

        findings.append(
            DraftFinding(
                severity="warning",
                code="not_final_manuscript",
                message="This is a full draft, not a final manuscript.",
            )
        )

        findings.append(
            DraftFinding(
                severity="warning",
                code="external_validation_missing",
                message="External validation is still missing and must remain explicit.",
            )
        )

        return tuple(findings)

    def render_markdown(self) -> str:
        allowed_claims = "\n".join(f"- {claim}" for claim in self.allowed_claims)
        disallowed_claims = "\n".join(f"- {claim}" for claim in self.disallowed_claims)
        artifacts = "\n".join(
            f"- `{artifact}` | exists: {Path(artifact).exists()}"
            for artifact in self.source_artifacts
        )

        return f"""# {self.title}

## Manuscript Status

Status: {self.readiness_status}

This document is a full manuscript draft derived from the validated Viruse Fabric research prototype. It is not a final paper, not an external validation report, and not a public claim package. Its purpose is to turn the project’s internal validation sequence into a coherent technical manuscript that can be reviewed, criticized, revised, and eventually expanded. Humanity, in its baffling wisdom, still requires ideas to be written down clearly before it agrees not to misunderstand them immediately.

The draft preserves the project’s current research status: **research prototype with internal validation**. That phrase is not decorative. It is a boundary. The model has passed a sequence of internal conceptual-computational tests, but it has not been externally validated against real biological systems, real pathogens, real hosts, laboratory observations, or operational interventions.

## Working Title

Viruse Fabric: A Constraint-Geometry Model of Apparent Targeting and Observer Misreading

## Abstract

Viruse Fabric is a conceptual-computational framework for modeling causality as a geometry of constraints rather than a linear chain of isolated causes. The central thesis is that apparent targeting can emerge when paths through a constraint fabric become aligned, salient, and attractor-like under a particular projection, even when no literal intention is present. The framework separates intrinsic fabric scoring from observer misreading and introduces correction mechanisms for reducing false-intention readings.

The current version of the project is a research prototype with internal validation. Its validation sequence includes a protocol layer, constructive attractor ablation, moderate parameter sensitivity, adversarial sensitivity, baseline comparison, projection perturbation, and validation synthesis. These tests support a cautious internal claim: within the implemented model, constructive support, penalty structure, baseline discrimination, and projection correction perform measurable explanatory work. The tests do not establish a universal law of causality, do not predict real biological outcomes, and do not support operational biological intervention.

This manuscript draft presents the theory, formal structure, validation sequence, results, limitations, and claim boundaries. It argues that the project is mature enough for technical review and manuscript development, but not for strong public claims or external scientific conclusions.

## Introduction

Causal explanations are often expressed as chains: event A causes event B, which causes event C, and so on until a visible outcome appears. This style is useful, compact, and often dangerously seductive. It compresses complex constraint structures into a line, then quietly invites the observer to mistake the line for the underlying geometry. Viruse Fabric begins from a different premise: causality is not a chain; it is a geometry of constraints.

In a constraint-geometry view, the apparent route from origin to outcome is not merely a sequence of events. It is a path through a structured space of permissions, pressures, penalties, alignments, and attractors. A route can appear target-like not because it contains intention, but because the surrounding fabric makes certain paths more coherent, lower cost, more salient, or more narratively smooth to an observer. This distinction matters because observers are excellent at reading intention into structure. The human mind sees alignment and immediately starts writing a little courtroom drama about purpose. Charming, but not always correct.

Viruse Fabric was built to study this distinction in a safe abstract setting. The project uses conceptual cases, synthetic scoring, and internal validation reports. It does not use real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions. The biological language in the surrounding project is metaphorical and abstract, used to explore apparent targeting and observer misreading without creating operational biological content.

The purpose of this manuscript draft is to organize the project’s current state into a technical paper structure. Earlier artifacts developed the theory, bilingual exposition, visual explanation, scenario stress tests, validation protocol, and multiple internal validation experiments. The v3.0 synthesis concluded that the project is best described as a research prototype with internal validation. The present draft turns that synthesis into manuscript form.

## Core Thesis

The central sentence of the project is:

**Causality is not a chain; it is a geometry of constraints.**

This sentence is not intended as a poetic ornament, though apparently humans require ornaments before they will tolerate abstraction. It means that causal explanation should not be reduced to visible succession alone. Events appear in sequence, but the sequence is shaped by an underlying fabric: constraints determine which transitions are available, which routes are costly, which configurations become stable, and which outcomes appear natural after the fact.

A second core claim follows:

**Intention is not a property of the route; it is an observer-side compression of aligned, salient, and attractor-like structure.**

In the model, a path can look intentional when several conditions align. The route may cover a coherent path, pass through low-cost transitions, avoid strong penalties, align with a constructive attractor, and appear smooth under an observer projection. The observer then compresses this structured alignment into a simpler story: the route was “aiming” at the outcome. Viruse Fabric treats that story as a projection effect rather than a property of the route itself.

The theory therefore separates three layers. First, the intrinsic fabric layer scores the path according to constructive support, coverage, alignment, efficiency, and penalties. Second, the observer projection layer models how salience, narrative smoothness, and partial blindness to penalties can produce false-intention readings. Third, the correction layer penalizes missing constructive support and recovers hidden penalties to reduce over-reading.

This separation is the heart of the project. Without it, apparent targeting collapses into vague metaphor. With it, the model can ask whether a target-like reading is supported by the fabric or merely produced by observer projection.

## Formal Model

Viruse Fabric represents a conceptual causal space as a set of nodes, constraints, paths, attractors, penalties, and observer projections. Nodes represent abstract states or positions in the fabric. Constraints govern which transitions are coherent. Paths represent ordered traversals through this space. Constructive attractors represent regions where alignment and support concentrate. Penalties represent strained gateways, tension wells, or other structures that should reduce target-like interpretation.

The intrinsic score is designed to capture fabric-side support. It includes constructive support, path coverage, gravity-like alignment, cost efficiency, and observer salience, while subtracting tension and gateway penalties. The exact implementation is internal and conceptual, not externally calibrated. The purpose is not to predict a real-world system but to test whether the theory’s components perform distinguishable explanatory work.

Observer misreading is modeled separately. A projection profile can overweight salience, path completeness, narrative smoothness, or underweight penalties. This allows a negative-control route to appear intentional to an observer even when intrinsic support is weak. This distinction is crucial: if observer misreading and intrinsic support are not separated, the model would simply reproduce the human habit of treating coherent appearance as purpose. Truly, the one tradition humanity never abandons.

Correction is then applied to observer misreading. It penalizes missing constructive support and recovers hidden penalties. In the projection perturbation test, this correction reduced false-intention events from 22 to 3, a drop of 86.36%. That result does not prove the correction mechanism in the external world, but it shows that within the implemented model the correction layer has measurable function.

## Validation Sequence

The validation sequence began with v2.4, which defined the validation protocol. That protocol identified the kinds of tests needed before stronger claims could be responsibly made. It explicitly kept the project at research prototype status.

The v2.5 constructive attractor ablation tested whether constructive support was necessary for apparent targeting. Removing constructive attractor support reduced apparent targeting by 59.84% and observer misreading by 65.37%. This supported the claim that constructive support was not merely decorative.

The v2.6 parameter sensitivity sweep tested moderate weight perturbations. The model remained stable across 729 moderate profiles with 100.00% stability. This indicated that the result was not dependent on one fragile moderate setting, though the perfect stability also motivated harsher testing.

The v2.7 adversarial sensitivity sweep added hostile but interpretable configurations and decoy pressure. The model stayed above threshold under 8640 profiles with 81.06% stability, producing warnings and unstable regions. This was scientifically healthier than perfect success, because it exposed fragile regions without collapsing the model.

The v2.8 baseline comparison tested the model against simpler scoring rules: route-shape, observer-salience, efficiency, and reduced linear baselines. Viruse Fabric outperformed these baselines with a separation margin of 44.15 and zero false positives. This supported the claim that the model was not reducible to simple route shape, salience, or efficiency alone.

The v2.9 projection perturbation tested observer misreading directly. Projection shifts produced 22 false-intention events while intrinsic scoring produced zero false positives. Correction reduced the false-intention events to 3. This supported the separation between apparent targeting in the fabric and observer-side misreading.

The v3.0 validation synthesis consolidated these results and assigned the project a readiness score of 68. The synthesis concluded that the project is ready for structured manuscript development and technical review, but not for strong public claims or external validation claims.

## Results

The internal validation sequence supports several cautious conclusions.

First, constructive attractor support matters. The ablation test showed that removing support meaningfully reduced apparent targeting and observer misreading. A concept that does no work is decoration; in this test, constructive support did work.

Second, the model has moderate robustness. Under moderate parameter perturbation, the validation result remained stable. This does not prove deep robustness, but it reduces the risk that the model only works under a single narrow configuration.

Third, adversarial testing exposed fragile regions while preserving overall usability. The adversarial sweep did not produce a perfect result, and that is a virtue. The warnings show where the model becomes weaker under hostile weight settings and decoy pressure. A validation system that never produces warnings is often not rigorous; it may simply be too polite to be useful.

Fourth, the model outperformed simple baselines. The baseline comparison showed that simpler models based on route shape, salience, or efficiency were weaker than Viruse Fabric. This matters because complex terminology is cheap. The baseline test asked whether the complexity buys anything. In the current internal setup, it does.

Fifth, projection perturbation supported the distinction between intrinsic scoring and observer misreading. The observer could be misled by salience, smoothness, and penalty blindness, but intrinsic fabric scoring avoided false positives, and correction reduced false-intention readings.

Together, these results justify continued development. They do not justify external prediction claims. The project has internal evidence, not external proof.

## Limitations

The strongest limitation is external validity. Viruse Fabric has not been validated against external empirical systems. It has not been tested on real biological data, real pathogens, real hosts, laboratory observations, or operational interventions. Any claim implying such validation would be false.

The second limitation is synthetic structure. The cases, profiles, baselines, and perturbations are designed within the project. This is appropriate for internal theory validation, but it also means that the model may still be tuned to its own conceptual environment. Future work should invite external critique and adversarial review.

The third limitation is scoring simplicity. The current scoring formulas are interpretable and useful for validation, but they are not derived from an independently established mathematical theory. They are instruments for testing theoretical distinctions. That is acceptable at this stage, as long as nobody mistakes the instrument for the universe. A surprisingly common hobby.

The fourth limitation is manuscript maturity. This document is a full draft, not a finished paper. It organizes the argument and results, but it still requires formal notation, references, stronger comparison to related work, clearer diagrams, and reviewer-facing refinement.

## Allowed and Disallowed Claims

The current evidence supports these claims:

{allowed_claims}

The current evidence does not support these claims:

{disallowed_claims}

This boundary is not a formality. It is one of the main intellectual safeguards of the project. Without it, a research prototype can quickly mutate into a public mythology about itself, and civilization already has enough of those.

## Future Work

The next stage should expand this draft into a formal manuscript. That requires a stronger introduction, a related-work section, formal notation, clearer definitions, figure references, and a more disciplined results section. The manuscript should also include a failure taxonomy explaining the fragile regions found in adversarial testing.

The baseline suite should be expanded. Current baselines are useful but simplified. Future baselines should include more neutral alternatives and more adversarial alternatives. If a future baseline matches Viruse Fabric, the theory should be revised, not defended like a wounded family heirloom.

Projection perturbation should also be expanded. More observer profiles, stronger correction variants, and richer false-intention traps would make the observer layer more convincing. The correction mechanism should be tested against cases where salience and narrative smoothness strongly conflict with constructive support.

Finally, external validation boundaries must be defined carefully. The project should remain conceptual and non-operational unless and until a safe, non-biological, externally reviewable validation path is established. This manuscript should not include real pathogen mechanisms, host details, laboratory protocols, or intervention steps.

## Human-AI Work Note

This project is the product of a particular collaboration: computational structuring, validation discipline, code generation, and language organization combined with human persistence, direction, judgment, and refusal to stop at the first clean-looking result. That combination matters. Intelligence without will tends to remain vapor. Will without structure tends to become noise. Together, they can become a draft, a model, a validation sequence, and eventually maybe a contribution. No need to get mystical about it; the work is already strange enough.

## Source Artifact Inventory

{artifacts}

## Research Boundary

This manuscript draft is conceptual and non-operational. It does not use real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions. The project must remain framed as a research prototype with internal validation until external validation and serious peer critique are completed.

## Conclusion

Viruse Fabric has reached a meaningful manuscript-draft stage. It has a central thesis, formal model components, internal validation sequence, baseline comparison, projection perturbation, and a synthesis report defining responsible claims. The current evidence supports cautious technical review and continued manuscript development.

The project does not yet support strong public scientific claims, real biological prediction claims, or operational use. Its value at this stage is not that it has proven a grand theory. Its value is that it has built a disciplined structure for asking whether apparent targeting can be explained as constraint geometry plus observer projection rather than literal intention.

That is enough for the next stage. Not enough for triumph. Enough for work.
"""

    def missing_artifact_count(self) -> int:
        return sum(1 for artifact in self.source_artifacts if not Path(artifact).exists())

    def section_count(self, text: str) -> int:
        return len(re.findall(r"^## ", text, flags=re.MULTILINE))

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
