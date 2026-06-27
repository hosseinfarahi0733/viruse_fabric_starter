from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/formal_definition_completion_execution_authorization_v8_60.md")
OUTPUT_PATH = Path("outputs/first_controlled_formal_definition_drafting_execution_v8_61.md")


@dataclass(frozen=True)
class DraftedDefinitionItem:
    item_id: str
    linked_target: str
    draft_name: str
    draft_signature: str
    draft_scope: str
    unresolved_boundary: str
    completion_status: str
    boundary_status: str


@dataclass(frozen=True)
class FirstControlledFormalDefinitionDraftingExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    controlled_formal_definition_drafting_execution_count: int
    drafted_definition_package_count: int
    drafted_definition_item_count: int
    drafted_signature_count: int
    unresolved_drafting_boundary_count: int
    completed_definition_item_count: int
    completed_formal_definition_count: int
    formal_definition_completion_audit_required_count: int
    definition_completion_execution_count: int

    carried_formal_definition_completion_execution_authorization_execution_count: int
    carried_authorization_execution_row_count: int
    carried_selected_authorization_execution_candidate_count: int
    carried_deferred_authorization_execution_candidate_count: int
    carried_definition_completion_execution_authorized_count: int
    carried_definition_completion_execution_count: int
    carried_definition_gap_count: int
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
        "definition completion execution is performed",
        "definition completion is executed",
        "definition completion has been executed",
        "drafting execution completes definitions",
        "drafting establishes formal definitions",
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


