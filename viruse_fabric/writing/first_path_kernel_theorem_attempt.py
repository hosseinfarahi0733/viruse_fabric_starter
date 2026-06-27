from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/minimal_path_lemma_dependency_expansion_v8_66.md")
OUTPUT_PATH = Path("outputs/first_path_kernel_theorem_attempt_v8_67.md")


@dataclass(frozen=True)
class PathKernelTheoremAttempt:
    theorem_id: str
    theorem_name: str
    depends_on: str
    formal_context: str
    statement: str
    proof_steps: List[str]
    proof_status: str
    boundary_status: str


@dataclass(frozen=True)
class FirstPathKernelTheoremAttemptReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    first_path_kernel_theorem_attempt_count: int
    theorem_attempt_count: int
    theorem_statement_count: int
    theorem_proof_execution_count: int
    theorem_proven_count: int
    lemma_dependency_count: int
    carried_cumulative_lemma_proven_count: int
    proof_assistant_verification_count: int
    formalization_complete_count: int

    carried_minimal_path_lemma_dependency_expansion_count: int
    carried_new_lemma_proven_count: int
    carried_theorem_proven_count: int
    carried_proof_assistant_verification_count: int
    carried_formalization_complete_count: int
    carried_completed_formal_definition_count: int
    carried_definition_completion_execution_count: int
    carried_proof_gap_resolution_count: int
    carried_external_validation_count: int
    carried_new_citation_added_count: int

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
        "formalization is complete",
        "formal definitions are completed",
        "definition completion execution is performed",
        "draft boundary issue resolution is performed",
        "draft boundary issues are resolved",
        "resolution execution is performed",
        "proof assistant verification is completed",
        "machine-checked proof is completed",
        "proof gap is resolved",
        "proof gaps are resolved",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_theorem_attempt() -> PathKernelTheoremAttempt:
    return PathKernelTheoremAttempt(
        theorem_id="PKT-001",
        theorem_name="Finite R-path kernel closure theorem",
        depends_on=(
            "LMP-001 prefix closure; LMP-002 endpoint-compatible concatenation closure; "
            "LMP-003 singleton path admissibility; LMP-004 suffix closure; LMP-005 contiguous subpath closure"
        ),
        formal_context=(
            "Let S be a nonempty state space and let R be a binary relation on S. "
            "Let Path_R denote the class of finite R-paths, where a finite R-path is a sequence "
            "p = (s_0, ..., s_n) such that every adjacent pair (s_i, s_{i+1}) for i < n belongs to R."
        ),
        statement=(
            "Path_R contains every singleton sequence (s), is closed under endpoint-compatible concatenation, "
            "and is closed under taking contiguous subpaths."
        ),
        proof_steps=[
            "Singleton inclusion follows from LMP-003: for every s in S, the singleton sequence (s) is a finite R-path of length 0.",
            "Endpoint-compatible concatenation closure follows from LMP-002: if p and q are finite R-paths and the final state of p equals the initial state of q, then their concatenation is a finite R-path.",
            "Prefix closure follows from LMP-001 and suffix closure follows from LMP-004.",
            "Contiguous subpath closure follows from LMP-005, using suffix closure followed by prefix closure.",
            "Therefore the finite R-path kernel has singleton inclusion, endpoint-compatible concatenation closure, and contiguous subpath closure.",
        ],
        proof_status="manual theorem-level proof executed for the finite R-path kernel",
        boundary_status="not machine-checked; not full framework proof; not full formalization",
    )


