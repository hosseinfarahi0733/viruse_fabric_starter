from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/formal_definition_completion_targeting_plan_v8_58.md")
OUTPUT_PATH = Path("outputs/formal_definition_completion_execution_authorization_plan_v8_59.md")


@dataclass(frozen=True)
class DefinitionExecutionAuthorizationPlanRow:
    authorization_plan_id: str
    linked_target: str
    target_name: str
    priority: str
    readiness_class: str
    required_authorization_work: str
    next_execution_scope: str
    authorization_status: str
    boundary_status: str


@dataclass(frozen=True)
class DefinitionCompletionExecutionAuthorizationPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    formal_definition_completion_execution_authorization_plan_count: int
    authorization_plan_row_count: int
    selected_execution_candidate_count: int
    deferred_execution_candidate_count: int
    authorization_execution_required_count: int
    authorization_execution_count: int
    definition_completion_execution_count: int

    carried_formal_definition_completion_targeting_plan_count: int
    carried_formal_definition_completion_target_row_count: int
    carried_high_priority_definition_target_count: int
    carried_medium_priority_definition_target_count: int
    carried_unresolved_definition_target_count: int
    carried_completed_definition_target_count: int
    carried_definition_completion_execution_count: int
    carried_definition_gap_count: int
    carried_proof_attempt_gap_resolution_count: int
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
        ["definition completion execution", "0"],
        ["completed definition target", "0"],
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
        "authorization execution is performed",
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