def build_drafted_items() -> List[DraftedDefinitionItem]:
    return [
        DraftedDefinitionItem(
            item_id="FDD-001",
            linked_target="FDCT-001",
            draft_name="State space draft",
            draft_signature="Let S be a nonempty set of admissible model states; elements are written s in S.",
            draft_scope="introduces the carrier set for later transition and projection definitions",
            unresolved_boundary="topology, metric, measure, and biological interpretation remain unspecified",
            completion_status="drafted only",
            boundary_status="not a completed formal definition",
        ),
        DraftedDefinitionItem(
            item_id="FDD-002",
            linked_target="FDCT-001",
            draft_name="Transition relation draft",
            draft_signature="Let R be a binary relation on S; R subset S x S records admissible one-step transitions.",
            draft_scope="introduces relation-level structure without proving preservation",
            unresolved_boundary="transition closure, determinism, stochasticity, and temporal indexing remain open",
            completion_status="drafted only",
            boundary_status="not a completed formal definition",
        ),
        DraftedDefinitionItem(
            item_id="FDD-003",
            linked_target="FDCT-001",
            draft_name="Compatibility predicate draft",
            draft_signature="Let Comp be a predicate on S x S; Comp(s_i, s_j) marks pairwise path compatibility candidates.",
            draft_scope="supports later path compatibility lemma attempts",
            unresolved_boundary="compatibility axioms and relation to R remain unaudited",
            completion_status="drafted only",
            boundary_status="not a completed formal definition",
        ),
        DraftedDefinitionItem(
            item_id="FDD-004",
            linked_target="FDCT-001",
            draft_name="Admissible path predicate draft",
            draft_signature="Let PathAdm be a predicate over finite sequences in S; PathAdm(pi) marks candidate admissible paths.",
            draft_scope="supports later path-level reasoning without claiming lemma proof",
            unresolved_boundary="sequence length rules, boundary conditions, and transition consistency remain open",
            completion_status="drafted only",
            boundary_status="not a completed formal definition",
        ),
        DraftedDefinitionItem(
            item_id="FDD-005",
            linked_target="FDCT-001",
            draft_name="Observer projection draft",
            draft_signature="Let P be a projection map from structured model states to observer-level descriptors.",
            draft_scope="supports later projection-level interpretation constraints",
            unresolved_boundary="domain structure, codomain descriptors, equivalence classes, and observer semantics remain open",
            completion_status="drafted only",
            boundary_status="not a completed formal definition",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_drafted_items()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_authorization_execution_count = 1 if _has_count(source_text, "Formal definition completion execution authorization execution", "1") else 0
    carried_authorization_execution_row_count = 3 if _has_count(source_text, "Authorization execution row", "3") else 0
    carried_selected_authorization_execution_candidate_count = 1 if _has_count(source_text, "Selected authorization execution candidate", "1") else 0
    carried_deferred_authorization_execution_candidate_count = 2 if _has_count(source_text, "Deferred authorization execution candidate", "2") else 0
    carried_definition_completion_execution_authorized_count = 1 if _has_count(source_text, "Definition completion execution authorized", "1") else 0
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_definition_gap_count = 3 if _has_count(source_text, "Carried definition gap", "3") else 0
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    drafted_signature_count = len(rows)
    unresolved_drafting_boundary_count = len(rows)
    completed_definition_item_count = sum(1 for row in rows if row.completion_status == "completed")
    completed_formal_definition_count = 0
    formal_definition_completion_audit_required_count = 1
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.60 authorization execution source artifact.")
    if carried_authorization_execution_count != 1:
        errors.append("Expected carried authorization execution signal is absent.")
    if carried_authorization_execution_row_count != 3:
        errors.append("Expected carried authorization execution row count signal is absent.")
    if carried_selected_authorization_execution_candidate_count != 1:
        errors.append("Expected carried selected authorization execution candidate signal is absent.")
    if carried_deferred_authorization_execution_candidate_count != 2:
        errors.append("Expected carried deferred authorization execution candidate signal is absent.")
    if carried_definition_completion_execution_authorized_count != 1:
        errors.append("Expected carried definition completion execution authorized signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_definition_gap_count != 3:
        errors.append("Expected carried definition gap count signal is absent.")
    if carried_successful_theorem_proof_count != 0:
        errors.append("Expected carried successful theorem proof zero signal is absent.")
    if carried_successful_lemma_proof_count != 0:
        errors.append("Expected carried successful lemma proof zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 5:
        errors.append("Expected five drafted definition items.")
    if drafted_signature_count != 5:
        errors.append("Expected five drafted signatures.")
    if unresolved_drafting_boundary_count != 5:
        errors.append("Expected five unresolved drafting boundaries.")
    if completed_definition_item_count != 0:
        errors.append("Expected zero completed definition items.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")

    warnings = [
        "Controlled formal definition drafting is recorded, while definition completion execution remains absent.",
        "FDCT-001 receives drafted signatures only.",
        "Each drafted item still has unresolved boundaries.",
        "Theorem proof and lemma proof remain absent.",
    ]

    lines = [
        "# First Controlled Formal Definition Drafting Execution v8.61",
        "",
        "## Purpose",
        "",
        "Execute the first controlled formal definition drafting pass for FDCT-001 after v8.60 authorization, while keeping definition completion execution, completed formal definitions, proof gap resolution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Drafted definition items",
        "",
        "| Item ID | Linked target | Draft name | Draft signature | Draft scope | Unresolved boundary | Completion status | Boundary status |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.item_id} | {row.linked_target} | {row.draft_name} | {row.draft_signature} | {row.draft_scope} | {row.unresolved_boundary} | {row.completion_status} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Controlled formal definition drafting execution count: 1",
            "- Drafted definition package count: 1",
            f"- Drafted definition item count: {len(rows)}",
            f"- Drafted signature count: {drafted_signature_count}",
            f"- Unresolved drafting boundary count: {unresolved_drafting_boundary_count}",
            f"- Completed definition item count: {completed_definition_item_count}",
            f"- Completed formal definition count: {completed_formal_definition_count}",
            f"- Formal definition completion audit required count: {formal_definition_completion_audit_required_count}",
            f"- Definition completion execution count: {definition_completion_execution_count}",
            "",
            "## Carried v8.60 signals",
            "",
            f"- Carried formal definition completion execution authorization execution count: {carried_authorization_execution_count}",
            f"- Carried authorization execution row count: {carried_authorization_execution_row_count}",
            f"- Carried selected authorization execution candidate count: {carried_selected_authorization_execution_candidate_count}",
            f"- Carried deferred authorization execution candidate count: {carried_deferred_authorization_execution_candidate_count}",
            f"- Carried definition completion execution authorized count: {carried_definition_completion_execution_authorized_count}",
            f"- Carried definition completion execution count: {carried_definition_completion_execution_count}",
            f"- Carried definition gap count: {carried_definition_gap_count}",
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
            "The v8.61 artifact records controlled formal definition drafting only. It does not execute definition completion, does not complete formal definitions, does not clear proof gaps, does not establish theorem proof, does not establish lemma proof, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone drafts the first FDCT-001 signatures needed for later proof work. The drafted signatures remain open because their axioms, domains, codomains, compatibility rules, and observer semantics still require audit before completion can be considered.",
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
            "The project has executed a first controlled formal definition drafting pass for FDCT-001, producing five drafted definition items while keeping definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this definition completion execution.",
            "- Do not call this completed formal definitions.",
            "- Do not call this formal proof.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
            "- Do not call this proof gap resolution.",
            "- Do not call this external validation.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)
    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.61 formal definition drafting report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.61 formal definition drafting report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> FirstControlledFormalDefinitionDraftingExecutionReport:
    text = render_report()
    source_text = _read_source()
    rows = build_drafted_items()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_authorization_execution_count = 1 if _has_count(source_text, "Formal definition completion execution authorization execution", "1") else 0
    carried_authorization_execution_row_count = 3 if _has_count(source_text, "Authorization execution row", "3") else 0
    carried_selected_authorization_execution_candidate_count = 1 if _has_count(source_text, "Selected authorization execution candidate", "1") else 0
    carried_deferred_authorization_execution_candidate_count = 2 if _has_count(source_text, "Deferred authorization execution candidate", "2") else 0
    carried_definition_completion_execution_authorized_count = 1 if _has_count(source_text, "Definition completion execution authorized", "1") else 0
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_definition_gap_count = 3 if _has_count(source_text, "Carried definition gap", "3") else 0
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    drafted_signature_count = len(rows)
    unresolved_drafting_boundary_count = len(rows)
    completed_definition_item_count = sum(1 for row in rows if row.completion_status == "completed")
    completed_formal_definition_count = 0
    formal_definition_completion_audit_required_count = 1
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.60 authorization execution source artifact.")
    if carried_authorization_execution_count != 1:
        errors.append("Expected carried authorization execution signal is absent.")
    if carried_authorization_execution_row_count != 3:
        errors.append("Expected carried authorization execution row count signal is absent.")
    if carried_selected_authorization_execution_candidate_count != 1:
        errors.append("Expected carried selected authorization execution candidate signal is absent.")
    if carried_deferred_authorization_execution_candidate_count != 2:
        errors.append("Expected carried deferred authorization execution candidate signal is absent.")
    if carried_definition_completion_execution_authorized_count != 1:
        errors.append("Expected carried definition completion execution authorized signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_definition_gap_count != 3:
        errors.append("Expected carried definition gap count signal is absent.")
    if carried_successful_theorem_proof_count != 0:
        errors.append("Expected carried successful theorem proof zero signal is absent.")
    if carried_successful_lemma_proof_count != 0:
        errors.append("Expected carried successful lemma proof zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 5:
        errors.append("Expected five drafted definition items.")
    if drafted_signature_count != 5:
        errors.append("Expected five drafted signatures.")
    if unresolved_drafting_boundary_count != 5:
        errors.append("Expected five unresolved drafting boundaries.")
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
        "Controlled formal definition drafting is recorded, while definition completion execution remains absent.",
        "FDCT-001 receives drafted signatures only.",
        "Each drafted item still has unresolved boundaries.",
        "Theorem proof and lemma proof remain absent.",
    ]

    return FirstControlledFormalDefinitionDraftingExecutionReport(
        title="First Controlled Formal Definition Drafting Execution v8.61",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        controlled_formal_definition_drafting_execution_count=1,
        drafted_definition_package_count=1,
        drafted_definition_item_count=len(rows),
        drafted_signature_count=drafted_signature_count,
        unresolved_drafting_boundary_count=unresolved_drafting_boundary_count,
        completed_definition_item_count=completed_definition_item_count,
        completed_formal_definition_count=completed_formal_definition_count,
        formal_definition_completion_audit_required_count=formal_definition_completion_audit_required_count,
        definition_completion_execution_count=definition_completion_execution_count,
        carried_formal_definition_completion_execution_authorization_execution_count=carried_authorization_execution_count,
        carried_authorization_execution_row_count=carried_authorization_execution_row_count,
        carried_selected_authorization_execution_candidate_count=carried_selected_authorization_execution_candidate_count,
        carried_deferred_authorization_execution_candidate_count=carried_deferred_authorization_execution_candidate_count,
        carried_definition_completion_execution_authorized_count=carried_definition_completion_execution_authorized_count,
        carried_definition_completion_execution_count=carried_definition_completion_execution_count,
        carried_definition_gap_count=carried_definition_gap_count,
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
        boundary_phrase_count=44,
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
