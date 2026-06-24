from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class ValidationCriterion:
    name: str
    category: str
    question: str
    method: str
    pass_signal: str
    fail_signal: str
    priority: str


@dataclass(frozen=True)
class ValidationProtocolReport:
    title: str
    output_path: str
    criterion_count: int
    high_priority_count: int
    failure_condition_count: int
    presentation_status: str
    passed: bool
    interpretation: str


class ValidationProtocolBuilder:
    title = "Viruse Fabric Validation Protocol v2.4"

    criteria: tuple[ValidationCriterion, ...] = (
        ValidationCriterion(
            name="Constructive attractor ablation",
            category="ablation",
            question="Does apparent targeting drop when the constructive attractor is removed?",
            method=(
                "Compare a coherent constructive route against the same route after removing constructive support."
            ),
            pass_signal="Apparent targeting and observer misreading decrease substantially.",
            fail_signal="The model still reports high targeting without a constructive attractor.",
            priority="high",
        ),
        ValidationCriterion(
            name="Tension well injection",
            category="stress test",
            question="Does the model avoid treating crisis concentration as intention?",
            method=(
                "Inject a tension well into B or C and check whether the path avoids it instead of promoting it to a target."
            ),
            pass_signal="Targeting remains low and the path avoids the tension well.",
            fail_signal="The model turns a tension well into a strong target-like explanation.",
            priority="high",
        ),
        ValidationCriterion(
            name="Strained gateway penalty",
            category="stress test",
            question="Does the model distinguish forced passage from target-like organization?",
            method=(
                "Evaluate shortcut routes that pass through a strained gateway and compare them with coherent supported routes."
            ),
            pass_signal="Shortcut routes remain low-targeting relative to coherent supported routes.",
            fail_signal="A costly gateway is misread as a constructive target.",
            priority="high",
        ),
        ValidationCriterion(
            name="Parameter sensitivity sweep",
            category="sensitivity",
            question="Are conclusions stable under reasonable changes in weights and thresholds?",
            method=(
                "Sweep scoring weights for path coverage, gravity alignment, constructive support, and penalties."
            ),
            pass_signal="Rank ordering of core scenarios remains broadly stable.",
            fail_signal="Small parameter changes reverse the main interpretation.",
            priority="high",
        ),
        ValidationCriterion(
            name="Baseline comparison",
            category="baseline",
            question="Does the model outperform a trivial rule-based explanation?",
            method=(
                "Compare Viruse Fabric scoring against a simple baseline that labels any complete path as target-like."
            ),
            pass_signal="Viruse Fabric rejects invalid and disrupted cases better than the trivial baseline.",
            fail_signal="The baseline performs equally well or better on stress scenarios.",
            priority="high",
        ),
        ValidationCriterion(
            name="Projection perturbation",
            category="observer model",
            question="Can the same causal fabric produce different observer-facing readings under different projections?",
            method=(
                "Perturb observer visibility and salience assumptions while keeping the underlying path fixed."
            ),
            pass_signal="Observer misreading changes while causal structure remains stable.",
            fail_signal="Observer misreading is insensitive to projection changes.",
            priority="medium",
        ),
        ValidationCriterion(
            name="Negative control scenarios",
            category="negative control",
            question="Can the model avoid finding target-like structure where none should exist?",
            method=(
                "Generate incoherent routes with no constructive attractor and no stable path support."
            ),
            pass_signal="Targeting and misreading remain low.",
            fail_signal="The model reports high targeting for incoherent unsupported routes.",
            priority="high",
        ),
        ValidationCriterion(
            name="External validation boundary",
            category="external validation",
            question="What kind of evidence would be needed before making stronger claims?",
            method=(
                "Define external datasets, competing models, or expert-coded scenario sets that could challenge the model."
            ),
            pass_signal="The project clearly states that external validation is not yet complete.",
            fail_signal="The project presents internal simulations as empirical proof.",
            priority="high",
        ),
    )

    failure_conditions: tuple[str, ...] = (
        "The model makes almost every scenario look target-like.",
        "The model makes no scenario look target-like, including coherent constructive routes.",
        "Removing constructive attractors does not reduce apparent targeting.",
        "Adding a tension well increases targeting instead of triggering avoidance or penalty.",
        "Small parameter changes reverse the main scenario ranking.",
        "A trivial baseline performs as well as the full model.",
        "Observer misreading does not respond to projection changes.",
        "The project claims empirical proof without external validation.",
    )

    current_status = (
        "Viruse Fabric is currently suitable as a conceptual-computational research prototype. "
        "It is not yet suitable for strong public claims, empirical claims, or biological prediction."
    )

    safety_boundary = (
        "This validation protocol remains conceptual and non-operational. "
        "It does not use real pathogens, real hosts, doses, receptors, laboratory protocols, "
        "executable biological procedures, or deployable interventions."
    )

    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path or Path("outputs/validation_protocol_v2_4.md")

    def build(self) -> ValidationProtocolReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        markdown = self.render_markdown()
        self.output_path.write_text(markdown, encoding="utf-8")

        high_priority_count = sum(
            1 for criterion in self.criteria if criterion.priority == "high"
        )

        return ValidationProtocolReport(
            title=self.title,
            output_path=str(self.output_path),
            criterion_count=len(self.criteria),
            high_priority_count=high_priority_count,
            failure_condition_count=len(self.failure_conditions),
            presentation_status="research prototype only",
            passed=True,
            interpretation=(
                "The project now has a validation protocol that defines what would strengthen, weaken, "
                "or falsify its current internal claims."
            ),
        )

    def render_markdown(self) -> str:
        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This document defines how Viruse Fabric should be tested before it is presented as anything stronger "
                "than a conceptual-computational research prototype."
            ),
            "",
            "The goal is not to make the project look impressive. The goal is to identify what would make it fail.",
            "",
            "## Current status",
            "",
            "**Presentation status:** research prototype only",
            "",
            self.current_status,
            "",
            "## Validation criteria",
            "",
            "| Criterion | Category | Priority | Question | Method | Pass signal | Fail signal |",
            "|---|---|---|---|---|---|---|",
        ]

        for criterion in self.criteria:
            lines.append(
                f"| {criterion.name} | {criterion.category} | {criterion.priority} | "
                f"{criterion.question} | {criterion.method} | "
                f"{criterion.pass_signal} | {criterion.fail_signal} |"
            )

        lines.extend(
            [
                "",
                "## Failure conditions",
                "",
            ]
        )

        for item in self.failure_conditions:
            lines.append(f"- {item}")

        lines.extend(
            [
                "",
                "## Minimum bar before stronger presentation",
                "",
                "Before the project deserves stronger public presentation, it should pass:",
                "",
                "1. ablation tests;",
                "2. parameter sensitivity sweeps;",
                "3. negative control scenarios;",
                "4. baseline comparison;",
                "5. projection perturbation tests;",
                "6. a clearly documented external validation plan.",
                "",
                "## What would count as progress",
                "",
                (
                    "Progress means the model becomes harder to fool. "
                    "It should reject broken scenarios, remain stable under reasonable parameter variation, "
                    "and outperform trivial baselines."
                ),
                "",
                "## What would count as failure",
                "",
                (
                    "Failure means the model is too flexible. "
                    "If it can explain every pattern after the fact, it explains nothing. "
                    "If it cannot distinguish coherent constructive routes from crisis concentration, "
                    "its central claim is not yet useful."
                ),
                "",
                "## Safety boundary",
                "",
                self.safety_boundary,
                "",
                "## Interpretation",
                "",
                (
                    "Viruse Fabric has internal structure, manuscript outputs, visual explanation, and internal stress tests. "
                    "The next serious step is validation pressure: sensitivity, ablation, negative controls, and baselines."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
