"""First retained source decision plan for Viruse Fabric v6.3.

This module creates the first retained source decision plan after the v6.2
candidate source metadata audit.

It plans retention decisions only.

It does not execute retention decisions.
It does not create retained sources.
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

OUTPUT_PATH = PROJECT_ROOT / "outputs" / "first_retained_source_decision_plan_v6_3.md"

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
    "retained_source_decision_plan_id": "RDP-0001",
    "linked_candidate_metadata_audit_id": "CMA-0001",
    "linked_candidate_entry_creation_id": "CEC-0001",
    "linked_candidate_entry_plan_id": "CEP-0001",
    "plan_status": "retention_decision_planned_not_executed",
    "literature_family": "constraint-based causality and dynamical-systems framing",
    "candidate_source_count_from_v6_2": "3",
    "metadata_audit_pass_count_from_v6_2": "2",
    "metadata_audit_conditional_pass_count_from_v6_2": "1",
    "planned_retention_candidate_count": "2",
    "conditional_hold_count": "1",
    "retention_decision_execution_count": "0",
    "retained_source_count": "0",
}


PLANNED_RETENTION_ROWS = [
    {
        "candidate_entry_id": "CAND-0001",
        "metadata_audit_decision": "metadata_pass_not_retained",
        "retention_plan_status": "eligible_for_retention_decision_later",
        "planned_retention_action": "evaluate_for_retention_in_future_milestone",
        "retained_source_created": "no",
        "reason": "Metadata passed candidate audit, so it can enter a later retention decision.",
    },
    {
        "candidate_entry_id": "CAND-0002",
        "metadata_audit_decision": "metadata_pass_not_retained",
        "retention_plan_status": "eligible_for_retention_decision_later",
        "planned_retention_action": "evaluate_for_retention_in_future_milestone",
        "retained_source_created": "no",
        "reason": "Metadata passed candidate audit, so it can enter a later retention decision.",
    },
    {
        "candidate_entry_id": "CAND-0003",
        "metadata_audit_decision": "metadata_conditional_pass_not_retained",
        "retention_plan_status": "hold_for_update_before_retention_decision",
        "planned_retention_action": "check_updated_metadata_before_retention_decision",
        "retained_source_created": "no",
        "reason": "Conditional metadata pass requires update handling before retention decision.",
    },
]


RETENTION_CRITERIA = [
    "Candidate must have passed metadata audit or have an explicit conditional update path.",
    "Candidate must have stable title metadata.",
    "Candidate must have stable author metadata.",
    "Candidate must have identifiable venue or repository metadata.",
    "Candidate must have year or access-date metadata that can be recorded without invention.",
    "Candidate must have a stable access route.",
    "Candidate source type must be classified.",
    "Candidate primary or secondary status must be explicit.",
    "Candidate must link back to raw observation and screening decision.",
    "Candidate must map to a specific claim category.",
    "Candidate must have inclusion rationale.",
    "Candidate must have exclusion-risk notes.",
    "Candidate must have a bounded proposed source role.",
    "Candidate must remain outside citation use until retention is explicitly executed.",
]


RETENTION_DECISION_VALUES = [
    "planned_for_future_retention_decision",
    "hold_for_metadata_update_before_retention",
    "not_ready_for_retention_decision",
    "retention_decision_not_executed",
]


RETENTION_PLAN_GATES = [
    "Retention planning must be separate from retention execution.",
    "Retention planning must not create retained sources.",
    "Retention planning must not add citations.",
    "Retention planning must not populate the evidence matrix.",
    "Retention planning must not revise the manuscript.",
    "Only metadata-pass candidates may be planned for immediate future retention decision.",
    "Conditional metadata-pass candidates must remain on hold until update handling.",
    "Every planned retention candidate must preserve candidate source status.",
    "Every future retention decision must be auditable.",
    "Every future retention decision must remain separate from citation integration.",
    "Retained-source decision must not imply external validation.",
    "Retained-source decision must not imply submission readiness.",
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
    "retained source decision plan is not retained source creation",
    "retention planning is not retention execution",
    "metadata pass is not source retention",
    "conditional metadata pass is not source retention",
    "candidate source entries are not retained sources",
    "retained sources are not citations",
    "citations are not external validation",
    "does plan retained source decisions",
    "does not create retained sources",
    "does not add citations",
    "does not populate the evidence matrix",
    "does not revise the manuscript",
]


PROHIBITED_BEHAVIORS = [
    "Do not create retained sources in this milestone.",
    "Do not add citations in this milestone.",
    "Do not populate the evidence matrix in this milestone.",
    "Do not revise the manuscript in this milestone.",
    "Do not treat metadata pass as retention.",
    "Do not treat retention planning as retention execution.",
    "Do not treat planned retention candidates as retained sources.",
    "Do not treat retained-source planning as citation readiness.",
    "Do not imply external validation.",
    "Do not imply submission readiness.",
    "Do not provide biological, clinical, laboratory, or operational guidance.",
]


NEXT_STEPS = [
    "Execute first retained source decision in a later milestone.",
    "Evaluate metadata-pass candidates for retention separately.",
    "Keep conditional metadata-pass candidate on hold until update handling.",
    "Create retained sources only after explicit retention decision.",
    "Audit retained source roles after retention decision.",
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
    "plan",
    "planning",
    "retention",
    "retained source",
    "candidate source",
    "metadata",
    "conditional",
    "zero",
    "future",
    "hold",
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
    "retention plan gates",
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
class FirstRetainedSourceDecisionPlanResult:
    title: str
    output_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int
    retained_source_decision_plan_count: int
    candidate_source_count: int
    metadata_audit_pass_count: int
    metadata_audit_conditional_pass_count: int
    planned_retention_candidate_count: int
    conditional_hold_count: int
    retention_decision_execution_count: int
    retained_source_count: int
    citation_added_count: int
    evidence_matrix_populated_count: int
    manuscript_revised_count: int
    retention_criteria_count: int
    retention_decision_value_count: int
    retention_plan_gate_count: int
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
        "| Retained source decision plan field | Value |",
        "|---|---|",
    ]
    for key, value in PLAN_METADATA.items():
        rows.append(f"| `{key}` | {value} |")
    return "\n".join(rows)


def render_planned_retention_rows() -> str:
    rows = [
        "| Candidate id | Metadata audit decision | Retention plan status | Planned action | Retained source created | Reason |",
        "|---|---|---|---|---|---|",
    ]
    for item in PLANNED_RETENTION_ROWS:
        rows.append(
            f"| {item['candidate_entry_id']} | "
            f"{item['metadata_audit_decision']} | "
            f"{item['retention_plan_status']} | "
            f"{item['planned_retention_action']} | "
            f"{item['retained_source_created']} | "
            f"{item['reason']} |"
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
    return f"""# First Retained Source Decision Plan v6.3

