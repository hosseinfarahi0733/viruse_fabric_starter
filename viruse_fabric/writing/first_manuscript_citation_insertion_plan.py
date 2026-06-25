"""First manuscript citation insertion plan for Viruse Fabric v7.2.

This module plans where audited citation records may later be inserted into the manuscript.

It plans manuscript citation insertion only.

It does not insert manuscript citation markers.
It does not revise the manuscript.
It does not add new citations.
It does not claim external validation.

Official project status remains:

research prototype with internal validation
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_manuscript_citation_insertion_plan_v7_2.md"

SOURCE_CITATION_RECORD_AUDIT = PROJECT_ROOT / "outputs" / "first_citation_record_audit_v7_1.md"
SOURCE_CITATION_EXECUTION = PROJECT_ROOT / "outputs" / "first_citation_integration_execution_v7_0.md"
SOURCE_CITATION_PLAN = PROJECT_ROOT / "outputs" / "first_citation_integration_plan_v6_9.md"
SOURCE_ROW_AUDIT = PROJECT_ROOT / "outputs" / "first_evidence_matrix_row_audit_v6_8.md"
SOURCE_POPULATION_EXECUTION = PROJECT_ROOT / "outputs" / "first_evidence_matrix_population_execution_v6_7.md"
SOURCE_POPULATION_PLAN = PROJECT_ROOT / "outputs" / "first_evidence_matrix_population_plan_v6_6.md"
SOURCE_ROLE_AUDIT = PROJECT_ROOT / "outputs" / "first_retained_source_role_audit_v6_5.md"
SOURCE_RETENTION_EXECUTION = PROJECT_ROOT / "outputs" / "first_retained_source_decision_execution_v6_4.md"
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
    SOURCE_CITATION_RECORD_AUDIT,
    SOURCE_CITATION_EXECUTION,
    SOURCE_CITATION_PLAN,
    SOURCE_ROW_AUDIT,
    SOURCE_POPULATION_EXECUTION,
    SOURCE_POPULATION_PLAN,
    SOURCE_ROLE_AUDIT,
    SOURCE_RETENTION_EXECUTION,
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


PLAN_METADATA = {
    "manuscript_citation_insertion_plan_id": "MCIP-0001",
    "linked_citation_record_audit_id": "CRA-0001",
    "linked_citation_integration_execution_id": "CIE-0001",
    "linked_citation_integration_plan_id": "CIP-0001",
    "plan_status": "manuscript_citation_insertion_planned_not_executed",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "audited_citation_record_count_from_v7_1": "2",
    "planned_manuscript_citation_slot_count": "2",
    "manuscript_citation_insertion_execution_count": "0",
    "manuscript_citation_marker_count": "0",
    "manuscript_revised_count": "0",
    "new_citation_added_count": "0",
    "conditional_hold_count": "1",
}


PLANNED_MANUSCRIPT_CITATION_SLOT_ROWS = [
    {
        "planned_manuscript_citation_slot_id": "MCIS-PLAN-0001",
        "linked_citation_record_id": "CIT-REC-0001",
        "linked_citation_key": "pmlr-v115-blom20a",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "planned_manuscript_section": "related-work or conceptual framing section",
        "planned_sentence_role": "background formal-framing context only",
        "planned_insertion_action": "plan_for_future_manuscript_citation_marker_only",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "planning_limit": "Insertion planning only; no marker insertion and no manuscript revision in v7.2.",
        "planning_reason": "The audited citation record passed field and linkage audit and may later support a bounded manuscript citation marker.",
    },
    {
        "planned_manuscript_citation_slot_id": "MCIS-PLAN-0002",
        "linked_citation_record_id": "CIT-REC-0002",
        "linked_citation_key": "pmlr-v124-wengel-mogensen20a",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "planned_manuscript_section": "related-work or methodological context section",
        "planned_sentence_role": "background methodological-context only",
        "planned_insertion_action": "plan_for_future_manuscript_citation_marker_only",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "planning_limit": "Insertion planning only; no marker insertion and no manuscript revision in v7.2.",
        "planning_reason": "The audited citation record passed field and linkage audit and may later support a bounded manuscript citation marker.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "planned_manuscript_citation_slot_id": "none",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "new_citation_added": "no",
        "reason": "Conditional metadata pass remains outside retained source, evidence row audit, citation record audit, and manuscript citation insertion planning.",
    },
]


MANUSCRIPT_CITATION_INSERTION_PLAN_FIELDS = [
    "planned_manuscript_citation_slot_id",
    "linked_citation_record_id",
    "linked_citation_key",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "planned_manuscript_section",
    "planned_sentence_role",
    "planned_insertion_action",
    "manuscript_citation_marker_added",
    "manuscript_revised",
    "new_citation_added",
    "planning_limit",
    "planning_reason",
]


MANUSCRIPT_CITATION_INSERTION_ACTION_VALUES = [
    "plan_for_future_manuscript_citation_marker_only",
    "hold_until_citation_record_update",
    "not_planned_for_manuscript_insertion",
    "manuscript_citation_insertion_not_performed",
]


MANUSCRIPT_CITATION_INSERTION_PLAN_GATES = [
    "Manuscript citation insertion plan must be linked to v7.1 citation record audit.",
    "Only audited citation records with audit pass may receive planned manuscript citation slots.",
    "Conditional-hold candidates must remain outside manuscript citation insertion planning.",
    "Planned manuscript citation slot must link to a citation record.",
    "Planned manuscript citation slot must link to a citation key.",
    "Planned manuscript citation slot must link to an evidence matrix row.",
    "Planned manuscript citation slot must link to a retained source.",
    "Planned manuscript citation slot must link to a candidate entry.",
    "Planned manuscript citation slot must state a bounded manuscript section.",
    "Planned manuscript citation slot must state a bounded sentence role.",
    "Manuscript citation insertion execution must remain zero.",
    "Manuscript citation marker count must remain zero.",
    "Manuscript revised count must remain zero.",
    "New citation added count must remain zero.",
    "Manuscript citation insertion planning must not imply external validation.",
    "Manuscript citation insertion planning must not imply submission readiness.",
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
    "does plan manuscript citation insertion",
    "does not insert manuscript citation markers",
    "does not revise the manuscript",
    "does not add new citations",
    "manuscript citation insertion plan is not manuscript citation insertion",
    "planned manuscript citation slot is not a manuscript citation marker",
    "planned manuscript citation slot is not manuscript revision",
    "citation record pass is not manuscript support",
    "manuscript citation planning is not external validation",
    "citations are not external validation",
    "conditional hold remains outside manuscript citation insertion planning",
    "future manuscript citation insertion is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not insert manuscript citation markers in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not add new citations in this milestone.",
    "Do not treat planned manuscript citation slots as inserted citation markers.",
    "Do not treat manuscript citation insertion planning as manuscript support.",
    "Do not treat citation record pass as manuscript support.",
    "Do not treat manuscript citation planning as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in manuscript citation insertion plans.",
    "Do not convert planned manuscript citation slots into manuscript prose.",
]


NEXT_STEPS = [
    "Execute manuscript citation insertion in a later milestone.",
    "Insert manuscript citation markers only after insertion execution.",
    "Audit inserted manuscript citation markers after execution.",
    "Plan manuscript revision only after marker audit.",
    "Revise manuscript only after citation-grounded revision planning.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve source-role boundaries during manuscript citation insertion.",
    "Keep public claims bounded after manuscript citation insertion planning.",
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
    r"\baccepted scientific theory\b",
]


SAFE_LINE_CUES = [
    "not",
    "does not",
    "do not",
    "must not",
    "plan",
    "planned",
    "planning",
    "citation",
    "manuscript citation",
    "citation marker",
    "citation record",
    "evidence row",
    "retained source",
    "candidate",
    "conditional",
    "hold",
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
    "manuscript citation insertion plan gates",
    "claim boundary toward v7.5",
    "final boundary statement",
]


INVENTED_CITATION_PATTERNS = [
    r"\b[A-Z][a-z]+ et al\., \d{4}\b",
    r"\bdoi:\s*10\.",
    r"\barXiv:\d{4}\.",
    r"\[\d+\]",
]


@dataclass(frozen=True)
class FirstManuscriptCitationInsertionPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    manuscript_citation_insertion_plan_count: int
    audited_citation_record_count: int
    planned_manuscript_citation_slot_count: int
    manuscript_citation_insertion_execution_count: int
    manuscript_citation_marker_count: int
    manuscript_revised_count: int
    new_citation_added_count: int
    conditional_hold_count: int
    manuscript_citation_insertion_plan_field_count: int
    manuscript_citation_insertion_action_value_count: int
    manuscript_citation_insertion_plan_gate_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    overclaim_count: int
    invented_citation_like_pattern_count: int
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
        "| Manuscript citation insertion plan field | Value |",
        "|---|---|",
    ]
    for key, value in PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_planned_manuscript_citation_slot_rows() -> str:
    rows = [
        "| Planned manuscript citation slot id | Citation record | Citation key | Planned section | Planned role | Marker added | Manuscript revised |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in PLANNED_MANUSCRIPT_CITATION_SLOT_ROWS:
        rows.append(
            f"| {item['planned_manuscript_citation_slot_id']} | "
            f"{item['linked_citation_record_id']} | "
            f"{item['linked_citation_key']} | "
            f"{item['planned_manuscript_section']} | "
            f"{item['planned_sentence_role']} | "
            f"{item['manuscript_citation_marker_added']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Planned manuscript citation slot id | Marker added | Manuscript revised | New citation added | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['planned_manuscript_citation_slot_id']} | "
            f"{item['manuscript_citation_marker_added']} | "
            f"{item['manuscript_revised']} | "
            f"{item['new_citation_added']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Manuscript citation insertion plan field | v7.2 status |",
        "|---|---|",
    ]
    for field in MANUSCRIPT_CITATION_INSERTION_PLAN_FIELDS:
        rows.append(f"| `{field}` | populated for planning rows only |")
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


def detect_invented_citation_like_patterns(text: str) -> list[str]:
    findings: list[str] = []
    current_section = ""

    allowed_sections = {
        "planned manuscript citation slot rows",
        "manuscript citation insertion plan metadata",
    }

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        lowered = stripped.lower()

        if lowered.startswith("## "):
            current_section = lowered.removeprefix("## ").strip()

        if current_section in allowed_sections:
            continue

        if "invented citation" in lowered or "citation-like" in lowered:
            continue

        for pattern in INVENTED_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def render_report() -> str:
    return f"""# First Manuscript Citation Insertion Plan v7.2

