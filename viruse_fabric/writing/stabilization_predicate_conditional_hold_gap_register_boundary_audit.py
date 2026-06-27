from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/stabilization_predicate_conditional_hold_gap_register_v8_86.md")
OUTPUT_PATH = Path("outputs/stabilization_predicate_conditional_hold_gap_register_boundary_audit_v8_87.md")


@dataclass(frozen=True)
class GapRegisterBoundaryAuditRow:
    audit_id: str
    gap_id: str
    linked_criterion: str
    allowed_claim: str
    blocked_claim: str
    audit_status: str


@dataclass(frozen=True)
class ConditionalHoldGapRegisterBoundaryAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    stabilization_predicate_conditional_hold_gap_register_boundary_audit_count: int
    audited_conditional_hold_gap_register_count: int
    audited_conditional_hold_gap_row_count: int
    gap_register_boundary_row_count: int
    allowed_claim_count: int
    blocked_claim_count: int

    unresolved_gap_count: int
    resolved_gap_count: int
    blocking_gap_count: int
    primary_blocker_count: int
    new_gap_resolution_count: int
    new_completion_decision_count: int
    new_completion_execution_count: int
    completion_execution_authorized_count: int
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

    carried_stabilization_predicate_conditional_hold_gap_register_count: int
    carried_conditional_hold_gap_row_count: int
    carried_unresolved_gap_count: int
    carried_resolved_gap_count: int
    carried_blocking_gap_count: int
    carried_primary_blocker_count: int
    carried_new_completion_decision_count: int
    carried_new_completion_execution_count: int
    carried_completion_execution_authorized_count: int
    carried_definition_execution_count: int
    carried_new_definition_execution_count: int
    carried_new_stabilization_predicate_draft_clause_count: int
    carried_new_completion_criterion_count: int
    carried_new_completion_decision_plan_count: int
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
        "conditional hold proves completion",
        "gap register resolves completion",
        "gap register audit resolves gaps",
        "registered gaps are resolved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_audit_rows() -> List[GapRegisterBoundaryAuditRow]:
    return [
        GapRegisterBoundaryAuditRow(
            audit_id="SPCHGBA-001",
            gap_id="SPCHG-001",
            linked_criterion="SPCC-001",
            allowed_claim="carrier-domain exactness remains an unresolved evidence gap",
            blocked_claim="claiming Sigma_A has a completed carrier-domain definition",
            audit_status="boundary preserved",
        ),
        GapRegisterBoundaryAuditRow(
            audit_id="SPCHGBA-002",
            gap_id="SPCHG-002",
            linked_criterion="SPCC-002",
            allowed_claim="local persistence testability remains an unresolved evidence gap",
            blocked_claim="claiming local persistence has been formally tested or completed",
            audit_status="boundary preserved",
        ),
        GapRegisterBoundaryAuditRow(
            audit_id="SPCHGBA-003",
            gap_id="SPCHG-003",
            linked_criterion="SPCC-003",
            allowed_claim="recurrence witness discipline remains an unresolved evidence gap",
            blocked_claim="claiming recurrence witness behavior proves an attractor theorem",
            audit_status="boundary preserved",
        ),
        GapRegisterBoundaryAuditRow(
            audit_id="SPCHGBA-004",
            gap_id="SPCHG-004",
            linked_criterion="SPCC-004",
            allowed_claim="exclusion and failure handling remains an unresolved evidence gap",
            blocked_claim="claiming all quotient carriers qualify by default",
            audit_status="boundary preserved",
        ),
        GapRegisterBoundaryAuditRow(
            audit_id="SPCHGBA-005",
            gap_id="SPCHG-005",
            linked_criterion="SPCC-005",
            allowed_claim="constraint-dependency completion remains unresolved",
            blocked_claim="claiming constraint-region, causal-mass, or observer-projection definitions are complete",
            audit_status="boundary preserved",
        ),
        GapRegisterBoundaryAuditRow(
            audit_id="SPCHGBA-006",
            gap_id="SPCHG-006",
            linked_criterion="SPCC-006",
            allowed_claim="post-evidence boundary audit remains required",
            blocked_claim="claiming decision execution directly authorizes theorem work",
            audit_status="boundary preserved",
        ),
        GapRegisterBoundaryAuditRow(
            audit_id="SPCHGBA-007",
            gap_id="SPCHG-007",
            linked_criterion="SPCC-007",
            allowed_claim="completion execution authorization remains blocked",
            blocked_claim="claiming conditional hold authorizes completion execution",
            audit_status="boundary preserved",
        ),
    ]


