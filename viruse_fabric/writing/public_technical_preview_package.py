"""Public technical preview package for Viruse Fabric v4.0.

This module generates a public-safe technical preview artifact.

The artifact summarizes the project thesis, conceptual model, validation status,
manuscript status, citation-readiness status, and limitations while preserving
the project's official boundary:

research prototype with internal validation

It does not claim external validation, biological applicability, clinical
relevance, laboratory relevance, operational guidance, or submission readiness.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_ARTIFACTS = [
    PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md",
    PROJECT_ROOT / "outputs" / "integrated_manuscript_quality_audit_v3_8.md",
    PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md",
    PROJECT_ROOT / "outputs" / "validation_synthesis_v3_0.md",
    PROJECT_ROOT / "outputs" / "public_demo_report_v2_3.md",
    PROJECT_ROOT / "outputs" / "fabric_diagram_v2_1.png",
]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "public_technical_preview_package_v4_0.md"


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "not operational guidance",
    "not biological guidance",
    "not clinical guidance",
    "not laboratory guidance",
    "internal validation only",
    "internal validation",
    "does not provide external validation",
    "does not establish empirical adequacy",
    "does not support biological intervention",
    "does not support clinical intervention",
    "does not support laboratory use",
    "does not support operational use",
    "citation placeholders are not citations",
]


PUBLIC_SECTIONS = [
    "Public Technical Preview",
    "One-Sentence Thesis",
    "Plain-Language Summary",
    "What the Project Is",
    "What the Project Is Not",
    "Core Concepts",
    "Conceptual Model",
    "Validation Status",
    "Manuscript Status",
    "Citation Status",
    "Limitations",
    "Safe Public Description",
    "Suggested Public Abstract",
    "Review Checklist",
    "Next Steps",
]


OVERCLAIM_PATTERNS = [
    r"\bproves\b",
    r"\bproven\b",
    r"\bestablishes\b",
    r"\bdefinitive\b",
    r"\buniversal theory\b",
    r"\bexternally validated\b",
    r"\bclinical relevance\b",
    r"\blaboratory relevance\b",
    r"\bbiological intervention\b",
    r"\boperational intervention\b",
    r"\bpredicts real biological systems\b",
    r"\bready for submission\b",
    r"\bpublication-ready\b",
    r"\bsubmission-ready manuscript\b",
]


SAFE_CONTEXT_CUES = [
    "not",
    "does not",
    "no claim",
    "without",
    "cannot",
    "should not",
    "not yet",
    "boundary",
    "limitation",
    "limitations",
    "prototype",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not operational",
    "not biological",
    "not clinical",
    "not laboratory",
]


SAFE_SECTION_CUES = [
    "what the project is not",
    "unsafe validation statement",
    "limitations",
    "final boundary statement",
    "review checklist",
    "public communication guidance",
    "avoid this kind of language",
    "unsafe because",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class PublicPreviewResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    section_count: int
    word_count: int
    boundary_phrase_count: int
    public_section_count: int
    overclaim_count: int
    fake_citation_count: int
    limitation_count: int
    next_step_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    interpretation: str


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w\-']+\b", text, flags=re.UNICODE))


def count_sections(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.startswith("## "))


def count_present_terms(text: str, terms: list[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def line_is_safe_context(line: str) -> bool:
    lowered = line.lower()
    return any(cue in lowered for cue in SAFE_CONTEXT_CUES)


def update_header_context(line: str, active_headers: list[str]) -> list[str]:
    if not line.startswith("#"):
        return active_headers

    level = len(line) - len(line.lstrip("#"))
    title = line.lstrip("#").strip()

    trimmed = active_headers[: max(level - 1, 0)]
    trimmed.append(title)
    return trimmed


def safe_section_context(active_headers: list[str], previous_line: str) -> bool:
    context = " / ".join(active_headers + [previous_line]).lower()
    return any(cue in context for cue in SAFE_SECTION_CUES)


def detect_overclaims(text: str) -> list[str]:
    findings: list[str] = []
    active_headers: list[str] = []
    previous_nonempty = ""

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        active_headers = update_header_context(stripped, active_headers)
        lowered = stripped.lower()

        if line_is_safe_context(lowered):
            previous_nonempty = stripped
            continue

        if safe_section_context(active_headers, previous_nonempty):
            previous_nonempty = stripped
            continue

        for pattern in OVERCLAIM_PATTERNS:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                findings.append(stripped)
                break

        previous_nonempty = stripped

    return findings


def detect_fake_citations(text: str) -> list[str]:
    findings: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def missing_source_artifacts() -> list[Path]:
    return [path for path in SOURCE_ARTIFACTS if not path.exists()]


def relative(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def render_report() -> str:
    source_lines = "\n".join(
        f"- `{relative(path)}` — {'present' if path.exists() else 'missing'}"
        for path in SOURCE_ARTIFACTS
    )

    return f"""# Public Technical Preview Package v4.0