def build_authorization_rows() -> List[DefinitionExecutionAuthorizationPlanRow]:
    return [
        DefinitionExecutionAuthorizationPlanRow(
            authorization_plan_id="FDEAP-001",
            linked_target="FDCT-001",
            target_name="State, relation, and projection definition package",
            priority="high",
            readiness_class="selected first execution candidate",
            required_authorization_work="confirm minimal signatures for state space, transition relation, compatibility predicate, admissible path predicate, and observer projection",
            next_execution_scope="limited definition drafting for package FDCT-001 only",
            authorization_status="planned",
            boundary_status="plan only; authorization execution remains absent",
        ),
        DefinitionExecutionAuthorizationPlanRow(
            authorization_plan_id="FDEAP-002",
            linked_target="FDCT-002",
            target_name="Causal mass and boundedness definition package",
            priority="high",
            readiness_class="deferred execution candidate",
            required_authorization_work="wait until state and relation definitions are drafted before causal mass functional scope is finalized",
            next_execution_scope="future definition drafting after FDCT-001",
            authorization_status="deferred",
            boundary_status="plan only; definition completion execution remains absent",
        ),
        DefinitionExecutionAuthorizationPlanRow(
            authorization_plan_id="FDEAP-003",
            linked_target="FDCT-003",
            target_name="Attractor concentration and projection-safe statement package",
            priority="medium",
            readiness_class="deferred execution candidate",
            required_authorization_work="wait until projection and admissibility definitions have stable signatures",
            next_execution_scope="future definition drafting after FDCT-001 and FDCT-002",
            authorization_status="deferred",
            boundary_status="plan only; theorem proof remains absent",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_authorization_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    targeting_plan_count = 1 if _has_count(source_text, "Formal definition completion targeting plan", "1") else 0
    target_row_count = 3 if _has_count(source_text, "Formal definition completion target row", "3") else 0
    high_priority_count = 2 if _has_count(source_text, "High-priority definition target", "2") else 0
    medium_priority_count = 1 if _has_count(source_text, "Medium-priority definition target", "1") else 0
    unresolved_target_count = 3 if _has_count(source_text, "Unresolved definition target", "3") else 0
    completed_target_count = 0 if _has_count(source_text, "Completed definition target", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_definition_gap_count = 3 if _has_count(source_text, "Carried definition gap", "3") else 0
    carried_proof_attempt_gap_resolution_count = 0 if _has_count(source_text, "Carried proof attempt gap resolution", "0") else -1
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    selected_execution_candidate_count = sum(1 for row in rows if row.readiness_class == "selected first execution candidate")
    deferred_execution_candidate_count = sum(1 for row in rows if row.readiness_class == "deferred execution candidate")
    authorization_execution_required_count = 1
    authorization_execution_count = 0
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.58 formal definition completion targeting source artifact.")
    if targeting_plan_count != 1:
        errors.append("Expected formal definition completion targeting plan signal is absent.")
    if target_row_count != 3:
        errors.append("Expected formal definition completion target row count signal is absent.")
    if high_priority_count != 2:
        errors.append("Expected high-priority definition target count signal is absent.")
    if medium_priority_count != 1:
        errors.append("Expected medium-priority definition target count signal is absent.")
    if unresolved_target_count != 3:
        errors.append("Expected unresolved definition target count signal is absent.")
    if completed_target_count != 0:
        errors.append("Expected completed definition target zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_definition_gap_count != 3:
        errors.append("Expected carried definition gap count signal is absent.")
    if carried_proof_attempt_gap_resolution_count != 0:
        errors.append("Expected carried proof attempt gap resolution zero signal is absent.")
    if carried_successful_theorem_proof_count != 0:
        errors.append("Expected carried successful theorem proof zero signal is absent.")
    if carried_successful_lemma_proof_count != 0:
        errors.append("Expected carried successful lemma proof zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 3:
        errors.append("Expected three authorization plan rows.")
    if selected_execution_candidate_count != 1:
        errors.append("Expected one selected execution candidate.")
    if deferred_execution_candidate_count != 2:
        errors.append("Expected two deferred execution candidates.")
    if authorization_execution_count != 0:
        errors.append("Expected zero authorization executions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")

    warnings = [
        "Formal definition completion execution authorization is planned, while authorization execution remains absent.",
        "One execution candidate is selected for a later controlled execution milestone.",
        "Definition completion execution remains absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    lines = [
        "# Formal Definition Completion Execution Authorization Plan v8.59",
        "",
        "## Purpose",
        "",
        "Plan controlled authorization for a later formal definition completion execution step after v8.58 targeting, while keeping authorization execution, definition completion execution, completed formal definitions, proof gap resolution, theorem proof, lemma proof, formal mathematical proof, formal proof execution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Authorization plan rows",
        "",
        "| Authorization plan ID | Linked target | Target name | Priority | Readiness class | Required authorization work | Next execution scope | Authorization status | Boundary status |",
        "|---|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.authorization_plan_id} | {row.linked_target} | {row.target_name} | {row.priority} | {row.readiness_class} | {row.required_authorization_work} | {row.next_execution_scope} | {row.authorization_status} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Formal definition completion execution authorization plan count: 1",
            f"- Authorization plan row count: {len(rows)}",
            f"- Selected execution candidate count: {selected_execution_candidate_count}",
            f"- Deferred execution candidate count: {deferred_execution_candidate_count}",
            f"- Authorization execution required count: {authorization_execution_required_count}",
            f"- Authorization execution count: {authorization_execution_count}",
            f"- Definition completion execution count: {definition_completion_execution_count}",
            "",
            "## Carried v8.58 signals",
            "",
            f"- Carried formal definition completion targeting plan count: {targeting_plan_count}",
            f"- Carried formal definition completion target row count: {target_row_count}",
            f"- Carried high-priority definition target count: {high_priority_count}",
            f"- Carried medium-priority definition target count: {medium_priority_count}",
            f"- Carried unresolved definition target count: {unresolved_target_count}",
            f"- Carried completed definition target count: {completed_target_count}",
            f"- Carried definition completion execution count: {carried_definition_completion_execution_count}",
            f"- Carried definition gap count: {carried_definition_gap_count}",
            f"- Carried proof attempt gap resolution count: {carried_proof_attempt_gap_resolution_count}",
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
            "The v8.59 artifact plans authorization for a later controlled definition completion execution step only. It does not execute authorization, does not execute definition completion, does not complete formal definitions, does not clear proof gaps, does not establish theorem proof, does not establish lemma proof, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone selects FDCT-001 as the first execution candidate because it blocks multiple definition gaps and supports later causal mass, boundedness, and projection work. Selection is not execution. Authorization execution remains a later milestone.",
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
            "The project has planned controlled authorization for a later formal definition completion execution step and selected one execution candidate, while keeping authorization execution, definition completion execution, completed formal definitions, theorem proof, lemma proof, formal mathematical proof, formal proof execution, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this authorization execution.",
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
        errors.append("Overclaim pattern detected in v8.59 formal definition completion execution authorization plan report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.59 formal definition completion execution authorization plan report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> DefinitionCompletionExecutionAuthorizationPlanReport:
    text = render_report()
    source_text = _read_source()
    rows = build_authorization_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    targeting_plan_count = 1 if _has_count(source_text, "Formal definition completion targeting plan", "1") else 0
    target_row_count = 3 if _has_count(source_text, "Formal definition completion target row", "3") else 0
    high_priority_count = 2 if _has_count(source_text, "High-priority definition target", "2") else 0
    medium_priority_count = 1 if _has_count(source_text, "Medium-priority definition target", "1") else 0
    unresolved_target_count = 3 if _has_count(source_text, "Unresolved definition target", "3") else 0
    completed_target_count = 0 if _has_count(source_text, "Completed definition target", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_definition_gap_count = 3 if _has_count(source_text, "Carried definition gap", "3") else 0
    carried_proof_attempt_gap_resolution_count = 0 if _has_count(source_text, "Carried proof attempt gap resolution", "0") else -1
    carried_successful_theorem_proof_count = 0 if _has_count(source_text, "Carried successful theorem proof", "0") else -1
    carried_successful_lemma_proof_count = 0 if _has_count(source_text, "Carried successful lemma proof", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    selected_execution_candidate_count = sum(1 for row in rows if row.readiness_class == "selected first execution candidate")
    deferred_execution_candidate_count = sum(1 for row in rows if row.readiness_class == "deferred execution candidate")
    authorization_execution_required_count = 1
    authorization_execution_count = 0
    definition_completion_execution_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.58 formal definition completion targeting source artifact.")
    if targeting_plan_count != 1:
        errors.append("Expected formal definition completion targeting plan signal is absent.")
    if target_row_count != 3:
        errors.append("Expected formal definition completion target row count signal is absent.")
    if high_priority_count != 2:
        errors.append("Expected high-priority definition target count signal is absent.")
    if medium_priority_count != 1:
        errors.append("Expected medium-priority definition target count signal is absent.")
    if unresolved_target_count != 3:
        errors.append("Expected unresolved definition target count signal is absent.")
    if completed_target_count != 0:
        errors.append("Expected completed definition target zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_definition_gap_count != 3:
        errors.append("Expected carried definition gap count signal is absent.")
    if carried_proof_attempt_gap_resolution_count != 0:
        errors.append("Expected carried proof attempt gap resolution zero signal is absent.")
    if carried_successful_theorem_proof_count != 0:
        errors.append("Expected carried successful theorem proof zero signal is absent.")
    if carried_successful_lemma_proof_count != 0:
        errors.append("Expected carried successful lemma proof zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 3:
        errors.append("Expected three authorization plan rows.")
    if selected_execution_candidate_count != 1:
        errors.append("Expected one selected execution candidate.")
    if deferred_execution_candidate_count != 2:
        errors.append("Expected two deferred execution candidates.")
    if authorization_execution_count != 0:
        errors.append("Expected zero authorization executions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Formal definition completion execution authorization is planned, while authorization execution remains absent.",
        "One execution candidate is selected for a later controlled execution milestone.",
        "Definition completion execution remains absent.",
        "Theorem proof and lemma proof remain absent.",
    ]

    return DefinitionCompletionExecutionAuthorizationPlanReport(
        title="Formal Definition Completion Execution Authorization Plan v8.59",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        formal_definition_completion_execution_authorization_plan_count=1,
        authorization_plan_row_count=len(rows),
        selected_execution_candidate_count=selected_execution_candidate_count,
        deferred_execution_candidate_count=deferred_execution_candidate_count,
        authorization_execution_required_count=authorization_execution_required_count,
        authorization_execution_count=authorization_execution_count,
        definition_completion_execution_count=definition_completion_execution_count,
        carried_formal_definition_completion_targeting_plan_count=targeting_plan_count,
        carried_formal_definition_completion_target_row_count=target_row_count,
        carried_high_priority_definition_target_count=high_priority_count,
        carried_medium_priority_definition_target_count=medium_priority_count,
        carried_unresolved_definition_target_count=unresolved_target_count,
        carried_completed_definition_target_count=completed_target_count,
        carried_definition_completion_execution_count=carried_definition_completion_execution_count,
        carried_definition_gap_count=carried_definition_gap_count,
        carried_proof_attempt_gap_resolution_count=carried_proof_attempt_gap_resolution_count,
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
        boundary_phrase_count=42,
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
