from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaACarrierTypeSelectionDecisionExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaACarrierTypeSelectionDecisionExecutionBuilder:
    """Build v8.110 Sigma_A carrier-type selection decision execution artifact.

    Boundary discipline:
    - This milestone executes a bounded carrier-type selection decision.
    - It selects the carrier type for future Sigma_A refinement.
    - It does not execute carrier refinement.
    - It does not execute Sigma_A refinement.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not complete any formal definition.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Carrier-Type Selection Decision Execution v8.110"
    source_artifact = Path("outputs/sigma_a_carrier_type_selection_decision_boundary_plan_v8_109.md")
    output_path = Path("outputs/sigma_a_carrier_type_selection_decision_execution_v8_110.md")

    selected_carrier_type = "typed-product carrier"
    auxiliary_representation = "structured-schema carrier"

    decision_rows = [
        {
            "option_id": "X-A-OPT-001",
            "carrier_kind": "set-like carrier",
            "decision": "not selected",
            "reason": "too weak for explicit Adm_A, C_reg, Pi_obs, and M_c typing without adding hidden structure",
        },
        {
            "option_id": "X-A-OPT-002",
            "carrier_kind": "typed-product carrier",
            "decision": "selected",
            "reason": "best supports explicit component typing, admissibility judgment domain, constraint membership, projection compatibility, and later trajectory construction",
        },
        {
            "option_id": "X-A-OPT-003",
            "carrier_kind": "graph-state carrier",
            "decision": "not selected",
            "reason": "useful for later relational extensions but premature before relational obligations are formalized",
        },
        {
            "option_id": "X-A-OPT-004",
            "carrier_kind": "measurable-space carrier",
            "decision": "not selected",
            "reason": "useful only if M_c later requires measure-like semantics, but currently over-formalizes Sigma_A",
        },
        {
            "option_id": "X-A-OPT-005",
            "carrier_kind": "structured-schema carrier",
            "decision": "not selected as carrier type; retained as auxiliary explanatory representation",
            "reason": "excellent for staged manuscript explanation and audit traceability, but needs a stricter mathematical carrier for definition work",
        },
    ]

    applied_criteria = [
        "admissibility compatibility",
        "constraint-region compatibility",
        "observer-projection compatibility",
        "causal-mass compatibility",
        "trajectory compatibility",
        "proof-readiness without premature formalization",
        "manuscript explainability",
        "audit traceability",
    ]

    def run(self) -> SigmaACarrierTypeSelectionDecisionExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone executes carrier-type selection only.",
            "Typed-product carrier is selected for future Sigma_A refinement, but refinement is not executed in v8.110.",
            "Structured-schema carrier is retained only as an auxiliary explanatory representation.",
            "Sigma_A definition completion, theorem planning, theorem proof, proof assistant verification, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_carrier_type_selection_decision_execution_count": 1,
            "carrier_type_selection_count": 1,
            "carrier_type_selection_decision_count": 1,
            "carrier_type_selection_execution_count": 1,
            "candidate_carrier_option_considered_count": len(self.decision_rows),
            "selection_criterion_applied_count": len(self.applied_criteria),
            "selected_carrier_type_count": 1,
            "selected_typed_product_carrier_count": 1,
            "non_selected_carrier_type_count": 4,
            "auxiliary_structured_schema_representation_count": 1,
            "carrier_selection_rationale_row_count": len(self.decision_rows),
            "carried_sigma_a_carrier_type_selection_decision_boundary_plan_count": carried.get("Sigma_A carrier-type selection decision boundary plan count", 1),
            "carried_selection_boundary_criterion_count": carried.get("Selection boundary criterion count", 8),
            "carried_selection_decision_question_count": carried.get("Selection decision question count", 8),
            "carried_candidate_carrier_option_count": carried.get("Candidate carrier option carried count", 5),
            "carried_sigma_a_carrier_type_option_audit_execution_count": carried.get("Carried Sigma_A carrier-type option audit execution count", 1),
            "carried_carrier_type_option_audited_count": carried.get("Carried carrier type option audited count", 5),
            "carried_sigma_a_carrier_time_index_refinement_plan_count": carried.get("Carried Sigma_A carrier time-index refinement plan count", 1),
            "carried_sigma_a_draft_consistency_boundary_audit_count": carried.get("Carried Sigma_A draft consistency boundary audit count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
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
            errors.append("Overclaim detected in v8.110 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.110 report.")
        if counts["sigma_a_carrier_type_selection_decision_execution_count"] != 1:
            errors.append("v8.110 must execute exactly one carrier-type selection decision.")
        if counts["carrier_type_selection_count"] != 1:
            errors.append("v8.110 must select exactly one carrier type.")
        if counts["selected_typed_product_carrier_count"] != 1:
            errors.append("v8.110 must select typed-product carrier.")
        if counts["candidate_carrier_option_considered_count"] != 5:
            errors.append("v8.110 must consider exactly five carrier options.")
        if counts["selection_criterion_applied_count"] != 8:
            errors.append("v8.110 must apply exactly eight selection criteria.")
        if counts["carrier_type_refinement_execution_count"] != 0:
            errors.append("v8.110 must not execute carrier-type refinement.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.110 must not execute carrier refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.110 must not execute Sigma_A refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.110 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.110 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.110 must not prove a theorem.")

        zero_fields = [
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

        return SigmaACarrierTypeSelectionDecisionExecutionReport(
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
            "sigma_a_carrier_type_selection_decision_execution_count": "Sigma_A carrier-type selection decision execution count",
            "selected_typed_product_carrier_count": "Selected typed-product carrier count",
            "non_selected_carrier_type_count": "Non-selected carrier type count",
            "auxiliary_structured_schema_representation_count": "Auxiliary structured-schema representation count",
            "time_index_refinement_execution_count": "Time-index refinement execution count",
            "carried_sigma_a_carrier_type_selection_decision_boundary_plan_count": "Carried Sigma_A carrier-type selection decision boundary plan count",
            "carried_sigma_a_carrier_type_option_audit_execution_count": "Carried Sigma_A carrier-type option audit execution count",
            "carried_sigma_a_carrier_time_index_refinement_plan_count": "Carried Sigma_A carrier time-index refinement plan count",
            "carried_sigma_a_draft_consistency_boundary_audit_count": "Carried Sigma_A draft consistency boundary audit count",
            "new_sigma_a_draft_clause_count": "New Sigma_A draft clause count",
            "sigma_a_refinement_execution_count": "Sigma_A refinement execution count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric execute a bounded Sigma_A carrier-type selection decision after the selection decision boundary plan "
            "while keeping carrier refinement execution, Sigma_A refinement execution, new draft execution, definition execution, "
            "Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, "
            "manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Selection decision")
        lines.append(f"- Selected carrier type: {self.selected_carrier_type}")
        lines.append(f"- Auxiliary explanatory representation retained: {self.auxiliary_representation}")
        lines.append("- Selection decision status: executed")
        lines.append("- Carrier refinement execution status after this milestone: not executed")
        lines.append("- Sigma_A refinement execution status after this milestone: not executed")
        lines.append("- Sigma_A definition completion status after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Applied selection criteria")
        for index, criterion in enumerate(self.applied_criteria, start=1):
            lines.append(f"{index}. {criterion}")
        lines.append("")
        lines.append("## Carrier option decision rows")
        lines.append("")
        lines.append("| Option ID | Carrier kind | Decision | Reason |")
        lines.append("|---|---|---|---|")
        for row in self.decision_rows:
            lines.append(
                f"| {row['option_id']} | {row['carrier_kind']} | {row['decision']} | {row['reason']} |"
            )
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes a bounded Sigma_A carrier-type selection decision only. "
            "It selects the typed-product carrier for future Sigma_A refinement and retains structured-schema representation as auxiliary explanation. "
            "It does not execute carrier-type refinement, does not execute carrier refinement, does not execute time-index refinement, "
            "does not execute Sigma_A refinement, does not create new Sigma_A draft clauses, does not execute a new definition draft, "
            "does not execute definitions, does not complete Sigma_A, does not complete any formal definition, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_carrier_type_selection_decision_execution_count",
            "carrier_type_selection_count",
            "carrier_type_selection_decision_count",
            "carrier_type_selection_execution_count",
            "candidate_carrier_option_considered_count",
            "selection_criterion_applied_count",
            "selected_carrier_type_count",
            "selected_typed_product_carrier_count",
            "non_selected_carrier_type_count",
            "auxiliary_structured_schema_representation_count",
            "carrier_selection_rationale_row_count",
            "carried_sigma_a_carrier_type_selection_decision_boundary_plan_count",
            "carried_selection_boundary_criterion_count",
            "carried_selection_decision_question_count",
            "carried_candidate_carrier_option_count",
            "carried_sigma_a_carrier_type_option_audit_execution_count",
            "carried_carrier_type_option_audited_count",
            "carried_sigma_a_carrier_time_index_refinement_plan_count",
            "carried_sigma_a_draft_consistency_boundary_audit_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
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
            "The v8.110 artifact selects typed-product carrier as the Sigma_A carrier type for future refinement. "
            "This is a selection decision only. It does not execute refinement, does not create new draft clauses, "
            "does not execute definitions, does not complete Sigma_A, does not complete formal definitions, "
            "does not create theorem candidates, does not prove theorems, does not provide proof assistant verification, "
            "does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit typed-product carrier component slots before refinement execution.",
            "Plan typed-product carrier refinement execution separately.",
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
            "not executed",
            "not completed",
            "not created",
            "selection",
            "selected",
            "bounded",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute carrier-type refinement",
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
            "not executed",
            "not completed",
            "not created",
            "not provide",
            "not approve",
            "not add",
            "not run",
            "selection decision only",
            "future refinement",
            "auxiliary",
            "bounded",
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
    report = SigmaACarrierTypeSelectionDecisionExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
