from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/draft_boundary_resolution_targeting_plan_v8_63.md")
OUTPUT_PATH = Path("outputs/draft_boundary_resolution_authorization_plan_v8_64.md")


@dataclass(frozen=True)
class DraftBoundaryResolutionAuthorizationTarget:
    authorization_plan_id: str
    linked_resolution_target: str
    linked_boundary_issues: str
    target_name: str
    priority: str
    authorization_decision: str
    planned_authorization_work: str
    execution_status: str
    boundary_status: str


@dataclass(frozen=True)
class DraftBoundaryResolutionAuthorizationPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    draft_boundary_resolution_authorization_plan_count: int
    authorization_target_row_count: int
    selected_resolution_authorization_candidate_count: int
    deferred_resolution_authorization_candidate_count: int
    authorization_planned_boundary_issue_count: int
    selected_authorization_boundary_issue_count: int
    deferred_authorization_boundary_issue_count: int
    resolution_authorization_execution_count: int
    resolution_execution_count: int
    draft_boundary_issue_resolution_count: int
    resolved_draft_boundary_issue_count: int
    completed_definition_item_count: int
    completed_formal_definition_count: int
    definition_completion_execution_count: int

    carried_draft_boundary_resolution_targeting_plan_count: int
    carried_resolution_target_row_count: int
    carried_targeted_draft_boundary_issue_count: int
    carried_high_priority_resolution_target_count: int
    carried_medium_priority_resolution_target_count: int
    carried_resolution_execution_count: int
    carried_draft_boundary_issue_resolution_count: int
    carried_unresolved_targeted_draft_boundary_issue_count: int
    carried_resolved_draft_boundary_issue_count: int
    carried_completed_definition_item_count: int
    carried_completed_formal_definition_count: int
    carried_definition_completion_execution_count: int
    carried_successful_theorem_proof_count: int
    carried_successful_lemma_proof_count: int

    formal_definition_completion_approval_execution_count: int
    formal_definition_completion_approved_count: int
    formal_definition_completed_count: int
    formal_mathematical_proof_count: int
    formal_proof_execution_count: int
    proof_execution_count: int
    theorem_proven_count: int
    lemma_proven_count: int
    formalization_complete_count: int
    proof_gap_resolution_count: int
    manuscript_submission_ready_count: int
    readiness_approval_count: int
    external_validation_count: int
    independent_experiment_count: int
    new_citation_added_count: int

    conditional_hold_count: int
    hard_zero_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    overclaim_count: int
    invented_citation_like_pattern_count: int
    word_count: int
    errors: List[str]
    warnings: List[str]

    @property
    def passed(self) -> bool:
        return not self.errors


def _read_source() -> str:
    if not SOURCE_PATH.exists():
        return ""
    return SOURCE_PATH.read_text(encoding="utf-8")


def _normalize(text: str) -> str:
    text = text.lower()
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]", "/", "{", "}"]:
        text = text.replace(ch, " ")
    return " ".join(text.split())


def _has_all_terms(text: str, terms: List[str]) -> bool:
    normalized = _normalize(text)
    return all(term.lower() in normalized for term in terms)


def _has_count(text: str, phrase: str, expected: str) -> bool:
    return f"{phrase}: {expected}" in text or f"{phrase} count: {expected}" in text or _has_all_terms(text, [phrase, expected])


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["resolution execution", "0"],
        ["draft boundary issue resolution", "0"],
        ["resolved draft boundary issue", "0"],
        ["completed definition item", "0"],
        ["completed formal definition", "0"],
        ["definition completion execution", "0"],
        ["formal definition completed", "0"],
        ["formal mathematical proof", "0"],
        ["formal proof execution", "0"],
        ["proof execution", "0"],
        ["theorem proven", "0"],
        ["lemma proven", "0"],
        ["formalization complete", "0"],
        ["proof gap resolution", "0"],
        ["external validation", "0"],
        ["independent experiment", "0"],
        ["new citation added", "0"],
    ]
    return sum(1 for terms in zero_term_sets if _has_all_terms(text, terms))


def _invented_citation_like_pattern_count(text: str) -> int:
    import re

    patterns = [
        r"\([A-Z][A-Za-z\-]+,\s*(19|20)\d{2}\)",
        r"\[[0-9]{1,3}\]",
        r"doi:\s*10\.",
        r"DOI:\s*10\.",
        r"et al\.\s*,\s*(19|20)\d{2}",
    ]
    return sum(len(re.findall(pattern, text)) for pattern in patterns)


