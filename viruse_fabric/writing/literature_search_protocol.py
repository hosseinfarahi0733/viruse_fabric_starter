"""Literature search protocol for Viruse Fabric v4.7.

This module generates a protocol for future real literature search.

It does not add citations.
It does not claim that sources have been found.
It does not replace real database search, external review, or validation.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "literature_search_protocol_v4_7.md"

SOURCE_ARTIFACTS = [
    PROJECT_ROOT / "outputs" / "citation_placeholder_plan_v3_9.md",
    PROJECT_ROOT / "outputs" / "integrated_manuscript_draft_v3_7.md",
    PROJECT_ROOT / "outputs" / "integrated_manuscript_quality_audit_v3_8.md",
    PROJECT_ROOT / "outputs" / "public_release_readiness_audit_v4_6.md",
]


SEARCH_VENUES = [
    "Google Scholar",
    "Semantic Scholar",
    "arXiv",
    "PubMed",
    "PhilPapers",
    "Crossref",
    "publisher and journal search pages",
    "library-indexed databases when available",
]


LITERATURE_FAMILIES = [
    {
        "family": "constraint-based explanation",
        "purpose": "position constraint geometry against existing constraint-centered explanatory approaches",
        "queries": [
            '"constraint-based explanation" causality',
            '"constraint geometry" theory',
            '"constraints" "causal explanation"',
            '"constraint" "state space" "explanation"',
        ],
    },
    {
        "family": "causal models and structural causal modeling",
        "purpose": "compare the project with graph-based and intervention-centered causality frameworks",
        "queries": [
            '"structural causal model" "causal graph"',
            '"causal model" "intervention"',
            '"causal inference" "structural equations"',
            '"counterfactual causality" "graph"',
        ],
    },
    {
        "family": "dynamical systems and attractors",
        "purpose": "ground attractor language without implying biological or physical validation",
        "queries": [
            '"dynamical systems" attractor "state space"',
            '"attractor landscape" "complex systems"',
            '"basin of attraction" "system dynamics"',
            '"path dependence" "attractor"',
        ],
    },
    {
        "family": "complex systems and emergence",
        "purpose": "position apparent purpose as an emergent observer-facing pattern",
        "queries": [
            '"emergence" "complex systems" "constraints"',
            '"self-organization" "constraints" "complex systems"',
            '"emergent behavior" "observer"',
            '"teleonomy" "emergence"',
        ],
    },
    {
        "family": "teleology, teleonomy, and apparent purpose",
        "purpose": "separate apparent purpose from literal intention or agency claims",
        "queries": [
            '"teleology" "apparent purpose"',
            '"teleonomy" "purpose"',
            '"goal-directed behavior" "without intention"',
            '"purpose" "observer" "complex systems"',
        ],
    },
    {
        "family": "affordances, paths, and possibility spaces",
        "purpose": "compare path compatibility with existing language around affordances and possible actions",
        "queries": [
            '"affordance" "possibility space"',
            '"action possibilities" "constraints"',
            '"path compatibility" "constraints"',
            '"state space" "possible paths"',
        ],
    },
    {
        "family": "observer effects and projection",
        "purpose": "ground observer projection without importing unearned claims from physics or cognition",
        "queries": [
            '"observer" "projection" "model"',
            '"observer-dependent" "explanation"',
            '"perspective" "complex systems" "observer"',
            '"model observer" "interpretation"',
        ],
    },
    {
        "family": "formal ontology and process philosophy",
        "purpose": "map philosophical framing around process, relation, constraint, and structure",
        "queries": [
            '"process philosophy" "relations"',
            '"formal ontology" "constraints"',
            '"relations" "causality" "process"',
            '"structure" "causality" "philosophy"',
        ],
    },
]


CLAIM_CATEGORIES = [
    {
        "claim": "Causality is represented as a geometry of constraints rather than a simple chain.",
        "needs_literature": "causal models, constraint-based explanation, process and relational accounts",
        "status": "requires literature positioning",
    },
    {
        "claim": "Apparent purpose can emerge from constraint geometry, attractor concentration, path compatibility, and observer projection.",
        "needs_literature": "emergence, teleonomy, attractors, observer-dependent explanation",
        "status": "requires literature positioning",
    },
    {
        "claim": "The project currently provides internal validation only.",
        "needs_literature": "methodological boundary language, validation standards if used in a future paper",
        "status": "internal project status",
    },
    {
        "claim": "The public release path is ready for cautious public orientation, not submission.",
        "needs_literature": "does not need scientific citation; it is a release-governance statement",
        "status": "internal release status",
    },
    {
        "claim": "Citation placeholders are not citations.",
        "needs_literature": "does not need citation; it is a citation-integrity rule",
        "status": "internal protocol rule",
    },
    {
        "claim": "The framework should not be described as externally validated.",
        "needs_literature": "does not need citation unless discussing validation standards",
        "status": "boundary rule",
    },
    {
        "claim": "The model should not be used as biological, clinical, laboratory, or operational guidance.",
        "needs_literature": "does not need domain citation because it is a safety boundary",
        "status": "boundary rule",
    },
    {
        "claim": "Future manuscript revision must distinguish analogy, formalism, internal result, and externally supported claim.",
        "needs_literature": "writing and methodology standards may be useful later",
        "status": "manuscript-development rule",
    },
]


INCLUSION_CRITERIA = [
    "Source directly addresses one of the listed literature families.",
    "Source helps position a core claim without inflating it.",
    "Source is primary literature, a respected review, or a canonical scholarly reference.",
    "Source can be checked directly rather than inherited through another citation list.",
    "Source clarifies terminology used in the project.",
    "Source helps distinguish internal validation from external validation.",
    "Source helps compare Viruse Fabric with existing frameworks.",
    "Source can be summarized without misrepresenting its scope.",
]


EXCLUSION_CRITERIA = [
    "Source is only loosely related to the claim being mapped.",
    "Source is used only because its title sounds convenient.",
    "Source cannot be accessed or verified.",
    "Source would make the project sound more validated than it is.",
    "Source is a popular article used where scholarly literature is required.",
    "Source is cited to decorate a sentence rather than support it.",
    "Source introduces biological, clinical, laboratory, or operational implications not present in the project.",
    "Source is used before its argument is actually read.",
]


SEARCH_STEPS = [
    "Start from the citation placeholder plan.",
    "Search each literature family independently.",
    "Record search venue, query string, date searched, and result notes.",
    "Separate primary sources, review sources, and background sources.",
    "Map each candidate source to a claim category.",
    "Reject sources that only provide decorative authority.",
    "Write a short neutral summary for every retained source.",
    "Mark whether each source supports, contrasts with, or merely contextualizes the project.",
    "Do not add a citation to the manuscript until the source has been read and mapped.",
    "Re-audit the manuscript after citations are integrated.",
]


BOUNDARY_PHRASES = [
    "research prototype with internal validation",
    "not externally validated",
    "not submission-ready",
    "not a final paper",
    "not biological guidance",
    "not clinical guidance",
    "not laboratory guidance",
    "not operational guidance",
    "citation placeholders are not citations",
    "no citation is added by this protocol",
]


PROHIBITED_BEHAVIORS = [
    "Do not invent citations.",
    "Do not treat a search query as a source.",
    "Do not treat a citation placeholder as a real citation.",
    "Do not cite a source before reading the relevant part.",
    "Do not use citations as decoration.",
    "Do not use sources to imply external validation unless such validation exists.",
    "Do not use biological, clinical, laboratory, or operational sources to imply guidance.",
    "Do not call the manuscript submission-ready because a protocol exists.",
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


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "no citation",
    "no claim",
    "without",
    "cannot",
    "should not",
    "boundary",
    "boundary phrases",
    "prohibited",
    "excluded",
    "exclusion",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "unless such validation exists",
    "citation placeholders are not citations",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "exclusion criteria",
    "final boundary statement",
]


FAKE_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
    r"\(20\d{2}\)",
]


@dataclass(frozen=True)
class LiteratureSearchProtocolResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    search_venue_count: int
    literature_family_count: int
    future_query_count: int
    claim_category_count: int
    inclusion_criteria_count: int
    exclusion_criteria_count: int
    search_step_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    overclaim_count: int
    fake_citation_count: int
    word_count: int
    errors: list[str]
    warnings: list[str]
    passed: bool
    interpretation: str


def relative(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w\-']+\b", text, flags=re.UNICODE))


def count_present_terms(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term.lower() in lowered)


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def source_table() -> str:
    rows = [
        "| Source artifact | Exists |",
        "|---|---|",
    ]

    for path in SOURCE_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")

    return "\n".join(rows)


def literature_family_sections() -> str:
    sections: list[str] = []

    for item in LITERATURE_FAMILIES:
        sections.append(
            f"""### {item["family"]}

