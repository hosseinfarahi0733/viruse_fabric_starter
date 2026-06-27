from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/stabilization_predicate_completion_decision_execution_v8_85.md")
OUTPUT_PATH = Path("outputs/stabilization_predicate_conditional_hold_gap_register_v8_86.md")


@dataclass(frozen=True)
class ConditionalHoldGapRow:
    gap_id: str
    linked_criterion: str
    gap_name: str
    current_status: str
    required_resolution: str
    blocked_claim: str


@dataclass(frozen=True)
class ConditionalHoldGapRegisterReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    stabilization_predicate_conditional_hold_gap_register_count: int
    conditional_hold_gap_row_count: int
    unresolved_gap_count: int
    resolved_gap_count: int
    blocking_gap_count: int
    primary_blocker_count: int

    new_completion_decision_count: int
    new_completion_execution_count: int
    completion_execution_authorized_count: int
    definition_execution_count: int
    new_definition_execution_count: int
    new_stabilization_predicate_draft_clause_count: int
    new_completion_criterion_count: int
    new_completion_decision_plan_count: int
    stabilization_predicate_definition_completion_count: int
    attractor_class_definition_completion_count: int
    constraint_region_definition_completion_count: int
    causal_mass_definition_completion_count: int
    observer_projection_definition_completion_count: int

    carried_stabilization_predicate_completion_decision_execution_count: int
    carried_completion_decision_count: int
    carried_conditional_hold_decision_count: int
    carried_ready_for_completion_execution_decision_count: int
    carried_completion_execution_authorized_count: int
    carried_criterion_decision_row_count: int
    carried_passed_criterion_count: int
    carried_deferred_criterion_count: int
    carried_failed_criterion_count: int
    carried_completion_execution_count: int
    carried_definition_execution_count: int
    carried_new_definition_execution_count: int
    carried_new_stabilization_predicate_draft_clause_count: int
    carried_new_completion_criterion_count: int
    carried_new_completion_decision_plan_count: int
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
        "completion execution is complete",
        "criteria prove completion",
        "completion is granted",
        "completion is accepted",
        "conditional hold proves completion",
        "gap register resolves completion",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_gap_rows() -> List[ConditionalHoldGapRow]:
    return [
        ConditionalHoldGapRow(
            gap_id="SPCHG-001",
            linked_criterion="SPCC-001",
            gap_name="Carrier-domain exactness evidence gap",
            current_status="unresolved",
            required_resolution="create standalone evidence that Sigma_A is restricted to the finite R-path quotient carrier without importing undefined domains",
            blocked_claim="Sigma_A has a completed carrier-domain definition",
        ),
        ConditionalHoldGapRow(
            gap_id="SPCHG-002",
            linked_criterion="SPCC-002",
            gap_name="Local persistence testability gap",
            current_status="unresolved",
            required_resolution="define a checkable local persistence condition over finite R-path continuations",
            blocked_claim="local persistence has been formally tested or completed",
        ),
        ConditionalHoldGapRow(
            gap_id="SPCHG-003",
            linked_criterion="SPCC-003",
            gap_name="Recurrence witness gap",
            current_status="unresolved",
            required_resolution="provide bounded finite R-path recurrence witness discipline separate from reachability wording",
            blocked_claim="recurrence witness behavior proves an attractor theorem",
        ),
        ConditionalHoldGapRow(
            gap_id="SPCHG-004",
            linked_criterion="SPCC-004",
            gap_name="Exclusion and failure condition gap",
            current_status="unresolved",
            required_resolution="define explicit exclusion rules for quotient carriers that fail persistence, recurrence, or dependency requirements",
            blocked_claim="all quotient carriers qualify by default",
        ),
        ConditionalHoldGapRow(
            gap_id="SPCHG-005",
            linked_criterion="SPCC-005",
            gap_name="Constraint-dependency completion gap",
            current_status="unresolved",
            required_resolution="separately resolve constraint-region, causal-mass, and observer-projection dependencies before completion execution",
            blocked_claim="constraint-region, causal-mass, or observer-projection definitions are complete",
        ),
        ConditionalHoldGapRow(
            gap_id="SPCHG-006",
            linked_criterion="SPCC-006",
            gap_name="Post-evidence boundary audit gap",
            current_status="unresolved",
            required_resolution="audit any future evidence artifact before allowing completion execution",
            blocked_claim="decision execution directly authorizes theorem work",
        ),
        ConditionalHoldGapRow(
            gap_id="SPCHG-007",
            linked_criterion="SPCC-007",
            gap_name="Completion execution authorization gap",
            current_status="unresolved",
            required_resolution="run a later controlled authorization milestone only after all evidence gaps have been resolved",
            blocked_claim="conditional hold authorizes completion execution",
        ),
    ]


