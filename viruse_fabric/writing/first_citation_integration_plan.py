"""First citation integration plan for Viruse Fabric v6.9.

This module creates the first citation integration plan after evidence matrix
row audit.

It plans citation integration only.

It does not add citations.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_citation_integration_plan_v6_9.md"

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
    "citation_integration_plan_id": "CIP-0001",
    "linked_evidence_matrix_row_audit_id": "ERA-0001",
    "linked_evidence_matrix_population_execution_id": "EMX-0001",
    "linked_evidence_matrix_population_plan_id": "EMP-0001",
    "plan_status": "citation_integration_planned_not_executed",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "audited_evidence_row_count_from_v6_8": "2",
    "planned_citation_slot_count": "2",
    "citation_integration_execution_count": "0",
    "citation_added_count": "0",
    "manuscript_revised_count": "0",
    "conditional_hold_count": "1",
}


PLANNED_CITATION_SLOT_ROWS = [
    {
        "planned_citation_slot_id": "CIT-PLAN-0001",
        "linked_evidence_matrix_row_id": "EMR-0001",
        "linked_retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "planned_claim_category": "constraint-based causality and formal framing",
        "planned_citation_role": "background_formal_framing_context",
        "planned_manuscript_target": "related-work or conceptual framing section only",
        "citation_integration_action": "plan_for_future_citation_integration_only",
        "citation_added": "no",
        "manuscript_revised": "no",
        "planning_limit": "Citation slot plan only; not citation text and not manuscript revision in v6.9.",
        "planning_reason": "The audited evidence row passed as bounded formal framing context, so it may later support a careful citation slot.",
    },
    {
        "planned_citation_slot_id": "CIT-PLAN-0002",
        "linked_evidence_matrix_row_id": "EMR-0002",
        "linked_retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "planned_claim_category": "dynamical-systems screening and methodological context",
        "planned_citation_role": "background_methodological_context",
        "planned_manuscript_target": "related-work or methodological context section only",
        "citation_integration_action": "plan_for_future_citation_integration_only",
        "citation_added": "no",
        "manuscript_revised": "no",
        "planning_limit": "Citation slot plan only; not citation text and not manuscript revision in v6.9.",
        "planning_reason": "The audited evidence row passed as bounded methodological context, so it may later support a careful citation slot.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "evidence_matrix_row_id": "none",
        "planned_citation_slot_id": "none",
        "citation_added": "no",
        "manuscript_revised": "no",
        "reason": "Conditional metadata pass remains outside retained source, evidence row audit, and citation planning.",
    },
]


CITATION_PLAN_FIELDS = [
    "planned_citation_slot_id",
    "linked_evidence_matrix_row_id",
    "linked_retained_source_id",
    "linked_candidate_entry_id",
    "planned_claim_category",
    "planned_citation_role",
    "planned_manuscript_target",
    "citation_integration_action",
    "citation_added",
    "manuscript_revised",
    "planning_limit",
    "planning_reason",
]


CITATION_PLAN_ACTION_VALUES = [
    "plan_for_future_citation_integration_only",
    "hold_until_evidence_row_update",
    "not_planned_for_citation",
    "citation_integration_not_performed",
]


CITATION_PLAN_GATES = [
    "Citation integration plan must be linked to v6.8 evidence row audit.",
    "Only audited evidence rows with row pass may receive planned citation slots.",
    "Conditional-hold candidates must remain outside citation planning.",
    "Planned citation slot must link to an evidence matrix row.",
    "Planned citation slot must link to a retained source.",
    "Planned citation slot must link to a candidate entry.",
    "Planned citation slot must state a bounded claim category.",
    "Planned citation slot must state a bounded citation role.",
    "Planned citation slot must state a manuscript target without revising it.",
    "Citation integration execution must remain zero.",
    "Citation added count must remain zero.",
    "Manuscript revised count must remain zero.",
    "Citation planning must not imply external validation.",
    "Citation planning must not imply submission readiness.",
    "Citation planning must not create bibliography text.",
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
    "does plan citation integration",
    "does not add citations",
    "does not revise the manuscript",
    "citation integration plan is not citation integration",
    "planned citation slot is not a citation",
    "planned citation slot is not manuscript revision",
    "evidence row pass is not citation readiness",
    "citation planning is not external validation",
    "citations are not external validation",
    "conditional hold remains outside citation planning",
    "future citation use is separate",
    "future manuscript revision is separate",
]


PROHIBITED_BEHAVIORS = [
    "Do not add citations in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not create bibliography entries in this milestone.",
    "Do not treat planned citation slots as citations.",
    "Do not treat citation planning as manuscript support.",
    "Do not treat evidence row pass as citation readiness.",
    "Do not treat citation planning as external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in citation plans.",
    "Do not convert planned citation slots into citation text.",
]


NEXT_STEPS = [
    "Execute first citation integration in a later milestone.",
    "Add citations only after citation integration execution.",
    "Audit added citations after execution.",
    "Plan manuscript revision only after citation audit.",
    "Revise manuscript only after citation-grounded revision planning.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve citation-role boundaries during integration.",
    "Keep public language bounded after citation planning.",
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
    "plan",
    "planned",
    "planning",
    "citation",
    "evidence row",
    "evidence matrix",
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
    "citation plan gates",
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
class FirstCitationIntegrationPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    citation_integration_plan_count: int
    audited_evidence_row_count: int
    planned_citation_slot_count: int
    citation_integration_execution_count: int
    citation_added_count: int
    manuscript_revised_count: int
    conditional_hold_count: int
    citation_plan_field_count: int
    citation_plan_action_value_count: int
    citation_plan_gate_count: int
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
        "| Citation integration plan field | Value |",
        "|---|---|",
    ]
    for key, value in PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_planned_citation_slot_rows() -> str:
    rows = [
        "| Planned citation slot id | Evidence row id | Retained source id | Citation role | Action | Citation added | Manuscript revised |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in PLANNED_CITATION_SLOT_ROWS:
        rows.append(
            f"| {item['planned_citation_slot_id']} | "
            f"{item['linked_evidence_matrix_row_id']} | "
            f"{item['linked_retained_source_id']} | "
            f"{item['planned_citation_role']} | "
            f"{item['citation_integration_action']} | "
            f"{item['citation_added']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Evidence row id | Planned citation slot id | Citation added | Manuscript revised | Reason |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['evidence_matrix_row_id']} | "
            f"{item['planned_citation_slot_id']} | "
            f"{item['citation_added']} | "
            f"{item['manuscript_revised']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Citation plan field | v6.9 status |",
        "|---|---|",
    ]
    for field in CITATION_PLAN_FIELDS:
        rows.append(f"| `{field}` | populated for citation planning rows only |")
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

        if "fake citation" in lowered or "not citations" in lowered or "planned citation" in lowered:
            continue

        for pattern in FAKE_CITATION_PATTERNS:
            if re.search(pattern, stripped):
                findings.append(stripped)
                break

    return findings


def render_report() -> str:
    return f"""# First Citation Integration Plan v6.9