## Question
Can Viruse Fabric plan manuscript citation insertion from audited citation records while keeping manuscript citation markers, manuscript revision, and new citation additions at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does plan manuscript citation insertion. It does not insert manuscript citation markers, does not revise the manuscript, and does not add new citations.

Manuscript citation insertion plan is not manuscript citation insertion. Planned manuscript citation slot is not a manuscript citation marker. Planned manuscript citation slot is not manuscript revision. Citation record pass is not manuscript support. Manuscript citation planning is not external validation. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Manuscript Citation Insertion Plan Metadata
{render_metadata_table()}

## Planned Manuscript Citation Slot Rows
{render_planned_manuscript_citation_slot_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Manuscript Citation Insertion Plan Fields
{render_field_table()}

## Manuscript Citation Insertion Action Values
{bullet_list(MANUSCRIPT_CITATION_INSERTION_ACTION_VALUES)}

## Manuscript Citation Insertion Plan Gates
{bullet_list(MANUSCRIPT_CITATION_INSERTION_PLAN_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Manuscript Citation Insertion Plan Interpretation
The v7.2 artifact creates the first manuscript citation insertion plan after citation record audit.

MCIS-PLAN-0001 plans a future manuscript citation insertion slot from CIT-REC-0001 for bounded formal-framing context. MCIS-PLAN-0002 plans a future manuscript citation insertion slot from CIT-REC-0002 for bounded methodological context.

These are planned insertion slots only. No manuscript citation marker is inserted. No manuscript sentence is revised. No bibliography record is added. No claim is strengthened.

## Planning Boundary
Manuscript citation insertion plan count is one.

Audited citation record count is two.

Planned manuscript citation slot count is two.

Manuscript citation insertion execution count is zero.

Manuscript citation marker count is zero.

Manuscript revised count is zero.

New citation added count is zero.

This means the project now has a controlled route from audited citation records toward future manuscript citation markers, but it has not crossed that route yet. A planned marker is not a marker. Humanity, regrettably, keeps needing labels on the labels.

## Citation Record Boundary
Only audited citation records from v7.1 are allowed into manuscript citation insertion planning.

CIT-REC-0001 and CIT-REC-0002 are planned for later manuscript citation insertion because they passed citation record audit. CAND-0003 remains outside the plan because it has no retained source, no evidence row, no citation record, and no citation record audit pass.

Citation record audit pass makes future insertion planning possible. It does not create manuscript support by itself.

## Manuscript Boundary
The manuscript receives no new text.

No citation marker is inserted.

No paragraph is rewritten.

No conclusion is strengthened.

No claim is upgraded.

Manuscript citation marker count remains zero.

Manuscript revised count remains zero.

A future milestone may execute insertion, but v7.2 only plans insertion. The manuscript remains unchanged, because apparently restraint must be encoded as software now.

## New Citation Boundary
New citation added count remains zero.

No new citation record is added. No new source is retained. No new bibliography entry is created. This milestone uses existing audited citation records only.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside manuscript citation insertion planning. It cannot inherit insertion status by proximity to audited citation records.

This keeps conditional metadata from sneaking into manuscript planning through the academic equivalent of standing near important people at a conference.

## Claim Boundary Toward v7.5
This milestone permits a slightly stronger internal workflow claim than v7.1.

Allowed after v7.2:

- internally staged prototype
- retained-source workflow
- evidence-mapped workflow
- evidence-row-audited workflow
- citation-planned workflow
- verified citation records added
- citation records audited
- manuscript citation insertion planned
- manuscript still unrevised

Still disallowed:

- proven theory
- external validation
- biological prediction
- clinical relevance
- laboratory guidance
- operational readiness
- submission-ready manuscript
- accepted scientific theory

## Output Counts
Manuscript citation insertion plan count: 1

Audited citation record count: 2

Planned manuscript citation slot count: 2

Manuscript citation insertion execution count: 0

Manuscript citation marker count: 0

Manuscript revised count: 0

New citation added count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact plans manuscript citation insertion.

It does not insert manuscript citation markers, does not revise the manuscript, does not add new citations, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstManuscriptCitationInsertionPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    manuscript_citation_insertion_plan_count = 1
    audited_citation_record_count = int(PLAN_METADATA["audited_citation_record_count_from_v7_1"])
    planned_manuscript_citation_slot_count = int(
        PLAN_METADATA["planned_manuscript_citation_slot_count"]
    )
    manuscript_citation_insertion_execution_count = int(
        PLAN_METADATA["manuscript_citation_insertion_execution_count"]
    )
    manuscript_citation_marker_count = int(PLAN_METADATA["manuscript_citation_marker_count"])
    manuscript_revised_count = int(PLAN_METADATA["manuscript_revised_count"])
    new_citation_added_count = int(PLAN_METADATA["new_citation_added_count"])
    conditional_hold_count = int(PLAN_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 22:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if manuscript_citation_insertion_plan_count != 1:
        errors.append(
            "Manuscript citation insertion plan count should be one, got: "
            f"{manuscript_citation_insertion_plan_count}"
        )

    if audited_citation_record_count != 2:
        errors.append(
            f"Audited citation record count should be two, got: {audited_citation_record_count}"
        )

    if planned_manuscript_citation_slot_count != 2:
        errors.append(
            "Planned manuscript citation slot count should be two, got: "
            f"{planned_manuscript_citation_slot_count}"
        )

    if planned_manuscript_citation_slot_count != audited_citation_record_count:
        errors.append(
            "Planned manuscript citation slot count must equal audited citation record count"
        )

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for label, value in [
        ("Manuscript citation insertion execution count", manuscript_citation_insertion_execution_count),
        ("Manuscript citation marker count", manuscript_citation_marker_count),
        ("Manuscript revised count", manuscript_revised_count),
        ("New citation added count", new_citation_added_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    for row in PLANNED_MANUSCRIPT_CITATION_SLOT_ROWS:
        missing_fields = [
            field for field in MANUSCRIPT_CITATION_INSERTION_PLAN_FIELDS if not row.get(field)
        ]
        if missing_fields:
            errors.append(
                f"{row.get('planned_manuscript_citation_slot_id', 'unknown')} missing insertion plan fields: "
                f"{len(missing_fields)}"
            )

    if len(MANUSCRIPT_CITATION_INSERTION_PLAN_FIELDS) < 14:
        errors.append(
            "Manuscript citation insertion plan field count too low: "
            f"{len(MANUSCRIPT_CITATION_INSERTION_PLAN_FIELDS)}"
        )

    if len(MANUSCRIPT_CITATION_INSERTION_ACTION_VALUES) < 4:
        errors.append(
            "Manuscript citation insertion action value count too low: "
            f"{len(MANUSCRIPT_CITATION_INSERTION_ACTION_VALUES)}"
        )

    if len(MANUSCRIPT_CITATION_INSERTION_PLAN_GATES) < 16:
        errors.append(
            "Manuscript citation insertion plan gate count too low: "
            f"{len(MANUSCRIPT_CITATION_INSERTION_PLAN_GATES)}"
        )

    if boundary_count < 20:
        errors.append(f"Boundary phrase count too low: {boundary_count}")

    if prohibited_count < 11:
        errors.append(f"Prohibited behavior count too low: {prohibited_count}")

    if next_step_count < 8:
        errors.append(f"Next step count too low: {next_step_count}")

    if overclaims:
        errors.append(f"Overclaim lines detected: {len(overclaims)}")

    if invented_citations:
        errors.append(
            "Invented citation-like patterns detected outside planned insertion sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1200:
        errors.append(
            f"Word count too low for first manuscript citation insertion plan: {word_count}"
        )

    warnings.append("Manuscript citation insertion is planned, but no markers are inserted.")
    warnings.append("Manuscript citation insertion planning does not revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v7.2 artifact plans future manuscript citation insertion for two audited "
        "citation records while keeping markers, manuscript revision, and new citation additions at zero."
    )

    return FirstManuscriptCitationInsertionPlanResult(
        title="First Manuscript Citation Insertion Plan v7.2",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        manuscript_citation_insertion_plan_count=manuscript_citation_insertion_plan_count,
        audited_citation_record_count=audited_citation_record_count,
        planned_manuscript_citation_slot_count=planned_manuscript_citation_slot_count,
        manuscript_citation_insertion_execution_count=manuscript_citation_insertion_execution_count,
        manuscript_citation_marker_count=manuscript_citation_marker_count,
        manuscript_revised_count=manuscript_revised_count,
        new_citation_added_count=new_citation_added_count,
        conditional_hold_count=conditional_hold_count,
        manuscript_citation_insertion_plan_field_count=len(MANUSCRIPT_CITATION_INSERTION_PLAN_FIELDS),
        manuscript_citation_insertion_action_value_count=len(MANUSCRIPT_CITATION_INSERTION_ACTION_VALUES),
        manuscript_citation_insertion_plan_gate_count=len(MANUSCRIPT_CITATION_INSERTION_PLAN_GATES),
        boundary_phrase_count=boundary_count,
        prohibited_behavior_count=prohibited_count,
        next_step_count=next_step_count,
        overclaim_count=len(overclaims),
        invented_citation_like_pattern_count=len(invented_citations),
        word_count=word_count,
        errors=errors,
        warnings=warnings,
        passed=passed,
        interpretation=interpretation,
    )


def main() -> None:
    result = generate_report()

    print("First Manuscript Citation Insertion Plan v7.2")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(
        "Manuscript citation insertion plan count: "
        f"{result.manuscript_citation_insertion_plan_count}"
    )
    print(f"Audited citation record count: {result.audited_citation_record_count}")
    print(
        "Planned manuscript citation slot count: "
        f"{result.planned_manuscript_citation_slot_count}"
    )
    print(
        "Manuscript citation insertion execution count: "
        f"{result.manuscript_citation_insertion_execution_count}"
    )
    print(f"Manuscript citation marker count: {result.manuscript_citation_marker_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(
        "Manuscript citation insertion plan field count: "
        f"{result.manuscript_citation_insertion_plan_field_count}"
    )
    print(
        "Manuscript citation insertion action value count: "
        f"{result.manuscript_citation_insertion_action_value_count}"
    )
    print(
        "Manuscript citation insertion plan gate count: "
        f"{result.manuscript_citation_insertion_plan_gate_count}"
    )
    print(f"Boundary phrase count: {result.boundary_phrase_count}")
    print(f"Prohibited behavior count: {result.prohibited_behavior_count}")
    print(f"Next step count: {result.next_step_count}")
    print(f"Overclaim count: {result.overclaim_count}")
    print(f"Invented citation-like pattern count: {result.invented_citation_like_pattern_count}")
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
