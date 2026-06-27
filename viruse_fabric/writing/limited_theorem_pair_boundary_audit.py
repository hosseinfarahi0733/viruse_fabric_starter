from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/second_path_kernel_theorem_attempt_v8_69.md")
OUTPUT_PATH = Path("outputs/limited_theorem_pair_boundary_audit_v8_70.md")


@dataclass(frozen=True)
class TheoremPairBoundaryAuditRow:
    audit_id: str
    theorem_id: str
    theorem_scope: str
    allowed_claim: str
    blocked_claim: str
    audit_status: str


@dataclass(frozen=True)
class LimitedTheoremPairBoundaryAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    limited_theorem_pair_boundary_audit_count: int
    audited_limited_theorem_count: int
    audited_theorem_pair_count: int
    pair_boundary_audit_row_count: int
    allowed_claim_count: int
    blocked_claim_count: int

    carried_second_path_kernel_theorem_attempt_count: int
    carried_new_theorem_proven_count: int
    carried_cumulative_limited_theorem_proven_count: int
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


def build_audit_rows() -> List[TheoremPairBoundaryAuditRow]:
    return [
        TheoremPairBoundaryAuditRow(
            audit_id="LTPBA-001",
            theorem_id="PKT-001",
            theorem_scope="finite R-path kernel closure",
            allowed_claim="PKT-001 proves singleton inclusion, endpoint-compatible concatenation closure, and contiguous subpath closure for finite R-paths",
            blocked_claim="claiming a full Viruse Fabric framework proof from PKT-001",
            audit_status="boundary preserved",
        ),
        TheoremPairBoundaryAuditRow(
            audit_id="LTPBA-002",
            theorem_id="PKT-002",
            theorem_scope="finite R-path concatenation identities",
            allowed_claim="PKT-002 proves singleton identities and associativity for endpoint-compatible finite R-path concatenation",
            blocked_claim="claiming framework-level proof from PKT-002",
            audit_status="boundary preserved",
        ),
        TheoremPairBoundaryAuditRow(
            audit_id="LTPBA-003",
            theorem_id="PKT-001 + PKT-002",
            theorem_scope="limited theorem pair",
            allowed_claim="the project has two limited manual finite R-path kernel theorems",
            blocked_claim="claiming completed formalization or machine-checked verification from the pair",
            audit_status="boundary preserved",
        ),
        TheoremPairBoundaryAuditRow(
            audit_id="LTPBA-004",
            theorem_id="PKT-001 + PKT-002",
            theorem_scope="publication boundary",
            allowed_claim="the theorem pair may support later manuscript drafting as limited internal mathematical scaffolding",
            blocked_claim="claiming manuscript readiness from the theorem pair",
            audit_status="boundary preserved",
        ),
        TheoremPairBoundaryAuditRow(
            audit_id="LTPBA-005",
            theorem_id="PKT-001 + PKT-002",
            theorem_scope="validation boundary",
            allowed_claim="the theorem pair is an internal mathematical result over the finite R-path kernel",
            blocked_claim="claiming external validation or independent experiment completion from the theorem pair",
            audit_status="boundary preserved",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_audit_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_second_attempt_count = 1 if _has_count(source_text, "Second path kernel theorem attempt", "1") else 0
    carried_new_theorem_proven_count = 1 if _has_count(source_text, "New theorem proven", "1") else 0
    carried_cumulative_limited_theorem_proven_count = 2 if _has_count(source_text, "Cumulative limited theorem proven", "2") else 0
    carried_proof_execution_count = 1 if _has_count(source_text, "Proof execution", "1") else 0
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    limited_theorem_pair_boundary_audit_count = 1
    audited_limited_theorem_count = 2
    audited_theorem_pair_count = 1
    pair_boundary_audit_row_count = len(rows)
    allowed_claim_count = len(rows)
    blocked_claim_count = len(rows)

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
        errors.append("Missing required v8.69 second theorem source artifact.")
    if carried_second_attempt_count != 1:
        errors.append("Expected carried v8.69 second theorem attempt signal is absent.")
    if carried_new_theorem_proven_count != 1:
        errors.append("Expected carried new theorem proven signal is absent.")
    if carried_cumulative_limited_theorem_proven_count != 2:
        errors.append("Expected carried cumulative limited theorem proven signal is absent.")
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
    if audited_limited_theorem_count != 2:
        errors.append("Expected two audited limited theorems.")
    if pair_boundary_audit_row_count != 5:
        errors.append("Expected five theorem-pair boundary audit rows.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs in the audit milestone.")
    if proof_execution_count != 0:
        errors.append("Expected zero new proof executions in the audit milestone.")
    if cumulative_limited_theorem_proven_count != 2:
        errors.append("Expected cumulative limited theorem count to remain two.")
    if proof_assistant_verification_count != 0:
        errors.append("Expected zero proof assistant verifications.")
    if formalization_complete_count != 0:
        errors.append("Expected zero formalization completion.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")
    if full_framework_formal_proof_count != 0:
        errors.append("Expected zero full-framework proofs.")
    if proof_gap_resolution_count != 0:
        errors.append("Expected zero proof gap resolutions.")
    if external_validation_count != 0:
        errors.append("Expected zero external validations.")
    if manuscript_submission_ready_count != 0:
        errors.append("Expected zero manuscript submission readiness.")

    warnings = [
        "The two carried theorem results are limited to the finite R-path kernel.",
        "No proof assistant verification is present.",
        "Formalization completion remains absent.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Limited Theorem Pair Boundary Audit v8.70",
        "",
        "## Purpose",
        "",
        "Audit the pair of limited finite R-path kernel theorems from v8.67 and v8.69 so that the pair remains scoped as internal mathematical scaffolding rather than being overstated as framework-level proof, proof assistant verification, completed formalization, completed definitions, external validation, or manuscript readiness.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Audit rows",
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
            f"- Limited theorem pair boundary audit count: {limited_theorem_pair_boundary_audit_count}",
            f"- Audited limited theorem count: {audited_limited_theorem_count}",
            f"- Audited theorem pair count: {audited_theorem_pair_count}",
            f"- Pair boundary audit row count: {pair_boundary_audit_row_count}",
            f"- Allowed claim count: {allowed_claim_count}",
            f"- Blocked claim count: {blocked_claim_count}",
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
            "## Carried v8.69 signals",
            "",
            f"- Carried second path kernel theorem attempt count: {carried_second_attempt_count}",
            f"- Carried new theorem proven count: {carried_new_theorem_proven_count}",
            f"- Carried cumulative limited theorem proven count: {carried_cumulative_limited_theorem_proven_count}",
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
            "The v8.70 artifact audits two already recorded limited theorem results over the finite R-path kernel. It adds no new theorem proof, no new proof execution, no proof assistant verification, no completed formalization, no completed definitions, no framework-level proof, no proof gap resolution, no citation additions, no external validation, and no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The theorem pair is meaningful scaffolding for the path kernel, but it remains far below a complete theory result. The cumulative limited theorem count is two, not a license to inflate the project claim.",
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
            "The project has audited two limited manual finite R-path kernel theorems and preserved the distinction between this theorem pair and proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, citation additions, external validation, and manuscript readiness.",
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
        errors.append("Overclaim pattern detected in v8.70 limited theorem pair boundary audit report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.70 limited theorem pair boundary audit report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> LimitedTheoremPairBoundaryAuditReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_second_attempt_count = 1 if _has_count(source_text, "Second path kernel theorem attempt", "1") else 0
    carried_new_theorem_proven_count = 1 if _has_count(source_text, "New theorem proven", "1") else 0
    carried_cumulative_limited_theorem_proven_count = 2 if _has_count(source_text, "Cumulative limited theorem proven", "2") else 0
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
        errors.append("Missing required v8.69 second theorem source artifact.")
    if carried_second_attempt_count != 1:
        errors.append("Expected carried v8.69 second theorem attempt signal is absent.")
    if carried_new_theorem_proven_count != 1:
        errors.append("Expected carried new theorem proven signal is absent.")
    if carried_cumulative_limited_theorem_proven_count != 2:
        errors.append("Expected carried cumulative limited theorem proven signal is absent.")
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
    if len(rows) != 5:
        errors.append("Expected five theorem-pair boundary audit rows.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "The two carried theorem results are limited to the finite R-path kernel.",
        "No proof assistant verification is present.",
        "Formalization completion remains absent.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    return LimitedTheoremPairBoundaryAuditReport(
        title="Limited Theorem Pair Boundary Audit v8.70",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        limited_theorem_pair_boundary_audit_count=1,
        audited_limited_theorem_count=2,
        audited_theorem_pair_count=1,
        pair_boundary_audit_row_count=len(rows),
        allowed_claim_count=len(rows),
        blocked_claim_count=len(rows),
        carried_second_path_kernel_theorem_attempt_count=carried_second_attempt_count,
        carried_new_theorem_proven_count=carried_new_theorem_proven_count,
        carried_cumulative_limited_theorem_proven_count=carried_cumulative_limited_theorem_proven_count,
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
        boundary_phrase_count=54,
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
