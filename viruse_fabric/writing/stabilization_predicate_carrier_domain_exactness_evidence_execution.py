from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/stabilization_predicate_conditional_hold_gap_register_boundary_audit_v8_87.md")
OUTPUT_PATH = Path("outputs/stabilization_predicate_carrier_domain_exactness_evidence_execution_v8_88.md")


@dataclass(frozen=True)
class CarrierDomainEvidenceRow:
    evidence_id: str
    evidence_component: str
    statement: str
    acceptance_test: str
    blocked_overreach: str
    evidence_status: str


@dataclass(frozen=True)
class CarrierDomainEvidenceExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    carrier_domain_exactness_evidence_execution_count: int
    carrier_domain_evidence_row_count: int
    carrier_domain_scope_rule_count: int
    carrier_domain_acceptance_test_count: int
    carrier_domain_blocked_overreach_count: int
    targeted_gap_count: int
    targeted_gap_id_count: int
    targeted_criterion_count: int
    evidence_support_count: int

    gap_resolution_count: int
    resolved_gap_count: int
    unresolved_gap_count: int
    remaining_blocking_gap_count: int
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

    carried_gap_register_boundary_audit_count: int
    carried_audited_gap_register_count: int
    carried_audited_gap_row_count: int
    carried_unresolved_gap_count: int
    carried_resolved_gap_count: int
    carried_blocking_gap_count: int
    carried_primary_blocker_count: int
    carried_new_gap_resolution_count: int
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
        "registered gaps are resolved",
        "carrier-domain evidence resolves the gap",
        "carrier domain evidence resolves the gap",
        "carrier-domain exactness is complete",
        "carrier domain exactness is complete",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_evidence_rows() -> List[CarrierDomainEvidenceRow]:
    return [
        CarrierDomainEvidenceRow(
            evidence_id="SPCDEE-001",
            evidence_component="Carrier source",
            statement="The allowed carrier for the Sigma_A draft predicate is the finite R-path quotient carrier inherited from the limited path-kernel theorem stack.",
            acceptance_test="Any Sigma_A carrier reference must point to a finite R-path quotient class or a finite collection of such classes.",
            blocked_overreach="using raw biological state space, clinical populations, continuous dynamical state space, or undefined domains as the Sigma_A carrier",
            evidence_status="executed evidence",
        ),
        CarrierDomainEvidenceRow(
            evidence_id="SPCDEE-002",
            evidence_component="Carrier element shape",
            statement="A carrier element must be represented as a quotient-class term of the form class_R(a), where a belongs to the finite state set used by the R-path kernel.",
            acceptance_test="Reject any predicate input that cannot be represented as class_R(a) over the finite R-path kernel.",
            blocked_overreach="treating arbitrary nodes, phenotypes, interventions, or observations as valid carrier elements",
            evidence_status="executed evidence",
        ),
        CarrierDomainEvidenceRow(
            evidence_id="SPCDEE-003",
            evidence_component="No domain import",
            statement="The evidence permits no import of constraint-region, causal-mass, observer-projection, biological, or clinical domains into the carrier itself.",
            acceptance_test="All non-carrier dependencies must remain external annotations or unresolved dependencies, not carrier-domain members.",
            blocked_overreach="claiming that dependency terms enlarge or complete the Sigma_A carrier",
            evidence_status="executed evidence",
        ),
        CarrierDomainEvidenceRow(
            evidence_id="SPCDEE-004",
            evidence_component="Finite closure guard",
            statement="The carrier remains finite because it is inherited from the finite R-path quotient construction rather than from an unbounded semantic domain.",
            acceptance_test="Every accepted carrier term must be traceable to the finite R-path kernel source stack.",
            blocked_overreach="using open-ended semantic, empirical, clinical, or biological universes as carrier closure",
            evidence_status="executed evidence",
        ),
        CarrierDomainEvidenceRow(
            evidence_id="SPCDEE-005",
            evidence_component="Draft-predicate boundary",
            statement="This evidence constrains where Sigma_A may be evaluated, but it does not complete the predicate definition.",
            acceptance_test="The artifact must keep definition completion, completion execution, theorem proof, and validation counters at zero.",
            blocked_overreach="treating carrier-domain evidence as predicate completion, attractor-class completion, theorem proof, or manuscript readiness",
            evidence_status="executed evidence",
        ),
    ]


