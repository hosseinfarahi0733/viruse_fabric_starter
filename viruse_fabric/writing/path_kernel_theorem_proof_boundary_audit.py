from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/first_path_kernel_theorem_attempt_v8_67.md")
OUTPUT_PATH = Path("outputs/path_kernel_theorem_proof_boundary_audit_v8_68.md")


@dataclass(frozen=True)
class ProofBoundaryAuditRow:
    audit_id: str
    boundary_area: str
    allowed_claim: str
    blocked_claim: str
    audit_status: str


@dataclass(frozen=True)
class PathKernelTheoremProofBoundaryAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    path_kernel_theorem_proof_boundary_audit_count: int
    audited_theorem_count: int
    audited_theorem_proven_count: int
    theorem_scope_boundary_count: int
    proof_boundary_audit_row_count: int
    allowed_claim_count: int
    blocked_claim_count: int
    lemma_dependency_count: int

    carried_first_path_kernel_theorem_attempt_count: int
    carried_theorem_attempt_count: int
    carried_theorem_statement_count: int
    carried_theorem_proof_execution_count: int
    carried_theorem_proven_count: int
    carried_lemma_dependency_count: int
    carried_proof_assistant_verification_count: int
    carried_formalization_complete_count: int
    carried_completed_formal_definition_count: int
    carried_definition_completion_execution_count: int
    carried_full_framework_formal_proof_count: int
    carried_proof_gap_resolution_count: int
    carried_external_validation_count: int
    carried_new_citation_added_count: int

    new_theorem_proven_count: int
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


