"""Citation placeholder and literature mapping plan for Viruse Fabric v3.9.

This module creates a citation-safe planning artifact for the integrated
manuscript. It does not invent citations, references, authors, dates, DOIs,
arXiv identifiers, or bibliography entries.

The goal is to map claims and manuscript sections to literature families and
future search queries, while preserving the project's cautious status:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parents[2]

SOURCE_MANUSCRIPT_PATH = PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md"
SOURCE_AUDIT_PATH = PROJECT_ROOT / "outputs" / "integrated_manuscript_quality_audit_v3_8.md"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md"


LITERATURE_FAMILIES = [
    {
        "name": "Linear causal-chain models",
        "role": "Position Viruse Fabric against event-chain explanations that treat causality mainly as ordered links.",
        "citation_need": "Needed for the related-work contrast between causal chains and constraint geometry.",
        "query_templates": [
            "linear causal chain models causality explanation",
            "event chain causality model philosophy of science",
            "causal sequence explanation limitations",
        ],
        "manuscript_targets": [
            "Related Work and Positioning",
            "Core Thesis",
            "Why chain causality is insufficient",
        ],
        "boundary_note": "Use only for conceptual positioning, not as proof that Viruse Fabric replaces existing causal theories.",
    },
    {
        "name": "Network causality",
        "role": "Map adjacent approaches where causal relations are modeled as networks rather than single chains.",
        "citation_need": "Needed to clarify the difference between network connectivity and constraint geometry.",
        "query_templates": [
            "network causality causal graphs complex systems",
            "causal network explanation directed graph model",
            "causal graph limitations complex systems",
        ],
        "manuscript_targets": [
            "Related Work and Positioning",
            "Constraint geometry versus causal network",
            "Formal notation scaffold",
        ],
        "boundary_note": "Do not claim network models are wrong; only specify the different explanatory focus.",
    },
    {
        "name": "Dynamical systems and attractors",
        "role": "Support positioning around attractors, stability, trajectories, and path-like behavior in abstract systems.",
        "citation_need": "Needed for the constructive-attractor terminology and for explaining why apparent direction can emerge from system structure.",
        "query_templates": [
            "dynamical systems attractors stability trajectories",
            "attractor dynamics complex systems explanation",
            "trajectory stability basin attractor model",
        ],
        "manuscript_targets": [
            "Constructive Attractor",
            "Formal notation",
            "Validation mapping",
        ],
        "boundary_note": "Use as conceptual adjacency. Do not imply the prototype is a full dynamical-system theory.",
    },
    {
        "name": "Constraint-based explanation",
        "role": "Anchor the central idea that constraints shape the space of possible paths.",
        "citation_need": "Needed for the manuscript's strongest conceptual claim: causality as geometry of constraints.",
        "query_templates": [
            "constraint based explanation causality",
            "constraints shape possible trajectories model",
            "constraint satisfaction explanation complex systems",
        ],
        "manuscript_targets": [
            "Constraint definition",
            "Constraint geometry",
            "Central thesis",
        ],
        "boundary_note": "Use to position the project, not to claim external validation.",
    },
    {
        "name": "Observer-dependent interpretation",
        "role": "Support the distinction between intrinsic structure and observer projection.",
        "citation_need": "Needed for false intentionality, projection correction, and observer-dependent interpretation.",
        "query_templates": [
            "observer dependent interpretation model perception causality",
            "observer projection pattern interpretation purpose",
            "agency attribution observer bias complex systems",
        ],
        "manuscript_targets": [
            "Observer Projection",
            "Projection Perturbation",
            "False intentionality",
        ],
        "boundary_note": "Keep this tied to interpretation and attribution, not biological intention.",
    },
    {
        "name": "Teleology and apparent purpose",
        "role": "Position apparent intentionality against philosophical and scientific discussions of purpose-like behavior.",
        "citation_need": "Needed to avoid sounding like the manuscript claims literal intention in non-intentional systems.",
        "query_templates": [
            "apparent purpose teleology non intentional systems",
            "teleology apparent intentionality philosophy biology",
            "purpose like behavior without intention systems",
        ],
        "manuscript_targets": [
            "Apparent intentionality",
            "Disallowed claims",
            "Conclusion",
        ],
        "boundary_note": "Do not cite this as support for real purpose or agency. The claim remains apparent intentionality only.",
    },
    {
        "name": "Model validation and stress testing",
        "role": "Support the internal validation framing, ablation, perturbation, baseline comparison, and adversarial stress testing.",
        "citation_need": "Needed for explaining why internal validation is useful but insufficient for external validity.",
        "query_templates": [
            "model validation stress testing ablation perturbation baseline comparison",
            "internal validation computational model limitations",
            "adversarial stress testing model evaluation",
        ],
        "manuscript_targets": [
            "Validation protocol",
            "Validation synthesis",
            "Integrated validation table",
        ],
        "boundary_note": "Use this family to strengthen caution: internal validation is not external validation.",
    },
    {
        "name": "Scientific model boundaries and epistemic caution",
        "role": "Support the manuscript's discipline around scope, limitations, and claim control.",
        "citation_need": "Needed for limitation language and for preventing premature submission or inflated claims.",
        "query_templates": [
            "scientific model limitations scope conditions validation",
            "epistemic caution modeling claims limitations",
            "conceptual model validation boundary conditions",
        ],
        "manuscript_targets": [
            "Limitations",
            "Audit status",
            "Research boundary",
        ],
        "boundary_note": "This family protects the manuscript from overclaiming rather than expanding claims.",
    },
]


CITATION_SLOT_PLAN = [
    {
        "slot_id": "CITE_CHAIN_CAUSALITY",
        "claim_type": "background contrast",
        "claim_text": "Some causal explanations are organized as ordered chains of events.",
        "needs_real_citation": True,
        "target_family": "Linear causal-chain models",
        "citation_status": "placeholder only",
    },
    {
        "slot_id": "CITE_NETWORK_CAUSALITY",
        "claim_type": "background contrast",
        "claim_text": "Network approaches model causal relations through nodes, links, and connectivity patterns.",
        "needs_real_citation": True,
        "target_family": "Network causality",
        "citation_status": "placeholder only",
    },
    {
        "slot_id": "CITE_ATTRACTOR_DYNAMICS",
        "claim_type": "conceptual adjacency",
        "claim_text": "Attractor language is adjacent to work on stability, trajectories, and convergence in abstract systems.",
        "needs_real_citation": True,
        "target_family": "Dynamical systems and attractors",
        "citation_status": "placeholder only",
    },
    {
        "slot_id": "CITE_CONSTRAINT_EXPLANATION",
        "claim_type": "central positioning",
        "claim_text": "Constraint-based explanation provides an adjacent family for thinking about how possible paths are shaped.",
        "needs_real_citation": True,
        "target_family": "Constraint-based explanation",
        "citation_status": "placeholder only",
    },
    {
        "slot_id": "CITE_OBSERVER_PROJECTION",
        "claim_type": "interpretive framing",
        "claim_text": "Observers can attribute structure, purpose, or agency to patterns that do not intrinsically contain intention.",
        "needs_real_citation": True,
        "target_family": "Observer-dependent interpretation",
        "citation_status": "placeholder only",
    },
    {
        "slot_id": "CITE_APPARENT_TELEOLOGY",
        "claim_type": "terminology boundary",
        "claim_text": "Apparent purpose should be distinguished from literal intention or agency.",
        "needs_real_citation": True,
        "target_family": "Teleology and apparent purpose",
        "citation_status": "placeholder only",
    },
    {
        "slot_id": "CITE_MODEL_VALIDATION",
        "claim_type": "method framing",
        "claim_text": "Ablation, perturbation, baseline comparison, and stress testing can support internal model evaluation.",
        "needs_real_citation": True,
        "target_family": "Model validation and stress testing",
        "citation_status": "placeholder only",
    },
    {
        "slot_id": "CITE_MODEL_LIMITATIONS",
        "claim_type": "scope boundary",
        "claim_text": "Internal validation does not establish external validity or empirical adequacy.",
        "needs_real_citation": True,
        "target_family": "Scientific model boundaries and epistemic caution",
        "citation_status": "placeholder only",
    },
]


INTERNAL_ONLY_CLAIMS = [
    {
        "claim": "Experiment 38 passed with zero overclaim findings.",
        "source": "outputs/integrated_manuscript_quality_audit_v3_8.md",
        "external_citation_needed": False,
    },
    {
        "claim": "The v3.7 manuscript contains formal notation, related-work positioning, validation mapping, and research boundaries.",
        "source": "outputs/integrated_manuscript_draft_v3_7.md",
        "external_citation_needed": False,
    },
    {
        "claim": "The project status is research prototype with internal validation.",
        "source": "internal milestone synthesis",
        "external_citation_needed": False,
    },
    {
        "claim": "The audit did not detect fake citation patterns or submission-ready claims.",
        "source": "outputs/integrated_manuscript_quality_audit_v3_8.md",
        "external_citation_needed": False,
    },
]


PROHIBITED_CITATION_BEHAVIORS = [
    "Do not invent author names.",
    "Do not invent publication dates.",
    "Do not invent journal names.",
    "Do not invent DOI strings.",
    "Do not invent arXiv identifiers.",
    "Do not create numbered bibliography entries before real source lookup.",
    "Do not imply external validation from internal experiments.",
    "Do not cite adjacent literature as proof of Viruse Fabric.",
]


READINESS_BOUNDARIES = [
    "The manuscript is not submission-ready.",
    "The plan is a citation map, not a bibliography.",
    "Real citations require later source search and source verification.",
    "The project remains a research prototype with internal validation.",
    "No biological, clinical, laboratory, or operational claim is supported.",
    "No citation slot should be converted into a reference without source verification.",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class CitationPlanResult:
    title: str
    output_path: Path
    source_manuscript_exists: bool
    source_audit_exists: bool
    literature_family_count: int
    citation_slot_count: int
    query_count: int
    internal_only_claim_count: int
    prohibited_behavior_count: int
    readiness_boundary_count: int
    fake_citation_count: int
    word_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    interpretation: str


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w\-']+\b", text, flags=re.UNICODE))


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


def total_query_count() -> int:
    return sum(len(family["query_templates"]) for family in LITERATURE_FAMILIES)


def render_family_section() -> str:
    sections: list[str] = []

    for family in LITERATURE_FAMILIES:
        query_lines = "\n".join(f"- `{query}`" for query in family["query_templates"])
        target_lines = "\n".join(f"- {target}" for target in family["manuscript_targets"])

        sections.append(
            f"""### {family["name"]}

