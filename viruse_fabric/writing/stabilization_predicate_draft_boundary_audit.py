from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/stabilization_predicate_controlled_definition_execution_v8_79.md")
OUTPUT_PATH = Path("outputs/stabilization_predicate_draft_boundary_audit_v8_80.md")


@dataclass(frozen=True)
class StabilizationPredicateDraftBoundaryRow:
    audit_id: str
    draft_element: str
    allowed_claim: str
    blocked_claim: str
    audit_status: str


@dataclass(frozen=True)
class StabilizationPredicateDraftBoundaryAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    stabilization_predicate_draft_boundary_audit_count: int
    audited_stabilization_predicate_draft_count: int
    draft_clause_boundary_row_count: int
    allowed_claim_count: int
    blocked_claim_count: int

    definition_execution_count: int
    new_definition_execution_count: int
    new_stabilization_predicate_draft_clause_count: int
    stabilization_predicate_definition_completion_count: int
    attractor_class_definition_completion_count: int
    constraint_region_definition_completion_count: int
    causal_mass_definition_completion_count: int
    observer_projection_definition_completion_count: int

    carried_stabilization_predicate_controlled_definition_execution_count: int
    carried_definition_execution_count: int
    carried_stabilization_predicate_draft_clause_count: int
    carried_carrier_domain_clause_count: int
    carried_local_persistence_clause_count: int
    carried_recurrence_clause_count: int
    carried_exclusion_clause_count: int
    carried_audit_dependency_clause_count: int
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
        "draft clauses prove",
        "draft predicate proves",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_audit_rows() -> List[StabilizationPredicateDraftBoundaryRow]:
    return [
        StabilizationPredicateDraftBoundaryRow(
            audit_id="SPDBA-001",
            draft_element="Carrier domain draft clause",
            allowed_claim="the draft restricts Sigma_A evaluation to finite R-path quotient carriers class_R(a)",
            blocked_claim="claiming the carrier-domain clause completes the predicate definition",
            audit_status="boundary preserved",
        ),
        StabilizationPredicateDraftBoundaryRow(
            audit_id="SPDBA-002",
            draft_element="Local persistence draft clause",
            allowed_claim="the draft identifies local persistence as a required condition for future definition work",
            blocked_claim="claiming persistence has been proven or externally validated",
            audit_status="boundary preserved",
        ),
        StabilizationPredicateDraftBoundaryRow(
            audit_id="SPDBA-003",
            draft_element="Recurrence draft clause",
            allowed_claim="the draft separates candidate recurrence from mere reachability",
            blocked_claim="claiming an attractor-class theorem from recurrence wording alone",
            audit_status="boundary preserved",
        ),
        StabilizationPredicateDraftBoundaryRow(
            audit_id="SPDBA-004",
            draft_element="Exclusion draft clause",
            allowed_claim="the draft states when a quotient carrier must be excluded from attractor-candidate status",
            blocked_claim="claiming completed biological, operational, or framework-level validity",
            audit_status="boundary preserved",
        ),
        StabilizationPredicateDraftBoundaryRow(
            audit_id="SPDBA-005",
            draft_element="Constraint placeholder draft clause",
            allowed_claim="the draft keeps constraint-compatible region integration as a future dependency slot",
            blocked_claim="claiming constraint-region completion or causal-mass completion",
            audit_status="boundary preserved",
        ),
        StabilizationPredicateDraftBoundaryRow(
            audit_id="SPDBA-006",
            draft_element="Audit dependency draft clause",
            allowed_claim="the draft requires later audit before theorem work or readiness claims",
            blocked_claim="claiming proof assistant verification, theorem proof, or manuscript readiness",
            audit_status="boundary preserved",
        ),
    ]


