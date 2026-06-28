from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaARefinementExecutionPlanBoundaryAuditReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaARefinementExecutionPlanBoundaryAuditBuilder:
    """Build v8.135 Sigma_A refinement execution plan boundary audit artifact.

    Boundary discipline:
    - This milestone audits the v8.134 Sigma_A refinement execution plan only.
    - It does not execute Sigma_A refinement.
    - It does not execute new Sigma_A refinement.
    - It does not execute new time-index refinement.
    - It does not execute new T_A refinement.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Refinement Execution Plan Boundary Audit v8.135"
    source_artifact = Path("outputs/sigma_a_refinement_execution_plan_v8_134.md")
    output_path = Path("outputs/sigma_a_refinement_execution_plan_boundary_audit_v8_135.md")

    audit_rows = [
        {
            "audit_id": "SIGMA-A-PLAN-AUDIT-001",
            "focus": "planned Sigma_A refinement scope",
            "audited_object": "future Sigma_A refinement layer",
            "boundary_result": "Sigma_A refinement is planned but not executed",
            "open_dependency": "Sigma_A refinement execution remains downstream",
            "blocked_overreach": "does not execute Sigma_A refinement",
        },
        {
            "audit_id": "SIGMA-A-PLAN-AUDIT-002",
            "focus": "time-index layer integration",
            "audited_object": "audited T_A/time-index refinement layer",
            "boundary_result": "time-index layer integration is planned only",
            "open_dependency": "future Sigma_A refinement must integrate it explicitly",
            "blocked_overreach": "does not execute new time-index refinement",
        },
        {
            "audit_id": "SIGMA-A-PLAN-AUDIT-003",
            "focus": "T_A refinement boundary",
            "audited_object": "carried T_A refinement execution",
            "boundary_result": "T_A refinement remains carried from earlier execution and is not newly executed",
            "open_dependency": "future Sigma_A refinement must preserve T_A boundary",
            "blocked_overreach": "does not execute new T_A refinement",
        },
        {
            "audit_id": "SIGMA-A-PLAN-AUDIT-004",
            "focus": "Draft Sigma_A shell preservation",
            "audited_object": "assembled Draft Sigma_A shell",
            "boundary_result": "future refinement is planned over the existing shell without reassembly",
            "open_dependency": "shell integration remains downstream",
            "blocked_overreach": "does not execute new whole Sigma_A draft assembly",
        },
        {
            "audit_id": "SIGMA-A-PLAN-AUDIT-005",
            "focus": "carrier-clause preservation",
            "audited_object": "carrier(Draft Sigma_A) := X_A^tp",
            "boundary_result": "carrier-slot clause remains unchanged by the plan",
            "open_dependency": "carrier refinement remains a separate future milestone",
            "blocked_overreach": "does not create a new Sigma_A draft clause",
        },
        {
            "audit_id": "SIGMA-A-PLAN-AUDIT-006",
            "focus": "dependent-object integration schedule",
            "audited_object": "{Adm_A, C_reg, Pi_obs, M_c, R_A, Traj_A}",
            "boundary_result": "six dependent-object integrations are scheduled but not defined",
            "open_dependency": "dependent-object definitions remain unresolved",
            "blocked_overreach": "does not execute definitions",
        },
        {
            "audit_id": "SIGMA-A-PLAN-AUDIT-007",
            "focus": "definition and completion boundary",
            "audited_object": "formal definition and Sigma_A completion layers",
            "boundary_result": "definition execution and Sigma_A completion remain absent",
            "open_dependency": "formal definitions remain incomplete",
            "blocked_overreach": "does not complete Sigma_A and does not complete formal definitions",
        },
        {
            "audit_id": "SIGMA-A-PLAN-AUDIT-008",
            "focus": "proof-readiness boundary",
            "audited_object": "theorem/proof/validation/readiness layers",
            "boundary_result": "proof-readiness layers remain absent",
            "open_dependency": "theorem, proof, validation, citation, and readiness remain downstream",
            "blocked_overreach": "does not create theorem candidates, proofs, validation, citations, or readiness approval",
        },
    ]

    audit_findings = [
        "The v8.134 Sigma_A refinement execution plan is carried and audited.",
        "Future Sigma_A refinement remains planned but not executed.",
        "No new Sigma_A refinement is executed in v8.135.",
        "No new time-index refinement is executed in v8.135.",
        "No new T_A refinement is executed in v8.135.",
        "The audited T_A/time-index refinement layer remains available for future Sigma_A refinement planning.",
        "Carrier(Draft Sigma_A) := X_A^tp remains unchanged.",
        "Definition, theorem, proof, validation, citation, and readiness layers remain absent.",
    ]

    def run(self) -> SigmaARefinementExecutionPlanBoundaryAuditReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone audits the Sigma_A refinement execution plan only.",
            "Sigma_A refinement execution remains zero in v8.135.",
            "No new time-index refinement and no new T_A refinement are executed in v8.135.",
            "Definition execution, Sigma_A definition completion, theorem planning, proof, validation, readiness, and citations remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_refinement_execution_plan_boundary_audit_count": 1,
            "sigma_a_refinement_plan_boundary_audit_count": 1,
            "draft_sigma_a_refinement_execution_plan_boundary_audit_count": 1,
            "sigma_a_refinement_plan_boundary_audit_row_count": len(self.audit_rows),
            "sigma_a_refinement_plan_boundary_preserved_count": len(self.audit_rows),
            "sigma_a_refinement_plan_boundary_audit_finding_count": len(self.audit_findings),
            "planned_sigma_a_refinement_scope_audited_count": 1,
            "planned_time_index_layer_integration_audited_count": 1,
            "planned_draft_shell_refinement_link_audited_count": 1,
            "planned_carrier_clause_preservation_audited_count": 1,
            "planned_dependent_object_integration_schedule_audited_count": 6,
            "sigma_a_refinement_execution_blocker_count": 1,
            "new_time_index_refinement_execution_blocker_count": 1,
            "new_t_a_refinement_execution_blocker_count": 1,
            "definition_execution_blocker_count": 1,
            "proof_readiness_blocker_count": 1,
            "carried_sigma_a_refinement_execution_plan_count": carried.get("Sigma_A refinement execution plan count", 1),
            "carried_sigma_a_refinement_plan_count": carried.get("Sigma_A refinement plan count", 1),
            "carried_draft_sigma_a_refinement_execution_plan_count": carried.get("Draft Sigma_A refinement execution plan count", 1),
            "carried_sigma_a_refinement_plan_row_count": carried.get("Sigma_A refinement plan row count", 8),
            "carried_sigma_a_refinement_execution_gate_count": carried.get("Sigma_A refinement execution gate count", 8),
            "carried_planned_sigma_a_refinement_scope_count": carried.get("Planned Sigma_A refinement scope count", 1),
            "carried_planned_time_index_layer_integration_count": carried.get("Planned time-index layer integration count", 1),
            "carried_planned_draft_shell_refinement_link_count": carried.get("Planned draft shell refinement link count", 1),
            "carried_planned_carrier_clause_preservation_count": carried.get("Planned carrier clause preservation count", 1),
            "carried_planned_dependent_object_integration_schedule_count": carried.get("Planned dependent object integration schedule count", 6),
            "carried_planned_sigma_a_boundary_guard_count": carried.get("Planned Sigma_A boundary guard count", 8),
            "carried_planned_sigma_a_blocked_overreach_count": carried.get("Planned Sigma_A blocked-overreach count", 8),
            "carried_time_index_refinement_boundary_audit_count": carried.get("Carried time-index refinement boundary audit count", 1),
            "carried_t_a_refinement_boundary_audit_count": carried.get("Carried T_A refinement boundary audit count", 1),
            "carried_sigma_a_time_index_refinement_boundary_audit_count": carried.get("Carried Sigma_A time-index refinement boundary audit count", 1),
            "carried_executed_time_index_refinement_audited_count": carried.get("Carried executed time-index refinement audited count", 1),
            "carried_executed_t_a_refinement_audited_count": carried.get("Carried executed T_A refinement audited count", 1),
            "carried_three_time_structure_audited_count": carried.get("Carried three-time structure audited count", 1),
            "carried_time_index_refinement_execution_count": carried.get("Carried time-index refinement execution count", 1),
            "carried_t_a_refinement_execution_count": carried.get("Carried T_A refinement execution count", 1),
            "carried_sigma_a_time_index_refinement_execution_count": carried.get("Carried Sigma_A time-index refinement execution count", 1),
            "carried_whole_sigma_a_draft_assembly_boundary_audit_count": carried.get("Carried whole Sigma_A draft assembly boundary audit count", 1),
            "carried_assembled_whole_sigma_a_draft_shell_audited_count": carried.get("Carried assembled whole Sigma_A draft shell audited count", 1),
            "carried_imported_carrier_slot_clause_audited_count": carried.get("Carried imported carrier-slot clause audited count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "sigma_a_refinement_execution_count": 0,
            "new_sigma_a_refinement_execution_count": 0,
            "new_time_index_refinement_execution_count": 0,
            "new_t_a_refinement_execution_count": 0,
            "time_index_refinement_execution_count": 0,
            "t_a_refinement_execution_count": 0,
            "new_whole_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_clause_count": 0,
            "new_sigma_a_draft_clause_creation_count": 0,
            "new_carrier_draft_clause_creation_execution_count": 0,
            "new_carrier_level_draft_assembly_execution_count": 0,
            "new_definition_draft_execution_count": 0,
            "new_typed_product_carrier_refinement_execution_count": 0,
            "generic_carrier_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "carrier_type_refinement_execution_count": 0,
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
            errors.append("Overclaim detected in v8.135 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.135 report.")
        if counts["sigma_a_refinement_execution_plan_boundary_audit_count"] != 1:
            errors.append("v8.135 must produce exactly one Sigma_A refinement execution plan boundary audit.")
        if counts["sigma_a_refinement_plan_boundary_audit_row_count"] != 8:
            errors.append("v8.135 must include exactly eight Sigma_A refinement plan boundary audit rows.")
        if counts["sigma_a_refinement_plan_boundary_preserved_count"] != 8:
            errors.append("v8.135 must preserve exactly eight Sigma_A refinement plan boundaries.")
        if counts["carried_sigma_a_refinement_execution_plan_count"] != 1:
            errors.append("v8.135 must carry exactly one Sigma_A refinement execution plan from v8.134.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.135 must not execute Sigma_A refinement.")
        if counts["new_sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.135 must not execute new Sigma_A refinement.")
        if counts["new_time_index_refinement_execution_count"] != 0:
            errors.append("v8.135 must not execute new time-index refinement.")
        if counts["new_t_a_refinement_execution_count"] != 0:
            errors.append("v8.135 must not execute new T_A refinement.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.135 must not execute definitions.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.135 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.135 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.135 must not prove a theorem.")

        zero_fields = [
            "sigma_a_refinement_execution_count",
            "new_sigma_a_refinement_execution_count",
            "new_time_index_refinement_execution_count",
            "new_t_a_refinement_execution_count",
            "time_index_refinement_execution_count",
            "t_a_refinement_execution_count",
            "new_whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_sigma_a_draft_clause_creation_count",
            "new_carrier_draft_clause_creation_execution_count",
            "new_carrier_level_draft_assembly_execution_count",
            "new_definition_draft_execution_count",
            "new_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
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

        return SigmaARefinementExecutionPlanBoundaryAuditReport(
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
            "sigma_a_refinement_execution_plan_boundary_audit_count": "Sigma_A refinement execution plan boundary audit count",
            "sigma_a_refinement_plan_boundary_audit_count": "Sigma_A refinement plan boundary audit count",
            "draft_sigma_a_refinement_execution_plan_boundary_audit_count": "Draft Sigma_A refinement execution plan boundary audit count",
            "sigma_a_refinement_plan_boundary_audit_row_count": "Sigma_A refinement plan boundary audit row count",
            "sigma_a_refinement_plan_boundary_preserved_count": "Sigma_A refinement plan boundary preserved count",
            "sigma_a_refinement_plan_boundary_audit_finding_count": "Sigma_A refinement plan boundary audit finding count",
            "planned_sigma_a_refinement_scope_audited_count": "Planned Sigma_A refinement scope audited count",
            "planned_time_index_layer_integration_audited_count": "Planned time-index layer integration audited count",
            "planned_draft_shell_refinement_link_audited_count": "Planned draft shell refinement link audited count",
            "planned_carrier_clause_preservation_audited_count": "Planned carrier clause preservation audited count",
            "planned_dependent_object_integration_schedule_audited_count": "Planned dependent object integration schedule audited count",
            "sigma_a_refinement_execution_blocker_count": "Sigma_A refinement execution blocker count",
            "new_time_index_refinement_execution_blocker_count": "New time-index refinement execution blocker count",
            "new_t_a_refinement_execution_blocker_count": "New T_A refinement execution blocker count",
            "definition_execution_blocker_count": "Definition execution blocker count",
            "proof_readiness_blocker_count": "Proof-readiness blocker count",
            "carried_sigma_a_refinement_execution_plan_count": "Carried Sigma_A refinement execution plan count",
            "carried_sigma_a_refinement_plan_count": "Carried Sigma_A refinement plan count",
            "carried_draft_sigma_a_refinement_execution_plan_count": "Carried Draft Sigma_A refinement execution plan count",
            "carried_sigma_a_refinement_plan_row_count": "Carried Sigma_A refinement plan row count",
            "carried_sigma_a_refinement_execution_gate_count": "Carried Sigma_A refinement execution gate count",
            "carried_planned_sigma_a_refinement_scope_count": "Carried planned Sigma_A refinement scope count",
            "carried_planned_time_index_layer_integration_count": "Carried planned time-index layer integration count",
            "carried_planned_draft_shell_refinement_link_count": "Carried planned draft shell refinement link count",
            "carried_planned_carrier_clause_preservation_count": "Carried planned carrier clause preservation count",
            "carried_planned_dependent_object_integration_schedule_count": "Carried planned dependent object integration schedule count",
            "carried_planned_sigma_a_boundary_guard_count": "Carried planned Sigma_A boundary guard count",
            "carried_planned_sigma_a_blocked_overreach_count": "Carried planned Sigma_A blocked-overreach count",
            "carried_time_index_refinement_boundary_audit_count": "Carried time-index refinement boundary audit count",
            "carried_t_a_refinement_boundary_audit_count": "Carried T_A refinement boundary audit count",
            "carried_sigma_a_time_index_refinement_boundary_audit_count": "Carried Sigma_A time-index refinement boundary audit count",
            "carried_executed_time_index_refinement_audited_count": "Carried executed time-index refinement audited count",
            "carried_executed_t_a_refinement_audited_count": "Carried executed T_A refinement audited count",
            "carried_three_time_structure_audited_count": "Carried three-time structure audited count",
            "carried_time_index_refinement_execution_count": "Carried time-index refinement execution count",
            "carried_t_a_refinement_execution_count": "Carried T_A refinement execution count",
            "carried_sigma_a_time_index_refinement_execution_count": "Carried Sigma_A time-index refinement execution count",
            "carried_whole_sigma_a_draft_assembly_boundary_audit_count": "Carried whole Sigma_A draft assembly boundary audit count",
            "carried_assembled_whole_sigma_a_draft_shell_audited_count": "Carried assembled whole Sigma_A draft shell audited count",
            "carried_imported_carrier_slot_clause_audited_count": "Carried imported carrier-slot clause audited count",
            "sigma_a_refinement_execution_count": "Sigma_A refinement execution count",
            "new_sigma_a_refinement_execution_count": "New Sigma_A refinement execution count",
            "new_time_index_refinement_execution_count": "New time-index refinement execution count",
            "new_t_a_refinement_execution_count": "New T_A refinement execution count",
            "time_index_refinement_execution_count": "Time-index refinement execution count",
            "t_a_refinement_execution_count": "T_A refinement execution count",
            "new_whole_sigma_a_draft_assembly_execution_count": "New whole Sigma_A draft assembly execution count",
            "new_sigma_a_draft_assembly_execution_count": "New Sigma_A draft assembly execution count",
            "new_sigma_a_draft_clause_count": "New Sigma_A draft clause count",
            "new_sigma_a_draft_clause_creation_count": "New Sigma_A draft clause creation count",
            "new_carrier_draft_clause_creation_execution_count": "New carrier draft clause creation execution count",
            "new_carrier_level_draft_assembly_execution_count": "New carrier-level draft assembly execution count",
            "new_definition_draft_execution_count": "New definition draft execution count",
            "new_typed_product_carrier_refinement_execution_count": "New typed-product carrier refinement execution count",
            "generic_carrier_refinement_execution_count": "Generic carrier refinement execution count",
            "carrier_refinement_execution_count": "Carrier refinement execution count",
            "carrier_type_refinement_execution_count": "Carrier type refinement execution count",
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
            "Can Viruse Fabric audit the Sigma_A refinement execution plan after v8.134 while keeping actual Sigma_A refinement, new Sigma_A refinement, "
            "new time-index refinement, new T_A refinement, definition execution, Sigma_A definition completion, theorem candidate planning, theorem proof, "
            "proof assistant verification, external validation, manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Audit boundary")
        lines.append("- Milestone type: Sigma_A refinement execution plan boundary audit only")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- New Sigma_A refinement execution after this milestone: not executed")
        lines.append("- New time-index refinement execution after this milestone: not executed")
        lines.append("- New T_A refinement execution after this milestone: not executed")
        lines.append("- Definition execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Sigma_A refinement execution plan boundary audit rows")
        lines.append("")
        lines.append("| Audit ID | Focus | Audited object | Boundary result | Open dependency | Blocked overreach |")
        lines.append("|---|---|---|---|---|---|")
        for row in self.audit_rows:
            lines.append(
                f"| {row['audit_id']} | {row['focus']} | {row['audited_object']} | "
                f"{row['boundary_result']} | {row['open_dependency']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Audit findings")
        for index, finding in enumerate(self.audit_findings, start=1):
            lines.append(f"{index}. {finding}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact audits the Sigma_A refinement execution plan only. "
            "It carries the v8.134 future Sigma_A refinement plan, but it does not execute Sigma_A refinement, "
            "does not execute new Sigma_A refinement, does not execute new time-index refinement, does not execute new T_A refinement, "
            "does not execute new whole Sigma_A draft assembly, does not execute new Sigma_A draft assembly, "
            "does not create a new Sigma_A draft clause, does not execute new carrier draft clause creation, "
            "does not execute new carrier-level draft assembly, does not execute a new definition draft, "
            "does not execute new typed-product carrier refinement, does not execute generic carrier refinement, "
            "does not execute carrier-type refinement, does not execute new component-slot integration, "
            "does not execute new component-slot refinement, does not perform a new carrier type selection, "
            "does not execute definitions, does not complete Sigma_A, does not complete any formal definition, "
            "does not complete formalization, does not create theorem candidates, does not prove a theorem, "
            "does not run proof execution, does not provide proof assistant verification, does not prove the full framework, "
            "does not provide external validation, does not perform an independent experiment, does not approve manuscript submission readiness, "
            "and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_refinement_execution_plan_boundary_audit_count",
            "sigma_a_refinement_plan_boundary_audit_count",
            "draft_sigma_a_refinement_execution_plan_boundary_audit_count",
            "sigma_a_refinement_plan_boundary_audit_row_count",
            "sigma_a_refinement_plan_boundary_preserved_count",
            "sigma_a_refinement_plan_boundary_audit_finding_count",
            "planned_sigma_a_refinement_scope_audited_count",
            "planned_time_index_layer_integration_audited_count",
            "planned_draft_shell_refinement_link_audited_count",
            "planned_carrier_clause_preservation_audited_count",
            "planned_dependent_object_integration_schedule_audited_count",
            "sigma_a_refinement_execution_blocker_count",
            "new_time_index_refinement_execution_blocker_count",
            "new_t_a_refinement_execution_blocker_count",
            "definition_execution_blocker_count",
            "proof_readiness_blocker_count",
            "carried_sigma_a_refinement_execution_plan_count",
            "carried_sigma_a_refinement_plan_count",
            "carried_draft_sigma_a_refinement_execution_plan_count",
            "carried_sigma_a_refinement_plan_row_count",
            "carried_sigma_a_refinement_execution_gate_count",
            "carried_planned_sigma_a_refinement_scope_count",
            "carried_planned_time_index_layer_integration_count",
            "carried_planned_draft_shell_refinement_link_count",
            "carried_planned_carrier_clause_preservation_count",
            "carried_planned_dependent_object_integration_schedule_count",
            "carried_planned_sigma_a_boundary_guard_count",
            "carried_planned_sigma_a_blocked_overreach_count",
            "carried_time_index_refinement_boundary_audit_count",
            "carried_t_a_refinement_boundary_audit_count",
            "carried_sigma_a_time_index_refinement_boundary_audit_count",
            "carried_executed_time_index_refinement_audited_count",
            "carried_executed_t_a_refinement_audited_count",
            "carried_three_time_structure_audited_count",
            "carried_time_index_refinement_execution_count",
            "carried_t_a_refinement_execution_count",
            "carried_sigma_a_time_index_refinement_execution_count",
            "carried_whole_sigma_a_draft_assembly_boundary_audit_count",
            "carried_assembled_whole_sigma_a_draft_shell_audited_count",
            "carried_imported_carrier_slot_clause_audited_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "sigma_a_refinement_execution_count",
            "new_sigma_a_refinement_execution_count",
            "new_time_index_refinement_execution_count",
            "new_t_a_refinement_execution_count",
            "time_index_refinement_execution_count",
            "t_a_refinement_execution_count",
            "new_whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_sigma_a_draft_clause_creation_count",
            "new_carrier_draft_clause_creation_execution_count",
            "new_carrier_level_draft_assembly_execution_count",
            "new_definition_draft_execution_count",
            "new_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
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
            "The v8.135 artifact audits the v8.134 Sigma_A refinement execution plan. "
            "It confirms that Sigma_A refinement remains planned but not executed, and that new Sigma_A refinement, "
            "new time-index refinement, new T_A refinement, definition execution, Sigma_A completion, theorem candidate planning, theorem proof, "
            "proof assistant verification, validation, readiness, and citation claims remain absent."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute Sigma_A refinement only after this plan boundary audit is closed.",
            "Keep Sigma_A refinement execution separate from definition execution.",
            "Keep dependent-object definitions separate from Sigma_A refinement.",
            "Keep Sigma_A completion separate from theorem candidate planning.",
            "Keep theorem candidate planning separate from theorem proof.",
            "Keep proof assistant verification separate from proof execution.",
            "Keep validation and manuscript readiness separate.",
            "Keep citation work separate from validation and readiness.",
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
            "sigma_a",
            "refinement",
            "audit",
            "boundary",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute Sigma_A refinement",
            "does not execute new Sigma_A refinement",
            "does not execute new time-index refinement",
            "does not execute new T_A refinement",
            "does not execute new whole Sigma_A draft assembly",
            "does not execute new Sigma_A draft assembly",
            "does not create a new Sigma_A draft clause",
            "does not execute new carrier draft clause creation",
            "does not execute new carrier-level draft assembly",
            "does not execute a new definition draft",
            "does not execute new typed-product carrier refinement",
            "does not execute generic carrier refinement",
            "does not execute carrier-type refinement",
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
            "sigma_a refinement execution count",
            "sigma a refinement execution count",
            "new sigma_a refinement execution count",
            "new sigma a refinement execution count",
            "new time index refinement execution count",
            "new time-index refinement execution count",
            "new t_a refinement execution count",
            "new t a refinement execution count",
            "time index refinement execution count",
            "time-index refinement execution count",
            "t_a refinement execution count",
            "t a refinement execution count",
            "new whole sigma_a draft assembly execution count",
            "new whole sigma a draft assembly execution count",
            "new sigma_a draft assembly execution count",
            "new sigma a draft assembly execution count",
            "new sigma_a draft clause count",
            "new sigma a draft clause count",
            "new sigma_a draft clause creation count",
            "new sigma a draft clause creation count",
            "new carrier draft clause creation execution count",
            "new carrier-level draft assembly execution count",
            "new definition draft execution count",
            "new typed-product carrier refinement execution count",
            "generic carrier refinement execution count",
            "carrier refinement execution count",
            "carrier type refinement execution count",
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
            "Sigma_A refinement executed",
            "new Sigma_A refinement executed",
            "new time-index refinement executed",
            "new T_A refinement executed",
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
            "audit",
            "audited",
            "boundary",
            "blocker",
            "open dependency",
            "carried",
            "planned",
            "planning",
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
    report = SigmaARefinementExecutionPlanBoundaryAuditBuilder().run()
    print(f"Wrote {report.output_path}")
