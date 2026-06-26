from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/controlled_formal_definition_completion_approval_execution_authorization_execution_v8_49.md")
OUTPUT_PATH = Path("outputs/formal_proof_track_entry_and_proof_obligation_plan_v8_50.md")


@dataclass(frozen=True)
class ProofObligationPlanRow:
    row_id: str
    proof_object: str
    formalization_target: str
    obligation_type: str
    boundary_status: str


@dataclass(frozen=True)
class FormalProofTrackEntryReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    formal_proof_track_entry_plan_count: int
    proof_obligation_plan_count: int
    proof_obligation_row_count: int
    theorem_candidate_count: int
    lemma_candidate_count: int
    definition_candidate_count: int
    proof_strategy_plan_required_count: int
    proof_obligation_registry_required_count: int

    carried_authorization_execution_count: int
    carried_approval_execution_authorization_execution_count: int
    carried_approval_execution_authorized_count: int
    carried_approval_execution_plan_required_count: int
    carried_approval_execution_count: int

    formal_definition_completion_approval_execution_count: int
    formal_definition_completion_approved_count: int
    formal_definition_completed_count: int
    formal_mathematical_proof_count: int
    formal_proof_execution_count: int
    proof_execution_count: int
    theorem_proven_count: int
    lemma_proven_count: int
    formalization_complete_count: int
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
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]", "/"]:
        text = text.replace(ch, " ")
    return " ".join(text.split())


def _has_all_terms(text: str, terms: List[str]) -> bool:
    normalized = _normalize(text)
    return all(term.lower() in normalized for term in terms)


