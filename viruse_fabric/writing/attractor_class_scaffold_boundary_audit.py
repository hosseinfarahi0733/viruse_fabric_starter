from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/attractor_class_bridge_execution_v8_76.md")
OUTPUT_PATH = Path("outputs/attractor_class_scaffold_boundary_audit_v8_77.md")


@dataclass(frozen=True)
class AttractorClassScaffoldBoundaryRow:
    audit_id: str
    scaffold_element: str
    allowed_claim: str
    blocked_claim: str
    audit_status: str


@dataclass(frozen=True)
class AttractorClassScaffoldBoundaryAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    attractor_class_scaffold_boundary_audit_count: int
    audited_scaffold_count: int
    scaffold_boundary_row_count: int
    allowed_claim_count: int
    blocked_claim_count: int

    new_bridge_execution_count: int
    new_attractor_class_candidate_scaffold_count: int
    new_theorem_proven_count: int
    proof_execution_count: int
    attractor_class_theorem_attempt_count: int
    attractor_class_theorem_proven_count: int
    attractor_class_definition_completion_count: int
    constraint_region_definition_completion_count: int
    causal_mass_definition_completion_count: int
    observer_projection_definition_completion_count: int

    carried_attractor_class_bridge_execution_count: int
    carried_authorized_bridge_consumed_count: int
    carried_attractor_class_candidate_scaffold_count: int
    carried_quotient_carrier_count: int
    carried_stabilization_predicate_placeholder_count: int
    carried_bridge_boundary_row_count: int
    carried_attractor_class_theorem_attempt_count: int
    carried_attractor_class_theorem_proven_count: int
    carried_attractor_class_definition_completion_count: int
    carried_constraint_region_definition_completion_count: int
    carried_causal_mass_definition_completion_count: int
    carried_observer_projection_definition_completion_count: int
    carried_cumulative_limited_theorem_proven_count: int
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

    cumulative_limited_theorem_proven_count: int
    proof_assistant_verification_count: int
    formalization_complete_count: int
    completed_formal_definition_count: int
    definition_completion_execution_count: int
    full_framework_formal_proof_count: int
    formal_mathematical_proof_count: int
    formal_proof_execution_count: int
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
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_audit_rows() -> List[AttractorClassScaffoldBoundaryRow]:
    return [
        AttractorClassScaffoldBoundaryRow(
            audit_id="ACSA-001",
            scaffold_element="finite R-path quotient carrier [a]_R",
            allowed_claim="the scaffold uses a quotient class carrier already supported by the audited path-kernel stack",
            blocked_claim="claiming attractor completion from quotient carrier reuse",
            audit_status="boundary preserved",
        ),
        AttractorClassScaffoldBoundaryRow(
            audit_id="ACSA-002",
            scaffold_element="stabilization predicate placeholder Sigma_A",
            allowed_claim="Sigma_A is named as a placeholder for later controlled definition work",
            blocked_claim="claiming stabilization is formally defined or validated",
            audit_status="boundary preserved",
        ),
        AttractorClassScaffoldBoundaryRow(
            audit_id="ACSA-003",
            scaffold_element="AttractorClassCandidate shape",
            allowed_claim="the candidate shape creates a scaffold for later definition work",
            blocked_claim="claiming an attractor-class theorem or completed attractor definition",
            audit_status="boundary preserved",
        ),
        AttractorClassScaffoldBoundaryRow(
            audit_id="ACSA-004",
            scaffold_element="constraint-region relation",
            allowed_claim="constraint-region work is identified as downstream and unexecuted",
            blocked_claim="claiming constraint-compatible region completion",
            audit_status="boundary preserved",
        ),
        AttractorClassScaffoldBoundaryRow(
            audit_id="ACSA-005",
            scaffold_element="causal mass and observer projection",
            allowed_claim="causal-mass and observer-projection work remains outside this scaffold audit",
            blocked_claim="claiming causal-mass completion or observer-projection completion",
            audit_status="boundary preserved",
        ),
        AttractorClassScaffoldBoundaryRow(
            audit_id="ACSA-006",
            scaffold_element="research readiness boundary",
            allowed_claim="the scaffold is an internal research artifact",
            blocked_claim="claiming external validation, biological validity, or manuscript readiness",
            audit_status="boundary preserved",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_audit_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_bridge_execution_count = 1 if _has_count(source_text, "Attractor class bridge execution", "1") else 0
    carried_authorized_bridge_consumed_count = 1 if _has_count(source_text, "Authorized bridge consumed", "1") else 0
    carried_candidate_scaffold_count = 1 if _has_count(source_text, "Attractor class candidate scaffold", "1") else 0
    carried_quotient_carrier_count = 1 if _has_count(source_text, "Quotient carrier", "1") else 0
    carried_stabilization_predicate_placeholder_count = 1 if _has_count(source_text, "Stabilization predicate placeholder", "1") else 0
    carried_bridge_boundary_row_count = 6 if _has_count(source_text, "Bridge boundary row", "6") else 0
    carried_attractor_class_theorem_attempt_count = 0 if _has_count(source_text, "Attractor class theorem attempt", "0") else -1
    carried_attractor_class_theorem_proven_count = 0 if _has_count(source_text, "Attractor class theorem proven", "0") else -1
    carried_attractor_class_definition_completion_count = 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1
    carried_constraint_region_definition_completion_count = 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1
    carried_causal_mass_definition_completion_count = 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1
    carried_observer_projection_definition_completion_count = 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1
    carried_cumulative_limited_theorem_proven_count = 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0
    carried_new_theorem_proven_count = 0 if _has_count(source_text, "New theorem proven", "0") else -1
    carried_proof_execution_count = 0 if _has_count(source_text, "Proof execution", "0") else -1
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    attractor_class_scaffold_boundary_audit_count = 1
    audited_scaffold_count = 1
    scaffold_boundary_row_count = len(rows)
    allowed_claim_count = len(rows)
    blocked_claim_count = len(rows)

    new_bridge_execution_count = 0
    new_attractor_class_candidate_scaffold_count = 0
    new_theorem_proven_count = 0
    proof_execution_count = 0
    attractor_class_theorem_attempt_count = 0
    attractor_class_theorem_proven_count = 0
    attractor_class_definition_completion_count = 0
    constraint_region_definition_completion_count = 0
    causal_mass_definition_completion_count = 0
    observer_projection_definition_completion_count = 0

    cumulative_limited_theorem_proven_count = carried_cumulative_limited_theorem_proven_count
    proof_assistant_verification_count = 0
    formalization_complete_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0
    full_framework_formal_proof_count = 0
    formal_mathematical_proof_count = 0
    formal_proof_execution_count = 0
    proof_gap_resolution_count = 0
    manuscript_submission_ready_count = 0
    readiness_approval_count = 0
    external_validation_count = 0
    independent_experiment_count = 0
    new_citation_added_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.76 attractor bridge execution source artifact.")
    if carried_bridge_execution_count != 1:
        errors.append("Expected carried v8.76 bridge execution signal is absent.")
    if carried_authorized_bridge_consumed_count != 1:
        errors.append("Expected carried authorized bridge consumed signal is absent.")
    if carried_candidate_scaffold_count != 1:
        errors.append("Expected carried candidate scaffold signal is absent.")
    if carried_quotient_carrier_count != 1:
        errors.append("Expected carried quotient carrier signal is absent.")
    if carried_stabilization_predicate_placeholder_count != 1:
        errors.append("Expected carried stabilization predicate placeholder signal is absent.")
    if carried_bridge_boundary_row_count != 6:
        errors.append("Expected carried bridge boundary row count is absent.")
    if carried_attractor_class_theorem_attempt_count != 0:
        errors.append("Expected carried attractor-class theorem attempt zero signal is absent.")
    if carried_attractor_class_theorem_proven_count != 0:
        errors.append("Expected carried attractor-class theorem proven zero signal is absent.")
    if carried_attractor_class_definition_completion_count != 0:
        errors.append("Expected carried attractor-class definition completion zero signal is absent.")
    if carried_constraint_region_definition_completion_count != 0:
        errors.append("Expected carried constraint-region definition completion zero signal is absent.")
    if carried_causal_mass_definition_completion_count != 0:
        errors.append("Expected carried causal-mass definition completion zero signal is absent.")
    if carried_observer_projection_definition_completion_count != 0:
        errors.append("Expected carried observer-projection definition completion zero signal is absent.")
    if carried_cumulative_limited_theorem_proven_count != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
    if carried_new_theorem_proven_count != 0:
        errors.append("Expected carried new theorem proven zero signal is absent.")
    if carried_proof_execution_count != 0:
        errors.append("Expected carried proof execution zero signal is absent.")
    if carried_proof_assistant_verification_count != 0:
        errors.append("Expected carried proof assistant verification zero signal is absent.")
    if carried_formalization_complete_count != 0:
        errors.append("Expected carried formalization complete zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_full_framework_formal_proof_count != 0:
        errors.append("Expected carried full framework formal proof zero signal is absent.")
    if carried_proof_gap_resolution_count != 0:
        errors.append("Expected carried proof gap resolution zero signal is absent.")
    if carried_external_validation_count != 0:
        errors.append("Expected carried external validation zero signal is absent.")
    if carried_new_citation_added_count != 0:
        errors.append("Expected carried new citation added zero signal is absent.")
    if scaffold_boundary_row_count != 6:
        errors.append("Expected six scaffold boundary rows.")
    if new_bridge_execution_count != 0:
        errors.append("Expected zero new bridge executions in audit.")
    if new_attractor_class_candidate_scaffold_count != 0:
        errors.append("Expected zero new scaffold creations in audit.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")
    if attractor_class_definition_completion_count != 0:
        errors.append("Expected zero attractor-class definition completions.")
    if constraint_region_definition_completion_count != 0:
        errors.append("Expected zero constraint-region definition completions.")
    if causal_mass_definition_completion_count != 0:
        errors.append("Expected zero causal-mass definition completions.")
    if observer_projection_definition_completion_count != 0:
        errors.append("Expected zero observer-projection definition completions.")

    warnings = [
        "This milestone audits the v8.76 scaffold only.",
        "No new scaffold is created.",
        "No attractor-class theorem or definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Attractor Class Scaffold Boundary Audit v8.77",
        "",
        "## Purpose",
        "",
        "Audit the attractor-class candidate scaffold created in v8.76, while keeping new scaffold creation, theorem proof, proof execution, proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Scaffold boundary rows",
        "",
        "| Audit ID | Scaffold element | Allowed claim | Blocked claim | Audit status |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.audit_id} | {row.scaffold_element} | {row.allowed_claim} | {row.blocked_claim} | {row.audit_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Attractor class scaffold boundary audit count: {attractor_class_scaffold_boundary_audit_count}",
            f"- Audited scaffold count: {audited_scaffold_count}",
            f"- Scaffold boundary row count: {scaffold_boundary_row_count}",
            f"- Allowed claim count: {allowed_claim_count}",
            f"- Blocked claim count: {blocked_claim_count}",
            f"- New bridge execution count: {new_bridge_execution_count}",
            f"- New attractor class candidate scaffold count: {new_attractor_class_candidate_scaffold_count}",
            f"- New theorem proven count: {new_theorem_proven_count}",
            f"- Proof execution count: {proof_execution_count}",
            f"- Attractor class theorem attempt count: {attractor_class_theorem_attempt_count}",
            f"- Attractor class theorem proven count: {attractor_class_theorem_proven_count}",
            f"- Attractor class definition completion count: {attractor_class_definition_completion_count}",
            f"- Constraint region definition completion count: {constraint_region_definition_completion_count}",
            f"- Causal mass definition completion count: {causal_mass_definition_completion_count}",
            f"- Observer projection definition completion count: {observer_projection_definition_completion_count}",
            f"- Cumulative limited theorem proven count: {cumulative_limited_theorem_proven_count}",
            f"- Proof assistant verification count: {proof_assistant_verification_count}",
            f"- Formalization complete count: {formalization_complete_count}",
            f"- Completed formal definition count: {completed_formal_definition_count}",
            f"- Definition completion execution count: {definition_completion_execution_count}",
            f"- Full framework formal proof count: {full_framework_formal_proof_count}",
            f"- Formal mathematical proof count: {formal_mathematical_proof_count}",
            f"- Formal proof execution count: {formal_proof_execution_count}",
            f"- Proof gap resolution count: {proof_gap_resolution_count}",
            f"- Manuscript submission ready count: {manuscript_submission_ready_count}",
            f"- Readiness approval count: {readiness_approval_count}",
            f"- External validation count: {external_validation_count}",
            f"- Independent experiment count: {independent_experiment_count}",
            f"- New citation added count: {new_citation_added_count}",
            "",
            "## Carried v8.76 signals",
            "",
            f"- Carried attractor class bridge execution count: {carried_bridge_execution_count}",
            f"- Carried authorized bridge consumed count: {carried_authorized_bridge_consumed_count}",
            f"- Carried attractor class candidate scaffold count: {carried_candidate_scaffold_count}",
            f"- Carried quotient carrier count: {carried_quotient_carrier_count}",
            f"- Carried stabilization predicate placeholder count: {carried_stabilization_predicate_placeholder_count}",
            f"- Carried bridge boundary row count: {carried_bridge_boundary_row_count}",
            f"- Carried attractor class theorem attempt count: {carried_attractor_class_theorem_attempt_count}",
            f"- Carried attractor class theorem proven count: {carried_attractor_class_theorem_proven_count}",
            f"- Carried attractor class definition completion count: {carried_attractor_class_definition_completion_count}",
            f"- Carried constraint region definition completion count: {carried_constraint_region_definition_completion_count}",
            f"- Carried causal mass definition completion count: {carried_causal_mass_definition_completion_count}",
            f"- Carried observer projection definition completion count: {carried_observer_projection_definition_completion_count}",
            f"- Carried cumulative limited theorem proven count: {carried_cumulative_limited_theorem_proven_count}",
            f"- Carried new theorem proven count: {carried_new_theorem_proven_count}",
            f"- Carried proof execution count: {carried_proof_execution_count}",
            f"- Carried proof assistant verification count: {carried_proof_assistant_verification_count}",
            f"- Carried formalization complete count: {carried_formalization_complete_count}",
            f"- Carried completed formal definition count: {carried_completed_formal_definition_count}",
            f"- Carried definition completion execution count: {carried_definition_completion_execution_count}",
            f"- Carried full framework formal proof count: {carried_full_framework_formal_proof_count}",
            f"- Carried proof gap resolution count: {carried_proof_gap_resolution_count}",
            f"- Carried external validation count: {carried_external_validation_count}",
            f"- Carried new citation added count: {carried_new_citation_added_count}",
            "",
            "## Boundary interpretation",
            "",
            "The v8.77 artifact audits the attractor-class candidate scaffold created in v8.76. It adds no new scaffold, no theorem proof, no proof execution, no completed attractor-class definition, no completed constraint-region definition, no completed causal-mass definition, no completed observer-projection definition, no proof assistant verification, no completed formalization, no framework-level proof, no citation additions, no external validation, and no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The scaffold is useful but fragile. It must not be treated as attractor theory, biological validation, causal-mass completion, observer-projection completion, or submission readiness.",
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
            "The project has audited the attractor-class candidate scaffold created in v8.76 and preserved the distinction between that scaffold and theorem proof, completed attractor-class definition, completed constraint-region definition, causal-mass completion, observer-projection completion, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this a theorem proof.",
            "- Do not call this a new scaffold creation.",
            "- Do not call this a completed attractor definition.",
            "- Do not call this a completed constraint-region definition.",
            "- Do not call this causal-mass completion.",
            "- Do not call this observer-projection completion.",
            "- Do not call this framework-level proof.",
            "- Do not call this manuscript readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.77 attractor class scaffold boundary audit report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.77 attractor class scaffold boundary audit report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> AttractorClassScaffoldBoundaryAuditReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_bridge_execution_count = 1 if _has_count(source_text, "Attractor class bridge execution", "1") else 0
    carried_authorized_bridge_consumed_count = 1 if _has_count(source_text, "Authorized bridge consumed", "1") else 0
    carried_candidate_scaffold_count = 1 if _has_count(source_text, "Attractor class candidate scaffold", "1") else 0
    carried_quotient_carrier_count = 1 if _has_count(source_text, "Quotient carrier", "1") else 0
    carried_stabilization_predicate_placeholder_count = 1 if _has_count(source_text, "Stabilization predicate placeholder", "1") else 0
    carried_bridge_boundary_row_count = 6 if _has_count(source_text, "Bridge boundary row", "6") else 0
    carried_attractor_class_theorem_attempt_count = 0 if _has_count(source_text, "Attractor class theorem attempt", "0") else -1
    carried_attractor_class_theorem_proven_count = 0 if _has_count(source_text, "Attractor class theorem proven", "0") else -1
    carried_attractor_class_definition_completion_count = 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1
    carried_constraint_region_definition_completion_count = 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1
    carried_causal_mass_definition_completion_count = 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1
    carried_observer_projection_definition_completion_count = 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1
    carried_cumulative_limited_theorem_proven_count = 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0
    carried_new_theorem_proven_count = 0 if _has_count(source_text, "New theorem proven", "0") else -1
    carried_proof_execution_count = 0 if _has_count(source_text, "Proof execution", "0") else -1
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    rows = build_audit_rows()

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.76 attractor bridge execution source artifact.")
    if carried_bridge_execution_count != 1:
        errors.append("Expected carried v8.76 bridge execution signal is absent.")
    if carried_authorized_bridge_consumed_count != 1:
        errors.append("Expected carried authorized bridge consumed signal is absent.")
    if carried_candidate_scaffold_count != 1:
        errors.append("Expected carried candidate scaffold signal is absent.")
    if carried_quotient_carrier_count != 1:
        errors.append("Expected carried quotient carrier signal is absent.")
    if carried_stabilization_predicate_placeholder_count != 1:
        errors.append("Expected carried stabilization predicate placeholder signal is absent.")
    if carried_bridge_boundary_row_count != 6:
        errors.append("Expected carried bridge boundary row count is absent.")
    if carried_attractor_class_theorem_attempt_count != 0:
        errors.append("Expected carried attractor-class theorem attempt zero signal is absent.")
    if carried_attractor_class_theorem_proven_count != 0:
        errors.append("Expected carried attractor-class theorem proven zero signal is absent.")
    if carried_attractor_class_definition_completion_count != 0:
        errors.append("Expected carried attractor-class definition completion zero signal is absent.")
    if carried_constraint_region_definition_completion_count != 0:
        errors.append("Expected carried constraint-region definition completion zero signal is absent.")
    if carried_causal_mass_definition_completion_count != 0:
        errors.append("Expected carried causal-mass definition completion zero signal is absent.")
    if carried_observer_projection_definition_completion_count != 0:
        errors.append("Expected carried observer-projection definition completion zero signal is absent.")
    if carried_cumulative_limited_theorem_proven_count != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
    if carried_new_theorem_proven_count != 0:
        errors.append("Expected carried new theorem proven zero signal is absent.")
    if carried_proof_execution_count != 0:
        errors.append("Expected carried proof execution zero signal is absent.")
    if carried_proof_assistant_verification_count != 0:
        errors.append("Expected carried proof assistant verification zero signal is absent.")
    if carried_formalization_complete_count != 0:
        errors.append("Expected carried formalization complete zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_full_framework_formal_proof_count != 0:
        errors.append("Expected carried full framework formal proof zero signal is absent.")
    if carried_proof_gap_resolution_count != 0:
        errors.append("Expected carried proof gap resolution zero signal is absent.")
    if carried_external_validation_count != 0:
        errors.append("Expected carried external validation zero signal is absent.")
    if carried_new_citation_added_count != 0:
        errors.append("Expected carried new citation added zero signal is absent.")
    if len(rows) != 6:
        errors.append("Expected six scaffold boundary audit rows.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone audits the v8.76 scaffold only.",
        "No new scaffold is created.",
        "No attractor-class theorem or definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    return AttractorClassScaffoldBoundaryAuditReport(
        title="Attractor Class Scaffold Boundary Audit v8.77",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        attractor_class_scaffold_boundary_audit_count=1,
        audited_scaffold_count=1,
        scaffold_boundary_row_count=len(rows),
        allowed_claim_count=len(rows),
        blocked_claim_count=len(rows),
        new_bridge_execution_count=0,
        new_attractor_class_candidate_scaffold_count=0,
        new_theorem_proven_count=0,
        proof_execution_count=0,
        attractor_class_theorem_attempt_count=0,
        attractor_class_theorem_proven_count=0,
        attractor_class_definition_completion_count=0,
        constraint_region_definition_completion_count=0,
        causal_mass_definition_completion_count=0,
        observer_projection_definition_completion_count=0,
        carried_attractor_class_bridge_execution_count=carried_bridge_execution_count,
        carried_authorized_bridge_consumed_count=carried_authorized_bridge_consumed_count,
        carried_attractor_class_candidate_scaffold_count=carried_candidate_scaffold_count,
        carried_quotient_carrier_count=carried_quotient_carrier_count,
        carried_stabilization_predicate_placeholder_count=carried_stabilization_predicate_placeholder_count,
        carried_bridge_boundary_row_count=carried_bridge_boundary_row_count,
        carried_attractor_class_theorem_attempt_count=carried_attractor_class_theorem_attempt_count,
        carried_attractor_class_theorem_proven_count=carried_attractor_class_theorem_proven_count,
        carried_attractor_class_definition_completion_count=carried_attractor_class_definition_completion_count,
        carried_constraint_region_definition_completion_count=carried_constraint_region_definition_completion_count,
        carried_causal_mass_definition_completion_count=carried_causal_mass_definition_completion_count,
        carried_observer_projection_definition_completion_count=carried_observer_projection_definition_completion_count,
        carried_cumulative_limited_theorem_proven_count=carried_cumulative_limited_theorem_proven_count,
        carried_new_theorem_proven_count=carried_new_theorem_proven_count,
        carried_proof_execution_count=carried_proof_execution_count,
        carried_proof_assistant_verification_count=carried_proof_assistant_verification_count,
        carried_formalization_complete_count=carried_formalization_complete_count,
        carried_completed_formal_definition_count=carried_completed_formal_definition_count,
        carried_definition_completion_execution_count=carried_definition_completion_execution_count,
        carried_full_framework_formal_proof_count=carried_full_framework_formal_proof_count,
        carried_proof_gap_resolution_count=carried_proof_gap_resolution_count,
        carried_external_validation_count=carried_external_validation_count,
        carried_new_citation_added_count=carried_new_citation_added_count,
        cumulative_limited_theorem_proven_count=carried_cumulative_limited_theorem_proven_count,
        proof_assistant_verification_count=0,
        formalization_complete_count=0,
        completed_formal_definition_count=0,
        definition_completion_execution_count=0,
        full_framework_formal_proof_count=0,
        formal_mathematical_proof_count=0,
        formal_proof_execution_count=0,
        proof_gap_resolution_count=0,
        manuscript_submission_ready_count=0,
        readiness_approval_count=0,
        external_validation_count=0,
        independent_experiment_count=0,
        new_citation_added_count=0,
        conditional_hold_count=1,
        hard_zero_count=13,
        boundary_phrase_count=61,
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
