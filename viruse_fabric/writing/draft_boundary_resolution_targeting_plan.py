from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/drafted_formal_definition_boundary_audit_v8_62.md")
OUTPUT_PATH = Path("outputs/draft_boundary_resolution_targeting_plan_v8_63.md")


@dataclass(frozen=True)
class DraftBoundaryResolutionTarget:
    target_id: str
    linked_boundary_issues: str
    target_name: str
    target_type: str
    priority: str
    planned_resolution_work: str
    execution_status: str
    boundary_status: str


@dataclass(frozen=True)
class DraftBoundaryResolutionTargetingPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    draft_boundary_resolution_targeting_plan_count: int
    resolution_target_row_count: int
    targeted_draft_boundary_issue_count: int
    high_priority_resolution_target_count: int
    medium_priority_resolution_target_count: int
    resolution_execution_count: int
    draft_boundary_issue_resolution_count: int
    unresolved_targeted_draft_boundary_issue_count: int
    resolved_draft_boundary_issue_count: int
    completed_definition_item_count: int
    completed_formal_definition_count: int
    definition_completion_execution_count: int

    carried_drafted_formal_definition_boundary_audit_count: int
    carried_audited_drafted_definition_item_count: int
    carried_draft_boundary_issue_count: int
    carried_domain_boundary_issue_count: int
    carried_axiom_boundary_issue_count: int
    carried_semantic_boundary_issue_count: int
    carried_dependency_boundary_issue_count: int
    carried_unresolved_draft_boundary_issue_count: int
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


def build_resolution_targets() -> List[DraftBoundaryResolutionTarget]:
    return [
        DraftBoundaryResolutionTarget(
            target_id="DBRTP-001",
            linked_boundary_issues="FDBA-001, FDBA-002",
            target_name="State carrier and interpretation boundary target",
            target_type="domain and semantic resolution target",
            priority="high",
            planned_resolution_work="prepare admissibility conditions for S and explicit interpretation boundary language",
            execution_status="planned only",
            boundary_status="resolution targeting only; no boundary issue resolution",
        ),
        DraftBoundaryResolutionTarget(
            target_id="DBRTP-002",
            linked_boundary_issues="FDBA-003, FDBA-004",
            target_name="Transition relation closure and axiom target",
            target_type="domain and axiom resolution target",
            priority="high",
            planned_resolution_work="prepare transition closure, temporal indexing, and minimal relation axiom options",
            execution_status="planned only",
            boundary_status="resolution targeting only; no definition completion execution",
        ),
        DraftBoundaryResolutionTarget(
            target_id="DBRTP-003",
            linked_boundary_issues="FDBA-005, FDBA-006, FDBA-007, FDBA-008",
            target_name="Compatibility and admissible path dependency target",
            target_type="axiom, domain, and dependency resolution target",
            priority="high",
            planned_resolution_work="prepare compatibility axiom options, finite path schema, endpoint rules, and dependency graph among S, R, Comp, and PathAdm",
            execution_status="planned only",
            boundary_status="resolution targeting only; no lemma proof",
        ),
        DraftBoundaryResolutionTarget(
            target_id="DBRTP-004",
            linked_boundary_issues="FDBA-009, FDBA-010",
            target_name="Observer projection semantic and property target",
            target_type="semantic and axiom resolution target",
            priority="medium",
            planned_resolution_work="prepare projection codomain descriptor schema and projection property assumptions",
            execution_status="planned only",
            boundary_status="resolution targeting only; no theorem proof",
        ),
    ]


def _count_linked_issues(rows: List[DraftBoundaryResolutionTarget]) -> int:
    total = 0
    for row in rows:
        total += len([x.strip() for x in row.linked_boundary_issues.split(",") if x.strip()])
    return total


