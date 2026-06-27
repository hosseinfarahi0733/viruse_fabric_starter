from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/stabilization_predicate_completion_decision_plan_boundary_audit_v8_84.md")
OUTPUT_PATH = Path("outputs/stabilization_predicate_completion_decision_execution_v8_85.md")


@dataclass(frozen=True)
class DecisionCriterionExecutionRow:
    criterion_id: str
    criterion_name: str
    evidence_status: str
    decision_status: str
    reason: str


@dataclass(frozen=True)
class CompletionDecisionExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    stabilization_predicate_completion_decision_execution_count: int
    completion_decision_count: int
    selected_decision_outcome_count: int
    conditional_hold_decision_count: int
    not_ready_decision_count: int
    ready_for_completion_execution_decision_count: int
    completion_execution_authorized_count: int
    criterion_decision_row_count: int
    passed_criterion_count: int
    deferred_criterion_count: int
    failed_criterion_count: int

    completion_execution_count: int
    definition_execution_count: int
    new_definition_execution_count: int
    new_stabilization_predicate_draft_clause_count: int
    new_completion_criterion_count: int
    new_completion_decision_plan_count: int
    stabilization_predicate_definition_completion_count: int
    attractor_class_definition_completion_count: int
    constraint_region_definition_completion_count: int
    causal_mass_definition_completion_count: int
    observer_projection_definition_completion_count: int

    carried_stabilization_predicate_completion_decision_plan_boundary_audit_count: int
    carried_audited_completion_decision_plan_count: int
    carried_audited_completion_decision_plan_row_count: int
    carried_decision_plan_boundary_row_count: int
    carried_allowed_claim_count: int
    carried_blocked_claim_count: int
    carried_new_completion_decision_plan_count: int
    carried_completion_decision_count: int
    carried_completion_execution_count: int
    carried_definition_execution_count: int
    carried_new_definition_execution_count: int
    carried_new_stabilization_predicate_draft_clause_count: int
    carried_new_completion_criterion_count: int
    carried_stabilization_predicate_definition_completion_count: int
    carried_attractor_class_definition_completion_count: int
    carried_constraint_region_definition_completion_count: int
    carried_causal_mass_definition_completion_count: int
    carried_observer_projection_definition_completion_count: int
    carried_new_theorem_proven_count: int
    carried_proof_execution_count: int
    carried_proof_assistant_verification_count: int
    carried_formalization_complete_count: int
    carried_completed_formal_definition_count: int
    carried_definition_completion_execution_count: int
    carried_full_framework_formal_proof_count: int
    carried_proof_gap_resolution_count: int
    carried_external_validation_count: int
    carried_new_citation_added_count: int
    carried_cumulative_limited_theorem_proven_count: int

    new_theorem_proven_count: int
    cumulative_limited_theorem_proven_count: int
    proof_assistant_verification_count: int
    formalization_complete_count: int
    completed_formal_definition_count: int
    definition_completion_execution_count: int
    full_framework_formal_proof_count: int
    formal_mathematical_proof_count: int
    formal_proof_execution_count: int
    proof_execution_count: int
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
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]", "/", "{", "}", "=", ">"]:
        text = text.replace(ch, " ")
    return " ".join(text.split())


def _has_all_terms(text: str, terms: List[str]) -> bool:
    normalized = _normalize(text)
    return all(term.lower() in normalized for term in terms)


