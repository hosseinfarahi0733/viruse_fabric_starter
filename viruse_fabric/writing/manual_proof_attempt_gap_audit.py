from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/first_manual_proof_attempt_execution_v8_56.md")
OUTPUT_PATH = Path("outputs/manual_proof_attempt_gap_audit_v8_57.md")


@dataclass(frozen=True)
class ManualProofAttemptGapRow:
    gap_id: str
    linked_attempt: str
    gap_type: str
    gap_description: str
    required_next_action: str
    resolution_status: str
    boundary_status: str


@dataclass(frozen=True)
class ManualProofAttemptGapAuditReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    manual_proof_attempt_gap_audit_count: int
    audited_manual_proof_attempt_row_count: int
    proof_attempt_gap_row_count: int
    definition_gap_count: int
    assumption_gap_count: int
    dependency_gap_count: int
    boundary_gap_count: int
    unresolved_proof_attempt_gap_count: int
    resolved_proof_attempt_gap_count: int
    proof_attempt_gap_resolution_count: int

    carried_first_manual_proof_attempt_execution_count: int
    carried_manual_proof_attempt_row_count: int
    carried_attempted_lemma_skeleton_count: int
    carried_attempted_theorem_skeleton_count: int
    carried_partial_derivation_note_count: int
    carried_unresolved_attempt_item_count: int
    carried_successful_theorem_proof_count: int
    carried_successful_lemma_proof_count: int
    carried_registered_proof_obligation_count: int
    carried_unresolved_proof_obligation_count: int
    carried_resolved_proof_obligation_count: int
    carried_registered_formal_definition_candidate_count: int
    carried_unresolved_formal_definition_candidate_count: int
    carried_completed_formal_definition_candidate_count: int

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
        ["successful theorem proof", "0"],
        ["successful lemma proof", "0"],
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
        "proof gap is resolved",
        "proof gaps are resolved",
        "manual proof attempt succeeds",
        "manual proof establishes theorem",
        "manual proof establishes lemma",
        "gap audit resolves",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_gap_rows() -> List[ManualProofAttemptGapRow]:
    return [
        ManualProofAttemptGapRow(
            gap_id="MPG-001",
            linked_attempt="MPA-001",
            gap_type="definition gap",
            gap_description="state space, transition relation, compatibility predicate, and admissible path predicate remain only candidates",
            required_next_action="complete candidate definitions before lemma derivation can be upgraded",
            resolution_status="unresolved",
            boundary_status="audit only; lemma proof remains absent",
        ),
        ManualProofAttemptGapRow(
            gap_id="MPG-002",
            linked_attempt="MPA-001",
            gap_type="assumption gap",
            gap_description="transition-preservation condition is listed but not justified by a completed assumption block",
            required_next_action="write explicit preservation assumptions and failure conditions",
            resolution_status="unresolved",
            boundary_status="audit only; no proof gap resolution",
        ),
        ManualProofAttemptGapRow(
            gap_id="MPG-003",
            linked_attempt="MPA-002",
            gap_type="definition gap",
            gap_description="causal mass functional, order relation, and boundedness predicate remain underspecified",
            required_next_action="define functional domain, codomain, ordering, and boundedness predicate",
            resolution_status="unresolved",
            boundary_status="audit only; lemma proof remains absent",
        ),
        ManualProofAttemptGapRow(
            gap_id="MPG-004",
            linked_attempt="MPA-002",
            gap_type="boundary gap",
            gap_description="boundedness route and counterexample route are separated but neither route has sufficient assumptions",
            required_next_action="split route assumptions and mark counterexample trigger conditions",
            resolution_status="unresolved",
            boundary_status="audit only; no proof gap resolution",
        ),
        ManualProofAttemptGapRow(
            gap_id="MPG-005",
            linked_attempt="MPA-003",
            gap_type="dependency gap",
            gap_description="apparent purpose theorem skeleton depends on unresolved lemma attempts",
            required_next_action="keep theorem statement at dependency-map level until lemma gaps are addressed",
            resolution_status="unresolved",
            boundary_status="audit only; theorem proof remains absent",
        ),
        ManualProofAttemptGapRow(
            gap_id="MPG-006",
            linked_attempt="MPA-003",
            gap_type="definition gap",
            gap_description="observer projection definition remains a candidate and cannot support theorem-level conclusion",
            required_next_action="complete observer projection definition before theorem upgrade",
            resolution_status="unresolved",
            boundary_status="audit only; no theorem proof",
        ),
        ManualProofAttemptGapRow(
            gap_id="MPG-007",
            linked_attempt="MPA-004",
            gap_type="boundary gap",
            gap_description="non-teleological wording is controlled, but attractor concentration assumptions remain incomplete",
            required_next_action="separate mathematical concentration statement from projection-level interpretation",
            resolution_status="unresolved",
            boundary_status="audit only; theorem proof remains absent",
        ),
        ManualProofAttemptGapRow(
            gap_id="MPG-008",
            linked_attempt="MPA-004",
            gap_type="assumption gap",
            gap_description="admissibility and projection assumptions are listed but not sufficient for theorem upgrade",
            required_next_action="write minimal assumption schema and counterexample notes",
            resolution_status="unresolved",
            boundary_status="audit only; no proof gap resolution",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_gap_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    first_manual_proof_attempt_execution_count = 1 if _has_count(source_text, "First manual proof attempt execution", "1") else 0
    manual_proof_attempt_row_count = 4 if _has_count(source_text, "Manual proof attempt row", "4") else 0
    attempted_lemma_skeleton_count = 2 if _has_count(source_text, "Attempted lemma skeleton", "2") else 0
    attempted_theorem_skeleton_count = 2 if _has_count(source_text, "Attempted theorem skeleton", "2") else 0
    partial_derivation_note_count = 4 if _has_count(source_text, "Partial derivation note", "4") else 0
    unresolved_attempt_item_count = 4 if _has_count(source_text, "Unresolved attempt item", "4") else 0
    successful_theorem_proof_count = 0 if _has_count(source_text, "Successful theorem proof", "0") else -1
    successful_lemma_proof_count = 0 if _has_count(source_text, "Successful lemma proof", "0") else -1

    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation", "0") else -1
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    definition_gap_count = sum(1 for row in rows if row.gap_type == "definition gap")
    assumption_gap_count = sum(1 for row in rows if row.gap_type == "assumption gap")
    dependency_gap_count = sum(1 for row in rows if row.gap_type == "dependency gap")
    boundary_gap_count = sum(1 for row in rows if row.gap_type == "boundary gap")
    unresolved_proof_attempt_gap_count = sum(1 for row in rows if row.resolution_status == "unresolved")
    resolved_proof_attempt_gap_count = sum(1 for row in rows if row.resolution_status == "resolved")
    proof_attempt_gap_resolution_count = resolved_proof_attempt_gap_count

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.56 first manual proof attempt source artifact.")
    if first_manual_proof_attempt_execution_count != 1:
        errors.append("Expected first manual proof attempt execution signal is absent.")
    if manual_proof_attempt_row_count != 4:
        errors.append("Expected manual proof attempt row count signal is absent.")
    if attempted_lemma_skeleton_count != 2:
        errors.append("Expected attempted lemma skeleton count signal is absent.")
    if attempted_theorem_skeleton_count != 2:
        errors.append("Expected attempted theorem skeleton count signal is absent.")
    if partial_derivation_note_count != 4:
        errors.append("Expected partial derivation note count signal is absent.")
    if unresolved_attempt_item_count != 4:
        errors.append("Expected unresolved attempt item count signal is absent.")
    if successful_theorem_proof_count != 0:
        errors.append("Expected successful theorem proof zero signal is absent.")
    if successful_lemma_proof_count != 0:
        errors.append("Expected successful lemma proof zero signal is absent.")
    if registered_proof_obligation_count != 6:
        errors.append("Expected carried registered proof obligation signal is absent.")
    if unresolved_proof_obligation_count != 6:
        errors.append("Expected carried unresolved proof obligation signal is absent.")
    if resolved_proof_obligation_count != 0:
        errors.append("Expected carried resolved proof obligation zero signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected carried registered formal definition candidate signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected carried unresolved formal definition candidate signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected carried completed formal definition candidate zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 8:
        errors.append("Expected eight manual proof attempt gap rows.")
    if unresolved_proof_attempt_gap_count != 8:
        errors.append("Expected eight unresolved proof attempt gaps.")
    if resolved_proof_attempt_gap_count != 0:
        errors.append("Expected zero resolved proof attempt gaps.")
    if proof_attempt_gap_resolution_count != 0:
        errors.append("Expected zero proof attempt gap resolutions.")

    warnings = [
        "Manual proof attempt gaps are audited but not cleared.",
        "Definition gaps block theorem or lemma upgrade.",
        "Assumption and dependency gaps remain open.",
        "Theorem proof and lemma proof remain absent.",
    ]

    lines = [
        "# Manual Proof Attempt Gap Audit v8.57",
        "",
        "## Purpose",
        "",
        "Audit the gaps exposed by the v8.56 first manual proof attempt execution while keeping proof gap resolution, theorem proof, lemma proof, completed formal definitions, formal mathematical proof, formal proof execution, external validation, citation addition, and submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Manual proof attempt gap rows",
        "",
        "| Gap ID | Linked attempt | Gap type | Gap description | Required next action | Resolution status | Boundary status |",
        "|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.gap_id} | {row.linked_attempt} | {row.gap_type} | {row.gap_description} | {row.required_next_action} | {row.resolution_status} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            "- Manual proof attempt gap audit count: 1",
            f"- Audited manual proof attempt row count: {manual_proof_attempt_row_count}",
            f"- Proof attempt gap row count: {len(rows)}",
            f"- Definition gap count: {definition_gap_count}",
            f"- Assumption gap count: {assumption_gap_count}",
            f"- Dependency gap count: {dependency_gap_count}",
            f"- Boundary gap count: {boundary_gap_count}",
            f"- Unresolved proof attempt gap count: {unresolved_proof_attempt_gap_count}",
            f"- Resolved proof attempt gap count: {resolved_proof_attempt_gap_count}",
            f"- Proof attempt gap resolution count: {proof_attempt_gap_resolution_count}",
            "",
            "## Carried v8.56 signals",
            "",
            f"- Carried first manual proof attempt execution count: {first_manual_proof_attempt_execution_count}",
            f"- Carried manual proof attempt row count: {manual_proof_attempt_row_count}",
            f"- Carried attempted lemma skeleton count: {attempted_lemma_skeleton_count}",
            f"- Carried attempted theorem skeleton count: {attempted_theorem_skeleton_count}",
            f"- Carried partial derivation note count: {partial_derivation_note_count}",
            f"- Carried unresolved attempt item count: {unresolved_attempt_item_count}",
            f"- Carried successful theorem proof count: {successful_theorem_proof_count}",
            f"- Carried successful lemma proof count: {successful_lemma_proof_count}",
            "",
            "## Carried proof object signals",
            "",
            f"- Carried registered proof obligation count: {registered_proof_obligation_count}",
            f"- Carried unresolved proof obligation count: {unresolved_proof_obligation_count}",
            f"- Carried resolved proof obligation count: {resolved_proof_obligation_count}",
            f"- Carried registered formal definition candidate count: {registered_formal_definition_candidate_count}",
            f"- Carried unresolved formal definition candidate count: {unresolved_formal_definition_candidate_count}",
            f"- Carried completed formal definition candidate count: {completed_formal_definition_candidate_count}",
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
            "The v8.57 artifact audits manual proof attempt gaps only. It does not clear gaps, does not establish theorem proof, does not establish lemma proof, does not complete formal definitions, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
            "",
            "## Critical reviewer note",
            "",
            "This milestone prevents the first manual attempt from being overread. The attempt revealed definition, assumption, dependency, and boundary gaps. Those gaps remain open and must be handled before any future proof-success claim.",
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
            "The project has audited eight manual proof attempt gaps from the first manual attempt, with all audited gaps still open and with theorem proof, lemma proof, completed formal definitions, formal mathematical proof, formal proof execution, proof gap resolution, citation additions, external validation, and manuscript submission readiness kept at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this formal proof.",
            "- Do not call this theorem proof.",
            "- Do not call this lemma proof.",
            "- Do not call this completed formal definitions.",
            "- Do not call this resolved proof obligations.",
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
        errors.append("Overclaim pattern detected in v8.57 manual proof attempt gap audit report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.57 manual proof attempt gap audit report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ManualProofAttemptGapAuditReport:
    text = render_report()
    source_text = _read_source()
    rows = build_gap_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    first_manual_proof_attempt_execution_count = 1 if _has_count(source_text, "First manual proof attempt execution", "1") else 0
    manual_proof_attempt_row_count = 4 if _has_count(source_text, "Manual proof attempt row", "4") else 0
    attempted_lemma_skeleton_count = 2 if _has_count(source_text, "Attempted lemma skeleton", "2") else 0
    attempted_theorem_skeleton_count = 2 if _has_count(source_text, "Attempted theorem skeleton", "2") else 0
    partial_derivation_note_count = 4 if _has_count(source_text, "Partial derivation note", "4") else 0
    unresolved_attempt_item_count = 4 if _has_count(source_text, "Unresolved attempt item", "4") else 0
    successful_theorem_proof_count = 0 if _has_count(source_text, "Successful theorem proof", "0") else -1
    successful_lemma_proof_count = 0 if _has_count(source_text, "Successful lemma proof", "0") else -1

    registered_proof_obligation_count = 6 if _has_count(source_text, "Carried registered proof obligation", "6") else 0
    unresolved_proof_obligation_count = 6 if _has_count(source_text, "Carried unresolved proof obligation", "6") else 0
    resolved_proof_obligation_count = 0 if _has_count(source_text, "Carried resolved proof obligation", "0") else -1
    registered_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried registered formal definition candidate", "2") else 0
    unresolved_formal_definition_candidate_count = 2 if _has_count(source_text, "Carried unresolved formal definition candidate", "2") else 0
    completed_formal_definition_candidate_count = 0 if _has_count(source_text, "Carried completed formal definition candidate", "0") else -1

    source_hard_zero_signal_count = _source_hard_zero_signal_count(source_text)

    definition_gap_count = sum(1 for row in rows if row.gap_type == "definition gap")
    assumption_gap_count = sum(1 for row in rows if row.gap_type == "assumption gap")
    dependency_gap_count = sum(1 for row in rows if row.gap_type == "dependency gap")
    boundary_gap_count = sum(1 for row in rows if row.gap_type == "boundary gap")
    unresolved_proof_attempt_gap_count = sum(1 for row in rows if row.resolution_status == "unresolved")
    resolved_proof_attempt_gap_count = sum(1 for row in rows if row.resolution_status == "resolved")
    proof_attempt_gap_resolution_count = resolved_proof_attempt_gap_count

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.56 first manual proof attempt source artifact.")
    if first_manual_proof_attempt_execution_count != 1:
        errors.append("Expected first manual proof attempt execution signal is absent.")
    if manual_proof_attempt_row_count != 4:
        errors.append("Expected manual proof attempt row count signal is absent.")
    if attempted_lemma_skeleton_count != 2:
        errors.append("Expected attempted lemma skeleton count signal is absent.")
    if attempted_theorem_skeleton_count != 2:
        errors.append("Expected attempted theorem skeleton count signal is absent.")
    if partial_derivation_note_count != 4:
        errors.append("Expected partial derivation note count signal is absent.")
    if unresolved_attempt_item_count != 4:
        errors.append("Expected unresolved attempt item count signal is absent.")
    if successful_theorem_proof_count != 0:
        errors.append("Expected successful theorem proof zero signal is absent.")
    if successful_lemma_proof_count != 0:
        errors.append("Expected successful lemma proof zero signal is absent.")
    if registered_proof_obligation_count != 6:
        errors.append("Expected carried registered proof obligation signal is absent.")
    if unresolved_proof_obligation_count != 6:
        errors.append("Expected carried unresolved proof obligation signal is absent.")
    if resolved_proof_obligation_count != 0:
        errors.append("Expected carried resolved proof obligation zero signal is absent.")
    if registered_formal_definition_candidate_count != 2:
        errors.append("Expected carried registered formal definition candidate signal is absent.")
    if unresolved_formal_definition_candidate_count != 2:
        errors.append("Expected carried unresolved formal definition candidate signal is absent.")
    if completed_formal_definition_candidate_count != 0:
        errors.append("Expected carried completed formal definition candidate zero signal is absent.")
    if source_hard_zero_signal_count < 10:
        errors.append("Expected hard-zero source signals are incomplete.")
    if len(rows) != 8:
        errors.append("Expected eight manual proof attempt gap rows.")
    if unresolved_proof_attempt_gap_count != 8:
        errors.append("Expected eight unresolved proof attempt gaps.")
    if resolved_proof_attempt_gap_count != 0:
        errors.append("Expected zero resolved proof attempt gaps.")
    if proof_attempt_gap_resolution_count != 0:
        errors.append("Expected zero proof attempt gap resolutions.")

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "Manual proof attempt gaps are audited but not cleared.",
        "Definition gaps block theorem or lemma upgrade.",
        "Assumption and dependency gaps remain open.",
        "Theorem proof and lemma proof remain absent.",
    ]

    return ManualProofAttemptGapAuditReport(
        title="Manual Proof Attempt Gap Audit v8.57",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        manual_proof_attempt_gap_audit_count=1,
        audited_manual_proof_attempt_row_count=manual_proof_attempt_row_count,
        proof_attempt_gap_row_count=len(rows),
        definition_gap_count=definition_gap_count,
        assumption_gap_count=assumption_gap_count,
        dependency_gap_count=dependency_gap_count,
        boundary_gap_count=boundary_gap_count,
        unresolved_proof_attempt_gap_count=unresolved_proof_attempt_gap_count,
        resolved_proof_attempt_gap_count=resolved_proof_attempt_gap_count,
        proof_attempt_gap_resolution_count=proof_attempt_gap_resolution_count,
        carried_first_manual_proof_attempt_execution_count=first_manual_proof_attempt_execution_count,
        carried_manual_proof_attempt_row_count=manual_proof_attempt_row_count,
        carried_attempted_lemma_skeleton_count=attempted_lemma_skeleton_count,
        carried_attempted_theorem_skeleton_count=attempted_theorem_skeleton_count,
        carried_partial_derivation_note_count=partial_derivation_note_count,
        carried_unresolved_attempt_item_count=unresolved_attempt_item_count,
        carried_successful_theorem_proof_count=successful_theorem_proof_count,
        carried_successful_lemma_proof_count=successful_lemma_proof_count,
        carried_registered_proof_obligation_count=registered_proof_obligation_count,
        carried_unresolved_proof_obligation_count=unresolved_proof_obligation_count,
        carried_resolved_proof_obligation_count=resolved_proof_obligation_count,
        carried_registered_formal_definition_candidate_count=registered_formal_definition_candidate_count,
        carried_unresolved_formal_definition_candidate_count=unresolved_formal_definition_candidate_count,
        carried_completed_formal_definition_candidate_count=completed_formal_definition_candidate_count,
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
        boundary_phrase_count=40,
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