Role:
{family["role"]}

Citation need:
{family["citation_need"]}

Future search queries:
{query_lines}

Manuscript targets:
{target_lines}

Boundary note:
{family["boundary_note"]}
"""
        )

    return "\n".join(sections)


def render_slot_section() -> str:
    rows = [
        "| Slot ID | Claim type | Target family | Citation status |",
        "|---|---:|---|---|",
    ]

    for slot in CITATION_SLOT_PLAN:
        rows.append(
            f"| `{slot['slot_id']}` | {slot['claim_type']} | {slot['target_family']} | {slot['citation_status']} |"
        )

    details: list[str] = []

    for slot in CITATION_SLOT_PLAN:
        details.append(
            f"""### {slot["slot_id"]}

Claim text:
{slot["claim_text"]}

Needs real citation:
{slot["needs_real_citation"]}

Target family:
{slot["target_family"]}

Citation status:
{slot["citation_status"]}
"""
        )

    return "\n".join(rows) + "\n\n" + "\n".join(details)


def render_internal_claims() -> str:
    lines = []

    for item in INTERNAL_ONLY_CLAIMS:
        lines.append(
            f"""### Internal claim

Claim:
{item["claim"]}

Internal source:
`{item["source"]}`

External citation needed:
{item["external_citation_needed"]}
"""
        )

    return "\n".join(lines)


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def render_report() -> str:
    family_section = render_family_section()
    slot_section = render_slot_section()
    internal_claims = render_internal_claims()

    query_count = total_query_count()

    return f"""# Citation Placeholder Plan v3.9

