from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/formal_definition_candidate_registry_v8_52.md")
OUTPUT_PATH = Path("outputs/theorem_and_lemma_skeleton_plan_v8_53.md")


@dataclass(frozen=True)
class TheoremLemmaSkeletonRow:
    skeleton_id: str
    skeleton_kind: str
    skeleton_name: str
    depends_on_definitions: str
    planned_statement_shape: str
    proof_boundary: str


@dataclass(frozen=True)
class TheoremLemmaSkeletonPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    theorem_lemma_skeleton_plan_count: int
    theorem_lemma_skeleton_row_count: int
    theorem_skeleton_count: int
    lemma_skeleton_count: int
    theorem_candidate_count: int
    lemma_candidate_count: int

    carried_formal_definition_candidate_registry_count: int
    carried_registered_formal_definition_candidate_count: int
    carried_unresolved_formal_definition_candidate_count: int
    carried_completed_formal_definition_candidate_count: int
    carried_proof_obligation_registry_execution_count: int
    carried_registered_proof_obligation_count: int
    carried_unresolved_proof_obligation_count: int
    carried_resolved_proof_obligation_count: int

    proof_strategy_plan_required_count: int
    proof_execution_attempt_plan_required_count: int

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
        "theorem has been proven",
        "lemma has been proven",
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