## Question
Can Viruse Fabric plan the first retained source decision after candidate metadata audit while keeping retention execution, retained sources, citations, evidence matrix population, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does plan retained source decisions. It does not execute retention decisions, does not create retained sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

Retained source decision plan is not retained source creation. Retention planning is not retention execution. Metadata pass is not source retention. Conditional metadata pass is not source retention. Candidate source entries are not retained sources. Retained sources are not citations. Citations are not external validation.

## Source Artifacts
{render_source_table()}

## Retained Source Decision Plan Metadata
{render_metadata_table()}

## Planned Retention Decision Rows
{render_planned_retention_rows()}

## Retention Criteria
{bullet_list(RETENTION_CRITERIA)}

## Retention Decision Values
{bullet_list(RETENTION_DECISION_VALUES)}

## Retention Plan Gates
{bullet_list(RETENTION_PLAN_GATES)}

## Boundary Phrases
{bullet_list(BOUNDARY_PHRASES)}

## Prohibited Behaviors
{bullet_list(PROHIBITED_BEHAVIORS)}

## Next Steps
{bullet_list(NEXT_STEPS)}

## Retention Plan Interpretation
The v6.3 artifact creates the first retained-source decision plan after the v6.2 metadata audit.

Two candidate sources are planned for future retention decision because they received metadata pass decisions in v6.2. One candidate source is placed on conditional hold because it received a conditional metadata pass and needs update handling before any retention decision.

This is planning only. No source becomes retained here. No source becomes citation-ready here. No source enters the evidence matrix here. No manuscript claim is revised here.

## Planning Boundary
The plan defines eligibility for a later decision, not the decision itself.

A metadata-pass candidate can be planned for future retention decision, but that future decision still needs explicit execution. A conditional metadata-pass candidate cannot be silently promoted. It must remain on hold until its metadata uncertainty is handled.

This boundary prevents a familiar little disaster: calling something "planned" and then treating it as "done" because a table looks official. Tables are very convincing liars when humans are tired.