## Question
Can Viruse Fabric prepare a citation-safe literature mapping plan for the integrated manuscript without inventing citations?

## Source Artifacts
- Integrated manuscript draft: `outputs/integrated_manuscript_draft_v3_7.md`
- Integrated manuscript quality audit: `outputs/integrated_manuscript_quality_audit_v3_8.md`

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is a planning document. It is not a bibliography, not a literature review, and not a submission-ready reference section.

## Summary Metrics
- Literature family count: {len(LITERATURE_FAMILIES)}
- Citation slot count: {len(CITATION_SLOT_PLAN)}
- Future query count: {query_count}
- Internal-only claim count: {len(INTERNAL_ONLY_CLAIMS)}
- Prohibited citation behavior count: {len(PROHIBITED_CITATION_BEHAVIORS)}
- Readiness boundary count: {len(READINESS_BOUNDARIES)}

## Literature Families
{family_section}

## Citation Slot Plan
The following slots mark where real citations may later be inserted after source lookup and verification.

No slot is a citation. No slot is a bibliographic reference. No slot should be treated as evidence.

{slot_section}

## Internal-Only Claims
These claims are supported by project artifacts and do not need external citation unless they are rewritten as broader scientific claims.

{internal_claims}

## Prohibited Citation Behaviors
{bullet_list(PROHIBITED_CITATION_BEHAVIORS)}

## Readiness Boundaries
{bullet_list(READINESS_BOUNDARIES)}

