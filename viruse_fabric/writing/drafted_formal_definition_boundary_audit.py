from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/first_controlled_formal_definition_drafting_execution_v8_61.md")
OUTPUT_PATH = Path("outputs/drafted_formal_definition_boundary_audit_v8_62.md")


@dataclass(frozen=True)
class DraftBoundaryIssue:
    issue_id: str
    linked_draft_item: str
    draft_name: str
    issue_type: str
    issue_description: str
    required_next_action: str
    resolution_status: str
    boundary_status: str


@dataclass(frozen=True)
class DraftedFormalDefinitionBoundaryAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    drafted_formal_definition_boundary_audit_count: int
    audited_drafted_definition_item_count: int
    draft_boundary_issue_count: int
    domain_boundary_issue_count: int
    axiom_boundary_issue_count: int
    semantic_boundary_issue_count: int
    dependency_boundary_issue_count: int
    unresolved_draft_boundary_issue_count: int
    resolved_draft_boundary_issue_count: int
    completed_definition_item_count: int
    completed_formal_definition_count: int
    definition_completion_execution_count: int
    formal_definition_completion_audit_required_count: int

    carried_controlled_formal_definition_drafting_execution_count: int
    carried_drafted_definition_package_count: int
    carried_drafted_definition_item_count: int
    carried_drafted_signature_count: int
    carried_unresolved_drafting_boundary_count: int
    carried_completed_definition_item_count: int
    carried_completed_formal_definition_count: int
    carried_formal_definition_completion_audit_required_count: int
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
        "boundary audit resolves",
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


