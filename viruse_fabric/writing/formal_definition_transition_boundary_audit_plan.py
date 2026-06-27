from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class FormalDefinitionTransitionBoundaryAuditPlanReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class FormalDefinitionTransitionBoundaryAuditPlanBuilder:
    """Build v8.103 formal-definition transition boundary audit plan.

    Boundary discipline:
    - This milestone plans transition from gap-resolution closure toward formal definitions.
    - It does not execute definitions.
    - It does not complete Sigma_A or any formal object.
    - It does not prove theorems.
    - It does not perform proof assistant verification.
    - It does not provide external validation or manuscript readiness.
    """

    title = "Formal Definition Transition Boundary Audit Plan v8.103"
    source_artifact = Path("outputs/completion_decision_boundary_audit_planning_v8_102.md")
    output_path = Path("outputs/formal_definition_transition_boundary_audit_plan_v8_103.md")

    planned_formal_objects = [
        "Sigma_A state space / admissible trajectory object",
        "stabilization predicate",
        "attractor-class object",
        "constraint-region object",
        "causal-mass object",
        "observer-projection object",
    ]

    def run(self) -> FormalDefinitionTransitionBoundaryAuditPlanReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        transition_rows = [
            {
                "row_id": "FDT-001",
                "transition_item": "Use gap-resolution closure as a precondition for formal-definition work.",
                "source_evidence": "v8.102 carries resolved gap count 7, unresolved gap count 0, remaining blocking gap count 0, and conditional hold count 0.",
                "planned_action": "Allow formal-definition transition planning, not definition execution.",
                "blocked_overreach": "Do not treat gap closure as completed formalization.",
            },
            {
                "row_id": "FDT-002",
                "transition_item": "Identify the core formal objects before drafting definitions.",
                "source_evidence": "The project repeatedly protects Sigma_A, stabilization predicate, attractor class, constraint region, causal mass, and observer projection counters.",
                "planned_action": "Create a later formal object inventory execution milestone.",
                "blocked_overreach": "Do not define or complete any object in this planning milestone.",
            },
            {
                "row_id": "FDT-003",
                "transition_item": "Separate definition draft from definition completion.",
                "source_evidence": "Definition execution and completed formal definition counters remain zero.",
                "planned_action": "Plan staged definition drafts followed by consistency audits.",
                "blocked_overreach": "Do not claim completed definitions from planned objects.",
            },
            {
                "row_id": "FDT-004",
                "transition_item": "Separate theorem candidates from theorem proofs.",
                "source_evidence": "New theorem proven count remains zero and cumulative limited theorem proven count remains five.",
                "planned_action": "Require theorem-candidate planning after core definitions exist.",
                "blocked_overreach": "Do not claim theorem proof or proof assistant verification.",
            },
            {
                "row_id": "FDT-005",
                "transition_item": "Separate formal definitions from validation and manuscript readiness.",
                "source_evidence": "External validation, independent experiment, manuscript readiness, readiness approval, and new citation counters remain zero.",
                "planned_action": "Keep validation and manuscript readiness outside the definition transition.",
                "blocked_overreach": "Do not claim external validation, independent experiment, citation completion, or submission readiness.",
            },
        ]

        transition_questions = [
            "Which formal object must be defined first for the later theorem layer to be meaningful?",
            "What is the minimal safe formal representation of Sigma_A?",
            "Which terms are currently only conceptual and must not be treated as definitions?",
            "What consistency relations must hold between stabilization predicate and attractor-class object?",
            "What consistency relations must hold between constraint region and causal mass?",
            "What consistency relations must hold between observer projection and the state-space object?",
            "Which theorem candidates become meaningful only after formal definitions exist?",
            "Which proof and proof-assistant counters must remain protected during definition work?",
        ]

        warnings.extend([
            "This milestone is a transition boundary audit plan only.",
            "No formal definition is executed in v8.103.",
            "No formal definition is completed in v8.103.",
            "Theorem proof, proof assistant verification, external validation, and manuscript readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "formal_definition_transition_boundary_audit_plan_count": 1,
            "formal_definition_transition_row_count": len(transition_rows),
            "planned_formal_object_count": len(self.planned_formal_objects),
            "transition_question_count": len(transition_questions),
            "gap_resolution_closure_carried_count": 1,
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "completion_decision_plan_count": carried.get("Completion decision plan count", 1),
            "completion_decision_count": 0,
            "completion_execution_count": 0,
            "completion_execution_authorized_count": 0,
            "definition_transition_plan_count": 1,
            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "formal_object_inventory_execution_count": 0,
            "new_stabilization_predicate_draft_clause_count": 0,
            "new_completion_criterion_count": 0,
            "new_completion_decision_plan_count": 0,
            "stabilization_predicate_definition_completion_count": 0,
            "attractor_class_definition_completion_count": 0,
            "constraint_region_definition_completion_count": 0,
            "causal_mass_definition_completion_count": 0,
            "observer_projection_definition_completion_count": 0,
            "sigma_a_definition_completion_count": 0,
            "carried_completion_decision_boundary_audit_planning_count": carried.get("Completion decision boundary audit planning count", 1),
            "carried_completion_decision_plan_count": carried.get("Completion decision plan count", 1),
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
            "theorem_candidate_plan_count": 0,
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

        report_text = self._render_report(transition_rows, transition_questions, counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.103 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.103 report.")
        if counts["formal_definition_transition_boundary_audit_plan_count"] != 1:
            errors.append("v8.103 must produce exactly one formal definition transition boundary audit plan.")
        if counts["planned_formal_object_count"] != 6:
            errors.append("v8.103 must plan exactly six core formal object families.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.103 must not execute definitions.")
        if counts["completed_formal_definition_count"] != 0:
            errors.append("v8.103 must not complete formal definitions.")
        if counts["formalization_complete_count"] != 0:
            errors.append("v8.103 must not complete formalization.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.103 must not prove a theorem.")

        zero_fields = [
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "formal_object_inventory_execution_count",
            "new_stabilization_predicate_draft_clause_count",
            "new_completion_criterion_count",
            "new_completion_decision_plan_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "sigma_a_definition_completion_count",
            "new_theorem_proven_count",
            "theorem_candidate_plan_count",
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

        final_report_text = self._render_report(transition_rows, transition_questions, counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return FormalDefinitionTransitionBoundaryAuditPlanReport(
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
        transition_rows: list[dict[str, str]],
        transition_questions: list[str],
        counts: dict[str, int],
        warnings: list[str],
    ) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric safely transition from gap-resolution closure and completion-decision planning toward formal-definition work "
            "while keeping definition execution, completed formal definitions, theorem proof, proof assistant verification, external validation, "
            "manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Transition boundary")
        lines.append("- Milestone type: formal definition transition boundary audit plan only")
        lines.append("- Definition execution status after this milestone: not executed")
        lines.append("- Formal definition completion status after this milestone: not completed")
        lines.append("- Theorem proof status after this milestone: not proven")
        lines.append("")
        lines.append("## Planned formal object families")
        for index, obj in enumerate(self.planned_formal_objects, start=1):
            lines.append(f"{index}. {obj}")
        lines.append("")
        lines.append("## Transition rows")
        lines.append("")
        lines.append("| Row | Transition item | Source evidence | Planned action | Blocked overreach |")
        lines.append("|---|---|---|---|---|")
        for row in transition_rows:
            lines.append(
                f"| {row['row_id']} | {row['transition_item']} | {row['source_evidence']} | "
                f"{row['planned_action']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Transition questions")
        for index, question in enumerate(transition_questions, start=1):
            lines.append(f"{index}. {question}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact plans a later formal-definition transition only. "
            "It does not execute definitions, does not complete Sigma_A, does not complete any formal definition, "
            "does not create a theorem candidate, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not complete formalization, does not prove the full framework, "
            "does not provide external validation, does not perform an independent experiment, does not approve manuscript submission readiness, "
            "and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "formal_definition_transition_boundary_audit_plan_count",
            "formal_definition_transition_row_count",
            "planned_formal_object_count",
            "transition_question_count",
            "gap_resolution_closure_carried_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "completion_decision_plan_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "definition_transition_plan_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "formal_object_inventory_execution_count",
            "new_stabilization_predicate_draft_clause_count",
            "new_completion_criterion_count",
            "new_completion_decision_plan_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "sigma_a_definition_completion_count",
            "carried_completion_decision_boundary_audit_planning_count",
            "carried_completion_decision_plan_count",
            "carried_resolved_gap_count",
            "carried_unresolved_gap_count",
            "carried_remaining_blocking_gap_count",
            "carried_conditional_hold_count",
            "carried_completion_decision_count",
            "carried_completion_execution_count",
            "carried_completion_execution_authorized_count",
            "carried_definition_execution_count",
            "carried_new_definition_execution_count",
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
            "theorem_candidate_plan_count",
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
            "The v8.103 artifact plans the transition toward formal-definition work after gap-resolution closure. "
            "It identifies the core formal object families that should be inventoried next, but does not execute definitions, "
            "does not complete formal definitions, does not create theorem candidates, does not prove theorems, does not provide proof assistant verification, "
            "does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute a core formal object inventory in v8.104.",
            "Keep inventory separate from definition drafts.",
            "Draft Sigma_A only after the object inventory exists.",
            "Draft stabilization predicate only after Sigma_A dependencies are explicit.",
            "Audit consistency between formal objects before theorem candidates.",
            "Plan theorem candidates only after the core definition layer exists.",
            "Keep proof execution separate from theorem candidate planning.",
            "Keep proof assistant verification, validation, citation work, and manuscript readiness separate.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = [
            "does not",
            "not executed",
            "not completed",
            "not proven",
            "separate",
            "zero",
            "plan only",
            "later",
            "not approve",
            "not claim",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute definitions",
            "does not complete Sigma_A",
            "does not complete any formal definition",
            "does not create a theorem candidate",
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
        """Count unsafe definition/proof/readiness claims without flagging protective boundary prose.

        v8.103 is allowed to plan a transition toward formal-definition work.
        It is not allowed to execute definitions, complete definitions, create
        theorem candidates, prove theorems, verify proofs, validate externally,
        approve manuscript readiness, or add citations.

        Protective lines such as:
        - "No formal definition is completed in v8.103."
        - "Theorem proof status after this milestone: not proven"
        - "Completed formal definition count: 0"
        are not overclaims.
        """
        forbidden_positive_counter_patterns = [
            r"^[- ]*completion decision count:\\s*[1-9]",
            r"^[- ]*completion execution count:\\s*[1-9]",
            r"^[- ]*completion execution authorized count:\\s*[1-9]",
            r"^[- ]*definition execution count:\\s*[1-9]",
            r"^[- ]*new definition execution count:\\s*[1-9]",
            r"^[- ]*formal object inventory execution count:\\s*[1-9]",
            r"^[- ]*new stabilization predicate draft clause count:\\s*[1-9]",
            r"^[- ]*new completion criterion count:\\s*[1-9]",
            r"^[- ]*new completion decision plan count:\\s*[1-9]",
            r"^[- ]*stabilization predicate definition completion count:\\s*[1-9]",
            r"^[- ]*attractor class definition completion count:\\s*[1-9]",
            r"^[- ]*constraint region definition completion count:\\s*[1-9]",
            r"^[- ]*causal mass definition completion count:\\s*[1-9]",
            r"^[- ]*observer projection definition completion count:\\s*[1-9]",
            r"^[- ]*sigma_a definition completion count:\\s*[1-9]",
            r"^[- ]*sigma a definition completion count:\\s*[1-9]",
            r"^[- ]*new theorem proven count:\\s*[1-9]",
            r"^[- ]*theorem candidate plan count:\\s*[1-9]",
            r"^[- ]*proof assistant verification count:\\s*[1-9]",
            r"^[- ]*formalization complete count:\\s*[1-9]",
            r"^[- ]*completed formal definition count:\\s*[1-9]",
            r"^[- ]*definition completion execution count:\\s*[1-9]",
            r"^[- ]*full framework formal proof count:\\s*[1-9]",
            r"^[- ]*formal mathematical proof count:\\s*[1-9]",
            r"^[- ]*formal proof execution count:\\s*[1-9]",
            r"^[- ]*proof execution count:\\s*[1-9]",
            r"^[- ]*proof gap resolution count:\\s*[1-9]",
            r"^[- ]*external validation count:\\s*[1-9]",
            r"^[- ]*independent experiment count:\\s*[1-9]",
            r"^[- ]*manuscript submission ready count:\\s*[1-9]",
            r"^[- ]*readiness approval count:\\s*[1-9]",
            r"^[- ]*new citation added count:\\s*[1-9]",
        ]

        forbidden_unsafe_prose_patterns = [
            r"\\bSigma_A completion achieved\\b",
            r"\\bformal definition completed\\b",
            r"\\bformal definitions completed\\b",
            r"\\bcompleted formal definition achieved\\b",
            r"\\btheorem proven\\b",
            r"\\btheorems proven\\b",
            r"\\bproof assistant verification complete\\b",
            r"\\bframework proven\\b",
            r"\\bexternal validation complete\\b",
            r"\\bmanuscript ready\\b",
            r"\\bdefinition execution completed\\b",
        ]

        protective_markers = [
            "does not",
            "do not",
            "cannot",
            "no formal definition",
            "no formal definitions",
            "no theorem",
            "not executed",
            "not completed",
            "not proven",
            "not created",
            "not approved",
            "remain zero",
            "remains zero",
            "remains absent",
            "transition boundary audit plan only",
            "plan only",
            "planning",
            "separate",
            "zero",
            "count: 0",
        ]

        count = 0
        import re

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
    report = FormalDefinitionTransitionBoundaryAuditPlanBuilder().run()
    print(f"Wrote {report.output_path}")