## Search Workflow for Later Versions
1. Search one literature family at a time.
2. Prefer peer-reviewed papers, academic books, or official documentation depending on the family.
3. Record exact source metadata only after source verification.
4. Add citations only where a source directly supports the manuscript claim.
5. Keep internal validation claims separate from external literature claims.
6. Re-run manuscript audit after adding any citations.
7. Keep citation-needed placeholders visible until real sources are verified.

## Claim Classification Rules
Use this classification before adding references:

- Internal artifact claim: cite or reference project artifact only.
- Background literature claim: requires real external source lookup.
- Conceptual adjacency claim: requires cautious source support and careful wording.
- Validation claim: must stay internal unless externally replicated.
- Biological or operational claim: prohibited in this project stage.
- Submission-readiness claim: prohibited in this project stage.

## Interpretation
The v3.9 plan prepares the manuscript for real literature mapping without fabricating citations.

It separates citation-needed background claims from internal project claims, assigns each citation need to a literature family, and preserves the project's cautious research boundary.

The manuscript remains not submission-ready.
"""


def generate_report() -> CitationPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    fake_citation_lines = detect_fake_citations(report)
    word_count = count_words(report)

    source_manuscript_exists = SOURCE_MANUSCRIPT_PATH.exists()
    source_audit_exists = SOURCE_AUDIT_PATH.exists()

    errors: list[str] = []
    warnings: list[str] = []

    if not source_manuscript_exists:
        errors.append(f"Missing source manuscript: {SOURCE_MANUSCRIPT_PATH.relative_to(PROJECT_ROOT)}")

    if not source_audit_exists:
        errors.append(f"Missing source audit: {SOURCE_AUDIT_PATH.relative_to(PROJECT_ROOT)}")

    if len(LITERATURE_FAMILIES) < 8:
        errors.append(f"Literature family count too low: {len(LITERATURE_FAMILIES)}")

    if len(CITATION_SLOT_PLAN) < 8:
        errors.append(f"Citation slot count too low: {len(CITATION_SLOT_PLAN)}")

    if total_query_count() < 24:
        errors.append(f"Future query count too low: {total_query_count()}")

    if len(INTERNAL_ONLY_CLAIMS) < 4:
        errors.append(f"Internal-only claim count too low: {len(INTERNAL_ONLY_CLAIMS)}")

    if len(PROHIBITED_CITATION_BEHAVIORS) < 8:
        errors.append(f"Prohibited citation behavior count too low: {len(PROHIBITED_CITATION_BEHAVIORS)}")

    if len(READINESS_BOUNDARIES) < 6:
        errors.append(f"Readiness boundary count too low: {len(READINESS_BOUNDARIES)}")

    if fake_citation_lines:
        errors.append(f"Fake citation-like pattern detected: {len(fake_citation_lines)}")

    if word_count < 1700:
        warnings.append(f"Report is concise for a literature mapping plan: {word_count} words")

    if "submission-ready" not in report:
        errors.append("Missing submission-readiness boundary language.")

    if "research prototype with internal validation" not in report:
        errors.append("Missing project status boundary language.")

    passed = not errors

    interpretation = (
        "The citation placeholder plan maps the integrated manuscript to "
        "literature families and citation slots without inventing citations. "
        "It keeps internal artifact claims separate from external literature "
        "claims and preserves the project's non-submission-ready status."
    )

    return CitationPlanResult(
        title="Citation Placeholder Plan v3.9",
        output_path=OUTPUT_PATH,
        source_manuscript_exists=source_manuscript_exists,
        source_audit_exists=source_audit_exists,
        literature_family_count=len(LITERATURE_FAMILIES),
        citation_slot_count=len(CITATION_SLOT_PLAN),
        query_count=total_query_count(),
        internal_only_claim_count=len(INTERNAL_ONLY_CLAIMS),
        prohibited_behavior_count=len(PROHIBITED_CITATION_BEHAVIORS),
        readiness_boundary_count=len(READINESS_BOUNDARIES),
        fake_citation_count=len(fake_citation_lines),
        word_count=word_count,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("Citation Placeholder Plan v3.9")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source manuscript exists: {result.source_manuscript_exists}")
    print(f"Source audit exists: {result.source_audit_exists}")
    print(f"Literature family count: {result.literature_family_count}")
    print(f"Citation slot count: {result.citation_slot_count}")
    print(f"Future query count: {result.query_count}")
    print(f"Internal-only claim count: {result.internal_only_claim_count}")
    print(f"Prohibited citation behavior count: {result.prohibited_behavior_count}")
    print(f"Readiness boundary count: {result.readiness_boundary_count}")
    print(f"Fake citation-like pattern count: {result.fake_citation_count}")
    print(f"Word count: {result.word_count}")
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
