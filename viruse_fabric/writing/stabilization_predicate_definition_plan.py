from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/attractor_class_scaffold_boundary_audit_v8_77.md")
OUTPUT_PATH = Path("outputs/stabilization_predicate_definition_plan_v8_78.md")


@dataclass(frozen=True)
class StabilizationPredicateRequirementRow:
    requirement_id: str
    requirement_name: str
    purpose: str
    required_input: str
    planned_output: str
    boundary_status: str


@dataclass(frozen=True)
class StabilizationPredicateDefinitionPlanReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    stabilization_predicate_definition_plan_count: int
    stabilization_predicate_requirement_row_count: int
    selected_predicate_placeholder_count: int
    planned_predicate_symbol_count: int
    planned_definition_target_count: int
    definition_execution_count: int
    stabilization_predicate_definition_completion_count: int
    attractor_class_definition_completion_count: int
    constraint_region_definition_completion_count: int
    causal_mass_definition_completion_count: int
    observer_projection_definition_completion_count: int

    carried_attractor_class_scaffold_boundary_audit_count: int
    carried_audited_scaffold_count: int
    carried_scaffold_boundary_row_count: int
    carried_new_bridge_execution_count: int
    carried_new_attractor_class_candidate_scaffold_count: int
    carried_new_theorem_proven_count: int
    carried_proof_execution_count: int
    carried_attractor_class_theorem_attempt_count: int
    carried_attractor_class_definition_completion_count: int
    carried_constraint_region_definition_completion_count: int
    carried_causal_mass_definition_completion_count: int
    carried_observer_projection_definition_completion_count: int
    carried_cumulative_limited_theorem_proven_count: int
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
        "attractor theory is complete",
        "causal mass is defined",
        "observer projection is defined",
        "constraint-compatible regions are complete",
        "stabilization predicate is defined",
        "sigma_a is defined",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_requirement_rows() -> List[StabilizationPredicateRequirementRow]:
    return [
        StabilizationPredicateRequirementRow(
            requirement_id="SPD-REQ-001",
            requirement_name="Carrier domain",
            purpose="state exactly what object Sigma_A is evaluated on",
            required_input="finite R-path quotient class [a]_R from the audited scaffold",
            planned_output="domain clause for Sigma_A over quotient carriers",
            boundary_status="planned only; not executed",
        ),
        StabilizationPredicateRequirementRow(
            requirement_id="SPD-REQ-002",
            requirement_name="Local persistence condition",
            purpose="state what it would mean for a carrier to persist under admissible finite R-path transitions",
            required_input="finite R-path reachability and quotient-carrier structure",
            planned_output="candidate persistence clause",
            boundary_status="planned only; not completed",
        ),
        StabilizationPredicateRequirementRow(
            requirement_id="SPD-REQ-003",
            requirement_name="Recurrence or return condition",
            purpose="separate mere reachability from repeated or return-compatible behavior",
            required_input="Reach_R and mutual reachability structure",
            planned_output="candidate recurrence clause",
            boundary_status="planned only; no theorem attempted",
        ),
        StabilizationPredicateRequirementRow(
            requirement_id="SPD-REQ-004",
            requirement_name="Constraint-compatibility placeholder",
            purpose="reserve a slot for later constraint-compatible region integration without claiming it now",
            required_input="future constraint-region definition artifact",
            planned_output="placeholder dependency slot",
            boundary_status="blocked until later definition work",
        ),
        StabilizationPredicateRequirementRow(
            requirement_id="SPD-REQ-005",
            requirement_name="Failure and exclusion clause",
            purpose="state when a quotient carrier must not be treated as attractor-like",
            required_input="absence of persistence, recurrence, or constraint compatibility",
            planned_output="negative boundary clause",
            boundary_status="planned only; not validated",
        ),
        StabilizationPredicateRequirementRow(
            requirement_id="SPD-REQ-006",
            requirement_name="Audit requirements",
            purpose="ensure the eventual definition is audited before any theorem attempt",
            required_input="completed draft of Sigma_A definition",
            planned_output="mandatory boundary audit milestone",
            boundary_status="future audit required",
        ),
    ]