Purpose:
{item["purpose"]}

Future queries:
{bullet_list(item["queries"])}
"""
        )

    return "\n".join(sections)


def claim_category_table() -> str:
    rows = [
        "| Claim category | Literature need | Status |",
        "|---|---|---|",
    ]

    for item in CLAIM_CATEGORIES:
        rows.append(f"| {item['claim']} | {item['needs_literature']} | {item['status']} |")

    return "\n".join(rows)


def missing_sources() -> list[Path]:
    return [path for path in SOURCE_ARTIFACTS if not path.exists()]


def line_is_safe_context(line: str) -> bool:
    lowered = line.lower()
    return any(cue in lowered for cue in SAFE_LINE_CUES)


def detect_overclaims(text: str) -> list[str]:
    findings: list[str] = []
    current_section = ""

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        lowered = stripped.lower()

        if lowered.startswith("## "):
            current_section = lowered.removeprefix("## ").strip()

        if current_section in SAFE_SECTION_HEADINGS:
            continue

        if line_is_safe_context(lowered):
            continue

        for pattern in OVERCLAIM_PATTERNS:
            if re.search(pattern, lowered, flags=re.IGNORECASE):
                findings.append(stripped)
                break

    return findings


def detect_fake_citations(text: str) -> list[str]:
    findings: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        lowered = stripped.lower()

        if "citation placeholder" in lowered or "fake citation" in lowered:
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def render_report() -> str:
    return f"""# Literature Search Protocol v4.7

