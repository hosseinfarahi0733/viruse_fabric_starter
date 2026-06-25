"""Empty literature search log artifact for Viruse Fabric v5.2.

This module generates a real but empty literature search log artifact.

It connects:
- the v5.1 literature search log template,
- the v4.7 literature search protocol,
- the v4.8 literature family evidence matrix,
- the v4.9 claim-to-citation readiness map,
- the v5.0 citation-grounded manuscript revision plan.

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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"

SOURCE_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_SEARCH_PROTOCOL = PROJECT_ROOT / "outputs" / "literature_search_protocol_v4_7.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"
SOURCE_REVISION_PLAN = PROJECT_ROOT / "outputs" / "citation_grounded_manuscript_revision_plan_v5_0.md"

SOURCE_ARTIFACTS = [
    SOURCE_LOG_TEMPLATE,
    SOURCE_SEARCH_PROTOCOL,
    SOURCE_EVIDENCE_MATRIX,
    SOURCE_CLAIM_MAP,
    SOURCE_REVISION_PLAN,
]


EMPTY_REGISTRIES = [
    "search_run_registry",
    "candidate_source_registry",
    "retained_source_registry",
    "deferred_source_registry",
    "rejected_source_registry",
    "claim_mapping_registry",
    "audit_decision_registry",
    "evidence_matrix_transfer_registry",
]


EMPTY_SEARCH_RUN_COLUMNS = [
    "search_run_id",
    "search_date",
    "searcher",
    "literature_family",
    "claim_category",
    "search_venue",
    "query_string",
    "query_rationale",
    "raw_result_count",
    "screened_result_count",
    "candidate_source_count",
    "retained_source_count",
    "deferred_source_count",
    "rejected_source_count",
    "status",
    "notes",
]


EMPTY_CANDIDATE_SOURCE_COLUMNS = [
    "candidate_source_id",
    "search_run_id",
    "source_status",
    "source_role",
    "title_pending",
    "author_pending",
    "year_pending",
    "venue_pending",
    "identifier_pending",
    "abstract_screening_notes",
    "relevant_passage_notes",
    "claim_link",
    "evidence_strength",
    "boundary_effect",
    "decision",
    "decision_rationale",
    "audit_notes",
]


EMPTY_CLAIM_MAPPING_COLUMNS = [
    "claim_id",
    "claim_text",
    "readiness_category",
    "citation_action",
    "evidence_need",
    "allowed_use_level",
    "validation_boundary",
    "candidate_source_id",
    "source_role",
    "decision",
    "revision_instruction",
    "audit_status",
]


INITIAL_STATUS_VALUES = [
    "empty",
    "not_started",
    "awaiting_real_search",
    "awaiting_candidate_sources",
    "awaiting_audit",
    "not_ready_for_evidence_matrix_population",
    "not_ready_for_manuscript_revision",
]


LOG_RULES = [
    "The log starts empty.",
    "No search run is recorded until a real search is performed.",
    "No candidate source is recorded until a real source is found.",
    "No retained source is recorded until a candidate source is reviewed.",
    "No citation is recorded in this artifact.",
    "No source is transferred to the evidence matrix from this artifact yet.",
    "No manuscript revision is triggered by this artifact.",
    "Every future search run must preserve exact query text.",
    "Every future candidate source must preserve a review decision.",
    "Every future retained source must preserve a source role and boundary effect.",
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
    "no source is added by this artifact",
    "no citation is added by this artifact",
    "no search is run by this artifact",
    "the evidence matrix is not populated by this artifact",
    "the manuscript is not revised by this artifact",
]


PROHIBITED_BEHAVIORS = [
    "Do not add invented sources.",
    "Do not add invented citations.",
    "Do not add fake search runs.",
    "Do not add fake query strings.",
    "Do not record fake author names.",
    "Do not record fake identifiers.",
    "Do not treat empty registries as evidence.",
    "Do not treat this artifact as a bibliography.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not populate the evidence matrix from an empty log.",
    "Do not revise the manuscript from an empty log.",
]


NEXT_STEPS = [
    "Use this empty log as the controlled starting point for real search.",
    "Create real search run entries only after searches are performed.",
    "Record exact query strings from real searches.",
    "Record candidate sources only after they are found.",
    "Screen candidate sources against inclusion and exclusion criteria.",
    "Audit candidate source decisions before retention.",
    "Transfer retained sources to the evidence matrix only after audit.",
    "Prepare manuscript revision notes only after evidence mapping is complete.",
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
    "no source",
    "no citation",
    "no search",
    "no candidate",
    "no retained",
    "no manuscript",
    "cannot",
    "empty",
    "awaiting",
    "not ready",
    "boundary",
    "prohibited",
    "future",
    "pending",
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
    "log rules",
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
class EmptyLiteratureSearchLogResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    empty_registry_count: int
    search_run_column_count: int
    candidate_source_column_count: int
    claim_mapping_column_count: int
    initial_status_value_count: int
    log_rule_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    search_run_count: int
    candidate_source_count: int
    retained_source_count: int
    deferred_source_count: int
    rejected_source_count: int
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


def render_empty_registry_table() -> str:
    rows = [
        "| Registry | Current row count | Status |",
        "|---|---:|---|",
    ]
    for registry in EMPTY_REGISTRIES:
        rows.append(f"| `{registry}` | 0 | empty |")
    return "\n".join(rows)


def render_column_table(title: str, columns: list[str]) -> str:
    rows = [
        f"| {title} column | Current value |",
        "|---|---|",
    ]
    for column in columns:
        rows.append(f"| `{column}` | `EMPTY` |")
    return "\n".join(rows)


def render_status_table() -> str:
    rows = [
        "| Initial status value | Meaning |",
        "|---|---|",
    ]
    for value in INITIAL_STATUS_VALUES:
        rows.append(f"| `{value}` | controlled empty-log status for future audit |")
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
    return f"""# Empty Literature Search Log v5.2

