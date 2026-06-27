from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/path_kernel_theorem_stack_boundary_audit_v8_74.md")
OUTPUT_PATH = Path("outputs/attractor_class_bridge_authorization_plan_v8_75.md")


@dataclass(frozen=True)
class AttractorClassBridgeCandidate:
    candidate_id: str
    candidate_name: str
    source_structure: str
    target_structure: str
    authorization_status: str
    allowed_next_step: str
    blocked_claim: str


@dataclass(frozen=True)
class AttractorClassBridgeAuthorizationPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    attractor_class_bridge_authorization_plan_count: int
    bridge_candidate_count: int
    selected_bridge_candidate_count: int
    authorized_bridge_candidate_count: int
    bridge_execution_count: int
    attractor_class_theorem_attempt_count: int
    attractor_class_definition_completion_count: int
    constraint_region_definition_completion_count: int

    carried_path_kernel_theorem_stack_boundary_audit_count: int
    carried_audited_limited_theorem_count: int
    carried_theorem_stack_count: int
    carried_theorem_stack_boundary_audit_row_count: int
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
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_candidates() -> List[AttractorClassBridgeCandidate]:
    return [
        AttractorClassBridgeCandidate(
            candidate_id="ACB-001",
            candidate_name="Quotient class as attractor-class carrier",
            source_structure="finite R-path quotient class [a]_R from PKT-005",
            target_structure="candidate attractor class carrier for later controlled definition",
            authorization_status="authorized for next controlled bridge execution",
            allowed_next_step="define an attractor-class candidate as a quotient class plus an explicitly declared stabilization predicate",
            blocked_claim="claiming attractor theory completion from quotient classes alone",
        ),
        AttractorClassBridgeCandidate(
            candidate_id="ACB-002",
            candidate_name="Reachability basin as precursor region",
            source_structure="Reach_R preorder and mutual reachability quotient family",
            target_structure="candidate basin-like precursor for constraint-compatible region work",
            authorization_status="deferred",
            allowed_next_step="use only after the attractor-class carrier bridge is audited",
            blocked_claim="claiming basin validity or biological meaning without additional definitions",
        ),
        AttractorClassBridgeCandidate(
            candidate_id="ACB-003",
            candidate_name="Constraint-compatible region bridge",
            source_structure="quotient partition induced by mutual finite R-path reachability",
            target_structure="candidate constraint-compatible region scaffold",
            authorization_status="deferred",
            allowed_next_step="use only after attractor-class candidate boundaries are established",
            blocked_claim="claiming causal mass, observer projection, or framework-level geometry from the path kernel stack",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    candidates = build_candidates()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_stack_audit_count = 1 if _has_count(source_text, "Path kernel theorem stack boundary audit", "1") else 0
    carried_audited_limited_theorem_count = 5 if _has_count(source_text, "Audited limited theorem", "5") else 0
    carried_theorem_stack_count = 1 if _has_count(source_text, "Theorem stack", "1") else 0
    carried_theorem_stack_boundary_audit_row_count = 7 if _has_count(source_text, "Theorem stack boundary audit row", "7") else 0
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

    attractor_class_bridge_authorization_plan_count = 1
    bridge_candidate_count = len(candidates)
    selected_bridge_candidate_count = 1
    authorized_bridge_candidate_count = 1
    bridge_execution_count = 0
    attractor_class_theorem_attempt_count = 0
    attractor_class_definition_completion_count = 0
    constraint_region_definition_completion_count = 0

    new_theorem_proven_count = 0
    cumulative_limited_theorem_proven_count = carried_cumulative_limited_theorem_proven_count
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
        errors.append("Missing required v8.74 path kernel theorem stack audit source artifact.")
    if carried_stack_audit_count != 1:
        errors.append("Expected carried v8.74 theorem stack audit signal is absent.")
    if carried_audited_limited_theorem_count != 5:
        errors.append("Expected carried audited limited theorem count of five is absent.")
    if carried_theorem_stack_count != 1:
        errors.append("Expected carried theorem stack signal is absent.")
    if carried_theorem_stack_boundary_audit_row_count != 7:
        errors.append("Expected carried theorem stack boundary audit row count is absent.")
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
    if bridge_candidate_count != 3:
        errors.append("Expected three bridge candidates.")
    if selected_bridge_candidate_count != 1:
        errors.append("Expected one selected bridge candidate.")
    if authorized_bridge_candidate_count != 1:
        errors.append("Expected one authorized bridge candidate.")
    if bridge_execution_count != 0:
        errors.append("Expected zero bridge executions in authorization plan.")
    if attractor_class_theorem_attempt_count != 0:
        errors.append("Expected zero attractor-class theorem attempts.")
    if attractor_class_definition_completion_count != 0:
        errors.append("Expected zero attractor-class definition completions.")
    if constraint_region_definition_completion_count != 0:
        errors.append("Expected zero constraint-region definition completions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")
    if cumulative_limited_theorem_proven_count != 5:
        errors.append("Expected cumulative limited theorem count to remain five.")
    if proof_assistant_verification_count != 0:
        errors.append("Expected zero proof assistant verifications.")
    if formalization_complete_count != 0:
        errors.append("Expected zero formalization completion.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")
    if full_framework_formal_proof_count != 0:
        errors.append("Expected zero framework-level proofs.")
    if proof_gap_resolution_count != 0:
        errors.append("Expected zero proof gap resolutions.")
    if external_validation_count != 0:
        errors.append("Expected zero external validations.")
    if manuscript_submission_ready_count != 0:
        errors.append("Expected zero manuscript submission readiness.")

    warnings = [
        "This milestone authorizes a controlled bridge only; it does not execute the bridge.",
        "No attractor-class theorem is attempted.",
        "No attractor-class or constraint-region definition is completed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Attractor Class Bridge Authorization Plan v8.75",
        "",
        "## Purpose",
        "",
        "Authorize one controlled bridge from the audited finite R-path quotient structure toward an attractor-class candidate scaffold, while keeping bridge execution, new theorem proof, proof execution, proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, citation addition, and manuscript submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Bridge candidates",
        "",
        "| Candidate ID | Candidate name | Source structure | Target structure | Authorization status | Allowed next step | Blocked claim |",
        "|---|---|---|---|---|---|---|",
    ]

    for candidate in candidates:
        lines.append(
            f"| {candidate.candidate_id} | {candidate.candidate_name} | {candidate.source_structure} | {candidate.target_structure} | {candidate.authorization_status} | {candidate.allowed_next_step} | {candidate.blocked_claim} |"
        )

    lines.extend(
        [
            "",
            "## Selected bridge",
            "",
            "- Selected bridge candidate: ACB-001",
            "- Rationale: quotient classes are already supported by the finite R-path theorem stack and are the least inflated bridge target for later attractor-class work.",
            "- Execution status: not executed in this milestone.",
            "",
            "## Counts",
            "",
            f"- Attractor class bridge authorization plan count: {attractor_class_bridge_authorization_plan_count}",
            f"- Bridge candidate count: {bridge_candidate_count}",
            f"- Selected bridge candidate count: {selected_bridge_candidate_count}",
            f"- Authorized bridge candidate count: {authorized_bridge_candidate_count}",
            f"- Bridge execution count: {bridge_execution_count}",
            f"- Attractor class theorem attempt count: {attractor_class_theorem_attempt_count}",
            f"- Attractor class definition completion count: {attractor_class_definition_completion_count}",
            f"- Constraint region definition completion count: {constraint_region_definition_completion_count}",
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
            "## Carried v8.74 signals",
            "",
            f"- Carried path kernel theorem stack boundary audit count: {carried_stack_audit_count}",
            f"- Carried audited limited theorem count: {carried_audited_limited_theorem_count}",
            f"- Carried theorem stack count: {carried_theorem_stack_count}",
            f"- Carried theorem stack boundary audit row count: {carried_theorem_stack_boundary_audit_row_count}",
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
            "The v8.75 artifact authorizes one controlled bridge from the audited finite R-path quotient structure toward a later attractor-class candidate scaffold. It adds no bridge execution, no new theorem proof, no proof execution, no proof assistant verification, no completed formalization, no completed definitions, no framework-level proof, no proof gap resolution, no citation additions, no external validation, and no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "ACB-001 is intentionally narrow. It allows the next milestone to define an attractor-class candidate using quotient classes plus an explicit stabilization predicate, but it does not claim that attractor theory, causal mass, observer projection, or constraint-compatible regions are complete.",
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
            "The project has authorized one controlled bridge from the audited finite R-path quotient structure toward a later attractor-class candidate scaffold while keeping bridge execution, theorem proof, proof execution, proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, citation additions, external validation, and manuscript readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this bridge execution.",
            "- Do not call this a new theorem proof.",
            "- Do not call this proof assistant verification.",
            "- Do not call this completed formalization.",
            "- Do not call this completed definitions.",
            "- Do not call this framework-level proof.",
            "- Do not call this external validation.",
            "- Do not call this manuscript readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.75 attractor class bridge authorization plan.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.75 attractor class bridge authorization plan.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> AttractorClassBridgeAuthorizationPlanReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_stack_audit_count = 1 if _has_count(source_text, "Path kernel theorem stack boundary audit", "1") else 0
    carried_audited_limited_theorem_count = 5 if _has_count(source_text, "Audited limited theorem", "5") else 0
    carried_theorem_stack_count = 1 if _has_count(source_text, "Theorem stack", "1") else 0
    carried_theorem_stack_boundary_audit_row_count = 7 if _has_count(source_text, "Theorem stack boundary audit row", "7") else 0
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

    candidates = build_candidates()

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.74 path kernel theorem stack audit source artifact.")
    if carried_stack_audit_count != 1:
        errors.append("Expected carried theorem stack audit signal is absent.")
    if carried_audited_limited_theorem_count != 5:
        errors.append("Expected carried audited limited theorem count of five is absent.")
    if carried_theorem_stack_count != 1:
        errors.append("Expected carried theorem stack signal is absent.")
    if carried_theorem_stack_boundary_audit_row_count != 7:
        errors.append("Expected carried theorem stack audit row count is absent.")
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
    if len(candidates) != 3:
        errors.append("Expected three bridge candidates.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone authorizes a controlled bridge only; it does not execute the bridge.",
        "No attractor-class theorem is attempted.",
        "No attractor-class or constraint-region definition is completed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    return AttractorClassBridgeAuthorizationPlanReport(
        title="Attractor Class Bridge Authorization Plan v8.75",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        attractor_class_bridge_authorization_plan_count=1,
        bridge_candidate_count=len(candidates),
        selected_bridge_candidate_count=1,
        authorized_bridge_candidate_count=1,
        bridge_execution_count=0,
        attractor_class_theorem_attempt_count=0,
        attractor_class_definition_completion_count=0,
        constraint_region_definition_completion_count=0,
        carried_path_kernel_theorem_stack_boundary_audit_count=carried_stack_audit_count,
        carried_audited_limited_theorem_count=carried_audited_limited_theorem_count,
        carried_theorem_stack_count=carried_theorem_stack_count,
        carried_theorem_stack_boundary_audit_row_count=carried_theorem_stack_boundary_audit_row_count,
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
        new_theorem_proven_count=0,
        cumulative_limited_theorem_proven_count=carried_cumulative_limited_theorem_proven_count,
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
        boundary_phrase_count=59,
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