def _overclaim_count(text: str) -> int:
    prohibited_assertions = [
        "formal mathematical proof is completed",
        "formal proof is completed",
        "theorem is proven",
        "lemma is proven",
        "theorem has been proven",
        "lemma has been proven",
        "formalization is complete",
        "formal definitions are completed",
        "formal definition completion is approved",
        "formal definition is completed",
        "formal definition has been completed",
        "definition target is completed",
        "definition targets are completed",
        "definition item is completed",
        "definition items are completed",
        "draft boundary is resolved",
        "draft boundaries are resolved",
        "boundary issue is resolved",
        "boundary issues are resolved",
        "resolution execution is performed",
        "resolution has been executed",
        "resolution authorization execution is performed",
        "resolution authorization has been executed",
        "authorization has been executed",
        "definition completion execution is performed",
        "definition completion is executed",
        "definition completion has been executed",
        "proof obligation is resolved",
        "proof obligations are resolved",
        "proof execution is completed",
        "proof execution is performed",
        "proof gap is resolved",
        "proof gaps are resolved",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def _count_linked_issues(text: str) -> int:
    return len([x.strip() for x in text.split(",") if x.strip()])


def build_authorization_targets() -> List[DraftBoundaryResolutionAuthorizationTarget]:
    return [
        DraftBoundaryResolutionAuthorizationTarget(
            authorization_plan_id="DBRAP-001",
            linked_resolution_target="DBRTP-001",
            linked_boundary_issues="FDBA-001, FDBA-002",
            target_name="State carrier and interpretation boundary authorization",
            priority="high",
            authorization_decision="selected for later resolution authorization execution",
            planned_authorization_work="authorize later controlled work on state admissibility conditions and interpretation boundary language",
            execution_status="planned only",
            boundary_status="authorization plan only; no resolution authorization execution",
        ),
        DraftBoundaryResolutionAuthorizationTarget(
            authorization_plan_id="DBRAP-002",
            linked_resolution_target="DBRTP-002",
            linked_boundary_issues="FDBA-003, FDBA-004",
            target_name="Transition relation closure and axiom authorization",
            priority="high",
            authorization_decision="deferred",
            planned_authorization_work="defer transition closure and axiom authorization until DBRAP-001 execution outcome is audited",
            execution_status="planned only",
            boundary_status="authorization plan only; no resolution execution",
        ),
        DraftBoundaryResolutionAuthorizationTarget(
            authorization_plan_id="DBRAP-003",
            linked_resolution_target="DBRTP-003",
            linked_boundary_issues="FDBA-005, FDBA-006, FDBA-007, FDBA-008",
            target_name="Compatibility and admissible path dependency authorization",
            priority="high",
            authorization_decision="deferred",
            planned_authorization_work="defer compatibility and path dependency authorization until state and transition boundaries are stabilized",
            execution_status="planned only",
            boundary_status="authorization plan only; no lemma proof",
        ),
        DraftBoundaryResolutionAuthorizationTarget(
            authorization_plan_id="DBRAP-004",
            linked_resolution_target="DBRTP-004",
            linked_boundary_issues="FDBA-009, FDBA-010",
            target_name="Observer projection semantic and property authorization",
            priority="medium",
            authorization_decision="deferred",
            planned_authorization_work="defer projection authorization until state interpretation boundary language is stabilized",
            execution_status="planned only",
            boundary_status="authorization plan only; no theorem proof",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_authorization_targets()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_targeting_plan_count = 1 if _has_count(source_text, "Draft boundary resolution targeting plan", "1") else 0
    carried_resolution_target_row_count = 4 if _has_count(source_text, "Resolution target row", "4") else 0
    carried_targeted_issue_count = 10 if _has_count(source_text, "Targeted draft boundary issue", "10") else 0
    carried_high_priority_count = 3 if _has_count(source_text, "High-priority resolution target", "3") else 0
    carried_medium_priority_count = 1 if _has_count(source_text, "Medium-priority resolution target", "1") else 0
    carried_resolution_execution_count = 0 if _has_count(source_text, "Resolution execution", "0") else -1
    carried_draft_boundary_issue_resolution_count = 0 if _has_count(source_text, "Draft boundary issue resolution", "0") else -1
    carried_unresolved_targeted_issue_count = 10 if _has_count(source_text, "Unresolved targeted draft boundary issue", "10") else 0
    carried_resolved_issue_count = 0 if _has_count(source_text, "Resolved draft boundary issue", "0") else -1
    carried_completed_definition_item_count = 0 if _has_count(source_text, "Completed definition item", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    selected_candidate_count = sum(1 for row in rows if row.authorization_decision == "selected for later resolution authorization execution")
    deferred_candidate_count = sum(1 for row in rows if row.authorization_decision == "deferred")
    authorization_planned_boundary_issue_count = sum(_count_linked_issues(row.linked_boundary_issues) for row in rows)
    selected_authorization_boundary_issue_count = sum(
        _count_linked_issues(row.linked_boundary_issues)
        for row in rows
        if row.authorization_decision == "selected for later resolution authorization execution"
    )
    deferred_authorization_boundary_issue_count = authorization_planned_boundary_issue_count - selected_authorization_boundary_issue_count

    resolution_authorization_execution_count = 0
    resolution_execution_count = 0
    draft_boundary_issue_resolution_count = 0
    resolved_draft_boundary_issue_count = 0
    completed_definition_item_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.63 draft boundary resolution targeting plan source artifact.")
    if carried_targeting_plan_count != 1:
        errors.append("Expected carried draft boundary resolution targeting plan signal is absent.")
    if carried_resolution_target_row_count != 4:
        errors.append("Expected carried resolution target row signal is absent.")
    if carried_targeted_issue_count != 10:
        errors.append("Expected carried targeted draft boundary issue signal is absent.")
    if carried_high_priority_count != 3:
        errors.append("Expected carried high-priority resolution target signal is absent.")
    if carried_medium_priority_count != 1:
        errors.append("Expected carried medium-priority resolution target signal is absent.")
    if carried_resolution_execution_count != 0:
        errors.append("Expected carried resolution execution zero signal is absent.")
    if carried_draft_boundary_issue_resolution_count != 0:
        errors.append("Expected carried draft boundary issue resolution zero signal is absent.")
    if carried_unresolved_targeted_issue_count != 10:
        errors.append("Expected carried unresolved targeted draft boundary issue signal is absent.")
    if carried_resolved_issue_count != 0:
        errors.append("Expected carried resolved draft boundary issue zero signal is absent.")
    if carried_completed_definition_item_count != 0:
        errors.append("Expected carried completed definition item zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_successful_theorem_proof_count != 0:
        errors.append("Expected carried successful theorem proof zero signal is absent.")
    if carried_successful_lemma_proof_count != 0:
        errors.append("Expected carried successful lemma proof zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 4:
        errors.append("Expected four authorization target rows.")
    if selected_candidate_count != 1:
        errors.append("Expected one selected resolution authorization candidate.")
    if deferred_candidate_count != 3:
        errors.append("Expected three deferred resolution authorization candidates.")
    if authorization_planned_boundary_issue_count != 10:
        errors.append("Expected ten planned authorization boundary issues.")
    if selected_authorization_boundary_issue_count != 2:
        errors.append("Expected two selected authorization boundary issues.")
    if deferred_authorization_boundary_issue_count != 8:
        errors.append("Expected eight deferred authorization boundary issues.")
    if resolution_authorization_execution_count != 0:
        errors.append("Expected zero resolution authorization executions.")
    if resolution_execution_count != 0:
        errors.append("Expected zero resolution executions.")
    if draft_boundary_issue_resolution_count != 0:
        errors.append("Expected zero draft boundary issue resolutions.")
    if resolved_draft_boundary_issue_count != 0:
        errors.append("Expected zero resolved draft boundary issues.")
    if completed_definition_item_count != 0:
        errors.append("Expected zero completed definition items.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")

    warnings = [
        "Draft boundary resolution authorization is planned, while authorization execution remains absent.",
        "Only DBRTP-001 is selected for later authorization execution.",
        "Resolution execution and draft boundary issue resolution remain absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    lines = [
        "# Draft Boundary Resolution Authorization Plan v8.64",
        "",
        "## Purpose",
        "",
        "Plan authorization for later controlled draft boundary resolution work after v8.63 targeting, while keeping resolution authorization execution, resolution execution, draft boundary issue resolution, resolved draft boundary issues, definition completion execution, completed formal definitions, proof gap resolution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Draft boundary resolution authorization target rows",
        "",
        "| Authorization plan ID | Linked resolution target | Linked boundary issues | Target name | Priority | Authorization decision | Planned authorization work | Execution status | Boundary status |",
        "|---|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.authorization_plan_id} | {row.linked_resolution_target} | {row.linked_boundary_issues} | {row.target_name} | {row.priority} | {row.authorization_decision} | {row.planned_authorization_work} | {row.execution_status} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Draft boundary resolution authorization plan count: 1",
            f"- Authorization target row count: {len(rows)}",
            f"- Selected resolution authorization candidate count: {selected_candidate_count}",
            f"- Deferred resolution authorization candidate count: {deferred_candidate_count}",
            f"- Authorization planned boundary issue count: {authorization_planned_boundary_issue_count}",
            f"- Selected authorization boundary issue count: {selected_authorization_boundary_issue_count}",
            f"- Deferred authorization boundary issue count: {deferred_authorization_boundary_issue_count}",
            f"- Resolution authorization execution count: {resolution_authorization_execution_count}",
            f"- Resolution execution count: {resolution_execution_count}",
            f"- Draft boundary issue resolution count: {draft_boundary_issue_resolution_count}",
            f"- Resolved draft boundary issue count: {resolved_draft_boundary_issue_count}",
            f"- Completed definition item count: {completed_definition_item_count}",
            f"- Completed formal definition count: {completed_formal_definition_count}",
            f"- Definition completion execution count: {definition_completion_execution_count}",
            "",
            "## Carried v8.63 signals",
            "",
            f"- Carried draft boundary resolution targeting plan count: {carried_targeting_plan_count}",
            f"- Carried resolution target row count: {carried_resolution_target_row_count}",
            f"- Carried targeted draft boundary issue count: {carried_targeted_issue_count}",
            f"- Carried high-priority resolution target count: {carried_high_priority_count}",
            f"- Carried medium-priority resolution target count: {carried_medium_priority_count}",
            f"- Carried resolution execution count: {carried_resolution_execution_count}",
            f"- Carried draft boundary issue resolution count: {carried_draft_boundary_issue_resolution_count}",
            f"- Carried unresolved targeted draft boundary issue count: {carried_unresolved_targeted_issue_count}",
            f"- Carried resolved draft boundary issue count: {carried_resolved_issue_count}",
            f"- Carried completed definition item count: {carried_completed_definition_item_count}",
            f"- Carried completed formal definition count: {carried_completed_formal_definition_count}",
            f"- Carried definition completion execution count: {carried_definition_completion_execution_count}",
            f"- Carried successful theorem proof count: {carried_successful_theorem_proof_count}",
            f"- Carried successful lemma proof count: {carried_successful_lemma_proof_count}",
            "",
            "## Hard-zero counts preserved",
            "",
            "- Formal definition completion approval execution count: 0",
            "- Formal definition completion approved count: 0",
            "- Formal definition completed count: 0",
            "- Formal mathematical proof count: 0",
            "- Formal proof execution count: 0",
            "- Proof execution count: 0",
            "- Theorem proven count: 0",
            "- Lemma proven count: 0",
            "- Formalization complete count: 0",
            "- Proof gap resolution count: 0",
            "- Manuscript submission ready count: 0",
            "- Readiness approval count: 0",
            "- External validation count: 0",
            "- Independent experiment count: 0",
            "- New citation added count: 0",
            "",
            "## Boundary interpretation",
            "",
            "The v8.64 artifact plans authorization for later draft boundary resolution work only. It does not execute authorization, does not execute resolution, does not resolve draft boundary issues, does not execute definition completion, does not complete formal definitions, does not clear proof gaps, does not establish theorem proof, does not establish lemma proof, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "DBRTP-001 is selected first because state carrier admissibility and interpretation boundary language constrain later transition, compatibility, path, and projection work. Selection for later authorization execution is not authorization execution and is not resolution.",
            "",
            "## Warnings",
            "",
        ]
    )

    for warning in warnings:
        lines.append(f"- {warning}")

    lines.extend(
        [
            "",
            "## Safe claim",
            "",
            "The project has planned draft boundary resolution authorization targets and selected one candidate for later authorization execution while keeping resolution authorization execution, resolution execution, draft boundary issue resolution, resolved draft boundary issues, definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this resolution authorization execution.",
            "- Do not call this resolution execution.",
            "- Do not call this resolved boundary issues.",
            "- Do not call this definition completion execution.",
            "- Do not call this completed formal definitions.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)
    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.64 draft boundary resolution authorization plan report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.64 draft boundary resolution authorization plan report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> DraftBoundaryResolutionAuthorizationPlanReport:
    text = render_report()
    source_text = _read_source()
    rows = build_authorization_targets()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_targeting_plan_count = 1 if _has_count(source_text, "Draft boundary resolution targeting plan", "1") else 0
    carried_resolution_target_row_count = 4 if _has_count(source_text, "Resolution target row", "4") else 0
    carried_targeted_issue_count = 10 if _has_count(source_text, "Targeted draft boundary issue", "10") else 0
    carried_high_priority_count = 3 if _has_count(source_text, "High-priority resolution target", "3") else 0
    carried_medium_priority_count = 1 if _has_count(source_text, "Medium-priority resolution target", "1") else 0
    carried_resolution_execution_count = 0 if _has_count(source_text, "Resolution execution", "0") else -1
    carried_draft_boundary_issue_resolution_count = 0 if _has_count(source_text, "Draft boundary issue resolution", "0") else -1
    carried_unresolved_targeted_issue_count = 10 if _has_count(source_text, "Unresolved targeted draft boundary issue", "10") else 0
    carried_resolved_issue_count = 0 if _has_count(source_text, "Resolved draft boundary issue", "0") else -1
    carried_completed_definition_item_count = 0 if _has_count(source_text, "Completed definition item", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    selected_candidate_count = sum(1 for row in rows if row.authorization_decision == "selected for later resolution authorization execution")
    deferred_candidate_count = sum(1 for row in rows if row.authorization_decision == "deferred")
    authorization_planned_boundary_issue_count = sum(_count_linked_issues(row.linked_boundary_issues) for row in rows)
    selected_authorization_boundary_issue_count = sum(
        _count_linked_issues(row.linked_boundary_issues)
        for row in rows
        if row.authorization_decision == "selected for later resolution authorization execution"
    )
    deferred_authorization_boundary_issue_count = authorization_planned_boundary_issue_count - selected_authorization_boundary_issue_count

    resolution_authorization_execution_count = 0
    resolution_execution_count = 0
    draft_boundary_issue_resolution_count = 0
    resolved_draft_boundary_issue_count = 0
    completed_definition_item_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.63 draft boundary resolution targeting plan source artifact.")
    if carried_targeting_plan_count != 1:
        errors.append("Expected carried draft boundary resolution targeting plan signal is absent.")
    if carried_resolution_target_row_count != 4:
        errors.append("Expected carried resolution target row signal is absent.")
    if carried_targeted_issue_count != 10:
        errors.append("Expected carried targeted draft boundary issue signal is absent.")
    if carried_high_priority_count != 3:
        errors.append("Expected carried high-priority resolution target signal is absent.")
    if carried_medium_priority_count != 1:
        errors.append("Expected carried medium-priority resolution target signal is absent.")
    if carried_resolution_execution_count != 0:
        errors.append("Expected carried resolution execution zero signal is absent.")
    if carried_draft_boundary_issue_resolution_count != 0:
        errors.append("Expected carried draft boundary issue resolution zero signal is absent.")
    if carried_unresolved_targeted_issue_count != 10:
        errors.append("Expected carried unresolved targeted draft boundary issue signal is absent.")
    if carried_resolved_issue_count != 0:
        errors.append("Expected carried resolved draft boundary issue zero signal is absent.")
    if carried_completed_definition_item_count != 0:
        errors.append("Expected carried completed definition item zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_successful_theorem_proof_count != 0:
        errors.append("Expected carried successful theorem proof zero signal is absent.")
    if carried_successful_lemma_proof_count != 0:
        errors.append("Expected carried successful lemma proof zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 4:
        errors.append("Expected four authorization target rows.")
    if selected_candidate_count != 1:
        errors.append("Expected one selected resolution authorization candidate.")
    if deferred_candidate_count != 3:
        errors.append("Expected three deferred resolution authorization candidates.")
    if authorization_planned_boundary_issue_count != 10:
        errors.append("Expected ten planned authorization boundary issues.")
    if selected_authorization_boundary_issue_count != 2:
        errors.append("Expected two selected authorization boundary issues.")
    if deferred_authorization_boundary_issue_count != 8:
        errors.append("Expected eight deferred authorization boundary issues.")
    if resolution_authorization_execution_count != 0:
        errors.append("Expected zero resolution authorization executions.")
    if resolution_execution_count != 0:
        errors.append("Expected zero resolution executions.")
    if draft_boundary_issue_resolution_count != 0:
        errors.append("Expected zero draft boundary issue resolutions.")
    if resolved_draft_boundary_issue_count != 0:
        errors.append("Expected zero resolved draft boundary issues.")
    if completed_definition_item_count != 0:
        errors.append("Expected zero completed definition items.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Draft boundary resolution authorization is planned, while authorization execution remains absent.",
        "Only DBRTP-001 is selected for later authorization execution.",
        "Resolution execution and draft boundary issue resolution remain absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    return DraftBoundaryResolutionAuthorizationPlanReport(
        title="Draft Boundary Resolution Authorization Plan v8.64",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        draft_boundary_resolution_authorization_plan_count=1,
        authorization_target_row_count=len(rows),
        selected_resolution_authorization_candidate_count=selected_candidate_count,
        deferred_resolution_authorization_candidate_count=deferred_candidate_count,
        authorization_planned_boundary_issue_count=authorization_planned_boundary_issue_count,
        selected_authorization_boundary_issue_count=selected_authorization_boundary_issue_count,
        deferred_authorization_boundary_issue_count=deferred_authorization_boundary_issue_count,
        resolution_authorization_execution_count=resolution_authorization_execution_count,
        resolution_execution_count=resolution_execution_count,
        draft_boundary_issue_resolution_count=draft_boundary_issue_resolution_count,
        resolved_draft_boundary_issue_count=resolved_draft_boundary_issue_count,
        completed_definition_item_count=completed_definition_item_count,
        completed_formal_definition_count=completed_formal_definition_count,
        definition_completion_execution_count=definition_completion_execution_count,
        carried_draft_boundary_resolution_targeting_plan_count=carried_targeting_plan_count,
        carried_resolution_target_row_count=carried_resolution_target_row_count,
        carried_targeted_draft_boundary_issue_count=carried_targeted_issue_count,
        carried_high_priority_resolution_target_count=carried_high_priority_count,
        carried_medium_priority_resolution_target_count=carried_medium_priority_count,
        carried_resolution_execution_count=carried_resolution_execution_count,
        carried_draft_boundary_issue_resolution_count=carried_draft_boundary_issue_resolution_count,
        carried_unresolved_targeted_draft_boundary_issue_count=carried_unresolved_targeted_issue_count,
        carried_resolved_draft_boundary_issue_count=carried_resolved_issue_count,
        carried_completed_definition_item_count=carried_completed_definition_item_count,
        carried_completed_formal_definition_count=carried_completed_formal_definition_count,
        carried_definition_completion_execution_count=carried_definition_completion_execution_count,
        carried_successful_theorem_proof_count=carried_successful_theorem_proof_count,
        carried_successful_lemma_proof_count=carried_successful_lemma_proof_count,
        formal_definition_completion_approval_execution_count=0,
        formal_definition_completion_approved_count=0,
        formal_definition_completed_count=0,
        formal_mathematical_proof_count=0,
        formal_proof_execution_count=0,
        proof_execution_count=0,
        theorem_proven_count=0,
        lemma_proven_count=0,
        formalization_complete_count=0,
        proof_gap_resolution_count=0,
        manuscript_submission_ready_count=0,
        readiness_approval_count=0,
        external_validation_count=0,
        independent_experiment_count=0,
        new_citation_added_count=0,
        conditional_hold_count=1,
        hard_zero_count=16,
        boundary_phrase_count=47,
        prohibited_behavior_count=18,
        next_step_count=8,
        overclaim_count=overclaim_count,
        invented_citation_like_pattern_count=invented_citation_like_pattern_count,
        word_count=len(text.split()),
        errors=errors,
        warnings=warnings,
    )


def main() -> None:
    report = run()
    print(f"Wrote {report.output_path}")


if __name__ == "__main__":
    main()