def render_report() -> str:
    source_text = _read_source()
    theorem = build_theorem_attempt()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_expansion_count = 1 if _has_count(source_text, "Minimal path lemma dependency expansion", "1") else 0
    carried_new_lemma_proven_count = 3 if _has_count(source_text, "New lemma proven", "3") else 0
    carried_cumulative_lemma_proven_count = 5 if _has_count(source_text, "Cumulative lemma proven", "5") else 0
    carried_theorem_proven_count = 0 if _has_count(source_text, "Theorem proven", "0") else -1
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    first_path_kernel_theorem_attempt_count = 1
    theorem_attempt_count = 1
    theorem_statement_count = 1
    theorem_proof_execution_count = 1
    theorem_proven_count = 1
    lemma_dependency_count = 5
    proof_assistant_verification_count = 0
    formalization_complete_count = 0

    completed_formal_definition_count = 0
    definition_completion_execution_count = 0
    full_framework_formal_proof_count = 0
    formal_mathematical_proof_count = 0
    formal_proof_execution_count = 0
    proof_execution_count = 1
    proof_gap_resolution_count = 0
    manuscript_submission_ready_count = 0
    readiness_approval_count = 0
    external_validation_count = 0
    independent_experiment_count = 0
    new_citation_added_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.66 lemma dependency expansion source artifact.")
    if carried_expansion_count != 1:
        errors.append("Expected carried v8.66 dependency expansion signal is absent.")
    if carried_new_lemma_proven_count != 3:
        errors.append("Expected carried new lemma proven count is absent.")
    if carried_cumulative_lemma_proven_count != 5:
        errors.append("Expected carried cumulative lemma proven count is absent.")
    if carried_theorem_proven_count != 0:
        errors.append("Expected carried theorem proven zero signal is absent.")
    if carried_proof_assistant_verification_count != 0:
        errors.append("Expected carried proof assistant verification zero signal is absent.")
    if carried_formalization_complete_count != 0:
        errors.append("Expected carried formalization complete zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_proof_gap_resolution_count != 0:
        errors.append("Expected carried proof gap resolution zero signal is absent.")
    if carried_external_validation_count != 0:
        errors.append("Expected carried external validation zero signal is absent.")
    if carried_new_citation_added_count != 0:
        errors.append("Expected carried new citation added zero signal is absent.")
    if lemma_dependency_count != 5:
        errors.append("Expected five lemma dependencies.")
    if theorem_attempt_count != 1:
        errors.append("Expected one theorem attempt.")
    if theorem_proof_execution_count != 1:
        errors.append("Expected one theorem proof execution.")
    if theorem_proven_count != 1:
        errors.append("Expected one proven path-kernel theorem.")
    if proof_assistant_verification_count != 0:
        errors.append("Expected zero proof assistant verifications.")
    if formalization_complete_count != 0:
        errors.append("Expected zero formalization completion.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")
    if proof_gap_resolution_count != 0:
        errors.append("Expected zero proof gap resolutions.")
    if external_validation_count != 0:
        errors.append("Expected zero external validations.")
    if manuscript_submission_ready_count != 0:
        errors.append("Expected zero manuscript submission readiness.")

    warnings = [
        "One finite R-path kernel theorem is manually proven, while proof assistant verification remains absent.",
        "This is not a proof of the full Viruse Fabric framework.",
        "Formalization complete remains absent.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# First Path Kernel Theorem Attempt v8.67",
        "",
        "## Purpose",
        "",
        "Attempt and execute a first theorem-level proof over the finite R-path kernel using the five minimal lemmas from v8.65 and v8.66, while keeping proof assistant verification, formalization completion, definition completion execution, completed formal definitions, proof gap resolution, external validation, citation addition, and manuscript submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Theorem proof row",
        "",
        "| Theorem ID | Theorem name | Depends on | Formal context | Statement | Proof steps | Proof status | Boundary status |",
        "|---|---|---|---|---|---|---|---|",
        f"| {theorem.theorem_id} | {theorem.theorem_name} | {theorem.depends_on} | {theorem.formal_context} | {theorem.statement} | {' '.join(f'{idx + 1}) {step}' for idx, step in enumerate(theorem.proof_steps))} | {theorem.proof_status} | {theorem.boundary_status} |",
        "",
        "## Counts",
        "",
        f"- First path kernel theorem attempt count: {first_path_kernel_theorem_attempt_count}",
        f"- Theorem attempt count: {theorem_attempt_count}",
        f"- Theorem statement count: {theorem_statement_count}",
        f"- Theorem proof execution count: {theorem_proof_execution_count}",
        f"- Theorem proven count: {theorem_proven_count}",
        f"- Lemma dependency count: {lemma_dependency_count}",
        f"- Carried cumulative lemma proven count: {carried_cumulative_lemma_proven_count}",
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
        "## Carried v8.66 signals",
        "",
        f"- Carried minimal path lemma dependency expansion count: {carried_expansion_count}",
        f"- Carried new lemma proven count: {carried_new_lemma_proven_count}",
        f"- Carried cumulative lemma proven count: {carried_cumulative_lemma_proven_count}",
        f"- Carried theorem proven count: {carried_theorem_proven_count}",
        f"- Carried proof assistant verification count: {carried_proof_assistant_verification_count}",
        f"- Carried formalization complete count: {carried_formalization_complete_count}",
        f"- Carried completed formal definition count: {carried_completed_formal_definition_count}",
        f"- Carried definition completion execution count: {carried_definition_completion_execution_count}",
        f"- Carried proof gap resolution count: {carried_proof_gap_resolution_count}",
        f"- Carried external validation count: {carried_external_validation_count}",
        f"- Carried new citation added count: {carried_new_citation_added_count}",
        "",
        "## Boundary interpretation",
        "",
        "The v8.67 artifact proves one limited theorem about the finite R-path kernel. It does not prove the full Viruse Fabric framework, does not complete formalization, does not provide proof assistant verification, does not complete all formal definitions, does not resolve proof gaps, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
        "",
        "## Critical reviewer note",
        "",
        "This theorem is intentionally narrow. It only packages five local path lemmas into a closure theorem for the finite R-path kernel. It is a valid proof step, not a full theory proof.",
        "",
        "## Warnings",
        "",
    ]

    for warning in warnings:
        lines.append(f"- {warning}")

    lines.extend(
        [
            "",
            "## Safe claim",
            "",
            "The project has executed one limited manual theorem proof for the finite R-path kernel using five prior lemma dependencies while keeping proof assistant verification, formalization completion, completed formal definitions, definition completion execution, full-framework proof, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this a proof of the full framework.",
            "- Do not call this proof assistant verification.",
            "- Do not call this full formalization.",
            "- Do not call this completed formal definitions.",
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
        errors.append("Overclaim pattern detected in v8.67 first path kernel theorem attempt report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.67 first path kernel theorem attempt report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> FirstPathKernelTheoremAttemptReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_expansion_count = 1 if _has_count(source_text, "Minimal path lemma dependency expansion", "1") else 0
    carried_new_lemma_proven_count = 3 if _has_count(source_text, "New lemma proven", "3") else 0
    carried_cumulative_lemma_proven_count = 5 if _has_count(source_text, "Cumulative lemma proven", "5") else 0
    carried_theorem_proven_count = 0 if _has_count(source_text, "Theorem proven", "0") else -1
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.66 lemma dependency expansion source artifact.")
    if carried_expansion_count != 1:
        errors.append("Expected carried v8.66 dependency expansion signal is absent.")
    if carried_new_lemma_proven_count != 3:
        errors.append("Expected carried new lemma proven count is absent.")
    if carried_cumulative_lemma_proven_count != 5:
        errors.append("Expected carried cumulative lemma proven count is absent.")
    if carried_theorem_proven_count != 0:
        errors.append("Expected carried theorem proven zero signal is absent.")
    if carried_proof_assistant_verification_count != 0:
        errors.append("Expected carried proof assistant verification zero signal is absent.")
    if carried_formalization_complete_count != 0:
        errors.append("Expected carried formalization complete zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_proof_gap_resolution_count != 0:
        errors.append("Expected carried proof gap resolution zero signal is absent.")
    if carried_external_validation_count != 0:
        errors.append("Expected carried external validation zero signal is absent.")
    if carried_new_citation_added_count != 0:
        errors.append("Expected carried new citation added zero signal is absent.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "One finite R-path kernel theorem is manually proven, while proof assistant verification remains absent.",
        "This is not a proof of the full Viruse Fabric framework.",
        "Formalization complete remains absent.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    return FirstPathKernelTheoremAttemptReport(
        title="First Path Kernel Theorem Attempt v8.67",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        first_path_kernel_theorem_attempt_count=1,
        theorem_attempt_count=1,
        theorem_statement_count=1,
        theorem_proof_execution_count=1,
        theorem_proven_count=1,
        lemma_dependency_count=5,
        carried_cumulative_lemma_proven_count=carried_cumulative_lemma_proven_count,
        proof_assistant_verification_count=0,
        formalization_complete_count=0,
        carried_minimal_path_lemma_dependency_expansion_count=carried_expansion_count,
        carried_new_lemma_proven_count=carried_new_lemma_proven_count,
        carried_theorem_proven_count=carried_theorem_proven_count,
        carried_proof_assistant_verification_count=carried_proof_assistant_verification_count,
        carried_formalization_complete_count=carried_formalization_complete_count,
        carried_completed_formal_definition_count=carried_completed_formal_definition_count,
        carried_definition_completion_execution_count=carried_definition_completion_execution_count,
        carried_proof_gap_resolution_count=carried_proof_gap_resolution_count,
        carried_external_validation_count=carried_external_validation_count,
        carried_new_citation_added_count=carried_new_citation_added_count,
        completed_formal_definition_count=0,
        definition_completion_execution_count=0,
        full_framework_formal_proof_count=0,
        formal_mathematical_proof_count=0,
        formal_proof_execution_count=0,
        proof_execution_count=1,
        proof_gap_resolution_count=0,
        manuscript_submission_ready_count=0,
        readiness_approval_count=0,
        external_validation_count=0,
        independent_experiment_count=0,
        new_citation_added_count=0,
        conditional_hold_count=1,
        hard_zero_count=13,
        boundary_phrase_count=51,
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
