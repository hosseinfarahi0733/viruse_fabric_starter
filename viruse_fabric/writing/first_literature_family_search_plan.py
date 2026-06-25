"""First literature family search plan for Viruse Fabric v5.4.

This module generates a plan for the first future literature family search.

It connects:
- the v4.7 literature search protocol,
- the v4.8 literature family evidence matrix,
- the v4.9 claim-to-citation readiness map,
- the v5.1 literature search log template,
- the v5.2 empty literature search log,
- the v5.3 empty search log audit.

It does not run searches.
It does not add sources.
It does not add citations.
It does not populate the evidence matrix.
It does not revise the manuscript.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_literature_family_search_plan_v5_4.md"

SOURCE_SEARCH_PROTOCOL = PROJECT_ROOT / "outputs" / "literature_search_protocol_v4_7.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"
SOURCE_SEARCH_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_EMPTY_SEARCH_LOG = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"
SOURCE_EMPTY_SEARCH_LOG_AUDIT = PROJECT_ROOT / "outputs" / "empty_search_log_audit_v5_3.md"

SOURCE_ARTIFACTS = [
    SOURCE_SEARCH_PROTOCOL,
    SOURCE_EVIDENCE_MATRIX,
    SOURCE_CLAIM_MAP,
    SOURCE_SEARCH_LOG_TEMPLATE,
    SOURCE_EMPTY_SEARCH_LOG,
    SOURCE_EMPTY_SEARCH_LOG_AUDIT,
]


SELECTED_LITERATURE_FAMILY = {
    "family_id": "LF-01",
    "family_name": "constraint-based causality and dynamical-systems framing",
    "reason": (
        "This family is selected first because it is closest to the central thesis "
        "that apparent purpose can emerge from constraint geometry, attractor "
        "concentration, path compatibility, and observer projection."
    ),
    "allowed_use": "future literature positioning only",
    "not_allowed_use": "external validation, submission readiness, or empirical proof",
}


PLANNED_SEARCH_VENUES = [
    "Google Scholar",
    "Semantic Scholar",
    "arXiv",
    "PhilPapers",
    "PubMed for terminology only when relevant",
    "Crossref metadata lookup after candidate identification",
    "publisher pages after candidate identification",
    "library catalog or institutional access after candidate identification",
]


PLANNED_QUERY_STRINGS = [
    {
        "query_id": "Q-01",
        "query": '"constraint" "causality" "dynamical systems"',
        "purpose": "find background literature connecting constraints and causal structure",
    },
    {
        "query_id": "Q-02",
        "query": '"constraint-based" "causality"',
        "purpose": "find direct uses of constraint-based causality language",
    },
    {
        "query_id": "Q-03",
        "query": '"attractor" "causality" "dynamical systems"',
        "purpose": "find literature connecting attractor structure and causal interpretation",
    },
    {
        "query_id": "Q-04",
        "query": '"emergence" "constraints" "dynamical systems"',
        "purpose": "find background for emergence under constraints",
    },
    {
        "query_id": "Q-05",
        "query": '"teleonomy" "constraints" "emergence"',
        "purpose": "find literature around apparent purpose and constraint-based explanation",
    },
    {
        "query_id": "Q-06",
        "query": '"observer" "projection" "causality"',
        "purpose": "find background for observer-dependent interpretation language",
    },
    {
        "query_id": "Q-07",
        "query": '"path dependence" "constraints" "causality"',
        "purpose": "find literature connecting path compatibility and causal structure",
    },
    {
        "query_id": "Q-08",
        "query": '"state space" "constraints" "emergence"',
        "purpose": "find sources for state-space and constraint terminology",
    },
    {
        "query_id": "Q-09",
        "query": '"causal geometry" "constraints"',
        "purpose": "test whether adjacent terminology already exists",
    },
    {
        "query_id": "Q-10",
        "query": '"constraint geometry" "causality"',
        "purpose": "test whether the project phrase has nearby prior usage",
    },
]


CLAIM_CATEGORIES_FOR_FIRST_SEARCH = [
    "literature-needed: causality is not merely chain-like in this framework",
    "literature-needed: constraints shape possible trajectories",
    "literature-needed: attractor structure can shape apparent directionality",
    "literature-needed: observer projection can affect interpretation of purpose",
    "boundary-rule: literature context is not external validation",
    "manuscript-development-rule: related work must position but not overclaim",
]


INCLUSION_CRITERIA = [
    "Source discusses causality, constraints, dynamical systems, emergence, teleonomy, or state-space framing.",
    "Source is relevant to conceptual positioning rather than decorative authority.",
    "Source provides terminology, background, comparison, contrast, method context, or boundary context.",
    "Source can be linked to at least one claim category from the v4.9 claim map.",
    "Source has enough accessible abstract, metadata, or passage context for screening.",
    "Source can be logged with venue, query string, candidate source identifier, and decision rationale.",
    "Source does not need to agree with Viruse Fabric to be useful as contrast.",
    "Source can be deferred if full reading is needed before decision.",
]


EXCLUSION_CRITERIA = [
    "Exclude sources that are only keyword matches with no conceptual relevance.",
    "Exclude sources that would encourage external-validation language.",
    "Exclude sources that imply biological, clinical, laboratory, or operational guidance for this project.",
    "Exclude sources with insufficient metadata for controlled logging.",
    "Exclude sources that cannot be linked to a claim category or literature family.",
    "Exclude sources used only to make the manuscript look more authoritative.",
    "Exclude sources whose role cannot be described as background, terminology, comparison, contrast, method context, or boundary context.",
    "Exclude sources that would require invented bibliographic details.",
]


SEARCH_RUN_FIELDS_TO_FILL_LATER = [
    "search_run_id",
    "search_date",
    "searcher",
    "literature_family",
    "claim_category",
    "search_venue",
    "query_string",
    "query_rationale",
    "inclusion_criteria_used",
    "exclusion_criteria_used",
    "raw_result_count",
    "screened_result_count",
    "candidate_source_count",
    "retained_source_count",
    "deferred_source_count",
    "rejected_source_count",
    "notes",
]


CANDIDATE_SCREENING_STEPS = [
    "Run exactly one planned query in one planned venue.",
    "Record the exact query string before screening results.",
    "Record raw result count if the venue provides it.",
    "Screen only visible metadata and accessible abstract-level information first.",
    "Create candidate source entries only for sources with clear relevance.",
    "Assign source role as pending until a source is read closely.",
    "Do not retain a source before review.",
    "Do not cite a source before source-role and claim-link audit.",
]


FIRST_SEARCH_RUN_GATES = [
    "The empty search log audit must already be closed.",
    "The selected literature family must be named before search.",
    "The exact query string must be recorded before screening.",
    "The search venue must be recorded.",
    "The claim category must be recorded.",
    "Raw and screened counts must be recorded when available.",
    "Candidate source count must remain zero until candidate entries are created.",
    "Retained source count must remain zero until candidate audit passes.",
    "Citation added count must remain zero.",
    "Evidence matrix populated count must remain zero.",
    "Manuscript revised count must remain zero.",
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
    "no search is run by this plan",
    "no source is added by this plan",
    "no citation is added by this plan",
    "the evidence matrix is not populated by this plan",
    "the manuscript is not revised by this plan",
]


PROHIBITED_BEHAVIORS = [
    "Do not run live searches in this milestone.",
    "Do not add real sources in this milestone.",
    "Do not add citations in this milestone.",
    "Do not invent authors, titles, venues, identifiers, or publication years.",
    "Do not populate the evidence matrix.",
    "Do not revise the manuscript.",
    "Do not treat planned queries as completed searches.",
    "Do not treat candidate planning as source evidence.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not add biological, clinical, laboratory, or operational guidance.",
]


NEXT_STEPS = [
    "Use this plan to create the first real search run artifact.",
    "Run only one controlled query first.",
    "Record the exact query string and venue.",
    "Record raw and screened result counts.",
    "Create candidate source entries only after screening.",
    "Audit candidate source entries before retention.",
    "Keep evidence matrix population as a later milestone.",
    "Keep manuscript revision as a later milestone.",
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
    r"\bsubmission-ready\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "no search",
    "no source",
    "no citation",
    "not allowed",
    "exclude",
    "future",
    "planned",
    "pending",
    "boundary",
    "prohibited",
    "criteria",
    "gate",
    "zero",
    "only",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citation placeholders are not citations",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "exclusion criteria",
    "first search run gates",
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
class FirstLiteratureFamilySearchPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    selected_family_count: int
    planned_venue_count: int
    planned_query_count: int
    claim_category_count: int
    inclusion_criteria_count: int
    exclusion_criteria_count: int
    search_run_field_count: int
    screening_step_count: int
    search_run_gate_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    search_run_count: int
    source_added_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
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


def missing_sources() -> list[Path]:
    return [path for path in SOURCE_ARTIFACTS if not path.exists()]


def render_source_table() -> str:
    rows = [
        "| Source artifact | Exists |",
        "|---|---|",
    ]
    for path in SOURCE_ARTIFACTS:
        rows.append(f"| `{relative(path)}` | {path.exists()} |")
    return "\n".join(rows)


def render_selected_family_table() -> str:
    return "\n".join(
        [
            "| Field | Value |",
            "|---|---|",
            f"| `family_id` | `{SELECTED_LITERATURE_FAMILY['family_id']}` |",
            f"| `family_name` | {SELECTED_LITERATURE_FAMILY['family_name']} |",
            f"| `reason` | {SELECTED_LITERATURE_FAMILY['reason']} |",
            f"| `allowed_use` | {SELECTED_LITERATURE_FAMILY['allowed_use']} |",
            f"| `not_allowed_use` | {SELECTED_LITERATURE_FAMILY['not_allowed_use']} |",
        ]
    )


def render_query_table() -> str:
    rows = [
        "| Query ID | Planned query string | Purpose |",
        "|---|---|---|",
    ]
    for item in PLANNED_QUERY_STRINGS:
        rows.append(f"| {item['query_id']} | `{item['query']}` | {item['purpose']} |")
    return "\n".join(rows)


def render_field_table(fields: list[str]) -> str:
    rows = [
        "| Field | Status for v5.4 |",
        "|---|---|",
    ]
    for field in fields:
        rows.append(f"| `{field}` | planned for future first search run |")
    return "\n".join(rows)


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
    return f"""# First Literature Family Search Plan v5.4