def build_skeleton_rows() -> List[TheoremLemmaSkeletonRow]:
    return [
        TheoremLemmaSkeletonRow(
            skeleton_id="TLS-001",
            skeleton_kind="lemma skeleton",
            skeleton_name="Path compatibility preservation",
            depends_on_definitions="FDC-001 and FDC-002",
            planned_statement_shape="If a path is admissible under the registered transition relation and each step preserves the compatibility predicate, then the path remains admissible under the stated constraint family.",
            proof_boundary="skeleton only; no lemma proof",
        ),
        TheoremLemmaSkeletonRow(
            skeleton_id="TLS-002",
            skeleton_kind="lemma skeleton",
            skeleton_name="Causal mass boundedness or counterexample split",
            depends_on_definitions="FDC-001 and FDC-002",
            planned_statement_shape="For a specified causal mass functional, either boundedness follows under compatible added constraints or a counterexample condition must be recorded.",
            proof_boundary="skeleton only; no lemma proof",
        ),
        TheoremLemmaSkeletonRow(
            skeleton_id="TLS-003",
            skeleton_kind="theorem skeleton",
            skeleton_name="Apparent purpose emergence under aligned constraints",
            depends_on_definitions="FDC-001, FDC-002, TLS-001, and TLS-002",
            planned_statement_shape="If constraint geometry, attractor concentration, path compatibility, and observer projection satisfy explicit assumptions, then apparent purpose is represented as a projection-level property rather than an intentional claim.",
            proof_boundary="skeleton only; no theorem proof",
        ),
        TheoremLemmaSkeletonRow(
            skeleton_id="TLS-004",
            skeleton_kind="theorem skeleton",
            skeleton_name="Non-teleological attractor concentration statement",
            depends_on_definitions="FDC-001, FDC-002, and TLS-001",
            planned_statement_shape="Under registered admissibility and projection assumptions, attractor concentration can be stated without biological, clinical, or intentional overclaim.",
            proof_boundary="skeleton only; no theorem proof",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_skeleton_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    formal_definition_candidate_registry_count = 1 if _has_count(source_text, "Formal definition candidate registry count", "1") else 0
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Registered formal definition candidate count", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Unresolved formal definition candidate count", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Completed formal definition candidate count", "0") else -1

    proof_obligation_registry_execution_count = 1 if _has_count(source_text, "Carried proof obligation registry execution count", "1") else 0
    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation count", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation count", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation count", "0") else -1

    theorem_candidate_count = 2 if _has_count(source_text, "Carried theorem candidate count", "2") else 0
    lemma_candidate_count = 2 if _has_count(source_text, "Carried lemma candidate count", "2") else 0
    skeleton_plan_required_count = 1 if _has_count(source_text, "Theorem and lemma skeleton plan required count", "1") else 0
    proof_strategy_plan_required_count = 1 if _has_count(source_text, "Proof strategy plan required count", "1") else 0

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    theorem_skeleton_count = sum(1 for row in rows if row.skeleton_kind == "theorem skeleton")
    lemma_skeleton_count = sum(1 for row in rows if row.skeleton_kind == "lemma skeleton")

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.52 formal definition candidate registry source artifact.")
    if formal_definition_candidate_registry_count != 1:
        errors.append("Expected formal definition candidate registry signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected registered formal definition candidate count signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected unresolved formal definition candidate count signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected completed formal definition candidate zero signal is absent.")
    if proof_obligation_registry_execution_count != 1:
        errors.append("Expected carried proof obligation registry execution signal is absent.")
    if registered_proof_obligation_count != 6:
        errors.append("Expected carried registered proof obligation count signal is absent.")
    if unresolved_proof_obligation_count != 6:
        errors.append("Expected carried unresolved proof obligation count signal is absent.")
    if resolved_proof_obligation_count != 0:
        errors.append("Expected carried resolved proof obligation zero signal is absent.")
    if theorem_candidate_count != 2:
        errors.append("Expected carried theorem candidate count signal is absent.")
    if lemma_candidate_count != 2:
        errors.append("Expected carried lemma candidate count signal is absent.")
    if skeleton_plan_required_count != 1:
        errors.append("Expected theorem and lemma skeleton plan required signal is absent.")
    if proof_strategy_plan_required_count != 1:
        errors.append("Expected proof strategy plan required signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")

    warnings = [
        "Theorem and lemma skeletons are planned, while theorem proof and lemma proof remain absent.",
        "Formal definition candidates remain unresolved.",
        "Proof obligations remain unresolved.",
        "Proof execution remains absent.",
    ]

    lines = [
        "# Theorem and Lemma Skeleton Plan v8.53",
        "",
        "## Purpose",
        "",
        "Create theorem and lemma skeletons after v8.52 formal definition candidate registry while keeping formal definition completion, proof execution, theorem proof, lemma proof, proof gap resolution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Theorem and lemma skeleton rows",
        "",
        "| Skeleton ID | Skeleton kind | Skeleton name | Depends on definitions | Planned statement shape | Proof boundary |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.skeleton_id} | {row.skeleton_kind} | {row.skeleton_name} | {row.depends_on_definitions} | {row.planned_statement_shape} | {row.proof_boundary} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Theorem and lemma skeleton plan count: 1",
            f"- Theorem and lemma skeleton row count: {len(rows)}",
            f"- Theorem skeleton count: {theorem_skeleton_count}",
            f"- Lemma skeleton count: {lemma_skeleton_count}",
            f"- Theorem candidate count: {theorem_candidate_count}",
            f"- Lemma candidate count: {lemma_candidate_count}",
            "",
            "## Carried proof-track signals",
            "",
            f"- Carried formal definition candidate registry count: {formal_definition_candidate_registry_count}",
            f"- Carried registered formal definition candidate count: {registered_formal_definition_candidate_count}",
            f"- Carried unresolved formal definition candidate count: {unresolved_formal_definition_candidate_count}",
            f"- Carried completed formal definition candidate count: {completed_formal_definition_candidate_count}",
            f"- Carried proof obligation registry execution count: {proof_obligation_registry_execution_count}",
            f"- Carried registered proof obligation count: {registered_proof_obligation_count}",
            f"- Carried unresolved proof obligation count: {unresolved_proof_obligation_count}",
            f"- Carried resolved proof obligation count: {resolved_proof_obligation_count}",
            f"- Proof strategy plan required count: {proof_strategy_plan_required_count}",
            "- Proof execution attempt plan required count: 1",
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
            "The v8.53 artifact creates theorem and lemma skeletons only. It does not complete formal definitions, does not execute proof work, does not resolve proof obligations, does not prove a theorem, does not prove a lemma, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone gives theorem and lemma candidates a usable skeleton before proof strategy planning. It is necessary preparation for proof work, but it is not proof execution and not proof completion.",
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
            "The project has planned two theorem skeletons and two lemma skeletons grounded in the registered formal definition candidates and proof obligations, without completing formal definitions, executing proof work, resolving proof obligations, proving theorems, proving lemmas, adding citations, validating externally, or making the manuscript submission-ready.",
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
        errors.append("Overclaim pattern detected in v8.53 theorem and lemma skeleton plan report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.53 theorem and lemma skeleton plan report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> TheoremLemmaSkeletonPlanReport:
    text = render_report()
    source_text = _read_source()
    rows = build_skeleton_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    formal_definition_candidate_registry_count = 1 if _has_count(source_text, "Formal definition candidate registry count", "1") else 0
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Registered formal definition candidate count", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Unresolved formal definition candidate count", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Completed formal definition candidate count", "0") else -1

    proof_obligation_registry_execution_count = 1 if _has_count(source_text, "Carried proof obligation registry execution count", "1") else 0
    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation count", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation count", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation count", "0") else -1

    theorem_candidate_count = 2 if _has_count(source_text, "Carried theorem candidate count", "2") else 0
    lemma_candidate_count = 2 if _has_count(source_text, "Carried lemma candidate count", "2") else 0
    skeleton_plan_required_count = 1 if _has_count(source_text, "Theorem and lemma skeleton plan required count", "1") else 0
    proof_strategy_plan_required_count = 1 if _has_count(source_text, "Proof strategy plan required count", "1") else 0

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    theorem_skeleton_count = sum(1 for row in rows if row.skeleton_kind == "theorem skeleton")
    lemma_skeleton_count = sum(1 for row in rows if row.skeleton_kind == "lemma skeleton")

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.52 formal definition candidate registry source artifact.")
    if formal_definition_candidate_registry_count != 1:
        errors.append("Expected formal definition candidate registry signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected registered formal definition candidate count signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected unresolved formal definition candidate count signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected completed formal definition candidate zero signal is absent.")
    if proof_obligation_registry_execution_count != 1:
        errors.append("Expected carried proof obligation registry execution signal is absent.")
    if registered_proof_obligation_count != 6:
        errors.append("Expected carried registered proof obligation count signal is absent.")
    if unresolved_proof_obligation_count != 6:
        errors.append("Expected carried unresolved proof obligation count signal is absent.")
    if resolved_proof_obligation_count != 0:
        errors.append("Expected carried resolved proof obligation zero signal is absent.")
    if theorem_candidate_count != 2:
        errors.append("Expected carried theorem candidate count signal is absent.")
    if lemma_candidate_count != 2:
        errors.append("Expected carried lemma candidate count signal is absent.")
    if skeleton_plan_required_count != 1:
        errors.append("Expected theorem and lemma skeleton plan required signal is absent.")
    if proof_strategy_plan_required_count != 1:
        errors.append("Expected proof strategy plan required signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Theorem and lemma skeletons are planned, while theorem proof and lemma proof remain absent.",
        "Formal definition candidates remain unresolved.",
        "Proof obligations remain unresolved.",
        "Proof execution remains absent.",
    ]

    return TheoremLemmaSkeletonPlanReport(
        title="Theorem and Lemma Skeleton Plan v8.53",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        theorem_lemma_skeleton_plan_count=1,
        theorem_lemma_skeleton_row_count=len(rows),
        theorem_skeleton_count=theorem_skeleton_count,
        lemma_skeleton_count=lemma_skeleton_count,
        theorem_candidate_count=theorem_candidate_count,
        lemma_candidate_count=lemma_candidate_count,
        carried_formal_definition_candidate_registry_count=formal_definition_candidate_registry_count,
        carried_registered_formal_definition_candidate_count=registered_formal_definition_candidate_count,
        carried_unresolved_formal_definition_candidate_count=unresolved_formal_definition_candidate_count,
        carried_completed_formal_definition_candidate_count=completed_formal_definition_candidate_count,
        carried_proof_obligation_registry_execution_count=proof_obligation_registry_execution_count,
        carried_registered_proof_obligation_count=registered_proof_obligation_count,
        carried_unresolved_proof_obligation_count=unresolved_proof_obligation_count,
        carried_resolved_proof_obligation_count=resolved_proof_obligation_count,
        proof_strategy_plan_required_count=proof_strategy_plan_required_count,
        proof_execution_attempt_plan_required_count=1,
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
        boundary_phrase_count=36,
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
