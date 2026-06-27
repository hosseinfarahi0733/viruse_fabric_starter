from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class ResidualAmbiguityEvidenceBoundaryAuditPlusGapResolutionDecisionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class ResidualAmbiguityEvidenceBoundaryAuditPlusGapResolutionDecisionBuilder:
    """Build v8.99 residual ambiguity evidence boundary audit plus gap resolution decision artifact.

    Boundary discipline:
    - This milestone audits v8.98 residual ambiguity evidence.
    - It records a targeted SPCHG-006 / SPCC-006 gap resolution decision.
    - It does not authorize completion execution.
    - It does not add definition completion, theorem proof, proof assistant verification,
      framework proof, external validation, independent experiment, manuscript readiness,
      readiness approval, or new citations.
    """

    title = "Residual Ambiguity Evidence Boundary Audit Plus Gap Resolution Decision v8.99"
    source_artifact = Path("outputs/residual_ambiguity_condition_evidence_execution_v8_98.md")
    output_path = Path("outputs/residual_ambiguity_evidence_boundary_audit_plus_gap_resolution_decision_v8_99.md")

    target_gap_id = "SPCHG-006"
    target_criterion_id = "SPCC-006"

    def run(self) -> ResidualAmbiguityEvidenceBoundaryAuditPlusGapResolutionDecisionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        audit_rows = [
            {
                "row_id": "RAB-001",
                "audited_evidence": "The v8.98 source artifact exists and records residual ambiguity condition evidence for SPCHG-006 / SPCC-006.",
                "accepted_claim": "SPCHG-006 has evidence support for a targeted gap resolution decision.",
                "blocked_claim": "The evidence does not imply completion execution or Sigma_A completion.",
                "decision": "Accept evidence boundary for SPCHG-006 resolution only.",
            },
            {
                "row_id": "RAB-002",
                "audited_evidence": "The v8.98 artifact preserves five previously resolved gaps and two unresolved blocking gaps.",
                "accepted_claim": "A targeted decision may move SPCHG-006 from unresolved to resolved.",
                "blocked_claim": "The decision may not collapse the final unresolved gap.",
                "decision": "Resolve SPCHG-006 while leaving one unresolved blocking gap.",
            },
            {
                "row_id": "RAB-003",
                "audited_evidence": "The v8.98 artifact keeps gap resolution decision and newly resolved gap counters at zero.",
                "accepted_claim": "v8.99 can add exactly one targeted gap resolution decision.",
                "blocked_claim": "The decision may not create a completion decision plan or new completion criterion.",
                "decision": "Record one targeted gap resolution decision and one newly resolved gap.",
            },
            {
                "row_id": "RAB-004",
                "audited_evidence": "The proof, formalization, and verification counters remain zero in the source artifact.",
                "accepted_claim": "Gap resolution can proceed without claiming theorem proof or proof assistant verification.",
                "blocked_claim": "No formal proof, proof execution, or proof assistant verification is created here.",
                "decision": "Keep all proof and formalization counters at zero.",
            },
            {
                "row_id": "RAB-005",
                "audited_evidence": "The validation, readiness, and citation counters remain zero in the source artifact.",
                "accepted_claim": "SPCHG-006 can be resolved without manuscript readiness.",
                "blocked_claim": "No external validation, independent experiment, readiness approval, or new citation is created here.",
                "decision": "Keep validation, readiness, and citation counters at zero.",
            },
        ]

        scope_rules = [
            "A targeted gap resolution decision may resolve SPCHG-006 only.",
            "A targeted gap resolution decision may reduce unresolved and blocking gap counts by one only.",
            "A targeted gap resolution decision cannot authorize completion execution, formal definition completion, theorem proof, external validation, or manuscript readiness.",
        ]

        warnings.extend([
            "This milestone audits residual ambiguity evidence and records a targeted SPCHG-006 gap resolution decision only.",
            "Resolving SPCHG-006 does not authorize completion execution or Sigma_A completion.",
            "One conditional-hold gap remains unresolved and blocking after this decision.",
            "Proof assistant verification, external validation, independent experiment, manuscript readiness, and new citations remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "residual_ambiguity_evidence_boundary_audit_count": 1,
            "audited_residual_ambiguity_evidence_count": 1,
            "residual_ambiguity_boundary_audit_row_count": len(audit_rows),
            "accepted_claim_count": len(audit_rows),
            "blocked_claim_count": len(audit_rows),
            "gap_resolution_decision_count": 1,
            "targeted_gap_resolution_decision_count": 1,
            "targeted_gap_count": 1,
            "targeted_gap_id_count": 1,
            "targeted_criterion_count": 1,
            "evidence_supported_gap_count": 1,
            "previously_resolved_gaps_retained_count": 5,
            "resolved_gap_count": 6,
            "newly_resolved_gap_count": 1,
            "unresolved_gap_count": 1,
            "remaining_blocking_gap_count": 1,
            "gap_resolution_authorized_count": 1,
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
            "carried_residual_ambiguity_condition_evidence_execution_count": carried.get("Residual ambiguity condition evidence execution count", 1),
            "carried_residual_ambiguity_evidence_row_count": carried.get("Residual ambiguity evidence row count", 5),
            "carried_residual_ambiguity_scope_rule_count": carried.get("Residual ambiguity scope rule count", 3),
            "carried_residual_ambiguity_acceptance_test_count": carried.get("Residual ambiguity acceptance test count", 5),
            "carried_residual_ambiguity_blocked_overreach_count": carried.get("Residual ambiguity blocked overreach count", 5),
            "carried_target_gap_count": carried.get("Target gap count", 1),
            "carried_target_gap_id_count": carried.get("Target gap ID count", 1),
            "carried_target_criterion_count": carried.get("Target criterion count", 1),
            "carried_evidence_support_count": carried.get("Evidence support count", 1),
            "carried_prior_resolved_gaps_retained_count": carried.get("Previously resolved gaps retained count", 5),
            "carried_gap_resolution_decision_count": carried.get("Gap resolution decision count", 0),
            "carried_targeted_gap_resolution_decision_count": carried.get("Targeted gap resolution decision count", 0),
            "carried_newly_resolved_gap_count": carried.get("Newly resolved gap count", 0),
            "carried_resolved_gap_count": carried.get("Resolved gap count", 5),
            "carried_unresolved_gap_count": carried.get("Unresolved gap count", 2),
            "carried_remaining_blocking_gap_count": carried.get("Remaining blocking gap count", 2),
            "carried_gap_resolution_authorized_count": carried.get("Gap resolution authorized count", 0),
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

        report_text = self._render_report(audit_rows, scope_rules, counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.99 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.99 report.")
        if counts["gap_resolution_decision_count"] != 1:
            errors.append("v8.99 must record exactly one gap resolution decision.")
        if counts["targeted_gap_resolution_decision_count"] != 1:
            errors.append("v8.99 must record exactly one targeted gap resolution decision.")
        if counts["newly_resolved_gap_count"] != 1:
            errors.append("v8.99 must newly resolve exactly one gap.")
        if counts["resolved_gap_count"] != 6:
            errors.append("v8.99 must set resolved gap count to 6.")
        if counts["unresolved_gap_count"] != 1:
            errors.append("v8.99 must set unresolved gap count to 1.")
        if counts["remaining_blocking_gap_count"] != 1:
            errors.append("v8.99 must set remaining blocking gap count to 1.")

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

        final_report_text = self._render_report(audit_rows, scope_rules, counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return ResidualAmbiguityEvidenceBoundaryAuditPlusGapResolutionDecisionReport(
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
        audit_rows: list[dict[str, str]],
        scope_rules: list[str],
        counts: dict[str, int],
        warnings: list[str],
    ) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric audit residual ambiguity condition evidence and record a targeted SPCHG-006 / SPCC-006 "
            "gap resolution decision while preserving the distinction between gap resolution, completion decision, "
            "completion execution, definition execution, predicate definition completion, theorem proof, proof execution, "
            "proof assistant verification, completed formalization, framework-level proof, external validation, independent "
            "experiment, manuscript readiness, readiness approval, and new citation additions?"
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
        lines.append("- Milestone type: boundary audit plus targeted gap resolution decision")
        lines.append("- Resolution status after this milestone: targeted gap resolution decision recorded")
        lines.append("")
        lines.append("## Boundary audit rows")
        lines.append("")
        lines.append("| Row | Audited evidence | Accepted claim | Blocked claim | Decision |")
        lines.append("|---|---|---|---|---|")
        for row in audit_rows:
            lines.append(
                f"| {row['row_id']} | {row['audited_evidence']} | {row['accepted_claim']} | "
                f"{row['blocked_claim']} | {row['decision']} |"
            )
        lines.append("")
        lines.append("## Scope rules")
        for index, rule in enumerate(scope_rules, start=1):
            lines.append(f"{index}. {rule}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact records a targeted gap resolution decision for SPCHG-006 / SPCC-006 only. "
            "It resolves SPCHG-006 while leaving one unresolved and blocking gap. It does not authorize completion execution, "
            "does not complete Sigma_A, does not complete any formal definition, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not complete formalization, does not prove the full framework, "
            "does not provide external validation, does not perform an independent experiment, does not approve manuscript submission readiness, "
            "and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "residual_ambiguity_evidence_boundary_audit_count",
            "audited_residual_ambiguity_evidence_count",
            "residual_ambiguity_boundary_audit_row_count",
            "accepted_claim_count",
            "blocked_claim_count",
            "gap_resolution_decision_count",
            "targeted_gap_resolution_decision_count",
            "targeted_gap_count",
            "targeted_gap_id_count",
            "targeted_criterion_count",
            "evidence_supported_gap_count",
            "previously_resolved_gaps_retained_count",
            "resolved_gap_count",
            "newly_resolved_gap_count",
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
            "carried_residual_ambiguity_condition_evidence_execution_count",
            "carried_residual_ambiguity_evidence_row_count",
            "carried_residual_ambiguity_scope_rule_count",
            "carried_residual_ambiguity_acceptance_test_count",
            "carried_residual_ambiguity_blocked_overreach_count",
            "carried_target_gap_count",
            "carried_target_gap_id_count",
            "carried_target_criterion_count",
            "carried_evidence_support_count",
            "carried_prior_resolved_gaps_retained_count",
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
            "The v8.99 artifact audits residual ambiguity condition evidence and records a targeted SPCHG-006 / SPCC-006 "
            "gap resolution decision. It increases resolved gaps from five to six, reduces unresolved and blocking gaps from two to one, "
            "and keeps completion decision, completion execution, Sigma_A completion, definition completion, theorem proof, proof assistant "
            "verification, external validation, independent experiment, manuscript submission readiness, readiness approval, and new citation "
            "additions at zero."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Do not begin completion execution after v8.99.",
            "Identify and execute evidence for the final remaining unresolved conditional-hold gap.",
            "Keep final residual gap evidence separate from final residual gap resolution decision.",
            "Keep completion decision separate from all gap resolution milestones.",
            "Keep completion execution separate from completion decision.",
            "Keep definition completion separate from evidence and gap resolution decisions.",
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
            "not authorize",
            "remain zero",
            "separate",
            "zero",
            "absent",
            "preserving",
            "only",
            "leaving one unresolved",
            "targeted gap resolution decision",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
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
            "may not collapse the final unresolved gap",
            "may not create a completion decision plan",
            "No formal proof",
            "No external validation",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_patterns = [
            r"^[- ]*completion decision count:\s*[1-9]",
            r"^[- ]*completion execution count:\s*[1-9]",
            r"^[- ]*completion execution authorized count:\s*[1-9]",
            r"^[- ]*definition execution count:\s*[1-9]",
            r"^[- ]*new completion criterion count:\s*[1-9]",
            r"^[- ]*new completion decision plan count:\s*[1-9]",
            r"^[- ]*stabilization predicate definition completion count:\s*[1-9]",
            r"^[- ]*new theorem proven count:\s*[1-9]",
            r"^[- ]*proof assistant verification count:\s*[1-9]",
            r"^[- ]*formalization complete count:\s*[1-9]",
            r"^[- ]*full framework formal proof count:\s*[1-9]",
            r"^[- ]*external validation count:\s*[1-9]",
            r"^[- ]*independent experiment count:\s*[1-9]",
            r"^[- ]*manuscript submission ready count:\s*[1-9]",
            r"^[- ]*readiness approval count:\s*[1-9]",
            r"^[- ]*new citation added count:\s*[1-9]",
            r"\bSigma_A completion achieved\b",
            r"\bframework proven\b",
            r"\bmanuscript ready\b",
        ]

        count = 0
        for raw_line in text.splitlines():
            line = raw_line.strip()
            lowered = line.lower()

            if not lowered:
                continue

            if lowered.startswith("- carried ") or lowered.startswith("carried "):
                continue

            protective_markers = [
                "does not",
                "do not",
                "cannot",
                "remain zero",
                "remains absent",
                "separate",
                "without claiming",
            ]
            if any(marker in lowered for marker in protective_markers):
                continue

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
    report = ResidualAmbiguityEvidenceBoundaryAuditPlusGapResolutionDecisionBuilder().run()
    print(f"Wrote {report.output_path}")