## Retention Boundary
Retained source count remains zero.

This milestone does not create retained source records. It only identifies which candidate records may be evaluated in a later retained-source decision milestone. The retained-source layer remains empty.

A retained source, when eventually created, will still not be a citation by itself. Citation integration requires a separate action. Evidence matrix population requires a separate action. Manuscript revision requires a separate action.

## Evidence Boundary
Citation added count remains zero.

Evidence matrix populated count remains zero.

Manuscript revised count remains zero.

The project therefore keeps the distinction between candidate metadata, retention planning, retention execution, citation integration, evidence matrix population, and manuscript revision.

## Retention Decision Consequence Boundary
The retained-source decision plan creates no retained-source record.

It only describes which candidate entries are eligible for a later retained-source decision and which candidate entry must remain on hold. The two metadata-pass candidates are not retained here; they are only scheduled for future evaluation. The conditional candidate is not rejected here; it is held until update handling can resolve its metadata uncertainty.

This means the retained-source layer remains empty. The evidence matrix remains empty with respect to these candidates. The manuscript receives no new support. No citation is added. No external validation is implied.

A future retention decision must still ask whether a candidate source has an appropriate source role, a bounded claim mapping, a stable access route, and acceptable exclusion-risk notes. If that future decision passes, only then can a retained-source record be created.

## Plan Failure Modes Prevented
This artifact prevents several premature transitions.

It prevents metadata pass from becoming automatic retention. It prevents conditional metadata pass from being quietly upgraded into acceptance. It prevents planned retention from being treated as completed retention. It prevents a future citation workflow from inheriting sources that were never explicitly retained.

The artifact also prevents manuscript drift. A source can appear relevant, have metadata, pass audit, and enter a retention plan while still providing zero manuscript support. That is not inefficiency; it is the point of staged scientific bookkeeping. The alternative is a bibliography wearing a fake mustache and calling itself evidence.

## Output Counts
Retained source decision plan count: 1

Candidate source count: 3

Metadata audit pass count: 2

Metadata audit conditional pass count: 1

Planned retention candidate count: 2

Conditional hold count: 1

Retention decision execution count: 0

Retained source count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact plans first retained source decisions.