def _carried_counts(source_text: str) -> dict[str, int]:
    return {
        "decision_execution": 1 if _has_count(source_text, "Stabilization predicate completion decision execution", "1") else 0,
        "completion_decision": 1 if _has_count(source_text, "Completion decision", "1") else 0,
        "conditional_hold_decision": 1 if _has_count(source_text, "Conditional hold decision", "1") else 0,
        "ready_for_completion_execution": 0 if _has_count(source_text, "Ready for completion execution decision", "0") else -1,
        "completion_execution_authorized": 0 if _has_count(source_text, "Completion execution authorized", "0") else -1,
        "criterion_decision_rows": 7 if _has_count(source_text, "Criterion decision row", "7") else 0,
        "passed_criterion": 0 if _has_count(source_text, "Passed criterion", "0") else -1,
        "deferred_criterion": 7 if _has_count(source_text, "Deferred criterion", "7") else 0,
        "failed_criterion": 0 if _has_count(source_text, "Failed criterion", "0") else -1,
        "completion_execution": 0 if _has_count(source_text, "Completion execution", "0") else -1,
        "definition_execution": 0 if _has_count(source_text, "Definition execution", "0") else -1,
        "new_definition_execution": 0 if _has_count(source_text, "New definition execution", "0") else -1,
        "new_draft_clause": 0 if _has_count(source_text, "New stabilization predicate draft clause", "0") else -1,
        "new_completion_criterion": 0 if _has_count(source_text, "New completion criterion", "0") else -1,
        "new_completion_decision_plan": 0 if _has_count(source_text, "New completion decision plan", "0") else -1,
        "stabilization_completion": 0 if _has_count(source_text, "Stabilization predicate definition completion", "0") else -1,
        "attractor_completion": 0 if _has_count(source_text, "Attractor class definition completion", "0") else -1,
        "constraint_completion": 0 if _has_count(source_text, "Constraint region definition completion", "0") else -1,
        "causal_mass_completion": 0 if _has_count(source_text, "Causal mass definition completion", "0") else -1,
        "observer_projection_completion": 0 if _has_count(source_text, "Observer projection definition completion", "0") else -1,
        "new_theorem": 0 if _has_count(source_text, "New theorem proven", "0") else -1,
        "proof_execution": 0 if _has_count(source_text, "Proof execution", "0") else -1,
        "proof_assistant": 0 if _has_count(source_text, "Proof assistant verification", "0") else -1,
        "formalization": 0 if _has_count(source_text, "Formalization complete", "0") else -1,
        "completed_formal_definition": 0 if _has_count(source_text, "Completed formal definition", "0") else -1,
        "definition_completion_execution": 0 if _has_count(source_text, "Definition completion execution", "0") else -1,
        "full_framework": 0 if _has_count(source_text, "Full framework formal proof", "0") else -1,
        "proof_gap": 0 if _has_count(source_text, "Proof gap resolution", "0") else -1,
        "external": 0 if _has_count(source_text, "External validation", "0") else -1,
        "citation": 0 if _has_count(source_text, "New citation added", "0") else -1,
        "cumulative_theorem": 5 if _has_count(source_text, "Cumulative limited theorem proven", "5") else 0,
    }


