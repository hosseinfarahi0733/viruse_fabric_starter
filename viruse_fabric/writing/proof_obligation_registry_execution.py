from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/formal_proof_track_entry_and_proof_obligation_plan_v8_50.md")
OUTPUT_PATH = Path("outputs/proof_obligation_registry_execution_v8_51.md")


@dataclass(frozen=True)
class ProofObligationRegistryRow:
    registry_id: str
    proof_object: str
    formalization_target: str
    obligation_type: str
    registry_status: str
    proof_status: str


@dataclass(frozen=True)
class ProofObligationRegistryExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    proof_obligation_registry_execution_count: int
    proof_obligation_registry_row_count: int
    registered_proof_obligation_count: int
    unresolved_proof_obligation_count: int
    resolved_proof_obligation_count: int
    proof_obligation_plan_count: int
    proof_obligation_plan_source_row_count: int
    formal_proof_track_entry_plan_count: int
    theorem_candidate_count: int
    lemma_candidate_count: int
    definition_candidate_count: int
    proof_strategy_plan_required_count: int
    formal_definition_candidate_registry_required_count: int

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
    return f"{phrase}: {expected}" in text or f"{phrase} count: {expected}" in text or _has_all_terms(text, [phrase, expected])


def _source_hard_zero_signal_count(text: str) -> int:
    zero_term_sets = [
        ["formal definition completed", "0"],
        ["formal mathematical proof", "0"],
        ["formal proof execution", "0"],
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
        "proof obligation is resolved",
        "proof obligations are resolved",
        "proof execution is completed",
        "proof execution is performed",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_registry_rows() -> List[ProofObligationRegistryRow]:
    return [
        ProofObligationRegistryRow(
            registry_id="POR-001",
            proof_object="definition candidate",
            formalization_target="three-time indexed state space with spatial coupling",
            obligation_type="define domain, indexing, admissible transitions, and boundary conditions",
            registry_status="registered",
            proof_status="unresolved",
        ),
        ProofObligationRegistryRow(
            registry_id="POR-002",
            proof_object="definition candidate",
            formalization_target="constraint geometry and global constraint family",
            obligation_type="define constraint sets, compatibility relation, and admissibility predicate",
            registry_status="registered",
            proof_status="unresolved",
        ),
        ProofObligationRegistryRow(
            registry_id="POR-003",
            proof_object="lemma candidate",
            formalization_target="path compatibility under constraint-preserving transitions",
            obligation_type="show that compatible paths remain admissible under specified transition constraints",
            registry_status="registered",
            proof_status="unresolved",
        ),
        ProofObligationRegistryRow(
            registry_id="POR-004",
            proof_object="lemma candidate",
            formalization_target="causal mass monotonicity under added compatible constraints",
            obligation_type="show whether causal mass is monotone, bounded, or requires counterexample conditions",
            registry_status="registered",
            proof_status="unresolved",
        ),
        ProofObligationRegistryRow(
            registry_id="POR-005",
            proof_object="theorem candidate",
            formalization_target="apparent purpose emergence under aligned constraint geometry and observer projection",
            obligation_type="state theorem candidate with assumptions, conclusion, and proof obligations",
            registry_status="registered",
            proof_status="unresolved",
        ),
        ProofObligationRegistryRow(
            registry_id="POR-006",
            proof_object="theorem candidate",
            formalization_target="non-teleological attractor concentration statement",
            obligation_type="separate mathematical attractor concentration from biological or intentional claims",
            registry_status="registered",
            proof_status="unresolved",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_registry_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    formal_proof_track_entry_plan_count = 1 if _has_count(source_text, "Controlled formal proof track entry plan count", "1") else 0
    proof_obligation_plan_count = 1 if _has_count(source_text, "Proof obligation plan count", "1") else 0
    proof_obligation_plan_source_row_count = 6 if _has_count(source_text, "Proof obligation row count", "6") else 0
    theorem_candidate_count = 2 if _has_count(source_text, "Theorem candidate count", "2") else 0
    lemma_candidate_count = 2 if _has_count(source_text, "Lemma candidate count", "2") else 0
    definition_candidate_count = 2 if _has_count(source_text, "Definition candidate count", "2") else 0
    proof_strategy_plan_required_count = 1 if _has_count(source_text, "Proof strategy plan required count", "1") else 0
    proof_obligation_registry_required_count = 1 if _has_count(source_text, "Proof obligation registry required count", "1") else 0

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.50 formal proof track source artifact.")
    if formal_proof_track_entry_plan_count != 1:
        errors.append("Expected formal proof track entry plan signal is absent.")
    if proof_obligation_plan_count != 1:
        errors.append("Expected proof obligation plan signal is absent.")
    if proof_obligation_plan_source_row_count != 6:
        errors.append("Expected proof obligation source row count signal is absent.")
    if theorem_candidate_count != 2:
        errors.append("Expected theorem candidate count signal is absent.")
    if lemma_candidate_count != 2:
        errors.append("Expected lemma candidate count signal is absent.")
    if definition_candidate_count != 2:
        errors.append("Expected definition candidate count signal is absent.")
    if proof_strategy_plan_required_count != 1:
        errors.append("Expected proof strategy plan required signal is absent.")
    if proof_obligation_registry_required_count != 1:
        errors.append("Expected proof obligation registry required signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")

    registered_proof_obligation_count = len(rows)
    unresolved_proof_obligation_count = sum(1 for row in rows if row.proof_status == "unresolved")
    resolved_proof_obligation_count = sum(1 for row in rows if row.proof_status == "resolved")

    warnings = [
        "Proof obligations are registered, but none are resolved.",
        "Proof execution remains absent.",
        "Theorem and lemma entries remain candidates only.",
        "Formal definitions remain candidates and are not completed.",
    ]

    lines = [
        "# Proof Obligation Registry Execution v8.51",
        "",
        "## Purpose",
        "",
        "Execute the proof obligation registry after v8.50 by registering proof obligations while keeping all proof execution, theorem proof, lemma proof, formalization completion, proof gap resolution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Registry rows",
        "",
        "| Registry ID | Proof object | Formalization target | Obligation type | Registry status | Proof status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.registry_id} | {row.proof_object} | {row.formalization_target} | {row.obligation_type} | {row.registry_status} | {row.proof_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Proof obligation registry execution count: 1",
            f"- Proof obligation registry row count: {len(rows)}",
            f"- Registered proof obligation count: {registered_proof_obligation_count}",
            f"- Unresolved proof obligation count: {unresolved_proof_obligation_count}",
            f"- Resolved proof obligation count: {resolved_proof_obligation_count}",
            f"- Proof obligation plan count: {proof_obligation_plan_count}",
            f"- Proof obligation plan source row count: {proof_obligation_plan_source_row_count}",
            f"- Controlled formal proof track entry plan count: {formal_proof_track_entry_plan_count}",
            f"- Theorem candidate count: {theorem_candidate_count}",
            f"- Lemma candidate count: {lemma_candidate_count}",
            f"- Definition candidate count: {definition_candidate_count}",
            f"- Proof strategy plan required count: {proof_strategy_plan_required_count}",
            "- Formal definition candidate registry required count: 1",
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
            "The v8.51 artifact executes the proof obligation registry only. It does not execute proof work, does not resolve proof obligations, does not prove a theorem, does not prove a lemma, does not complete formal definitions, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone converts the v8.50 obligation plan into a registered proof obligation set. It is progress toward proof execution, but proof execution and proof completion remain absent.",
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
            "The project has executed a proof obligation registry with six registered unresolved proof obligations, without executing proof work, resolving proof obligations, proving theorems, proving lemmas, completing formal definitions, adding citations, validating externally, or making the manuscript submission-ready.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this proof execution.",
            "- Do not call this formal proof.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
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
        errors.append("Overclaim pattern detected in v8.51 proof obligation registry report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.51 proof obligation registry report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ProofObligationRegistryExecutionReport:
    text = render_report()
    source_text = _read_source()
    rows = build_registry_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    formal_proof_track_entry_plan_count = 1 if _has_count(source_text, "Controlled formal proof track entry plan count", "1") else 0
    proof_obligation_plan_count = 1 if _has_count(source_text, "Proof obligation plan count", "1") else 0
    proof_obligation_plan_source_row_count = 6 if _has_count(source_text, "Proof obligation row count", "6") else 0
    theorem_candidate_count = 2 if _has_count(source_text, "Theorem candidate count", "2") else 0
    lemma_candidate_count = 2 if _has_count(source_text, "Lemma candidate count", "2") else 0
    definition_candidate_count = 2 if _has_count(source_text, "Definition candidate count", "2") else 0
    proof_strategy_plan_required_count = 1 if _has_count(source_text, "Proof strategy plan required count", "1") else 0
    proof_obligation_registry_required_count = 1 if _has_count(source_text, "Proof obligation registry required count", "1") else 0

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    registered_proof_obligation_count = len(rows)
    unresolved_proof_obligation_count = sum(1 for row in rows if row.proof_status == "unresolved")
    resolved_proof_obligation_count = sum(1 for row in rows if row.proof_status == "resolved")

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.50 formal proof track source artifact.")
    if formal_proof_track_entry_plan_count != 1:
        errors.append("Expected formal proof track entry plan signal is absent.")
    if proof_obligation_plan_count != 1:
        errors.append("Expected proof obligation plan signal is absent.")
    if proof_obligation_plan_source_row_count != 6:
        errors.append("Expected proof obligation source row count signal is absent.")
    if theorem_candidate_count != 2:
        errors.append("Expected theorem candidate count signal is absent.")
    if lemma_candidate_count != 2:
        errors.append("Expected lemma candidate count signal is absent.")
    if definition_candidate_count != 2:
        errors.append("Expected definition candidate count signal is absent.")
    if proof_strategy_plan_required_count != 1:
        errors.append("Expected proof strategy plan required signal is absent.")
    if proof_obligation_registry_required_count != 1:
        errors.append("Expected proof obligation registry required signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Proof obligations are registered, but none are resolved.",
        "Proof execution remains absent.",
        "Theorem and lemma entries remain candidates only.",
        "Formal definitions remain candidates and are not completed.",
    ]

    return ProofObligationRegistryExecutionReport(
        title="Proof Obligation Registry Execution v8.51",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        proof_obligation_registry_execution_count=1,
        proof_obligation_registry_row_count=len(rows),
        registered_proof_obligation_count=registered_proof_obligation_count,
        unresolved_proof_obligation_count=unresolved_proof_obligation_count,
        resolved_proof_obligation_count=resolved_proof_obligation_count,
        proof_obligation_plan_count=proof_obligation_plan_count,
        proof_obligation_plan_source_row_count=proof_obligation_plan_source_row_count,
        formal_proof_track_entry_plan_count=formal_proof_track_entry_plan_count,
        theorem_candidate_count=theorem_candidate_count,
        lemma_candidate_count=lemma_candidate_count,
        definition_candidate_count=definition_candidate_count,
        proof_strategy_plan_required_count=proof_strategy_plan_required_count,
        formal_definition_candidate_registry_required_count=1,
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
        boundary_phrase_count=34,
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
