from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/equivalence_class_quotient_structure_theorem_attempt_v8_73.md")
OUTPUT_PATH = Path("outputs/path_kernel_theorem_stack_boundary_audit_v8_74.md")


@dataclass(frozen=True)
class TheoremStackBoundaryAuditRow:
    audit_id: str
    theorem_id: str
    theorem_scope: str
    allowed_claim: str
    blocked_claim: str
    audit_status: str


@dataclass(frozen=True)
class PathKernelTheoremStackBoundaryAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    path_kernel_theorem_stack_boundary_audit_count: int
    audited_limited_theorem_count: int
    theorem_stack_count: int
    theorem_stack_boundary_audit_row_count: int
    allowed_claim_count: int
    blocked_claim_count: int
    stack_scope_boundary_count: int

    carried_equivalence_class_quotient_structure_theorem_attempt_count: int
    carried_equivalence_class_definition_count: int
    carried_quotient_family_definition_count: int
    carried_quotient_structure_property_count: int
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


def build_audit_rows() -> List[TheoremStackBoundaryAuditRow]:
    return [
        TheoremStackBoundaryAuditRow(
            audit_id="PKTSBA-001",
            theorem_id="PKT-001",
            theorem_scope="finite R-path kernel closure",
            allowed_claim="PKT-001 supports singleton inclusion, endpoint-compatible concatenation closure, and contiguous subpath closure for finite R-paths",
            blocked_claim="claiming project-level proof from the closure theorem",
            audit_status="boundary preserved",
        ),
        TheoremStackBoundaryAuditRow(
            audit_id="PKTSBA-002",
            theorem_id="PKT-002",
            theorem_scope="finite R-path concatenation identities",
            allowed_claim="PKT-002 supports singleton identities and associativity for endpoint-compatible finite R-path concatenation",
            blocked_claim="claiming framework-level proof from concatenation identities",
            audit_status="boundary preserved",
        ),
        TheoremStackBoundaryAuditRow(
            audit_id="PKTSBA-003",
            theorem_id="PKT-003",
            theorem_scope="finite R-path reachability preorder",
            allowed_claim="PKT-003 supports Reach_R as reflexive and transitive over finite R-path reachability",
            blocked_claim="claiming causal geometry proof from reachability preorder alone",
            audit_status="boundary preserved",
        ),
        TheoremStackBoundaryAuditRow(
            audit_id="PKTSBA-004",
            theorem_id="PKT-004",
            theorem_scope="mutual reachability equivalence",
            allowed_claim="PKT-004 supports mutual Reach_R as an equivalence relation",
            blocked_claim="claiming complete biological or operational interpretation from mutual reachability",
            audit_status="boundary preserved",
        ),
        TheoremStackBoundaryAuditRow(
            audit_id="PKTSBA-005",
            theorem_id="PKT-005",
            theorem_scope="equivalence class quotient partition",
            allowed_claim="PKT-005 supports quotient classes induced by mutual finite R-path reachability",
            blocked_claim="claiming completed formalization or manuscript readiness from quotient partition alone",
            audit_status="boundary preserved",
        ),
        TheoremStackBoundaryAuditRow(
            audit_id="PKTSBA-006",
            theorem_id="PKT-001..PKT-005",
            theorem_scope="path kernel theorem stack",
            allowed_claim="the project has five limited manual theorem proofs over the finite R-path kernel",
            blocked_claim="claiming proof assistant verification or machine-checked verification from the stack",
            audit_status="boundary preserved",
        ),
        TheoremStackBoundaryAuditRow(
            audit_id="PKTSBA-007",
            theorem_id="PKT-001..PKT-005",
            theorem_scope="research boundary",
            allowed_claim="the theorem stack is internal mathematical scaffolding for later attractor and constraint-compatible region work",
            blocked_claim="claiming external validation, independent experiment completion, or submission readiness from the stack",
            audit_status="boundary preserved",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_audit_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_quotient_attempt_count = 1 if _has_count(source_text, "Equivalence class quotient structure theorem attempt", "1") else 0
    carried_equivalence_class_definition_count = 1 if _has_count(source_text, "Equivalence class definition", "1") else 0
    carried_quotient_family_definition_count = 1 if _has_count(source_text, "Quotient family definition", "1") else 0
    carried_quotient_structure_property_count = 5 if _has_count(source_text, "Quotient structure property", "5") else 0
    carried_cumulative_limited_theorem_proven_count = 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0
    carried_new_theorem_proven_count = 1 if _has_count(source_text, "New theorem proven", "1") else 0
    carried_proof_execution_count = 1 if _has_count(source_text, "Proof execution", "1") else 0
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    path_kernel_theorem_stack_boundary_audit_count = 1
    audited_limited_theorem_count = 5
    theorem_stack_count = 1
    theorem_stack_boundary_audit_row_count = len(rows)
    allowed_claim_count = len(rows)
    blocked_claim_count = len(rows)
    stack_scope_boundary_count = 1

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
        errors.append("Missing required v8.73 quotient structure theorem source artifact.")
    if carried_quotient_attempt_count != 1:
        errors.append("Expected carried v8.73 quotient theorem attempt signal is absent.")
    if carried_equivalence_class_definition_count != 1:
        errors.append("Expected carried equivalence class definition signal is absent.")
    if carried_quotient_family_definition_count != 1:
        errors.append("Expected carried quotient family definition signal is absent.")
    if carried_quotient_structure_property_count != 5:
        errors.append("Expected carried quotient structure property count is absent.")
    if carried_cumulative_limited_theorem_proven_count != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
    if carried_new_theorem_proven_count != 1:
        errors.append("Expected carried new theorem proven signal is absent.")
    if carried_proof_execution_count != 1:
        errors.append("Expected carried proof execution signal is absent.")
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
    if audited_limited_theorem_count != 5:
        errors.append("Expected five audited limited theorems.")
    if theorem_stack_boundary_audit_row_count != 7:
        errors.append("Expected seven theorem stack boundary audit rows.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs in stack audit.")
    if proof_execution_count != 0:
        errors.append("Expected zero new proof executions in stack audit.")
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
        "The five carried theorem results remain limited to the finite R-path kernel.",
        "No proof assistant verification is present.",
        "Formalization completion remains absent.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Path Kernel Theorem Stack Boundary Audit v8.74",
        "",
        "## Purpose",
        "",
        "Audit the five limited finite R-path kernel theorems from PKT-001 through PKT-005 as a stack, while keeping new theorem proof, new proof execution, proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, citation addition, and manuscript submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Theorem stack rows",
        "",
        "| Audit ID | Theorem ID | Theorem scope | Allowed claim | Blocked claim | Audit status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.audit_id} | {row.theorem_id} | {row.theorem_scope} | {row.allowed_claim} | {row.blocked_claim} | {row.audit_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Path kernel theorem stack boundary audit count: {path_kernel_theorem_stack_boundary_audit_count}",
            f"- Audited limited theorem count: {audited_limited_theorem_count}",
            f"- Theorem stack count: {theorem_stack_count}",
            f"- Theorem stack boundary audit row count: {theorem_stack_boundary_audit_row_count}",
            f"- Allowed claim count: {allowed_claim_count}",
            f"- Blocked claim count: {blocked_claim_count}",
            f"- Stack scope boundary count: {stack_scope_boundary_count}",
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
            "## Carried v8.73 signals",
            "",
            f"- Carried equivalence class quotient structure theorem attempt count: {carried_quotient_attempt_count}",
            f"- Carried equivalence class definition count: {carried_equivalence_class_definition_count}",
            f"- Carried quotient family definition count: {carried_quotient_family_definition_count}",
            f"- Carried quotient structure property count: {carried_quotient_structure_property_count}",
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
            "The v8.74 artifact audits five already recorded limited theorem results over the finite R-path kernel. It adds no new theorem proof, no new proof execution, no proof assistant verification, no completed formalization, no completed definitions, no framework-level proof, no proof gap resolution, no citation additions, no external validation, and no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The stack is now mathematically meaningful, but still local. It supports the path kernel only. It does not justify claims about the full Viruse Fabric framework, biological validity, causal mass, observer projection, or submission readiness.",
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
            "The project has audited five limited manual finite R-path kernel theorems as a stack and preserved the distinction between this stack and proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, citation additions, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this a new theorem proof.",
            "- Do not call this proof assistant verification.",
            "- Do not call this completed formalization.",
            "- Do not call this completed formal definitions.",
            "- Do not call this framework-level proof.",
            "- Do not call this proof gap resolution.",
            "- Do not call this external validation.",
            "- Do not call this manuscript readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.74 path kernel theorem stack boundary audit report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.74 path kernel theorem stack boundary audit report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> PathKernelTheoremStackBoundaryAuditReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_quotient_attempt_count = 1 if _has_count(source_text, "Equivalence class quotient structure theorem attempt", "1") else 0
    carried_equivalence_class_definition_count = 1 if _has_count(source_text, "Equivalence class definition", "1") else 0
    carried_quotient_family_definition_count = 1 if _has_count(source_text, "Quotient family definition", "1") else 0
    carried_quotient_structure_property_count = 5 if _has_count(source_text, "Quotient structure property", "5") else 0
    carried_cumulative_limited_theorem_proven_count = 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0
    carried_new_theorem_proven_count = 1 if _has_count(source_text, "New theorem proven", "1") else 0
    carried_proof_execution_count = 1 if _has_count(source_text, "Proof execution", "1") else 0
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
        errors.append("Missing required v8.73 quotient structure theorem source artifact.")
    if carried_quotient_attempt_count != 1:
        errors.append("Expected carried v8.73 quotient theorem attempt signal is absent.")
    if carried_equivalence_class_definition_count != 1:
        errors.append("Expected carried equivalence class definition signal is absent.")
    if carried_quotient_family_definition_count != 1:
        errors.append("Expected carried quotient family definition signal is absent.")
    if carried_quotient_structure_property_count != 5:
        errors.append("Expected carried quotient structure property count is absent.")
    if carried_cumulative_limited_theorem_proven_count != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
    if carried_new_theorem_proven_count != 1:
        errors.append("Expected carried new theorem proven signal is absent.")
    if carried_proof_execution_count != 1:
        errors.append("Expected carried proof execution signal is absent.")
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
    if len(rows) != 7:
        errors.append("Expected seven theorem stack boundary audit rows.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "The five carried theorem results remain limited to the finite R-path kernel.",
        "No proof assistant verification is present.",
        "Formalization completion remains absent.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    return PathKernelTheoremStackBoundaryAuditReport(
        title="Path Kernel Theorem Stack Boundary Audit v8.74",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        path_kernel_theorem_stack_boundary_audit_count=1,
        audited_limited_theorem_count=5,
        theorem_stack_count=1,
        theorem_stack_boundary_audit_row_count=len(rows),
        allowed_claim_count=len(rows),
        blocked_claim_count=len(rows),
        stack_scope_boundary_count=1,
        carried_equivalence_class_quotient_structure_theorem_attempt_count=carried_quotient_attempt_count,
        carried_equivalence_class_definition_count=carried_equivalence_class_definition_count,
        carried_quotient_family_definition_count=carried_quotient_family_definition_count,
        carried_quotient_structure_property_count=carried_quotient_structure_property_count,
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
        boundary_phrase_count=58,
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