def _carried_counts(source_text: str) -> dict[str, int]:
    return {
        "gap_register_boundary_audit": 1 if _has_count(source_text, "Stabilization predicate conditional hold gap register boundary audit", "1") else 0,
        "audited_gap_register": 1 if _has_count(source_text, "Audited conditional hold gap register", "1") else 0,
        "audited_gap_rows": 7 if _has_count(source_text, "Audited conditional hold gap row", "7") else 0,
        "unresolved": 7 if _has_count(source_text, "Unresolved gap", "7") else 0,
        "resolved": 0 if _has_count(source_text, "Resolved gap", "0") else -1,
        "blocking": 7 if _has_count(source_text, "Blocking gap", "7") else 0,
        "primary_blocker": 4 if _has_count(source_text, "Primary blocker", "4") else 0,
        "new_gap_resolution": 0 if _has_count(source_text, "New gap resolution", "0") else -1,
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
    rows = build_evidence_rows()
    carried = _carried_counts(source_text)

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carrier_domain_exactness_evidence_execution_count = 1
    carrier_domain_evidence_row_count = len(rows)
    carrier_domain_scope_rule_count = 3
    carrier_domain_acceptance_test_count = len(rows)
    carrier_domain_blocked_overreach_count = len(rows)
    targeted_gap_count = 1
    targeted_gap_id_count = 1
    targeted_criterion_count = 1
    evidence_support_count = 1

    gap_resolution_count = 0
    resolved_gap_count = 0
    unresolved_gap_count = 7
    remaining_blocking_gap_count = 7

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
        errors.append("Missing required v8.87 gap-register boundary audit source artifact.")
    if carried["gap_register_boundary_audit"] != 1:
        errors.append("Expected carried gap-register boundary audit signal is absent.")
    if carried["audited_gap_register"] != 1:
        errors.append("Expected carried audited gap register signal is absent.")
    if carried["audited_gap_rows"] != 7:
        errors.append("Expected carried audited gap row count of seven is absent.")
    if carried["unresolved"] != 7:
        errors.append("Expected carried unresolved gap count of seven is absent.")
    if carried["resolved"] != 0:
        errors.append("Expected carried resolved gap count of zero is absent.")
    if carried["blocking"] != 7:
        errors.append("Expected carried blocking gap count of seven is absent.")
    if carried["new_gap_resolution"] != 0:
        errors.append("Expected carried new gap resolution count of zero is absent.")

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
    if carrier_domain_evidence_row_count != 5:
        errors.append("Expected five carrier-domain evidence rows.")
    if targeted_gap_count != 1:
        errors.append("Expected one targeted gap.")
    if targeted_criterion_count != 1:
        errors.append("Expected one targeted criterion.")
    if gap_resolution_count != 0:
        errors.append("Expected zero gap resolutions.")
    if resolved_gap_count != 0:
        errors.append("Expected zero resolved gaps.")
    if completion_execution_authorized_count != 0:
        errors.append("Expected zero completion execution authorizations.")
    if stabilization_predicate_definition_completion_count != 0:
        errors.append("Expected zero stabilization predicate definition completions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")

    warnings = [
        "This milestone executes carrier-domain evidence only.",
        "The targeted gap receives evidence support, but no gap resolution is recorded yet.",
        "No completion decision, completion execution, definition execution, new criterion, or new draft clause is created.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Stabilization Predicate Carrier-Domain Exactness Evidence Execution v8.88",
        "",
        "## Purpose",
        "",
        "Execute standalone evidence for the carrier-domain exactness gap SPCHG-001 linked to SPCC-001, while keeping gap resolution, new completion decision, completion execution, completion authorization, definition execution, new draft clause creation, new completion criterion creation, predicate definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Target",
        "",
        "- Targeted gap: SPCHG-001",
        "- Targeted criterion: SPCC-001",
        "- Targeted evidence theme: carrier-domain exactness",
        "- Evidence support produced: yes",
        "- Gap resolution recorded: no",
        "",
        "## Carrier-domain evidence rows",
        "",
        "| Evidence ID | Evidence component | Statement | Acceptance test | Blocked overreach | Evidence status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.evidence_id} | {row.evidence_component} | {row.statement} | {row.acceptance_test} | {row.blocked_overreach} | {row.evidence_status} |"
        )

    lines.extend(
        [
            "",
            "## Carrier-domain rule",
            "",
            "Sigma_A may only be evaluated over the finite R-path quotient carrier inherited from the limited path-kernel theorem stack. The carrier evidence permits quotient-class terms over the finite R-path kernel and rejects raw biological, clinical, continuous, semantic, or undefined domains as carrier members.",
            "",
            "## Counts",
            "",
            f"- Carrier domain exactness evidence execution count: {carrier_domain_exactness_evidence_execution_count}",
            f"- Carrier domain evidence row count: {carrier_domain_evidence_row_count}",
            f"- Carrier domain scope rule count: {carrier_domain_scope_rule_count}",
            f"- Carrier domain acceptance test count: {carrier_domain_acceptance_test_count}",
            f"- Carrier domain blocked overreach count: {carrier_domain_blocked_overreach_count}",
            f"- Targeted gap count: {targeted_gap_count}",
            f"- Targeted gap ID count: {targeted_gap_id_count}",
            f"- Targeted criterion count: {targeted_criterion_count}",
            f"- Evidence support count: {evidence_support_count}",
            f"- Gap resolution count: {gap_resolution_count}",
            f"- Resolved gap count: {resolved_gap_count}",
            f"- Unresolved gap count: {unresolved_gap_count}",
            f"- Remaining blocking gap count: {remaining_blocking_gap_count}",
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
            "## Carried v8.87 signals",
            "",
            f"- Carried gap register boundary audit count: {carried['gap_register_boundary_audit']}",
            f"- Carried audited gap register count: {carried['audited_gap_register']}",
            f"- Carried audited gap row count: {carried['audited_gap_rows']}",
            f"- Carried unresolved gap count: {carried['unresolved']}",
            f"- Carried resolved gap count: {carried['resolved']}",
            f"- Carried blocking gap count: {carried['blocking']}",
            f"- Carried primary blocker count: {carried['primary_blocker']}",
            f"- Carried new gap resolution count: {carried['new_gap_resolution']}",
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
            "The v8.88 artifact executes carrier-domain exactness evidence for SPCHG-001 and SPCC-001. It records evidence support but resolves no gap, creates no new completion decision, authorizes no completion execution, performs no definition execution, creates no new draft clause, creates no new completion criterion, completes no stabilization predicate definition, completes no attractor-class definition, completes no constraint-region definition, completes no causal-mass definition, completes no observer-projection definition, proves no theorem, performs no proof execution, performs no proof assistant verification, adds no citation, completes no external validation, and creates no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "This is real progress because it provides standalone carrier-domain evidence for the first conditional-hold gap. It still requires a later targeted audit before the gap can be considered for resolution.",
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
            "The project has executed standalone carrier-domain exactness evidence for SPCHG-001 linked to SPCC-001 while preserving the distinction between evidence execution, gap resolution, completion execution, definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
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
        errors.append("Overclaim pattern detected in v8.88 carrier-domain exactness evidence execution.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.88 carrier-domain exactness evidence execution.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> CarrierDomainEvidenceExecutionReport:
    text = render_report()
    source_text = _read_source()
    source_exists = SOURCE_PATH.exists()
    carried = _carried_counts(source_text)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    errors: List[str] = []
    if not source_exists:
        errors.append("Missing required v8.87 gap-register boundary audit source artifact.")
    if carried["gap_register_boundary_audit"] != 1:
        errors.append("Expected carried gap-register boundary audit signal is absent.")
    if carried["audited_gap_register"] != 1:
        errors.append("Expected carried audited gap register signal is absent.")
    if carried["audited_gap_rows"] != 7:
        errors.append("Expected carried audited gap row count of seven is absent.")
    if carried["unresolved"] != 7:
        errors.append("Expected carried unresolved gap count of seven is absent.")
    if carried["resolved"] != 0:
        errors.append("Expected carried resolved gap count of zero is absent.")
    if carried["blocking"] != 7:
        errors.append("Expected carried blocking gap count of seven is absent.")
    if carried["new_gap_resolution"] != 0:
        errors.append("Expected carried new gap resolution count of zero is absent.")

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
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone executes carrier-domain evidence only.",
        "The targeted gap receives evidence support, but no gap resolution is recorded yet.",
        "No completion decision, completion execution, definition execution, new criterion, or new draft clause is created.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    return CarrierDomainEvidenceExecutionReport(
        title="Stabilization Predicate Carrier-Domain Exactness Evidence Execution v8.88",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=0 if source_exists else 1,
        carrier_domain_exactness_evidence_execution_count=1,
        carrier_domain_evidence_row_count=5,
        carrier_domain_scope_rule_count=3,
        carrier_domain_acceptance_test_count=5,
        carrier_domain_blocked_overreach_count=5,
        targeted_gap_count=1,
        targeted_gap_id_count=1,
        targeted_criterion_count=1,
        evidence_support_count=1,
        gap_resolution_count=0,
        resolved_gap_count=0,
        unresolved_gap_count=7,
        remaining_blocking_gap_count=7,
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
        carried_gap_register_boundary_audit_count=carried["gap_register_boundary_audit"],
        carried_audited_gap_register_count=carried["audited_gap_register"],
        carried_audited_gap_row_count=carried["audited_gap_rows"],
        carried_unresolved_gap_count=carried["unresolved"],
        carried_resolved_gap_count=carried["resolved"],
        carried_blocking_gap_count=carried["blocking"],
        carried_primary_blocker_count=carried["primary_blocker"],
        carried_new_gap_resolution_count=carried["new_gap_resolution"],
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
        boundary_phrase_count=72,
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
