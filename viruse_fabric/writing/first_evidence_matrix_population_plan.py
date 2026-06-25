"""First evidence matrix population plan for Viruse Fabric v6.6.

This module creates the first evidence matrix population plan after retained
source role audit.

It plans evidence matrix population only.

It does not populate the evidence matrix.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_evidence_matrix_population_plan_v6_6.md"

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
    "evidence_matrix_population_plan_id": "EMP-0001",
    "linked_retained_source_role_audit_id": "RSA-0001",
    "linked_retention_execution_id": "RDE-0001",
    "linked_retention_plan_id": "RDP-0001",
    "plan_status": "evidence_matrix_population_planned_not_executed",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "retained_source_count_from_v6_5": "2",
    "retained_source_role_audited_count_from_v6_5": "2",
    "planned_evidence_mapping_count": "2",
    "conditional_hold_count": "1",
    "evidence_matrix_population_execution_count": "0",
    "evidence_matrix_populated_count": "0",
    "citation_added_count": "0",
    "manuscript_revised_count": "0",
}


PLANNED_EVIDENCE_MAPPING_ROWS = [
    {
        "planned_mapping_id": "EMP-ROW-0001",
        "retained_source_id": "RET-0001",
        "linked_candidate_entry_id": "CAND-0001",
        "audited_role_from_v6_5": "formal_framing_source_for_constraint_based_causality_context",
        "planned_claim_category": "constraint-based causality and formal framing",
        "planned_evidence_role": "contextual_formal_framing_reference_candidate",
        "planned_matrix_action": "plan_for_future_population_only",
        "population_executed": "no",
        "citation_added": "no",
        "manuscript_revised": "no",
        "planning_reason": "Role audit passed for bounded formal framing context, but evidence matrix population is reserved for a later milestone.",
    },
    {
        "planned_mapping_id": "EMP-ROW-0002",
        "retained_source_id": "RET-0002",
        "linked_candidate_entry_id": "CAND-0002",
        "audited_role_from_v6_5": "methodological_context_source_for_dynamical_systems_screening",
        "planned_claim_category": "dynamical-systems screening and methodological context",
        "planned_evidence_role": "methodological_context_reference_candidate",
        "planned_matrix_action": "plan_for_future_population_only",
        "population_executed": "no",
        "citation_added": "no",
        "manuscript_revised": "no",
        "planning_reason": "Role audit passed for bounded methodological context, but evidence matrix population is reserved for a later milestone.",
    },
]


CONDITIONAL_HOLD_ROWS = [
    {
        "candidate_entry_id": "CAND-0003",
        "hold_status": "hold_for_update_before_retention_decision",
        "retained_source_id": "none",
        "role_audited": "no",
        "planned_evidence_mapping": "no",
        "reason": "Conditional metadata pass remains outside retained source and evidence matrix planning.",
    },
]


PLANNING_FIELDS = [
    "planned_mapping_id",
    "retained_source_id",
    "linked_candidate_entry_id",
    "audited_role_from_v6_5",
    "planned_claim_category",
    "planned_evidence_role",
    "planned_matrix_action",
    "population_executed",
    "citation_added",
    "manuscript_revised",
    "planning_reason",
]


PLANNED_MATRIX_ACTION_VALUES = [
    "plan_for_future_population_only",
    "hold_until_retained_source_update",
    "not_planned_for_population",
    "population_execution_not_performed",
]


POPULATION_PLAN_GATES = [
    "Evidence matrix population plan must be linked to v6.5 retained source role audit.",
    "Only retained sources with role pass may receive planned evidence mappings.",
    "Conditional-hold candidates must remain outside evidence matrix planning.",
    "Planned mapping must state a bounded claim category.",
    "Planned mapping must state a bounded evidence role.",
    "Planned mapping must not populate the evidence matrix.",
    "Planned mapping must not add citations.",
    "Planned mapping must not revise the manuscript.",
    "Evidence matrix population execution must remain zero.",
    "Evidence matrix populated count must remain zero.",
    "Citation added count must remain zero.",
    "Manuscript revised count must remain zero.",
    "Planning must not imply external validation.",
    "Planning must not imply submission readiness.",
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
    "does plan evidence matrix population",
    "does not populate the evidence matrix",
    "does not add citations",
    "does not revise the manuscript",
    "evidence matrix population plan is not evidence matrix population",
    "planned evidence mapping is not evidence matrix population",
    "planned evidence mapping is not citation readiness",
    "planned evidence mapping is not manuscript support",
    "retained source role pass is not matrix population",
    "citations are not external validation",
    "conditional hold remains outside evidence matrix planning",
    "future use is bounded",
]


PROHIBITED_BEHAVIORS = [
    "Do not populate the evidence matrix in this milestone.",
    "Do not add citations in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat planned evidence mapping as evidence matrix population.",
    "Do not treat planned evidence mapping as citation readiness.",
    "Do not treat planned evidence mapping as manuscript support.",
    "Do not treat role pass as evidence matrix population.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
    "Do not include conditional-hold candidates in planned evidence mappings.",
]


NEXT_STEPS = [
    "Execute first evidence matrix population in a later milestone.",
    "Populate evidence matrix only from audited retained-source roles.",
    "Keep citation integration separate from evidence matrix planning.",
    "Audit populated evidence matrix rows after execution.",
    "Add citations only in a later citation-specific milestone.",
    "Revise manuscript only after citation-grounded integration.",
    "Keep CAND-0003 on hold until update handling.",
    "Preserve public language boundaries after evidence planning.",
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
    "evidence matrix",
    "retained source",
    "role pass",
    "candidate",
    "conditional",
    "hold",
    "citation",
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
    "population plan gates",
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
class FirstEvidenceMatrixPopulationPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    evidence_matrix_population_plan_count: int
    retained_source_count: int
    retained_source_role_audited_count: int
    planned_evidence_mapping_count: int
    conditional_hold_count: int
    evidence_matrix_population_execution_count: int
    evidence_matrix_populated_count: int
    citation_added_count: int
    manuscript_revised_count: int
    planning_field_count: int
    planned_matrix_action_value_count: int
    population_plan_gate_count: int
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
        "| Evidence matrix population plan field | Value |",
        "|---|---|",
    ]
    for key, value in PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_planned_mapping_rows() -> str:
    rows = [
        "| Planned mapping id | Retained source id | Planned claim category | Planned evidence role | Population executed | Citation added | Manuscript revised |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in PLANNED_EVIDENCE_MAPPING_ROWS:
        rows.append(
            f"| {item['planned_mapping_id']} | "
            f"{item['retained_source_id']} | "
            f"{item['planned_claim_category']} | "
            f"{item['planned_evidence_role']} | "
            f"{item['population_executed']} | "
            f"{item['citation_added']} | "
            f"{item['manuscript_revised']} |"
        )
    return "\n".join(rows)


def render_conditional_hold_rows() -> str:
    rows = [
        "| Candidate id | Hold status | Retained source id | Planned evidence mapping | Reason |",
        "|---|---|---|---|---|",
    ]
    for item in CONDITIONAL_HOLD_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['hold_status']} | "
            f"{item['retained_source_id']} | "
            f"{item['planned_evidence_mapping']} | "
            f"{item['reason']} |"
        )
    return "\n".join(rows)


def render_field_table() -> str:
    rows = [
        "| Planning field | v6.6 status |",
        "|---|---|",
    ]
    for field in PLANNING_FIELDS:
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
    return f"""# First Evidence Matrix Population Plan v6.6