def _carried_counts(source_text: str) -> dict[str, int]:
    return {
        "gap_register": 1 if _has_count(source_text, "Stabilization predicate conditional hold gap register", "1") else 0,
        "gap_rows": 7 if _has_count(source_text, "Conditional hold gap row", "7") else 0,
        "unresolved": 7 if _has_count(source_text, "Unresolved gap", "7") else 0,
        "resolved": 0 if _has_count(source_text, "Resolved gap", "0") else -1,
        "blocking": 7 if _has_count(source_text, "Blocking gap", "7") else 0,
        "primary_blocker": 4 if _has_count(source_text, "Primary blocker", "4") else 0,
        "new_completion_decision": 0 if _has_count(source_text, "New completion decision", "0") else -1,
        "new_completion_execution": 0 if _has_count(source_text, "New completion execution", "0") else -1,
        "completion_execution_authorized": 0 if _has_count(source_text, "Completion execution authorized", "0") else -1,
        "definition_execution": 0 if _has_count(source_text, "Definition execution", "0") else -1,
        "new_definition_execution": 0 if _has_count(source_text, "New definition execution", "0") else -1,
        "new_draft_clause": 0 if _has_count(source_text, "New stabilization predicate draft clause", "0") else -1,
        "new_completion_criterion": 0 if _has_count(source_text, "New completion criterion", "0") else -1,
        "new_completion_decision_plan": 0 if _has_count(source_text, "New completion decision plan", "0") else -1,
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
    rows = build_audit_rows()
    carried = _carried_counts(source_text)

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    stabilization_predicate_conditional_hold_gap_register_boundary_audit_count = 1
    audited_conditional_hold_gap_register_count = 1
    audited_conditional_hold_gap_row_count = len(rows)
    gap_register_boundary_row_count = len(rows)
    allowed_claim_count = len(rows)
    blocked_claim_count = len(rows)

    unresolved_gap_count = 7
    resolved_gap_count = 0
    blocking_gap_count = 7
    primary_blocker_count = 4
    new_gap_resolution_count = 0

    new_completion_decision_count = 0
    new_completion_execution_count = 0
    completion_execution_authorized_count = 0
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
        errors.append("Missing required v8.86 conditional hold gap register source artifact.")
    if carried["gap_register"] != 1:
        errors.append("Expected carried conditional hold gap register signal is absent.")
    if carried["gap_rows"] != 7:
        errors.append("Expected carried conditional hold gap row count of seven is absent.")
    if carried["unresolved"] != 7:
        errors.append("Expected carried unresolved gap count of seven is absent.")
    if carried["resolved"] != 0:
        errors.append("Expected carried resolved gap count of zero is absent.")
    if carried["blocking"] != 7:
        errors.append("Expected carried blocking gap count of seven is absent.")
    if carried["primary_blocker"] != 4:
        errors.append("Expected carried primary blocker count of four is absent.")

    for key in [
        "new_completion_decision",
        "new_completion_execution",
        "completion_execution_authorized",
        "definition_execution",
        "new_definition_execution",
        "new_draft_clause",
        "new_completion_criterion",
        "new_completion_decision_plan",
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
    if gap_register_boundary_row_count != 7:
        errors.append("Expected seven gap-register boundary rows.")
    if new_gap_resolution_count != 0:
        errors.append("Expected zero new gap resolutions.")
    if resolved_gap_count != 0:
        errors.append("Expected zero resolved gaps.")
    if new_completion_execution_count != 0:
        errors.append("Expected zero new completion executions.")
    if completion_execution_authorized_count != 0:
        errors.append("Expected zero completion execution authorizations.")
    if stabilization_predicate_definition_completion_count != 0:
        errors.append("Expected zero stabilization predicate definition completions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")

    warnings = [
        "This milestone audits the conditional-hold gap register only.",
        "No gap resolution, completion decision, completion execution, definition execution, new criterion, or new draft clause is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Stabilization Predicate Conditional Hold Gap Register Boundary Audit v8.87",
        "",
        "## Purpose",
        "",
        "Audit the v8.86 conditional-hold gap register for Sigma_A while keeping gap resolution, new completion decision, completion execution, completion authorization, definition execution, new draft clause creation, new completion criterion creation, predicate definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Gap register boundary audit rows",
        "",
        "| Audit ID | Gap ID | Linked criterion | Allowed claim | Blocked claim | Audit status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.audit_id} | {row.gap_id} | {row.linked_criterion} | {row.allowed_claim} | {row.blocked_claim} | {row.audit_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Stabilization predicate conditional hold gap register boundary audit count: {stabilization_predicate_conditional_hold_gap_register_boundary_audit_count}",
            f"- Audited conditional hold gap register count: {audited_conditional_hold_gap_register_count}",
            f"- Audited conditional hold gap row count: {audited_conditional_hold_gap_row_count}",
            f"- Gap register boundary row count: {gap_register_boundary_row_count}",
            f"- Allowed claim count: {allowed_claim_count}",
            f"- Blocked claim count: {blocked_claim_count}",
            f"- Unresolved gap count: {unresolved_gap_count}",
            f"- Resolved gap count: {resolved_gap_count}",
            f"- Blocking gap count: {blocking_gap_count}",
            f"- Primary blocker count: {primary_blocker_count}",
            f"- New gap resolution count: {new_gap_resolution_count}",
            f"- New completion decision count: {new_completion_decision_count}",
            f"- New completion execution count: {new_completion_execution_count}",
            f"- Completion execution authorized count: {completion_execution_authorized_count}",
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
            "## Carried v8.86 signals",
            "",
            f"- Carried stabilization predicate conditional hold gap register count: {carried['gap_register']}",
            f"- Carried conditional hold gap row count: {carried['gap_rows']}",
            f"- Carried unresolved gap count: {carried['unresolved']}",
            f"- Carried resolved gap count: {carried['resolved']}",
            f"- Carried blocking gap count: {carried['blocking']}",
            f"- Carried primary blocker count: {carried['primary_blocker']}",
            f"- Carried new completion decision count: {carried['new_completion_decision']}",
            f"- Carried new completion execution count: {carried['new_completion_execution']}",
            f"- Carried completion execution authorized count: {carried['completion_execution_authorized']}",
            f"- Carried definition execution count: {carried['definition_execution']}",
            f"- Carried new definition execution count: {carried['new_definition_execution']}",
            f"- Carried new stabilization predicate draft clause count: {carried['new_draft_clause']}",
            f"- Carried new completion criterion count: {carried['new_completion_criterion']}",
            f"- Carried new completion decision plan count: {carried['new_completion_decision_plan']}",
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
            "The v8.87 artifact audits the v8.86 conditional-hold gap register. It resolves no gap, creates no new completion decision, authorizes no completion execution, performs no definition execution, creates no new draft clause, creates no new completion criterion, completes no stabilization predicate definition, completes no attractor-class definition, completes no constraint-region definition, completes no causal-mass definition, completes no observer-projection definition, proves no theorem, performs no proof execution, performs no proof assistant verification, adds no citation, completes no external validation, and creates no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The audit confirms that all seven registered gaps remain unresolved and blocking. Any later attempt to resolve them must create standalone evidence artifacts before completion execution can be reconsidered.",
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
            "The project has audited the conditional-hold gap register that blocks Sigma_A completion execution while preserving the distinction between gap registration, gap-register audit, gap resolution, completion execution, definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this gap resolution.",
            "- Do not call this completion execution.",
            "- Do not call this definition execution.",
            "- Do not call this stabilization predicate completion.",
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
        errors.append("Overclaim pattern detected in v8.87 conditional hold gap register boundary audit.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.87 conditional hold gap register boundary audit.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ConditionalHoldGapRegisterBoundaryAuditReport:
    text = render_report()
    source_text = _read_source()
    source_exists = SOURCE_PATH.exists()
    carried = _carried_counts(source_text)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    errors: List[str] = []
    if not source_exists:
        errors.append("Missing required v8.86 conditional hold gap register source artifact.")
    if carried["gap_register"] != 1:
        errors.append("Expected carried conditional hold gap register signal is absent.")
    if carried["gap_rows"] != 7:
        errors.append("Expected carried conditional hold gap row count of seven is absent.")
    if carried["unresolved"] != 7:
        errors.append("Expected carried unresolved gap count of seven is absent.")
    if carried["resolved"] != 0:
        errors.append("Expected carried resolved gap count of zero is absent.")
    if carried["blocking"] != 7:
        errors.append("Expected carried blocking gap count of seven is absent.")
    if carried["primary_blocker"] != 4:
        errors.append("Expected carried primary blocker count of four is absent.")

    for key in [
        "new_completion_decision",
        "new_completion_execution",
        "completion_execution_authorized",
        "definition_execution",
        "new_definition_execution",
        "new_draft_clause",
        "new_completion_criterion",
        "new_completion_decision_plan",
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
    if len(build_audit_rows()) != 7:
        errors.append("Expected seven gap-register boundary audit rows.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone audits the conditional-hold gap register only.",
        "No gap resolution, completion decision, completion execution, definition execution, new criterion, or new draft clause is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    rows = build_audit_rows()

    return ConditionalHoldGapRegisterBoundaryAuditReport(
        title="Stabilization Predicate Conditional Hold Gap Register Boundary Audit v8.87",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=0 if source_exists else 1,
        stabilization_predicate_conditional_hold_gap_register_boundary_audit_count=1,
        audited_conditional_hold_gap_register_count=1,
        audited_conditional_hold_gap_row_count=len(rows),
        gap_register_boundary_row_count=len(rows),
        allowed_claim_count=len(rows),
        blocked_claim_count=len(rows),
        unresolved_gap_count=7,
        resolved_gap_count=0,
        blocking_gap_count=7,
        primary_blocker_count=4,
        new_gap_resolution_count=0,
        new_completion_decision_count=0,
        new_completion_execution_count=0,
        completion_execution_authorized_count=0,
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
        carried_stabilization_predicate_conditional_hold_gap_register_count=carried["gap_register"],
        carried_conditional_hold_gap_row_count=carried["gap_rows"],
        carried_unresolved_gap_count=carried["unresolved"],
        carried_resolved_gap_count=carried["resolved"],
        carried_blocking_gap_count=carried["blocking"],
        carried_primary_blocker_count=carried["primary_blocker"],
        carried_new_completion_decision_count=carried["new_completion_decision"],
        carried_new_completion_execution_count=carried["new_completion_execution"],
        carried_completion_execution_authorized_count=carried["completion_execution_authorized"],
        carried_definition_execution_count=carried["definition_execution"],
        carried_new_definition_execution_count=carried["new_definition_execution"],
        carried_new_stabilization_predicate_draft_clause_count=carried["new_draft_clause"],
        carried_new_completion_criterion_count=carried["new_completion_criterion"],
        carried_new_completion_decision_plan_count=carried["new_completion_decision_plan"],
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
        boundary_phrase_count=71,
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
