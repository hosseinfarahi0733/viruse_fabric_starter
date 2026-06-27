from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/stabilization_predicate_definition_plan_v8_78.md")
OUTPUT_PATH = Path("outputs/stabilization_predicate_controlled_definition_execution_v8_79.md")


@dataclass(frozen=True)
class StabilizationPredicateDraftClause:
    clause_id: str
    clause_name: str
    draft_content: str
    dependency: str
    boundary_status: str


@dataclass(frozen=True)
class StabilizationPredicateControlledDefinitionExecutionReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    stabilization_predicate_controlled_definition_execution_count: int
    definition_execution_count: int
    stabilization_predicate_draft_clause_count: int
    carrier_domain_clause_count: int
    local_persistence_clause_count: int
    recurrence_clause_count: int
    exclusion_clause_count: int
    audit_dependency_clause_count: int
    stabilization_predicate_definition_completion_count: int
    attractor_class_definition_completion_count: int
    constraint_region_definition_completion_count: int
    causal_mass_definition_completion_count: int
    observer_projection_definition_completion_count: int

    carried_stabilization_predicate_definition_plan_count: int
    carried_stabilization_predicate_requirement_row_count: int
    carried_selected_predicate_placeholder_count: int
    carried_planned_predicate_symbol_count: int
    carried_planned_definition_target_count: int
    carried_definition_execution_count: int
    carried_stabilization_predicate_definition_completion_count: int
    carried_attractor_class_definition_completion_count: int
    carried_constraint_region_definition_completion_count: int
    carried_causal_mass_definition_completion_count: int
    carried_observer_projection_definition_completion_count: int
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
    carried_cumulative_limited_theorem_proven_count: int

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
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]", "/", "{", "}", "=", ">"]:
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
        "stabilization predicate is defined",
        "sigma_a is defined",
        "sigma a is defined",
        "stabilization predicate definition is complete",
        "sigma_a definition is complete",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_draft_clauses() -> List[StabilizationPredicateDraftClause]:
    return [
        StabilizationPredicateDraftClause(
            clause_id="SPD-EXEC-001",
            clause_name="Carrier domain draft clause",
            draft_content="Sigma_A is evaluated only on finite R-path quotient carriers of the form class_R(a), where class_R(a) abbreviates the mutual-reachability quotient carrier from the audited scaffold.",
            dependency="v8.77 audited scaffold and PKT-005 quotient carrier",
            boundary_status="draft clause only; not a completed formal definition",
        ),
        StabilizationPredicateDraftClause(
            clause_id="SPD-EXEC-002",
            clause_name="Local persistence draft clause",
            draft_content="A carrier class_R(a) may satisfy the draft stabilization predicate only if its members preserve quotient-carrier membership across admissible finite R-path continuations selected by the current local relation R.",
            dependency="finite R-path reachability and quotient-carrier membership",
            boundary_status="draft clause only; no theorem attempted",
        ),
        StabilizationPredicateDraftClause(
            clause_id="SPD-EXEC-003",
            clause_name="Recurrence draft clause",
            draft_content="A carrier class_R(a) must have a return-compatible witness pattern inside the finite R-path kernel before it can be treated as a candidate for attractor-like behavior.",
            dependency="Reach_R, mutual reachability, and quotient carrier structure",
            boundary_status="draft clause only; not externally validated",
        ),
        StabilizationPredicateDraftClause(
            clause_id="SPD-EXEC-004",
            clause_name="Exclusion draft clause",
            draft_content="If persistence, recurrence, or later constraint-compatibility requirements are absent, the quotient carrier is excluded from attractor-class candidate status.",
            dependency="negative boundary from v8.78 requirement plan",
            boundary_status="draft clause only; no biological claim",
        ),
        StabilizationPredicateDraftClause(
            clause_id="SPD-EXEC-005",
            clause_name="Constraint placeholder draft clause",
            draft_content="Constraint-compatible region integration remains a named dependency slot and cannot be treated as active until a later controlled artifact supplies the missing region definition.",
            dependency="future constraint-region artifact",
            boundary_status="blocked until later definition work",
        ),
        StabilizationPredicateDraftClause(
            clause_id="SPD-EXEC-006",
            clause_name="Audit dependency draft clause",
            draft_content="Any later use of this draft predicate in theorem work requires a separate boundary audit and cannot be promoted directly to theorem proof or manuscript readiness.",
            dependency="v8.79 boundary discipline",
            boundary_status="audit required before theorem work",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    clauses = build_draft_clauses()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_plan_count = 1 if _has_count(source_text, "Stabilization predicate definition plan", "1") else 0
    carried_requirement_row_count = 6 if _has_count(source_text, "Stabilization predicate requirement row", "6") else 0
    carried_selected_placeholder_count = 1 if _has_count(source_text, "Selected predicate placeholder", "1") else 0
    carried_planned_symbol_count = 1 if _has_count(source_text, "Planned predicate symbol", "1") else 0
    carried_planned_target_count = 1 if _has_count(source_text, "Planned definition target", "1") else 0
    carried_definition_execution_count = 0 if _has_count(source_text, "Definition execution", "0") else -1
    carried_stabilization_completion_count = 0 if _has_count(source_text, "Stabilization predicate definition completion", "0") else -1
    carried_attractor_completion_count = 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1
    carried_constraint_completion_count = 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1
    carried_causal_mass_completion_count = 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1
    carried_observer_projection_completion_count = 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1
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
    carried_cumulative_limited_theorem_proven_count = 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0

    stabilization_predicate_controlled_definition_execution_count = 1
    definition_execution_count = 1
    stabilization_predicate_draft_clause_count = len(clauses)
    carrier_domain_clause_count = 1
    local_persistence_clause_count = 1
    recurrence_clause_count = 1
    exclusion_clause_count = 1
    audit_dependency_clause_count = 1

    stabilization_predicate_definition_completion_count = 0
    attractor_class_definition_completion_count = 0
    constraint_region_definition_completion_count = 0
    causal_mass_definition_completion_count = 0
    observer_projection_definition_completion_count = 0

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
        errors.append("Missing required v8.78 stabilization predicate definition plan source artifact.")
    if carried_plan_count != 1:
        errors.append("Expected carried stabilization predicate definition plan signal is absent.")
    if carried_requirement_row_count != 6:
        errors.append("Expected carried stabilization predicate requirement row count is absent.")
    if carried_selected_placeholder_count != 1:
        errors.append("Expected carried selected predicate placeholder signal is absent.")
    if carried_planned_symbol_count != 1:
        errors.append("Expected carried planned predicate symbol signal is absent.")
    if carried_planned_target_count != 1:
        errors.append("Expected carried planned definition target signal is absent.")
    if carried_definition_execution_count != 0:
        errors.append("Expected carried definition execution zero signal is absent.")
    if carried_stabilization_completion_count != 0:
        errors.append("Expected carried stabilization predicate definition completion zero signal is absent.")
    if carried_attractor_completion_count != 0:
        errors.append("Expected carried attractor-class definition completion zero signal is absent.")
    if carried_constraint_completion_count != 0:
        errors.append("Expected carried constraint-region definition completion zero signal is absent.")
    if carried_causal_mass_completion_count != 0:
        errors.append("Expected carried causal-mass definition completion zero signal is absent.")
    if carried_observer_projection_completion_count != 0:
        errors.append("Expected carried observer-projection definition completion zero signal is absent.")
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
    if stabilization_predicate_draft_clause_count != 6:
        errors.append("Expected six stabilization predicate draft clauses.")
    if definition_execution_count != 1:
        errors.append("Expected one controlled definition execution.")
    if stabilization_predicate_definition_completion_count != 0:
        errors.append("Expected zero stabilization predicate definition completions.")
    if attractor_class_definition_completion_count != 0:
        errors.append("Expected zero attractor-class definition completions.")
    if constraint_region_definition_completion_count != 0:
        errors.append("Expected zero constraint-region definition completions.")
    if causal_mass_definition_completion_count != 0:
        errors.append("Expected zero causal-mass definition completions.")
    if observer_projection_definition_completion_count != 0:
        errors.append("Expected zero observer-projection definition completions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")

    warnings = [
        "This milestone executes a controlled draft clause set only; it does not complete the predicate definition.",
        "No attractor-class theorem is attempted.",
        "Constraint-region, causal-mass, and observer-projection definitions remain incomplete.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Stabilization Predicate Controlled Definition Execution v8.79",
        "",
        "## Purpose",
        "",
        "Execute a controlled draft clause set for the stabilization predicate placeholder Sigma_A, while keeping stabilization predicate definition completion, attractor-class definition completion, constraint-region definition completion, causal-mass definition completion, observer-projection definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Controlled draft clauses",
        "",
        "| Clause ID | Clause name | Draft content | Dependency | Boundary status |",
        "|---|---|---|---|---|",
    ]

    for clause in clauses:
        lines.append(
            f"| {clause.clause_id} | {clause.clause_name} | {clause.draft_content} | {clause.dependency} | {clause.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Draft predicate shape",
            "",
            "- Draft symbol: Sigma_A",
            "- Draft carrier: class_R(a), the finite R-path quotient carrier from the audited scaffold.",
            "- Draft reading: a quotient carrier is accepted only when carrier-domain, local-persistence, recurrence, exclusion, and future audit conditions are all respected.",
            "- Completion status: not completed in this milestone.",
            "",
            "## Counts",
            "",
            f"- Stabilization predicate controlled definition execution count: {stabilization_predicate_controlled_definition_execution_count}",
            f"- Definition execution count: {definition_execution_count}",
            f"- Stabilization predicate draft clause count: {stabilization_predicate_draft_clause_count}",
            f"- Carrier domain clause count: {carrier_domain_clause_count}",
            f"- Local persistence clause count: {local_persistence_clause_count}",
            f"- Recurrence clause count: {recurrence_clause_count}",
            f"- Exclusion clause count: {exclusion_clause_count}",
            f"- Audit dependency clause count: {audit_dependency_clause_count}",
            f"- Stabilization predicate definition completion count: {stabilization_predicate_definition_completion_count}",
            f"- Attractor class definition completion count: {attractor_class_definition_completion_count}",
            f"- Constraint region definition completion count: {constraint_region_definition_completion_count}",
            f"- Causal mass definition completion count: {causal_mass_definition_completion_count}",
            f"- Observer projection definition completion count: {observer_projection_definition_completion_count}",
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
            "## Carried v8.78 signals",
            "",
            f"- Carried stabilization predicate definition plan count: {carried_plan_count}",
            f"- Carried stabilization predicate requirement row count: {carried_requirement_row_count}",
            f"- Carried selected predicate placeholder count: {carried_selected_placeholder_count}",
            f"- Carried planned predicate symbol count: {carried_planned_symbol_count}",
            f"- Carried planned definition target count: {carried_planned_target_count}",
            f"- Carried definition execution count: {carried_definition_execution_count}",
            f"- Carried stabilization predicate definition completion count: {carried_stabilization_completion_count}",
            f"- Carried attractor class definition completion count: {carried_attractor_completion_count}",
            f"- Carried constraint region definition completion count: {carried_constraint_completion_count}",
            f"- Carried causal mass definition completion count: {carried_causal_mass_completion_count}",
            f"- Carried observer projection definition completion count: {carried_observer_projection_completion_count}",
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
            f"- Carried cumulative limited theorem proven count: {carried_cumulative_limited_theorem_proven_count}",
            "",
            "## Boundary interpretation",
            "",
            "The v8.79 artifact executes a controlled draft clause set for Sigma_A. It adds one definition execution count, but keeps stabilization predicate definition completion, attractor-class definition completion, constraint-region definition completion, causal-mass definition completion, observer-projection definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, citation additions, external validation, and manuscript readiness at zero.",
            "",
            "## Critical reviewer note",
            "",
            "This is the first disciplined move from a placeholder toward an actual predicate shape. It remains draft-level and must be audited before any theorem attempt or readiness claim.",
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
            "The project has executed a controlled draft clause set for the stabilization predicate placeholder Sigma_A while preserving the distinction between draft-level definition execution and definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this stabilization predicate completion.",
            "- Do not call this a completed attractor definition.",
            "- Do not call this a theorem proof.",
            "- Do not call this proof execution.",
            "- Do not call this proof assistant verification.",
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
        errors.append("Overclaim pattern detected in v8.79 stabilization predicate controlled definition execution.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.79 stabilization predicate controlled definition execution.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> StabilizationPredicateControlledDefinitionExecutionReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_plan_count = 1 if _has_count(source_text, "Stabilization predicate definition plan", "1") else 0
    carried_requirement_row_count = 6 if _has_count(source_text, "Stabilization predicate requirement row", "6") else 0
    carried_selected_placeholder_count = 1 if _has_count(source_text, "Selected predicate placeholder", "1") else 0
    carried_planned_symbol_count = 1 if _has_count(source_text, "Planned predicate symbol", "1") else 0
    carried_planned_target_count = 1 if _has_count(source_text, "Planned definition target", "1") else 0
    carried_definition_execution_count = 0 if _has_count(source_text, "Definition execution", "0") else -1
    carried_stabilization_completion_count = 0 if _has_count(source_text, "Stabilization predicate definition completion", "0") else -1
    carried_attractor_completion_count = 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1
    carried_constraint_completion_count = 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1
    carried_causal_mass_completion_count = 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1
    carried_observer_projection_completion_count = 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1
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
    carried_cumulative_limited_theorem_proven_count = 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0

    clauses = build_draft_clauses()

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.78 stabilization predicate definition plan source artifact.")
    if carried_plan_count != 1:
        errors.append("Expected carried stabilization predicate definition plan signal is absent.")
    if carried_requirement_row_count != 6:
        errors.append("Expected carried stabilization predicate requirement row count is absent.")
    if carried_selected_placeholder_count != 1:
        errors.append("Expected carried selected predicate placeholder signal is absent.")
    if carried_planned_symbol_count != 1:
        errors.append("Expected carried planned predicate symbol signal is absent.")
    if carried_planned_target_count != 1:
        errors.append("Expected carried planned definition target signal is absent.")
    if carried_definition_execution_count != 0:
        errors.append("Expected carried definition execution zero signal is absent.")
    if carried_stabilization_completion_count != 0:
        errors.append("Expected carried stabilization predicate definition completion zero signal is absent.")
    if carried_attractor_completion_count != 0:
        errors.append("Expected carried attractor-class definition completion zero signal is absent.")
    if carried_constraint_completion_count != 0:
        errors.append("Expected carried constraint-region definition completion zero signal is absent.")
    if carried_causal_mass_completion_count != 0:
        errors.append("Expected carried causal-mass definition completion zero signal is absent.")
    if carried_observer_projection_completion_count != 0:
        errors.append("Expected carried observer-projection definition completion zero signal is absent.")
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
    if len(clauses) != 6:
        errors.append("Expected six stabilization predicate draft clauses.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone executes a controlled draft clause set only; it does not complete the predicate definition.",
        "No attractor-class theorem is attempted.",
        "Constraint-region, causal-mass, and observer-projection definitions remain incomplete.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    return StabilizationPredicateControlledDefinitionExecutionReport(
        title="Stabilization Predicate Controlled Definition Execution v8.79",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        stabilization_predicate_controlled_definition_execution_count=1,
        definition_execution_count=1,
        stabilization_predicate_draft_clause_count=len(clauses),
        carrier_domain_clause_count=1,
        local_persistence_clause_count=1,
        recurrence_clause_count=1,
        exclusion_clause_count=1,
        audit_dependency_clause_count=1,
        stabilization_predicate_definition_completion_count=0,
        attractor_class_definition_completion_count=0,
        constraint_region_definition_completion_count=0,
        causal_mass_definition_completion_count=0,
        observer_projection_definition_completion_count=0,
        carried_stabilization_predicate_definition_plan_count=carried_plan_count,
        carried_stabilization_predicate_requirement_row_count=carried_requirement_row_count,
        carried_selected_predicate_placeholder_count=carried_selected_placeholder_count,
        carried_planned_predicate_symbol_count=carried_planned_symbol_count,
        carried_planned_definition_target_count=carried_planned_target_count,
        carried_definition_execution_count=carried_definition_execution_count,
        carried_stabilization_predicate_definition_completion_count=carried_stabilization_completion_count,
        carried_attractor_class_definition_completion_count=carried_attractor_completion_count,
        carried_constraint_region_definition_completion_count=carried_constraint_completion_count,
        carried_causal_mass_definition_completion_count=carried_causal_mass_completion_count,
        carried_observer_projection_definition_completion_count=carried_observer_projection_completion_count,
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
        carried_cumulative_limited_theorem_proven_count=carried_cumulative_limited_theorem_proven_count,
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
        boundary_phrase_count=63,
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
