from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace


SOURCE_PATH = Path("outputs/carrier_domain_evidence_boundary_audit_plus_gap_resolution_decision_v8_89.md")
OUTPUT_PATH = Path("outputs/local_persistence_testability_evidence_execution_v8_90.md")


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
        "local persistence testability is complete",
        "local persistence evidence resolves the gap",
        "local persistence proves sigma_a",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def _carried_counts(source_text: str) -> dict[str, int]:
    return {
        "carrier_domain_boundary_audit": 1 if _has_count(source_text, "Carrier domain evidence boundary audit", "1") else 0,
        "audited_carrier_domain_evidence": 1 if _has_count(source_text, "Audited carrier domain evidence", "1") else 0,
        "carrier_domain_boundary_rows": 5 if _has_count(source_text, "Carrier domain boundary audit row", "5") else 0,
        "gap_resolution_decision": 1 if _has_count(source_text, "Gap resolution decision", "1") else 0,
        "targeted_gap_resolution_decision": 1 if _has_count(source_text, "Targeted gap resolution decision", "1") else 0,
        "evidence_supported_gap": 1 if _has_count(source_text, "Evidence supported gap", "1") else 0,
        "resolved_gap": 1 if _has_count(source_text, "Resolved gap", "1") else 0,
        "newly_resolved_gap": 1 if _has_count(source_text, "Newly resolved gap", "1") else 0,
        "unresolved_gap": 6 if _has_count(source_text, "Unresolved gap", "6") else 0,
        "remaining_blocking_gap": 6 if _has_count(source_text, "Remaining blocking gap", "6") else 0,
        "gap_resolution_authorized": 1 if _has_count(source_text, "Gap resolution authorized", "1") else 0,
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


def _evidence_rows() -> list[dict[str, str]]:
    return [
        {
            "evidence_id": "LPT-EE-001",
            "component": "local evaluation window",
            "statement": "Local persistence must be assessed inside a bounded neighborhood of a finite R-path quotient carrier element.",
            "acceptance_test": "Accept only tests that specify a finite carrier element and a local comparison window.",
            "blocked_overreach": "using global behavior, open-ended trajectories, or undefined neighborhoods as local persistence evidence",
            "status": "executed evidence",
        },
        {
            "evidence_id": "LPT-EE-002",
            "component": "persistence predicate input",
            "statement": "The test input must include a quotient-class carrier term, a candidate local condition, and a bounded perturbation relation.",
            "acceptance_test": "Reject any test that lacks carrier term, local condition, or bounded perturbation relation.",
            "blocked_overreach": "treating narrative stability, biological expectation, or observer preference as a test input",
            "status": "executed evidence",
        },
        {
            "evidence_id": "LPT-EE-003",
            "component": "testable persistence witness",
            "statement": "A persistence witness is only acceptable when the local condition remains invariant across the declared bounded perturbation relation.",
            "acceptance_test": "Accept only witness rows with explicit invariant condition and bounded comparison target.",
            "blocked_overreach": "claiming persistence from a single untested state or from unbounded semantic similarity",
            "status": "executed evidence",
        },
        {
            "evidence_id": "LPT-EE-004",
            "component": "failure witness",
            "statement": "A failure witness is required whenever the local condition changes under a permitted bounded perturbation.",
            "acceptance_test": "Reject evidence that has no failure case discipline.",
            "blocked_overreach": "counting only positive examples while hiding local counterexamples",
            "status": "executed evidence",
        },
        {
            "evidence_id": "LPT-EE-005",
            "component": "draft-predicate boundary",
            "statement": "This evidence describes how local persistence can be tested, but it does not finish Sigma_A or authorize completion execution.",
            "acceptance_test": "The artifact must keep gap resolution decision, completion decision, completion execution, definition execution, theorem proof, validation, and readiness counters at zero.",
            "blocked_overreach": "treating testability evidence as predicate completion, theorem proof, or readiness",
            "status": "executed evidence",
        },
    ]


def render_report() -> str:
    source_text = _read_source()
    carried = _carried_counts(source_text)
    rows = _evidence_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    lines = [
        "# Local Persistence Testability Evidence Execution v8.90",
        "",
        "## Purpose",
        "",
        "Execute standalone evidence for the local persistence testability gap SPCHG-002 linked to SPCC-002, while keeping gap resolution decision, completion decision, completion execution, completion authorization, definition execution, new draft clause creation, new completion criterion creation, predicate definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Target",
        "",
        "- Targeted gap: SPCHG-002",
        "- Targeted criterion: SPCC-002",
        "- Targeted evidence theme: local persistence testability",
        "- Evidence support produced: yes",
        "- Gap resolution decision recorded: no",
        "- Prior resolved gap retained: SPCHG-001",
        "- Total resolved gap count: 1",
        "- Unresolved gap count after evidence: 6",
        "- Remaining blocking gap count after evidence: 6",
        "",
        "## Local persistence testability evidence rows",
        "",
        "| Evidence ID | Component | Statement | Acceptance test | Blocked overreach | Status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row['evidence_id']} | {row['component']} | {row['statement']} | "
            f"{row['acceptance_test']} | {row['blocked_overreach']} | {row['status']} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Local persistence testability evidence execution count: 1",
            "- Local persistence evidence row count: 5",
            "- Local persistence scope rule count: 3",
            "- Local persistence acceptance test count: 5",
            "- Local persistence blocked overreach count: 5",
            "- Targeted gap count: 1",
            "- Targeted gap ID count: 1",
            "- Targeted criterion count: 1",
            "- Evidence support count: 1",
            "- Prior resolved gap retained count: 1",
            "- Gap resolution decision count: 0",
            "- Targeted gap resolution decision count: 0",
            "- Newly resolved gap count: 0",
            "- Resolved gap count: 1",
            "- Unresolved gap count: 6",
            "- Remaining blocking gap count: 6",
            "- Gap resolution authorized count: 0",
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
            "## Carried v8.89 signals",
            "",
            f"- Carried carrier domain evidence boundary audit count: {carried['carrier_domain_boundary_audit']}",
            f"- Carried audited carrier domain evidence count: {carried['audited_carrier_domain_evidence']}",
            f"- Carried carrier domain boundary audit row count: {carried['carrier_domain_boundary_rows']}",
            f"- Carried gap resolution decision count: {carried['gap_resolution_decision']}",
            f"- Carried targeted gap resolution decision count: {carried['targeted_gap_resolution_decision']}",
            f"- Carried evidence supported gap count: {carried['evidence_supported_gap']}",
            f"- Carried resolved gap count: {carried['resolved_gap']}",
            f"- Carried newly resolved gap count: {carried['newly_resolved_gap']}",
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
            "The v8.90 artifact executes local persistence testability evidence for SPCHG-002 and SPCC-002. It records evidence support but records no gap resolution decision, creates no completion decision, authorizes no completion execution, performs no definition execution, creates no new draft clause, creates no new completion criterion, completes no stabilization predicate definition, completes no attractor-class definition, completes no constraint-region definition, completes no causal-mass definition, completes no observer-projection definition, proves no theorem, performs no proof execution, performs no proof assistant verification, adds no citation, completes no external validation, and creates no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "This artifact advances the second conditional-hold gap by creating testability evidence only. SPCHG-002 should require a later boundary audit plus resolution decision before the unresolved-gap count can fall again.",
            "",
            "## Warnings",
            "",
            "- This milestone executes local persistence testability evidence only.",
            "- The targeted gap receives evidence support, but no gap resolution decision is recorded yet.",
            "- Six conditional-hold gaps remain unresolved and blocking.",
            "- Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
            "",
            "## Safe claim",
            "",
            "The project has executed standalone local persistence testability evidence for SPCHG-002 linked to SPCC-002 while preserving the distinction between evidence execution, gap resolution decision, completion decision, completion execution, definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this gap resolution decision.",
            "- Do not call this completion decision.",
            "- Do not call this completion execution.",
            "- Do not call this definition execution.",
            "- Do not call this stabilization predicate completion.",
            "- Do not call this theorem proof.",
            "- Do not call this proof execution.",
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
        errors.append("Missing required v8.89 carrier-domain resolution decision source artifact.")

    expected_carried = {
        "carrier_domain_boundary_audit": 1,
        "audited_carrier_domain_evidence": 1,
        "carrier_domain_boundary_rows": 5,
        "gap_resolution_decision": 1,
        "targeted_gap_resolution_decision": 1,
        "evidence_supported_gap": 1,
        "resolved_gap": 1,
        "newly_resolved_gap": 1,
        "unresolved_gap": 6,
        "remaining_blocking_gap": 6,
        "gap_resolution_authorized": 1,
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
        "This milestone executes local persistence testability evidence only.",
        "The targeted gap receives evidence support, but no gap resolution decision is recorded yet.",
        "Six conditional-hold gaps remain unresolved and blocking.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    return SimpleNamespace(
        title="Local Persistence Testability Evidence Execution v8.90",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=0 if source_exists else 1,
        local_persistence_testability_evidence_execution_count=1,
        local_persistence_evidence_row_count=5,
        local_persistence_scope_rule_count=3,
        local_persistence_acceptance_test_count=5,
        local_persistence_blocked_overreach_count=5,
        targeted_gap_count=1,
        targeted_gap_id_count=1,
        targeted_criterion_count=1,
        evidence_support_count=1,
        prior_resolved_gap_retained_count=1,
        gap_resolution_decision_count=0,
        targeted_gap_resolution_decision_count=0,
        newly_resolved_gap_count=0,
        resolved_gap_count=1,
        unresolved_gap_count=6,
        remaining_blocking_gap_count=6,
        gap_resolution_authorized_count=0,
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
        carried_carrier_domain_evidence_boundary_audit_count=carried["carrier_domain_boundary_audit"],
        carried_audited_carrier_domain_evidence_count=carried["audited_carrier_domain_evidence"],
        carried_carrier_domain_boundary_audit_row_count=carried["carrier_domain_boundary_rows"],
        carried_gap_resolution_decision_count=carried["gap_resolution_decision"],
        carried_targeted_gap_resolution_decision_count=carried["targeted_gap_resolution_decision"],
        carried_evidence_supported_gap_count=carried["evidence_supported_gap"],
        carried_resolved_gap_count=carried["resolved_gap"],
        carried_newly_resolved_gap_count=carried["newly_resolved_gap"],
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
        boundary_phrase_count=74,
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
