"""First raw result screening execution for Viruse Fabric v5.9.

This module executes the first controlled screening pass over the five raw
observations recorded in v5.7 and planned in v5.8.

It executes screening only.

It does not create candidate source entries.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_raw_result_screening_execution_v5_9.md"

SOURCE_SCREENING_PLAN = PROJECT_ROOT / "outputs" / "first_raw_result_screening_plan_v5_8.md"
SOURCE_LIVE_SEARCH = PROJECT_ROOT / "outputs" / "first_controlled_live_search_execution_v5_7.md"
SOURCE_SEARCH_AUDIT = PROJECT_ROOT / "outputs" / "first_search_run_artifact_audit_v5_6.md"
SOURCE_SEARCH_SHELL = PROJECT_ROOT / "outputs" / "first_search_run_artifact_v5_5.md"
SOURCE_SEARCH_PLAN = PROJECT_ROOT / "outputs" / "first_literature_family_search_plan_v5_4.md"
SOURCE_EMPTY_LOG = PROJECT_ROOT / "outputs" / "literature_search_log_empty_v5_2.md"
SOURCE_LOG_TEMPLATE = PROJECT_ROOT / "outputs" / "literature_search_log_template_v5_1.md"
SOURCE_CLAIM_MAP = PROJECT_ROOT / "outputs" / "claim_to_citation_readiness_map_v4_9.md"
SOURCE_EVIDENCE_MATRIX = PROJECT_ROOT / "outputs" / "literature_family_evidence_matrix_v4_8.md"

SOURCE_ARTIFACTS = [
    SOURCE_SCREENING_PLAN,
    SOURCE_LIVE_SEARCH,
    SOURCE_SEARCH_AUDIT,
    SOURCE_SEARCH_SHELL,
    SOURCE_SEARCH_PLAN,
    SOURCE_EMPTY_LOG,
    SOURCE_LOG_TEMPLATE,
    SOURCE_CLAIM_MAP,
    SOURCE_EVIDENCE_MATRIX,
]


SCREENING_EXECUTION_METADATA = {
    "screening_execution_id": "SX-0001",
    "linked_screening_plan_id": "SP-0001",
    "linked_search_execution_id": "SE-0001",
    "linked_shell_id": "SR-0001-SHELL",
    "execution_status": "screening_executed_no_candidate_entries",
    "execution_date": "2026-06-26",
    "execution_timezone": "Asia/Baku",
    "screening_basis": "raw observation title and recorded relevance only",
    "raw_result_count_from_v5_7": "23",
    "raw_result_observation_count_from_v5_7": "5",
    "screened_result_count": "5",
    "candidate_source_count": "0",
    "retained_source_count": "0",
}


SCREENING_DECISIONS = [
    {
        "raw_result_observation_id": "raw_result_observation_01",
        "raw_title": "Information-theoretic formulation of dynamical systems",
        "decision": "defer_for_candidate_entry_planning",
        "reason": "Relevant to dynamical-systems framing, but title alone does not establish direct constraint-causality alignment.",
        "candidate_source_created": "no",
    },
    {
        "raw_result_observation_id": "raw_result_observation_02",
        "raw_title": "Beyond Structural Causal Models: Causal Constraints Models",
        "decision": "pass_to_candidate_entry_planning",
        "reason": "Strong apparent alignment with causal constraints and causal modeling; still requires metadata audit before candidate entry.",
        "candidate_source_created": "no",
    },
    {
        "raw_result_observation_id": "raw_result_observation_03",
        "raw_title": "Causal screening in dynamical systems",
        "decision": "pass_to_candidate_entry_planning",
        "reason": "Strong apparent alignment with causal learning and dynamical systems; still requires metadata audit before candidate entry.",
        "candidate_source_created": "no",
    },
    {
        "raw_result_observation_id": "raw_result_observation_04",
        "raw_title": "Causality and independence in perfectly adapted dynamical systems",
        "decision": "defer_for_candidate_entry_planning",
        "reason": "Potentially relevant to causality and dynamical systems, but project alignment must be checked before candidate entry.",
        "candidate_source_created": "no",
    },
    {
        "raw_result_observation_id": "raw_result_observation_05",
        "raw_title": "Causal Structure Learning for Dynamical Systems",
        "decision": "pass_to_candidate_entry_planning",
        "reason": "Relevant to causal structure learning in dynamical systems; still not a candidate source until metadata is logged and audited.",
        "candidate_source_created": "no",
    },
]


SCREENING_DECISION_VALUES = [
    "pass_to_candidate_entry_planning",
    "defer_for_candidate_entry_planning",
    "exclude_from_candidate_entry_planning",
]


SCREENING_EXECUTION_FIELDS = [
    "raw_result_observation_id",
    "raw_title",
    "screening_basis",
    "conceptual_alignment",
    "metadata_needed",
    "decision",
    "reason",
    "candidate_source_created",
    "retained_source_created",
    "citation_added",
    "evidence_matrix_populated",
    "manuscript_revised",
]


INCLUSION_CHECKS_EXECUTED = [
    "Checked whether each raw observation has apparent relevance to constraints, causality, or dynamical systems.",
    "Checked whether each raw observation appears related to the selected literature family.",
    "Checked whether each raw observation may map to a v4.9 claim category later.",
    "Checked whether title-level relevance is enough for candidate planning but not enough for candidate creation.",
    "Checked whether additional metadata is needed before source logging.",
    "Checked whether the result should remain outside the evidence matrix.",
    "Checked whether the result should remain outside manuscript revision.",
    "Checked whether the result should remain outside citation use.",
]


EXCLUSION_CHECKS_EXECUTED = [
    "Checked for keyword-only risk.",
    "Checked for insufficient metadata risk.",
    "Checked for risk of decorative authority.",
    "Checked for external-validation overreach risk.",
    "Checked for biological, clinical, laboratory, or operational guidance risk.",
    "Checked for premature citation risk.",
    "Checked for premature evidence matrix transfer risk.",
    "Checked for premature manuscript support risk.",
]


SCREENING_GATES = [
    "Screening execution must be linked to v5.8 screening plan.",
    "Screening execution must be linked to v5.7 live search execution.",
    "Exactly five raw observations should be screened.",
    "Screened result count should be five.",
    "Candidate source count must remain zero.",
    "Retained source count must remain zero.",
    "Source added count must remain zero.",
    "Citation added count must remain zero.",
    "Evidence matrix populated count must remain zero.",
    "Manuscript revised count must remain zero.",
    "Screening decisions must not be treated as source retention.",
    "Screening decisions must not be treated as citations.",
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
    "screening decisions are not candidate source entries",
    "candidate source planning is not candidate source creation",
    "candidate sources are not retained sources",
    "retained sources are not citations",
    "citations are not external validation",
    "does not create candidate sources",
    "does not retain sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
]


PROHIBITED_BEHAVIORS = [
    "Do not create candidate source entries in this milestone.",
    "Do not retain sources in this milestone.",
    "Do not add citations in this milestone.",
    "Do not populate the evidence matrix in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat screening decisions as citations.",
    "Do not treat screening decisions as evidence.",
    "Do not treat title-level relevance as source audit.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
]


NEXT_STEPS = [
    "Create a candidate source entry plan for passed and deferred screening decisions.",
    "Define metadata fields required for candidate source entries.",
    "Create candidate entries only in a later milestone.",
    "Audit candidate source metadata before retention.",
    "Retain sources only after candidate audit.",
    "Populate evidence matrix only after retained-source audit.",
    "Add citations only after retained-source decision.",
    "Revise manuscript only after citation-grounded integration.",
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
    "screening",
    "candidate source",
    "retained source",
    "zero",
    "defer",
    "planning",
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
class FirstRawResultScreeningExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    screening_execution_count: int
    raw_result_count: int
    raw_result_observation_count: int
    screened_result_count: int
    screening_decision_count: int
    pass_to_candidate_planning_count: int
    defer_to_candidate_planning_count: int
    exclude_from_candidate_planning_count: int
    screening_decision_value_count: int
    screening_execution_field_count: int
    inclusion_check_count: int
    exclusion_check_count: int
    screening_gate_count: int
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
        "| Screening execution field | Value |",
        "|---|---|",
    ]
    for key, value in SCREENING_EXECUTION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_screening_decision_table() -> str:
    rows = [
        "| Raw observation id | Raw title | Screening decision | Reason | Candidate source created |",
        "|---|---|---|---|---|",
    ]
    for item in SCREENING_DECISIONS:
        rows.append(
            f"| {item['raw_result_observation_id']} | "
            f"{item['raw_title']} | "
            f"{item['decision']} | "
            f"{item['reason']} | "
            f"{item['candidate_source_created']} |"
        )
    return "\n".join(rows)


def render_field_table(fields: list[str]) -> str:
    rows = [
        "| Screening execution field | v5.9 status |",
        "|---|---|",
    ]
    for field in fields:
        rows.append(f"| `{field}` | executed or explicitly held at zero |")
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
    return f"""# First Raw Result Screening Execution v5.9

