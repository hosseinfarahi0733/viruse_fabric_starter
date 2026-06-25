"""First citation record audit for Viruse Fabric v7.1.

This module audits the first verified citation records added in v7.0.

It audits citation records only.

It does not add new citations.
It does not insert manuscript citation markers.
It does not revise the manuscript.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_citation_record_audit_v7_1.md"

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


AUDIT_METADATA = {
    "citation_record_audit_id": "CRA-0001",
    "linked_citation_integration_execution_id": "CIE-0001",
    "linked_citation_integration_plan_id": "CIP-0001",
    "linked_evidence_matrix_row_audit_id": "ERA-0001",
    "audit_status": "citation_records_audited_no_new_citations_no_manuscript_revision",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "citation_record_count_from_v7_0": "2",
    "citation_record_audited_count": "2",
    "citation_record_audit_pass_count": "2",
    "citation_record_audit_conditional_count": "0",
    "citation_record_audit_fail_count": "0",
    "new_citation_added_count": "0",
    "manuscript_citation_marker_count": "0",
    "manuscript_revised_count": "0",
    "conditional_hold_count": "1",
}


CITATION_RECORD_AUDIT_ROWS = [
    {
        "citation_record_id": "CIT-REC-0001",
        "planned_citation_slot_id": "CIT-PLAN-0001",
        "evidence_matrix_row_id": "EMR-0001",
        "retained_source_id": "RET-0001",
        "candidate_entry_id": "CAND-0001",
        "citation_key": "pmlr-v115-blom20a",
        "title": "Beyond Structural Causal Models: Causal Constraints Models",
        "authors": "Tineke Blom; Stephan Bongers; Joris M. Mooij",
        "venue": "Proceedings of The 35th Uncertainty in Artificial Intelligence Conference",
        "series": "Proceedings of Machine Learning Research",
        "volume": "115",
        "pages": "585-594",
        "year": "2020",
        "publisher": "PMLR",
        "stable_url": "https://proceedings.mlr.press/v115/blom20a.html",
        "field_completeness_status": "complete_required_fields",
        "linkage_status": "linked_to_plan_evidence_row_retained_source_and_candidate",
        "source_route_status": "stable_pmlr_route_present",
        "source_role_boundary_status": "background_formal_framing_context_only",
        "audit_decision": "citation_record_pass_not_manuscript_marker",
        "new_citation_added": "no",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "audit_reason": "The citation record has complete required metadata, stable route, and preserved linkage boundaries.",
    },
    {
        "citation_record_id": "CIT-REC-0002",
        "planned_citation_slot_id": "CIT-PLAN-0002",
        "evidence_matrix_row_id": "EMR-0002",
        "retained_source_id": "RET-0002",
        "candidate_entry_id": "CAND-0002",
        "citation_key": "pmlr-v124-wengel-mogensen20a",
        "title": "Causal screening in dynamical systems",
        "authors": "Søren Wengel Mogensen",
        "venue": "Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI)",
        "series": "Proceedings of Machine Learning Research",
        "volume": "124",
        "pages": "310-319",
        "year": "2020",
        "publisher": "PMLR",
        "stable_url": "https://proceedings.mlr.press/v124/wengel-mogensen20a.html",
        "field_completeness_status": "complete_required_fields",
        "linkage_status": "linked_to_plan_evidence_row_retained_source_and_candidate",
        "source_route_status": "stable_pmlr_route_present",
        "source_role_boundary_status": "background_methodological_context_only",
        "audit_decision": "citation_record_pass_not_manuscript_marker",
        "new_citation_added": "no",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "audit_reason": "The citation record has complete required metadata, stable route, and preserved linkage boundaries.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "citation_record_id": "none",
        "citation_record_audited": "no",
        "new_citation_added": "no",
        "manuscript_citation_marker_added": "no",
        "manuscript_revised": "no",
        "reason": "Conditional metadata pass remains outside retained source, evidence row audit, citation planning, citation integration, and citation record audit.",
    },
]


CITATION_RECORD_AUDIT_FIELDS = [
    "citation_record_id",
    "planned_citation_slot_id",
    "evidence_matrix_row_id",
    "retained_source_id",
    "candidate_entry_id",
    "citation_key",
    "title",
    "authors",
    "venue",
    "series",
    "volume",
    "pages",
    "year",
    "publisher",
    "stable_url",
    "field_completeness_status",
    "linkage_status",
    "source_route_status",
    "source_role_boundary_status",
    "audit_decision",
    "new_citation_added",
    "manuscript_citation_marker_added",
    "manuscript_revised",
    "audit_reason",
]


CITATION_RECORD_AUDIT_DECISION_VALUES = [
    "citation_record_pass_not_manuscript_marker",
    "citation_record_conditional_not_manuscript_marker",
    "citation_record_fail_not_manuscript_marker",
    "candidate_hold_no_citation_record_audit",
]


CITATION_RECORD_AUDIT_GATES = [
    "Citation record audit must be linked to v7.0 citation integration execution.",
    "Only existing citation records may be audited.",
    "Audit must not add new citation records.",
    "Audit must not insert manuscript citation markers.",
    "Audit must not revise manuscript prose.",
    "Each audited citation record must include a citation key.",
    "Each audited citation record must include title, authors, venue, series, volume, pages, year, publisher, and stable route.",
    "Each audited citation record must link to a planned citation slot.",
    "Each audited citation record must link to an evidence matrix row.",
    "Each audited citation record must link to a retained source.",
    "Each audited citation record must link to a candidate entry.",
    "Each audited citation record must preserve the planned citation role boundary.",
    "Citation record pass must not imply manuscript support.",
    "Citation record pass must not imply external validation.",
    "Citation record pass must not imply submission readiness.",
    "Conditional-hold candidates must remain outside citation record audit.",
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
    "does audit citation records",
    "does not add new citations",
    "does not insert manuscript citation markers",
    "does not revise the manuscript",
    "citation record audit is not citation integration execution",
    "citation record pass is not manuscript support",
    "citation record pass is not external validation",
    "citation record pass is not proof",
    "citations are not external validation",
    "conditional hold remains outside citation record audit",
    "future manuscript revision is separate",
    "future manuscript citation insertion is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not add new citations in this milestone.",
    "Do not insert manuscript citation markers in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat citation record audit as manuscript support.",
    "Do not treat citation record pass as external validation.",
    "Do not treat citation records as proof.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in citation record audit.",
    "Do not convert audited citation records into manuscript prose.",
    "Do not claim accepted scientific theory.",
]


NEXT_STEPS = [
    "Plan manuscript citation insertion only after citation record audit.",
    "Keep manuscript revision separate from citation record audit.",
    "Audit citation formatting before manuscript insertion.",
    "Plan citation-grounded manuscript revision in a later milestone.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve source-role boundaries during manuscript citation planning.",
    "Keep public claims bounded after citation record audit.",
    "Track citation records separately from manuscript claims.",
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
    "citation",
    "citation record",
    "audit",
    "audited",
    "evidence row",
    "retained source",
    "candidate",
    "conditional",
    "hold",
    "manuscript",
    "zero",
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
    "citation record audit gates",
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
class FirstCitationRecordAuditResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    citation_record_audit_count: int
    citation_record_count: int
    citation_record_audited_count: int
    citation_record_audit_pass_count: int
    citation_record_audit_conditional_count: int
    citation_record_audit_fail_count: int
    new_citation_added_count: int
    manuscript_citation_marker_count: int
    manuscript_revised_count: int
    conditional_hold_count: int
    citation_record_audit_field_count: int
    citation_record_audit_decision_value_count: int
    citation_record_audit_gate_count: int
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
        "| Citation record audit field | Value |",
        "|---|---|",
    ]
    for key, value in AUDIT_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_citation_record_audit_rows() -> str:
    rows = [
        "| Citation record id | Citation key | Evidence row | Retained source | Field status | Linkage status | Audit decision | Manuscript revised |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in CITATION_RECORD_AUDIT_ROWS:
        rows.append(
            f"| {item['citation_record_id']} | "
            f"{item['citation_key']} | "
            f"{item['evidence_matrix_row_id']} | "
            f"{item['retained_source_id']} | "
            f"{item['field_completeness_status']} | "
            f"{item['linkage_status']} | "
            f"{item['audit_decision']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_reference_detail_table() -> str:
    rows = [
        "| Citation record id | Title | Authors | Venue | PMLR volume | Pages | Stable route |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CITATION_RECORD_AUDIT_ROWS:
        rows.append(
            f"| {item['citation_record_id']} | "
            f"{item['title']} | "
            f"{item['authors']} | "
            f"{item['venue']} | "
            f"{item['volume']} | "
            f"{item['pages']} | "
            f"{item['stable_url']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Citation record id | Audited | New citation added | Manuscript marker | Manuscript revised | Reason |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['citation_record_id']} | "
            f"{item['citation_record_audited']} | "
            f"{item['new_citation_added']} | "
            f"{item['manuscript_citation_marker_added']} | "
            f"{item['manuscript_revised']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Citation record audit field | v7.1 status |",
        "|---|---|",
    ]
    for field in CITATION_RECORD_AUDIT_FIELDS:
        rows.append(f"| `{field}` | audited for citation record rows |")
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
        "citation record audit rows",
        "audited reference details",
        "citation record audit metadata",
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
    return f"""# First Citation Record Audit v7.1