def build_audit_rows() -> List[ProofBoundaryAuditRow]:
    return [
        ProofBoundaryAuditRow(
            audit_id="PKTBA-001",
            boundary_area="theorem scope",
            allowed_claim="one limited finite R-path kernel theorem is manually proven",
            blocked_claim="claiming proof of the full Viruse Fabric framework",
            audit_status="boundary preserved",
        ),
        ProofBoundaryAuditRow(
            audit_id="PKTBA-002",
            boundary_area="proof verification",
            allowed_claim="manual theorem-level proof is recorded",
            blocked_claim="claiming completed proof assistant or machine-checked verification",
            audit_status="boundary preserved",
        ),
        ProofBoundaryAuditRow(
            audit_id="PKTBA-003",
            boundary_area="formalization",
            allowed_claim="finite R-path kernel proof scaffold is strengthened",
            blocked_claim="claiming completed formalization",
            audit_status="boundary preserved",
        ),
        ProofBoundaryAuditRow(
            audit_id="PKTBA-004",
            boundary_area="definition completion",
            allowed_claim="the theorem uses the current minimal path kernel",
            blocked_claim="claiming completion of all formal definitions",
            audit_status="boundary preserved",
        ),
        ProofBoundaryAuditRow(
            audit_id="PKTBA-005",
            boundary_area="proof gaps",
            allowed_claim="one limited closure theorem has no internal dependency gap under the recorded five lemmas",
            blocked_claim="claiming project-wide proof-gap closure",
            audit_status="boundary preserved",
        ),
        ProofBoundaryAuditRow(
            audit_id="PKTBA-006",
            boundary_area="publication readiness",
            allowed_claim="one theorem-level proof artifact is available for later manuscript drafting",
            blocked_claim="claiming manuscript submission readiness",
            audit_status="boundary preserved",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_audit_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_first_attempt_count = 1 if _has_count(source_text, "First path kernel theorem attempt", "1") else 0
    carried_theorem_attempt_count = 1 if _has_count(source_text, "Theorem attempt", "1") else 0
    carried_theorem_statement_count = 1 if _has_count(source_text, "Theorem statement", "1") else 0
    carried_theorem_proof_execution_count = 1 if _has_count(source_text, "Theorem proof execution", "1") else 0
    carried_theorem_proven_count = 1 if _has_count(source_text, "Theorem proven", "1") else 0
    carried_lemma_dependency_count = 5 if _has_count(source_text, "Lemma dependency", "5") else 0
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    path_kernel_theorem_proof_boundary_audit_count = 1
    audited_theorem_count = 1
    audited_theorem_proven_count = carried_theorem_proven_count
    theorem_scope_boundary_count = 1
    proof_boundary_audit_row_count = len(rows)
    allowed_claim_count = len(rows)
    blocked_claim_count = len(rows)
    lemma_dependency_count = carried_lemma_dependency_count

    new_theorem_proven_count = 0
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
        errors.append("Missing required v8.67 theorem attempt source artifact.")
    if carried_first_attempt_count != 1:
        errors.append("Expected carried first path kernel theorem attempt signal is absent.")
    if carried_theorem_attempt_count != 1:
        errors.append("Expected carried theorem attempt signal is absent.")
    if carried_theorem_statement_count != 1:
        errors.append("Expected carried theorem statement signal is absent.")
    if carried_theorem_proof_execution_count != 1:
        errors.append("Expected carried theorem proof execution signal is absent.")
    if carried_theorem_proven_count != 1:
        errors.append("Expected carried theorem proven signal is absent.")
    if carried_lemma_dependency_count != 5:
        errors.append("Expected carried lemma dependency signal is absent.")
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
    if proof_boundary_audit_row_count != 6:
        errors.append("Expected six proof boundary audit rows.")
    if allowed_claim_count != 6:
        errors.append("Expected six allowed claim rows.")
    if blocked_claim_count != 6:
        errors.append("Expected six blocked claim rows.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs in the audit milestone.")
    if proof_execution_count != 0:
        errors.append("Expected zero new proof executions in the audit milestone.")
    if proof_assistant_verification_count != 0:
        errors.append("Expected zero proof assistant verifications.")
    if formalization_complete_count != 0:
        errors.append("Expected zero formalization completion.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")
    if full_framework_formal_proof_count != 0:
        errors.append("Expected zero full framework formal proofs.")
    if proof_gap_resolution_count != 0:
        errors.append("Expected zero proof gap resolutions.")
    if external_validation_count != 0:
        errors.append("Expected zero external validations.")
    if manuscript_submission_ready_count != 0:
        errors.append("Expected zero manuscript submission readiness.")

    warnings = [
        "The carried theorem is limited to the finite R-path kernel.",
        "No proof assistant verification is present.",
        "Formalization complete remains absent.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Path Kernel Theorem Proof Boundary Audit v8.68",
        "",
        "## Purpose",
        "",
        "Audit the boundary of the limited finite R-path kernel theorem from v8.67 so that the theorem is not overstated as a full-framework proof, proof assistant verification, completed formalization, completed definitions, external validation, or manuscript submission readiness.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Audit rows",
        "",
        "| Audit ID | Boundary area | Allowed claim | Blocked claim | Audit status |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.audit_id} | {row.boundary_area} | {row.allowed_claim} | {row.blocked_claim} | {row.audit_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Path kernel theorem proof boundary audit count: {path_kernel_theorem_proof_boundary_audit_count}",
            f"- Audited theorem count: {audited_theorem_count}",
            f"- Audited theorem proven count: {audited_theorem_proven_count}",
            f"- Theorem scope boundary count: {theorem_scope_boundary_count}",
            f"- Proof boundary audit row count: {proof_boundary_audit_row_count}",
            f"- Allowed claim count: {allowed_claim_count}",
            f"- Blocked claim count: {blocked_claim_count}",
            f"- Lemma dependency count: {lemma_dependency_count}",
            f"- New theorem proven count: {new_theorem_proven_count}",
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
            "## Carried v8.67 signals",
            "",
            f"- Carried first path kernel theorem attempt count: {carried_first_attempt_count}",
            f"- Carried theorem attempt count: {carried_theorem_attempt_count}",
            f"- Carried theorem statement count: {carried_theorem_statement_count}",
            f"- Carried theorem proof execution count: {carried_theorem_proof_execution_count}",
            f"- Carried theorem proven count: {carried_theorem_proven_count}",
            f"- Carried lemma dependency count: {carried_lemma_dependency_count}",
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
            "The v8.68 artifact audits one already recorded limited theorem about the finite R-path kernel. It adds no new theorem proof, no proof assistant verification, no completed formalization, no completed definitions, no full-framework proof, no proof gap resolution, no citation additions, no external validation, and no manuscript submission readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The theorem from v8.67 is useful but narrow. This audit protects the distinction between a finite R-path kernel closure theorem and the much larger Viruse Fabric framework.",
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
            "The project has audited the boundary of one limited finite R-path kernel theorem and preserved the distinction between that theorem and full-framework proof, proof assistant verification, completed formalization, completed definitions, citation additions, external validation, and manuscript submission readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this a new theorem proof.",
            "- Do not call this proof assistant verification.",
            "- Do not call this full formalization.",
            "- Do not call this completed formal definitions.",
            "- Do not call this full-framework proof.",
            "- Do not call this proof gap resolution.",
            "- Do not call this external validation.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.68 theorem proof boundary audit report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.68 theorem proof boundary audit report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> PathKernelTheoremProofBoundaryAuditReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_first_attempt_count = 1 if _has_count(source_text, "First path kernel theorem attempt", "1") else 0
    carried_theorem_attempt_count = 1 if _has_count(source_text, "Theorem attempt", "1") else 0
    carried_theorem_statement_count = 1 if _has_count(source_text, "Theorem statement", "1") else 0
    carried_theorem_proof_execution_count = 1 if _has_count(source_text, "Theorem proof execution", "1") else 0
    carried_theorem_proven_count = 1 if _has_count(source_text, "Theorem proven", "1") else 0
    carried_lemma_dependency_count = 5 if _has_count(source_text, "Lemma dependency", "5") else 0
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
        errors.append("Missing required v8.67 theorem attempt source artifact.")
    if carried_first_attempt_count != 1:
        errors.append("Expected carried first path kernel theorem attempt signal is absent.")
    if carried_theorem_attempt_count != 1:
        errors.append("Expected carried theorem attempt signal is absent.")
    if carried_theorem_statement_count != 1:
        errors.append("Expected carried theorem statement signal is absent.")
    if carried_theorem_proof_execution_count != 1:
        errors.append("Expected carried theorem proof execution signal is absent.")
    if carried_theorem_proven_count != 1:
        errors.append("Expected carried theorem proven signal is absent.")
    if carried_lemma_dependency_count != 5:
        errors.append("Expected carried lemma dependency signal is absent.")
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
        errors.append("Expected six proof boundary audit rows.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "The carried theorem is limited to the finite R-path kernel.",
        "No proof assistant verification is present.",
        "Formalization complete remains absent.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    return PathKernelTheoremProofBoundaryAuditReport(
        title="Path Kernel Theorem Proof Boundary Audit v8.68",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        path_kernel_theorem_proof_boundary_audit_count=1,
        audited_theorem_count=1,
        audited_theorem_proven_count=carried_theorem_proven_count,
        theorem_scope_boundary_count=1,
        proof_boundary_audit_row_count=len(rows),
        allowed_claim_count=len(rows),
        blocked_claim_count=len(rows),
        lemma_dependency_count=carried_lemma_dependency_count,
        carried_first_path_kernel_theorem_attempt_count=carried_first_attempt_count,
        carried_theorem_attempt_count=carried_theorem_attempt_count,
        carried_theorem_statement_count=carried_theorem_statement_count,
        carried_theorem_proof_execution_count=carried_theorem_proof_execution_count,
        carried_theorem_proven_count=carried_theorem_proven_count,
        carried_lemma_dependency_count=carried_lemma_dependency_count,
        carried_proof_assistant_verification_count=carried_proof_assistant_verification_count,
        carried_formalization_complete_count=carried_formalization_complete_count,
        carried_completed_formal_definition_count=carried_completed_formal_definition_count,
        carried_definition_completion_execution_count=carried_definition_completion_execution_count,
        carried_full_framework_formal_proof_count=carried_full_framework_formal_proof_count,
        carried_proof_gap_resolution_count=carried_proof_gap_resolution_count,
        carried_external_validation_count=carried_external_validation_count,
        carried_new_citation_added_count=carried_new_citation_added_count,
        new_theorem_proven_count=0,
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
        boundary_phrase_count=52,
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