## Public Technical Preview
Viruse Fabric is presented here as a cautious technical preview.

Current status:

`research prototype with internal validation`

This package is designed for safe public explanation. It summarizes the thesis,
model vocabulary, validation history, manuscript status, citation status, and
limits of the project without converting internal validation into external
scientific proof.

## One-Sentence Thesis
Causality is not treated as a simple chain of events; it is modeled as a geometry
of constraints that shapes which paths become compatible, stable, or apparently
purposeful.

## Plain-Language Summary
Viruse Fabric asks a narrow conceptual question: what if some systems look
purposeful not because they contain intention, but because constraints shape the
available paths so strongly that observers later read the result as directed?

In this framing, a path can appear goal-like without containing a real goal. A
constructive attractor can concentrate compatible paths without intending
anything. An observer can project purpose onto a pattern after seeing the
outcome. The model separates these pieces so the manuscript can discuss apparent
intentionality without claiming literal agency.

The project is abstract and conceptual-computational. It does not provide
biological guidance, clinical guidance, laboratory guidance, or operational
intervention advice.

## What the Project Is
Viruse Fabric is:

- a conceptual-computational research prototype,
- an internal validation project,
- a manuscript-building project,
- a model for reasoning about constraint geometry,
- a way to separate apparent intentionality from literal intention,
- a framework for testing whether observer projection can create false readings
  of purpose,
- a technical preview candidate for cautious review.

## What the Project Is Not
Viruse Fabric is not:

- a biological protocol,
- a laboratory protocol,
- a clinical model,
- a medical claim,
- an operational intervention system,
- an externally validated theory,
- a submission-ready manuscript,
- a universal theory of causality,
- a replacement for existing causal frameworks.

This distinction matters because the project is strongest when it stays inside
its evidence boundary. The internal validation results are useful for technical
review, but they do not establish empirical adequacy outside the prototype.

## Core Concepts
### Constraint
A constraint is any abstract condition, pressure, relation, or filter that shapes
the space of possible paths.

A constraint does not need to be a command, a force, or an intention. It can make
one path easier, another harder, one configuration more stable, and another less
compatible.

### Constraint Geometry
Constraint geometry is the overall shape formed by constraints, pressures,
relations, filters, and compatible paths.

Instead of asking only whether A caused B, the model asks what geometry made
some paths more compatible or more stable than others.

### Constructive Attractor
A constructive attractor is a region or node where compatible paths, tension,
connection, and pressure concentrate.

It does not intend. It organizes.

### Path Compatibility
Path compatibility describes how well a path fits the active constraints in the
fabric.

A compatible path is not necessarily chosen by an agent. It may simply survive
or remain coherent under the current constraint structure.

### Observer Projection
Observer projection is the interpretation an observer places on a path or
pattern.

After seeing an outcome, an observer may describe the path as if it had a goal.
Viruse Fabric treats that reading as something to be modeled, not automatically
accepted.

### Apparent Intentionality
Apparent intentionality appears when constraint geometry, attractor
concentration, path compatibility, and observer projection align.

The safe phrasing is:

Something may look purposeful without containing literal purpose.

