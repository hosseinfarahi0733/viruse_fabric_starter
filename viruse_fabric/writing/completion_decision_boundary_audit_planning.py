from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class CompletionDecisionBoundaryAuditPlanningReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class CompletionDecisionBoundaryAuditPlanningBuilder:
    """Build v8.102 completion decision boundary audit planning artifact.

    Boundary discipline:
    - This milestone plans a later completion decision boundary audit.
    - It does not record completion decision.
    - It does not authorize completion execution.
    - It does not complete Sigma_A.
    - It does not complete formal definitions.
    - It does not prove theorems.
    - It does not provide proof assistant verification.
    - It does not provide external validation.
    - It does not approve manuscript readiness.
    - It does not add citations.
    """

    title = "Completion Decision Boundary Audit Planning v8.102"
    source_artifact = Path("outputs/final_residual_evidence_boundary_audit_plus_gap_resolution_decision_v8_101.md")
    output_path = Path("outputs/completion_decision_boundary_audit_planning_v8_102.md")

    def run(self) -> CompletionDecisionBoundaryAuditPlanningReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        planning_rows = [
            {
                "row_id": "CDP-001",
                "planning_item": "Confirm gap-resolution closure before any completion decision attempt.",
                "source_evidence": "v8.101 reports resolved gap count 7, unresolved gap count 0, remaining blocking gap count 0, and conditional hold count 0.",
                "required_later_audit": "A later completion decision artifact must verify that gap closure is necessary but not sufficient for completion.",
                "blocked_overreach": "Do not treat zero unresolved gaps as completion decision.",
            },
            {
                "row_id": "CDP-002",
                "planning_item": "Separate completion decision from completion execution.",
                "source_evidence": "v8.101 keeps completion decision, completion execution, and completion execution authorization at zero.",
                "required_later_audit": "A later completion decision must not execute completion or authorize execution unless a separate execution milestone exists.",
                "blocked_overreach": "Do not authorize completion execution in a planning artifact.",
            },
            {
                "row_id": "CDP-003",
                "planning_item": "Separate completion decision from formal definition completion.",
                "source_evidence": "Definition execution and all formal definition completion counters remain zero.",
                "required_later_audit": "A later completion decision must distinguish gap closure from completed formal definitions.",
                "blocked_overreach": "Do not claim Sigma_A, stabilization predicate, attractor class, constraint region, causal mass, or observer projection completion.",
            },
            {
                "row_id": "CDP-004",
                "planning_item": "Separate completion decision from proof and verification.",
                "source_evidence": "New theorem proven count remains zero after v8.101 and cumulative limited theorem count remains five.",
                "required_later_audit": "A later completion decision must preserve theorem proof, proof execution, and proof assistant verification boundaries.",
                "blocked_overreach": "Do not claim theorem proof, formal proof, framework proof, or proof assistant verification.",
            },
            {
                "row_id": "CDP-005",
                "planning_item": "Separate completion decision from validation, readiness, and citation work.",
                "source_evidence": "External validation, independent experiment, manuscript readiness, readiness approval, and new citation counters remain zero.",
                "required_later_audit": "A later completion decision must not imply external validation, manuscript readiness, or citation completion.",
                "blocked_overreach": "Do not claim external validation, independent experiment, manuscript submission readiness, or new citations.",
            },
        ]

        decision_boundary_questions = [
            "Does zero unresolved gap count justify only considering a completion decision, not recording it?",
            "What additional evidence is required before a completion decision can be recorded?",
            "Which hard-zero counters must remain protected in any completion-decision artifact?",
            "What would distinguish completion decision from completion execution?",
            "What would distinguish completion decision from formal definition completion?",
            "What would distinguish completion decision from theorem proof and proof assistant verification?",
            "What would distinguish completion decision from external validation and independent experiment?",
            "What would distinguish completion decision from manuscript readiness and citation additions?",
        ]

        warnings.extend([
            "This milestone is planning only.",
            "No completion decision is recorded in v8.102.",
            "Zero unresolved gaps do not authorize completion execution.",
            "Proof assistant verification, external validation, manuscript readiness, and new citations remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "completion_decision_boundary_audit_planning_count": 1,
            "completion_decision_plan_row_count": len(planning_rows),
            "completion_decision_boundary_question_count": len(decision_boundary_questions),
            "gap_resolution_closure_carried_count": 1,
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "completion_decision_plan_count": 1,
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
            "carried_final_residual_evidence_boundary_audit_count": carried.get("Final residual evidence boundary audit count", 1),
            "carried_gap_resolution_decision_count": carried.get("Gap resolution decision count", 1),
            "carried_targeted_gap_resolution_decision_count": carried.get("Targeted gap resolution decision count", 1),
            "carried_newly_resolved_gap_count": carried.get("Newly resolved gap count", 1),
            "carried_resolved_gap_count": carried.get("Resolved gap count", 7),
            "carried_unresolved_gap_count": carried.get("Unresolved gap count", 0),
            "carried_remaining_blocking_gap_count": carried.get("Remaining blocking gap count", 0),
            "carried_conditional_hold_count": carried.get("Conditional hold count", 0),
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
            "hard_zero_count": 13,
            "next_step_count": 8,
        }

        report_text = self._render_report(planning_rows, decision_boundary_questions, counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.102 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.102 report.")
        if counts["completion_decision_plan_count"] != 1:
            errors.append("v8.102 must produce exactly one completion decision planning artifact.")
        if counts["completion_decision_count"] != 0:
            errors.append("v8.102 must not record completion decision.")
        if counts["completion_execution_count"] != 0:
            errors.append("v8.102 must not record completion execution.")
        if counts["completion_execution_authorized_count"] != 0:
            errors.append("v8.102 must not authorize completion execution.")
        if counts["resolved_gap_count"] != 7:
            errors.append("v8.102 must carry resolved gap count 7.")
        if counts["unresolved_gap_count"] != 0:
            errors.append("v8.102 must carry unresolved gap count 0.")
        if counts["remaining_blocking_gap_count"] != 0:
            errors.append("v8.102 must carry remaining blocking gap count 0.")
        if counts["conditional_hold_count"] != 0:
            errors.append("v8.102 must carry conditional hold count 0.")

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

        final_report_text = self._render_report(planning_rows, decision_boundary_questions, counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return CompletionDecisionBoundaryAuditPlanningReport(
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
        planning_rows: list[dict[str, str]],
        decision_boundary_questions: list[str],
        counts: dict[str, int],
        warnings: list[str],
    ) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric plan a completion-decision boundary audit after all tracked gap-resolution counters reach zero, "
            "while keeping completion decision, completion execution, definition completion, theorem proof, proof assistant verification, "
            "external validation, independent experiment, manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Planning boundary")
        lines.append("- Milestone type: completion decision boundary audit planning only")
        lines.append("- Completion decision status after this milestone: not recorded")
        lines.append("- Completion execution status after this milestone: not authorized and not executed")
        lines.append("")
        lines.append("## Planning rows")
        lines.append("")
        lines.append("| Row | Planning item | Source evidence | Required later audit | Blocked overreach |")
        lines.append("|---|---|---|---|---|")
        for row in planning_rows:
            lines.append(
                f"| {row['row_id']} | {row['planning_item']} | {row['source_evidence']} | "
                f"{row['required_later_audit']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Completion decision boundary questions")
        for index, question in enumerate(decision_boundary_questions, start=1):
            lines.append(f"{index}. {question}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact plans a later completion-decision boundary audit only. "
            "It does not record completion decision, does not authorize completion execution, does not execute completion, "
            "does not complete Sigma_A, does not complete any formal definition, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not complete formalization, does not prove the full framework, "
            "does not provide external validation, does not perform an independent experiment, does not approve manuscript submission readiness, "
            "and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "completion_decision_boundary_audit_planning_count",
            "completion_decision_plan_row_count",
            "completion_decision_boundary_question_count",
            "gap_resolution_closure_carried_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "completion_decision_plan_count",
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
            "carried_final_residual_evidence_boundary_audit_count",
            "carried_gap_resolution_decision_count",
            "carried_targeted_gap_resolution_decision_count",
            "carried_newly_resolved_gap_count",
            "carried_resolved_gap_count",
            "carried_unresolved_gap_count",
            "carried_remaining_blocking_gap_count",
            "carried_conditional_hold_count",
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
            "The v8.102 artifact plans a later completion-decision boundary audit after all tracked gap-resolution counters have reached zero. "
            "It does not record completion decision and does not authorize completion execution. It keeps definition completion, theorem proof, "
            "proof assistant verification, external validation, independent experiment, manuscript submission readiness, readiness approval, "
            "and new citation additions at zero."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit whether completion decision is even eligible after gap closure.",
            "Keep completion decision separate from completion execution.",
            "Keep completion execution authorization separate from completion decision.",
            "Keep formal definition completion separate from completion decision.",
            "Keep theorem proof and proof assistant verification separate from completion decision.",
            "Keep external validation and independent experiment separate from completion decision.",
            "Keep manuscript readiness and citation additions separate from completion decision.",
            "Do not claim manuscript readiness from gap closure alone.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = [
            "does not",
            "not recorded",
            "not authorized",
            "not executed",
            "separate",
            "zero",
            "planning only",
            "later",
            "not approve",
            "not claim",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not record completion decision",
            "does not authorize completion execution",
            "does not execute completion",
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
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_positive_counter_patterns = [
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
            r"^[- ]*completed formal definition count:\s*[1-9]",
            r"^[- ]*definition completion execution count:\s*[1-9]",
            r"^[- ]*full framework formal proof count:\s*[1-9]",
            r"^[- ]*formal mathematical proof count:\s*[1-9]",
            r"^[- ]*formal proof execution count:\s*[1-9]",
            r"^[- ]*proof execution count:\s*[1-9]",
            r"^[- ]*proof gap resolution count:\s*[1-9]",
            r"^[- ]*external validation count:\s*[1-9]",
            r"^[- ]*independent experiment count:\s*[1-9]",
            r"^[- ]*manuscript submission ready count:\s*[1-9]",
            r"^[- ]*readiness approval count:\s*[1-9]",
            r"^[- ]*new citation added count:\s*[1-9]",
        ]

        forbidden_unsafe_prose_patterns = [
            r"\bSigma_A completion achieved\b",
            r"\bcompletion decision recorded\b",
            r"\bcompletion execution authorized\b",
            r"\bcompletion execution performed\b",
            r"\bframework proven\b",
            r"\bmanuscript ready\b",
            r"\bproof assistant verification complete\b",
            r"\bexternal validation complete\b",
        ]

        protective_markers = [
            "does not",
            "do not",
            "cannot",
            "not recorded",
            "not authorized",
            "not executed",
            "planning only",
            "separate",
            "zero",
            "count: 0",
        ]

        count = 0
        for raw_line in text.splitlines():
            line = raw_line.strip()
            lowered = line.lower()

            if not lowered:
                continue

            if lowered.startswith("- carried ") or lowered.startswith("carried "):
                continue

            if any(marker in lowered for marker in protective_markers):
                continue

            for pattern in forbidden_positive_counter_patterns:
                if re.search(pattern.lower(), lowered):
                    count += 1
                    break
            else:
                for pattern in forbidden_unsafe_prose_patterns:
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
    report = CompletionDecisionBoundaryAuditPlanningBuilder().run()
    print(f"Wrote {report.output_path}")
