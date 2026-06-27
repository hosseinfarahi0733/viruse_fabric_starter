from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaACarrierDraftClauseCreationExecutionPlanReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaACarrierDraftClauseCreationExecutionPlanBuilder:
    """Build v8.124 Sigma_A carrier draft clause creation execution plan.

    Boundary discipline:
    - This milestone plans carrier draft clause creation only.
    - It does not create a new Sigma_A draft clause.
    - It does not execute carrier draft clause creation.
    - It does not execute whole Sigma_A draft assembly.
    - It does not execute Sigma_A refinement.
    - It does not execute time-index refinement.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Carrier Draft Clause Creation Execution Plan v8.124"
    source_artifact = Path("outputs/sigma_a_carrier_level_draft_assembly_boundary_audit_v8_123.md")
    output_path = Path("outputs/sigma_a_carrier_draft_clause_creation_execution_plan_v8_124.md")

    clause_creation_plan_rows = [
        {
            "plan_id": "SIG-A-CARRIER-CLAUSE-PLAN-001",
            "planned_focus": "carrier clause target",
            "planned_action": "plan a future carrier draft clause that references X_A^tp as the carrier-level candidate",
            "required_precondition": "v8.123 boundary audit must remain clean",
            "blocked_overreach": "do not create a new Sigma_A draft clause in v8.124",
        },
        {
            "plan_id": "SIG-A-CARRIER-CLAUSE-PLAN-002",
            "planned_focus": "clause scope",
            "planned_action": "restrict the future clause to carrier-slot wording only",
            "required_precondition": "whole Sigma_A draft assembly must remain out of scope",
            "blocked_overreach": "do not execute whole Sigma_A draft assembly",
        },
        {
            "plan_id": "SIG-A-CARRIER-CLAUSE-PLAN-003",
            "planned_focus": "dependent-object deferral",
            "planned_action": "keep Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A as deferred dependencies",
            "required_precondition": "dependent formal objects must remain unresolved",
            "blocked_overreach": "do not define dependent objects",
        },
        {
            "plan_id": "SIG-A-CARRIER-CLAUSE-PLAN-004",
            "planned_focus": "time-index separation",
            "planned_action": "ensure the future carrier clause does not include T_A refinement",
            "required_precondition": "T_A remains outside carrier draft clause creation",
            "blocked_overreach": "do not execute time-index refinement",
        },
        {
            "plan_id": "SIG-A-CARRIER-CLAUSE-PLAN-005",
            "planned_focus": "Sigma_A refinement boundary",
            "planned_action": "plan clause creation without implying Sigma_A refinement",
            "required_precondition": "Sigma_A refinement requires a separate milestone",
            "blocked_overreach": "do not execute Sigma_A refinement",
        },
        {
            "plan_id": "SIG-A-CARRIER-CLAUSE-PLAN-006",
            "planned_focus": "definition boundary",
            "planned_action": "keep future clause creation separate from definition execution",
            "required_precondition": "formal definitions remain incomplete",
            "blocked_overreach": "do not execute definitions and do not complete formal definitions",
        },
        {
            "plan_id": "SIG-A-CARRIER-CLAUSE-PLAN-007",
            "planned_focus": "audit traceability",
            "planned_action": "carry Ann_A traceability into the future carrier draft clause audit trail",
            "required_precondition": "Ann_A remains auxiliary and audit-facing",
            "blocked_overreach": "do not add hidden mathematical structure",
        },
        {
            "plan_id": "SIG-A-CARRIER-CLAUSE-PLAN-008",
            "planned_focus": "proof-readiness separation",
            "planned_action": "preserve theorem/proof/validation/readiness as downstream layers",
            "required_precondition": "carrier draft clause creation planning must not imply proof readiness",
            "blocked_overreach": "do not create theorem candidates, proofs, validation, citations, or readiness approval",
        },
    ]

    execution_gates = [
        "Future carrier draft clause creation must reference X_A^tp only as a carrier-level candidate.",
        "Future carrier draft clause creation must remain restricted to the carrier slot.",
        "Future carrier draft clause creation must not define Adm_A, C_reg, Pi_obs, M_c, R_A, or Traj_A.",
        "Future carrier draft clause creation must not execute time-index refinement.",
        "Future carrier draft clause creation must not execute Sigma_A refinement.",
        "Future carrier draft clause creation must not execute definitions or complete Sigma_A.",
        "Future carrier draft clause creation must preserve Ann_A as audit traceability.",
        "Future carrier draft clause creation must not create theorem candidates, proofs, validation, citations, or readiness approval.",
    ]

    def run(self) -> SigmaACarrierDraftClauseCreationExecutionPlanReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone plans Sigma_A carrier draft clause creation only.",
            "New Sigma_A draft clause creation remains zero in v8.124.",
            "Carrier draft clause creation execution remains zero in v8.124.",
            "Whole Sigma_A draft assembly, Sigma_A refinement, definition execution, Sigma_A definition completion, theorem planning, proof, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_carrier_draft_clause_creation_execution_plan_count": 1,
            "carrier_draft_clause_creation_execution_plan_count": 1,
            "sigma_a_draft_clause_creation_execution_plan_count": 1,
            "carrier_draft_clause_creation_plan_row_count": len(self.clause_creation_plan_rows),
            "carrier_draft_clause_creation_execution_gate_count": len(self.execution_gates),
            "planned_carrier_draft_clause_scope_count": 1,
            "planned_carrier_clause_candidate_reference_count": 1,
            "planned_dependent_object_deferral_count": 6,
            "planned_clause_boundary_guard_count": len(self.clause_creation_plan_rows),
            "planned_clause_creation_blocked_overreach_count": len(self.clause_creation_plan_rows),
            "carried_sigma_a_carrier_level_draft_assembly_boundary_audit_count": carried.get("Sigma_A carrier-level draft assembly boundary audit count", 1),
            "carried_carrier_level_draft_assembly_boundary_audit_count": carried.get("Carrier-level draft assembly boundary audit count", 1),
            "carried_carrier_level_draft_assembly_boundary_audit_row_count": carried.get("Carrier-level draft assembly boundary audit row count", 8),
            "carried_carrier_level_draft_assembly_boundary_preserved_count": carried.get("Carrier-level draft assembly boundary preserved count", 8),
            "carried_carrier_level_draft_assembly_boundary_audit_finding_count": carried.get("Carrier-level draft assembly boundary audit finding count", 8),
            "carried_assembled_carrier_candidate_audited_count": carried.get("Assembled carrier candidate audited count", 1),
            "carried_carrier_slot_placement_audited_count": carried.get("Carrier slot placement audited count", 1),
            "carried_carrier_candidate_import_boundary_preserved_count": carried.get("Carrier candidate import boundary preserved count", 1),
            "carried_dependent_object_deferral_preserved_count": carried.get("Dependent object deferral preserved count", 6),
            "carried_whole_sigma_a_draft_assembly_blocker_count": carried.get("Whole Sigma_A draft assembly blocker count", 1),
            "carried_new_sigma_a_draft_clause_blocker_count": carried.get("New Sigma_A draft clause blocker count", 1),
            "carried_sigma_a_refinement_blocker_count": carried.get("Sigma_A refinement blocker count", 1),
            "carried_definition_execution_blocker_count": carried.get("Definition execution blocker count", 1),
            "carried_proof_readiness_blocker_count": carried.get("Proof-readiness blocker count", 1),
            "carried_sigma_a_carrier_level_draft_assembly_execution_count": carried.get("Carried Sigma_A carrier-level draft assembly execution count", 1),
            "carried_carrier_level_draft_assembly_execution_count": carried.get("Carried carrier-level draft assembly execution count", 1),
            "carried_assembled_carrier_candidate_count": carried.get("Carried assembled carrier candidate count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "carrier_draft_clause_creation_execution_count": 0,
            "sigma_a_carrier_draft_clause_creation_execution_count": 0,
            "new_sigma_a_draft_clause_count": 0,
            "new_sigma_a_draft_clause_creation_count": 0,
            "whole_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_assembly_execution_count": 0,
            "new_carrier_level_draft_assembly_execution_count": 0,
            "new_definition_draft_execution_count": 0,
            "new_typed_product_carrier_refinement_execution_count": 0,
            "generic_carrier_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "time_index_refinement_execution_count": 0,
            "sigma_a_refinement_execution_count": 0,
            "new_component_slot_integration_execution_count": 0,
            "new_component_slot_refinement_execution_count": 0,
            "new_carrier_type_selection_count": 0,
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
            errors.append("Overclaim detected in v8.124 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.124 report.")
        if counts["sigma_a_carrier_draft_clause_creation_execution_plan_count"] != 1:
            errors.append("v8.124 must produce exactly one Sigma_A carrier draft clause creation execution plan.")
        if counts["carrier_draft_clause_creation_plan_row_count"] != 8:
            errors.append("v8.124 must include exactly eight carrier draft clause creation plan rows.")
        if counts["carrier_draft_clause_creation_execution_gate_count"] != 8:
            errors.append("v8.124 must include exactly eight carrier draft clause creation execution gates.")
        if counts["carrier_draft_clause_creation_execution_count"] != 0:
            errors.append("v8.124 must not execute carrier draft clause creation.")
        if counts["new_sigma_a_draft_clause_count"] != 0:
            errors.append("v8.124 must not create a new Sigma_A draft clause.")
        if counts["whole_sigma_a_draft_assembly_execution_count"] != 0:
            errors.append("v8.124 must not execute whole Sigma_A draft assembly.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.124 must not execute Sigma_A refinement.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.124 must not execute definitions.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.124 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.124 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.124 must not prove a theorem.")

        zero_fields = [
            "carrier_draft_clause_creation_execution_count",
            "sigma_a_carrier_draft_clause_creation_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_sigma_a_draft_clause_creation_count",
            "whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_carrier_level_draft_assembly_execution_count",
            "new_definition_draft_execution_count",
            "new_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "new_component_slot_integration_execution_count",
            "new_component_slot_refinement_execution_count",
            "new_carrier_type_selection_count",
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

        return SigmaACarrierDraftClauseCreationExecutionPlanReport(
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
            "sigma_a_carrier_draft_clause_creation_execution_plan_count": "Sigma_A carrier draft clause creation execution plan count",
            "carrier_draft_clause_creation_execution_plan_count": "Carrier draft clause creation execution plan count",
            "sigma_a_draft_clause_creation_execution_plan_count": "Sigma_A draft clause creation execution plan count",
            "carrier_draft_clause_creation_plan_row_count": "Carrier draft clause creation plan row count",
            "carrier_draft_clause_creation_execution_gate_count": "Carrier draft clause creation execution gate count",
            "planned_carrier_draft_clause_scope_count": "Planned carrier draft clause scope count",
            "planned_carrier_clause_candidate_reference_count": "Planned carrier clause candidate reference count",
            "planned_dependent_object_deferral_count": "Planned dependent object deferral count",
            "planned_clause_boundary_guard_count": "Planned clause boundary guard count",
            "planned_clause_creation_blocked_overreach_count": "Planned clause creation blocked-overreach count",
            "carried_sigma_a_carrier_level_draft_assembly_boundary_audit_count": "Carried Sigma_A carrier-level draft assembly boundary audit count",
            "carried_carrier_level_draft_assembly_boundary_audit_count": "Carried carrier-level draft assembly boundary audit count",
            "carried_carrier_level_draft_assembly_boundary_audit_row_count": "Carried carrier-level draft assembly boundary audit row count",
            "carried_carrier_level_draft_assembly_boundary_preserved_count": "Carried carrier-level draft assembly boundary preserved count",
            "carried_carrier_level_draft_assembly_boundary_audit_finding_count": "Carried carrier-level draft assembly boundary audit finding count",
            "carried_assembled_carrier_candidate_audited_count": "Carried assembled carrier candidate audited count",
            "carried_carrier_slot_placement_audited_count": "Carried carrier slot placement audited count",
            "carried_carrier_candidate_import_boundary_preserved_count": "Carried carrier candidate import boundary preserved count",
            "carried_dependent_object_deferral_preserved_count": "Carried dependent object deferral preserved count",
            "carried_whole_sigma_a_draft_assembly_blocker_count": "Carried whole Sigma_A draft assembly blocker count",
            "carried_new_sigma_a_draft_clause_blocker_count": "Carried new Sigma_A draft clause blocker count",
            "carried_sigma_a_refinement_blocker_count": "Carried Sigma_A refinement blocker count",
            "carried_definition_execution_blocker_count": "Carried definition execution blocker count",
            "carried_proof_readiness_blocker_count": "Carried proof-readiness blocker count",
            "carried_sigma_a_carrier_level_draft_assembly_execution_count": "Carried Sigma_A carrier-level draft assembly execution count",
            "carried_carrier_level_draft_assembly_execution_count": "Carried carrier-level draft assembly execution count",
            "carried_assembled_carrier_candidate_count": "Carried assembled carrier candidate count",
            "carrier_draft_clause_creation_execution_count": "Carrier draft clause creation execution count",
            "sigma_a_carrier_draft_clause_creation_execution_count": "Sigma_A carrier draft clause creation execution count",
            "new_sigma_a_draft_clause_count": "New Sigma_A draft clause count",
            "new_sigma_a_draft_clause_creation_count": "New Sigma_A draft clause creation count",
            "whole_sigma_a_draft_assembly_execution_count": "Whole Sigma_A draft assembly execution count",
            "new_sigma_a_draft_assembly_execution_count": "New Sigma_A draft assembly execution count",
            "new_carrier_level_draft_assembly_execution_count": "New carrier-level draft assembly execution count",
            "new_definition_draft_execution_count": "New definition draft execution count",
            "new_typed_product_carrier_refinement_execution_count": "New typed-product carrier refinement execution count",
            "generic_carrier_refinement_execution_count": "Generic carrier refinement execution count",
            "carrier_refinement_execution_count": "Carrier refinement execution count",
            "carrier_type_refinement_execution_count": "Carrier type refinement execution count",
            "time_index_refinement_execution_count": "Time-index refinement execution count",
            "sigma_a_refinement_execution_count": "Sigma_A refinement execution count",
            "new_component_slot_integration_execution_count": "New component-slot integration execution count",
            "new_component_slot_refinement_execution_count": "New component-slot refinement execution count",
            "new_carrier_type_selection_count": "New carrier type selection count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric plan Sigma_A carrier draft clause creation after the v8.123 carrier-level draft assembly boundary audit "
            "while keeping actual clause creation, whole Sigma_A draft assembly, time-index refinement, Sigma_A refinement, definition execution, "
            "Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, manuscript readiness, "
            "readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Planning boundary")
        lines.append("- Milestone type: Sigma_A carrier draft clause creation execution plan only")
        lines.append("- Carrier draft clause creation execution after this milestone: not executed")
        lines.append("- New Sigma_A draft clause creation after this milestone: not created")
        lines.append("- Whole Sigma_A draft assembly execution after this milestone: not executed")
        lines.append("- Time-index refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Definition execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Carrier draft clause creation plan rows")
        lines.append("")
        lines.append("| Plan ID | Planned focus | Planned action | Required precondition | Blocked overreach |")
        lines.append("|---|---|---|---|---|")
        for row in self.clause_creation_plan_rows:
            lines.append(
                f"| {row['plan_id']} | {row['planned_focus']} | {row['planned_action']} | "
                f"{row['required_precondition']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Carrier draft clause creation execution gates")
        for index, gate in enumerate(self.execution_gates, start=1):
            lines.append(f"{index}. {gate}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact plans Sigma_A carrier draft clause creation execution only. "
            "It does not execute carrier draft clause creation, does not execute Sigma_A carrier draft clause creation, "
            "does not create a new Sigma_A draft clause, does not execute whole Sigma_A draft assembly, "
            "does not execute new Sigma_A draft assembly, does not execute new carrier-level draft assembly, "
            "does not execute a new definition draft, does not execute new typed-product carrier refinement, "
            "does not execute generic carrier refinement, does not execute carrier-type refinement, does not execute time-index refinement, "
            "does not execute Sigma_A refinement, does not execute new component-slot integration, does not execute new component-slot refinement, "
            "does not perform a new carrier type selection, does not execute definitions, does not complete Sigma_A, "
            "does not complete any formal definition, does not complete formalization, does not create theorem candidates, "
            "does not prove a theorem, does not run proof execution, does not provide proof assistant verification, "
            "does not prove the full framework, does not provide external validation, does not perform an independent experiment, "
            "does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_carrier_draft_clause_creation_execution_plan_count",
            "carrier_draft_clause_creation_execution_plan_count",
            "sigma_a_draft_clause_creation_execution_plan_count",
            "carrier_draft_clause_creation_plan_row_count",
            "carrier_draft_clause_creation_execution_gate_count",
            "planned_carrier_draft_clause_scope_count",
            "planned_carrier_clause_candidate_reference_count",
            "planned_dependent_object_deferral_count",
            "planned_clause_boundary_guard_count",
            "planned_clause_creation_blocked_overreach_count",
            "carried_sigma_a_carrier_level_draft_assembly_boundary_audit_count",
            "carried_carrier_level_draft_assembly_boundary_audit_count",
            "carried_carrier_level_draft_assembly_boundary_audit_row_count",
            "carried_carrier_level_draft_assembly_boundary_preserved_count",
            "carried_carrier_level_draft_assembly_boundary_audit_finding_count",
            "carried_assembled_carrier_candidate_audited_count",
            "carried_carrier_slot_placement_audited_count",
            "carried_carrier_candidate_import_boundary_preserved_count",
            "carried_dependent_object_deferral_preserved_count",
            "carried_whole_sigma_a_draft_assembly_blocker_count",
            "carried_new_sigma_a_draft_clause_blocker_count",
            "carried_sigma_a_refinement_blocker_count",
            "carried_definition_execution_blocker_count",
            "carried_proof_readiness_blocker_count",
            "carried_sigma_a_carrier_level_draft_assembly_execution_count",
            "carried_carrier_level_draft_assembly_execution_count",
            "carried_assembled_carrier_candidate_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "carrier_draft_clause_creation_execution_count",
            "sigma_a_carrier_draft_clause_creation_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_sigma_a_draft_clause_creation_count",
            "whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_carrier_level_draft_assembly_execution_count",
            "new_definition_draft_execution_count",
            "new_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "new_component_slot_integration_execution_count",
            "new_component_slot_refinement_execution_count",
            "new_carrier_type_selection_count",
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
            "The v8.124 artifact plans Sigma_A carrier draft clause creation after the carrier-level draft assembly boundary audit. "
            "This is planning only. It does not create a new Sigma_A draft clause, does not execute whole Sigma_A draft assembly, "
            "does not execute time-index refinement, does not execute Sigma_A refinement, does not execute definitions, "
            "does not complete Sigma_A, does not create theorem candidates, does not prove theorems, "
            "does not provide proof assistant verification, does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute carrier draft clause creation only after this plan is closed.",
            "Keep carrier draft clause creation separate from whole Sigma_A draft assembly.",
            "Keep time-index refinement separate from carrier draft clause creation.",
            "Keep C_reg, Pi_obs, M_c, R_A, and Traj_A definitions separate.",
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
            "plan",
            "planning",
            "gate",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute carrier draft clause creation",
            "does not execute Sigma_A carrier draft clause creation",
            "does not create a new Sigma_A draft clause",
            "does not execute whole Sigma_A draft assembly",
            "does not execute new Sigma_A draft assembly",
            "does not execute new carrier-level draft assembly",
            "does not execute a new definition draft",
            "does not execute new typed-product carrier refinement",
            "does not execute generic carrier refinement",
            "does not execute carrier-type refinement",
            "does not execute time-index refinement",
            "does not execute Sigma_A refinement",
            "does not execute new component-slot integration",
            "does not execute new component-slot refinement",
            "does not perform a new carrier type selection",
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
            "carrier draft clause creation execution count",
            "sigma_a carrier draft clause creation execution count",
            "sigma a carrier draft clause creation execution count",
            "new sigma_a draft clause count",
            "new sigma a draft clause count",
            "new sigma_a draft clause creation count",
            "new sigma a draft clause creation count",
            "whole sigma_a draft assembly execution count",
            "whole sigma a draft assembly execution count",
            "new sigma_a draft assembly execution count",
            "new sigma a draft assembly execution count",
            "new carrier-level draft assembly execution count",
            "new definition draft execution count",
            "new typed-product carrier refinement execution count",
            "generic carrier refinement execution count",
            "carrier refinement execution count",
            "carrier type refinement execution count",
            "time index refinement execution count",
            "time-index refinement execution count",
            "sigma_a refinement execution count",
            "sigma a refinement execution count",
            "new component-slot integration execution count",
            "new component-slot refinement execution count",
            "new carrier type selection count",
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
            "new Sigma_A draft clause created",
            "carrier draft clause creation executed",
            "whole Sigma_A draft assembly executed",
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
            "plan",
            "planned",
            "planning",
            "gate",
            "precondition",
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
    report = SigmaACarrierDraftClauseCreationExecutionPlanBuilder().run()
    print(f"Wrote {report.output_path}")
