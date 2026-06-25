"""First retained source decision execution for Viruse Fabric v6.4.

This module executes the first retained-source decision after the v6.3 retained
source decision plan.

It creates retained source records only.

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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_retained_source_decision_execution_v6_4.md"

SOURCE_RETENTION_PLAN = PROJECT_ROOT / "outputs" / "first_retained_source_decision_plan_v6_3.md"
SOURCE_METADATA_AUDIT = PROJECT_ROOT / "outputs" / "candidate_source_metadata_audit_v6_2.md"
SOURCE_CANDIDATE_CREATION = PROJECT_ROOT / "outputs" / "first_candidate_source_entry_creation_v6_1.md"
SOURCE_ENTRY_PLAN = PROJECT_ROOT / "outputs" / "first_candidate_source_entry_plan_v6_0.md"
SOURCE_SCREENING_EXECUTION = PROJECT_ROOT / "outputs" / "first_raw_result_screening_execution_v5_9.md"
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
    SOURCE_RETENTION_PLAN,
    SOURCE_METADATA_AUDIT,
    SOURCE_CANDIDATE_CREATION,
    SOURCE_ENTRY_PLAN,
    SOURCE_SCREENING_EXECUTION,
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


EXECUTION_METADATA = {
    "retained_source_decision_execution_id": "RDE-0001",
    "linked_retained_source_decision_plan_id": "RDP-0001",
    "linked_candidate_metadata_audit_id": "CMA-0001",
    "linked_candidate_entry_creation_id": "CEC-0001",
    "execution_status": "retained_sources_created_no_citations",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "candidate_source_count_from_v6_3": "3",
    "planned_retention_candidate_count_from_v6_3": "2",
    "conditional_hold_count_from_v6_3": "1",
    "retention_decision_execution_count": "1",
    "retained_source_count": "2",
    "citation_added_count": "0",
}


RETAINED_SOURCE_RECORDS = [
    {
        "retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "linked_raw_result_observation_id": "raw_result_observation_02",
        "source_title": "Beyond Structural Causal Models: Causal Constraints Models",
        "author_information": "Tineke Blom; Stephan Bongers; Joris M. Mooij",
        "venue_or_repository": "Proceedings of Machine Learning Research",
        "publication_context": "UAI proceedings record",
        "publication_year_or_access_date": "2020 PMLR proceedings record; earlier arXiv record also exists",
        "stable_access_route": "https://proceedings.mlr.press/v115/blom20a.html",
        "source_type": "conference_paper_with_preprint_record",
        "retention_decision": "retain_for_formal_framing_review",
        "retention_rationale": "The source directly addresses causal constraints models and dynamical systems at equilibrium.",
        "bounded_source_role": "formal_framing_candidate_for_future_evidence_matrix",
        "retention_limit": "Retained source only; not a citation and not manuscript support in this milestone.",
        "citation_added": "no",
        "evidence_matrix_populated": "no",
        "manuscript_revised": "no",
    },
    {
        "retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "linked_raw_result_observation_id": "raw_result_observation_03",
        "source_title": "Causal screening in dynamical systems",
        "author_information": "Søren Wengel Mogensen",
        "venue_or_repository": "Proceedings of Machine Learning Research",
        "publication_context": "UAI proceedings record",
        "publication_year_or_access_date": "2020",
        "stable_access_route": "https://proceedings.mlr.press/v124/wengel-mogensen20a.html",
        "source_type": "conference_paper",
        "retention_decision": "retain_for_methodological_context_review",
        "retention_rationale": "The source directly addresses causal screening methods in dynamical systems.",
        "bounded_source_role": "methodological_context_candidate_for_future_evidence_matrix",
        "retention_limit": "Retained source only; not a citation and not manuscript support in this milestone.",
        "citation_added": "no",
        "evidence_matrix_populated": "no",
        "manuscript_revised": "no",
    },
]


CONDITIONAL_HOLD_RECORDS = [
    {
        "candidate_entry_id": "CAND-0003",
        "source_title": "Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis",
        "metadata_audit_decision": "metadata_conditional_pass_not_retained",
        "hold_status": "hold_for_update_before_retention_decision",
        "retained_source_created": "no",
        "reason": "Conditional metadata pass requires update handling before retention decision.",
    },
]


RETAINED_SOURCE_FIELDS = [
    "retained_source_id",
    "linked_candidate_entry_id",
    "linked_raw_result_observation_id",
    "source_title",
    "author_information",
    "venue_or_repository",
    "publication_context",
    "publication_year_or_access_date",
    "stable_access_route",
    "source_type",
    "retention_decision",
    "retention_rationale",
    "bounded_source_role",
    "retention_limit",
    "citation_added",
    "evidence_matrix_populated",
    "manuscript_revised",
]


RETENTION_EXECUTION_GATES = [
    "Retention execution must be linked to the v6.3 retention plan.",
    "Retention execution must be linked to the v6.2 metadata audit.",
    "Only metadata-pass candidates may be retained in this milestone.",
    "Conditional metadata-pass candidates must remain on hold.",
    "Retained source records must link back to candidate entries.",
    "Retained source records must link back to raw observations.",
    "Retained source records must include bounded source roles.",
    "Retained source records must include retention limits.",
    "Retained source records must not become citations.",
    "Retained source records must not populate the evidence matrix.",
    "Retained source records must not revise the manuscript.",
    "Retention execution must not imply external validation.",
    "Retention execution must not imply submission readiness.",
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
    "does create retained source records",
    "retained source records are not citations",
    "retained source records are not evidence matrix population",
    "retained source records are not manuscript revision",
    "retained sources are not citations",
    "citations are not external validation",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
    "does not certify external validation",
]


PROHIBITED_BEHAVIORS = [
    "Do not add citations in this milestone.",
    "Do not populate the evidence matrix in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat retained source records as citations.",
    "Do not treat retained source records as evidence matrix rows.",
    "Do not treat retained source records as manuscript support.",
    "Do not treat retention as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not retain conditional-hold sources in this milestone.",
    "Do not convert retained source records into citation text.",
]


NEXT_STEPS = [
    "Audit retained source roles in a later milestone.",
    "Create an evidence matrix population plan after retained-source audit.",
    "Populate evidence matrix only after retained-source role audit.",
    "Add citations only after retained-source decision and citation integration plan.",
    "Revise manuscript only after citation-grounded integration.",
    "Keep conditional-hold candidate outside retention until update handling.",
    "Preserve retained-source boundary during public communication.",
    "Avoid external validation language after retention execution.",
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
    "retained source",
    "retention",
    "candidate",
    "conditional",
    "hold",
    "citation",
    "evidence matrix",
    "manuscript",
    "zero",
    "future",
    "audit",
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
    "retention execution gates",
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
class FirstRetainedSourceDecisionExecutionResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    retention_decision_execution_count: int
    candidate_source_count: int
    retained_source_count: int
    conditional_hold_count: int
    source_added_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
    retained_source_field_count: int
    retention_execution_gate_count: int
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
        "| Retention execution field | Value |",
        "|---|---|",
    ]
    for key, value in EXECUTION_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_retained_source_records() -> str:
    rows = [
        "| Retained source id | Candidate id | Title | Source role | Citation added | Evidence matrix populated | Manuscript revised |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in RETAINED_SOURCE_RECORDS:
        rows.append(
            f"| {item['retained_source_id']} | "
            f"{item['linked_candidate_entry_id']} | "
            f"{item['source_title']} | "
            f"{item['bounded_source_role']} | "
            f"{item['citation_added']} | "
            f"{item['evidence_matrix_populated']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_records() -> str:
    rows = [
        "| Candidate id | Title | Hold status | Retained source created | Reason |",
        "|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_RECORDS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['source_title']} | "
            f"{item['hold_status']} | "
            f"{item['retained_source_created']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Retained source field | v6.4 status |",
        "|---|---|",
    ]
    for field in RETAINED_SOURCE_FIELDS:
        rows.append(f"| `{field}` | populated for retained source records only |")
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
    return f"""# First Retained Source Decision Execution v6.4