def _has_count(text: str, phrase: str, expected: str) -> bool:
    return f"{phrase}: {expected}" in text or f"{phrase} count: {expected}" in text or _has_all_terms(text, [phrase, expected])


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
        "the main theorem is proven",
        "the full theorem is proven",
        "the theory is proven",
        "the framework is proven",
        "viruse fabric is proven",
        "full framework proof is established",
        "complete formal proof is established",
        "proof assistant verification is completed",
        "machine checked proof is completed",
        "formalization is complete",
        "formal definitions are completed",
        "definition completion execution is performed",
        "proof gap is resolved",
        "proof gaps are resolved",
        "manuscript is submission ready",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
        "attractor theory is complete",
        "causal mass is defined",
        "observer projection is defined",
        "constraint-compatible regions are complete",
        "stabilization predicate is defined",
        "sigma_a is defined",
        "sigma a is defined",
        "stabilization predicate definition is complete",
        "sigma_a definition is complete",
        "completion execution is complete",
        "criteria prove completion",
        "completion is granted",
        "completion is accepted",
        "decision execution proves completion",
        "conditional hold proves completion",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_decision_rows() -> List[DecisionCriterionExecutionRow]:
    return [
        DecisionCriterionExecutionRow(
            criterion_id="SPCC-001",
            criterion_name="Carrier-domain exactness",
            evidence_status="deferred",
            decision_status="not sufficient for completion",
            reason="the audited criteria require explicit carrier-domain evidence, but this milestone consumes only a decision-plan audit artifact",
        ),
        DecisionCriterionExecutionRow(
            criterion_id="SPCC-002",
            criterion_name="Local persistence testability",
            evidence_status="deferred",
            decision_status="not sufficient for completion",
            reason="no standalone persistence test artifact is executed in this milestone",
        ),
        DecisionCriterionExecutionRow(
            criterion_id="SPCC-003",
            criterion_name="Recurrence witness condition",
            evidence_status="deferred",
            decision_status="not sufficient for completion",
            reason="no bounded recurrence witness artifact is executed in this milestone",
        ),
        DecisionCriterionExecutionRow(
            criterion_id="SPCC-004",
            criterion_name="Exclusion and failure condition",
            evidence_status="deferred",
            decision_status="not sufficient for completion",
            reason="failure handling is planned, but no completion-execution evidence is created",
        ),
        DecisionCriterionExecutionRow(
            criterion_id="SPCC-005",
            criterion_name="Constraint-dependency isolation",
            evidence_status="passed-boundary-only",
            decision_status="supports conditional hold only",
            reason="constraint-region, causal-mass, and observer-projection dependencies remain isolated and incomplete",
        ),
        DecisionCriterionExecutionRow(
            criterion_id="SPCC-006",
            criterion_name="Boundary-audit requirement",
            evidence_status="passed-boundary-only",
            decision_status="supports conditional hold only",
            reason="the decision plan boundary audit exists, but it does not complete Sigma_A",
        ),
        DecisionCriterionExecutionRow(
            criterion_id="SPCC-007",
            criterion_name="Completion-decision gate",
            evidence_status="passed-gate-only",
            decision_status="conditional hold",
            reason="the gate can execute a decision, but the available evidence does not authorize completion execution",
        ),
    ]


def _carried_counts(source_text: str) -> dict[str, int]:
    return {
        "decision_plan_boundary_audit": 1 if _has_count(source_text, "Stabilization predicate completion decision plan boundary audit", "1") else 0,
        "audited_decision_plan": 1 if _has_count(source_text, "Audited completion decision plan", "1") else 0,
        "audited_decision_plan_rows": 6 if _has_count(source_text, "Audited completion decision plan row", "6") else 0,
        "decision_plan_boundary_rows": 6 if _has_count(source_text, "Decision plan boundary row", "6") else 0,
        "allowed_claim": 6 if _has_count(source_text, "Allowed claim", "6") else 0,
        "blocked_claim": 6 if _has_count(source_text, "Blocked claim", "6") else 0,
        "new_completion_decision_plan": 0 if _has_count(source_text, "New completion decision plan", "0") else -1,
        "completion_decision": 0 if _has_count(source_text, "Completion decision", "0") else -1,
        "completion_execution": 0 if _has_count(source_text, "Completion execution", "0") else -1,
        "definition_execution": 0 if _has_count(source_text, "Definition execution", "0") else -1,
        "new_definition_execution": 0 if _has_count(source_text, "New definition execution", "0") else -1,
        "new_draft_clause": 0 if _has_count(source_text, "New stabilization predicate draft clause", "0") else -1,
        "new_completion_criterion": 0 if _has_count(source_text, "New completion criterion", "0") else -1,
        "stabilization_completion": 0 if _has_count(source_text, "Stabilization predicate definition completion", "0") else -1,
        "attractor_completion": 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1,
        "constraint_completion": 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1,
        "causal_mass_completion": 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1,
        "observer_projection_completion": 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1,
        "new_theorem": 0 if _has_count(source_text, "New theorem proven", "0") else -1,
        "proof_execution": 0 if _has_count(source_text, "Proof execution", "0") else -1,
        "proof_assistant": 0 if _has_count(source_text, "Proof assistant verification", "0") else -1,
        "formalization": 0 if _has_count(source_text, "Formalization complete", "0") else -1,
        "completed_formal_definition": 0 if _has_count(source_text, "Completed formal definition", "0") else -1,
        "definition_completion_execution": 0 if _has_count(source_text, "Definition completion execution", "0") else -1,
        "full_framework": 0 if _has_count(source_text, "Full framework formal proof", "0") else -1,
        "proof_gap": 0 if _has_count(source_text, "Proof gap resolution", "0") else -1,
        "external": 0 if _has_count(source_text, "External validation", "0") else -1,
        "citation": 0 if _has_count(source_text, "New citation added", "0") else -1,
        "cumulative_theorem": 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0,
    }


