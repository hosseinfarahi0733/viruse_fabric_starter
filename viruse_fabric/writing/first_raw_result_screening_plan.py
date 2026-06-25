"""First raw result screening plan for Viruse Fabric v5.8.

This module creates a controlled screening plan for the raw results observed in v5.7.

It plans screening only.

It does not screen raw results.
It does not create candidate sources.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_raw_result_screening_plan_v5_8.md"

SOURCE_LIVE_SEARCH = PROJECT_ROOT / "outputs" / "first_controlled_live_search_execution_v5_7.md"
SOURCE_SEARCH_AUDIT = PROJECT_ROOT / "outputs" / "first_search_run_artifact_audit_v5_6.md"
SOURCE_SEARCH_SHELL = PROJECT_ROOT / "outputs" / "first_search_run_artifact_v5_5.md"
SOURCE_SEARCH_PLAN = PROJECT_ROOT / "outputs" / "first_literature_family_search_plan_v5_4.md"
SOURCE_EMPTY_LOG = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"
SOURCE_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"

SOURCE_ARTIFACTS = [
    SOURCE_LIVE_SEARCH,
    SOURCE_SEARCH_AUDIT,
    SOURCE_SEARCH_SHELL,
    SOURCE_SEARCH_PLAN,
    SOURCE_EMPTY_LOG,
    SOURCE_LOG_TEMPLATE,
    SOURCE_CLAIM_MAP,
    SOURCE_EVIDENCE_MATRIX,
]


SCREENING_PLAN_METADATA = {
    "screening_plan_id": "SP-0001",
    "linked_execution_id": "SE-0001",
    "linked_shell_id": "SR-0001-SHELL",
    "plan_status": "planned_not_executed",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "claim_category": "literature-needed: constraints shape possible trajectories",
    "raw_result_count_from_v5_7": "23",
    "raw_result_observation_count_from_v5_7": "5",
    "screened_result_count": "0",
    "candidate_source_count": "0",
    "retained_source_count": "0",
}


RAW_OBSERVATION_IDS = [
    "raw_result_observation_01",
    "raw_result_observation_02",
    "raw_result_observation_03",
    "raw_result_observation_04",
    "raw_result_observation_05",
]


SCREENING_FIELDS = [
    "raw_result_observation_id",
    "raw_result_title",
    "stable_access_route_present",
    "metadata_sufficiency",
    "claim_category_alignment",
    "conceptual_relevance",
    "source_type",
    "primary_or_secondary_status",
    "inclusion_reason",
    "exclusion_risk",
    "candidate_source_recommendation",
    "review_notes",
]


INCLUSION_CRITERIA = [
    "The result must address constraints, causality, dynamical systems, causal structure, or state-space reasoning.",
    "The result must connect to the selected literature family.",
    "The result must map to at least one v4.9 claim category.",
    "The result must have enough metadata for later candidate-source logging.",
    "The result must be more than a keyword-only match.",
    "The result must support either background, contrast, formal framing, or boundary clarification.",
    "The result must be reviewable without inventing bibliographic details.",
    "The result must be separable from biological, clinical, laboratory, or operational guidance claims.",
]


EXCLUSION_CRITERIA = [
    "Exclude results that only share vocabulary without conceptual relevance.",
    "Exclude results with insufficient metadata for controlled logging.",
    "Exclude results that would require invented authors, titles, venues, years, or identifiers.",
    "Exclude results that imply external validation of Viruse Fabric.",
    "Exclude results that push the project toward biological, clinical, laboratory, or operational guidance.",
    "Exclude results that cannot be mapped to a claim category.",
    "Exclude results that are useful only as decorative authority.",
    "Exclude results that cannot be responsibly reviewed in a later source audit.",
]


SCREENING_STEPS = [
    "Confirm the raw observation exists in the v5.7 execution artifact.",
    "Copy the raw title into the screening worksheet only as a raw observation.",
    "Check whether metadata are sufficient for later candidate-source logging.",
    "Check conceptual relevance against the selected literature family.",
    "Check alignment with the v4.9 claim category.",
    "Apply inclusion criteria.",
    "Apply exclusion criteria.",
    "Assign a non-binding screening recommendation.",
    "Keep candidate source count at zero.",
    "Record that actual screening has not yet been executed.",
]


SCREENING_RECOMMENDATION_VALUES = [
    "pending_screening",
    "possible_candidate_later",
    "defer_for_metadata_check",
    "exclude_later_if_keyword_only",
    "exclude_later_if_boundary_risk",
]


RAW_RESULT_TO_SCREENING_ROWS = [
    {
        "raw_result_observation_id": "raw_result_observation_01",
        "screening_status": "planned_not_screened",
        "candidate_source_status": "not_created",
    },
    {
        "raw_result_observation_id": "raw_result_observation_02",
        "screening_status": "planned_not_screened",
        "candidate_source_status": "not_created",
    },
    {
        "raw_result_observation_id": "raw_result_observation_03",
        "screening_status": "planned_not_screened",
        "candidate_source_status": "not_created",
    },
    {
        "raw_result_observation_id": "raw_result_observation_04",
        "screening_status": "planned_not_screened",
        "candidate_source_status": "not_created",
    },
    {
        "raw_result_observation_id": "raw_result_observation_05",
        "screening_status": "planned_not_screened",
        "candidate_source_status": "not_created",
    },
]


SCREENING_GATES = [
    "Screening must be planned before execution.",
    "Raw observations must remain raw observations.",
    "Screening status must remain planned_not_screened in this milestone.",
    "Candidate source status must remain not_created.",
    "Candidate source count must remain zero.",
    "Retained source count must remain zero.",
    "Citation added count must remain zero.",
    "Evidence matrix populated count must remain zero.",
    "Manuscript revised count must remain zero.",
    "No source may be treated as retained during this milestone.",
    "No raw result title may be treated as a citation.",
    "No raw result may be treated as external validation.",
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
    "screening plan is not screening execution",
    "does not create candidate sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
]


PROHIBITED_BEHAVIORS = [
    "Do not screen raw results in this milestone.",
    "Do not create candidate sources in this milestone.",
    "Do not retain sources in this milestone.",
    "Do not add citations in this milestone.",
    "Do not populate the evidence matrix in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat raw result titles as evidence.",
    "Do not treat raw snippets as source audit.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
]


NEXT_STEPS = [
    "Execute the first raw-result screening in a later milestone.",
    "Apply inclusion criteria to each raw observation.",
    "Apply exclusion criteria to each raw observation.",
    "Record screening decisions explicitly.",
    "Create candidate source entries only after screening execution.",
    "Audit candidate source metadata before retention.",
    "Retain sources only after candidate audit.",
    "Populate evidence matrix only after retained-source audit.",
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
    "screening plan",
    "planned",
    "not_screened",
    "not_created",
    "future",
    "later",
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
    "screening gates",
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
class FirstRawResultScreeningPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    raw_result_count: int
    raw_result_observation_count: int
    screening_plan_count: int
    screening_execution_count: int
    screening_field_count: int
    inclusion_criteria_count: int
    exclusion_criteria_count: int
    screening_step_count: int
    screening_recommendation_value_count: int
    screening_row_count: int
    screening_gate_count: int
    screened_result_count: int
    candidate_source_count: int
    retained_source_count: int
    source_added_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
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
        "| Screening plan field | Value |",
        "|---|---|",
    ]
    for key, value in SCREENING_PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_screening_rows() -> str:
    rows = [
        "| Raw observation id | Screening status | Candidate source status |",
        "|---|---|---|",
    ]
    for item in RAW_RESULT_TO_SCREENING_ROWS:
        rows.append(
            f"| {item['raw_result_observation_id']} | "
            f"{item['screening_status']} | "
            f"{item['candidate_source_status']} |"
        )
    return "\n".join(rows)


def render_field_table(fields: list[str]) -> str:
    rows = [
        "| Screening field | v5.8 status |",
        "|---|---|",
    ]
    for field in fields:
        rows.append(f"| `{field}` | planned for later screening execution |")
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
    return f"""# First Raw Result Screening Plan v5.8