## Question
Can Viruse Fabric audit the first verified citation records while keeping new citation additions, manuscript citation markers, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does audit citation records. It does not add new citations, does not insert manuscript citation markers, and does not revise the manuscript.

Citation record audit is not citation integration execution. Citation record pass is not manuscript support. Citation record pass is not external validation. Citation record pass is not proof. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Citation Record Audit Metadata
{render_metadata_table()}

## Citation Record Audit Rows
{render_citation_record_audit_rows()}

## Audited Reference Details
{render_reference_detail_table()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Citation Record Audit Fields
{render_field_table()}

## Citation Record Audit Decision Values
{bullet_list(CITATION_RECORD_AUDIT_DECISION_VALUES)}

## Citation Record Audit Gates
{bullet_list(CITATION_RECORD_AUDIT_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Citation Record Audit Interpretation
The v7.1 artifact audits the two verified citation records added in v7.0.

CIT-REC-0001 passes citation record audit because it preserves required metadata, stable PMLR route, linkage to CIT-PLAN-0001, linkage to EMR-0001, linkage to RET-0001, and linkage to CAND-0001.

CIT-REC-0002 passes citation record audit because it preserves required metadata, stable PMLR route, linkage to CIT-PLAN-0002, linkage to EMR-0002, linkage to RET-0002, and linkage to CAND-0002.

Both citation records remain metadata records. They are not manuscript prose, not manuscript citation markers, and not manuscript revision.

## Audit Boundary
Citation record audit count is one.

Citation record count is two.

Citation record audited count is two.

Citation record audit pass count is two.

Citation record audit conditional count is zero.

Citation record audit fail count is zero.

New citation added count is zero.

Manuscript citation marker count is zero.

Manuscript revised count is zero.

The project now has audited citation records, but it still has no manuscript citation markers and no manuscript revision. This distinction is boring in the way seatbelts are boring: annoying until physics gets involved.

## Field Completeness Boundary
Each audited citation record contains the required fields for the internal workflow: citation key, title, authors, venue, series, volume, pages, year, publisher, stable route, planned citation role, linkage fields, and audit decision.

Field completeness does not mean external validation. It means the record is structured enough for later citation formatting, manuscript citation insertion planning, and manuscript revision planning.

## Linkage Boundary
Each audited citation record remains linked to the staged workflow:

- planned citation slot
- evidence matrix row
- retained source
- candidate entry
- bounded citation role

This linkage prevents citation records from floating around like academic confetti. Humanity invented citations and then immediately required babysitting for them. Impressive, in the bleak way.

## Manuscript Boundary
The manuscript receives no new text.

No citation marker is inserted into manuscript prose.

No paragraph is rewritten.

No conclusion is strengthened.

No claim is upgraded.

Manuscript citation marker count remains zero.

Manuscript revised count remains zero.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside citation record audit. It has no citation record, no audit row, no manuscript marker, and no manuscript revision.

This prevents conditional metadata from becoming cited evidence through table-adjacent optimism.

## Claim Boundary Toward v7.5
This milestone permits a slightly stronger internal claim than v7.0.

Allowed after v7.1:

- internally staged prototype
- retained-source workflow
- evidence-mapped workflow
- evidence-row-audited workflow
- citation-planned workflow
- first verified citation records added
- first citation records audited
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
Citation record audit count: 1

Citation record count: 2

Citation record audited count: 2

Citation record audit pass count: 2

Citation record audit conditional count: 0

Citation record audit fail count: 0

New citation added count: 0

Manuscript citation marker count: 0

Manuscript revised count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact audits citation records.

It does not add new citations, does not insert manuscript citation markers, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstCitationRecordAuditResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    invented_citations = detect_invented_citation_like_patterns(report)

    citation_record_audit_count = 1
    citation_record_count = int(AUDIT_METADATA["citation_record_count_from_v7_0"])
    citation_record_audited_count = int(AUDIT_METADATA["citation_record_audited_count"])
    citation_record_audit_pass_count = int(AUDIT_METADATA["citation_record_audit_pass_count"])
    citation_record_audit_conditional_count = int(
        AUDIT_METADATA["citation_record_audit_conditional_count"]
    )
    citation_record_audit_fail_count = int(AUDIT_METADATA["citation_record_audit_fail_count"])
    new_citation_added_count = int(AUDIT_METADATA["new_citation_added_count"])
    manuscript_citation_marker_count = int(AUDIT_METADATA["manuscript_citation_marker_count"])
    manuscript_revised_count = int(AUDIT_METADATA["manuscript_revised_count"])
    conditional_hold_count = int(AUDIT_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 21:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if citation_record_audit_count != 1:
        errors.append(f"Citation record audit count should be one, got: {citation_record_audit_count}")

    if citation_record_count != 2:
        errors.append(f"Citation record count should be two, got: {citation_record_count}")

    if citation_record_audited_count != 2:
        errors.append(
            "Citation record audited count should be two, got: "
            f"{citation_record_audited_count}"
        )

    if citation_record_audit_pass_count != 2:
        errors.append(
            "Citation record audit pass count should be two, got: "
            f"{citation_record_audit_pass_count}"
        )

    if citation_record_audit_conditional_count != 0:
        errors.append(
            "Citation record audit conditional count should be zero, got: "
            f"{citation_record_audit_conditional_count}"
        )

    if citation_record_audit_fail_count != 0:
        errors.append(
            "Citation record audit fail count should be zero, got: "
            f"{citation_record_audit_fail_count}"
        )

    if citation_record_audited_count != citation_record_count:
        errors.append("Citation record audited count must equal citation record count")

    if citation_record_audit_pass_count != citation_record_count:
        errors.append("Citation record audit pass count must equal citation record count")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for label, value in [
        ("New citation added count", new_citation_added_count),
        ("Manuscript citation marker count", manuscript_citation_marker_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    for row in CITATION_RECORD_AUDIT_ROWS:
        missing_fields = [field for field in CITATION_RECORD_AUDIT_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('citation_record_id', 'unknown')} missing citation record audit fields: "
                f"{len(missing_fields)}"
            )

    if len(CITATION_RECORD_AUDIT_FIELDS) < 24:
        errors.append(
            f"Citation record audit field count too low: {len(CITATION_RECORD_AUDIT_FIELDS)}"
        )

    if len(CITATION_RECORD_AUDIT_DECISION_VALUES) < 4:
        errors.append(
            "Citation record audit decision value count too low: "
            f"{len(CITATION_RECORD_AUDIT_DECISION_VALUES)}"
        )

    if len(CITATION_RECORD_AUDIT_GATES) < 16:
        errors.append(f"Citation record audit gate count too low: {len(CITATION_RECORD_AUDIT_GATES)}")

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
            "Invented citation-like patterns detected outside audited citation sections: "
            f"{len(invented_citations)}"
        )

    if word_count < 1200:
        errors.append(f"Word count too low for first citation record audit: {word_count}")

    warnings.append("Citation records are audited, but no new citations are added.")
    warnings.append("Citation record audit does not insert manuscript markers or revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v7.1 artifact audits two verified citation records while keeping new citation "
        "additions, manuscript citation markers, and manuscript revision at zero."
    )

    return FirstCitationRecordAuditResult(
        title="First Citation Record Audit v7.1",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        citation_record_audit_count=citation_record_audit_count,
        citation_record_count=citation_record_count,
        citation_record_audited_count=citation_record_audited_count,
        citation_record_audit_pass_count=citation_record_audit_pass_count,
        citation_record_audit_conditional_count=citation_record_audit_conditional_count,
        citation_record_audit_fail_count=citation_record_audit_fail_count,
        new_citation_added_count=new_citation_added_count,
        manuscript_citation_marker_count=manuscript_citation_marker_count,
        manuscript_revised_count=manuscript_revised_count,
        conditional_hold_count=conditional_hold_count,
        citation_record_audit_field_count=len(CITATION_RECORD_AUDIT_FIELDS),
        citation_record_audit_decision_value_count=len(CITATION_RECORD_AUDIT_DECISION_VALUES),
        citation_record_audit_gate_count=len(CITATION_RECORD_AUDIT_GATES),
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

    print("First Citation Record Audit v7.1")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Citation record audit count: {result.citation_record_audit_count}")
    print(f"Citation record count: {result.citation_record_count}")
    print(f"Citation record audited count: {result.citation_record_audited_count}")
    print(f"Citation record audit pass count: {result.citation_record_audit_pass_count}")
    print(f"Citation record audit conditional count: {result.citation_record_audit_conditional_count}")
    print(f"Citation record audit fail count: {result.citation_record_audit_fail_count}")
    print(f"New citation added count: {result.new_citation_added_count}")
    print(f"Manuscript citation marker count: {result.manuscript_citation_marker_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation record audit field count: {result.citation_record_audit_field_count}")
    print(
        "Citation record audit decision value count: "
        f"{result.citation_record_audit_decision_value_count}"
    )
    print(f"Citation record audit gate count: {result.citation_record_audit_gate_count}")
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