## Question
Can Viruse Fabric plan first evidence matrix population from audited retained-source roles while keeping evidence matrix population execution, citations, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does plan evidence matrix population. It does not populate the evidence matrix, does not add citations, and does not revise the manuscript.

Evidence matrix population plan is not evidence matrix population. Planned evidence mapping is not evidence matrix population. Planned evidence mapping is not citation readiness. Planned evidence mapping is not manuscript support. Retained source role pass is not matrix population. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Evidence Matrix Population Plan Metadata
{render_metadata_table()}

## Planned Evidence Mapping Rows
{render_planned_mapping_rows()}

## Conditional Hold Rows
{render_conditional_hold_rows()}

## Planning Fields
{render_field_table()}

## Planned Matrix Action Values
{bullet_list(PLANNED_MATRIX_ACTION_VALUES)}

## Population Plan Gates
{bullet_list(POPULATION_PLAN_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Population Plan Interpretation
The v6.6 artifact plans how the first two audited retained source roles may later enter the evidence matrix.

RET-0001 is planned for a future evidence mapping role related to constraint-based causality and formal framing. RET-0002 is planned for a future evidence mapping role related to dynamical-systems screening and methodological context.

These are planned mappings only. No evidence matrix row is populated here. No citation is added here. No manuscript sentence is revised here.

## Planning Boundary
Planned evidence mapping count is two.

Evidence matrix population execution count is zero.

Evidence matrix populated count is zero.

This means the workflow now knows where retained source roles may go later, but it has not moved them there. A planned mapping is a scheduling artifact, not an evidence artifact. This distinction is tiny, bureaucratic, and somehow the only thing standing between a controlled research prototype and a spreadsheet pretending to be a paper.

## Retained Source Boundary
Retained source count remains two.

Retained source role audited count remains two.

The two retained sources have bounded audited roles from v6.5. The v6.6 plan uses those bounded roles to prepare future evidence matrix placement. It does not widen those roles, does not convert them into citations, and does not treat them as manuscript support.

A retained source can be planned for future evidence use and still remain outside the evidence matrix. That is not indecision; that is staged control.

## Conditional Hold Boundary
Conditional hold count remains one.

CAND-0003 remains outside this plan because it is not a retained source and did not receive retained-source role audit. It cannot be planned for evidence matrix population until it first passes update handling, retention decision, and role audit.

This boundary prevents a conditional candidate from sneaking into evidence planning by standing near more successful rows and hoping nobody checks the identifier. Tables, tragically, also need supervision.

## Citation Boundary
Citation added count remains zero.

No citation slot is filled. No bibliography entry is created. No reference text is added. No retained source role becomes citation text.

The planned evidence rows may support a later citation workflow, but they do not create citation readiness by themselves.

## Manuscript Boundary
Manuscript revised count remains zero.

The manuscript receives no new text, no rewritten claim, no strengthened conclusion, and no source-grounded revision from this artifact.

The project remains a research prototype with internal validation.

## Output Counts
Evidence matrix population plan count: 1

Retained source count: 2

Retained source role audited count: 2

Planned evidence mapping count: 2

Conditional hold count: 1

Evidence matrix population execution count: 0

Evidence matrix populated count: 0

Citation added count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact plans evidence matrix population.

It does not populate the evidence matrix, does not add citations, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstEvidenceMatrixPopulationPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    evidence_matrix_population_plan_count = 1
    retained_source_count = int(PLAN_METADATA["retained_source_count_from_v6_5"])
    retained_source_role_audited_count = int(
        PLAN_METADATA["retained_source_role_audited_count_from_v6_5"]
    )
    planned_evidence_mapping_count = int(PLAN_METADATA["planned_evidence_mapping_count"])
    conditional_hold_count = int(PLAN_METADATA["conditional_hold_count"])
    evidence_matrix_population_execution_count = int(
        PLAN_METADATA["evidence_matrix_population_execution_count"]
    )
    evidence_matrix_populated_count = int(PLAN_METADATA["evidence_matrix_populated_count"])
    citation_added_count = int(PLAN_METADATA["citation_added_count"])
    manuscript_revised_count = int(PLAN_METADATA["manuscript_revised_count"])

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 16:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if evidence_matrix_population_plan_count != 1:
        errors.append(
            "Evidence matrix population plan count should be one, got: "
            f"{evidence_matrix_population_plan_count}"
        )

    if retained_source_count != 2:
        errors.append(f"Retained source count should be two, got: {retained_source_count}")

    if retained_source_role_audited_count != 2:
        errors.append(
            "Retained source role audited count should be two, got: "
            f"{retained_source_role_audited_count}"
        )

    if planned_evidence_mapping_count != 2:
        errors.append(
            "Planned evidence mapping count should be two, got: "
            f"{planned_evidence_mapping_count}"
        )

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    if planned_evidence_mapping_count != retained_source_role_audited_count:
        errors.append("Planned evidence mapping count must equal audited retained source count")

    for label, value in [
        ("Evidence matrix population execution count", evidence_matrix_population_execution_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Citation added count", citation_added_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    for row in PLANNED_EVIDENCE_MAPPING_ROWS:
        missing_fields = [field for field in PLANNING_FIELDS if not row.get(field)]
        if missing_fields:
            errors.append(
                f"{row.get('planned_mapping_id', 'unknown')} missing planning fields: "
                f"{len(missing_fields)}"
            )

    if len(PLANNING_FIELDS) < 11:
        errors.append(f"Planning field count too low: {len(PLANNING_FIELDS)}")

    if len(PLANNED_MATRIX_ACTION_VALUES) < 4:
        errors.append(
            f"Planned matrix action value count too low: {len(PLANNED_MATRIX_ACTION_VALUES)}"
        )

    if len(POPULATION_PLAN_GATES) < 14:
        errors.append(f"Population plan gate count too low: {len(POPULATION_PLAN_GATES)}")

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
        errors.append(f"Word count too low for first evidence matrix population plan: {word_count}")

    warnings.append("Evidence matrix population is planned, but no evidence rows are populated.")
    warnings.append("Evidence planning does not add citations or revise the manuscript.")

    passed = not errors

    interpretation = (
        "The v6.6 artifact plans future evidence matrix population for two audited retained "
        "source roles while keeping matrix population execution, citations, and manuscript "
        "revision at zero."
    )

    return FirstEvidenceMatrixPopulationPlanResult(
        title="First Evidence Matrix Population Plan v6.6",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        evidence_matrix_population_plan_count=evidence_matrix_population_plan_count,
        retained_source_count=retained_source_count,
        retained_source_role_audited_count=retained_source_role_audited_count,
        planned_evidence_mapping_count=planned_evidence_mapping_count,
        conditional_hold_count=conditional_hold_count,
        evidence_matrix_population_execution_count=evidence_matrix_population_execution_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        citation_added_count=citation_added_count,
        manuscript_revised_count=manuscript_revised_count,
        planning_field_count=len(PLANNING_FIELDS),
        planned_matrix_action_value_count=len(PLANNED_MATRIX_ACTION_VALUES),
        population_plan_gate_count=len(POPULATION_PLAN_GATES),
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

    print("First Evidence Matrix Population Plan v6.6")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Evidence matrix population plan count: {result.evidence_matrix_population_plan_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Retained source role audited count: {result.retained_source_role_audited_count}")
    print(f"Planned evidence mapping count: {result.planned_evidence_mapping_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Evidence matrix population execution count: {result.evidence_matrix_population_execution_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Planning field count: {result.planning_field_count}")
    print(f"Planned matrix action value count: {result.planned_matrix_action_value_count}")
    print(f"Population plan gate count: {result.population_plan_gate_count}")
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