## Question
Can Viruse Fabric plan the first raw-result screening step without actually screening results, creating candidate sources, retaining sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This is a screening plan, not screening execution. The screening plan does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

## Source Artifacts
{render_source_table()}

## Screening Plan Metadata
{render_metadata_table()}

## Raw Observations to Be Screened Later
{bullet_list(RAW_OBSERVATION_IDS)}

## Screening Fields
{render_field_table(SCREENING_FIELDS)}

## Planned Screening Rows
{render_screening_rows()}

## Inclusion Criteria
{bullet_list(INCLUSION_CRITERIA)}

## Exclusion Criteria
{bullet_list(EXCLUSION_CRITERIA)}

## Screening Steps
{bullet_list(SCREENING_STEPS)}

## Screening Recommendation Values
{bullet_list(SCREENING_RECOMMENDATION_VALUES)}

## Screening Gates
{bullet_list(SCREENING_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Screening Interpretation
The v5.8 artifact prepares a screening procedure for the raw observations recorded in v5.7.

It does not screen them. It does not say any raw observation is useful. It does not say any raw observation is reliable. It does not say any raw observation should become a candidate source. It only defines how those questions should be asked later.

This matters because the raw result stage is where projects often become sloppy. A search result looks relevant, then someone treats it as a source. A source looks impressive, then someone treats it as support. Support looks convenient, then someone treats it as validation. This is how academic fog machines are built.

## Screening Boundary
Screening will be the first interpretive filter after live search.

The screening step must distinguish vocabulary overlap from conceptual relevance. It must distinguish a pointer from a source record. It must distinguish a possible candidate from a retained source. It must check metadata sufficiency before any candidate entry exists. The point is not to reject everything. The point is to stop the project from accepting things before it knows what they are.

The five raw observations from v5.7 are therefore treated as planned screening targets only. They are not candidate sources. They are not retained sources. They are not citations. They are not evidence matrix rows. They are not manuscript support.

## Candidate Boundary
A candidate source may only be created after screening execution.

A future candidate source entry should include enough metadata to be audited: stable title, author information when available, venue or repository, year or access date when appropriate, access route, claim-category mapping, inclusion rationale, exclusion risks, and proposed source role. Without that metadata, a result cannot responsibly enter the evidence workflow.

This milestone intentionally keeps candidate source count at zero. That is not a weakness. It is a boundary. A workflow that cannot tolerate zero counts before evidence exists is not a workflow; it is wishful thinking with headings.

## Output Counts
Raw result count: 23

Raw result observation count: 5

Screening plan count: 1

Screening execution count: 0

Screened result count: 0

Candidate source count: 0

Retained source count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact plans the first raw-result screening step.

It does not screen raw results, does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstRawResultScreeningPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    raw_result_count = int(SCREENING_PLAN_METADATA["raw_result_count_from_v5_7"])
    raw_result_observation_count = len(RAW_OBSERVATION_IDS)
    screening_plan_count = 1
    screening_execution_count = 0
    screened_result_count = int(SCREENING_PLAN_METADATA["screened_result_count"])
    candidate_source_count = int(SCREENING_PLAN_METADATA["candidate_source_count"])
    retained_source_count = int(SCREENING_PLAN_METADATA["retained_source_count"])
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

    if len(SOURCE_ARTIFACTS) < 8:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if raw_result_count < 1:
        errors.append(f"Raw result count should be positive, got: {raw_result_count}")

    if raw_result_observation_count < 5:
        errors.append(f"Raw result observation count too low: {raw_result_observation_count}")

    if screening_plan_count != 1:
        errors.append(f"Screening plan count should be one, got: {screening_plan_count}")

    if screening_execution_count != 0:
        errors.append(f"Screening execution count should be zero, got: {screening_execution_count}")

    if len(SCREENING_FIELDS) < 12:
        errors.append(f"Screening field count too low: {len(SCREENING_FIELDS)}")

    if len(INCLUSION_CRITERIA) < 8:
        errors.append(f"Inclusion criteria count too low: {len(INCLUSION_CRITERIA)}")

    if len(EXCLUSION_CRITERIA) < 8:
        errors.append(f"Exclusion criteria count too low: {len(EXCLUSION_CRITERIA)}")

    if len(SCREENING_STEPS) < 10:
        errors.append(f"Screening step count too low: {len(SCREENING_STEPS)}")

    if len(SCREENING_RECOMMENDATION_VALUES) < 5:
        errors.append(
            f"Screening recommendation value count too low: {len(SCREENING_RECOMMENDATION_VALUES)}"
        )

    if len(RAW_RESULT_TO_SCREENING_ROWS) < 5:
        errors.append(f"Screening row count too low: {len(RAW_RESULT_TO_SCREENING_ROWS)}")

    if len(SCREENING_GATES) < 12:
        errors.append(f"Screening gate count too low: {len(SCREENING_GATES)}")

    for label, value in [
        ("Screened result count", screened_result_count),
        ("Candidate source count", candidate_source_count),
        ("Retained source count", retained_source_count),
        ("Source added count", source_added_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if boundary_count < 16:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 11:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if fake_citations:
        errors.append(f"Fake citation-like patterns detected: {len(fake_citations)}")

    if word_count < 1200:
        errors.append(f"Word count too low for first raw result screening plan: {word_count}")

    warnings.append("Screening plan does not execute screening or create candidate sources.")
    warnings.append("Screening plan does not add citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v5.8 artifact plans the first raw-result screening step while keeping "
        "screening execution, candidate sources, retained sources, citations, "
        "evidence matrix population, and manuscript revision at zero."
    )

    return FirstRawResultScreeningPlanResult(
        title="First Raw Result Screening Plan v5.8",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        raw_result_count=raw_result_count,
        raw_result_observation_count=raw_result_observation_count,
        screening_plan_count=screening_plan_count,
        screening_execution_count=screening_execution_count,
        screening_field_count=len(SCREENING_FIELDS),
        inclusion_criteria_count=len(INCLUSION_CRITERIA),
        exclusion_criteria_count=len(EXCLUSION_CRITERIA),
        screening_step_count=len(SCREENING_STEPS),
        screening_recommendation_value_count=len(SCREENING_RECOMMENDATION_VALUES),
        screening_row_count=len(RAW_RESULT_TO_SCREENING_ROWS),
        screening_gate_count=len(SCREENING_GATES),
        screened_result_count=screened_result_count,
        candidate_source_count=candidate_source_count,
        retained_source_count=retained_source_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
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

    print("First Raw Result Screening Plan v5.8")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Raw result count: {result.raw_result_count}")
    print(f"Raw result observation count: {result.raw_result_observation_count}")
    print(f"Screening plan count: {result.screening_plan_count}")
    print(f"Screening execution count: {result.screening_execution_count}")
    print(f"Screening field count: {result.screening_field_count}")
    print(f"Inclusion criteria count: {result.inclusion_criteria_count}")
    print(f"Exclusion criteria count: {result.exclusion_criteria_count}")
    print(f"Screening step count: {result.screening_step_count}")
    print(f"Screening recommendation value count: {result.screening_recommendation_value_count}")
    print(f"Screening row count: {result.screening_row_count}")
    print(f"Screening gate count: {result.screening_gate_count}")
    print(f"Screened result count: {result.screened_result_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
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
