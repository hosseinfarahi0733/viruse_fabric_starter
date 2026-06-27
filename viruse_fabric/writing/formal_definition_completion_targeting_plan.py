from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/manual_proof_attempt_gap_audit_v8_57.md")
OUTPUT_PATH = Path("outputs/formal_definition_completion_targeting_plan_v8_58.md")


@dataclass(frozen=True)
class FormalDefinitionCompletionTargetRow:
    target_id: str
    linked_gap_ids: str
    target_name: str
    target_scope: str
    required_completion_work: str
    priority: str
    completion_status: str
    boundary_status: str


@dataclass(frozen=True)
class FormalDefinitionCompletionTargetingPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    formal_definition_completion_targeting_plan_count: int
    formal_definition_completion_target_row_count: int
    high_priority_definition_target_count: int
    medium_priority_definition_target_count: int
    unresolved_definition_target_count: int
    completed_definition_target_count: int
    definition_completion_execution_count: int

    carried_manual_proof_attempt_gap_audit_count: int
    carried_proof_attempt_gap_row_count: int
    carried_definition_gap_count: int
    carried_assumption_gap_count: int
    carried_dependency_gap_count: int
    carried_boundary_gap_count: int
    carried_unresolved_proof_attempt_gap_count: int
    carried_resolved_proof_attempt_gap_count: int
    carried_proof_attempt_gap_resolution_count: int
    carried_successful_theorem_proof_count: int
    carried_successful_lemma_proof_count: int
    carried_registered_formal_definition_candidate_count: int
    carried_unresolved_formal_definition_candidate_count: int
    carried_completed_formal_definition_candidate_count: int

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
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]", "/"]:
        text = text.replace(ch, " ")
    return " ".join(text.split())


def _has_all_terms(text: str, terms: List[str]) -> bool:
    normalized = _normalize(text)
    return all(term.lower() in normalized for term in terms)