## Conceptual Model
The formal scaffold used in the integrated manuscript is:

`F = (C, P, A, O)`

Where:

- `C` represents constraints,
- `P` represents possible paths,
- `A` represents constructive attractors,
- `O` represents observer projection.

Additional notation includes:

- `K(p, C)` for path compatibility,
- `alpha(p, A)` for attractor concentration,
- `I_app(p, O)` for apparent intentionality,
- `I_false` for false intentionality,
- `R(I_app)` for a correction operator,
- `Delta_R` for correction drop.

This notation is a scaffold. It helps organize the manuscript, but it is not a
complete mathematical theory.

## Validation Status
The project has internal validation artifacts, including:

- scenario stress testing,
- constructive attractor ablation,
- parameter sensitivity sweep,
- adversarial sensitivity sweep,
- baseline comparison,
- projection perturbation,
- validation synthesis,
- integrated manuscript quality audit.

The internal validation history supports a cautious technical-review status. It
does not provide external validation.

Safe validation statement:

Viruse Fabric has internal validation results that support further technical
review of the prototype.

Unsafe validation statement:

The model is externally validated or predicts real-world biological systems.

The unsafe statement is outside the current project boundary.

## Manuscript Status
The manuscript has progressed through:

- skeleton,
- full draft,
- quality audit,
- related-work positioning scaffold,
- formal notation scaffold,
- manuscript integration plan,
- integrated manuscript draft,
- integrated manuscript quality audit.

The latest manuscript stage supports cautious technical review.

It is not a final paper. It is not submission-ready.

## Citation Status
The project now has a citation placeholder and literature mapping plan.

That plan identifies literature families and future search queries. It does not
create real citations.

Citation placeholders are not citations. A slot such as `CITE_MODEL_VALIDATION`
is only a marker for later source lookup. It is not evidence and should not be
converted into a bibliography entry without source verification.

The next citation stage must use real source search and careful verification.

## Source Artifacts
{source_lines}

## Limitations
The public preview must keep the following limitations visible:

- Internal validation does not establish external validation.
- Conceptual coherence does not establish empirical truth.
- Formal notation does not make the model a complete mathematical theory.
- Related-work positioning does not replace real literature review.
- Citation placeholders are not citations.
- The manuscript is not submission-ready.
- The model does not support biological, clinical, laboratory, or operational
  claims.
- Apparent intentionality is not literal intention.

## Safe Public Description
Viruse Fabric is a conceptual-computational prototype exploring how constraint
geometry can shape compatible paths and produce apparent intentionality under
observer projection.

The project has internal validation artifacts and an integrated manuscript draft
for cautious technical review. It also includes a citation placeholder plan for
future literature mapping.

It remains a research prototype with internal validation.

## Public Communication Guidance
The public version should make the project understandable without making it
larger than the evidence allows.

Use this kind of language:

Viruse Fabric is an abstract prototype for studying how constraints can organize
possible paths and make some outcomes appear purposeful to an observer.

Avoid this kind of language:

Viruse Fabric proves a new universal law of causality.

The first sentence is safe because it describes a conceptual model and keeps the
status limited. The second sentence is unsafe because it turns a prototype into
a settled theory.

The preview should repeat the central boundary in plain language:

- The project is not externally validated.
- The manuscript is not submission-ready.
- The package is not a final paper.
- The model is not operational guidance.
- The model is not biological guidance.
- The model is not clinical guidance.
- The model is not laboratory guidance.
- The validation is internal validation only.
- The project does not provide external validation.
- The project does not establish empirical adequacy.
- The project does not support biological intervention.
- The project does not support clinical intervention.
- The project does not support laboratory use.
- The project does not support operational use.
- Citation placeholders are not citations.

This repetition is not decorative. It prevents a public reader from confusing a
technical preview with a completed theory. Apparently we do need to keep saying
this, because public-facing text has the survival instinct of a moth near a
lamp.

