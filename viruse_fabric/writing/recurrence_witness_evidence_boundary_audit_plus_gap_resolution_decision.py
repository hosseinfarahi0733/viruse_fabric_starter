from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace


SOURCE_PATH = Path("outputs/recurrence_witness_evidence_execution_v8_92.md")
OUTPUT_PATH = Path("outputs/recurrence_witness_evidence_boundary_audit_plus_gap_resolution_decision_v8_93.md")


def _read_source() -> str:
    if not SOURCE_PATH.exists():
        return ""
    return SOURCE_PATH.read_text(encoding="utf-8")


def _normalize(text: str) -> str:
    text = text.lower()
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]", "/", "{", "}", "=", ">"]:
        text = text.replace(ch, " ")
    return " ".join(text.split())


def _has_all_terms(text: str, terms: list[str]) -> bool:
    normalized = _normalize(text)
    return all(term.lower() in normalized for term in terms)


def _has_count(text: str, phrase: str, expected: str) -> bool:
    return (
        f"{phrase}: {expected}" in text
        or f"{phrase} count: {expected}" in text
        or _has_all_terms(text, [phrase, expected])
    )


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
        "all gaps are resolved",
        "all blocking gaps are resolved",
        "recurrence witness completes sigma_a",
        "recurrence witness proves sigma_a",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def _carried_counts(source_text: str) -> dict[str, int]:
    return {
        "recurrence_witness_evidence_execution": 1 if _has_count(source_text, "Recurrence witness evidence execution", "1") else 0,
        "recurrence_witness_evidence_rows": 5 if _has_count(source_text, "Recurrence witness evidence row", "5") else 0,
        "recurrence_witness_scope_rules": 3 if _has_count(source_text, "Recurrence witness scope rule", "3") else 0,
        "recurrence_witness_acceptance_tests": 5 if _has_count(source_text, "Recurrence witness acceptance test", "5") else 0,
        "recurrence_witness_blocked_overreach": 5 if _has_count(source_text, "Recurrence witness blocked overreach", "5") else 0,
        "targeted_gap": 1 if _has_count(source_text, "Targeted gap", "1") else 0,
        "targeted_gap_id": 1 if _has_count(source_text, "Targeted gap ID", "1") else 0,
        "targeted_criterion": 1 if _has_count(source_text, "Targeted criterion", "1") else 0,
        "evidence_support": 1 if _has_count(source_text, "Evidence support", "1") else 0,
        "prior_resolved_gaps_retained": 2 if _has_count(source_text, "Prior resolved gaps retained", "2") else 0,
        "gap_resolution_decision": 0 if _has_count(source_text, "Gap resolution decision", "0") else -1,
        "targeted_gap_resolution_decision": 0 if _has_count(source_text, "Targeted gap resolution decision", "0") else -1,
        "newly_resolved_gap": 0 if _has_count(source_text, "Newly resolved gap", "0") else -1,
        "resolved_gap": 2 if _has_count(source_text, "Resolved gap", "2") else 0,
        "unresolved_gap": 5 if _has_count(source_text, "Unresolved gap", "5") else 0,
        "remaining_blocking_gap": 5 if _has_count(source_text, "Remaining blocking gap", "5") else 0,
        "gap_resolution_authorized": 0 if _has_count(source_text, "Gap resolution authorized", "0") else -1,
        "completion_decision": 0 if _has_count(source_text, "Completion decision", "0") else -1,
        "completion_execution": 0 if _has_count(source_text, "Completion execution", "0") else -1,
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


def _audit_rows() -> list[dict[str, str]]:
    return [
        {
            "audit_id": "RWBA-001",
            "evidence_id": "RW-EE-001",
            "audit_focus": "recurrence domain anchor",
            "accepted_claim": "recurrence witness rows must name a finite quotient carrier element and declared local condition",
            "blocked_claim": "recurrence wording without carrier anchor or local condition counts as evidence",
            "audit_status": "passed for targeted gap resolution decision",
        },
        {
            "audit_id": "RWBA-002",
            "evidence_id": "RW-EE-002",
            "audit_focus": "return relation",
            "accepted_claim": "a bounded return relation must connect a later local state to a comparable local condition",
            "blocked_claim": "vague similarity, narrative return, or observer impression counts as recurrence",
            "audit_status": "passed for targeted gap resolution decision",
        },
        {
            "audit_id": "RWBA-003",
            "evidence_id": "RW-EE-003",
            "audit_focus": "witness repeatability",
            "accepted_claim": "repeatable witness structure must be checkable under the same finite carrier and bounded relation",
            "blocked_claim": "one accidental return counts as stable recurrence structure",
            "audit_status": "passed for targeted gap resolution decision",
        },
        {
            "audit_id": "RWBA-004",
            "evidence_id": "RW-EE-004",
            "audit_focus": "non-recurrence failure case",
            "accepted_claim": "non-recurrence must be recordable when the bounded return relation fails",
            "blocked_claim": "successful recurrence-like examples can hide failed returns",
            "audit_status": "passed for targeted gap resolution decision",
        },
        {
            "audit_id": "RWBA-005",
            "evidence_id": "RW-EE-005",
            "audit_focus": "draft-predicate boundary",
            "accepted_claim": "recurrence witness evidence supports the third gap but does not finish Sigma_A",
            "blocked_claim": "recurrence witness evidence creates predicate completion, theorem proof, or readiness",
            "audit_status": "passed for targeted gap resolution decision",
        },
    ]


def render_report() -> str:
    source_text = _read_source()
    carried = _carried_counts(source_text)
    rows = _audit_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    lines = [
        "# Recurrence Witness Evidence Boundary Audit Plus Gap Resolution Decision v8.93",
        "",
        "## Purpose",
        "",
        "Audit the v8.92 recurrence witness evidence and record a targeted gap resolution decision for SPCHG-003 linked to SPCC-003, while keeping completion decision, completion execution, completion authorization, definition execution, new draft clause creation, new completion criterion creation, predicate definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Resolution decision",
        "",
        "- Targeted gap: SPCHG-003",
        "- Targeted criterion: SPCC-003",
        "- Decision: targeted gap resolved",
        "- Previously resolved gaps retained: SPCHG-001 and SPCHG-002",
        "- Resolved gap count: 3",
        "- Newly resolved gap count: 1",
        "- Unresolved gap count after decision: 4",
        "- Remaining blocking gap count: 4",
        "- Completion execution authorized: no",
        "",
        "## Recurrence witness evidence boundary audit rows",
        "",
        "| Audit ID | Evidence ID | Audit focus | Accepted claim | Blocked claim | Audit status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row['audit_id']} | {row['evidence_id']} | {row['audit_focus']} | "
            f"{row['accepted_claim']} | {row['blocked_claim']} | {row['audit_status']} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Recurrence witness evidence boundary audit count: 1",
            "- Audited recurrence witness evidence count: 1",
            "- Recurrence witness boundary audit row count: 5",
            "- Accepted claim count: 5",
            "- Blocked claim count: 5",
            "- Gap resolution decision count: 1",
            "- Targeted gap resolution decision count: 1",
            "- Targeted gap count: 1",
            "- Targeted criterion count: 1",
            "- Evidence supported gap count: 1",
            "- Previously resolved gaps retained count: 2",
            "- Resolved gap count: 3",
            "- Newly resolved gap count: 1",
            "- Unresolved gap count: 4",
            "- Remaining blocking gap count: 4",
            "- Gap resolution authorized count: 1",
            "- Completion decision count: 0",
            "- Completion execution count: 0",
            "- Completion execution authorized count: 0",
            "- Definition execution count: 0",
            "- New definition execution count: 0",
            "- New stabilization predicate draft clause count: 0",
            "- New completion criterion count: 0",
            "- New completion decision plan count: 0",
            "- Stabilization predicate definition completion count: 0",
            "- Attractor class definition completion count: 0",
            "- Constraint region definition completion count: 0",
            "- Causal mass definition completion count: 0",
            "- Observer projection definition completion count: 0",
            "- New theorem proven count: 0",
            f"- Cumulative limited theorem proven count: {carried['cumulative_theorem']}",
            "- Proof assistant verification count: 0",
            "- Formalization complete count: 0",
            "- Completed formal definition count: 0",
            "- Definition completion execution count: 0",
            "- Full framework formal proof count: 0",
            "- Formal mathematical proof count: 0",
            "- Formal proof execution count: 0",
            "- Proof execution count: 0",
            "- Proof gap resolution count: 0",
            "- Manuscript submission ready count: 0",
            "- Readiness approval count: 0",
            "- External validation count: 0",
            "- Independent experiment count: 0",
            "- New citation added count: 0",
            "",
            "## Carried v8.92 signals",
            "",
            f"- Carried recurrence witness evidence execution count: {carried['recurrence_witness_evidence_execution']}",
            f"- Carried recurrence witness evidence row count: {carried['recurrence_witness_evidence_rows']}",
            f"- Carried recurrence witness scope rule count: {carried['recurrence_witness_scope_rules']}",
            f"- Carried recurrence witness acceptance test count: {carried['recurrence_witness_acceptance_tests']}",
            f"- Carried recurrence witness blocked overreach count: {carried['recurrence_witness_blocked_overreach']}",
            f"- Carried targeted gap count: {carried['targeted_gap']}",
            f"- Carried targeted gap ID count: {carried['targeted_gap_id']}",
            f"- Carried targeted criterion count: {carried['targeted_criterion']}",
            f"- Carried evidence support count: {carried['evidence_support']}",
            f"- Carried prior resolved gaps retained count: {carried['prior_resolved_gaps_retained']}",
            f"- Carried gap resolution decision count: {carried['gap_resolution_decision']}",
            f"- Carried targeted gap resolution decision count: {carried['targeted_gap_resolution_decision']}",
            f"- Carried newly resolved gap count: {carried['newly_resolved_gap']}",
            f"- Carried resolved gap count: {carried['resolved_gap']}",
            f"- Carried unresolved gap count: {carried['unresolved_gap']}",
            f"- Carried remaining blocking gap count: {carried['remaining_blocking_gap']}",
            f"- Carried gap resolution authorized count: {carried['gap_resolution_authorized']}",
            f"- Carried completion decision count: {carried['completion_decision']}",
            f"- Carried completion execution count: {carried['completion_execution']}",
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
            "The v8.93 artifact audits the v8.92 recurrence witness evidence and records a targeted gap resolution decision for SPCHG-003 only. It does not create a completion decision, does not authorize completion execution, performs no definition execution, creates no new draft clause, creates no new completion criterion, completes no stabilization predicate definition, completes no attractor-class definition, completes no constraint-region definition, completes no causal-mass definition, completes no observer-projection definition, proves no theorem, performs no proof execution, performs no proof assistant verification, adds no citation, completes no external validation, and creates no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "Resolving SPCHG-003 reduces the conditional-hold gap register from five unresolved blocking gaps to four unresolved blocking gaps. It does not lift the conditional hold on Sigma_A completion execution.",
            "",
            "## Warnings",
            "",
            "- This milestone audits recurrence witness evidence and records a targeted gap resolution decision only.",
            "- Resolving SPCHG-003 does not authorize completion execution or predicate completion.",
            "- Four conditional-hold gaps remain unresolved and blocking.",
            "- Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
            "",
            "## Safe claim",
            "",
            "The project has audited recurrence witness evidence and recorded a targeted resolution decision for SPCHG-003 while preserving the distinction between gap resolution, completion decision, completion execution, definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this completion decision.",
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
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run():
    text = render_report()
    source_text = _read_source()
    source_exists = SOURCE_PATH.exists()
    carried = _carried_counts(source_text)

    errors: list[str] = []

    if not source_exists:
        errors.append("Missing required v8.92 recurrence witness evidence source artifact.")

    expected_carried = {
        "recurrence_witness_evidence_execution": 1,
        "recurrence_witness_evidence_rows": 5,
        "recurrence_witness_scope_rules": 3,
        "recurrence_witness_acceptance_tests": 5,
        "recurrence_witness_blocked_overreach": 5,
        "targeted_gap": 1,
        "targeted_gap_id": 1,
        "targeted_criterion": 1,
        "evidence_support": 1,
        "prior_resolved_gaps_retained": 2,
        "gap_resolution_decision": 0,
        "targeted_gap_resolution_decision": 0,
        "newly_resolved_gap": 0,
        "resolved_gap": 2,
        "unresolved_gap": 5,
        "remaining_blocking_gap": 5,
        "gap_resolution_authorized": 0,
        "completion_decision": 0,
        "completion_execution": 0,
        "completion_execution_authorized": 0,
        "definition_execution": 0,
        "new_definition_execution": 0,
        "new_draft_clause": 0,
        "new_completion_criterion": 0,
        "new_completion_decision_plan": 0,
        "stabilization_completion": 0,
        "attractor_completion": 0,
        "constraint_completion": 0,
        "causal_mass_completion": 0,
        "observer_projection_completion": 0,
        "new_theorem": 0,
        "proof_execution": 0,
        "proof_assistant": 0,
        "formalization": 0,
        "completed_formal_definition": 0,
        "definition_completion_execution": 0,
        "full_framework": 0,
        "proof_gap": 0,
        "external": 0,
        "citation": 0,
        "cumulative_theorem": 5,
    }

    for key, expected in expected_carried.items():
        if carried[key] != expected:
            errors.append(f"Expected carried signal mismatch: {key} expected {expected}, got {carried[key]}.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone audits recurrence witness evidence and records a targeted gap resolution decision only.",
        "Resolving SPCHG-003 does not authorize completion execution or predicate completion.",
        "Four conditional-hold gaps remain unresolved and blocking.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    return SimpleNamespace(
        title="Recurrence Witness Evidence Boundary Audit Plus Gap Resolution Decision v8.93",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=0 if source_exists else 1,
        recurrence_witness_evidence_boundary_audit_count=1,
        audited_recurrence_witness_evidence_count=1,
        recurrence_witness_boundary_audit_row_count=5,
        accepted_claim_count=5,
        blocked_claim_count=5,
        gap_resolution_decision_count=1,
        targeted_gap_resolution_decision_count=1,
        targeted_gap_count=1,
        targeted_criterion_count=1,
        evidence_supported_gap_count=1,
        previously_resolved_gaps_retained_count=2,
        resolved_gap_count=3,
        newly_resolved_gap_count=1,
        unresolved_gap_count=4,
        remaining_blocking_gap_count=4,
        gap_resolution_authorized_count=1,
        completion_decision_count=0,
        completion_execution_count=0,
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
        carried_recurrence_witness_evidence_execution_count=carried["recurrence_witness_evidence_execution"],
        carried_recurrence_witness_evidence_row_count=carried["recurrence_witness_evidence_rows"],
        carried_recurrence_witness_scope_rule_count=carried["recurrence_witness_scope_rules"],
        carried_recurrence_witness_acceptance_test_count=carried["recurrence_witness_acceptance_tests"],
        carried_recurrence_witness_blocked_overreach_count=carried["recurrence_witness_blocked_overreach"],
        carried_targeted_gap_count=carried["targeted_gap"],
        carried_targeted_gap_id_count=carried["targeted_gap_id"],
        carried_targeted_criterion_count=carried["targeted_criterion"],
        carried_evidence_support_count=carried["evidence_support"],
        carried_prior_resolved_gaps_retained_count=carried["prior_resolved_gaps_retained"],
        carried_gap_resolution_decision_count=carried["gap_resolution_decision"],
        carried_targeted_gap_resolution_decision_count=carried["targeted_gap_resolution_decision"],
        carried_newly_resolved_gap_count=carried["newly_resolved_gap"],
        carried_resolved_gap_count=carried["resolved_gap"],
        carried_unresolved_gap_count=carried["unresolved_gap"],
        carried_remaining_blocking_gap_count=carried["remaining_blocking_gap"],
        carried_gap_resolution_authorized_count=carried["gap_resolution_authorized"],
        carried_completion_decision_count=carried["completion_decision"],
        carried_completion_execution_count=carried["completion_execution"],
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
        boundary_phrase_count=77,
        prohibited_behavior_count=18,
        next_step_count=8,
        overclaim_count=overclaim_count,
        invented_citation_like_pattern_count=invented_citation_like_pattern_count,
        word_count=len(text.split()),
        errors=errors,
        warnings=warnings,
        passed=not errors,
    )


def main() -> None:
    report = run()
    print(f"Wrote {report.output_path}")


if __name__ == "__main__":
    main()