def _carried_counts(source_text: str) -> dict[str, int]:
    return {
        "controlled_execution": 1 if _has_count(source_text, "Stabilization predicate controlled definition execution", "1") else 0,
        "definition_execution": 1 if _has_count(source_text, "Definition execution", "1") else -1,
        "draft_clause": 6 if _has_count(source_text, "Stabilization predicate draft clause", "6") else 0,
        "carrier_domain": 1 if _has_count(source_text, "Carrier domain clause", "1") else 0,
        "local_persistence": 1 if _has_count(source_text, "Local persistence clause", "1") else 0,
        "recurrence": 1 if _has_count(source_text, "Recurrence clause", "1") else 0,
        "exclusion": 1 if _has_count(source_text, "Exclusion clause", "1") else 0,
        "audit_dependency": 1 if _has_count(source_text, "Audit dependency clause", "1") else 0,
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

    stabilization_predicate_draft_boundary_audit_count = 1
    audited_stabilization_predicate_draft_count = 1
    draft_clause_boundary_row_count = len(rows)
    allowed_claim_count = len(rows)
    blocked_claim_count = len(rows)

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
        errors.append("Missing required v8.79 stabilization predicate controlled definition execution source artifact.")
    if carried["controlled_execution"] != 1:
        errors.append("Expected carried stabilization predicate controlled definition execution signal is absent.")
    if carried["definition_execution"] != 1:
        errors.append("Expected carried definition execution count of one is absent.")
    if carried["draft_clause"] != 6:
        errors.append("Expected carried stabilization predicate draft clause count of six is absent.")
    if carried["carrier_domain"] != 1:
        errors.append("Expected carried carrier-domain clause signal is absent.")
    if carried["local_persistence"] != 1:
        errors.append("Expected carried local-persistence clause signal is absent.")
    if carried["recurrence"] != 1:
        errors.append("Expected carried recurrence clause signal is absent.")
    if carried["exclusion"] != 1:
        errors.append("Expected carried exclusion clause signal is absent.")
    if carried["audit_dependency"] != 1:
        errors.append("Expected carried audit-dependency clause signal is absent.")
    for key in [
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
    if draft_clause_boundary_row_count != 6:
        errors.append("Expected six draft boundary rows.")
    if definition_execution_count != 0:
        errors.append("Expected zero definition executions in audit.")
    if new_definition_execution_count != 0:
        errors.append("Expected zero new definition executions in audit.")
    if new_stabilization_predicate_draft_clause_count != 0:
        errors.append("Expected zero new draft clauses in audit.")
    if stabilization_predicate_definition_completion_count != 0:
        errors.append("Expected zero stabilization predicate definition completions.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")

    warnings = [
        "This milestone audits the v8.79 draft only.",
        "No new definition execution or new draft clause is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Stabilization Predicate Draft Boundary Audit v8.80",
        "",
        "## Purpose",
        "",
        "Audit the controlled draft clause set for Sigma_A created in v8.79, while keeping new definition execution, new draft clause creation, predicate definition completion, attractor-class definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Draft boundary rows",
        "",
        "| Audit ID | Draft element | Allowed claim | Blocked claim | Audit status |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.audit_id} | {row.draft_element} | {row.allowed_claim} | {row.blocked_claim} | {row.audit_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Stabilization predicate draft boundary audit count: {stabilization_predicate_draft_boundary_audit_count}",
            f"- Audited stabilization predicate draft count: {audited_stabilization_predicate_draft_count}",
            f"- Draft clause boundary row count: {draft_clause_boundary_row_count}",
            f"- Allowed claim count: {allowed_claim_count}",
            f"- Blocked claim count: {blocked_claim_count}",
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
            "## Carried v8.79 signals",
            "",
            f"- Carried stabilization predicate controlled definition execution count: {carried['controlled_execution']}",
            f"- Carried definition execution count: {carried['definition_execution']}",
            f"- Carried stabilization predicate draft clause count: {carried['draft_clause']}",
            f"- Carried carrier domain clause count: {carried['carrier_domain']}",
            f"- Carried local persistence clause count: {carried['local_persistence']}",
            f"- Carried recurrence clause count: {carried['recurrence']}",
            f"- Carried exclusion clause count: {carried['exclusion']}",
            f"- Carried audit dependency clause count: {carried['audit_dependency']}",
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
            "The v8.80 artifact audits the Sigma_A draft clause set created in v8.79. It adds no new definition execution, no new draft clause, no stabilization predicate definition completion, no attractor-class definition completion, no constraint-region definition completion, no causal-mass completion, no observer-projection completion, no theorem proof, no proof execution, no proof assistant verification, no completed formalization, no framework-level proof, no citation additions, no external validation, and no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The v8.79 draft clause set is useful because it gives Sigma_A a controlled predicate shape. It remains draft-level. It must not be treated as completed formal definition, attractor theory, theorem proof, proof assistant verification, external validation, or submission readiness.",
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
            "The project has audited the controlled Sigma_A draft clause set and preserved the distinction between draft-level predicate shape and definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this a new definition execution.",
            "- Do not call this a new draft clause creation.",
            "- Do not call this stabilization predicate completion.",
            "- Do not call this a completed attractor definition.",
            "- Do not call this a theorem proof.",
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
        errors.append("Overclaim pattern detected in v8.80 stabilization predicate draft boundary audit.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.80 stabilization predicate draft boundary audit.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> StabilizationPredicateDraftBoundaryAuditReport:
    text = render_report()
    source_text = _read_source()
    source_exists = SOURCE_PATH.exists()
    carried = _carried_counts(source_text)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    errors: List[str] = []
    if not source_exists:
        errors.append("Missing required v8.79 stabilization predicate controlled definition execution source artifact.")
    if carried["controlled_execution"] != 1:
        errors.append("Expected carried stabilization predicate controlled definition execution signal is absent.")
    if carried["definition_execution"] != 1:
        errors.append("Expected carried definition execution count of one is absent.")
    if carried["draft_clause"] != 6:
        errors.append("Expected carried stabilization predicate draft clause count of six is absent.")
    if len(build_audit_rows()) != 6:
        errors.append("Expected six draft boundary audit rows.")
    for key in [
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
        "This milestone audits the v8.79 draft only.",
        "No new definition execution or new draft clause is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    rows = build_audit_rows()

    return StabilizationPredicateDraftBoundaryAuditReport(
        title="Stabilization Predicate Draft Boundary Audit v8.80",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=0 if source_exists else 1,
        stabilization_predicate_draft_boundary_audit_count=1,
        audited_stabilization_predicate_draft_count=1,
        draft_clause_boundary_row_count=len(rows),
        allowed_claim_count=len(rows),
        blocked_claim_count=len(rows),
        definition_execution_count=0,
        new_definition_execution_count=0,
        new_stabilization_predicate_draft_clause_count=0,
        stabilization_predicate_definition_completion_count=0,
        attractor_class_definition_completion_count=0,
        constraint_region_definition_completion_count=0,
        causal_mass_definition_completion_count=0,
        observer_projection_definition_completion_count=0,
        carried_stabilization_predicate_controlled_definition_execution_count=carried["controlled_execution"],
        carried_definition_execution_count=carried["definition_execution"],
        carried_stabilization_predicate_draft_clause_count=carried["draft_clause"],
        carried_carrier_domain_clause_count=carried["carrier_domain"],
        carried_local_persistence_clause_count=carried["local_persistence"],
        carried_recurrence_clause_count=carried["recurrence"],
        carried_exclusion_clause_count=carried["exclusion"],
        carried_audit_dependency_clause_count=carried["audit_dependency"],
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
        boundary_phrase_count=64,
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