## Question
Can Viruse Fabric create a real but empty search log artifact for future literature work without running searches, adding sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

No search is run by this artifact. No source is added by this artifact. No citation is added by this artifact. The evidence matrix is not populated by this artifact. The manuscript is not revised by this artifact. Citation placeholders are not citations.

## Source Artifacts
{render_source_table()}

## Purpose
The v5.2 artifact turns the v5.1 template into a concrete empty log file.

It is intentionally empty. That emptiness is not a defect; it is the controlled starting state. The project now has a place where future real search runs can be recorded without pretending that any search has already happened. Apparently "nothing has happened yet" needs its own artifact, because otherwise people start filling silence with confidence and citations.

## Empty Registry Summary
{render_empty_registry_table()}

## Empty Search Run Columns
{render_column_table("Search run", EMPTY_SEARCH_RUN_COLUMNS)}

## Empty Candidate Source Columns
{render_column_table("Candidate source", EMPTY_CANDIDATE_SOURCE_COLUMNS)}

## Empty Claim Mapping Columns
{render_column_table("Claim mapping", EMPTY_CLAIM_MAPPING_COLUMNS)}

## Initial Status Values
{render_status_table()}

## Log Rules
{bullet_list(LOG_RULES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Empty Log Discipline
The empty log should be treated as a baseline artifact.

A future search run must change the log in a visible way: it must add a run identifier, a real date, a venue, an exact query string, a literature family, a claim category, and screening counts. Until that happens, the search run count remains zero.

A future candidate source must also change the log in a visible way. It must receive a candidate source identifier, source status, source role, claim link, decision value, and audit notes. Until that happens, the candidate source count remains zero.

This discipline prevents a quiet but dangerous error: treating a planned search as if it were a completed search. Humans do this often, usually with a meeting title and an alarming amount of confidence.

## Relationship to Later Milestones
The v5.2 artifact does not replace the v5.1 template.

The template defines fields and rules. This artifact instantiates those fields as an empty operational log. A later milestone may create the first real search run entry. Another later milestone may audit candidate sources. Another later milestone may populate the evidence matrix. None of those actions happen here.

The distinction matters. A template is a schema. An empty log is a starting state. A populated log is evidence of search activity. A populated evidence matrix is evidence of reviewed source decisions. A citation-grounded manuscript is still another later object. Collapsing those stages would make the workflow faster and worse, which is a classic human bargain and therefore not accepted here.

## Empty-State Audit Meaning
The empty log should pass because it is empty in a controlled way, not because it contains useful evidence.

An empty search run registry means no searches have been executed. An empty candidate source registry means no source has been found, screened, or reviewed. An empty retained source registry means no source is available for evidence matrix transfer. These are not failures. They are explicit baseline counts.

This makes later changes auditable. When the first real search is added, the diff should show exactly which search run appeared, which query was used, which venue was searched, and which claim category was targeted. If a source appears without a search run, that should be treated as a process error rather than a discovery. Science is already hard enough without sources teleporting into existence like badly behaved rabbits.

## Evidence Discipline
This artifact also separates search activity from evidence status.

A search result is not a candidate source until it is recorded. A candidate source is not a retained source until it is reviewed. A retained source is not a citation until it is linked to a claim and assigned a role. A citation is not validation. External validation still requires independent evidence beyond literature positioning.

The project therefore keeps five different things separate: search, source screening, evidence mapping, citation insertion, and manuscript revision. This is tedious. It is also how the project avoids dressing assumptions in formal clothing and calling them results.

## Output Counts
Search run count: 0

Candidate source count: 0

Retained source count: 0

Deferred source count: 0

Rejected source count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact prepares a controlled empty literature search log.

It does not run searches, does not add sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> EmptyLiteratureSearchLogResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    search_run_count = 0
    candidate_source_count = 0
    retained_source_count = 0
    deferred_source_count = 0
    rejected_source_count = 0
    source_added_count = 0
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    log_rule_count = count_present_terms(report, LOG_RULES)
    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 5:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if len(EMPTY_REGISTRIES) < 8:
        errors.append(f"Empty registry count too low: {len(EMPTY_REGISTRIES)}")

    if len(EMPTY_SEARCH_RUN_COLUMNS) < 16:
        errors.append(f"Search run column count too low: {len(EMPTY_SEARCH_RUN_COLUMNS)}")

    if len(EMPTY_CANDIDATE_SOURCE_COLUMNS) < 16:
        errors.append(
            f"Candidate source column count too low: {len(EMPTY_CANDIDATE_SOURCE_COLUMNS)}"
        )

    if len(EMPTY_CLAIM_MAPPING_COLUMNS) < 11:
        errors.append(f"Claim mapping column count too low: {len(EMPTY_CLAIM_MAPPING_COLUMNS)}")

    if len(INITIAL_STATUS_VALUES) < 7:
        errors.append(f"Initial status value count too low: {len(INITIAL_STATUS_VALUES)}")

    if log_rule_count < 10:
        errors.append(f"Log rule count too low: {log_rule_count}")

    if boundary_count < 13:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 12:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    for label, value in [
        ("Search run count", search_run_count),
        ("Candidate source count", candidate_source_count),
        ("Retained source count", retained_source_count),
        ("Deferred source count", deferred_source_count),
        ("Rejected source count", rejected_source_count),
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
        errors.append(f"Word count too low for empty literature search log: {word_count}")

    warnings.append("Empty log adds no sources or citations; real search must happen later.")
    warnings.append("Empty log does not populate the evidence matrix or revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v5.2 artifact creates a real empty literature search log as a "
        "controlled starting state without running searches, adding sources, "
        "adding citations, populating the evidence matrix, or revising the manuscript."
    )

    return EmptyLiteratureSearchLogResult(
        title="Empty Literature Search Log v5.2",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        empty_registry_count=len(EMPTY_REGISTRIES),
        search_run_column_count=len(EMPTY_SEARCH_RUN_COLUMNS),
        candidate_source_column_count=len(EMPTY_CANDIDATE_SOURCE_COLUMNS),
        claim_mapping_column_count=len(EMPTY_CLAIM_MAPPING_COLUMNS),
        initial_status_value_count=len(INITIAL_STATUS_VALUES),
        log_rule_count=log_rule_count,
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        search_run_count=search_run_count,
        candidate_source_count=candidate_source_count,
        retained_source_count=retained_source_count,
        deferred_source_count=deferred_source_count,
        rejected_source_count=rejected_source_count,
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

    print("Empty Literature Search Log v5.2")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Empty registry count: {result.empty_registry_count}")
    print(f"Search run column count: {result.search_run_column_count}")
    print(f"Candidate source column count: {result.candidate_source_column_count}")
    print(f"Claim mapping column count: {result.claim_mapping_column_count}")
    print(f"Initial status value count: {result.initial_status_value_count}")
    print(f"Log rule count: {result.log_rule_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Search run count: {result.search_run_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Deferred source count: {result.deferred_source_count}")
    print(f"Rejected source count: {result.rejected_source_count}")
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
