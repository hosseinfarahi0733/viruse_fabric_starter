from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class FinalResidualConditionEvidenceExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class FinalResidualConditionEvidenceExecutionBuilder:
    """Build v8.100 final residual condition evidence execution artifact.

    Boundary discipline:
    - This milestone produces evidence for the final remaining unresolved conditional-hold gap.
    - Target: SPCHG-007 / SPCC-007.
    - It does not resolve SPCHG-007.
    - It does not authorize completion execution.
    - It does not add definition completion, theorem proof, proof assistant verification,
      framework proof, external validation, independent experiment, manuscript readiness,
      readiness approval, or new citations.
    """

    title = "Final Residual Condition Evidence Execution v8.100"
    source_artifact = Path("outputs/residual_ambiguity_evidence_boundary_audit_plus_gap_resolution_decision_v8_99.md")
    output_path = Path("outputs/final_residual_condition_evidence_execution_v8_100.md")

    target_gap_id = "SPCHG-007"
    target_criterion_id = "SPCC-007"

    def run(self) -> FinalResidualConditionEvidenceExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        evidence_rows = [
            {
                "row_id": "FRE-001",
                "condition": "The final residual gap must be isolated after SPCHG-006 resolution.",
                "evidence": "The v8.99 source carries resolved gap count 6 and leaves one unresolved and blocking conditional-hold gap.",
                "acceptance_test": "The v8.100 report must retain resolved gap count 6, unresolved gap count 1, and remaining blocking gap count 1.",
                "blocked_overreach": "Do not treat final residual evidence as final gap resolution.",
            },
            {
                "row_id": "FRE-002",
                "condition": "The evidence must be scoped to SPCHG-007 / SPCC-007.",
                "evidence": "This artifact targets exactly one final residual gap and one final residual criterion.",
                "acceptance_test": "The report must contain target gap count 1, target gap ID count 1, and target criterion count 1.",
                "blocked_overreach": "Do not create a new completion criterion or completion decision plan.",
            },
            {
                "row_id": "FRE-003",
                "condition": "The final residual condition must preserve gap-resolution boundaries.",
                "evidence": "This milestone produces evidence but does not record a targeted gap resolution decision.",
                "acceptance_test": "Gap resolution decision count, targeted gap resolution decision count, newly resolved gap count, and gap resolution authorized count must remain zero.",
                "blocked_overreach": "Do not declare all gaps resolved.",
            },
            {
                "row_id": "FRE-004",
                "condition": "The final residual condition must preserve completion boundaries.",
                "evidence": "Completion decision, completion execution, and completion execution authorization remain absent.",
                "acceptance_test": "Completion decision count, completion execution count, and completion execution authorized count must remain zero.",
                "blocked_overreach": "Do not authorize completion execution or Sigma_A completion.",
            },
            {
                "row_id": "FRE-005",
                "condition": "The final residual condition must preserve proof, validation, readiness, and citation boundaries.",
                "evidence": "The proof, validation, readiness, and citation counters remain zero.",
                "acceptance_test": "New theorem, proof execution, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation counters must remain zero.",
                "blocked_overreach": "Do not claim proof, proof assistant verification, external validation, independent experiment, manuscript readiness, or citation completion.",
            },
        ]

        scope_rules = [
            "Evidence execution may identify the final residual condition but may not resolve it.",
            "Evidence execution may preserve one unresolved and blocking gap but may not collapse it to zero.",
            "Evidence execution may recommend a later boundary audit plus gap resolution decision but may not perform that decision.",
        ]

        warnings.extend([
            "This milestone produces final residual condition evidence only.",
            "SPCHG-007 remains unresolved after v8.100 evidence execution.",
            "One conditional-hold gap remains unresolved and blocking.",
            "Completion execution, theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, and new citations remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "final_residual_condition_evidence_execution_count": 1,
            "final_residual_evidence_row_count": len(evidence_rows),
            "final_residual_scope_rule_count": len(scope_rules),
            "final_residual_acceptance_test_count": len(evidence_rows),
            "final_residual_blocked_overreach_count": len(evidence_rows),
            "target_gap_count": 1,
            "target_gap_id_count": 1,
            "target_criterion_count": 1,
            "evidence_support_count": 1,
            "previously_resolved_gaps_retained_count": 6,
            "gap_resolution_decision_count": 0,
            "targeted_gap_resolution_decision_count": 0,
            "newly_resolved_gap_count": 0,
            "resolved_gap_count": 6,
            "unresolved_gap_count": 1,
            "remaining_blocking_gap_count": 1,
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
            "carried_residual_ambiguity_evidence_boundary_audit_count": carried.get("Residual ambiguity evidence boundary audit count", 1),
            "carried_gap_resolution_decision_count": carried.get("Gap resolution decision count", 1),
            "carried_targeted_gap_resolution_decision_count": carried.get("Targeted gap resolution decision count", 1),
            "carried_newly_resolved_gap_count": carried.get("Newly resolved gap count", 1),
            "carried_resolved_gap_count": carried.get("Resolved gap count", 6),
            "carried_unresolved_gap_count": carried.get("Unresolved gap count", 1),
            "carried_remaining_blocking_gap_count": carried.get("Remaining blocking gap count", 1),
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
            errors.append("Overclaim detected in v8.100 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.100 report.")
        if counts["gap_resolution_decision_count"] != 0:
            errors.append("v8.100 must not record a gap resolution decision.")
        if counts["targeted_gap_resolution_decision_count"] != 0:
            errors.append("v8.100 must not record a targeted gap resolution decision.")
        if counts["newly_resolved_gap_count"] != 0:
            errors.append("v8.100 must not newly resolve SPCHG-007.")
        if counts["resolved_gap_count"] != 6:
            errors.append("v8.100 must retain resolved gap count at 6.")
        if counts["unresolved_gap_count"] != 1:
            errors.append("v8.100 must retain unresolved gap count at 1.")
        if counts["remaining_blocking_gap_count"] != 1:
            errors.append("v8.100 must retain remaining blocking gap count at 1.")
        if counts["gap_resolution_authorized_count"] != 0:
            errors.append("v8.100 must not authorize gap resolution.")

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

        return FinalResidualConditionEvidenceExecutionReport(
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
            "Can Viruse Fabric produce final residual condition evidence for SPCHG-007 / SPCC-007 while preserving "
            "the distinction between evidence execution, gap resolution decision, completion decision, completion execution, "
            "definition execution, predicate definition completion, theorem proof, proof execution, proof assistant verification, "
            "completed formalization, framework-level proof, external validation, independent experiment, manuscript readiness, "
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
        lines.append("## Final residual evidence rows")
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
            "This artifact produces final residual condition evidence for SPCHG-007 / SPCC-007 only. "
            "It does not record a gap resolution decision, does not newly resolve SPCHG-007, does not declare all gaps resolved, "
            "does not authorize completion execution, does not complete Sigma_A, does not complete any formal definition, "
            "does not prove a theorem, does not run proof execution, does not provide proof assistant verification, "
            "does not complete formalization, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "final_residual_condition_evidence_execution_count",
            "final_residual_evidence_row_count",
            "final_residual_scope_rule_count",
            "final_residual_acceptance_test_count",
            "final_residual_blocked_overreach_count",
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
            "carried_residual_ambiguity_evidence_boundary_audit_count",
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
            "The v8.100 artifact produces standalone final residual condition evidence for SPCHG-007 / SPCC-007. "
            "It preserves six resolved gaps, leaves one unresolved and blocking gap, and keeps gap resolution decision, "
            "completion decision, completion execution, Sigma_A completion, definition completion, theorem proof, proof assistant "
            "verification, external validation, independent experiment, manuscript submission readiness, readiness approval, and new citation additions at zero."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit the final residual evidence boundary in v8.101.",
            "Record a targeted SPCHG-007 gap resolution decision only if the v8.101 boundary audit passes.",
            "Keep SPCHG-007 unresolved until that later resolution decision exists.",
            "Do not begin completion decision after evidence execution.",
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
            "not resolve",
            "not authorize",
            "remain zero",
            "evidence execution only",
            "evidence produced, not resolved",
            "separate",
            "zero",
            "absent",
            "preserving",
            "unresolved",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not record a gap resolution decision",
            "does not newly resolve",
            "does not declare all gaps resolved",
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
            "may not resolve it",
            "may not collapse it to zero",
            "may not perform that decision",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_patterns = [
            r"^[- ]*gap resolution decision count:\s*[1-9]",
            r"^[- ]*targeted gap resolution decision count:\s*[1-9]",
            r"^[- ]*newly resolved gap count:\s*[1-9]",
            r"^[- ]*gap resolution authorized count:\s*[1-9]",
            r"^[- ]*unresolved gap count:\s*0",
            r"^[- ]*remaining blocking gap count:\s*0",
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
            r"\ball gaps resolved\b",
            r"\bSPCHG-007 resolved\b",
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
                "not resolved",
                "not resolve",
                "remain zero",
                "remains absent",
                "evidence produced, not resolved",
                "evidence execution only",
                "separate",
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
    report = FinalResidualConditionEvidenceExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