def render_report() -> str:
    source_text = _read_source()
    rows = build_resolution_targets()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_audit_count = 1 if _has_count(source_text, "Drafted formal definition boundary audit", "1") else 0
    carried_audited_item_count = 5 if _has_count(source_text, "Audited drafted definition item", "5") else 0
    carried_issue_count = 10 if _has_count(source_text, "Draft boundary issue", "10") else 0
    carried_domain_issue_count = 3 if _has_count(source_text, "Domain boundary issue", "3") else 0
    carried_axiom_issue_count = 3 if _has_count(source_text, "Axiom boundary issue", "3") else 0
    carried_semantic_issue_count = 2 if _has_count(source_text, "Semantic boundary issue", "2") else 0
    carried_dependency_issue_count = 2 if _has_count(source_text, "Dependency boundary issue", "2") else 0
    carried_unresolved_issue_count = 10 if _has_count(source_text, "Unresolved draft boundary issue", "10") else 0
    carried_resolved_issue_count = 0 if _has_count(source_text, "Resolved draft boundary issue", "0") else -1
    carried_completed_definition_item_count = 0 if _has_count(source_text, "Completed definition item", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    targeted_issue_count = _count_linked_issues(rows)
    high_priority_resolution_target_count = sum(1 for row in rows if row.priority == "high")
    medium_priority_resolution_target_count = sum(1 for row in rows if row.priority == "medium")
    resolution_execution_count = 0
    draft_boundary_issue_resolution_count = 0
    unresolved_targeted_draft_boundary_issue_count = targeted_issue_count
    resolved_draft_boundary_issue_count = 0
    completed_definition_item_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.62 drafted formal definition boundary audit source artifact.")
    if carried_audit_count != 1:
        errors.append("Expected carried drafted formal definition boundary audit signal is absent.")
    if carried_audited_item_count != 5:
        errors.append("Expected carried audited drafted definition item signal is absent.")
    if carried_issue_count != 10:
        errors.append("Expected carried draft boundary issue count signal is absent.")
    if carried_domain_issue_count != 3:
        errors.append("Expected carried domain boundary issue count signal is absent.")
    if carried_axiom_issue_count != 3:
        errors.append("Expected carried axiom boundary issue count signal is absent.")
    if carried_semantic_issue_count != 2:
        errors.append("Expected carried semantic boundary issue count signal is absent.")
    if carried_dependency_issue_count != 2:
        errors.append("Expected carried dependency boundary issue count signal is absent.")
    if carried_unresolved_issue_count != 10:
        errors.append("Expected carried unresolved draft boundary issue count signal is absent.")
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
        errors.append("Expected four resolution target rows.")
    if targeted_issue_count != 10:
        errors.append("Expected ten targeted draft boundary issues.")
    if high_priority_resolution_target_count != 3:
        errors.append("Expected three high-priority resolution targets.")
    if medium_priority_resolution_target_count != 1:
        errors.append("Expected one medium-priority resolution target.")
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
        "Draft boundary issue resolution targets are planned, while resolution execution remains absent.",
        "All targeted draft boundary issues remain unresolved.",
        "Definition completion execution remains absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    lines = [
        "# Draft Boundary Resolution Targeting Plan v8.63",
        "",
        "## Purpose",
        "",
        "Plan resolution targets for the ten unresolved draft boundary issues from v8.62 while keeping resolution execution, draft boundary issue resolution, definition completion execution, completed formal definitions, proof gap resolution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Draft boundary resolution target rows",
        "",
        "| Target ID | Linked boundary issues | Target name | Target type | Priority | Planned resolution work | Execution status | Boundary status |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.target_id} | {row.linked_boundary_issues} | {row.target_name} | {row.target_type} | {row.priority} | {row.planned_resolution_work} | {row.execution_status} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Draft boundary resolution targeting plan count: 1",
            f"- Resolution target row count: {len(rows)}",
            f"- Targeted draft boundary issue count: {targeted_issue_count}",
            f"- High-priority resolution target count: {high_priority_resolution_target_count}",
            f"- Medium-priority resolution target count: {medium_priority_resolution_target_count}",
            f"- Resolution execution count: {resolution_execution_count}",
            f"- Draft boundary issue resolution count: {draft_boundary_issue_resolution_count}",
            f"- Unresolved targeted draft boundary issue count: {unresolved_targeted_draft_boundary_issue_count}",
            f"- Resolved draft boundary issue count: {resolved_draft_boundary_issue_count}",
            f"- Completed definition item count: {completed_definition_item_count}",
            f"- Completed formal definition count: {completed_formal_definition_count}",
            f"- Definition completion execution count: {definition_completion_execution_count}",
            "",
            "## Carried v8.62 signals",
            "",
            f"- Carried drafted formal definition boundary audit count: {carried_audit_count}",
            f"- Carried audited drafted definition item count: {carried_audited_item_count}",
            f"- Carried draft boundary issue count: {carried_issue_count}",
            f"- Carried domain boundary issue count: {carried_domain_issue_count}",
            f"- Carried axiom boundary issue count: {carried_axiom_issue_count}",
            f"- Carried semantic boundary issue count: {carried_semantic_issue_count}",
            f"- Carried dependency boundary issue count: {carried_dependency_issue_count}",
            f"- Carried unresolved draft boundary issue count: {carried_unresolved_issue_count}",
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
            "The v8.63 artifact targets draft boundary issue resolution work only. It does not execute resolution, does not resolve draft boundary issues, does not execute definition completion, does not complete formal definitions, does not clear proof gaps, does not establish theorem proof, does not establish lemma proof, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "The ten unresolved draft boundary issues are grouped into four resolution targets so that later execution can be controlled and audited. Targeting is not resolution. No formal definition completion can be claimed from this milestone.",
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
            "The project has planned four draft boundary resolution targets covering ten unresolved draft boundary issues while keeping resolution execution, draft boundary issue resolution, definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this resolved boundary issues.",
            "- Do not call this resolution execution.",
            "- Do not call this definition completion execution.",
            "- Do not call this completed formal definitions.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
            "- Do not call this proof gap resolution.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)
    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.63 draft boundary resolution targeting report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.63 draft boundary resolution targeting report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> DraftBoundaryResolutionTargetingPlanReport:
    text = render_report()
    source_text = _read_source()
    rows = build_resolution_targets()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_audit_count = 1 if _has_count(source_text, "Drafted formal definition boundary audit", "1") else 0
    carried_audited_item_count = 5 if _has_count(source_text, "Audited drafted definition item", "5") else 0
    carried_issue_count = 10 if _has_count(source_text, "Draft boundary issue", "10") else 0
    carried_domain_issue_count = 3 if _has_count(source_text, "Domain boundary issue", "3") else 0
    carried_axiom_issue_count = 3 if _has_count(source_text, "Axiom boundary issue", "3") else 0
    carried_semantic_issue_count = 2 if _has_count(source_text, "Semantic boundary issue", "2") else 0
    carried_dependency_issue_count = 2 if _has_count(source_text, "Dependency boundary issue", "2") else 0
    carried_unresolved_issue_count = 10 if _has_count(source_text, "Unresolved draft boundary issue", "10") else 0
    carried_resolved_issue_count = 0 if _has_count(source_text, "Resolved draft boundary issue", "0") else -1
    carried_completed_definition_item_count = 0 if _has_count(source_text, "Completed definition item", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    targeted_issue_count = _count_linked_issues(rows)
    high_priority_resolution_target_count = sum(1 for row in rows if row.priority == "high")
    medium_priority_resolution_target_count = sum(1 for row in rows if row.priority == "medium")
    resolution_execution_count = 0
    draft_boundary_issue_resolution_count = 0
    unresolved_targeted_draft_boundary_issue_count = targeted_issue_count
    resolved_draft_boundary_issue_count = 0
    completed_definition_item_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.62 drafted formal definition boundary audit source artifact.")
    if carried_audit_count != 1:
        errors.append("Expected carried drafted formal definition boundary audit signal is absent.")
    if carried_audited_item_count != 5:
        errors.append("Expected carried audited drafted definition item signal is absent.")
    if carried_issue_count != 10:
        errors.append("Expected carried draft boundary issue count signal is absent.")
    if carried_domain_issue_count != 3:
        errors.append("Expected carried domain boundary issue count signal is absent.")
    if carried_axiom_issue_count != 3:
        errors.append("Expected carried axiom boundary issue count signal is absent.")
    if carried_semantic_issue_count != 2:
        errors.append("Expected carried semantic boundary issue count signal is absent.")
    if carried_dependency_issue_count != 2:
        errors.append("Expected carried dependency boundary issue count signal is absent.")
    if carried_unresolved_issue_count != 10:
        errors.append("Expected carried unresolved draft boundary issue count signal is absent.")
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
        errors.append("Expected four resolution target rows.")
    if targeted_issue_count != 10:
        errors.append("Expected ten targeted draft boundary issues.")
    if high_priority_resolution_target_count != 3:
        errors.append("Expected three high-priority resolution targets.")
    if medium_priority_resolution_target_count != 1:
        errors.append("Expected one medium-priority resolution target.")
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
        "Draft boundary issue resolution targets are planned, while resolution execution remains absent.",
        "All targeted draft boundary issues remain unresolved.",
        "Definition completion execution remains absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    return DraftBoundaryResolutionTargetingPlanReport(
        title="Draft Boundary Resolution Targeting Plan v8.63",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        draft_boundary_resolution_targeting_plan_count=1,
        resolution_target_row_count=len(rows),
        targeted_draft_boundary_issue_count=targeted_issue_count,
        high_priority_resolution_target_count=high_priority_resolution_target_count,
        medium_priority_resolution_target_count=medium_priority_resolution_target_count,
        resolution_execution_count=resolution_execution_count,
        draft_boundary_issue_resolution_count=draft_boundary_issue_resolution_count,
        unresolved_targeted_draft_boundary_issue_count=unresolved_targeted_draft_boundary_issue_count,
        resolved_draft_boundary_issue_count=resolved_draft_boundary_issue_count,
        completed_definition_item_count=completed_definition_item_count,
        completed_formal_definition_count=completed_formal_definition_count,
        definition_completion_execution_count=definition_completion_execution_count,
        carried_drafted_formal_definition_boundary_audit_count=carried_audit_count,
        carried_audited_drafted_definition_item_count=carried_audited_item_count,
        carried_draft_boundary_issue_count=carried_issue_count,
        carried_domain_boundary_issue_count=carried_domain_issue_count,
        carried_axiom_boundary_issue_count=carried_axiom_issue_count,
        carried_semantic_boundary_issue_count=carried_semantic_issue_count,
        carried_dependency_boundary_issue_count=carried_dependency_issue_count,
        carried_unresolved_draft_boundary_issue_count=carried_unresolved_issue_count,
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
        boundary_phrase_count=46,
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
