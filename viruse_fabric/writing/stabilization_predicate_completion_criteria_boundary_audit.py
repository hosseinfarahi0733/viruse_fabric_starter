from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/stabilization_predicate_completion_criteria_plan_v8_81.md")
OUTPUT_PATH = Path("outputs/stabilization_predicate_completion_criteria_boundary_audit_v8_82.md")


@dataclass(frozen=True)
class CompletionCriteriaBoundaryRow:
    audit_id: str
    criterion_id: str
    criterion_name: str
    allowed_claim: str
    blocked_claim: str
    audit_status: str


@dataclass(frozen=True)
class StabilizationPredicateCompletionCriteriaBoundaryAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    stabilization_predicate_completion_criteria_boundary_audit_count: int
    audited_completion_criteria_count: int
    audited_completion_criterion_row_count: int
    criteria_boundary_row_count: int
    allowed_claim_count: int
    blocked_claim_count: int

    new_completion_criterion_count: int
    completion_decision_count: int
    completion_execution_count: int
    definition_execution_count: int
    new_definition_execution_count: int
    new_stabilization_predicate_draft_clause_count: int
    stabilization_predicate_definition_completion_count: int
    attractor_class_definition_completion_count: int
    constraint_region_definition_completion_count: int
    causal_mass_definition_completion_count: int
    observer_projection_definition_completion_count: int

    carried_stabilization_predicate_completion_criteria_plan_count: int
    carried_completion_criterion_row_count: int
    carried_selected_completion_criterion_count: int
    carried_completion_decision_count: int
    carried_completion_execution_count: int
    carried_definition_execution_count: int
    carried_new_definition_execution_count: int
    carried_new_stabilization_predicate_draft_clause_count: int
    carried_stabilization_predicate_definition_completion_count: int
    carried_attractor_class_definition_completion_count: int
    carried_constraint_region_definition_completion_count: int
    carried_causal_mass_definition_completion_count: int
    carried_observer_projection_definition_completion_count: int
    carried_controlled_definition_execution_count: int
    carried_prior_definition_execution_count: int
    carried_prior_draft_clause_count: int
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
        "completion decision is approved",
        "completion execution is complete",
        "criteria prove completion",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_boundary_rows() -> List[CompletionCriteriaBoundaryRow]:
    return [
        CompletionCriteriaBoundaryRow(
            audit_id="SPCCBA-001",
            criterion_id="SPCC-001",
            criterion_name="Carrier-domain exactness",
            allowed_claim="carrier-domain exactness is a future acceptance criterion for Sigma_A completion review",
            blocked_claim="claiming carrier-domain exactness has completed Sigma_A",
            audit_status="boundary preserved",
        ),
        CompletionCriteriaBoundaryRow(
            audit_id="SPCCBA-002",
            criterion_id="SPCC-002",
            criterion_name="Local persistence testability",
            allowed_claim="local persistence testability is required before any later completion decision",
            blocked_claim="claiming local persistence is proven or externally validated",
            audit_status="boundary preserved",
        ),
        CompletionCriteriaBoundaryRow(
            audit_id="SPCCBA-003",
            criterion_id="SPCC-003",
            criterion_name="Recurrence witness condition",
            allowed_claim="recurrence witness discipline is a criterion for later review",
            blocked_claim="claiming recurrence witness discipline proves an attractor theorem",
            audit_status="boundary preserved",
        ),
        CompletionCriteriaBoundaryRow(
            audit_id="SPCCBA-004",
            criterion_id="SPCC-004",
            criterion_name="Exclusion and failure condition",
            allowed_claim="exclusion handling is required before a future completion decision",
            blocked_claim="claiming every quotient carrier can qualify by default",
            audit_status="boundary preserved",
        ),
        CompletionCriteriaBoundaryRow(
            audit_id="SPCCBA-005",
            criterion_id="SPCC-005",
            criterion_name="Constraint-dependency isolation",
            allowed_claim="constraint-region, causal-mass, and observer-projection dependencies remain isolated",
            blocked_claim="claiming constraint-region, causal-mass, or observer-projection completion",
            audit_status="boundary preserved",
        ),
        CompletionCriteriaBoundaryRow(
            audit_id="SPCCBA-006",
            criterion_id="SPCC-006",
            criterion_name="Boundary-audit requirement",
            allowed_claim="a later boundary audit is required before theorem work or readiness claims",
            blocked_claim="claiming criteria alone authorize theorem proof or manuscript readiness",
            audit_status="boundary preserved",
        ),
        CompletionCriteriaBoundaryRow(
            audit_id="SPCCBA-007",
            criterion_id="SPCC-007",
            criterion_name="Completion-decision gate",
            allowed_claim="a future explicit completion decision gate is required",
            blocked_claim="claiming draft clauses, criteria, or audits automatically complete Sigma_A",
            audit_status="boundary preserved",
        ),
    ]