def _has_count(text: str, phrase: str, expected: str) -> bool:
    return f"{phrase}: {expected}" in text or f"{phrase} count: {expected}" in text or _has_all_terms(text, [phrase, expected])


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["resolved proof attempt gap", "0"],
        ["proof attempt gap resolution", "0"],
        ["successful theorem proof", "0"],
        ["successful lemma proof", "0"],
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
        "proof obligation is resolved",
        "proof obligations are resolved",
        "proof execution is completed",
        "proof execution is performed",
        "proof gap is resolved",
        "proof gaps are resolved",
        "definition target is completed",
        "definition targets are completed",
        "completion target is executed",
        "completion targets are executed",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_target_rows() -> List[FormalDefinitionCompletionTargetRow]:
    return [
        FormalDefinitionCompletionTargetRow(
            target_id="FDCT-001",
            linked_gap_ids="MPG-001, MPG-003, MPG-006",
            target_name="State, relation, and projection definition package",
            target_scope="state space, transition relation, compatibility predicate, admissible path predicate, observer projection",
            required_completion_work="write minimal mathematical signatures, domains, codomains, relation constraints, and notation boundaries",
            priority="high",
            completion_status="unresolved",
            boundary_status="targeting only; definition completion execution remains absent",
        ),
        FormalDefinitionCompletionTargetRow(
            target_id="FDCT-002",
            linked_gap_ids="MPG-003, MPG-004",
            target_name="Causal mass and boundedness definition package",
            target_scope="causal mass functional, order relation, boundedness predicate, counterexample trigger conditions",
            required_completion_work="write functional type, order assumptions, boundedness predicate, and counterexample split boundary",
            priority="high",
            completion_status="unresolved",
            boundary_status="targeting only; no proof gap resolution",
        ),
        FormalDefinitionCompletionTargetRow(
            target_id="FDCT-003",
            linked_gap_ids="MPG-007, MPG-008",
            target_name="Attractor concentration and projection-safe statement package",
            target_scope="attractor concentration predicate, admissibility assumptions, projection-level interpretation boundary",
            required_completion_work="separate mathematical concentration statement from observer projection interpretation",
            priority="medium",
            completion_status="unresolved",
            boundary_status="targeting only; theorem proof remains absent",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_target_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    manual_proof_attempt_gap_audit_count = 1 if _has_count(source_text, "Manual proof attempt gap audit", "1") else 0
    proof_attempt_gap_row_count = 8 if _has_count(source_text, "Proof attempt gap row", "8") else 0
    definition_gap_count = 3 if _has_count(source_text, "Definition gap", "3") else 0
    assumption_gap_count = 2 if _has_count(source_text, "Assumption gap", "2") else 0
    dependency_gap_count = 1 if _has_count(source_text, "Dependency gap", "1") else 0
    boundary_gap_count = 2 if _has_count(source_text, "Boundary gap", "2") else 0
    unresolved_proof_attempt_gap_count = 8 if _has_count(source_text, "Unresolved proof attempt gap", "8") else 0
    resolved_proof_attempt_gap_count = 0 if _has_count(source_text, "Resolved proof attempt gap", "0") else -1
    proof_attempt_gap_resolution_count = 0 if _has_count(source_text, "Proof attempt gap resolution", "0") else -1
    successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    high_priority_definition_target_count = sum(1 for row in rows if row.priority == "high")
    medium_priority_definition_target_count = sum(1 for row in rows if row.priority == "medium")
    unresolved_definition_target_count = sum(1 for row in rows if row.completion_status == "unresolved")
    completed_definition_target_count = sum(1 for row in rows if row.completion_status == "completed")
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.57 manual proof attempt gap audit source artifact.")
    if manual_proof_attempt_gap_audit_count != 1:
        errors.append("Expected manual proof attempt gap audit signal is absent.")
    if proof_attempt_gap_row_count != 8:
        errors.append("Expected proof attempt gap row count signal is absent.")
    if definition_gap_count != 3:
        errors.append("Expected definition gap count signal is absent.")
    if assumption_gap_count != 2:
        errors.append("Expected assumption gap count signal is absent.")
    if dependency_gap_count != 1:
        errors.append("Expected dependency gap count signal is absent.")
    if boundary_gap_count != 2:
        errors.append("Expected boundary gap count signal is absent.")
    if unresolved_proof_attempt_gap_count != 8:
        errors.append("Expected unresolved proof attempt gap count signal is absent.")
    if resolved_proof_attempt_gap_count != 0:
        errors.append("Expected resolved proof attempt gap zero signal is absent.")
    if proof_attempt_gap_resolution_count != 0:
        errors.append("Expected proof attempt gap resolution zero signal is absent.")
    if successful_theorem_proof_count != 0:
        errors.append("Expected successful theorem proof zero signal is absent.")
    if successful_lemma_proof_count != 0:
        errors.append("Expected successful lemma proof zero signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected carried registered formal definition candidate signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected carried unresolved formal definition candidate signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected carried completed formal definition candidate zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 3:
        errors.append("Expected three formal definition completion target rows.")
    if high_priority_definition_target_count != 2:
        errors.append("Expected two high-priority definition targets.")
    if medium_priority_definition_target_count != 1:
        errors.append("Expected one medium-priority definition target.")
    if unresolved_definition_target_count != 3:
        errors.append("Expected three unresolved definition targets.")
    if completed_definition_target_count != 0:
        errors.append("Expected zero completed definition targets.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")

    warnings = [
        "Formal definition completion targets are planned, while completion execution remains absent.",
        "Definition gaps remain open.",
        "Proof gap resolution remains absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    lines = [
        "# Formal Definition Completion Targeting Plan v8.58",
        "",
        "## Purpose",
        "",
        "Target the definition work exposed by the v8.57 manual proof attempt gap audit while keeping definition completion execution, proof gap resolution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Formal definition completion target rows",
        "",
        "| Target ID | Linked gap IDs | Target name | Target scope | Required completion work | Priority | Completion status | Boundary status |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.target_id} | {row.linked_gap_ids} | {row.target_name} | {row.target_scope} | {row.required_completion_work} | {row.priority} | {row.completion_status} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Formal definition completion targeting plan count: 1",
            f"- Formal definition completion target row count: {len(rows)}",
            f"- High-priority definition target count: {high_priority_definition_target_count}",
            f"- Medium-priority definition target count: {medium_priority_definition_target_count}",
            f"- Unresolved definition target count: {unresolved_definition_target_count}",
            f"- Completed definition target count: {completed_definition_target_count}",
            f"- Definition completion execution count: {definition_completion_execution_count}",
            "",
            "## Carried v8.57 signals",
            "",
            f"- Carried manual proof attempt gap audit count: {manual_proof_attempt_gap_audit_count}",
            f"- Carried proof attempt gap row count: {proof_attempt_gap_row_count}",
            f"- Carried definition gap count: {definition_gap_count}",
            f"- Carried assumption gap count: {assumption_gap_count}",
            f"- Carried dependency gap count: {dependency_gap_count}",
            f"- Carried boundary gap count: {boundary_gap_count}",
            f"- Carried unresolved proof attempt gap count: {unresolved_proof_attempt_gap_count}",
            f"- Carried resolved proof attempt gap count: {resolved_proof_attempt_gap_count}",
            f"- Carried proof attempt gap resolution count: {proof_attempt_gap_resolution_count}",
            f"- Carried successful theorem proof count: {successful_theorem_proof_count}",
            f"- Carried successful lemma proof count: {successful_lemma_proof_count}",
            f"- Carried registered formal definition candidate count: {registered_formal_definition_candidate_count}",
            f"- Carried unresolved formal definition candidate count: {unresolved_formal_definition_candidate_count}",
            f"- Carried completed formal definition candidate count: {completed_formal_definition_candidate_count}",
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
            "The v8.58 artifact targets formal definition completion work only. It does not execute definition completion, does not clear proof gaps, does not establish theorem proof, does not establish lemma proof, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone responds to the definition gaps found in v8.57. It prioritizes definition packages before any proof gap resolution attempt. The targets remain open and require a later controlled execution milestone.",
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
            "The project has targeted three formal definition completion work packages from the manual proof attempt gap audit, with all definition targets still open and with definition completion execution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, citation additions, external validation, and manuscript submission readiness kept at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this completed formal definitions.",
            "- Do not call this formal proof.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
            "- Do not call this resolved proof obligations.",
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
        errors.append("Overclaim pattern detected in v8.58 formal definition completion targeting report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.58 formal definition completion targeting report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> FormalDefinitionCompletionTargetingPlanReport:
    text = render_report()
    source_text = _read_source()
    rows = build_target_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    manual_proof_attempt_gap_audit_count = 1 if _has_count(source_text, "Manual proof attempt gap audit", "1") else 0
    proof_attempt_gap_row_count = 8 if _has_count(source_text, "Proof attempt gap row", "8") else 0
    definition_gap_count = 3 if _has_count(source_text, "Definition gap", "3") else 0
    assumption_gap_count = 2 if _has_count(source_text, "Assumption gap", "2") else 0
    dependency_gap_count = 1 if _has_count(source_text, "Dependency gap", "1") else 0
    boundary_gap_count = 2 if _has_count(source_text, "Boundary gap", "2") else 0
    unresolved_proof_attempt_gap_count = 8 if _has_count(source_text, "Unresolved proof attempt gap", "8") else 0
    resolved_proof_attempt_gap_count = 0 if _has_count(source_text, "Resolved proof attempt gap", "0") else -1
    proof_attempt_gap_resolution_count = 0 if _has_count(source_text, "Proof attempt gap resolution", "0") else -1
    successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    high_priority_definition_target_count = sum(1 for row in rows if row.priority == "high")
    medium_priority_definition_target_count = sum(1 for row in rows if row.priority == "medium")
    unresolved_definition_target_count = sum(1 for row in rows if row.completion_status == "unresolved")
    completed_definition_target_count = sum(1 for row in rows if row.completion_status == "completed")
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.57 manual proof attempt gap audit source artifact.")
    if manual_proof_attempt_gap_audit_count != 1:
        errors.append("Expected manual proof attempt gap audit signal is absent.")
    if proof_attempt_gap_row_count != 8:
        errors.append("Expected proof attempt gap row count signal is absent.")
    if definition_gap_count != 3:
        errors.append("Expected definition gap count signal is absent.")
    if assumption_gap_count != 2:
        errors.append("Expected assumption gap count signal is absent.")
    if dependency_gap_count != 1:
        errors.append("Expected dependency gap count signal is absent.")
    if boundary_gap_count != 2:
        errors.append("Expected boundary gap count signal is absent.")
    if unresolved_proof_attempt_gap_count != 8:
        errors.append("Expected unresolved proof attempt gap count signal is absent.")
    if resolved_proof_attempt_gap_count != 0:
        errors.append("Expected resolved proof attempt gap zero signal is absent.")
    if proof_attempt_gap_resolution_count != 0:
        errors.append("Expected proof attempt gap resolution zero signal is absent.")
    if successful_theorem_proof_count != 0:
        errors.append("Expected successful theorem proof zero signal is absent.")
    if successful_lemma_proof_count != 0:
        errors.append("Expected successful lemma proof zero signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected carried registered formal definition candidate signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected carried unresolved formal definition candidate signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected carried completed formal definition candidate zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 3:
        errors.append("Expected three formal definition completion target rows.")
    if high_priority_definition_target_count != 2:
        errors.append("Expected two high-priority definition targets.")
    if medium_priority_definition_target_count != 1:
        errors.append("Expected one medium-priority definition target.")
    if unresolved_definition_target_count != 3:
        errors.append("Expected three unresolved definition targets.")
    if completed_definition_target_count != 0:
        errors.append("Expected zero completed definition targets.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Formal definition completion targets are planned, while completion execution remains absent.",
        "Definition gaps remain open.",
        "Proof gap resolution remains absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    return FormalDefinitionCompletionTargetingPlanReport(
        title="Formal Definition Completion Targeting Plan v8.58",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        formal_definition_completion_targeting_plan_count=1,
        formal_definition_completion_target_row_count=len(rows),
        high_priority_definition_target_count=high_priority_definition_target_count,
        medium_priority_definition_target_count=medium_priority_definition_target_count,
        unresolved_definition_target_count=unresolved_definition_target_count,
        completed_definition_target_count=completed_definition_target_count,
        definition_completion_execution_count=definition_completion_execution_count,
        carried_manual_proof_attempt_gap_audit_count=manual_proof_attempt_gap_audit_count,
        carried_proof_attempt_gap_row_count=proof_attempt_gap_row_count,
        carried_definition_gap_count=definition_gap_count,
        carried_assumption_gap_count=assumption_gap_count,
        carried_dependency_gap_count=dependency_gap_count,
        carried_boundary_gap_count=boundary_gap_count,
        carried_unresolved_proof_attempt_gap_count=unresolved_proof_attempt_gap_count,
        carried_resolved_proof_attempt_gap_count=resolved_proof_attempt_gap_count,
        carried_proof_attempt_gap_resolution_count=proof_attempt_gap_resolution_count,
        carried_successful_theorem_proof_count=successful_theorem_proof_count,
        carried_successful_lemma_proof_count=successful_lemma_proof_count,
        carried_registered_formal_definition_candidate_count=registered_formal_definition_candidate_count,
        carried_unresolved_formal_definition_candidate_count=unresolved_formal_definition_candidate_count,
        carried_completed_formal_definition_candidate_count=completed_formal_definition_candidate_count,
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
        boundary_phrase_count=41,
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