def build_boundary_issues() -> List[DraftBoundaryIssue]:
    return [
        DraftBoundaryIssue(
            issue_id="FDBA-001",
            linked_draft_item="FDD-001",
            draft_name="State space draft",
            issue_type="domain boundary issue",
            issue_description="state membership is named, but admissibility criteria are not axiomatized",
            required_next_action="draft explicit admissibility conditions for S before completion review",
            resolution_status="unresolved",
            boundary_status="audit only; not a completed formal definition",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-002",
            linked_draft_item="FDD-001",
            draft_name="State space draft",
            issue_type="semantic boundary issue",
            issue_description="biological or observer-level interpretation of state elements remains intentionally absent",
            required_next_action="write interpretation boundary before any manuscript-level claim",
            resolution_status="unresolved",
            boundary_status="audit only; no external validation",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-003",
            linked_draft_item="FDD-002",
            draft_name="Transition relation draft",
            issue_type="domain boundary issue",
            issue_description="R is placed inside S x S, but temporal indexing and transition closure remain open",
            required_next_action="draft transition closure and indexing boundary conditions",
            resolution_status="unresolved",
            boundary_status="audit only; definition completion execution remains absent",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-004",
            linked_draft_item="FDD-002",
            draft_name="Transition relation draft",
            issue_type="axiom boundary issue",
            issue_description="no axioms specify determinism, nondeterminism, or admissible transition composition",
            required_next_action="separate minimal relation axioms from optional model assumptions",
            resolution_status="unresolved",
            boundary_status="audit only; no proof execution",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-005",
            linked_draft_item="FDD-003",
            draft_name="Compatibility predicate draft",
            issue_type="axiom boundary issue",
            issue_description="compatibility predicate lacks reflexive, symmetric, transitive, or path-specific constraints",
            required_next_action="draft explicit compatibility axiom options and reject overstrong assumptions",
            resolution_status="unresolved",
            boundary_status="audit only; no lemma proof",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-006",
            linked_draft_item="FDD-003",
            draft_name="Compatibility predicate draft",
            issue_type="dependency boundary issue",
            issue_description="relation between Comp and transition relation R remains undefined",
            required_next_action="map Comp-R dependency before any path compatibility lemma attempt",
            resolution_status="unresolved",
            boundary_status="audit only; proof gap resolution remains absent",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-007",
            linked_draft_item="FDD-004",
            draft_name="Admissible path predicate draft",
            issue_type="domain boundary issue",
            issue_description="finite sequence domain is named, but length rules and boundary endpoints remain open",
            required_next_action="draft finite path schema and endpoint conditions",
            resolution_status="unresolved",
            boundary_status="audit only; not a completed formal definition",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-008",
            linked_draft_item="FDD-004",
            draft_name="Admissible path predicate draft",
            issue_type="dependency boundary issue",
            issue_description="PathAdm dependency on R and Comp remains unaudited",
            required_next_action="write dependency graph among S, R, Comp, and PathAdm",
            resolution_status="unresolved",
            boundary_status="audit only; theorem proof remains absent",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-009",
            linked_draft_item="FDD-005",
            draft_name="Observer projection draft",
            issue_type="semantic boundary issue",
            issue_description="projection codomain descriptors and observer semantics remain unspecified",
            required_next_action="draft codomain descriptor schema and observer boundary language",
            resolution_status="unresolved",
            boundary_status="audit only; no biological prediction",
        ),
        DraftBoundaryIssue(
            issue_id="FDBA-010",
            linked_draft_item="FDD-005",
            draft_name="Observer projection draft",
            issue_type="axiom boundary issue",
            issue_description="projection properties such as invariance, equivalence, and information loss are not stated",
            required_next_action="draft projection property options and mark which are assumptions",
            resolution_status="unresolved",
            boundary_status="audit only; no theorem proof",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_boundary_issues()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_controlled_drafting_execution_count = 1 if _has_count(source_text, "Controlled formal definition drafting execution", "1") else 0
    carried_drafted_definition_package_count = 1 if _has_count(source_text, "Drafted definition package", "1") else 0
    carried_drafted_definition_item_count = 5 if _has_count(source_text, "Drafted definition item", "5") else 0
    carried_drafted_signature_count = 5 if _has_count(source_text, "Drafted signature", "5") else 0
    carried_unresolved_drafting_boundary_count = 5 if _has_count(source_text, "Unresolved drafting boundary", "5") else 0
    carried_completed_definition_item_count = 0 if _has_count(source_text, "Completed definition item", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_formal_definition_completion_audit_required_count = 1 if _has_count(source_text, "Formal definition completion audit required", "1") else 0
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    domain_boundary_issue_count = sum(1 for row in rows if row.issue_type == "domain boundary issue")
    axiom_boundary_issue_count = sum(1 for row in rows if row.issue_type == "axiom boundary issue")
    semantic_boundary_issue_count = sum(1 for row in rows if row.issue_type == "semantic boundary issue")
    dependency_boundary_issue_count = sum(1 for row in rows if row.issue_type == "dependency boundary issue")
    unresolved_draft_boundary_issue_count = sum(1 for row in rows if row.resolution_status == "unresolved")
    resolved_draft_boundary_issue_count = sum(1 for row in rows if row.resolution_status == "resolved")
    completed_definition_item_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0
    formal_definition_completion_audit_required_count = 1

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.61 drafting source artifact.")
    if carried_controlled_drafting_execution_count != 1:
        errors.append("Expected carried controlled drafting execution signal is absent.")
    if carried_drafted_definition_package_count != 1:
        errors.append("Expected carried drafted definition package signal is absent.")
    if carried_drafted_definition_item_count != 5:
        errors.append("Expected carried drafted definition item signal is absent.")
    if carried_drafted_signature_count != 5:
        errors.append("Expected carried drafted signature signal is absent.")
    if carried_unresolved_drafting_boundary_count != 5:
        errors.append("Expected carried unresolved drafting boundary signal is absent.")
    if carried_completed_definition_item_count != 0:
        errors.append("Expected carried completed definition item zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_formal_definition_completion_audit_required_count != 1:
        errors.append("Expected carried formal definition completion audit required signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_successful_theorem_proof_count != 0:
        errors.append("Expected carried successful theorem proof zero signal is absent.")
    if carried_successful_lemma_proof_count != 0:
        errors.append("Expected carried successful lemma proof zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 10:
        errors.append("Expected ten draft boundary issues.")
    if domain_boundary_issue_count != 3:
        errors.append("Expected three domain boundary issues.")
    if axiom_boundary_issue_count != 3:
        errors.append("Expected three axiom boundary issues.")
    if semantic_boundary_issue_count != 2:
        errors.append("Expected two semantic boundary issues.")
    if dependency_boundary_issue_count != 2:
        errors.append("Expected two dependency boundary issues.")
    if unresolved_draft_boundary_issue_count != 10:
        errors.append("Expected ten unresolved draft boundary issues.")
    if resolved_draft_boundary_issue_count != 0:
        errors.append("Expected zero resolved draft boundary issues.")
    if completed_definition_item_count != 0:
        errors.append("Expected zero completed definition items.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")

    warnings = [
        "Drafted formal definitions are audited but not completed.",
        "All draft boundary issues remain unresolved.",
        "Definition completion execution remains absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    lines = [
        "# Drafted Formal Definition Boundary Audit v8.62",
        "",
        "## Purpose",
        "",
        "Audit boundaries of the five FDCT-001 drafted definition items from v8.61 while keeping draft boundary issue resolution, definition completion execution, completed formal definitions, proof gap resolution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Draft boundary issue rows",
        "",
        "| Issue ID | Linked draft item | Draft name | Issue type | Issue description | Required next action | Resolution status | Boundary status |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.issue_id} | {row.linked_draft_item} | {row.draft_name} | {row.issue_type} | {row.issue_description} | {row.required_next_action} | {row.resolution_status} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Drafted formal definition boundary audit count: 1",
            "- Audited drafted definition item count: 5",
            f"- Draft boundary issue count: {len(rows)}",
            f"- Domain boundary issue count: {domain_boundary_issue_count}",
            f"- Axiom boundary issue count: {axiom_boundary_issue_count}",
            f"- Semantic boundary issue count: {semantic_boundary_issue_count}",
            f"- Dependency boundary issue count: {dependency_boundary_issue_count}",
            f"- Unresolved draft boundary issue count: {unresolved_draft_boundary_issue_count}",
            f"- Resolved draft boundary issue count: {resolved_draft_boundary_issue_count}",
            f"- Completed definition item count: {completed_definition_item_count}",
            f"- Completed formal definition count: {completed_formal_definition_count}",
            f"- Definition completion execution count: {definition_completion_execution_count}",
            f"- Formal definition completion audit required count: {formal_definition_completion_audit_required_count}",
            "",
            "## Carried v8.61 signals",
            "",
            f"- Carried controlled formal definition drafting execution count: {carried_controlled_drafting_execution_count}",
            f"- Carried drafted definition package count: {carried_drafted_definition_package_count}",
            f"- Carried drafted definition item count: {carried_drafted_definition_item_count}",
            f"- Carried drafted signature count: {carried_drafted_signature_count}",
            f"- Carried unresolved drafting boundary count: {carried_unresolved_drafting_boundary_count}",
            f"- Carried completed definition item count: {carried_completed_definition_item_count}",
            f"- Carried completed formal definition count: {carried_completed_formal_definition_count}",
            f"- Carried formal definition completion audit required count: {carried_formal_definition_completion_audit_required_count}",
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
            "The v8.62 artifact audits boundary issues in drafted formal definition items only. It does not resolve draft boundary issues, does not execute definition completion, does not complete formal definitions, does not clear proof gaps, does not establish theorem proof, does not establish lemma proof, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "The five drafted items are useful scaffolding, but each remains blocked by domain, axiom, semantic, or dependency boundary issues. Completion cannot be claimed until a later milestone resolves and audits those boundaries.",
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
            "The project has audited ten boundary issues across five drafted formal definition items while keeping all draft boundary issues unresolved and keeping definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this resolved boundary issues.",
            "- Do not call this definition completion execution.",
            "- Do not call this completed formal definitions.",
            "- Do not call this formal proof.",
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
        errors.append("Overclaim pattern detected in v8.62 drafted formal definition boundary audit report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.62 drafted formal definition boundary audit report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> DraftedFormalDefinitionBoundaryAuditReport:
    text = render_report()
    source_text = _read_source()
    rows = build_boundary_issues()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_controlled_drafting_execution_count = 1 if _has_count(source_text, "Controlled formal definition drafting execution", "1") else 0
    carried_drafted_definition_package_count = 1 if _has_count(source_text, "Drafted definition package", "1") else 0
    carried_drafted_definition_item_count = 5 if _has_count(source_text, "Drafted definition item", "5") else 0
    carried_drafted_signature_count = 5 if _has_count(source_text, "Drafted signature", "5") else 0
    carried_unresolved_drafting_boundary_count = 5 if _has_count(source_text, "Unresolved drafting boundary", "5") else 0
    carried_completed_definition_item_count = 0 if _has_count(source_text, "Completed definition item", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_formal_definition_completion_audit_required_count = 1 if _has_count(source_text, "Formal definition completion audit required", "1") else 0
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    domain_boundary_issue_count = sum(1 for row in rows if row.issue_type == "domain boundary issue")
    axiom_boundary_issue_count = sum(1 for row in rows if row.issue_type == "axiom boundary issue")
    semantic_boundary_issue_count = sum(1 for row in rows if row.issue_type == "semantic boundary issue")
    dependency_boundary_issue_count = sum(1 for row in rows if row.issue_type == "dependency boundary issue")
    unresolved_draft_boundary_issue_count = sum(1 for row in rows if row.resolution_status == "unresolved")
    resolved_draft_boundary_issue_count = sum(1 for row in rows if row.resolution_status == "resolved")
    completed_definition_item_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0
    formal_definition_completion_audit_required_count = 1

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.61 drafting source artifact.")
    if carried_controlled_drafting_execution_count != 1:
        errors.append("Expected carried controlled drafting execution signal is absent.")
    if carried_drafted_definition_package_count != 1:
        errors.append("Expected carried drafted definition package signal is absent.")
    if carried_drafted_definition_item_count != 5:
        errors.append("Expected carried drafted definition item signal is absent.")
    if carried_drafted_signature_count != 5:
        errors.append("Expected carried drafted signature signal is absent.")
    if carried_unresolved_drafting_boundary_count != 5:
        errors.append("Expected carried unresolved drafting boundary signal is absent.")
    if carried_completed_definition_item_count != 0:
        errors.append("Expected carried completed definition item zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_formal_definition_completion_audit_required_count != 1:
        errors.append("Expected carried formal definition completion audit required signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_successful_theorem_proof_count != 0:
        errors.append("Expected carried successful theorem proof zero signal is absent.")
    if carried_successful_lemma_proof_count != 0:
        errors.append("Expected carried successful lemma proof zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 10:
        errors.append("Expected ten draft boundary issues.")
    if domain_boundary_issue_count != 3:
        errors.append("Expected three domain boundary issues.")
    if axiom_boundary_issue_count != 3:
        errors.append("Expected three axiom boundary issues.")
    if semantic_boundary_issue_count != 2:
        errors.append("Expected two semantic boundary issues.")
    if dependency_boundary_issue_count != 2:
        errors.append("Expected two dependency boundary issues.")
    if unresolved_draft_boundary_issue_count != 10:
        errors.append("Expected ten unresolved draft boundary issues.")
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
        "Drafted formal definitions are audited but not completed.",
        "All draft boundary issues remain unresolved.",
        "Definition completion execution remains absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    return DraftedFormalDefinitionBoundaryAuditReport(
        title="Drafted Formal Definition Boundary Audit v8.62",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        drafted_formal_definition_boundary_audit_count=1,
        audited_drafted_definition_item_count=5,
        draft_boundary_issue_count=len(rows),
        domain_boundary_issue_count=domain_boundary_issue_count,
        axiom_boundary_issue_count=axiom_boundary_issue_count,
        semantic_boundary_issue_count=semantic_boundary_issue_count,
        dependency_boundary_issue_count=dependency_boundary_issue_count,
        unresolved_draft_boundary_issue_count=unresolved_draft_boundary_issue_count,
        resolved_draft_boundary_issue_count=resolved_draft_boundary_issue_count,
        completed_definition_item_count=completed_definition_item_count,
        completed_formal_definition_count=completed_formal_definition_count,
        definition_completion_execution_count=definition_completion_execution_count,
        formal_definition_completion_audit_required_count=formal_definition_completion_audit_required_count,
        carried_controlled_formal_definition_drafting_execution_count=carried_controlled_drafting_execution_count,
        carried_drafted_definition_package_count=carried_drafted_definition_package_count,
        carried_drafted_definition_item_count=carried_drafted_definition_item_count,
        carried_drafted_signature_count=carried_drafted_signature_count,
        carried_unresolved_drafting_boundary_count=carried_unresolved_drafting_boundary_count,
        carried_completed_definition_item_count=carried_completed_definition_item_count,
        carried_completed_formal_definition_count=carried_completed_formal_definition_count,
        carried_formal_definition_completion_audit_required_count=carried_formal_definition_completion_audit_required_count,
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
        boundary_phrase_count=45,
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