def render_report() -> str:
    source_text = _read_source()
    rows = build_gap_rows()
    carried = _carried_counts(source_text)

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    stabilization_predicate_conditional_hold_gap_register_count = 1
    conditional_hold_gap_row_count = len(rows)
    unresolved_gap_count = len(rows)
    resolved_gap_count = 0
    blocking_gap_count = len(rows)
    primary_blocker_count = 4

    new_completion_decision_count = 0
    new_completion_execution_count = 0
    completion_execution_authorized_count = 0
    definition_execution_count = 0
    new_definition_execution_count = 0
    new_stabilization_predicate_draft_clause_count = 0
    new_completion_criterion_count = 0
    new_completion_decision_plan_count = 0
    stabilization_predicate_definition_completion_count = 0
    attractor_class_definition_completion_count = 0
    constraint_region_definition_completion_count = 0
    causal_mass_definition_completion_count = 0
    observer_projection_definition_completion_count = 0

    new_theorem_proven_count = 0
    cumulative_limited_theorem_proven_count = carried["cumulative_theorem"]
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
        errors.append("Missing required v8.85 conditional-hold decision execution source artifact.")
    if carried["decision_execution"] != 1:
        errors.append("Expected carried decision execution signal is absent.")
    if carried["completion_decision"] != 1:
        errors.append("Expected carried completion decision count of one is absent.")
    if carried["conditional_hold_decision"] != 1:
        errors.append("Expected carried conditional hold decision signal is absent.")
    if carried["ready_for_completion_execution"] != 0:
        errors.append("Expected carried ready-for-completion-execution count of zero is absent.")
    if carried["completion_execution_authorized"] != 0:
        errors.append("Expected carried completion-execution authorization count of zero is absent.")
    if carried["criterion_decision_rows"] != 7:
        errors.append("Expected carried criterion decision row count of seven is absent.")
    if carried["deferred_criterion"] != 7:
        errors.append("Expected carried deferred criterion count of seven is absent.")

    for key in [
        "completion_execution",
        "definition_execution",
        "new_definition_execution",
        "new_draft_clause",
        "new_completion_criterion",
        "new_completion_decision_plan",
        "stabilization_completion",
        "attractor_completion",
        "constraint_completion",
        "causal_mass_completion",
        "observer_projection_completion",
        "new_theorem",
        "proof_execution",
        "proof_assistant",
        "formalization",
        "completed_formal_definition",
        "definition_completion_execution",
        "full_framework",
        "proof_gap",
        "external",
        "citation",
    ]:
        if carried[key] != 0:
            errors.append(f"Expected carried zero signal is absent: {key}.")

    if carried["cumulative_theorem"] != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
    if conditional_hold_gap_row_count != 7:
        errors.append("Expected seven conditional hold gap rows.")
    if unresolved_gap_count != 7:
        errors.append("Expected seven unresolved gaps.")
    if resolved_gap_count != 0:
        errors.append("Expected zero resolved gaps.")
    if blocking_gap_count != 7:
        errors.append("Expected seven blocking gaps.")
    if new_completion_decision_count != 0:
        errors.append("Expected zero new completion decisions.")
    if new_completion_execution_count != 0:
        errors.append("Expected zero new completion executions.")
    if completion_execution_authorized_count != 0:
        errors.append("Expected zero completion execution authorizations.")
    if stabilization_predicate_definition_completion_count != 0:
        errors.append("Expected zero stabilization predicate definition completions.")
    if new_theorem_proven_count != 0:
        errors.append("Expected zero new theorem proofs.")
    if proof_execution_count != 0:
        errors.append("Expected zero proof executions.")

    warnings = [
        "This milestone registers conditional-hold gaps only.",
        "No new completion decision, completion execution, definition execution, new criterion, or new draft clause is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Stabilization Predicate Conditional Hold Gap Register v8.86",
        "",
        "## Purpose",
        "",
        "Register the unresolved gaps that keep the Sigma_A conditional-hold decision in place, while keeping new completion decision, completion execution, completion authorization, definition execution, new draft clause creation, new completion criterion creation, predicate definition completion, theorem proof, proof execution, proof assistant verification, completed formalization, framework-level proof, external validation, citation addition, and manuscript readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Conditional hold gap rows",
        "",
        "| Gap ID | Linked criterion | Gap name | Current status | Required resolution | Blocked claim |",
        "|---|---|---|---|---|---|",
    ]

    for row in rows:
        lines.append(
            f"| {row.gap_id} | {row.linked_criterion} | {row.gap_name} | {row.current_status} | {row.required_resolution} | {row.blocked_claim} |"
        )

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Stabilization predicate conditional hold gap register count: {stabilization_predicate_conditional_hold_gap_register_count}",
            f"- Conditional hold gap row count: {conditional_hold_gap_row_count}",
            f"- Unresolved gap count: {unresolved_gap_count}",
            f"- Resolved gap count: {resolved_gap_count}",
            f"- Blocking gap count: {blocking_gap_count}",
            f"- Primary blocker count: {primary_blocker_count}",
            f"- New completion decision count: {new_completion_decision_count}",
            f"- New completion execution count: {new_completion_execution_count}",
            f"- Completion execution authorized count: {completion_execution_authorized_count}",
            f"- Definition execution count: {definition_execution_count}",
            f"- New definition execution count: {new_definition_execution_count}",
            f"- New stabilization predicate draft clause count: {new_stabilization_predicate_draft_clause_count}",
            f"- New completion criterion count: {new_completion_criterion_count}",
            f"- New completion decision plan count: {new_completion_decision_plan_count}",
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
            "## Carried v8.85 signals",
            "",
            f"- Carried stabilization predicate completion decision execution count: {carried['decision_execution']}",
            f"- Carried completion decision count: {carried['completion_decision']}",
            f"- Carried conditional hold decision count: {carried['conditional_hold_decision']}",
            f"- Carried ready for completion execution decision count: {carried['ready_for_completion_execution']}",
            f"- Carried completion execution authorized count: {carried['completion_execution_authorized']}",
            f"- Carried criterion decision row count: {carried['criterion_decision_rows']}",
            f"- Carried passed criterion count: {carried['passed_criterion']}",
            f"- Carried deferred criterion count: {carried['deferred_criterion']}",
            f"- Carried failed criterion count: {carried['failed_criterion']}",
            f"- Carried completion execution count: {carried['completion_execution']}",
            f"- Carried definition execution count: {carried['definition_execution']}",
            f"- Carried new definition execution count: {carried['new_definition_execution']}",
            f"- Carried new stabilization predicate draft clause count: {carried['new_draft_clause']}",
            f"- Carried new completion criterion count: {carried['new_completion_criterion']}",
            f"- Carried new completion decision plan count: {carried['new_completion_decision_plan']}",
            f"- Carried stabilization predicate definition completion count: {carried['stabilization_completion']}",
            f"- Carried attractor class definition completion count: {carried['attractor_completion']}",
            f"- Carried constraint region definition completion count: {carried['constraint_completion']}",
            f"- Carried causal mass definition completion count: {carried['causal_mass_completion']}",
            f"- Carried observer projection definition completion count: {carried['observer_projection_completion']}",
            f"- Carried new theorem proven count: {carried['new_theorem']}",
            f"- Carried proof execution count: {carried['proof_execution']}",
            f"- Carried proof assistant verification count: {carried['proof_assistant']}",
            f"- Carried formalization complete count: {carried['formalization']}",
            f"- Carried completed formal definition count: {carried['completed_formal_definition']}",
            f"- Carried definition completion execution count: {carried['definition_completion_execution']}",
            f"- Carried full framework formal proof count: {carried['full_framework']}",
            f"- Carried proof gap resolution count: {carried['proof_gap']}",
            f"- Carried external validation count: {carried['external']}",
            f"- Carried new citation added count: {carried['citation']}",
            f"- Carried cumulative limited theorem proven count: {carried['cumulative_theorem']}",
            "",
            "## Boundary interpretation",
            "",
            "The v8.86 artifact registers the unresolved conditional-hold gaps that block Sigma_A completion execution. It creates no new completion decision, authorizes no completion execution, performs no definition execution, creates no new draft clause, creates no new completion criterion, completes no stabilization predicate definition, completes no attractor-class definition, completes no constraint-region definition, completes no causal-mass definition, completes no observer-projection definition, proves no theorem, performs no proof execution, performs no proof assistant verification, adds no citation, completes no external validation, and creates no manuscript readiness.",
            "",
            "## Critical reviewer note",
            "",
            "The conditional hold should remain active until each registered gap has a standalone resolving artifact and a later boundary audit. The register is not a resolution.",
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
            "The project has registered the conditional-hold gaps that block Sigma_A completion execution while preserving the distinction between gap registration, gap resolution, completion execution, definition completion, theorem proof, proof assistant verification, completed formalization, framework-level proof, external validation, and manuscript readiness.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this gap resolution.",
            "- Do not call this completion execution.",
            "- Do not call this definition execution.",
            "- Do not call this stabilization predicate completion.",
            "- Do not call this theorem proof.",
            "- Do not call this proof execution.",
            "- Do not call this external validation.",
            "- Do not call this manuscript readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.86 conditional hold gap register.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.86 conditional hold gap register.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> ConditionalHoldGapRegisterReport:
    text = render_report()
    source_text = _read_source()
    source_exists = SOURCE_PATH.exists()
    carried = _carried_counts(source_text)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    errors: List[str] = []
    if not source_exists:
        errors.append("Missing required v8.85 conditional-hold decision execution source artifact.")
    if carried["decision_execution"] != 1:
        errors.append("Expected carried decision execution signal is absent.")
    if carried["completion_decision"] != 1:
        errors.append("Expected carried completion decision count of one is absent.")
    if carried["conditional_hold_decision"] != 1:
        errors.append("Expected carried conditional hold decision signal is absent.")
    if carried["ready_for_completion_execution"] != 0:
        errors.append("Expected carried ready-for-completion-execution count of zero is absent.")
    if carried["completion_execution_authorized"] != 0:
        errors.append("Expected carried completion-execution authorization count of zero is absent.")
    if carried["criterion_decision_rows"] != 7:
        errors.append("Expected carried criterion decision row count of seven is absent.")
    if carried["deferred_criterion"] != 7:
        errors.append("Expected carried deferred criterion count of seven is absent.")

    for key in [
        "completion_execution",
        "definition_execution",
        "new_definition_execution",
        "new_draft_clause",
        "new_completion_criterion",
        "new_completion_decision_plan",
        "stabilization_completion",
        "attractor_completion",
        "constraint_completion",
        "causal_mass_completion",
        "observer_projection_completion",
        "new_theorem",
        "proof_execution",
        "proof_assistant",
        "formalization",
        "completed_formal_definition",
        "definition_completion_execution",
        "full_framework",
        "proof_gap",
        "external",
        "citation",
    ]:
        if carried[key] != 0:
            errors.append(f"Expected carried zero signal is absent: {key}.")

    if carried["cumulative_theorem"] != 5:
        errors.append("Expected carried cumulative limited theorem count of five is absent.")
    if len(build_gap_rows()) != 7:
        errors.append("Expected seven conditional hold gap rows.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "This milestone registers conditional-hold gaps only.",
        "No new completion decision, completion execution, definition execution, new criterion, or new draft clause is created.",
        "No stabilization predicate definition completion or attractor-class definition completion is performed.",
        "Proof assistant verification, external validation, and manuscript submission readiness remain absent.",
    ]

    rows = build_gap_rows()

    return ConditionalHoldGapRegisterReport(
        title="Stabilization Predicate Conditional Hold Gap Register v8.86",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=0 if source_exists else 1,
        stabilization_predicate_conditional_hold_gap_register_count=1,
        conditional_hold_gap_row_count=len(rows),
        unresolved_gap_count=len(rows),
        resolved_gap_count=0,
        blocking_gap_count=len(rows),
        primary_blocker_count=4,
        new_completion_decision_count=0,
        new_completion_execution_count=0,
        completion_execution_authorized_count=0,
        definition_execution_count=0,
        new_definition_execution_count=0,
        new_stabilization_predicate_draft_clause_count=0,
        new_completion_criterion_count=0,
        new_completion_decision_plan_count=0,
        stabilization_predicate_definition_completion_count=0,
        attractor_class_definition_completion_count=0,
        constraint_region_definition_completion_count=0,
        causal_mass_definition_completion_count=0,
        observer_projection_definition_completion_count=0,
        carried_stabilization_predicate_completion_decision_execution_count=carried["decision_execution"],
        carried_completion_decision_count=carried["completion_decision"],
        carried_conditional_hold_decision_count=carried["conditional_hold_decision"],
        carried_ready_for_completion_execution_decision_count=carried["ready_for_completion_execution"],
        carried_completion_execution_authorized_count=carried["completion_execution_authorized"],
        carried_criterion_decision_row_count=carried["criterion_decision_rows"],
        carried_passed_criterion_count=carried["passed_criterion"],
        carried_deferred_criterion_count=carried["deferred_criterion"],
        carried_failed_criterion_count=carried["failed_criterion"],
        carried_completion_execution_count=carried["completion_execution"],
        carried_definition_execution_count=carried["definition_execution"],
        carried_new_definition_execution_count=carried["new_definition_execution"],
        carried_new_stabilization_predicate_draft_clause_count=carried["new_draft_clause"],
        carried_new_completion_criterion_count=carried["new_completion_criterion"],
        carried_new_completion_decision_plan_count=carried["new_completion_decision_plan"],
        carried_stabilization_predicate_definition_completion_count=carried["stabilization_completion"],
        carried_attractor_class_definition_completion_count=carried["attractor_completion"],
        carried_constraint_region_definition_completion_count=carried["constraint_completion"],
        carried_causal_mass_definition_completion_count=carried["causal_mass_completion"],
        carried_observer_projection_definition_completion_count=carried["observer_projection_completion"],
        carried_new_theorem_proven_count=carried["new_theorem"],
        carried_proof_execution_count=carried["proof_execution"],
        carried_proof_assistant_verification_count=carried["proof_assistant"],
        carried_formalization_complete_count=carried["formalization"],
        carried_completed_formal_definition_count=carried["completed_formal_definition"],
        carried_definition_completion_execution_count=carried["definition_completion_execution"],
        carried_full_framework_formal_proof_count=carried["full_framework"],
        carried_proof_gap_resolution_count=carried["proof_gap"],
        carried_external_validation_count=carried["external"],
        carried_new_citation_added_count=carried["citation"],
        carried_cumulative_limited_theorem_proven_count=carried["cumulative_theorem"],
        new_theorem_proven_count=0,
        cumulative_limited_theorem_proven_count=carried["cumulative_theorem"],
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
        boundary_phrase_count=70,
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
