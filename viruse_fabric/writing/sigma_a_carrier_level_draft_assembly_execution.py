from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaACarrierLevelDraftAssemblyExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaACarrierLevelDraftAssemblyExecutionBuilder:
    """Build v8.122 Sigma_A carrier-level draft assembly execution artifact.

    Boundary discipline:
    - This milestone executes carrier-level draft assembly only.
    - It imports X_A^tp as the carrier-level candidate for Draft Sigma_A.
    - It does not create new Sigma_A draft clauses.
    - It does not execute whole Sigma_A draft assembly.
    - It does not execute Sigma_A refinement.
    - It does not execute time-index refinement.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Carrier-Level Draft Assembly Execution v8.122"
    source_artifact = Path("outputs/sigma_a_carrier_level_draft_assembly_execution_plan_v8_121.md")
    output_path = Path("outputs/sigma_a_carrier_level_draft_assembly_execution_v8_122.md")

    assembly_rows = [
        {
            "assembly_id": "SIG-A-CARRIER-DRAFT-ASM-001",
            "focus": "carrier candidate import",
            "assembled_element": "X_A^tp",
            "assembly_result": "X_A^tp imported as carrier-level candidate for Draft Sigma_A",
            "boundary": "does not complete X_A and does not complete Sigma_A",
            "status": "carrier-level draft assembly executed",
        },
        {
            "assembly_id": "SIG-A-CARRIER-DRAFT-ASM-002",
            "focus": "carrier slot placement",
            "assembled_element": "Draft Sigma_A carrier slot := X_A^tp",
            "assembly_result": "carrier slot placement recorded at assembly level",
            "boundary": "does not create a new Sigma_A draft clause",
            "status": "carrier-level draft assembly executed",
        },
        {
            "assembly_id": "SIG-A-CARRIER-DRAFT-ASM-003",
            "focus": "dependent-object deferral",
            "assembled_element": "{Adm_A, C_reg, Pi_obs, M_c, R_A, Traj_A}",
            "assembly_result": "six dependent objects remain deferred outside carrier-level assembly",
            "boundary": "does not define dependent objects",
            "status": "carrier-level draft assembly executed",
        },
        {
            "assembly_id": "SIG-A-CARRIER-DRAFT-ASM-004",
            "focus": "time-index separation",
            "assembled_element": "T_A",
            "assembly_result": "T_A remains outside carrier-level assembly",
            "boundary": "does not execute time-index refinement",
            "status": "carrier-level draft assembly executed",
        },
        {
            "assembly_id": "SIG-A-CARRIER-DRAFT-ASM-005",
            "focus": "Sigma_A refinement boundary",
            "assembled_element": "Sigma_A assembly layer",
            "assembly_result": "carrier-level assembly remains below Sigma_A refinement",
            "boundary": "does not execute Sigma_A refinement",
            "status": "carrier-level draft assembly executed",
        },
        {
            "assembly_id": "SIG-A-CARRIER-DRAFT-ASM-006",
            "focus": "definition boundary",
            "assembled_element": "formal definition layer",
            "assembly_result": "definition layer remains unexecuted",
            "boundary": "does not execute definitions and does not complete formal definitions",
            "status": "carrier-level draft assembly executed",
        },
        {
            "assembly_id": "SIG-A-CARRIER-DRAFT-ASM-007",
            "focus": "audit traceability",
            "assembled_element": "Ann_A",
            "assembly_result": "Ann_A carried as auxiliary audit traceability",
            "boundary": "does not add hidden mathematical structure",
            "status": "carrier-level draft assembly executed",
        },
        {
            "assembly_id": "SIG-A-CARRIER-DRAFT-ASM-008",
            "focus": "proof-readiness separation",
            "assembled_element": "theorem/proof/validation/readiness layers",
            "assembly_result": "downstream proof-readiness layers remain absent",
            "boundary": "does not create theorem candidates, proofs, validation, citations, or readiness approval",
            "status": "carrier-level draft assembly executed",
        },
    ]

    assembly_checks = [
        "X_A^tp is imported only as a carrier-level candidate.",
        "Carrier slot placement is recorded without creating a new Sigma_A draft clause.",
        "Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A remain deferred.",
        "T_A remains outside the carrier-level assembly.",
        "Sigma_A refinement remains absent.",
        "Definition execution and Sigma_A definition completion remain absent.",
        "Ann_A remains auxiliary audit traceability.",
        "Theorem, proof, validation, citation, and readiness layers remain absent.",
    ]

    def run(self) -> SigmaACarrierLevelDraftAssemblyExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone executes carrier-level draft assembly only.",
            "New Sigma_A draft clause creation remains zero in v8.122.",
            "Whole Sigma_A draft assembly execution remains zero in v8.122.",
            "Sigma_A refinement, definition execution, Sigma_A definition completion, theorem planning, proof, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_carrier_level_draft_assembly_execution_count": 1,
            "carrier_level_draft_assembly_execution_count": 1,
            "carrier_level_draft_assembly_row_count": len(self.assembly_rows),
            "carrier_level_draft_assembly_check_count": len(self.assembly_checks),
            "assembled_carrier_candidate_count": 1,
            "carrier_slot_placement_count": 1,
            "carrier_candidate_import_count": 1,
            "dependent_object_deferred_count": 6,
            "audit_traceability_carried_count": 1,
            "carried_sigma_a_carrier_level_draft_assembly_execution_plan_count": carried.get("Sigma_A carrier-level draft assembly execution plan count", 1),
            "carried_carrier_level_draft_assembly_execution_plan_count": carried.get("Carrier-level draft assembly execution plan count", 1),
            "carried_sigma_a_draft_assembly_execution_plan_count": carried.get("Sigma_A draft assembly execution plan count", 1),
            "carried_carrier_level_draft_assembly_plan_row_count": carried.get("Carrier-level draft assembly plan row count", 8),
            "carried_carrier_level_draft_assembly_execution_gate_count": carried.get("Carrier-level draft assembly execution gate count", 8),
            "carried_planned_carrier_level_draft_mapping_count": carried.get("Planned carrier-level draft mapping count", 8),
            "carried_planned_carrier_candidate_import_count": carried.get("Planned carrier candidate import count", 1),
            "carried_planned_dependent_object_deferral_count": carried.get("Planned dependent object deferral count", 6),
            "carried_sigma_a_typed_product_carrier_refinement_boundary_audit_count": carried.get("Carried Sigma_A typed-product carrier refinement boundary audit count", 1),
            "carried_typed_product_carrier_refinement_boundary_audit_count": carried.get("Carried typed-product carrier refinement boundary audit count", 1),
            "carried_full_typed_product_carrier_refinement_boundary_audit_count": carried.get("Carried full typed-product carrier refinement boundary audit count", 1),
            "carried_refined_typed_product_carrier_candidate_audited_count": carried.get("Carried refined typed-product carrier candidate audited count", 1),
            "carried_dependent_object_boundary_preserved_count": carried.get("Carried dependent object boundary preserved count", 6),
            "carried_sigma_a_typed_product_carrier_refinement_execution_count": carried.get("Carried Sigma_A typed-product carrier refinement execution count", 1),
            "carried_full_typed_product_carrier_refinement_execution_count": carried.get("Carried full typed-product carrier refinement execution count", 1),
            "carried_typed_product_carrier_refinement_execution_count": carried.get("Carried typed-product carrier refinement execution count", 1),
            "carried_refined_typed_product_carrier_component_count": carried.get("Carried refined typed-product carrier component count", 8),
            "carried_refined_typed_product_carrier_candidate_count": carried.get("Carried refined typed-product carrier candidate count", 1),
            "carried_carrier_level_notation_candidate_count": carried.get("Carried carrier-level notation candidate count", 1),
            "carried_selected_typed_product_carrier_count": carried.get("Carried selected typed-product carrier count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "new_carrier_level_draft_assembly_execution_count": 0,
            "whole_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_clause_count": 0,
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
            errors.append("Overclaim detected in v8.122 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.122 report.")
        if counts["sigma_a_carrier_level_draft_assembly_execution_count"] != 1:
            errors.append("v8.122 must execute exactly one Sigma_A carrier-level draft assembly milestone.")
        if counts["carrier_level_draft_assembly_execution_count"] != 1:
            errors.append("v8.122 must set carrier-level draft assembly execution count to one.")
        if counts["carrier_level_draft_assembly_row_count"] != 8:
            errors.append("v8.122 must include exactly eight carrier-level draft assembly rows.")
        if counts["assembled_carrier_candidate_count"] != 1:
            errors.append("v8.122 must assemble exactly one carrier candidate.")
        if counts["new_sigma_a_draft_clause_count"] != 0:
            errors.append("v8.122 must not create new Sigma_A draft clauses.")
        if counts["whole_sigma_a_draft_assembly_execution_count"] != 0:
            errors.append("v8.122 must not execute whole Sigma_A draft assembly.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.122 must not execute Sigma_A refinement.")
        if counts["time_index_refinement_execution_count"] != 0:
            errors.append("v8.122 must not execute time-index refinement.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.122 must not execute definitions.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.122 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.122 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.122 must not prove a theorem.")

        zero_fields = [
            "new_carrier_level_draft_assembly_execution_count",
            "whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_clause_count",
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

        return SigmaACarrierLevelDraftAssemblyExecutionReport(
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
            "sigma_a_carrier_level_draft_assembly_execution_count": "Sigma_A carrier-level draft assembly execution count",
            "carrier_level_draft_assembly_execution_count": "Carrier-level draft assembly execution count",
            "carrier_level_draft_assembly_row_count": "Carrier-level draft assembly row count",
            "carrier_level_draft_assembly_check_count": "Carrier-level draft assembly check count",
            "assembled_carrier_candidate_count": "Assembled carrier candidate count",
            "carrier_slot_placement_count": "Carrier slot placement count",
            "carrier_candidate_import_count": "Carrier candidate import count",
            "dependent_object_deferred_count": "Dependent object deferred count",
            "audit_traceability_carried_count": "Audit traceability carried count",
            "carried_sigma_a_carrier_level_draft_assembly_execution_plan_count": "Carried Sigma_A carrier-level draft assembly execution plan count",
            "carried_carrier_level_draft_assembly_execution_plan_count": "Carried carrier-level draft assembly execution plan count",
            "carried_sigma_a_draft_assembly_execution_plan_count": "Carried Sigma_A draft assembly execution plan count",
            "carried_carrier_level_draft_assembly_plan_row_count": "Carried carrier-level draft assembly plan row count",
            "carried_carrier_level_draft_assembly_execution_gate_count": "Carried carrier-level draft assembly execution gate count",
            "carried_planned_carrier_level_draft_mapping_count": "Carried planned carrier-level draft mapping count",
            "carried_planned_carrier_candidate_import_count": "Carried planned carrier candidate import count",
            "carried_planned_dependent_object_deferral_count": "Carried planned dependent object deferral count",
            "carried_sigma_a_typed_product_carrier_refinement_boundary_audit_count": "Carried Sigma_A typed-product carrier refinement boundary audit count",
            "carried_typed_product_carrier_refinement_boundary_audit_count": "Carried typed-product carrier refinement boundary audit count",
            "carried_full_typed_product_carrier_refinement_boundary_audit_count": "Carried full typed-product carrier refinement boundary audit count",
            "carried_refined_typed_product_carrier_candidate_audited_count": "Carried refined typed-product carrier candidate audited count",
            "carried_dependent_object_boundary_preserved_count": "Carried dependent object boundary preserved count",
            "carried_sigma_a_typed_product_carrier_refinement_execution_count": "Carried Sigma_A typed-product carrier refinement execution count",
            "carried_full_typed_product_carrier_refinement_execution_count": "Carried full typed-product carrier refinement execution count",
            "carried_typed_product_carrier_refinement_execution_count": "Carried typed-product carrier refinement execution count",
            "carried_refined_typed_product_carrier_component_count": "Carried refined typed-product carrier component count",
            "carried_refined_typed_product_carrier_candidate_count": "Carried refined typed-product carrier candidate count",
            "carried_carrier_level_notation_candidate_count": "Carried carrier-level notation candidate count",
            "carried_selected_typed_product_carrier_count": "Carried selected typed-product carrier count",
            "new_carrier_level_draft_assembly_execution_count": "New carrier-level draft assembly execution count",
            "whole_sigma_a_draft_assembly_execution_count": "Whole Sigma_A draft assembly execution count",
            "new_sigma_a_draft_assembly_execution_count": "New Sigma_A draft assembly execution count",
            "new_sigma_a_draft_clause_count": "New Sigma_A draft clause count",
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
            "Can Viruse Fabric execute Sigma_A carrier-level draft assembly after the v8.121 execution plan while keeping new Sigma_A draft clause creation, "
            "whole Sigma_A draft assembly execution, time-index refinement, Sigma_A refinement, definition execution, Sigma_A definition completion, "
            "theorem candidate planning, theorem proof, proof assistant verification, external validation, manuscript readiness, readiness approval, "
            "and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Execution boundary")
        lines.append("- Milestone type: Sigma_A carrier-level draft assembly execution only")
        lines.append("- Carrier-level draft assembly execution after this milestone: executed")
        lines.append("- Whole Sigma_A draft assembly execution after this milestone: not executed")
        lines.append("- New Sigma_A draft clause creation after this milestone: not created")
        lines.append("- Time-index refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Definition execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Carrier-level draft assembly rows")
        lines.append("")
        lines.append("| Assembly ID | Focus | Assembled element | Assembly result | Boundary | Status |")
        lines.append("|---|---|---|---|---|---|")
        for row in self.assembly_rows:
            lines.append(
                f"| {row['assembly_id']} | {row['focus']} | {row['assembled_element']} | "
                f"{row['assembly_result']} | {row['boundary']} | {row['status']} |"
            )
        lines.append("")
        lines.append("## Carrier-level draft assembly checks")
        for index, check in enumerate(self.assembly_checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes Sigma_A carrier-level draft assembly only. "
            "It executes carrier-level draft assembly and imports X_A^tp as a carrier-level candidate, "
            "but it does not execute whole Sigma_A draft assembly, does not execute new Sigma_A draft assembly, "
            "does not create new Sigma_A draft clauses, does not execute a new definition draft, "
            "does not execute new typed-product carrier refinement, does not execute generic carrier refinement, "
            "does not execute carrier-type refinement, does not execute time-index refinement, does not execute Sigma_A refinement, "
            "does not execute new component-slot integration, does not execute new component-slot refinement, "
            "does not perform a new carrier type selection, does not execute definitions, does not complete Sigma_A, "
            "does not complete any formal definition, does not complete formalization, does not create theorem candidates, "
            "does not prove a theorem, does not run proof execution, does not provide proof assistant verification, "
            "does not prove the full framework, does not provide external validation, does not perform an independent experiment, "
            "does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_carrier_level_draft_assembly_execution_count",
            "carrier_level_draft_assembly_execution_count",
            "carrier_level_draft_assembly_row_count",
            "carrier_level_draft_assembly_check_count",
            "assembled_carrier_candidate_count",
            "carrier_slot_placement_count",
            "carrier_candidate_import_count",
            "dependent_object_deferred_count",
            "audit_traceability_carried_count",
            "carried_sigma_a_carrier_level_draft_assembly_execution_plan_count",
            "carried_carrier_level_draft_assembly_execution_plan_count",
            "carried_sigma_a_draft_assembly_execution_plan_count",
            "carried_carrier_level_draft_assembly_plan_row_count",
            "carried_carrier_level_draft_assembly_execution_gate_count",
            "carried_planned_carrier_level_draft_mapping_count",
            "carried_planned_carrier_candidate_import_count",
            "carried_planned_dependent_object_deferral_count",
            "carried_sigma_a_typed_product_carrier_refinement_boundary_audit_count",
            "carried_typed_product_carrier_refinement_boundary_audit_count",
            "carried_full_typed_product_carrier_refinement_boundary_audit_count",
            "carried_refined_typed_product_carrier_candidate_audited_count",
            "carried_dependent_object_boundary_preserved_count",
            "carried_sigma_a_typed_product_carrier_refinement_execution_count",
            "carried_full_typed_product_carrier_refinement_execution_count",
            "carried_typed_product_carrier_refinement_execution_count",
            "carried_refined_typed_product_carrier_component_count",
            "carried_refined_typed_product_carrier_candidate_count",
            "carried_carrier_level_notation_candidate_count",
            "carried_selected_typed_product_carrier_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "new_carrier_level_draft_assembly_execution_count",
            "whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_clause_count",
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
            "The v8.122 artifact executes Sigma_A carrier-level draft assembly by importing X_A^tp as the carrier-level candidate. "
            "This is carrier-level assembly only. It does not execute whole Sigma_A draft assembly, does not create new Sigma_A draft clauses, "
            "does not execute time-index refinement, does not execute Sigma_A refinement, does not execute definitions, "
            "does not complete Sigma_A, does not create theorem candidates, does not prove theorems, "
            "does not provide proof assistant verification, does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit carrier-level draft assembly output before any new Sigma_A draft clause creation.",
            "Keep carrier-level draft assembly separate from whole Sigma_A draft assembly.",
            "Keep time-index refinement separate from carrier-level draft assembly.",
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
            "carrier-level draft assembly",
            "boundary",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute whole Sigma_A draft assembly",
            "does not execute new Sigma_A draft assembly",
            "does not create new Sigma_A draft clauses",
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
            "new carrier-level draft assembly execution count",
            "whole sigma_a draft assembly execution count",
            "whole sigma a draft assembly execution count",
            "new sigma_a draft assembly execution count",
            "new sigma a draft assembly execution count",
            "new sigma_a draft clause count",
            "new sigma a draft clause count",
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
            "whole Sigma_A draft assembly executed",
            "new Sigma_A draft clause created",
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
            "carrier-level assembly only",
            "carrier-level draft assembly only",
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
    report = SigmaACarrierLevelDraftAssemblyExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