## Question
Can Viruse Fabric plan first citation integration from audited evidence matrix rows while keeping citation integration execution, added citations, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does plan citation integration. It does not add citations and does not revise the manuscript.

Citation integration plan is not citation integration. Planned citation slot is not a citation. Planned citation slot is not manuscript revision. Evidence row pass is not citation readiness. Citation planning is not external validation. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Citation Integration Plan Metadata
{render_metadata_table()}

## Planned Citation Slot Rows
{render_planned_citation_slot_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Citation Plan Fields
{render_field_table()}

## Citation Plan Action Values
{bullet_list(CITATION_PLAN_ACTION_VALUES)}

## Citation Plan Gates
{bullet_list(CITATION_PLAN_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Citation Plan Interpretation
The v6.9 artifact creates the first citation integration plan after evidence matrix row audit.

CIT-PLAN-0001 plans a future citation slot from EMR-0001 and RET-0001 for bounded formal-framing context. CIT-PLAN-0002 plans a future citation slot from EMR-0002 and RET-0002 for bounded methodological context.

These are planned citation slots only. No citation text is created. No bibliography entry is created. No manuscript sentence is revised. The plan prepares a future citation integration step without executing it.

## Planning Boundary
Citation integration plan count is one.

Planned citation slot count is two.

Citation integration execution count is zero.

Citation added count is zero.

This means the project now has a controlled route from audited evidence rows toward future citations, but it has not crossed that route yet. A planned citation slot is a map, not a citation. Humanity keeps confusing maps with territory, which is why workflow gates now have to babysit tables.

## Evidence Row Boundary
Audited evidence row count is two.

Only EMR-0001 and EMR-0002 are allowed into citation planning because they passed row audit in v6.8. CAND-0003 remains outside citation planning because it never became a retained source, evidence row, or audited evidence row.

Evidence row pass makes future citation planning possible. It does not make a source cited. It does not make manuscript support real. It does not create external validation.

## Citation Boundary
Citation added count remains zero.

No citation slot is filled. No reference text is added. No bibliography entry is created. No citation marker is inserted. No source is used inside manuscript prose.

The project is now citation-planning-ready for two bounded evidence rows, but it is not yet citation-integrated.

## Manuscript Boundary
Manuscript revised count remains zero.

The manuscript receives no new text, no rewritten claim, no strengthened conclusion, and no citation-grounded revision from this artifact.

A future milestone may use this plan to add citations, but manuscript revision remains separate and later.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside citation planning because it is still on conditional hold. It cannot inherit citation planning status from nearby rows, even if it looks lonely in the table.

This boundary keeps the citation workflow from becoming a soup where every candidate floats upward and calls itself evidence.

## Claim Boundary Toward v7.5
This plan moves the project closer to bounded citation-grounded claims, but it does not yet authorize strong claims.

After later citation execution, citation audit, manuscript revision planning, and manuscript revision audit, the project may support limited framework-level statements such as: internally staged, source-retained, evidence-mapped, and citation-grounded prototype.

It still must not claim proof, external validation, biological prediction, clinical relevance, laboratory guidance, operational readiness, or submission readiness.

## Output Counts
Citation integration plan count: 1

Audited evidence row count: 2

Planned citation slot count: 2

Citation integration execution count: 0

Citation added count: 0

Manuscript revised count: 0

Conditional hold count: 1

## Final Boundary Statement
This artifact plans citation integration.

It does not add citations, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstCitationIntegrationPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    citation_integration_plan_count = 1
    audited_evidence_row_count = int(PLAN_METADATA["audited_evidence_row_count_from_v6_8"])
    planned_citation_slot_count = int(PLAN_METADATA["planned_citation_slot_count"])
    citation_integration_execution_count = int(
        PLAN_METADATA["citation_integration_execution_count"]
    )
    citation_added_count = int(PLAN_METADATA["citation_added_count"])
    manuscript_revised_count = int(PLAN_METADATA["manuscript_revised_count"])
    conditional_hold_count = int(PLAN_METADATA["conditional_hold_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 19:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if citation_integration_plan_count != 1:
        errors.append(
            "Citation integration plan count should be one, got: "
            f"{citation_integration_plan_count}"
        )

    if audited_evidence_row_count != 2:
        errors.append(f"Audited evidence row count should be two, got: {audited_evidence_row_count}")

    if planned_citation_slot_count != 2:
        errors.append(
            "Planned citation slot count should be two, got: "
            f"{planned_citation_slot_count}"
        )

    if planned_citation_slot_count != audited_evidence_row_count:
        errors.append("Planned citation slot count must equal audited evidence row count")

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for label, value in [
        ("Citation integration execution count", citation_integration_execution_count),
        ("Citation added count", citation_added_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    for row in PLANNED_CITATION_SLOT_ROWS:
        missing_fields = [field for field in CITATION_PLAN_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('planned_citation_slot_id', 'unknown')} missing citation plan fields: "
                f"{len(missing_fields)}"
            )

    if len(CITATION_PLAN_FIELDS) < 12:
        errors.append(f"Citation plan field count too low: {len(CITATION_PLAN_FIELDS)}")

    if len(CITATION_PLAN_ACTION_VALUES) < 4:
        errors.append(
            f"Citation plan action value count too low: {len(CITATION_PLAN_ACTION_VALUES)}"
        )

    if len(CITATION_PLAN_GATES) < 15:
        errors.append(f"Citation plan gate count too low: {len(CITATION_PLAN_GATES)}")

    if boundary_count < 20:
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
        errors.append(f"Word count too low for first citation integration plan: {word_count}")

    warnings.append("Citation integration is planned, but no citations are added.")
    warnings.append("Citation planning does not revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v6.9 artifact plans future citation integration for two audited evidence "
        "rows while keeping citation execution, added citations, and manuscript revision at zero."
    )

    return FirstCitationIntegrationPlanResult(
        title="First Citation Integration Plan v6.9",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        citation_integration_plan_count=citation_integration_plan_count,
        audited_evidence_row_count=audited_evidence_row_count,
        planned_citation_slot_count=planned_citation_slot_count,
        citation_integration_execution_count=citation_integration_execution_count,
        citation_added_count=citation_added_count,
        manuscript_revised_count=manuscript_revised_count,
        conditional_hold_count=conditional_hold_count,
        citation_plan_field_count=len(CITATION_PLAN_FIELDS),
        citation_plan_action_value_count=len(CITATION_PLAN_ACTION_VALUES),
        citation_plan_gate_count=len(CITATION_PLAN_GATES),
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

    print("First Citation Integration Plan v6.9")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Citation integration plan count: {result.citation_integration_plan_count}")
    print(f"Audited evidence row count: {result.audited_evidence_row_count}")
    print(f"Planned citation slot count: {result.planned_citation_slot_count}")
    print(f"Citation integration execution count: {result.citation_integration_execution_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Citation plan field count: {result.citation_plan_field_count}")
    print(f"Citation plan action value count: {result.citation_plan_action_value_count}")
    print(f"Citation plan gate count: {result.citation_plan_gate_count}")
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