A safe public version should prefer modest verbs: explores, models, separates,
tests, audits, and prepares. It should avoid inflated verbs: proves, establishes,
solves, validates, predicts, or replaces. The difference is not cosmetic; it is
the boundary between a useful preview and an overconfident brochure wearing a lab
coat.

## Suggested Public Abstract
Viruse Fabric explores a constraint-geometric view of causality. Rather than
treating causality only as a sequence of event-to-event links, the project models
how constraints, possible paths, constructive attractors, and observer projection
can interact to produce apparent intentionality.

The current prototype includes internal validation through stress tests,
ablation, sensitivity analysis, baseline comparison, projection perturbation, and
manuscript-level audits. These artifacts support cautious technical review, but
do not establish external validation or submission readiness.

The project is intended as a public technical preview of an abstract framework,
not as biological, clinical, laboratory, or operational guidance.

## Review Checklist
Before any public use, confirm:

- The status says `research prototype with internal validation`.
- The text says not externally validated.
- The text says not submission-ready.
- The text does not claim proof.
- The text does not claim real biological prediction.
- The text does not contain fake citations.
- The text separates internal validation from external literature.
- The text keeps limitations visible.

## Next Steps
The recommended next steps are:

1. Run a public-preview quality audit.
2. Convert the preview into a shorter public-safe one-page version.
3. Perform real literature search for the v3.9 citation families.
4. Add verified citations only after source review.
5. Re-run citation and overclaim audits after citations are added.
6. Keep all public language inside the internal-validation boundary.

## Final Boundary Statement
This package supports a public technical preview only.

It does not certify external validation, empirical adequacy, biological
applicability, clinical relevance, laboratory relevance, operational usefulness,
or submission readiness.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> PublicPreviewResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_source_artifacts()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    section_count = count_sections(report)
    word_count = count_words(report)
    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    public_section_count = count_present_terms(report, PUBLIC_SECTIONS)
    limitation_count = report.lower().count("not ") + report.lower().count("does not")
    next_step_count = len(re.findall(r"^\d+\.", report, flags=re.MULTILINE))

    errors: list[str] = []
    warnings: list[str] = []

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if section_count < 14:
        errors.append(f"Section count too low: {section_count}")

    if word_count < 1500:
        errors.append(f"Word count too low for public technical preview: {word_count}")

    if boundary_count < 8:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if public_section_count < 12:
        errors.append(f"Public section coverage too low: {public_section_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if limitation_count < 12:
        errors.append(f"Limitation language count too low: {limitation_count}")

    if next_step_count < 6:
        errors.append(f"Next-step count too low: {next_step_count}")

    if word_count < 1800:
        warnings.append("Preview is concise; expand only if public context requires more explanation.")

    if boundary_count < 10:
        warnings.append("Boundary coverage is acceptable but should remain visible in any public rewrite.")

    passed = not errors

    interpretation = (
        "The v4.0 public technical preview package summarizes Viruse Fabric for "
        "cautious public-facing technical review while preserving the project's "
        "internal-validation boundary and avoiding fake citations or overclaiming."
    )

    return PublicPreviewResult(
        title="Public Technical Preview Package v4.0",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        section_count=section_count,
        word_count=word_count,
        boundary_phrase_count=boundary_count,
        public_section_count=public_section_count,
        overclaim_count=len(overclaims),
        fake_citation_count=len(fake_citations),
        limitation_count=limitation_count,
        next_step_count=next_step_count,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("Public Technical Preview Package v4.0")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Section count: {result.section_count}")
    print(f"Word count: {result.word_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Public section count: {result.public_section_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Limitation language count: {result.limitation_count}")
    print(f"Next-step count: {result.next_step_count}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Passed: {result.passed}")
    print(f"Report exists: {result.output_path.exists()}")
    print(f"Report size: {result.output_path.stat().st_size if result.output_path.exists() else 0}")
    print(f"Interpretation: {result.interpretation}")

    if result.errors:
        print("Errors:")
        for error in result.errors:
            print(f"- {error}")

    if result.warnings:
        print("Warnings:")
        for warning in result.warnings:
            print(f"- {warning}")

    if not result.passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
