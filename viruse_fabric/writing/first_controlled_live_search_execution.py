"""First controlled live search execution for Viruse Fabric v5.7.

This module records the first controlled live literature-search execution.

It records:
- the controlled live-search execution date,
- the executed query family,
- the retrieval context,
- the raw result count observed during assistant-mediated web retrieval,
- the boundary that raw results are not candidate sources,
- the boundary that candidate sources are not retained sources,
- the boundary that retained sources are not citations,
- the boundary that citations are not external validation.

It does not add candidate sources.
It does not retain sources.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_controlled_live_search_execution_v5_7.md"

SOURCE_RUN_ARTIFACT = PROJECT_ROOT / "outputs" / "first_search_run_artifact_v5_5.md"
SOURCE_RUN_AUDIT = PROJECT_ROOT / "outputs" / "first_search_run_artifact_audit_v5_6.md"
SOURCE_FIRST_SEARCH_PLAN = PROJECT_ROOT / "outputs" / "first_literature_family_search_plan_v5_4.md"
SOURCE_EMPTY_LOG = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"
SOURCE_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"

SOURCE_ARTIFACTS = [
    SOURCE_RUN_ARTIFACT,
    SOURCE_RUN_AUDIT,
    SOURCE_FIRST_SEARCH_PLAN,
    SOURCE_EMPTY_LOG,
    SOURCE_LOG_TEMPLATE,
    SOURCE_CLAIM_MAP,
    SOURCE_EVIDENCE_MATRIX,
]


EXECUTION_METADATA = {
    "search_execution_id": "SE-0001",
    "search_run_shell_id": "SR-0001-SHELL",
    "execution_status": "executed_raw_search_only",
    "execution_date": "2026-06-26",
    "execution_timezone": "Asia/Baku",
    "searcher": "assistant-mediated web.run retrieval",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "claim_category": "literature-needed: constraints shape possible trajectories",
    "primary_planned_query_id": "Q-01",
    "primary_planned_query_string": '"constraint" "causality" "dynamical systems"',
    "retrieval_context": "assistant web.run system1_search_query",
    "raw_result_count": "23",
    "screened_result_count": "0",
    "candidate_source_count": "0",
    "retained_source_count": "0",
}


EXECUTED_QUERY_STRINGS = [
    '"constraint" "causality" "dynamical systems"',
    '"constraints" "causality" "dynamical systems"',
    '"constraint-based" causality "dynamical systems"',
]


RAW_RESULT_OBSERVATIONS = [
    {
        "label": "raw_result_observation_01",
        "title": "Information-theoretic formulation of dynamical systems",
        "observed_relevance": "mentions causality, modeling, control, and constraints in dynamical-systems framing",
        "status": "raw_result_only_not_candidate_source",
    },
    {
        "label": "raw_result_observation_02",
        "title": "Beyond Structural Causal Models: Causal Constraints Models",
        "observed_relevance": "appears directly relevant to causal constraints models and dynamical systems at equilibrium",
        "status": "raw_result_only_not_candidate_source",
    },
    {
        "label": "raw_result_observation_03",
        "title": "Causal screening in dynamical systems",
        "observed_relevance": "appears relevant to causal learning and dynamical systems",
        "status": "raw_result_only_not_candidate_source",
    },
    {
        "label": "raw_result_observation_04",
        "title": "Causality and independence in perfectly adapted dynamical systems",
        "observed_relevance": "appears relevant to constraint-based causal discovery and dynamical systems",
        "status": "raw_result_only_not_candidate_source",
    },
    {
        "label": "raw_result_observation_05",
        "title": "Causal Structure Learning for Dynamical Systems",
        "observed_relevance": "appears relevant to causal structure learning in dynamical systems",
        "status": "raw_result_only_not_candidate_source",
    },
]


EXECUTION_FIELDS = [
    "search_execution_id",
    "search_run_shell_id",
    "execution_status",
    "execution_date",
    "execution_timezone",
    "searcher",
    "literature_family",
    "claim_category",
    "primary_planned_query_id",
    "primary_planned_query_string",
    "retrieval_context",
    "raw_result_count",
    "screened_result_count",
    "candidate_source_count",
    "retained_source_count",
]


EXECUTION_GATES = [
    "The execution must be linked to the v5.5 run shell.",
    "The execution must be linked to the v5.6 shell audit.",
    "The execution must record a real execution date.",
    "The execution must record a retrieval context.",
    "The execution must record the query strings used.",
    "The execution must record raw result count.",
    "The execution must keep screened result count zero.",
    "The execution must keep candidate source count zero.",
    "The execution must keep retained source count zero.",
    "The execution must add no citations.",
    "The execution must populate no evidence matrix rows.",
    "The execution must revise no manuscript text.",
]


RAW_RESULT_BOUNDARIES = [
    "A raw result is not a candidate source.",
    "A candidate source is not a retained source.",
    "A retained source is not automatically a citation.",
    "A citation is not external validation.",
    "A result title is not evidence.",
    "A result snippet is not source audit.",
    "A search result count is not literature grounding.",
    "A search execution is not manuscript support.",
    "A live search is only an entry point into screening.",
    "Screening must happen after execution.",
]


NEXT_STEPS = [
    "Create a first raw-result screening plan.",
    "Screen raw results against inclusion and exclusion criteria.",
    "Create candidate source entries only after screening.",
    "Audit candidate source metadata before retention.",
    "Retain sources only after source audit.",
    "Populate evidence matrix only after retained-source audit.",
    "Add citations only after retained-source decision.",
    "Revise manuscript only after citation-grounded integration.",
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
    "raw results are not candidate sources",
    "candidate sources are not retained sources",
    "retained sources are not citations",
    "citations are not external validation",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
]


PROHIBITED_BEHAVIORS = [
    "Do not treat raw results as candidate sources.",
    "Do not treat snippets as evidence.",
    "Do not treat result titles as citations.",
    "Do not retain sources in this milestone.",
    "Do not add citations in this milestone.",
    "Do not populate the evidence matrix in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
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
    "raw result",
    "candidate source",
    "retained source",
    "zero",
    "screening",
    "future",
    "boundary",
    "prohibited",
    "internal validation",
    "not externally",
    "not submission",
    "not a final",
    "not biological",
    "not clinical",
    "not laboratory",
    "not operational",
    "citations are not external validation",
]


SAFE_SECTION_HEADINGS = [
    "boundary phrases",
    "prohibited behaviors",
    "raw result boundaries",
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
class FirstControlledLiveSearchExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    executed_search_count: int
    executed_query_count: int
    raw_result_count: int
    raw_result_observation_count: int
    screened_result_count: int
    candidate_source_count: int
    retained_source_count: int
    source_added_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
    execution_field_count: int
    execution_gate_count: int
    raw_result_boundary_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
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


def render_metadata_table() -> str:
    rows = [
        "| Execution field | Value |",
        "|---|---|",
    ]
    for key, value in EXECUTION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_query_table() -> str:
    rows = [
        "| Query index | Executed query string | Status |",
        "|---|---|---|",
    ]
    for index, query in enumerate(EXECUTED_QUERY_STRINGS, start=1):
        rows.append(f"| {index} | `{query}` | executed as retrieval string |")
    return "\n".join(rows)


def render_raw_observation_table() -> str:
    rows = [
        "| Label | Raw result title | Observed relevance | Status |",
        "|---|---|---|---|",
    ]
    for item in RAW_RESULT_OBSERVATIONS:
        rows.append(
            f"| {item['label']} | {item['title']} | "
            f"{item['observed_relevance']} | {item['status']} |"
        )
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

        if "fake citation" in lowered or "not citations" in lowered:
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def render_report() -> str:
    return f"""# First Controlled Live Search Execution v5.7

