from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaACarrierTypeSelectionDecisionBoundaryPlanReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaACarrierTypeSelectionDecisionBoundaryPlanBuilder:
    """Build v8.109 Sigma_A carrier-type selection decision boundary plan.

    Boundary discipline:
    - This milestone plans the decision boundary for a future carrier-type selection.
    - It does not select a carrier type.
    - It does not execute a carrier-type selection decision.
    - It does not execute carrier refinement.
    - It does not execute Sigma_A refinement.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Carrier-Type Selection Decision Boundary Plan v8.109"
    source_artifact = Path("outputs/sigma_a_carrier_type_option_audit_execution_v8_108.md")
    output_path = Path("outputs/sigma_a_carrier_type_selection_decision_boundary_plan_v8_109.md")

    decision_boundary_rows = [
        {
            "criterion_id": "X-A-SEL-BND-001",
            "criterion": "Admissibility compatibility",
            "decision_test": "The selected carrier must support a clear Adm_A judgment domain.",
            "blocked_overreach": "Do not select the carrier in this planning milestone.",
        },
        {
            "criterion_id": "X-A-SEL-BND-002",
            "criterion": "Constraint-region compatibility",
            "decision_test": "The selected carrier must support C_reg membership without adding hidden state assumptions.",
            "blocked_overreach": "Do not complete C_reg or Sigma_A.",
        },
        {
            "criterion_id": "X-A-SEL-BND-003",
            "criterion": "Observer-projection compatibility",
            "decision_test": "The selected carrier must expose a domain compatible with Pi_obs.",
            "blocked_overreach": "Do not define Pi_obs or claim proof readiness.",
        },
        {
            "criterion_id": "X-A-SEL-BND-004",
            "criterion": "Causal-mass compatibility",
            "decision_test": "The selected carrier must not block later M_c typing as functional, valuation, or measure-like object.",
            "blocked_overreach": "Do not define M_c or execute refinement.",
        },
        {
            "criterion_id": "X-A-SEL-BND-005",
            "criterion": "Trajectory compatibility",
            "decision_test": "The selected carrier must support Traj_A construction after R_A and T_A are refined.",
            "blocked_overreach": "Do not complete trajectories or theorem candidates.",
        },
        {
            "criterion_id": "X-A-SEL-BND-006",
            "criterion": "Proof-readiness without premature formalization",
            "decision_test": "The selected carrier must be strong enough for future proof work but not force unjustified assumptions.",
            "blocked_overreach": "Do not claim formal proof readiness.",
        },
        {
            "criterion_id": "X-A-SEL-BND-007",
            "criterion": "Manuscript explainability",
            "decision_test": "The selected carrier should remain explainable in a manuscript before proof assistant translation.",
            "blocked_overreach": "Do not claim manuscript readiness.",
        },
        {
            "criterion_id": "X-A-SEL-BND-008",
            "criterion": "Audit traceability",
            "decision_test": "The selected carrier must be traceable back to v8.108 option audit findings.",
            "blocked_overreach": "Do not treat traceability as validation.",
        },
    ]

    candidate_options = [
        "set-like carrier",
        "typed-product carrier",
        "graph-state carrier",
        "measurable-space carrier",
        "structured-schema carrier",
    ]

    decision_questions = [
        "Which carrier option best supports Adm_A without hidden assumptions?",
        "Which carrier option best supports C_reg membership?",
        "Which carrier option best supports Pi_obs domain clarity?",
        "Which carrier option best preserves future M_c typing flexibility?",
        "Which carrier option best supports later trajectory construction?",
        "Which carrier option avoids premature over-formalization?",
        "Which carrier option is most explainable in manuscript form?",
        "Which carrier option is most traceable from v8.108 audit findings?",
    ]

    def run(self) -> SigmaACarrierTypeSelectionDecisionBoundaryPlanReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone plans the carrier-type selection decision boundary only.",
            "No carrier type is selected in v8.109.",
            "No carrier-type selection decision is executed in v8.109.",
            "Carrier refinement, Sigma_A refinement, Sigma_A completion, theorem planning, proof, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_carrier_type_selection_decision_boundary_plan_count": 1,
            "selection_boundary_criterion_count": len(self.decision_boundary_rows),
            "selection_decision_question_count": len(self.decision_questions),
            "candidate_carrier_option_carried_count": len(self.candidate_options),
            "selection_boundary_blocked_overreach_count": len(self.decision_boundary_rows),
            "carried_sigma_a_carrier_type_option_audit_execution_count": carried.get("Sigma_A carrier-type option audit execution count", 1),
            "carried_carrier_type_option_audited_count": carried.get("Carrier type option audited count", 5),
            "carried_carrier_type_option_audit_row_count": carried.get("Carrier type option audit row count", 5),
            "carried_carrier_option_evaluation_criterion_count": carried.get("Carrier option evaluation criterion count", 8),
            "carried_carrier_option_not_selected_status_count": carried.get("Carrier option not selected status count", 5),
            "carried_sigma_a_carrier_time_index_refinement_plan_count": carried.get("Carried Sigma_A carrier time-index refinement plan count", 1),
            "carried_sigma_a_draft_consistency_boundary_audit_count": carried.get("Carried Sigma_A draft consistency boundary audit count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "carrier_type_selection_count": 0,
            "carrier_type_selection_decision_count": 0,
            "carrier_type_selection_execution_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "time_index_refinement_execution_count": 0,
            "sigma_a_refinement_execution_count": 0,
            "new_sigma_a_draft_clause_count": 0,
            "new_definition_draft_execution_count": 0,
            "definition_inventory_execution_count": 0,
            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "completed_formal_definition_count": 0,
            "formalization_complete_count": 0,
            "sigma_a_definition_completion_count": 0,
            "stabilization_predicate_definition_completion_count": 0,
            "attractor_class_definition_completion_count": 0,
            "constraint_region_definition_completion_count": 0,
            "causal_mass_definition_completion_count": 0,
            "observer_projection_definition_completion_count": 0,
            "completion_decision_plan_count": carried.get("Completion decision plan count", 1),
            "completion_decision_count": 0,
            "completion_execution_count": 0,
            "completion_execution_authorized_count": 0,
            "theorem_candidate_plan_count": 0,
            "new_theorem_proven_count": 0,
            "cumulative_limited_theorem_proven_count": 5,
            "proof_assistant_verification_count": 0,
            "formal_mathematical_proof_count": 0,
            "formal_proof_execution_count": 0,
            "proof_execution_count": 0,
            "proof_gap_resolution_count": 0,
            "definition_completion_execution_count": 0,
            "full_framework_formal_proof_count": 0,
            "manuscript_submission_ready_count": 0,
            "readiness_approval_count": 0,
            "external_validation_count": 0,
            "independent_experiment_count": 0,
            "new_citation_added_count": 0,
            "hard_zero_count": 13,
            "next_step_count": 8,
        }

        report_text = self._render_report(counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.109 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.109 report.")
        if counts["sigma_a_carrier_type_selection_decision_boundary_plan_count"] != 1:
            errors.append("v8.109 must produce exactly one carrier-type selection decision boundary plan.")
        if counts["selection_boundary_criterion_count"] != 8:
            errors.append("v8.109 must include exactly eight selection boundary criteria.")
        if counts["selection_decision_question_count"] != 8:
            errors.append("v8.109 must include exactly eight selection decision questions.")
        if counts["candidate_carrier_option_carried_count"] != 5:
            errors.append("v8.109 must carry exactly five candidate carrier options.")
        if counts["carrier_type_selection_count"] != 0:
            errors.append("v8.109 must not select a carrier type.")
        if counts["carrier_type_selection_decision_count"] != 0:
            errors.append("v8.109 must not execute a carrier-type selection decision.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.109 must not execute carrier refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.109 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.109 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.109 must not prove a theorem.")

        zero_fields = [
            "carrier_type_selection_count",
            "carrier_type_selection_decision_count",
            "carrier_type_selection_execution_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_definition_draft_execution_count",
            "definition_inventory_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "theorem_candidate_plan_count",
            "new_theorem_proven_count",
            "proof_assistant_verification_count",
            "formal_mathematical_proof_count",
            "formal_proof_execution_count",
            "proof_execution_count",
            "proof_gap_resolution_count",
            "definition_completion_execution_count",
            "full_framework_formal_proof_count",
            "manuscript_submission_ready_count",
            "readiness_approval_count",
            "external_validation_count",
            "independent_experiment_count",
            "new_citation_added_count",
        ]

        for field in zero_fields:
            if counts[field] != 0:
                errors.append(f"{field} must remain zero, found {counts[field]}.")

        final_report_text = self._render_report(counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return SigmaACarrierTypeSelectionDecisionBoundaryPlanReport(
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

    def _format_label(self, key: str) -> str:
        overrides = {
            "sigma_a_carrier_type_selection_decision_boundary_plan_count": "Sigma_A carrier-type selection decision boundary plan count",
            "carried_sigma_a_carrier_type_option_audit_execution_count": "Carried Sigma_A carrier-type option audit execution count",
            "carried_sigma_a_carrier_time_index_refinement_plan_count": "Carried Sigma_A carrier time-index refinement plan count",
            "carried_sigma_a_draft_consistency_boundary_audit_count": "Carried Sigma_A draft consistency boundary audit count",
            "new_sigma_a_draft_clause_count": "New Sigma_A draft clause count",
            "sigma_a_refinement_execution_count": "Sigma_A refinement execution count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
            "carrier_type_selection_decision_count": "Carrier type selection decision count",
            "carrier_type_selection_execution_count": "Carrier type selection execution count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric plan the decision boundary for a future Sigma_A carrier-type selection after carrier-type option audit "
            "while keeping carrier selection, carrier selection decision execution, carrier refinement execution, Sigma_A refinement execution, "
            "new draft execution, definition execution, Sigma_A definition completion, theorem candidate planning, theorem proof, "
            "proof assistant verification, external validation, manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Planning boundary")
        lines.append("- Milestone type: Sigma_A carrier-type selection decision boundary plan only")
        lines.append("- Carrier type selection after this milestone: not selected")
        lines.append("- Carrier type selection decision after this milestone: not executed")
        lines.append("- Carrier refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Candidate carrier options carried from v8.108")
        for index, option in enumerate(self.candidate_options, start=1):
            lines.append(f"{index}. {option}")
        lines.append("")
        lines.append("## Selection boundary criteria")
        lines.append("")
        lines.append("| Criterion ID | Criterion | Decision test | Blocked overreach |")
        lines.append("|---|---|---|---|")
        for row in self.decision_boundary_rows:
            lines.append(
                f"| {row['criterion_id']} | {row['criterion']} | {row['decision_test']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Selection decision questions")
        for index, question in enumerate(self.decision_questions, start=1):
            lines.append(f"{index}. {question}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact plans the Sigma_A carrier-type selection decision boundary only. "
            "It does not select a carrier type, does not execute a carrier-type selection decision, "
            "does not execute carrier refinement, does not execute time-index refinement, does not execute Sigma_A refinement, "
            "does not create new Sigma_A draft clauses, does not execute a new definition draft, does not execute definitions, "
            "does not complete Sigma_A, does not complete any formal definition, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_carrier_type_selection_decision_boundary_plan_count",
            "selection_boundary_criterion_count",
            "selection_decision_question_count",
            "candidate_carrier_option_carried_count",
            "selection_boundary_blocked_overreach_count",
            "carried_sigma_a_carrier_type_option_audit_execution_count",
            "carried_carrier_type_option_audited_count",
            "carried_carrier_type_option_audit_row_count",
            "carried_carrier_option_evaluation_criterion_count",
            "carried_carrier_option_not_selected_status_count",
            "carried_sigma_a_carrier_time_index_refinement_plan_count",
            "carried_sigma_a_draft_consistency_boundary_audit_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "carrier_type_selection_count",
            "carrier_type_selection_decision_count",
            "carrier_type_selection_execution_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_definition_draft_execution_count",
            "definition_inventory_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "completion_decision_plan_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "theorem_candidate_plan_count",
            "new_theorem_proven_count",
            "cumulative_limited_theorem_proven_count",
            "proof_assistant_verification_count",
            "formal_mathematical_proof_count",
            "formal_proof_execution_count",
            "proof_execution_count",
            "proof_gap_resolution_count",
            "definition_completion_execution_count",
            "full_framework_formal_proof_count",
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
                lines.append(f"- {self._format_label(key)}: {counts[key]}")
        lines.append("")
        lines.append("## Warnings")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")
        lines.append("## Interpretation")
        lines.append(
            "The v8.109 artifact plans the future carrier-type selection decision boundary. "
            "It defines selection criteria and decision questions, but does not select a carrier type, "
            "does not execute a selection decision, does not execute refinement, does not create new draft clauses, "
            "does not execute definitions, does not complete Sigma_A, does not create theorem candidates, "
            "does not prove theorems, does not provide proof assistant verification, does not provide external validation, "
            "and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute a carrier-type selection decision only after this boundary plan is closed.",
            "Keep carrier selection separate from carrier refinement execution.",
            "Keep carrier refinement execution separate from Sigma_A completion.",
            "Keep time-index selection separate from carrier selection.",
            "Keep Sigma_A completion separate from theorem candidate planning.",
            "Keep theorem candidate planning separate from theorem proof.",
            "Keep proof assistant verification separate from proof execution.",
            "Keep validation, citation work, and manuscript readiness separate.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = [
            "does not",
            "not selected",
            "not executed",
            "not completed",
            "not created",
            "plan",
            "boundary",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not select a carrier type",
            "does not execute a carrier-type selection decision",
            "does not execute carrier refinement",
            "does not execute time-index refinement",
            "does not execute Sigma_A refinement",
            "does not create new Sigma_A draft clauses",
            "does not execute a new definition draft",
            "does not execute definitions",
            "does not complete Sigma_A",
            "does not complete any formal definition",
            "does not complete formalization",
            "does not create theorem candidates",
            "does not prove a theorem",
            "does not run proof execution",
            "does not provide proof assistant verification",
            "does not prove the full framework",
            "does not provide external validation",
            "does not perform an independent experiment",
            "does not approve manuscript submission readiness",
            "does not add new citations",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_positive_counter_names = {
            "carrier type selection count",
            "carrier type selection decision count",
            "carrier type selection execution count",
            "carrier type refinement execution count",
            "carrier refinement execution count",
            "time index refinement execution count",
            "time-index refinement execution count",
            "sigma_a refinement execution count",
            "sigma a refinement execution count",
            "new sigma_a draft clause count",
            "new sigma a draft clause count",
            "new definition draft execution count",
            "definition inventory execution count",
            "definition execution count",
            "new definition execution count",
            "completed formal definition count",
            "formalization complete count",
            "sigma_a definition completion count",
            "sigma a definition completion count",
            "stabilization predicate definition completion count",
            "attractor class definition completion count",
            "constraint region definition completion count",
            "causal mass definition completion count",
            "observer projection definition completion count",
            "completion decision count",
            "completion execution count",
            "completion execution authorized count",
            "theorem candidate plan count",
            "new theorem proven count",
            "proof assistant verification count",
            "formal mathematical proof count",
            "formal proof execution count",
            "proof execution count",
            "proof gap resolution count",
            "definition completion execution count",
            "full framework formal proof count",
            "external validation count",
            "independent experiment count",
            "manuscript submission ready count",
            "readiness approval count",
            "new citation added count",
        }

        unsafe_phrases = [
            "carrier type selected",
            "carrier selection completed",
            "carrier-type selection decision executed",
            "carrier refinement executed",
            "Sigma_A refinement executed",
            "Sigma_A definition completed",
            "Sigma_A completion achieved",
            "formal definition completed",
            "formal definitions completed",
            "theorem candidate created",
            "theorem proven",
            "proof assistant verification complete",
            "framework proven",
            "external validation complete",
            "manuscript ready",
        ]

        protective_markers = [
            "does not",
            "do not",
            "cannot",
            "not selected",
            "not executed",
            "not completed",
            "not created",
            "not provide",
            "not approve",
            "not add",
            "not run",
            "plan",
            "planned",
            "planning",
            "boundary",
            "decision question",
            "decision test",
            "blocked overreach",
            "separate",
            "carried",
            "cumulative limited",
            "remain absent",
            "remains absent",
            "remain zero",
            "remains zero",
            "at zero",
            "zero",
            "count: 0",
        ]

        count = 0
        for raw_line in text.splitlines():
            line = raw_line.strip().lstrip("-").strip()
            lowered = line.lower()

            if not lowered:
                continue

            counter_match = re.match(r"^([a-z0-9_ /-]+ count):\s*([0-9]+)\s*$", lowered)
            if counter_match:
                counter_name = counter_match.group(1).replace("_", " ").strip()
                value = int(counter_match.group(2))
                if value > 0 and counter_name in forbidden_positive_counter_names:
                    count += 1
                continue

            if any(marker in lowered for marker in protective_markers):
                continue

            for phrase in unsafe_phrases:
                if phrase.lower() in lowered:
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
    report = SigmaACarrierTypeSelectionDecisionBoundaryPlanBuilder().run()
    print(f"Wrote {report.output_path}")