## Question
Can Viruse Fabric choose the first literature family and define a controlled first-search plan without running searches, adding sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This plan is not externally validated, not submission-ready, and not a final paper.

No search is run by this plan. No source is added by this plan. No citation is added by this plan. The evidence matrix is not populated by this plan. The manuscript is not revised by this plan. Citation placeholders are not citations.

## Source Artifacts
{render_source_table()}

## Selected Literature Family
{render_selected_family_table()}

## Planned Search Venues
{bullet_list(PLANNED_SEARCH_VENUES)}

## Planned Query Strings
{render_query_table()}

## Claim Categories for First Search
{bullet_list(CLAIM_CATEGORIES_FOR_FIRST_SEARCH)}

## Inclusion Criteria
{bullet_list(INCLUSION_CRITERIA)}

## Exclusion Criteria
{bullet_list(EXCLUSION_CRITERIA)}

## Search Run Fields to Fill Later
{render_field_table(SEARCH_RUN_FIELDS_TO_FILL_LATER)}

## Candidate Screening Steps
{bullet_list(CANDIDATE_SCREENING_STEPS)}

## First Search Run Gates
{bullet_list(FIRST_SEARCH_RUN_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Planning Logic
The first literature family is selected because it is closest to the core conceptual claim of Viruse Fabric.

The project should not begin with a broad literature sweep. A broad sweep would create too many candidate sources too quickly, and then someone would inevitably start treating search noise as scholarship. This plan intentionally starts narrow: one family, controlled venues, planned queries, explicit inclusion criteria, explicit exclusion criteria, and visible gates.

The selected family is meant to support future positioning, not future triumph. It may provide background terminology, comparison, contrast, or boundary context. It may also show that some project language needs to be changed. A useful source is not always a friendly source. Humanity would be calmer if it remembered this before turning every bibliography into a victory parade.

## Search Discipline
The future first search run should be small enough to audit.

The first actual search should use one planned query and one venue. It should record the exact query string before screening. It should record raw result count, screened result count, and candidate source count. Candidate sources should not become retained sources until review. Retained sources should not become citations until they are mapped to claims and audited.

This plan keeps the first search from becoming a messy pile of promising links. A pile of promising links is not evidence. It is just clutter with academic perfume.

## Output Counts
Search run count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This plan prepares the first future literature family search.

It does not run searches, does not add sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstLiteratureFamilySearchPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    search_run_count = 0
    source_added_count = 0
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 6:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if not SELECTED_LITERATURE_FAMILY:
        errors.append("No selected literature family defined")

    if len(PLANNED_SEARCH_VENUES) < 8:
        errors.append(f"Planned search venue count too low: {len(PLANNED_SEARCH_VENUES)}")

    if len(PLANNED_QUERY_STRINGS) < 10:
        errors.append(f"Planned query count too low: {len(PLANNED_QUERY_STRINGS)}")

    if len(CLAIM_CATEGORIES_FOR_FIRST_SEARCH) < 6:
        errors.append(f"Claim category count too low: {len(CLAIM_CATEGORIES_FOR_FIRST_SEARCH)}")

    if len(INCLUSION_CRITERIA) < 8:
        errors.append(f"Inclusion criteria count too low: {len(INCLUSION_CRITERIA)}")

    if len(EXCLUSION_CRITERIA) < 8:
        errors.append(f"Exclusion criteria count too low: {len(EXCLUSION_CRITERIA)}")

    if len(SEARCH_RUN_FIELDS_TO_FILL_LATER) < 16:
        errors.append(f"Search run field count too low: {len(SEARCH_RUN_FIELDS_TO_FILL_LATER)}")

    if len(CANDIDATE_SCREENING_STEPS) < 8:
        errors.append(f"Screening step count too low: {len(CANDIDATE_SCREENING_STEPS)}")

    if len(FIRST_SEARCH_RUN_GATES) < 10:
        errors.append(f"Search run gate count too low: {len(FIRST_SEARCH_RUN_GATES)}")

    if boundary_count < 13:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 10:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    for label, value in [
        ("Search run count", search_run_count),
        ("Source added count", source_added_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for first literature family search plan: {word_count}")

    warnings.append("Plan defines future search only; it does not perform literature search.")
    warnings.append("Plan does not add sources, citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v5.4 plan selects the first literature family and defines controlled "
        "future search parameters without running searches, adding sources, adding "
        "citations, populating the evidence matrix, or revising the manuscript."
    )

    return FirstLiteratureFamilySearchPlanResult(
        title="First Literature Family Search Plan v5.4",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        selected_family_count=1 if SELECTED_LITERATURE_FAMILY else 0,
        planned_venue_count=len(PLANNED_SEARCH_VENUES),
        planned_query_count=len(PLANNED_QUERY_STRINGS),
        claim_category_count=len(CLAIM_CATEGORIES_FOR_FIRST_SEARCH),
        inclusion_criteria_count=len(INCLUSION_CRITERIA),
        exclusion_criteria_count=len(EXCLUSION_CRITERIA),
        search_run_field_count=len(SEARCH_RUN_FIELDS_TO_FILL_LATER),
        screening_step_count=len(CANDIDATE_SCREENING_STEPS),
        search_run_gate_count=len(FIRST_SEARCH_RUN_GATES),
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        search_run_count=search_run_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
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

    print("First Literature Family Search Plan v5.4")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Selected family count: {result.selected_family_count}")
    print(f"Planned venue count: {result.planned_venue_count}")
    print(f"Planned query count: {result.planned_query_count}")
    print(f"Claim category count: {result.claim_category_count}")
    print(f"Inclusion criteria count: {result.inclusion_criteria_count}")
    print(f"Exclusion criteria count: {result.exclusion_criteria_count}")
    print(f"Search run field count: {result.search_run_field_count}")
    print(f"Screening step count: {result.screening_step_count}")
    print(f"Search run gate count: {result.search_run_gate_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Search run count: {result.search_run_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
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
