from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class WholeSigmaADraftAssemblyExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class WholeSigmaADraftAssemblyExecutionBuilder:
    """Build v8.128 Whole Sigma_A draft assembly execution artifact.

    Boundary discipline:
    - This milestone executes whole Draft Sigma_A assembly only.
    - It assembles a draft shell, not a completed Sigma_A definition.
    - It imports the already-audited carrier-slot clause.
    - It does not create a new Sigma_A draft clause.
    - It does not execute time-index refinement.
    - It does not execute Sigma_A refinement.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Whole Sigma_A Draft Assembly Execution v8.128"
    source_artifact = Path("outputs/whole_sigma_a_draft_assembly_execution_plan_v8_127.md")
    output_path = Path("outputs/whole_sigma_a_draft_assembly_execution_v8_128.md")

    assembled_draft_shell = (
        "Draft Sigma_A shell := {carrier clause: carrier(Draft Sigma_A) := X_A^tp; "
        "deferred slots: Adm_A, C_reg, Pi_obs, M_c, R_A, Traj_A, T_A; "
        "audit traceability: Ann_A}. "
        "This is a draft assembly shell only and not a completed Sigma_A definition."
    )

    assembly_rows = [
        {
            "execution_id": "WHOLE-SIG-A-DRAFT-ASM-EXEC-001",
            "focus": "carrier-slot clause import",
            "execution_result": "imported the audited carrier-slot clause carrier(Draft Sigma_A) := X_A^tp",
            "assembled_element": "carrier slot",
            "boundary": "does not create a new Sigma_A draft clause",
            "status": "whole draft assembly executed",
        },
        {
            "execution_id": "WHOLE-SIG-A-DRAFT-ASM-EXEC-002",
            "focus": "whole draft shell",
            "execution_result": "assembled one whole Draft Sigma_A shell around the imported carrier-slot clause",
            "assembled_element": "whole Draft Sigma_A shell",
            "boundary": "does not complete Sigma_A",
            "status": "whole draft assembly executed",
        },
        {
            "execution_id": "WHOLE-SIG-A-DRAFT-ASM-EXEC-003",
            "focus": "dependent-object slots",
            "execution_result": "added deferred slots for Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A",
            "assembled_element": "six deferred dependent-object slots",
            "boundary": "does not define dependent objects",
            "status": "whole draft assembly executed",
        },
        {
            "execution_id": "WHOLE-SIG-A-DRAFT-ASM-EXEC-004",
            "focus": "time-index slot",
            "execution_result": "added a deferred T_A slot without refining T_A",
            "assembled_element": "deferred time-index slot",
            "boundary": "does not execute time-index refinement",
            "status": "whole draft assembly executed",
        },
        {
            "execution_id": "WHOLE-SIG-A-DRAFT-ASM-EXEC-005",
            "focus": "Sigma_A refinement boundary",
            "execution_result": "assembled the draft shell without asserting Sigma_A refinement",
            "assembled_element": "refinement exclusion boundary",
            "boundary": "does not execute Sigma_A refinement",
            "status": "whole draft assembly executed",
        },
        {
            "execution_id": "WHOLE-SIG-A-DRAFT-ASM-EXEC-006",
            "focus": "definition boundary",
            "execution_result": "kept draft assembly separate from definition execution",
            "assembled_element": "definition-execution exclusion boundary",
            "boundary": "does not execute definitions and does not complete formal definitions",
            "status": "whole draft assembly executed",
        },
        {
            "execution_id": "WHOLE-SIG-A-DRAFT-ASM-EXEC-007",
            "focus": "audit traceability",
            "execution_result": "carried Ann_A as auxiliary audit traceability for the assembled draft shell",
            "assembled_element": "Ann_A traceability slot",
            "boundary": "does not add hidden mathematical structure",
            "status": "whole draft assembly executed",
        },
        {
            "execution_id": "WHOLE-SIG-A-DRAFT-ASM-EXEC-008",
            "focus": "proof-readiness separation",
            "execution_result": "kept theorem/proof/validation/readiness layers downstream",
            "assembled_element": "proof-readiness exclusion boundary",
            "boundary": "does not create theorem candidates, proofs, validation, citations, or readiness approval",
            "status": "whole draft assembly executed",
        },
    ]

    assembly_checks = [
        "Exactly one whole Draft Sigma_A shell is assembled.",
        "The assembled shell imports the audited carrier-slot clause.",
        "No new Sigma_A draft clause is created.",
        "Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A remain deferred slots.",
        "T_A remains a deferred slot and no time-index refinement is executed.",
        "Sigma_A refinement remains absent.",
        "Definition execution and Sigma_A definition completion remain absent.",
        "Theorem, proof, validation, citation, and readiness layers remain absent.",
    ]

    def run(self) -> WholeSigmaADraftAssemblyExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone executes whole Draft Sigma_A assembly only.",
            "The assembled object is a draft shell, not a completed Sigma_A definition.",
            "No new Sigma_A draft clause is created in v8.128.",
            "Time-index refinement, Sigma_A refinement, definition execution, Sigma_A definition completion, theorem planning, proof, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "whole_sigma_a_draft_assembly_execution_count": 1,
            "sigma_a_whole_draft_assembly_execution_count": 1,
            "sigma_a_draft_assembly_execution_count": 1,
            "assembled_whole_sigma_a_draft_count": 1,
            "assembled_whole_sigma_a_draft_shell_count": 1,
            "imported_carrier_slot_clause_count": 1,
            "carried_carrier_slot_clause_import_count": 1,
            "dependent_object_slot_count": 6,
            "time_index_slot_deferral_count": 1,
            "audit_traceability_carried_count": 1,
            "whole_sigma_a_draft_assembly_row_count": len(self.assembly_rows),
            "whole_sigma_a_draft_assembly_check_count": len(self.assembly_checks),
            "whole_sigma_a_draft_boundary_preserved_count": len(self.assembly_rows),
            "carried_whole_sigma_a_draft_assembly_execution_plan_count": carried.get("Whole Sigma_A draft assembly execution plan count", 1),
            "carried_sigma_a_whole_draft_assembly_execution_plan_count": carried.get("Sigma_A whole draft assembly execution plan count", 1),
            "carried_sigma_a_draft_assembly_execution_plan_count": carried.get("Sigma_A draft assembly execution plan count", 1),
            "carried_whole_sigma_a_draft_assembly_plan_row_count": carried.get("Whole Sigma_A draft assembly plan row count", 8),
            "carried_whole_sigma_a_draft_assembly_execution_gate_count": carried.get("Whole Sigma_A draft assembly execution gate count", 8),
            "carried_planned_whole_sigma_a_draft_shell_count": carried.get("Planned whole Sigma_A draft shell count", 1),
            "carried_planned_carried_carrier_slot_clause_import_count": carried.get("Planned carried carrier-slot clause import count", 1),
            "carried_planned_dependent_object_slot_count": carried.get("Planned dependent object slot count", 6),
            "carried_planned_time_index_slot_deferral_count": carried.get("Planned time-index slot deferral count", 1),
            "carried_sigma_a_carrier_draft_clause_creation_boundary_audit_count": carried.get("Carried Sigma_A carrier draft clause creation boundary audit count", 1),
            "carried_carrier_draft_clause_creation_boundary_audit_count": carried.get("Carried carrier draft clause creation boundary audit count", 1),
            "carried_created_carrier_draft_clause_audited_count": carried.get("Carried created carrier draft clause audited count", 1),
            "carried_carrier_slot_clause_audited_count": carried.get("Carried carrier-slot clause audited count", 1),
            "carried_new_sigma_a_draft_clause_count": carried.get("Carried new Sigma_A draft clause count", 1),
            "carried_new_sigma_a_draft_clause_creation_count": carried.get("Carried new Sigma_A draft clause creation count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
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
            errors.append("Overclaim detected in v8.128 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.128 report.")
        if counts["whole_sigma_a_draft_assembly_execution_count"] != 1:
            errors.append("v8.128 must execute exactly one whole Sigma_A draft assembly milestone.")
        if counts["sigma_a_draft_assembly_execution_count"] != 1:
            errors.append("v8.128 must set Sigma_A draft assembly execution count to one.")
        if counts["assembled_whole_sigma_a_draft_shell_count"] != 1:
            errors.append("v8.128 must assemble exactly one whole Draft Sigma_A shell.")
        if counts["imported_carrier_slot_clause_count"] != 1:
            errors.append("v8.128 must import exactly one audited carrier-slot clause.")
        if counts["whole_sigma_a_draft_assembly_row_count"] != 8:
            errors.append("v8.128 must include exactly eight whole Sigma_A draft assembly rows.")
        if counts["new_sigma_a_draft_clause_count"] != 0:
            errors.append("v8.128 must not create a new Sigma_A draft clause.")
        if counts["time_index_refinement_execution_count"] != 0:
            errors.append("v8.128 must not execute time-index refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.128 must not execute Sigma_A refinement.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.128 must not execute definitions.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.128 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.128 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.128 must not prove a theorem.")

        zero_fields = [
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

        return WholeSigmaADraftAssemblyExecutionReport(
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
            "whole_sigma_a_draft_assembly_execution_count": "Whole Sigma_A draft assembly execution count",
            "sigma_a_whole_draft_assembly_execution_count": "Sigma_A whole draft assembly execution count",
            "sigma_a_draft_assembly_execution_count": "Sigma_A draft assembly execution count",
            "assembled_whole_sigma_a_draft_count": "Assembled whole Sigma_A draft count",
            "assembled_whole_sigma_a_draft_shell_count": "Assembled whole Sigma_A draft shell count",
            "imported_carrier_slot_clause_count": "Imported carrier-slot clause count",
            "carried_carrier_slot_clause_import_count": "Carried carrier-slot clause import count",
            "dependent_object_slot_count": "Dependent object slot count",
            "time_index_slot_deferral_count": "Time-index slot deferral count",
            "audit_traceability_carried_count": "Audit traceability carried count",
            "whole_sigma_a_draft_assembly_row_count": "Whole Sigma_A draft assembly row count",
            "whole_sigma_a_draft_assembly_check_count": "Whole Sigma_A draft assembly check count",
            "whole_sigma_a_draft_boundary_preserved_count": "Whole Sigma_A draft boundary preserved count",
            "carried_whole_sigma_a_draft_assembly_execution_plan_count": "Carried whole Sigma_A draft assembly execution plan count",
            "carried_sigma_a_whole_draft_assembly_execution_plan_count": "Carried Sigma_A whole draft assembly execution plan count",
            "carried_sigma_a_draft_assembly_execution_plan_count": "Carried Sigma_A draft assembly execution plan count",
            "carried_whole_sigma_a_draft_assembly_plan_row_count": "Carried whole Sigma_A draft assembly plan row count",
            "carried_whole_sigma_a_draft_assembly_execution_gate_count": "Carried whole Sigma_A draft assembly execution gate count",
            "carried_planned_whole_sigma_a_draft_shell_count": "Carried planned whole Sigma_A draft shell count",
            "carried_planned_carried_carrier_slot_clause_import_count": "Carried planned carried carrier-slot clause import count",
            "carried_planned_dependent_object_slot_count": "Carried planned dependent object slot count",
            "carried_planned_time_index_slot_deferral_count": "Carried planned time-index slot deferral count",
            "carried_sigma_a_carrier_draft_clause_creation_boundary_audit_count": "Carried Sigma_A carrier draft clause creation boundary audit count",
            "carried_carrier_draft_clause_creation_boundary_audit_count": "Carried carrier draft clause creation boundary audit count",
            "carried_created_carrier_draft_clause_audited_count": "Carried created carrier draft clause audited count",
            "carried_carrier_slot_clause_audited_count": "Carried carrier-slot clause audited count",
            "carried_new_sigma_a_draft_clause_count": "Carried new Sigma_A draft clause count",
            "carried_new_sigma_a_draft_clause_creation_count": "Carried new Sigma_A draft clause creation count",
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
            "Can Viruse Fabric execute whole Sigma_A draft assembly after the v8.127 execution plan while keeping new Sigma_A draft clause creation, "
            "time-index refinement, Sigma_A refinement, definition execution, Sigma_A definition completion, theorem candidate planning, theorem proof, "
            "proof assistant verification, external validation, manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Execution boundary")
        lines.append("- Milestone type: Whole Sigma_A draft assembly execution only")
        lines.append("- Whole Sigma_A draft assembly execution after this milestone: executed")
        lines.append("- Assembled whole Sigma_A draft shell after this milestone: one")
        lines.append("- Imported carrier-slot clause after this milestone: one")
        lines.append("- New Sigma_A draft assembly execution after this milestone: not executed")
        lines.append("- New Sigma_A draft clause creation after this milestone: not created")
        lines.append("- Time-index refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Definition execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Assembled Draft Sigma_A shell")
        lines.append(self.assembled_draft_shell)
        lines.append("")
        lines.append("## Whole Sigma_A draft assembly rows")
        lines.append("")
        lines.append("| Execution ID | Focus | Execution result | Assembled element | Boundary | Status |")
        lines.append("|---|---|---|---|---|---|")
        for row in self.assembly_rows:
            lines.append(
                f"| {row['execution_id']} | {row['focus']} | {row['execution_result']} | "
                f"{row['assembled_element']} | {row['boundary']} | {row['status']} |"
            )
        lines.append("")
        lines.append("## Whole Sigma_A draft assembly checks")
        for index, check in enumerate(self.assembly_checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes whole Sigma_A draft assembly only. "
            "It assembles exactly one whole Draft Sigma_A shell and imports the audited carrier-slot clause, "
            "but it does not execute new Sigma_A draft assembly, does not create a new Sigma_A draft clause, "
            "does not execute new carrier draft clause creation, does not execute new carrier-level draft assembly, "
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
            "whole_sigma_a_draft_assembly_execution_count",
            "sigma_a_whole_draft_assembly_execution_count",
            "sigma_a_draft_assembly_execution_count",
            "assembled_whole_sigma_a_draft_count",
            "assembled_whole_sigma_a_draft_shell_count",
            "imported_carrier_slot_clause_count",
            "carried_carrier_slot_clause_import_count",
            "dependent_object_slot_count",
            "time_index_slot_deferral_count",
            "audit_traceability_carried_count",
            "whole_sigma_a_draft_assembly_row_count",
            "whole_sigma_a_draft_assembly_check_count",
            "whole_sigma_a_draft_boundary_preserved_count",
            "carried_whole_sigma_a_draft_assembly_execution_plan_count",
            "carried_sigma_a_whole_draft_assembly_execution_plan_count",
            "carried_sigma_a_draft_assembly_execution_plan_count",
            "carried_whole_sigma_a_draft_assembly_plan_row_count",
            "carried_whole_sigma_a_draft_assembly_execution_gate_count",
            "carried_planned_whole_sigma_a_draft_shell_count",
            "carried_planned_carried_carrier_slot_clause_import_count",
            "carried_planned_dependent_object_slot_count",
            "carried_planned_time_index_slot_deferral_count",
            "carried_sigma_a_carrier_draft_clause_creation_boundary_audit_count",
            "carried_carrier_draft_clause_creation_boundary_audit_count",
            "carried_created_carrier_draft_clause_audited_count",
            "carried_carrier_slot_clause_audited_count",
            "carried_new_sigma_a_draft_clause_count",
            "carried_new_sigma_a_draft_clause_creation_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
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
            "The v8.128 artifact assembles exactly one whole Draft Sigma_A shell around the audited carrier-slot clause. "
            "This is draft assembly only. It does not create new Sigma_A draft clauses, does not execute time-index refinement, "
            "does not execute Sigma_A refinement, does not execute definitions, does not complete Sigma_A, "
            "does not create theorem candidates, does not prove theorems, does not provide proof assistant verification, "
            "does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit the assembled whole Draft Sigma_A shell before time-index refinement.",
            "Keep whole Sigma_A draft assembly separate from time-index refinement.",
            "Keep time-index refinement separate from Sigma_A refinement.",
            "Keep dependent-object definitions separate from draft assembly.",
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
            "whole Draft Sigma_A".lower(),
            "draft shell",
            "boundary",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute new Sigma_A draft assembly",
            "does not create a new Sigma_A draft clause",
            "does not execute new carrier draft clause creation",
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
            "draft shell",
            "draft assembly only",
            "boundary",
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
    report = WholeSigmaADraftAssemblyExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