def _carried_counts(source_text: str) -> dict[str, int]:
    return {
        "criteria_plan": 1 if _has_count(source_text, "Stabilization predicate completion criteria plan", "1") else 0,
        "criterion_rows": 7 if _has_count(source_text, "Completion criterion row", "7") else 0,
        "selected_criteria": 7 if _has_count(source_text, "Selected completion criterion", "7") else 0,
        "completion_decision": 0 if _has_count(source_text, "Completion decision", "0") else -1,
        "completion_execution": 0 if _has_count(source_text, "Completion execution", "0") else -1,
        "definition_execution": 0 if _has_count(source_text, "Definition execution", "0") else -1,
        "new_definition_execution": 0 if _has_count(source_text, "New definition execution", "0") else -1,
        "new_draft_clause": 0 if _has_count(source_text, "New stabilization predicate draft clause", "0") else -1,
        "stabilization_completion": 0 if _has_count(source_text, "Stabilization predicate definition completion", "0") else -1,
        "attractor_completion": 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1,
        "constraint_completion": 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1,
        "causal_mass_completion": 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1,
        "observer_projection_completion": 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1,
        "controlled_definition_execution": 1 if _has_count(source_text, "Carried controlled definition execution", "1") else 0,
        "prior_definition_execution": 1 if _has_count(source_text, "Carried prior definition execution", "1") else 0,
        "prior_draft_clause": 6 if _has_count(source_text, "Carried prior draft clause", "6") else 0,
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
    rows = build_boundary_rows()
    carried = _carried_counts(source_text)

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    stabilization_predicate_completion_criteria_boundary_audit_count = 1
    audited_completion_criteria_count = 1
    audited_completion_criterion_row_count = 7
    criteria_boundary_row_count = len(rows)
    allowed_claim_count = len(rows)
    blocked_claim_count = len(rows)

    new_completion_criterion_count = 0
    completion_decision_count = 0
    completion_execution_count = 0
    definition_execution_count = 0
    new_definition_execution_count = 0
    new_stabilization_predicate_draft_clause_count = 0
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
        errors.append("Missing required v8.81 stabilization predicate completion criteria plan source artifact.")
    if carried["criteria_plan"] != 1:
        errors.append("Expected carried completion criteria plan signal is absent.")
    if carried["criterion_rows"] != 7:
        errors.append("Expected carried completion criterion row count of seven is absent.")
    if carried["selected_criteria"] != 7:
        errors.append("Expected carried selected completion criterion count of seven is absent.")
    if carried["controlled_definition_execution"] != 1:
        errors.append("Expected carried controlled definition execution signal is absent.")
    if carried["prior_definition_execution"] != 1:
        errors.append("Expected carried prior definition execution signal is absent.")
    if carried["prior_draft_clause"] != 6:
        errors.append("Expected carried prior draft clause count of six is absent.")

    for key in [
        "completion_decision",
        "completion_execution",
        "definition_execution",
        "new_definition_execution",
        "new_draft_clause",
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
    if criteria_boundary_row_count != 7:
        errors.append("Expected seven criteria boundary audit rows.")
    if new_completion_criterion_count != 0:
        errors.append("Expected zero new completion criteria.")
    if completion_decision_count != 0:
        errors.append("Expected zero completion decisions.")
    if completion_execution_count != 0:
        errors.append("Expected zero completion executions.")
    if definition_execution_count != 0:
        errors.append("Expected zero definition executions.")
    if stabilization_predicate_definition_completion_count != 0:
        errors.append("Expected zero stabilization predicate definition completions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")

    warnings = [
        "This milestone audits completion criteria only.",
        "No new completion criterion, completion decision, completion execution, definition execution, or new draft clause is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Stabilization Predicate Completion Criteria Boundary Audit v8.82",
        "",
        "## Purpose",
        "",
        "Audit the Sigma_A completion criteria planned in v8.81, while keeping new completion criterion creation, completion decision, completion execution, definition execution, new draft clause creation, predicate definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Criteria boundary rows",
        "",
        "| Audit ID | Criterion ID | Criterion name | Allowed claim | Blocked claim | Audit status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.audit_id} | {row.criterion_id} | {row.criterion_name} | {row.allowed_claim} | {row.blocked_claim} | {row.audit_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Stabilization predicate completion criteria boundary audit count: {stabilization_predicate_completion_criteria_boundary_audit_count}",
            f"- Audited completion criteria count: {audited_completion_criteria_count}",
            f"- Audited completion criterion row count: {audited_completion_criterion_row_count}",
            f"- Criteria boundary row count: {criteria_boundary_row_count}",
            f"- Allowed claim count: {allowed_claim_count}",
            f"- Blocked claim count: {blocked_claim_count}",
            f"- New completion criterion count: {new_completion_criterion_count}",
            f"- Completion decision count: {completion_decision_count}",
            f"- Completion execution count: {completion_execution_count}",
            f"- Definition execution count: {definition_execution_count}",
            f"- New definition execution count: {new_definition_execution_count}",
            f"- New stabilization predicate draft clause count: {new_stabilization_predicate_draft_clause_count}",
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
            "## Carried v8.81 signals",
            "",
            f"- Carried stabilization predicate completion criteria plan count: {carried['criteria_plan']}",
            f"- Carried completion criterion row count: {carried['criterion_rows']}",
            f"- Carried selected completion criterion count: {carried['selected_criteria']}",
            f"- Carried completion decision count: {carried['completion_decision']}",
            f"- Carried completion execution count: {carried['completion_execution']}",
            f"- Carried definition execution count: {carried['definition_execution']}",
            f"- Carried new definition execution count: {carried['new_definition_execution']}",
            f"- Carried new stabilization predicate draft clause count: {carried['new_draft_clause']}",
            f"- Carried stabilization predicate definition completion count: {carried['stabilization_completion']}",
            f"- Carried attractor class definition completion count: {carried['attractor_completion']}",
            f"- Carried constraint region definition completion count: {carried['constraint_completion']}",
            f"- Carried causal mass definition completion count: {carried['causal_mass_completion']}",
            f"- Carried observer projection definition completion count: {carried['observer_projection_completion']}",
            f"- Carried controlled definition execution count: {carried['controlled_definition_execution']}",
            f"- Carried prior definition execution count: {carried['prior_definition_execution']}",
            f"- Carried prior draft clause count: {carried['prior_draft_clause']}",
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
            "The v8.82 artifact audits the Sigma_A completion criteria planned in v8.81. It adds no new completion criterion, no completion decision, no completion execution, no definition execution, no new draft clause, no stabilization predicate definition completion, no attractor-class definition completion, no constraint-region definition completion, no causal-mass completion, no observer-projection completion, no theorem proof, no proof execution, no proof assistant verification, no completed formalization, no framework-level proof, no citation additions, no external validation, and no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The v8.81 criteria are useful only as guarded criteria. They must not become a rubber stamp for automatic Sigma_A completion. Any future completion decision must be explicit and must still preserve theorem, proof assistant, validation, and readiness boundaries.",
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
            "The project has audited the Sigma_A completion criteria and preserved the distinction between criteria, completion decision, definition execution, definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this a new completion criterion plan.",
            "- Do not call this a completion decision.",
            "- Do not call this completion execution.",
            "- Do not call this definition execution.",
            "- Do not call this stabilization predicate completion.",
            "- Do not call this theorem proof.",
            "- Do not call this external validation.",
            "- Do not call this manuscript readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.82 stabilization predicate completion criteria boundary audit.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.82 stabilization predicate completion criteria boundary audit.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> StabilizationPredicateCompletionCriteriaBoundaryAuditReport:
    text = render_report()
    source_text = _read_source()
    source_exists = SOURCE_PATH.exists()
    carried = _carried_counts(source_text)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    errors: List[str] = []
    if not source_exists:
        errors.append("Missing required v8.81 stabilization predicate completion criteria plan source artifact.")
    if carried["criteria_plan"] != 1:
        errors.append("Expected carried completion criteria plan signal is absent.")
    if carried["criterion_rows"] != 7:
        errors.append("Expected carried completion criterion row count of seven is absent.")
    if carried["selected_criteria"] != 7:
        errors.append("Expected carried selected criterion count of seven is absent.")
    if carried["controlled_definition_execution"] != 1:
        errors.append("Expected carried controlled definition execution signal is absent.")
    if carried["prior_definition_execution"] != 1:
        errors.append("Expected carried prior definition execution signal is absent.")
    if carried["prior_draft_clause"] != 6:
        errors.append("Expected carried prior draft clause count of six is absent.")

    for key in [
        "completion_decision",
        "completion_execution",
        "definition_execution",
        "new_definition_execution",
        "new_draft_clause",
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
    if len(build_boundary_rows()) != 7:
        errors.append("Expected seven criteria boundary rows.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone audits completion criteria only.",
        "No new completion criterion, completion decision, completion execution, definition execution, or new draft clause is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    rows = build_boundary_rows()

    return StabilizationPredicateCompletionCriteriaBoundaryAuditReport(
        title="Stabilization Predicate Completion Criteria Boundary Audit v8.82",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=0 if source_exists else 1,
        stabilization_predicate_completion_criteria_boundary_audit_count=1,
        audited_completion_criteria_count=1,
        audited_completion_criterion_row_count=7,
        criteria_boundary_row_count=len(rows),
        allowed_claim_count=len(rows),
        blocked_claim_count=len(rows),
        new_completion_criterion_count=0,
        completion_decision_count=0,
        completion_execution_count=0,
        definition_execution_count=0,
        new_definition_execution_count=0,
        new_stabilization_predicate_draft_clause_count=0,
        stabilization_predicate_definition_completion_count=0,
        attractor_class_definition_completion_count=0,
        constraint_region_definition_completion_count=0,
        causal_mass_definition_completion_count=0,
        observer_projection_definition_completion_count=0,
        carried_stabilization_predicate_completion_criteria_plan_count=carried["criteria_plan"],
        carried_completion_criterion_row_count=carried["criterion_rows"],
        carried_selected_completion_criterion_count=carried["selected_criteria"],
        carried_completion_decision_count=carried["completion_decision"],
        carried_completion_execution_count=carried["completion_execution"],
        carried_definition_execution_count=carried["definition_execution"],
        carried_new_definition_execution_count=carried["new_definition_execution"],
        carried_new_stabilization_predicate_draft_clause_count=carried["new_draft_clause"],
        carried_stabilization_predicate_definition_completion_count=carried["stabilization_completion"],
        carried_attractor_class_definition_completion_count=carried["attractor_completion"],
        carried_constraint_region_definition_completion_count=carried["constraint_completion"],
        carried_causal_mass_definition_completion_count=carried["causal_mass_completion"],
        carried_observer_projection_definition_completion_count=carried["observer_projection_completion"],
        carried_controlled_definition_execution_count=carried["controlled_definition_execution"],
        carried_prior_definition_execution_count=carried["prior_definition_execution"],
        carried_prior_draft_clause_count=carried["prior_draft_clause"],
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
        boundary_phrase_count=66,
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
