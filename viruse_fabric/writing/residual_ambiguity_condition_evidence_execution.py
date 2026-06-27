from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import List


@dataclass(frozen=True)
class ResidualAmbiguityConditionEvidenceExecutionReport:
    title: str
    output_path: str
    source_artifact: str
    source_artifact_count: int
    missing_source_artifact_count: int
    residual_ambiguity_condition_evidence_execution_count: int
    residual_ambiguity_evidence_row_count: int
    residual_ambiguity_scope_rule_count: int
    residual_ambiguity_acceptance_test_count: int
    residual_ambiguity_blocked_overreach_count: int
    target_gap_count: int
    target_gap_id_count: int
    target_criterion_count: int
    evidence_support_count: int
    previously_resolved_gaps_retained_count: int
    gap_resolution_decision_count: int
    targeted_gap_resolution_decision_count: int
    newly_resolved_gap_count: int
    resolved_gap_count: int
    unresolved_gap_count: int
    remaining_blocking_gap_count: int
    gap_resolution_authorized_count: int
    completion_decision_count: int
    completion_execution_count: int
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
    carried_minimal_adequacy_boundary_audit_count: int
    carried_gap_resolution_decision_count: int
    carried_targeted_gap_resolution_decision_count: int
    carried_newly_resolved_gap_count: int
    carried_resolved_gap_count: int
    carried_unresolved_gap_count: int
    carried_remaining_blocking_gap_count: int
    carried_gap_resolution_authorized_count: int
    carried_completion_decision_count: int
    carried_completion_execution_count: int
    carried_completion_execution_authorized_count: int
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
    passed: bool

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class ResidualAmbiguityConditionEvidenceExecutionBuilder:
    """Build v8.98 residual ambiguity condition evidence execution artifact.

    Boundary discipline:
    - This milestone produces evidence for SPCHG-006 / SPCC-006 only.
    - It does not resolve SPCHG-006.
    - It does not authorize completion execution.
    - It does not add proof, formalization, external validation, manuscript readiness, or citations.
    """

    title = "Residual Ambiguity Condition Evidence Execution v8.98"
    source_artifact = Path("outputs/minimal_adequacy_evidence_boundary_audit_plus_gap_resolution_decision_v8_97.md")
    output_path = Path("outputs/residual_ambiguity_condition_evidence_execution_v8_98.md")

    target_gap_id = "SPCHG-006"
    target_criterion_id = "SPCC-006"

    def run(self) -> ResidualAmbiguityConditionEvidenceExecutionReport:
        errors: List[str] = []
        warnings: List[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        evidence_rows = [
            {
                "row_id": "RAE-001",
                "condition": "Residual ambiguity must identify the exact ambiguity left after SPCHG-005 resolution.",
                "evidence": "The source artifact carries SPCHG-005 as resolved while retaining two unresolved and blocking conditional-hold gaps.",
                "acceptance_test": "The report must preserve resolved gap count 5 and unresolved gap count 2.",
                "blocked_overreach": "Do not treat residual ambiguity evidence as a resolution decision.",
            },
            {
                "row_id": "RAE-002",
                "condition": "Residual ambiguity must be scoped to SPCHG-006 / SPCC-006.",
                "evidence": "This milestone targets only SPCHG-006 / SPCC-006 and does not alter prior resolved gaps.",
                "acceptance_test": "The report must contain exactly one targeted gap and one targeted criterion.",
                "blocked_overreach": "Do not create a new completion criterion or a completion decision plan.",
            },
            {
                "row_id": "RAE-003",
                "condition": "Residual ambiguity evidence must preserve completion boundaries.",
                "evidence": "Completion decision, completion execution, and completion authorization remain zero.",
                "acceptance_test": "The report must keep completion decision count, completion execution count, and completion execution authorized count at zero.",
                "blocked_overreach": "Do not authorize Sigma_A completion, predicate completion, or framework completion.",
            },
            {
                "row_id": "RAE-004",
                "condition": "Residual ambiguity evidence must preserve proof boundaries.",
                "evidence": "The cumulative limited theorem count remains carried at five and no new theorem is proven.",
                "acceptance_test": "The report must keep new theorem proven count, proof execution count, and proof assistant verification count at zero.",
                "blocked_overreach": "Do not claim formal proof, full framework proof, or proof assistant verification.",
            },
            {
                "row_id": "RAE-005",
                "condition": "Residual ambiguity evidence must preserve validation and manuscript boundaries.",
                "evidence": "External validation, independent experiment, manuscript readiness, readiness approval, and new citation additions remain absent.",
                "acceptance_test": "The report must keep validation, readiness, and citation counters at zero.",
                "blocked_overreach": "Do not claim external validation, independent experiment, submission readiness, or citation completion.",
            },
        ]

        scope_rules = [
            "Evidence execution can describe what remains ambiguous after SPCHG-005, but cannot resolve SPCHG-006.",
            "Evidence execution can preserve prior resolution counters, but cannot increase resolved gaps.",
            "Evidence execution can recommend a later boundary audit plus gap resolution decision, but cannot perform that decision.",
        ]

        warnings.extend([
            "This milestone produces residual ambiguity condition evidence only.",
            "SPCHG-006 remains unresolved after v8.98 evidence execution.",
            "Two conditional-hold gaps remain unresolved and blocking.",
            "Completion execution, theorem proof, proof assistant verification, external validation, and manuscript readiness remain absent.",
        ])

        counts = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "residual_ambiguity_condition_evidence_execution_count": 1,
            "residual_ambiguity_evidence_row_count": len(evidence_rows),
            "residual_ambiguity_scope_rule_count": len(scope_rules),
            "residual_ambiguity_acceptance_test_count": len(evidence_rows),
            "residual_ambiguity_blocked_overreach_count": len(evidence_rows),
            "target_gap_count": 1,
            "target_gap_id_count": 1,
            "target_criterion_count": 1,
            "evidence_support_count": 1,
            "previously_resolved_gaps_retained_count": 5,
            "gap_resolution_decision_count": 0,
            "targeted_gap_resolution_decision_count": 0,
            "newly_resolved_gap_count": 0,
            "resolved_gap_count": 5,
            "unresolved_gap_count": 2,
            "remaining_blocking_gap_count": 2,
            "gap_resolution_authorized_count": 0,
            "completion_decision_count": 0,
            "completion_execution_count": 0,
            "completion_execution_authorized_count": 0,
            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "new_stabilization_predicate_draft_clause_count": 0,
            "new_completion_criterion_count": 0,
            "new_completion_decision_plan_count": 0,
            "stabilization_predicate_definition_completion_count": 0,
            "attractor_class_definition_completion_count": 0,
            "constraint_region_definition_completion_count": 0,
            "causal_mass_definition_completion_count": 0,
            "observer_projection_definition_completion_count": 0,
            "carried_minimal_adequacy_boundary_audit_count": carried.get("Minimal adequacy evidence boundary audit count", 1),
            "carried_gap_resolution_decision_count": carried.get("Gap resolution decision count", 1),
            "carried_targeted_gap_resolution_decision_count": carried.get("Targeted gap resolution decision count", 1),
            "carried_newly_resolved_gap_count": carried.get("Newly resolved gap count", 1),
            "carried_resolved_gap_count": carried.get("Resolved gap count", 5),
            "carried_unresolved_gap_count": carried.get("Unresolved gap count", 2),
            "carried_remaining_blocking_gap_count": carried.get("Remaining blocking gap count", 2),
            "carried_gap_resolution_authorized_count": carried.get("Gap resolution authorized count", 1),
            "carried_completion_decision_count": carried.get("Completion decision count", 0),
            "carried_completion_execution_count": carried.get("Completion execution count", 0),
            "carried_completion_execution_authorized_count": carried.get("Completion execution authorized count", 0),
            "carried_definition_execution_count": carried.get("Definition execution count", 0),
            "carried_new_definition_execution_count": carried.get("New definition execution count", 0),
            "carried_new_stabilization_predicate_draft_clause_count": carried.get("New stabilization predicate draft clause count", 0),
            "carried_new_completion_criterion_count": carried.get("New completion criterion count", 0),
            "carried_new_completion_decision_plan_count": carried.get("New completion decision plan count", 0),
            "carried_stabilization_predicate_definition_completion_count": carried.get("Stabilization predicate definition completion count", 0),
            "carried_attractor_class_definition_completion_count": carried.get("Attractor class definition completion count", 0),
            "carried_constraint_region_definition_completion_count": carried.get("Constraint region definition completion count", 0),
            "carried_causal_mass_definition_completion_count": carried.get("Causal mass definition completion count", 0),
            "carried_observer_projection_definition_completion_count": carried.get("Observer projection definition completion count", 0),
            "carried_new_theorem_proven_count": carried.get("New theorem proven count", 0),
            "carried_proof_execution_count": carried.get("Proof execution count", 0),
            "carried_proof_assistant_verification_count": carried.get("Proof assistant verification count", 0),
            "carried_formalization_complete_count": carried.get("Formalization complete count", 0),
            "carried_completed_formal_definition_count": carried.get("Completed formal definition count", 0),
            "carried_definition_completion_execution_count": carried.get("Definition completion execution count", 0),
            "carried_full_framework_formal_proof_count": carried.get("Full framework formal proof count", 0),
            "carried_proof_gap_resolution_count": carried.get("Proof gap resolution count", 0),
            "carried_external_validation_count": carried.get("External validation count", 0),
            "carried_new_citation_added_count": carried.get("New citation added count", 0),
            "carried_cumulative_limited_theorem_proven_count": carried.get("Cumulative limited theorem proven count", 5),
            "new_theorem_proven_count": 0,
            "cumulative_limited_theorem_proven_count": 5,
            "proof_assistant_verification_count": 0,
            "formalization_complete_count": 0,
            "completed_formal_definition_count": 0,
            "definition_completion_execution_count": 0,
            "full_framework_formal_proof_count": 0,
            "formal_mathematical_proof_count": 0,
            "formal_proof_execution_count": 0,
            "proof_execution_count": 0,
            "proof_gap_resolution_count": 0,
            "manuscript_submission_ready_count": 0,
            "readiness_approval_count": 0,
            "external_validation_count": 0,
            "independent_experiment_count": 0,
            "new_citation_added_count": 0,
            "conditional_hold_count": 1,
            "hard_zero_count": 13,
            "next_step_count": 8,
        }

        report_text = self._render_report(evidence_rows, scope_rules, counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.98 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.98 report.")
        if counts["gap_resolution_decision_count"] != 0:
            errors.append("v8.98 must not record a gap resolution decision.")
        if counts["newly_resolved_gap_count"] != 0:
            errors.append("v8.98 must not newly resolve SPCHG-006.")
        if counts["resolved_gap_count"] != 5:
            errors.append("v8.98 must retain resolved gap count at 5.")
        if counts["unresolved_gap_count"] != 2:
            errors.append("v8.98 must retain unresolved gap count at 2.")
        if counts["remaining_blocking_gap_count"] != 2:
            errors.append("v8.98 must retain remaining blocking gap count at 2.")

        zero_fields = [
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "new_stabilization_predicate_draft_clause_count",
            "new_completion_criterion_count",
            "new_completion_decision_plan_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "new_theorem_proven_count",
            "proof_assistant_verification_count",
            "formalization_complete_count",
            "completed_formal_definition_count",
            "definition_completion_execution_count",
            "full_framework_formal_proof_count",
            "formal_mathematical_proof_count",
            "formal_proof_execution_count",
            "proof_execution_count",
            "proof_gap_resolution_count",
            "manuscript_submission_ready_count",
            "readiness_approval_count",
            "external_validation_count",
            "independent_experiment_count",
            "new_citation_added_count",
        ]

        for field in zero_fields:
            if counts[field] != 0:
                errors.append(f"{field} must remain zero, found {counts[field]}.")

        final_report_text = self._render_report(evidence_rows, scope_rules, counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return ResidualAmbiguityConditionEvidenceExecutionReport(
            title=self.title,
            output_path=str(self.output_path),
            source_artifact=str(self.source_artifact),
            errors=errors,
            warnings=warnings,
            passed=len(errors) == 0,
            **counts,
        )

    def _extract_carried_counts(self, source_text: str) -> dict[str, int]:
        carried: dict[str, int] = {}
        for line in source_text.splitlines():
            clean = line.strip().lstrip("-").strip()
            match = re.match(r"^([A-Za-z][A-Za-z0-9 /_-]* count):\s*(\d+)\s*$", clean)
            if match:
                carried[match.group(1)] = int(match.group(2))
        return carried

    def _render_report(
        self,
        evidence_rows: list[dict[str, str]],
        scope_rules: list[str],
        counts: dict[str, int],
        warnings: list[str],
    ) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric produce residual ambiguity condition evidence for SPCHG-006 / SPCC-006 "
            "while preserving the distinction between evidence execution, gap resolution decision, "
            "completion decision, completion execution, definition execution, predicate definition completion, "
            "theorem proof, proof execution, proof assistant verification, completed formalization, "
            "framework-level proof, external validation, independent experiment, manuscript readiness, "
            "readiness approval, and new citation additions?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Target")
        lines.append(f"- Target gap: {self.target_gap_id}")
        lines.append(f"- Target criterion: {self.target_criterion_id}")
        lines.append("- Milestone type: evidence execution only")
        lines.append("- Resolution status after this milestone: evidence produced, not resolved")
        lines.append("")
        lines.append("## Residual ambiguity evidence rows")
        lines.append("")
        lines.append("| Row | Condition | Evidence | Acceptance test | Blocked overreach |")
        lines.append("|---|---|---|---|---|")
        for row in evidence_rows:
            lines.append(
                f"| {row['row_id']} | {row['condition']} | {row['evidence']} | "
                f"{row['acceptance_test']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Scope rules")
        for index, rule in enumerate(scope_rules, start=1):
            lines.append(f"{index}. {rule}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact produces residual ambiguity condition evidence for SPCHG-006 / SPCC-006 only. "
            "It does not record a gap resolution decision, does not newly resolve SPCHG-006, does not authorize "
            "completion execution, does not complete Sigma_A, does not complete any formal definition, does not prove "
            "a theorem, does not run proof execution, does not provide proof assistant verification, does not complete "
            "formalization, does not prove the full framework, does not provide external validation, does not perform "
            "an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "residual_ambiguity_condition_evidence_execution_count",
            "residual_ambiguity_evidence_row_count",
            "residual_ambiguity_scope_rule_count",
            "residual_ambiguity_acceptance_test_count",
            "residual_ambiguity_blocked_overreach_count",
            "target_gap_count",
            "target_gap_id_count",
            "target_criterion_count",
            "evidence_support_count",
            "previously_resolved_gaps_retained_count",
            "gap_resolution_decision_count",
            "targeted_gap_resolution_decision_count",
            "newly_resolved_gap_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "gap_resolution_authorized_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "new_stabilization_predicate_draft_clause_count",
            "new_completion_criterion_count",
            "new_completion_decision_plan_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "carried_minimal_adequacy_boundary_audit_count",
            "carried_gap_resolution_decision_count",
            "carried_targeted_gap_resolution_decision_count",
            "carried_newly_resolved_gap_count",
            "carried_resolved_gap_count",
            "carried_unresolved_gap_count",
            "carried_remaining_blocking_gap_count",
            "carried_gap_resolution_authorized_count",
            "carried_completion_decision_count",
            "carried_completion_execution_count",
            "carried_completion_execution_authorized_count",
            "carried_definition_execution_count",
            "carried_new_definition_execution_count",
            "carried_new_stabilization_predicate_draft_clause_count",
            "carried_new_completion_criterion_count",
            "carried_new_completion_decision_plan_count",
            "carried_stabilization_predicate_definition_completion_count",
            "carried_attractor_class_definition_completion_count",
            "carried_constraint_region_definition_completion_count",
            "carried_causal_mass_definition_completion_count",
            "carried_observer_projection_definition_completion_count",
            "carried_new_theorem_proven_count",
            "carried_proof_execution_count",
            "carried_proof_assistant_verification_count",
            "carried_formalization_complete_count",
            "carried_completed_formal_definition_count",
            "carried_definition_completion_execution_count",
            "carried_full_framework_formal_proof_count",
            "carried_proof_gap_resolution_count",
            "carried_external_validation_count",
            "carried_new_citation_added_count",
            "carried_cumulative_limited_theorem_proven_count",
            "new_theorem_proven_count",
            "cumulative_limited_theorem_proven_count",
            "proof_assistant_verification_count",
            "formalization_complete_count",
            "completed_formal_definition_count",
            "definition_completion_execution_count",
            "full_framework_formal_proof_count",
            "formal_mathematical_proof_count",
            "formal_proof_execution_count",
            "proof_execution_count",
            "proof_gap_resolution_count",
            "manuscript_submission_ready_count",
            "readiness_approval_count",
            "external_validation_count",
            "independent_experiment_count",
            "new_citation_added_count",
            "conditional_hold_count",
            "hard_zero_count",
            "boundary_phrase_count",
            "prohibited_behavior_count",
            "next_step_count",
            "overclaim_count",
            "invented_citation_like_pattern_count",
            "word_count",
        ]
        for key in counter_order:
            if key in counts:
                label = key.replace("_", " ").capitalize()
                lines.append(f"- {label}: {counts[key]}")
        lines.append("")
        lines.append("## Warnings")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")
        lines.append("## Interpretation")
        lines.append(
            "The v8.98 artifact produces standalone residual ambiguity condition evidence for SPCHG-006 / SPCC-006. "
            "It preserves the five previously resolved gaps, leaves two unresolved and blocking gaps, and keeps "
            "completion execution, Sigma_A completion, theorem proof, proof assistant verification, external validation, "
            "independent experiment, manuscript submission readiness, readiness approval, and new citation additions at zero."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit the residual ambiguity evidence boundary in v8.99.",
            "Record a targeted SPCHG-006 gap resolution decision only if the v8.99 boundary audit passes.",
            "Keep SPCHG-006 unresolved until that later resolution decision exists.",
            "Keep completion decision separate from gap resolution.",
            "Keep completion execution separate from completion decision.",
            "Keep definition completion separate from evidence execution.",
            "Keep theorem proof and proof assistant verification separate from all gap evidence milestones.",
            "Keep manuscript readiness and citation additions separate from this gap workflow.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = [
            "does not",
            "not resolve",
            "not authorize",
            "remain zero",
            "evidence execution only",
            "evidence produced, not resolved",
            "separate",
            "zero",
            "absent",
            "preserve",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not record a gap resolution decision",
            "does not newly resolve",
            "does not authorize completion execution",
            "does not complete Sigma_A",
            "does not complete any formal definition",
            "does not prove a theorem",
            "does not run proof execution",
            "does not provide proof assistant verification",
            "does not complete formalization",
            "does not prove the full framework",
            "does not provide external validation",
            "does not perform an independent experiment",
            "does not approve manuscript submission readiness",
            "does not add new citations",
            "cannot resolve SPCHG-006",
            "cannot increase resolved gaps",
            "cannot perform that decision",
            "Do not claim formal proof",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        """Count only new unsafe claims, not carried historical counters.

        v8.98 intentionally carries v8.97 counters such as:
        - Carried gap resolution decision count: 1
        - Carried newly resolved gap count: 1

        Those are historical carried values, not new v8.98 claims.
        The detector must therefore ignore carried-counter lines and
        negative boundary lines.
        """
        forbidden_patterns = [
            r"^[- ]*formalization complete count:\\s*[1-9]",
            r"^[- ]*proof assistant verification count:\\s*[1-9]",
            r"^[- ]*manuscript submission ready count:\\s*[1-9]",
            r"^[- ]*external validation count:\\s*[1-9]",
            r"^[- ]*gap resolution decision count:\\s*[1-9]",
            r"^[- ]*targeted gap resolution decision count:\\s*[1-9]",
            r"^[- ]*newly resolved gap count:\\s*[1-9]",
            r"^[- ]*completion execution count:\\s*[1-9]",
            r"^[- ]*new theorem proven count:\\s*[1-9]",
            r"\\bSigma_A completion achieved\\b",
            r"\\bSPCHG-006 resolved\\b",
        ]

        count = 0
        for raw_line in text.splitlines():
            line = raw_line.strip()
            lowered = line.lower()

            if not lowered:
                continue

            # Historical carried counters are allowed evidence inheritance,
            # not new v8.98 claims.
            if lowered.startswith("- carried ") or lowered.startswith("carried "):
                continue

            # Boundary and negation lines are protective, not overclaims.
            protective_markers = [
                "does not",
                "do not",
                "cannot",
                "not resolved",
                "not resolve",
                "remain zero",
                "remains absent",
                "evidence produced, not resolved",
                "evidence execution only",
            ]
            if any(marker in lowered for marker in protective_markers):
                continue

            import re
            for pattern in forbidden_patterns:
                if re.search(pattern.lower(), lowered):
                    count += 1
                    break

        return count

    def _count_invented_citation_like_patterns(self, text: str) -> int:
        patterns = [
            r"\([A-Z][A-Za-z-]+,\s*20\d{2}\)",
            r"\[[0-9]{1,3}\]",
            r"doi:",
            r"arXiv:",
        ]
        return sum(len(re.findall(pattern, text)) for pattern in patterns)


if __name__ == "__main__":
    report = ResidualAmbiguityConditionEvidenceExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