## Question
Can Viruse Fabric define a real literature-search protocol before adding citations, while avoiding fake citations, overclaiming, and premature submission language?

## Status
Current project status remains:

`research prototype with internal validation`

This protocol is not externally validated, not submission-ready, and not a final paper.

No citation is added by this protocol. Citation placeholders are not citations.

## Source Artifacts
The protocol is based on existing internal artifacts, especially the citation placeholder plan and manuscript audit.

{source_table()}

## Search Venues
Future searches should use these venues when available and appropriate.

{bullet_list(SEARCH_VENUES)}

## Literature Families
Each family must be searched separately. The purpose is not to force the project into existing literature, but to find where it belongs, where it differs, and where it must be more careful.

{literature_family_sections()}

## Claim-to-Literature Map
Each project claim must be classified before citation insertion.

{claim_category_table()}

## Inclusion Criteria
Candidate sources may be retained only when they satisfy the protocol.

{bullet_list(INCLUSION_CRITERIA)}

## Exclusion Criteria
Candidate sources should be rejected when they create noise, inflation, or citation theater.

{bullet_list(EXCLUSION_CRITERIA)}

## Search Procedure
The future literature search should proceed in the following order.

{bullet_list(SEARCH_STEPS)}

## Evidence Record Template
Every retained source should be recorded later with these fields:

- Source title
- Authors
- Venue
- Year
- Search venue used
- Query string used
- Literature family
- Claim category
- Source role: support, contrast, context, method, or terminology
- Relevant passage summary
- Boundary note
- Decision: retain, defer, or reject

This template is intentionally empty in v4.7. Adding invented entries would be faster, and also useless, which has never stopped humanity before but will stop us here.

## Source Evaluation Notes
A retained source should earn its place in the project.

The source should not merely contain a familiar word such as constraint, attractor, emergence, or causality. It must help explain, contrast, constrain, or correct a specific part of the Viruse Fabric framework. A source that only sounds related should be rejected or deferred.