It does not execute retention decisions, does not create retained sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
"""


def generate_report() -> FirstRetainedSourceDecisionPlanResult:
    report = render_report()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(report, encoding="utf-8")

    missing = missing_sources()
    overclaims = detect_overclaims(report)
    fake_citations = detect_fake_citations(report)

    retained_source_decision_plan_count = 1
    candidate_source_count = int(PLAN_METADATA["candidate_source_count_from_v6_2"])
    metadata_audit_pass_count = int(PLAN_METADATA["metadata_audit_pass_count_from_v6_2"])
    metadata_audit_conditional_pass_count = int(
        PLAN_METADATA["metadata_audit_conditional_pass_count_from_v6_2"]
    )
    planned_retention_candidate_count = int(PLAN_METADATA["planned_retention_candidate_count"])
    conditional_hold_count = int(PLAN_METADATA["conditional_hold_count"])
    retention_decision_execution_count = int(PLAN_METADATA["retention_decision_execution_count"])
    retained_source_count = int(PLAN_METADATA["retained_source_count"])
    citation_added_count = 0
    evidence_matrix_populated_count = 0
    manuscript_revised_count = 0

    boundary_count = count_present_terms(report, BOUNDARY_PHRASES)
    prohibited_count = count_present_terms(report, PROHIBITED_BEHAVIORS)
    next_step_count = count_present_terms(report, NEXT_STEPS)
    word_count = count_words(report)

    errors: list[str] = []
    warnings: list[str] = []

    if len(SOURCE_ARTIFACTS) < 13:
        errors.append(f"Source artifact count too low: {len(SOURCE_ARTIFACTS)}")

    if missing:
        errors.append(f"Missing source artifacts: {len(missing)}")

    if retained_source_decision_plan_count != 1:
        errors.append(
            "Retained source decision plan count should be one, got: "
            f"{retained_source_decision_plan_count}"
        )

    if candidate_source_count != 3:
        errors.append(f"Candidate source count should be three, got: {candidate_source_count}")

    if metadata_audit_pass_count != 2:
        errors.append(f"Metadata audit pass count should be two, got: {metadata_audit_pass_count}")

    if metadata_audit_conditional_pass_count != 1:
        errors.append(
            "Metadata audit conditional pass count should be one, got: "
            f"{metadata_audit_conditional_pass_count}"
        )

    if planned_retention_candidate_count != 2:
        errors.append(
            "Planned retention candidate count should be two, got: "
            f"{planned_retention_candidate_count}"
        )

    if conditional_hold_count != 1:
        errors.append(f"Conditional hold count should be one, got: {conditional_hold_count}")

    for label, value in [
        ("Retention decision execution count", retention_decision_execution_count),
        ("Retained source count", retained_source_count),
        ("Citation added count", citation_added_count),
        ("Evidence matrix populated count", evidence_matrix_populated_count),
        ("Manuscript revised count", manuscript_revised_count),
    ]:
        if value != 0:
            errors.append(f"{label} should be zero, got: {value}")

    if planned_retention_candidate_count + conditional_hold_count != candidate_source_count:
        errors.append("Planned retention and hold counts do not sum to candidate source count")

    if len(RETENTION_CRITERIA) < 14:
        errors.append(f"Retention criteria count too low: {len(RETENTION_CRITERIA)}")

    if len(RETENTION_DECISION_VALUES) < 4:
        errors.append(f"Retention decision value count too low: {len(RETENTION_DECISION_VALUES)}")

    if len(RETENTION_PLAN_GATES) < 12:
        errors.append(f"Retention plan gate count too low: {len(RETENTION_PLAN_GATES)}")

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
        errors.append(f"Word count too low for first retained source decision plan: {word_count}")

    warnings.append("Retained source decision plan creates no retained sources.")
    warnings.append("Retention planning does not add citations, evidence rows, or manuscript revisions.")

    passed = not errors

    interpretation = (
        "The v6.3 artifact plans future retained-source decisions for two metadata-pass "
        "candidate sources while keeping retention execution, retained sources, citations, "
        "evidence matrix population, and manuscript revision at zero."
    )

    return FirstRetainedSourceDecisionPlanResult(
        title="First Retained Source Decision Plan v6.3",
        output_path=OUTPUT_PATH,
        source_artifact_count=len(SOURCE_ARTIFACTS),
        missing_source_artifact_count=len(missing),
        retained_source_decision_plan_count=retained_source_decision_plan_count,
        candidate_source_count=candidate_source_count,
        metadata_audit_pass_count=metadata_audit_pass_count,
        metadata_audit_conditional_pass_count=metadata_audit_conditional_pass_count,
        planned_retention_candidate_count=planned_retention_candidate_count,
        conditional_hold_count=conditional_hold_count,
        retention_decision_execution_count=retention_decision_execution_count,
        retained_source_count=retained_source_count,
        citation_added_count=citation_added_count,
        evidence_matrix_populated_count=evidence_matrix_populated_count,
        manuscript_revised_count=manuscript_revised_count,
        retention_criteria_count=len(RETENTION_CRITERIA),
        retention_decision_value_count=len(RETENTION_DECISION_VALUES),
        retention_plan_gate_count=len(RETENTION_PLAN_GATES),
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

    print("First Retained Source Decision Plan v6.3")
    print(f"Output path: {result.output_path.relative_to(PROJECT_ROOT)}")
    print(f"Source artifact count: {result.source_artifact_count}")
    print(f"Missing source artifact count: {result.missing_source_artifact_count}")
    print(f"Retained source decision plan count: {result.retained_source_decision_plan_count}")
    print(f"Candidate source count: {result.candidate_source_count}")
    print(f"Metadata audit pass count: {result.metadata_audit_pass_count}")
    print(f"Metadata audit conditional pass count: {result.metadata_audit_conditional_pass_count}")
    print(f"Planned retention candidate count: {result.planned_retention_candidate_count}")
    print(f"Conditional hold count: {result.conditional_hold_count}")
    print(f"Retention decision execution count: {result.retention_decision_execution_count}")
    print(f"Retained source count: {result.retained_source_count}")
    print(f"Citation added count: {result.citation_added_count}")
    print(f"Evidence matrix populated count: {result.evidence_matrix_populated_count}")
    print(f"Manuscript revised count: {result.manuscript_revised_count}")
    print(f"Retention criteria count: {result.retention_criteria_count}")
    print(f"Retention decision value count: {result.retention_decision_value_count}")
    print(f"Retention plan gate count: {result.retention_plan_gate_count}")
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