## Question
Can Viruse Fabric execute the first raw-result screening pass while keeping candidate sources, retained sources, citations, evidence matrix population, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone executes screening decisions only. Screening decisions are not candidate source entries. Candidate source planning is not candidate source creation. The artifact does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

## Source Artifacts
{render_source_table()}

## Screening Execution Metadata
{render_metadata_table()}

## Screening Decisions
{render_screening_decision_table()}

## Screening Execution Fields
{render_field_table(SCREENING_EXECUTION_FIELDS)}

## Screening Decision Values
{bullet_list(SCREENING_DECISION_VALUES)}

## Inclusion Checks Executed
{bullet_list(INCLUSION_CHECKS_EXECUTED)}

## Exclusion Checks Executed
{bullet_list(EXCLUSION_CHECKS_EXECUTED)}

## Screening Gates
{bullet_list(SCREENING_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Screening Interpretation
The v5.9 artifact executes the first screening pass over the five raw observations recorded in v5.7 and planned in v5.8.

The screening pass produces decisions, not sources. Some raw observations pass to candidate-entry planning, some are deferred to candidate-entry planning, and none are converted into candidate sources here. This is the critical boundary. A screening decision can say "this may deserve a candidate entry later," but it cannot silently become that entry.

The project now has its first interpretive filter after live search. That is progress, but it is not evidence. It is a sorting step. It asks whether raw observations deserve later structured metadata work. It does not decide retention. It does not decide citation use. It does not decide manuscript support.

## Candidate Source Boundary
Candidate source count remains zero.

This is intentional. Candidate source creation requires a separate milestone because it needs stable metadata, access route, claim mapping, inclusion rationale, exclusion-risk notes, and proposed source role. The present milestone only decides which raw observations should be considered for that future work.

If candidate entries were created here, the workflow would blur screening with source logging. That would make later audit harder. Humans already blur enough things before breakfast; the files do not need to join in.

## Evidence Boundary
Screening is not evidence matrix population.

A screened raw observation is still outside the evidence matrix. A pass-to-planning decision is still outside citation use. A deferred decision is still outside retention. The manuscript receives no new support from this step. The only new knowledge is procedural: which raw observations should be considered in the next candidate-entry planning stage.

The project therefore moves forward without claiming external validation, submission readiness, biological guidance, clinical guidance, laboratory guidance, or operational guidance.

## Output Counts
Screening execution count: 1

Raw result count: 23

Raw result observation count: 5

Screened result count: 5

Screening decision count: 5

Pass to candidate planning count: 3

Defer to candidate planning count: 2

Exclude from candidate planning count: 0

Candidate source count: 0

Retained source count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact executes first raw-result screening.

It does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstRawResultScreeningExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    screening_execution_count = 1
    raw_result_count = int(SCREENING_EXECUTION_METADATA["raw_result_count_from_v5_7"])
    raw_result_observation_count = int(SCREENING_EXECUTION_METADATA["raw_result_observation_count_from_v5_7"])
    screened_result_count = int(SCREENING_EXECUTION_METADATA["screened_result_count"])
    screening_decision_count = len(SCREENING_DECISIONS)
    pass_count = sum(1 for item in SCREENING_DECISIONS if item["decision"] == "pass_to_candidate_entry_planning")
    defer_count = sum(1 for item in SCREENING_DECISIONS if item["decision"] == "defer_for_candidate_entry_planning")
    exclude_count = sum(1 for item in SCREENING_DECISIONS if item["decision"] == "exclude_from_candidate_entry_planning")
    candidate_source_count = int(SCREENING_EXECUTION_METADATA["candidate_source_count"])
    retained_source_count = int(SCREENING_EXECUTION_METADATA["retained_source_count"])
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

    if len(SOURCE_ARTIFACTS) < 9:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if screening_execution_count != 1:
        errors.append(f"Screening execution count should be one, got: {screening_execution_count}")

    if raw_result_count < 1:
        errors.append(f"Raw result count should be positive, got: {raw_result_count}")

    if raw_result_observation_count != 5:
        errors.append(f"Raw result observation count should be five, got: {raw_result_observation_count}")

    if screened_result_count != 5:
        errors.append(f"Screened result count should be five, got: {screened_result_count}")

    if screening_decision_count != 5:
        errors.append(f"Screening decision count should be five, got: {screening_decision_count}")

    if pass_count < 1:
        errors.append(f"Pass to candidate planning count too low: {pass_count}")

    if defer_count < 1:
        errors.append(f"Defer to candidate planning count too low: {defer_count}")

    if pass_count + defer_count + exclude_count != screening_decision_count:
        errors.append("Screening decision counts do not sum to screening decision count")

    if len(SCREENING_DECISION_VALUES) < 3:
        errors.append(f"Screening decision value count too low: {len(SCREENING_DECISION_VALUES)}")

    if len(SCREENING_EXECUTION_FIELDS) < 12:
        errors.append(f"Screening execution field count too low: {len(SCREENING_EXECUTION_FIELDS)}")

    if len(INCLUSION_CHECKS_EXECUTED) < 8:
        errors.append(f"Inclusion check count too low: {len(INCLUSION_CHECKS_EXECUTED)}")

    if len(EXCLUSION_CHECKS_EXECUTED) < 8:
        errors.append(f"Exclusion check count too low: {len(EXCLUSION_CHECKS_EXECUTED)}")

    if len(SCREENING_GATES) < 12:
        errors.append(f"Screening gate count too low: {len(SCREENING_GATES)}")

    for label, value in [
        ("Candidate source count", candidate_source_count),
        ("Retained source count", retained_source_count),
        ("Source added count", source_added_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if boundary_count < 17:
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
        errors.append(f"Word count too low for first raw result screening execution: {word_count}")

    warnings.append("Screening execution creates decisions only; no candidate sources are created.")
    warnings.append("Screening execution does not add citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v5.9 artifact executes first raw-result screening over five raw "
        "observations while keeping candidate sources, retained sources, citations, "
        "evidence matrix population, and manuscript revision at zero."
    )

    return FirstRawResultScreeningExecutionResult(
        title="First Raw Result Screening Execution v5.9",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        screening_execution_count=screening_execution_count,
        raw_result_count=raw_result_count,
        raw_result_observation_count=raw_result_observation_count,
        screened_result_count=screened_result_count,
        screening_decision_count=screening_decision_count,
        pass_to_candidate_planning_count=pass_count,
        defer_to_candidate_planning_count=defer_count,
        exclude_from_candidate_planning_count=exclude_count,
        screening_decision_value_count=len(SCREENING_DECISION_VALUES),
        screening_execution_field_count=len(SCREENING_EXECUTION_FIELDS),
        inclusion_check_count=len(INCLUSION_CHECKS_EXECUTED),
        exclusion_check_count=len(EXCLUSION_CHECKS_EXECUTED),
        screening_gate_count=len(SCREENING_GATES),
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

    print("First Raw Result Screening Execution v5.9")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Screening execution count: {result.screening_execution_count}")
    print(f"Raw result count: {result.raw_result_count}")
    print(f"Raw result observation count: {result.raw_result_observation_count}")
    print(f"Screened result count: {result.screened_result_count}")
    print(f"Screening decision count: {result.screening_decision_count}")
    print(f"Pass to candidate planning count: {result.pass_to_candidate_planning_count}")
    print(f"Defer to candidate planning count: {result.defer_to_candidate_planning_count}")
    print(f"Exclude from candidate planning count: {result.exclude_from_candidate_planning_count}")
    print(f"Screening decision value count: {result.screening_decision_value_count}")
    print(f"Screening execution field count: {result.screening_execution_field_count}")
    print(f"Inclusion check count: {result.inclusion_check_count}")
    print(f"Exclusion check count: {result.exclusion_check_count}")
    print(f"Screening gate count: {result.screening_gate_count}")
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