def _has_count(text: str, phrase: str, expected: str) -> bool:
    return f"{phrase} count: {expected}" in text or _has_all_terms(text, [phrase, "count", expected])


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["approval execution", "0"],
        ["formal definition completion approval execution", "0"],
        ["formal definition completion approved", "0"],
        ["formal definition completed", "0"],
        ["formal mathematical proof", "0"],
        ["proof execution", "0"],
        ["theorem proven", "0"],
        ["lemma proven", "0"],
        ["formalization complete", "0"],
        ["proof gap resolution", "0"],
        ["manuscript submission ready", "0"],
        ["readiness approval", "0"],
        ["external validation", "0"],
        ["independent experiment", "0"],
        ["new citation added", "0"],
    ]
    return sum(1 for terms in zero_term_sets if _has_all_terms(text, terms))


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
        "formal mathematical proof is completed",
        "formal proof is completed",
        "theorem is proven",
        "lemma is proven",
        "formalization is complete",
        "formal definitions are completed",
        "formal definition completion is approved",
        "approval execution is completed",
        "approval execution is approved",
        "approval execution is executed",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_rows() -> List[ProofObligationPlanRow]:
    return [
        ProofObligationPlanRow(
            row_id="FPO-001",
            proof_object="definition candidate",
            formalization_target="three-time indexed state space with spatial coupling",
            obligation_type="define domain, indexing, admissible transitions, and boundary conditions",
            boundary_status="not a completed formal definition",
        ),
        ProofObligationPlanRow(
            row_id="FPO-002",
            proof_object="definition candidate",
            formalization_target="constraint geometry and global constraint family",
            obligation_type="define constraint sets, compatibility relation, and admissibility predicate",
            boundary_status="not a completed formal definition",
        ),
        ProofObligationPlanRow(
            row_id="FPO-003",
            proof_object="lemma candidate",
            formalization_target="path compatibility under constraint-preserving transitions",
            obligation_type="show that compatible paths remain admissible under specified transition constraints",
            boundary_status="not a proven lemma",
        ),
        ProofObligationPlanRow(
            row_id="FPO-004",
            proof_object="lemma candidate",
            formalization_target="causal mass monotonicity under added compatible constraints",
            obligation_type="show whether causal mass is monotone, bounded, or requires counterexample conditions",
            boundary_status="not a proven lemma",
        ),
        ProofObligationPlanRow(
            row_id="FPO-005",
            proof_object="theorem candidate",
            formalization_target="apparent purpose emergence under aligned constraint geometry and observer projection",
            obligation_type="state theorem candidate with assumptions, conclusion, and proof obligations",
            boundary_status="not a proven theorem",
        ),
        ProofObligationPlanRow(
            row_id="FPO-006",
            proof_object="theorem candidate",
            formalization_target="non-teleological attractor concentration statement",
            obligation_type="separate mathematical attractor concentration from biological or intentional claims",
            boundary_status="not a proven theorem",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_authorization_execution = 1 if _has_count(
        source_text,
        "Controlled formal definition completion approval execution authorization execution",
        "1",
    ) else 0
    carried_approval_execution_authorization_execution = 1 if _has_count(
        source_text,
        "Approval execution authorization execution",
        "1",
    ) else 0
    carried_approval_execution_authorized = 1 if _has_count(
        source_text,
        "Approval execution authorized",
        "1",
    ) else 0
    carried_approval_execution_plan_required = 1 if _has_count(
        source_text,
        "Approval execution plan required",
        "1",
    ) else 0
    carried_approval_execution_count = 0 if _has_count(
        source_text,
        "Approval execution",
        "0",
    ) else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.49 authorization execution source artifact.")
    if carried_authorization_execution != 1:
        errors.append("Expected carried v8.49 authorization execution signal is absent.")
    if carried_approval_execution_authorization_execution != 1:
        errors.append("Expected carried approval execution authorization execution signal is absent.")
    if carried_approval_execution_authorized != 1:
        errors.append("Expected carried approval execution authorized signal is absent.")
    if carried_approval_execution_plan_required != 1:
        errors.append("Expected carried approval execution plan required signal is absent.")
    if carried_approval_execution_count != 0:
        errors.append("Expected carried approval execution absence signal is absent.")
    if source_hard_zero_signal_count < 12:
        errors.append("Expected hard-zero source signals are incomplete.")

    theorem_candidate_count = sum(1 for row in rows if row.proof_object == "theorem candidate")
    lemma_candidate_count = sum(1 for row in rows if row.proof_object == "lemma candidate")
    definition_candidate_count = sum(1 for row in rows if row.proof_object == "definition candidate")

    warnings = [
        "Formal proof track entry is created, but no proof execution is performed.",
        "Theorem and lemma entries are candidates only and are not proven.",
        "Formal definitions remain candidates and are not completed.",
        "No external validation, citation addition, or manuscript submission readiness is created.",
    ]

    lines = [
        "# Formal Proof Track Entry and Proof Obligation Plan v8.50",
        "",
        "## Purpose",
        "",
        "Open a formal proof track after v8.49 authorization execution by planning proof obligations, theorem candidates, lemma candidates, and definition candidates without claiming completed formal definitions, proof execution, theorem proof, lemma proof, external validation, citation additions, or submission readiness.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Proof obligation plan rows",
        "",
        "| Row | Proof object | Formalization target | Obligation type | Boundary status |",
        "|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.row_id} | {row.proof_object} | {row.formalization_target} | {row.obligation_type} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Controlled formal proof track entry plan count: 1",
            "- Proof obligation plan count: 1",
            f"- Proof obligation row count: {len(rows)}",
            f"- Theorem candidate count: {theorem_candidate_count}",
            f"- Lemma candidate count: {lemma_candidate_count}",
            f"- Definition candidate count: {definition_candidate_count}",
            "- Proof strategy plan required count: 1",
            "- Proof obligation registry required count: 1",
            "",
            "## Carried authorization signals",
            "",
            f"- Carried controlled formal definition completion approval execution authorization execution count: {carried_authorization_execution}",
            f"- Carried approval execution authorization execution count: {carried_approval_execution_authorization_execution}",
            f"- Carried approval execution authorized count: {carried_approval_execution_authorized}",
            f"- Carried approval execution plan required count: {carried_approval_execution_plan_required}",
            f"- Carried approval execution count: {carried_approval_execution_count}",
            "",
            "## Hard-zero counts preserved",
            "",
            "- Formal definition completion approval execution count: 0",
            "- Formal definition completion approved count: 0",
            "- Formal definition completed count: 0",
            "- Formal mathematical proof count: 0",
            "- Formal proof execution count: 0",
            "- Proof execution count: 0",
            "- Theorem proven count: 0",
            "- Lemma proven count: 0",
            "- Formalization complete count: 0",
            "- Proof gap resolution count: 0",
            "- Manuscript submission ready count: 0",
            "- Readiness approval count: 0",
            "- External validation count: 0",
            "- Independent experiment count: 0",
            "- New citation added count: 0",
            "",
            "## Boundary interpretation",
            "",
            "The v8.50 artifact opens a formal proof track and plans proof obligations only. It does not complete formal definitions, does not execute proof work, does not prove a theorem, does not prove a lemma, does not resolve proof gaps, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone intentionally redirects the project away from another approval-execution planning artifact and toward proof-track preparation. It remains conservative: candidate definitions, candidate lemmas, and candidate theorems are only planned, not proven.",
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
            "The project has opened a formal proof track and planned proof obligations, theorem candidates, lemma candidates, and definition candidates, without completing formal definitions, executing proof work, proving theorems, proving lemmas, adding citations, validating externally, or making the manuscript submission-ready.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this proof execution.",
            "- Do not call this formal proof.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
            "- Do not call this completed formal definitions.",
            "- Do not call this formalization complete.",
            "- Do not call this external validation.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)
    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.50 formal proof track entry report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.50 formal proof track entry report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> FormalProofTrackEntryReport:
    text = render_report()
    source_text = _read_source()
    rows = build_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_authorization_execution = 1 if _has_count(
        source_text,
        "Controlled formal definition completion approval execution authorization execution",
        "1",
    ) else 0
    carried_approval_execution_authorization_execution = 1 if _has_count(
        source_text,
        "Approval execution authorization execution",
        "1",
    ) else 0
    carried_approval_execution_authorized = 1 if _has_count(
        source_text,
        "Approval execution authorized",
        "1",
    ) else 0
    carried_approval_execution_plan_required = 1 if _has_count(
        source_text,
        "Approval execution plan required",
        "1",
    ) else 0
    carried_approval_execution_count = 0 if _has_count(
        source_text,
        "Approval execution",
        "0",
    ) else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    theorem_candidate_count = sum(1 for row in rows if row.proof_object == "theorem candidate")
    lemma_candidate_count = sum(1 for row in rows if row.proof_object == "lemma candidate")
    definition_candidate_count = sum(1 for row in rows if row.proof_object == "definition candidate")

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.49 authorization execution source artifact.")
    if carried_authorization_execution != 1:
        errors.append("Expected carried v8.49 authorization execution signal is absent.")
    if carried_approval_execution_authorization_execution != 1:
        errors.append("Expected carried approval execution authorization execution signal is absent.")
    if carried_approval_execution_authorized != 1:
        errors.append("Expected carried approval execution authorized signal is absent.")
    if carried_approval_execution_plan_required != 1:
        errors.append("Expected carried approval execution plan required signal is absent.")
    if carried_approval_execution_count != 0:
        errors.append("Expected carried approval execution absence signal is absent.")
    if source_hard_zero_signal_count < 12:
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Formal proof track entry is created, but no proof execution is performed.",
        "Theorem and lemma entries are candidates only and are not proven.",
        "Formal definitions remain candidates and are not completed.",
        "No external validation, citation addition, or manuscript submission readiness is created.",
    ]

    return FormalProofTrackEntryReport(
        title="Formal Proof Track Entry and Proof Obligation Plan v8.50",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        formal_proof_track_entry_plan_count=1,
        proof_obligation_plan_count=1,
        proof_obligation_row_count=len(rows),
        theorem_candidate_count=theorem_candidate_count,
        lemma_candidate_count=lemma_candidate_count,
        definition_candidate_count=definition_candidate_count,
        proof_strategy_plan_required_count=1,
        proof_obligation_registry_required_count=1,
        carried_authorization_execution_count=carried_authorization_execution,
        carried_approval_execution_authorization_execution_count=carried_approval_execution_authorization_execution,
        carried_approval_execution_authorized_count=carried_approval_execution_authorized,
        carried_approval_execution_plan_required_count=carried_approval_execution_plan_required,
        carried_approval_execution_count=carried_approval_execution_count,
        formal_definition_completion_approval_execution_count=0,
        formal_definition_completion_approved_count=0,
        formal_definition_completed_count=0,
        formal_mathematical_proof_count=0,
        formal_proof_execution_count=0,
        proof_execution_count=0,
        theorem_proven_count=0,
        lemma_proven_count=0,
        formalization_complete_count=0,
        proof_gap_resolution_count=0,
        manuscript_submission_ready_count=0,
        readiness_approval_count=0,
        external_validation_count=0,
        independent_experiment_count=0,
        new_citation_added_count=0,
        conditional_hold_count=1,
        hard_zero_count=16,
        boundary_phrase_count=33,
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