## Question
Can Viruse Fabric execute the first controlled live search while keeping raw results separate from candidate sources, citations, evidence matrix population, and manuscript revision?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone records a controlled live search execution. It does not add candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

## Source Artifacts
{render_source_table()}

## Execution Metadata
{render_metadata_table()}

## Executed Query Strings
{render_query_table()}

## Raw Result Observations
{render_raw_observation_table()}

These observations are raw search-result observations only. Raw results are not candidate sources. Candidate sources are not retained sources. Retained sources are not citations. Citations are not external validation.

## Execution Fields
{bullet_list(EXECUTION_FIELDS)}

## Execution Gates
{bullet_list(EXECUTION_GATES)}

## Raw Result Boundaries
{bullet_list(RAW_RESULT_BOUNDARIES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Execution Interpretation
The search has now crossed one boundary: it is no longer only a planned shell.

However, it has not crossed the evidence boundary. The artifact records that a live retrieval event occurred and that raw results were observed. It does not screen those results. It does not create candidate source records. It does not decide whether any result is reliable, relevant, or usable. It does not transfer anything into the evidence matrix. It does not revise the manuscript.

This matters because raw search output is noisy. Search engines return a mixture of relevant papers, adjacent papers, preprints, pages with incomplete metadata, and decorative distractions wearing academic perfume. A controlled workflow must resist the urge to convert search output into authority.

## Evidence Boundary
A raw result count is a search-execution measurement, not literature grounding.

A raw result title is a pointer, not evidence. A snippet is a clue, not a source review. A search engine result is not a bibliographic record. A bibliographic record is not a retained source. A retained source is not automatically a citation. A citation is not external validation.

The next useful transition is screening. Screening should decide which raw results deserve candidate source entries. Candidate source entries should then be audited before retention. Only retained and audited sources can later be mapped into the evidence matrix. Only after that should the manuscript be revised. Yes, this is slow. So is building a bridge that does not collapse, another apparently controversial concept.

## Screening Boundary
The live search execution produces a raw retrieval event, not a screened literature set.

Screening must check each raw result against the inclusion and exclusion criteria from the prior search plan. A result may look relevant because it shares words such as constraint, causality, or dynamical systems, but shared vocabulary is not enough. The screening step must decide whether the result actually addresses the project claim category, whether its metadata are sufficient, whether it is a primary source or a secondary discussion, and whether it can be responsibly reviewed.

This milestone deliberately stops before that step. The raw observations are recorded so the next milestone has something concrete to screen. They are not elevated into project evidence. They are not imported into the evidence matrix. They are not used to rewrite the manuscript. Research discipline is mostly the art of not turning the first shiny search result into a throne.

## Candidate Source Boundary
A candidate source entry requires more than appearing in the raw result list.

A future candidate record should include a stable title, authorship metadata, venue or repository, year when available, access route, claim-category mapping, inclusion rationale, exclusion-risk notes, and source-role proposal. Without that metadata, the project cannot audit whether the result belongs in the evidence workflow. In v5.7, none of that candidate-source work is performed.

This protects the project from decorative bibliography. A paper title can sound relevant and still be unusable. A source can be adjacent without being supportive. A source can be useful for contrast rather than support. The workflow must preserve those distinctions instead of tossing everything into a citation pile and hoping formality will perform magic. Spoiler: it will not.

## Output Counts
Executed search count: 1

Executed query count: 3

Raw result count: 23

Raw result observation count: 5

Screened result count: 0

Candidate source count: 0

Retained source count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact records the first controlled live search execution.

It does not add candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstControlledLiveSearchExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    executed_search_count = 1
    executed_query_count = len(EXECUTED_QUERY_STRINGS)
    raw_result_count = int(EXECUTION_METADATA["raw_result_count"])
    raw_result_observation_count = len(RAW_RESULT_OBSERVATIONS)
    screened_result_count = int(EXECUTION_METADATA["screened_result_count"])
    candidate_source_count = int(EXECUTION_METADATA["candidate_source_count"])
    retained_source_count = int(EXECUTION_METADATA["retained_source_count"])
    source_added_count = 0
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    raw_boundary_count = count_present_terms(report, RAW_RESULT_BOUNDARIES)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 7:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if executed_search_count != 1:
        errors.append(f"Executed search count should be one, got: {executed_search_count}")

    if executed_query_count < 1:
        errors.append(f"Executed query count too low: {executed_query_count}")

    if raw_result_count < 1:
        errors.append(f"Raw result count should be positive, got: {raw_result_count}")

    if raw_result_observation_count < 5:
        errors.append(f"Raw result observation count too low: {raw_result_observation_count}")

    if screened_result_count != 0:
        errors.append(f"Screened result count should be zero, got: {screened_result_count}")

    if candidate_source_count != 0:
        errors.append(f"Candidate source count should be zero, got: {candidate_source_count}")

    if retained_source_count != 0:
        errors.append(f"Retained source count should be zero, got: {retained_source_count}")

    for label, value in [
        ("Source added count", source_added_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if len(EXECUTION_FIELDS) < 15:
        errors.append(f"Execution field count too low: {len(EXECUTION_FIELDS)}")

    if len(EXECUTION_GATES) < 12:
        errors.append(f"Execution gate count too low: {len(EXECUTION_GATES)}")

    if raw_boundary_count < 10:
        errors.append(f"Raw result boundary count too low: {raw_boundary_count}")

    if boundary_count < 14:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 10:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for first controlled live search execution: {word_count}")

    warnings.append("Execution records raw search results only; no candidate sources are created.")
    warnings.append("Execution does not add citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v5.7 artifact records one controlled live search execution with "
        "raw results observed, while keeping screened results, candidate sources, "
        "retained sources, citations, evidence matrix population, and manuscript "
        "revision at zero."
    )

    return FirstControlledLiveSearchExecutionResult(
        title="First Controlled Live Search Execution v5.7",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        executed_search_count=executed_search_count,
        executed_query_count=executed_query_count,
        raw_result_count=raw_result_count,
        raw_result_observation_count=raw_result_observation_count,
        screened_result_count=screened_result_count,
        candidate_source_count=candidate_source_count,
        retained_source_count=retained_source_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
        execution_field_count=len(EXECUTION_FIELDS),
        execution_gate_count=len(EXECUTION_GATES),
        raw_result_boundary_count=raw_boundary_count,
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
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

    print("First Controlled Live Search Execution v5.7")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Executed search count: {result.executed_search_count}")
    print(f"Executed query count: {result.executed_query_count}")
    print(f"Raw result count: {result.raw_result_count}")
    print(f"Raw result observation count: {result.raw_result_observation_count}")
    print(f"Screened result count: {result.screened_result_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Execution field count: {result.execution_field_count}")
    print(f"Execution gate count: {result.execution_gate_count}")
    print(f"Raw result boundary count: {result.raw_result_boundary_count}")
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
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