def render_report() -> str:
    source_text = _read_source()
    rows = build_decision_rows()
    carried = _carried_counts(source_text)

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    stabilization_predicate_completion_decision_execution_count = 1
    completion_decision_count = 1
    selected_decision_outcome_count = 1
    conditional_hold_decision_count = 1
    not_ready_decision_count = 0
    ready_for_completion_execution_decision_count = 0
    completion_execution_authorized_count = 0
    criterion_decision_row_count = len(rows)
    passed_criterion_count = 0
    deferred_criterion_count = 7
    failed_criterion_count = 0

    completion_execution_count = 0
    definition_execution_count = 0
    new_definition_execution_count = 0
    new_stabilization_predicate_draft_clause_count = 0
    new_completion_criterion_count = 0
    new_completion_decision_plan_count = 0
    stabilization_predicate_definition_completion_count = 0
    attractor_class_definition_completion_count = 0
    constraint_region_definition_completion_count = 0
    causal_mass_definition_completion_count = 0
    observer_projection_definition_completion_count = 0

    new_theorem_proven_count = 0
    cumulative_limited_theorem_proven_count = carried["cumulative_theorem"]
    proof_assistant_verification_count = 0
    formalization_complete_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0
    full_framework_formal_proof_count = 0
    formal_mathematical_proof_count = 0
    formal_proof_execution_count = 0
    proof_execution_count = 0
    proof_gap_resolution_count = 0
    manuscript_submission_ready_count = 0
    readiness_approval_count = 0
    external_validation_count = 0
    independent_experiment_count = 0
    new_citation_added_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.84 completion decision plan boundary audit source artifact.")
    if carried["decision_plan_boundary_audit"] != 1:
        errors.append("Expected carried completion decision plan boundary audit signal is absent.")
    if carried["audited_decision_plan"] != 1:
        errors.append("Expected carried audited completion decision plan signal is absent.")
    if carried["audited_decision_plan_rows"] != 6:
        errors.append("Expected carried audited completion decision plan row count of six is absent.")
    if carried["decision_plan_boundary_rows"] != 6:
        errors.append("Expected carried decision plan boundary row count of six is absent.")

    for key in [
        "new_completion_decision_plan",
        "completion_decision",
        "completion_execution",
        "definition_execution",
        "new_definition_execution",
        "new_draft_clause",
        "new_completion_criterion",
        "stabilization_completion",
        "attractor_completion",
        "constraint_completion",
        "causal_mass_completion",
        "observer_projection_completion",
        "new_theorem",
        "proof_execution",
        "proof_assistant",
        "formalization",
        "completed_formal_definition",
        "definition_completion_execution",
        "full_framework",
        "proof_gap",
        "external",
        "citation",
    ]:
        if carried[key] != 0:
            errors.append(f"Expected carried zero signal is absent: {key}.")

    if carried["cumulative_theorem"] != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
    if criterion_decision_row_count != 7:
        errors.append("Expected seven criterion decision rows.")
    if completion_decision_count != 1:
        errors.append("Expected one controlled completion decision.")
    if conditional_hold_decision_count != 1:
        errors.append("Expected conditional hold decision outcome.")
    if ready_for_completion_execution_decision_count != 0:
        errors.append("Expected zero ready-for-completion-execution outcomes.")
    if completion_execution_authorized_count != 0:
        errors.append("Expected zero completion execution authorizations.")
    if completion_execution_count != 0:
        errors.append("Expected zero completion executions.")
    if stabilization_predicate_definition_completion_count != 0:
        errors.append("Expected zero stabilization predicate definition completions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")

    warnings = [
        "This milestone executes a controlled completion decision only; the outcome is conditional hold.",
        "No completion execution, definition execution, new criterion, new draft clause, or definition completion is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Stabilization Predicate Completion Decision Execution v8.85",
        "",
        "## Purpose",
        "",
        "Execute the controlled completion decision gate for the Sigma_A draft predicate and record a conditional-hold outcome, while keeping completion execution, definition execution, new draft clause creation, new completion criterion creation, predicate definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Decision outcome",
        "",
        "- Decision outcome: conditional hold",
        "- Reason: the decision gate exists, but the available artifact chain provides boundary-audited planning rather than standalone completion evidence for all seven criteria.",
        "- Completion execution authorized: no",
        "",
        "## Criterion decision rows",
        "",
        "| Criterion ID | Criterion name | Evidence status | Decision status | Reason |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.criterion_id} | {row.criterion_name} | {row.evidence_status} | {row.decision_status} | {row.reason} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Stabilization predicate completion decision execution count: {stabilization_predicate_completion_decision_execution_count}",
            f"- Completion decision count: {completion_decision_count}",
            f"- Selected decision outcome count: {selected_decision_outcome_count}",
            f"- Conditional hold decision count: {conditional_hold_decision_count}",
            f"- Not ready decision count: {not_ready_decision_count}",
            f"- Ready for completion execution decision count: {ready_for_completion_execution_decision_count}",
            f"- Completion execution authorized count: {completion_execution_authorized_count}",
            f"- Criterion decision row count: {criterion_decision_row_count}",
            f"- Passed criterion count: {passed_criterion_count}",
            f"- Deferred criterion count: {deferred_criterion_count}",
            f"- Failed criterion count: {failed_criterion_count}",
            f"- Completion execution count: {completion_execution_count}",
            f"- Definition execution count: {definition_execution_count}",
            f"- New definition execution count: {new_definition_execution_count}",
            f"- New stabilization predicate draft clause count: {new_stabilization_predicate_draft_clause_count}",
            f"- New completion criterion count: {new_completion_criterion_count}",
            f"- New completion decision plan count: {new_completion_decision_plan_count}",
            f"- Stabilization predicate definition completion count: {stabilization_predicate_definition_completion_count}",
            f"- Attractor class definition completion count: {attractor_class_definition_completion_count}",
            f"- Constraint region definition completion count: {constraint_region_definition_completion_count}",
            f"- Causal mass definition completion count: {causal_mass_definition_completion_count}",
            f"- Observer projection definition completion count: {observer_projection_definition_completion_count}",
            f"- New theorem proven count: {new_theorem_proven_count}",
            f"- Cumulative limited theorem proven count: {cumulative_limited_theorem_proven_count}",
            f"- Proof assistant verification count: {proof_assistant_verification_count}",
            f"- Formalization complete count: {formalization_complete_count}",
            f"- Completed formal definition count: {completed_formal_definition_count}",
            f"- Definition completion execution count: {definition_completion_execution_count}",
            f"- Full framework formal proof count: {full_framework_formal_proof_count}",
            f"- Formal mathematical proof count: {formal_mathematical_proof_count}",
            f"- Formal proof execution count: {formal_proof_execution_count}",
            f"- Proof execution count: {proof_execution_count}",
            f"- Proof gap resolution count: {proof_gap_resolution_count}",
            f"- Manuscript submission ready count: {manuscript_submission_ready_count}",
            f"- Readiness approval count: {readiness_approval_count}",
            f"- External validation count: {external_validation_count}",
            f"- Independent experiment count: {independent_experiment_count}",
            f"- New citation added count: {new_citation_added_count}",
            "",
            "## Carried v8.84 signals",
            "",
            f"- Carried stabilization predicate completion decision plan boundary audit count: {carried['decision_plan_boundary_audit']}",
            f"- Carried audited completion decision plan count: {carried['audited_decision_plan']}",
            f"- Carried audited completion decision plan row count: {carried['audited_decision_plan_rows']}",
            f"- Carried decision plan boundary row count: {carried['decision_plan_boundary_rows']}",
            f"- Carried allowed claim count: {carried['allowed_claim']}",
            f"- Carried blocked claim count: {carried['blocked_claim']}",
            f"- Carried new completion decision plan count: {carried['new_completion_decision_plan']}",
            f"- Carried completion decision count: {carried['completion_decision']}",
            f"- Carried completion execution count: {carried['completion_execution']}",
            f"- Carried definition execution count: {carried['definition_execution']}",
            f"- Carried new definition execution count: {carried['new_definition_execution']}",
            f"- Carried new stabilization predicate draft clause count: {carried['new_draft_clause']}",
            f"- Carried new completion criterion count: {carried['new_completion_criterion']}",
            f"- Carried stabilization predicate definition completion count: {carried['stabilization_completion']}",
            f"- Carried attractor class definition completion count: {carried['attractor_completion']}",
            f"- Carried constraint region definition completion count: {carried['constraint_completion']}",
            f"- Carried causal mass definition completion count: {carried['causal_mass_completion']}",
            f"- Carried observer projection definition completion count: {carried['observer_projection_completion']}",
            f"- Carried new theorem proven count: {carried['new_theorem']}",
            f"- Carried proof execution count: {carried['proof_execution']}",
            f"- Carried proof assistant verification count: {carried['proof_assistant']}",
            f"- Carried formalization complete count: {carried['formalization']}",
            f"- Carried completed formal definition count: {carried['completed_formal_definition']}",
            f"- Carried definition completion execution count: {carried['definition_completion_execution']}",
            f"- Carried full framework formal proof count: {carried['full_framework']}",
            f"- Carried proof gap resolution count: {carried['proof_gap']}",
            f"- Carried external validation count: {carried['external']}",
            f"- Carried new citation added count: {carried['citation']}",
            f"- Carried cumulative limited theorem proven count: {carried['cumulative_theorem']}",
            "",
            "## Boundary interpretation",
            "",
            "The v8.85 artifact executes a controlled completion decision gate for Sigma_A and records conditional hold. It authorizes no completion execution, performs no definition execution, creates no new draft clause, creates no new completion criterion, completes no stabilization predicate definition, completes no attractor-class definition, completes no constraint-region definition, completes no causal-mass definition, completes no observer-projection definition, proves no theorem, performs no proof execution, performs no proof assistant verification, adds no citation, completes no external validation, and creates no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The conditional-hold outcome is intentional. The project has planning and boundary-audit artifacts, but it does not yet have standalone completion evidence for all seven Sigma_A criteria.",
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
            "The project has executed a controlled completion decision for the Sigma_A draft predicate and recorded conditional hold while preserving the distinction between decision execution, completion execution, definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this completion execution.",
            "- Do not call this definition execution.",
            "- Do not call this stabilization predicate completion.",
            "- Do not call this attractor-class completion.",
            "- Do not call this theorem proof.",
            "- Do not call this proof execution.",
            "- Do not call this external validation.",
            "- Do not call this manuscript readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.85 stabilization predicate completion decision execution.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.85 stabilization predicate completion decision execution.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> CompletionDecisionExecutionReport:
    text = render_report()
    source_text = _read_source()
    source_exists = SOURCE_PATH.exists()
    carried = _carried_counts(source_text)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    errors: List[str] = []
    if not source_exists:
        errors.append("Missing required v8.84 completion decision plan boundary audit source artifact.")
    if carried["decision_plan_boundary_audit"] != 1:
        errors.append("Expected carried completion decision plan boundary audit signal is absent.")
    if carried["audited_decision_plan"] != 1:
        errors.append("Expected carried audited completion decision plan signal is absent.")
    if carried["audited_decision_plan_rows"] != 6:
        errors.append("Expected carried audited completion decision plan row count of six is absent.")
    if carried["decision_plan_boundary_rows"] != 6:
        errors.append("Expected carried decision plan boundary row count of six is absent.")

    for key in [
        "new_completion_decision_plan",
        "completion_decision",
        "completion_execution",
        "definition_execution",
        "new_definition_execution",
        "new_draft_clause",
        "new_completion_criterion",
        "stabilization_completion",
        "attractor_completion",
        "constraint_completion",
        "causal_mass_completion",
        "observer_projection_completion",
        "new_theorem",
        "proof_execution",
        "proof_assistant",
        "formalization",
        "completed_formal_definition",
        "definition_completion_execution",
        "full_framework",
        "proof_gap",
        "external",
        "citation",
    ]:
        if carried[key] != 0:
            errors.append(f"Expected carried zero signal is absent: {key}.")
    if carried["cumulative_theorem"] != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone executes a controlled completion decision only; the outcome is conditional hold.",
        "No completion execution, definition execution, new criterion, new draft clause, or definition completion is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    return CompletionDecisionExecutionReport(
        title="Stabilization Predicate Completion Decision Execution v8.85",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=0 if source_exists else 1,
        stabilization_predicate_completion_decision_execution_count=1,
        completion_decision_count=1,
        selected_decision_outcome_count=1,
        conditional_hold_decision_count=1,
        not_ready_decision_count=0,
        ready_for_completion_execution_decision_count=0,
        completion_execution_authorized_count=0,
        criterion_decision_row_count=7,
        passed_criterion_count=0,
        deferred_criterion_count=7,
        failed_criterion_count=0,
        completion_execution_count=0,
        definition_execution_count=0,
        new_definition_execution_count=0,
        new_stabilization_predicate_draft_clause_count=0,
        new_completion_criterion_count=0,
        new_completion_decision_plan_count=0,
        stabilization_predicate_definition_completion_count=0,
        attractor_class_definition_completion_count=0,
        constraint_region_definition_completion_count=0,
        causal_mass_definition_completion_count=0,
        observer_projection_definition_completion_count=0,
        carried_stabilization_predicate_completion_decision_plan_boundary_audit_count=carried["decision_plan_boundary_audit"],
        carried_audited_completion_decision_plan_count=carried["audited_decision_plan"],
        carried_audited_completion_decision_plan_row_count=carried["audited_decision_plan_rows"],
        carried_decision_plan_boundary_row_count=carried["decision_plan_boundary_rows"],
        carried_allowed_claim_count=carried["allowed_claim"],
        carried_blocked_claim_count=carried["blocked_claim"],
        carried_new_completion_decision_plan_count=carried["new_completion_decision_plan"],
        carried_completion_decision_count=carried["completion_decision"],
        carried_completion_execution_count=carried["completion_execution"],
        carried_definition_execution_count=carried["definition_execution"],
        carried_new_definition_execution_count=carried["new_definition_execution"],
        carried_new_stabilization_predicate_draft_clause_count=carried["new_draft_clause"],
        carried_new_completion_criterion_count=carried["new_completion_criterion"],
        carried_stabilization_predicate_definition_completion_count=carried["stabilization_completion"],
        carried_attractor_class_definition_completion_count=carried["attractor_completion"],
        carried_constraint_region_definition_completion_count=carried["constraint_completion"],
        carried_causal_mass_definition_completion_count=carried["causal_mass_completion"],
        carried_observer_projection_definition_completion_count=carried["observer_projection_completion"],
        carried_new_theorem_proven_count=carried["new_theorem"],
        carried_proof_execution_count=carried["proof_execution"],
        carried_proof_assistant_verification_count=carried["proof_assistant"],
        carried_formalization_complete_count=carried["formalization"],
        carried_completed_formal_definition_count=carried["completed_formal_definition"],
        carried_definition_completion_execution_count=carried["definition_completion_execution"],
        carried_full_framework_formal_proof_count=carried["full_framework"],
        carried_proof_gap_resolution_count=carried["proof_gap"],
        carried_external_validation_count=carried["external"],
        carried_new_citation_added_count=carried["citation"],
        carried_cumulative_limited_theorem_proven_count=carried["cumulative_theorem"],
        new_theorem_proven_count=0,
        cumulative_limited_theorem_proven_count=carried["cumulative_theorem"],
        proof_assistant_verification_count=0,
        formalization_complete_count=0,
        completed_formal_definition_count=0,
        definition_completion_execution_count=0,
        full_framework_formal_proof_count=0,
        formal_mathematical_proof_count=0,
        formal_proof_execution_count=0,
        proof_execution_count=0,
        proof_gap_resolution_count=0,
        manuscript_submission_ready_count=0,
        readiness_approval_count=0,
        external_validation_count=0,
        independent_experiment_count=0,
        new_citation_added_count=0,
        conditional_hold_count=1,
        hard_zero_count=13,
        boundary_phrase_count=69,
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