## Question
Can Viruse Fabric execute the first retained-source decision for two metadata-pass candidate sources while keeping citations, evidence matrix population, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does create retained source records. It does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

Retained source records are not citations. Retained source records are not evidence matrix population. Retained source records are not manuscript revision. Retained sources are not citations. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Retention Decision Execution Metadata
{render_metadata_table()}

## Retained Source Records Created
{render_retained_source_records()}

## Conditional Hold Records
{render_conditional_hold_records()}

## Retained Source Fields
{render_field_table()}

## Retention Execution Gates
{bullet_list(RETENTION_EXECUTION_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Retention Execution Interpretation
The v6.4 artifact executes the first retained-source decision in the Viruse Fabric literature workflow.

Two candidate sources are retained because they passed metadata audit and were planned for future retention decision in v6.3. One conditional candidate remains on hold because v6.2 marked it as conditional and v6.3 kept it outside immediate retention planning.

This is the first milestone where retained source count is intentionally nonzero. That is progress, but it is not citation integration. A retained source is a controlled record that may later be considered for evidence matrix population. It is not automatically a manuscript citation and it is not external validation.

## Retained Source Boundary
Retained source count is two.

The retained records preserve links to candidate entries, raw observations, source metadata, bounded roles, and retention limits. Those records are now available for later retained-source role audit or evidence matrix planning. They are not used as manuscript support here.

The conditional hold record remains outside retention. It is not rejected, but it is also not retained. It needs update handling before any future retention decision. Apparently a middle state is possible; someone alert bureaucracy.

## Citation Boundary
Citation added count remains zero.

No citation text is created. No bibliography entry is added to the manuscript. No citation slot is filled. Retained source records remain internal workflow records only.

This boundary matters because retention is still weaker than citation use. A retained source can be appropriate for future evidence mapping and still not be ready to support a manuscript claim. The retained-source layer is a staging area, not a victory parade.

## Evidence Boundary
Evidence matrix populated count remains zero.

Manuscript revised count remains zero.

The evidence matrix receives no rows from this milestone. The manuscript receives no new support. No project claim is strengthened by this artifact. The only change is that two candidate source records become retained source records for future audited handling.

## Retention Consequence Boundary
The retained-source layer now has two records, but the evidence layer still has zero new entries.

RET-0001 and RET-0002 can be audited later for role quality, claim alignment, and evidence-matrix placement. They are not inserted into the evidence matrix here. They are not used to strengthen any manuscript sentence. They are not converted into references, footnotes, bibliography entries, or claim-support language.

This matters because a retained source is still only an internal workflow object. It says that the source survived candidate review and retention decision. It does not say that the source has already been mapped to a claim, quoted, cited, or integrated into the manuscript.

The workflow therefore has four separate states: candidate source, retained source, evidence-matrix source, and manuscript citation. This milestone moves two records from candidate source to retained source only.

## Conditional Hold Boundary
CAND-0003 remains outside the retained-source set.

The conditional hold is not a hidden rejection and not a hidden acceptance. It is a tracked waiting state. The source may be reconsidered after update handling, but it is not retained in this milestone and cannot silently appear in later citation or evidence work without a separate retained-source decision.

This prevents the classic paperwork hallucination where a maybe becomes a yes because nobody wanted to read the row label. Civilization trembles, but the table survives.

## Output Counts
Retention decision execution count: 1

Candidate source count: 3

Retained source count: 2

Conditional hold count: 1

Source added count: 2

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact creates first retained source records.

It does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstRetainedSourceDecisionExecutionResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    retention_decision_execution_count = int(EXECUTION_METADATA["retention_decision_execution_count"])
    candidate_source_count = int(EXECUTION_METADATA["candidate_source_count_from_v6_3"])
    retained_source_count = len(RETAINED_SOURCE_RECORDS)
    conditional_hold_count = len(CONDITIONAL_HOLD_RECORDS)
    source_added_count = retained_source_count
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 14:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if retention_decision_execution_count != 1:
        errors.append(
            "Retention decision execution count should be one, got: "
            f"{retention_decision_execution_count}"
        )

    if candidate_source_count != 3:
        errors.append(f"Candidate source count should be three, got: {candidate_source_count}")

    if retained_source_count != 2:
        errors.append(f"Retained source count should be two, got: {retained_source_count}")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    if retained_source_count + conditional_hold_count != candidate_source_count:
        errors.append("Retained source and hold counts do not sum to candidate source count")

    if source_added_count != 2:
        errors.append(f"Source added count should be two retained records, got: {source_added_count}")

    for entry in RETAINED_SOURCE_RECORDS:
        missing_fields = [field for field in RETAINED_SOURCE_FIELDS if not entry.get(field)]
        if missing_fields:
            errors.append(
                f"{entry.get('retained_source_id', 'unknown')} missing fields: {len(missing_fields)}"
            )

    if len(RETAINED_SOURCE_FIELDS) < 17:
        errors.append(f"Retained source field count too low: {len(RETAINED_SOURCE_FIELDS)}")

    if len(RETENTION_EXECUTION_GATES) < 13:
        errors.append(f"Retention execution gate count too low: {len(RETENTION_EXECUTION_GATES)}")

    for label, value in [
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if boundary_count < 18:
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
        errors.append(f"Word count too low for first retained source decision execution: {word_count}")

    warnings.append("Retained source records are created, but no citations are added.")
    warnings.append("Retention execution does not populate evidence rows or revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v6.4 artifact creates two retained source records from metadata-pass candidates "
        "while keeping citations, evidence matrix population, and manuscript revision at zero."
    )

    return FirstRetainedSourceDecisionExecutionResult(
        title="First Retained Source Decision Execution v6.4",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        retention_decision_execution_count=retention_decision_execution_count,
        candidate_source_count=candidate_source_count,
        retained_source_count=retained_source_count,
        conditional_hold_count=conditional_hold_count,
        source_added_count=source_added_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
        retained_source_field_count=len(RETAINED_SOURCE_FIELDS),
        retention_execution_gate_count=len(RETENTION_EXECUTION_GATES),
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

    print("First Retained Source Decision Execution v6.4")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Retention decision execution count: {result.retention_decision_execution_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Source added count: {result.source_added_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Retained source field count: {result.retained_source_field_count}")
    print(f"Retention execution gate count: {result.retention_execution_gate_count}")
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