Every source should be mapped to a claim before citation insertion. If the source supports terminology but not the claim, it should be labeled as terminology. If it gives historical context but not direct support, it should be labeled as context. If it challenges the project, it should be preserved as contrast rather than ignored. Convenient disagreement is still disagreement, even when humans would rather bury it under nicer prose.

## Claim Discipline
The literature search should protect the project from claim drift.

A citation may justify vocabulary, background, comparison, or contrast. It should not magically turn internal validation into external validation. It should not turn a conceptual model into a biological, clinical, laboratory, or operational tool. It should not make the manuscript submission-ready by decorative proximity.

The correct question for each candidate source is not "Can we cite this?" but "What exact sentence does this source responsibly support?" If that sentence cannot be named, the source should not enter the manuscript yet.

## Search Log Requirements
Every future search pass should preserve enough information to be reproducible.

At minimum, the search log should record the venue, exact query, search date, filters used, first-screen relevance notes, candidate source decisions, and reasons for rejection. This is tedious because reality often is. Still, it prevents the later disaster where a citation appears in the manuscript and nobody remembers why it was added, which is how scholarly archaeology becomes office work with worse lighting.

## Boundary Phrases
The protocol preserves the following boundary phrases:

{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
The following behaviors remain prohibited:

{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Milestone
The next logical milestone is:

`v4.8 — Literature Family Evidence Matrix`

That milestone should create an empty evidence matrix structure for real sources. It should not invent sources.

## Final Boundary Statement
This protocol prepares real literature search.

It does not provide citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> LiteratureSearchProtocolResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    future_query_count = sum(len(item["queries"]) for item in LITERATURE_FAMILIES)
    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 4:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if len(SEARCH_VENUES) < 7:
        errors.append(f"Search venue count too low: {len(SEARCH_VENUES)}")

    if len(LITERATURE_FAMILIES) < 8:
        errors.append(f"Literature family count too low: {len(LITERATURE_FAMILIES)}")

    if future_query_count < 32:
        errors.append(f"Future query count too low: {future_query_count}")

    if len(CLAIM_CATEGORIES) < 8:
        errors.append(f"Claim category count too low: {len(CLAIM_CATEGORIES)}")

    if len(INCLUSION_CRITERIA) < 8:
        errors.append(f"Inclusion criteria count too low: {len(INCLUSION_CRITERIA)}")

    if len(EXCLUSION_CRITERIA) < 8:
        errors.append(f"Exclusion criteria count too low: {len(EXCLUSION_CRITERIA)}")

    if len(SEARCH_STEPS) < 10:
        errors.append(f"Search step count too low: {len(SEARCH_STEPS)}")

    if boundary_count < 9:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 8:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for literature search protocol: {word_count}")

    warnings.append("Protocol creates no citations; real source search must happen later.")
    warnings.append("Search venues and query strings must be reviewed before live use.")

    passed = not errors

    interpretation = (
        "The v4.7 protocol prepares real literature search by defining venues, "
        "literature families, future queries, claim categories, inclusion rules, "
        "exclusion rules, and citation-integrity boundaries without adding citations."
    )

    return LiteratureSearchProtocolResult(
        title="Literature Search Protocol v4.7",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        search_venue_count=len(SEARCH_VENUES),
        literature_family_count=len(LITERATURE_FAMILIES),
        future_query_count=future_query_count,
        claim_category_count=len(CLAIM_CATEGORIES),
        inclusion_criteria_count=len(INCLUSION_CRITERIA),
        exclusion_criteria_count=len(EXCLUSION_CRITERIA),
        search_step_count=len(SEARCH_STEPS),
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        overclaim_count=len(overclaims),
        fake_citation_count=len(fake_citations),
        word_count=word_count,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("Literature Search Protocol v4.7")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Search venue count: {result.search_venue_count}")
    print(f"Literature family count: {result.literature_family_count}")
    print(f"Future query count: {result.future_query_count}")
    print(f"Claim category count: {result.claim_category_count}")
    print(f"Inclusion criteria count: {result.inclusion_criteria_count}")
    print(f"Exclusion criteria count: {result.exclusion_criteria_count}")
    print(f"Search step count: {result.search_step_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Overclaim count: {result.overclaim_count}")
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