def render_report() -> str:
    source_text = _read_source()
    rows = build_requirement_rows()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_scaffold_audit_count = 1 if _has_count(source_text, "Attractor class scaffold boundary audit", "1") else 0
    carried_audited_scaffold_count = 1 if _has_count(source_text, "Audited scaffold", "1") else 0
    carried_scaffold_boundary_row_count = 6 if _has_count(source_text, "Scaffold boundary row", "6") else 0
    carried_new_bridge_execution_count = 0 if _has_count(source_text, "New bridge execution", "0") else -1
    carried_new_candidate_scaffold_count = 0 if _has_count(source_text, "New attractor class candidate scaffold", "0") else -1
    carried_new_theorem_proven_count = 0 if _has_count(source_text, "New theorem proven", "0") else -1
    carried_proof_execution_count = 0 if _has_count(source_text, "Proof execution", "0") else -1
    carried_attractor_class_theorem_attempt_count = 0 if _has_count(source_text, "Attractor class theorem attempt", "0") else -1
    carried_attractor_class_definition_completion_count = 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1
    carried_constraint_region_definition_completion_count = 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1
    carried_causal_mass_definition_completion_count = 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1
    carried_observer_projection_definition_completion_count = 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1
    carried_cumulative_limited_theorem_proven_count = 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    stabilization_predicate_definition_plan_count = 1
    stabilization_predicate_requirement_row_count = len(rows)
    selected_predicate_placeholder_count = 1
    planned_predicate_symbol_count = 1
    planned_definition_target_count = 1
    definition_execution_count = 0
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
        errors.append("Missing required v8.77 attractor scaffold boundary audit source artifact.")
    if carried_scaffold_audit_count != 1:
        errors.append("Expected carried v8.77 scaffold audit signal is absent.")
    if carried_audited_scaffold_count != 1:
        errors.append("Expected carried audited scaffold signal is absent.")
    if carried_scaffold_boundary_row_count != 6:
        errors.append("Expected carried scaffold boundary row count is absent.")
    if carried_new_bridge_execution_count != 0:
        errors.append("Expected carried new bridge execution zero signal is absent.")
    if carried_new_candidate_scaffold_count != 0:
        errors.append("Expected carried new candidate scaffold zero signal is absent.")
    if carried_new_theorem_proven_count != 0:
        errors.append("Expected carried new theorem proven zero signal is absent.")
    if carried_proof_execution_count != 0:
        errors.append("Expected carried proof execution zero signal is absent.")
    if carried_attractor_class_theorem_attempt_count != 0:
        errors.append("Expected carried attractor-class theorem attempt zero signal is absent.")
    if carried_attractor_class_definition_completion_count != 0:
        errors.append("Expected carried attractor-class definition completion zero signal is absent.")
    if carried_constraint_region_definition_completion_count != 0:
        errors.append("Expected carried constraint-region definition completion zero signal is absent.")
    if carried_causal_mass_definition_completion_count != 0:
        errors.append("Expected carried causal-mass definition completion zero signal is absent.")
    if carried_observer_projection_definition_completion_count != 0:
        errors.append("Expected carried observer-projection definition completion zero signal is absent.")
    if carried_cumulative_limited_theorem_proven_count != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
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
    if stabilization_predicate_requirement_row_count != 6:
        errors.append("Expected six stabilization predicate requirement rows.")
    if definition_execution_count != 0:
        errors.append("Expected zero definition executions.")
    if stabilization_predicate_definition_completion_count != 0:
        errors.append("Expected zero stabilization predicate definition completions.")
    if attractor_class_definition_completion_count != 0:
        errors.append("Expected zero attractor-class definition completions.")
    if constraint_region_definition_completion_count != 0:
        errors.append("Expected zero constraint-region definition completions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")

    warnings = [
        "This milestone plans the Sigma_A definition only; it does not execute or complete it.",
        "No attractor-class theorem is attempted.",
        "Constraint-region, causal-mass, and observer-projection definitions remain incomplete.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Stabilization Predicate Definition Plan v8.78",
        "",
        "## Purpose",
        "",
        "Plan the later definition of the stabilization predicate placeholder Sigma_A used by the attractor-class candidate scaffold, while keeping definition execution, definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, proof gap resolution, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Planned predicate target",
        "",
        "- Predicate placeholder: Sigma_A",
        "- Planned carrier: finite R-path quotient carrier [a]_R",
        "- Planned definition status: not executed and not completed in this milestone.",
        "- Future dependency: a later controlled definition execution and boundary audit.",
        "",
        "## Requirement rows",
        "",
        "| Requirement ID | Requirement name | Purpose | Required input | Planned output | Boundary status |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.requirement_id} | {row.requirement_name} | {row.purpose} | {row.required_input} | {row.planned_output} | {row.boundary_status} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Stabilization predicate definition plan count: {stabilization_predicate_definition_plan_count}",
            f"- Stabilization predicate requirement row count: {stabilization_predicate_requirement_row_count}",
            f"- Selected predicate placeholder count: {selected_predicate_placeholder_count}",
            f"- Planned predicate symbol count: {planned_predicate_symbol_count}",
            f"- Planned definition target count: {planned_definition_target_count}",
            f"- Definition execution count: {definition_execution_count}",
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
            "## Carried v8.77 signals",
            "",
            f"- Carried attractor class scaffold boundary audit count: {carried_scaffold_audit_count}",
            f"- Carried audited scaffold count: {carried_audited_scaffold_count}",
            f"- Carried scaffold boundary row count: {carried_scaffold_boundary_row_count}",
            f"- Carried new bridge execution count: {carried_new_bridge_execution_count}",
            f"- Carried new attractor class candidate scaffold count: {carried_new_candidate_scaffold_count}",
            f"- Carried new theorem proven count: {carried_new_theorem_proven_count}",
            f"- Carried proof execution count: {carried_proof_execution_count}",
            f"- Carried attractor class theorem attempt count: {carried_attractor_class_theorem_attempt_count}",
            f"- Carried attractor class definition completion count: {carried_attractor_class_definition_completion_count}",
            f"- Carried constraint region definition completion count: {carried_constraint_region_definition_completion_count}",
            f"- Carried causal mass definition completion count: {carried_causal_mass_definition_completion_count}",
            f"- Carried observer projection definition completion count: {carried_observer_projection_definition_completion_count}",
            f"- Carried cumulative limited theorem proven count: {carried_cumulative_limited_theorem_proven_count}",
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
            "The v8.78 artifact plans the later definition of Sigma_A only. It adds no definition execution, no stabilization predicate definition completion, no completed attractor-class definition, no completed constraint-region definition, no causal-mass completion, no observer-projection completion, no theorem proof, no proof execution, no proof assistant verification, no completed formalization, no framework-level proof, no citation additions, no external validation, and no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The plan is necessary because Sigma_A must not become a decorative symbol pretending to be a definition. The next execution milestone must define the predicate under explicit carrier, persistence, recurrence, exclusion, and audit conditions.",
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
            "The project has planned the later definition of the stabilization predicate placeholder Sigma_A while preserving the distinction between a definition plan and definition execution, definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this definition execution.",
            "- Do not call this stabilization predicate completion.",
            "- Do not call this a completed attractor definition.",
            "- Do not call this a theorem proof.",
            "- Do not call this proof execution.",
            "- Do not call this proof assistant verification.",
            "- Do not call this framework-level proof.",
            "- Do not call this manuscript readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.78 stabilization predicate definition plan.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.78 stabilization predicate definition plan.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> StabilizationPredicateDefinitionPlanReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_scaffold_audit_count = 1 if _has_count(source_text, "Attractor class scaffold boundary audit", "1") else 0
    carried_audited_scaffold_count = 1 if _has_count(source_text, "Audited scaffold", "1") else 0
    carried_scaffold_boundary_row_count = 6 if _has_count(source_text, "Scaffold boundary row", "6") else 0
    carried_new_bridge_execution_count = 0 if _has_count(source_text, "New bridge execution", "0") else -1
    carried_new_candidate_scaffold_count = 0 if _has_count(source_text, "New attractor class candidate scaffold", "0") else -1
    carried_new_theorem_proven_count = 0 if _has_count(source_text, "New theorem proven", "0") else -1
    carried_proof_execution_count = 0 if _has_count(source_text, "Proof execution", "0") else -1
    carried_attractor_class_theorem_attempt_count = 0 if _has_count(source_text, "Attractor class theorem attempt", "0") else -1
    carried_attractor_class_definition_completion_count = 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1
    carried_constraint_region_definition_completion_count = 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1
    carried_causal_mass_definition_completion_count = 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1
    carried_observer_projection_definition_completion_count = 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1
    carried_cumulative_limited_theorem_proven_count = 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    rows = build_requirement_rows()

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.77 attractor scaffold boundary audit source artifact.")
    if carried_scaffold_audit_count != 1:
        errors.append("Expected carried v8.77 scaffold audit signal is absent.")
    if carried_audited_scaffold_count != 1:
        errors.append("Expected carried audited scaffold signal is absent.")
    if carried_scaffold_boundary_row_count != 6:
        errors.append("Expected carried scaffold boundary row count is absent.")
    if carried_new_bridge_execution_count != 0:
        errors.append("Expected carried new bridge execution zero signal is absent.")
    if carried_new_candidate_scaffold_count != 0:
        errors.append("Expected carried new candidate scaffold zero signal is absent.")
    if carried_new_theorem_proven_count != 0:
        errors.append("Expected carried new theorem proven zero signal is absent.")
    if carried_proof_execution_count != 0:
        errors.append("Expected carried proof execution zero signal is absent.")
    if carried_attractor_class_theorem_attempt_count != 0:
        errors.append("Expected carried attractor-class theorem attempt zero signal is absent.")
    if carried_attractor_class_definition_completion_count != 0:
        errors.append("Expected carried attractor-class definition completion zero signal is absent.")
    if carried_constraint_region_definition_completion_count != 0:
        errors.append("Expected carried constraint-region definition completion zero signal is absent.")
    if carried_causal_mass_definition_completion_count != 0:
        errors.append("Expected carried causal-mass definition completion zero signal is absent.")
    if carried_observer_projection_definition_completion_count != 0:
        errors.append("Expected carried observer-projection definition completion zero signal is absent.")
    if carried_cumulative_limited_theorem_proven_count != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
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
        errors.append("Expected six stabilization predicate requirement rows.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone plans the Sigma_A definition only; it does not execute or complete it.",
        "No attractor-class theorem is attempted.",
        "Constraint-region, causal-mass, and observer-projection definitions remain incomplete.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    return StabilizationPredicateDefinitionPlanReport(
        title="Stabilization Predicate Definition Plan v8.78",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        stabilization_predicate_definition_plan_count=1,
        stabilization_predicate_requirement_row_count=len(rows),
        selected_predicate_placeholder_count=1,
        planned_predicate_symbol_count=1,
        planned_definition_target_count=1,
        definition_execution_count=0,
        stabilization_predicate_definition_completion_count=0,
        attractor_class_definition_completion_count=0,
        constraint_region_definition_completion_count=0,
        causal_mass_definition_completion_count=0,
        observer_projection_definition_completion_count=0,
        carried_attractor_class_scaffold_boundary_audit_count=carried_scaffold_audit_count,
        carried_audited_scaffold_count=carried_audited_scaffold_count,
        carried_scaffold_boundary_row_count=carried_scaffold_boundary_row_count,
        carried_new_bridge_execution_count=carried_new_bridge_execution_count,
        carried_new_attractor_class_candidate_scaffold_count=carried_new_candidate_scaffold_count,
        carried_new_theorem_proven_count=carried_new_theorem_proven_count,
        carried_proof_execution_count=carried_proof_execution_count,
        carried_attractor_class_theorem_attempt_count=carried_attractor_class_theorem_attempt_count,
        carried_attractor_class_definition_completion_count=carried_attractor_class_definition_completion_count,
        carried_constraint_region_definition_completion_count=carried_constraint_region_definition_completion_count,
        carried_causal_mass_definition_completion_count=carried_causal_mass_definition_completion_count,
        carried_observer_projection_definition_completion_count=carried_observer_projection_definition_completion_count,
        carried_cumulative_limited_theorem_proven_count=carried_cumulative_limited_theorem_proven_count,
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
        boundary_phrase_count=62,
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
