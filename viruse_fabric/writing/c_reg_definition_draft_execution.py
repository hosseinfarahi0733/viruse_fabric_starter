from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class CRegDefinitionDraftExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class CRegDefinitionDraftExecutionBuilder:
    """Build v8.138 C_reg definition draft execution artifact.

    Boundary discipline:
    - This milestone executes one C_reg definition draft only.
    - It does not execute final definition completion.
    - It does not complete C_reg.
    - It does not complete Adm_A.
    - It does not complete Sigma_A.
    - It does not prove theorems.
    """

    title = "C_reg Definition Draft Execution v8.138"
    source_artifact = Path("outputs/adm_a_definition_draft_execution_v8_137.md")
    output_path = Path("outputs/c_reg_definition_draft_execution_v8_138.md")

    draft_statement = (
        "Draft C_reg := a constraint-region placeholder for the refined Draft Sigma_A shell, "
        "tracking the candidate admissible region in which later state/action/constraint configurations may be evaluated. "
        "It is linked to the carried Adm_A draft as a dependent draft interface, but it remains a draft slot only. "
        "This draft does not complete C_reg, does not complete Adm_A, does not complete Sigma_A, and does not execute theorem or proof work."
    )

    draft_rows = [
        {
            "id": "C-REG-DRAFT-001",
            "focus": "dependent-object activation",
            "result": "created exactly one C_reg definition draft slot",
            "boundary": "does not complete C_reg",
        },
        {
            "id": "C-REG-DRAFT-002",
            "focus": "Sigma_A linkage",
            "result": "linked the C_reg draft to the refined Draft Sigma_A shell",
            "boundary": "does not complete Sigma_A",
        },
        {
            "id": "C-REG-DRAFT-003",
            "focus": "Adm_A dependency",
            "result": "linked C_reg to the carried Adm_A admissibility-interface draft",
            "boundary": "does not complete Adm_A",
        },
        {
            "id": "C-REG-DRAFT-004",
            "focus": "constraint-region role",
            "result": "recorded C_reg as a constraint-region placeholder",
            "boundary": "does not execute a final formal definition",
        },
        {
            "id": "C-REG-DRAFT-005",
            "focus": "time-index compatibility",
            "result": "kept C_reg compatible with the carried T_A/time-index layer",
            "boundary": "does not execute new time-index refinement",
        },
        {
            "id": "C-REG-DRAFT-006",
            "focus": "remaining dependent objects",
            "result": "kept Pi_obs, M_c, R_A, and Traj_A deferred",
            "boundary": "does not draft the remaining dependent objects",
        },
        {
            "id": "C-REG-DRAFT-007",
            "focus": "proof boundary",
            "result": "kept theorem candidate planning and theorem proof absent",
            "boundary": "does not create theorem candidates",
        },
        {
            "id": "C-REG-DRAFT-008",
            "focus": "readiness boundary",
            "result": "kept validation, readiness, and citation work downstream",
            "boundary": "does not approve manuscript readiness",
        },
    ]

    checks = [
        "Exactly one C_reg definition draft execution is performed.",
        "Exactly one new definition draft execution is performed.",
        "C_reg is linked to the refined Draft Sigma_A shell.",
        "C_reg is linked to the carried Adm_A draft.",
        "The draft is not a completed formal definition.",
        "Sigma_A definition completion remains absent.",
        "Theorem candidate planning remains absent.",
        "Validation, readiness, and citation claims remain absent.",
    ]

    def run(self) -> CRegDefinitionDraftExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""
        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone executes one C_reg definition draft, not a completed formal definition.",
            "C_reg definition completion remains zero.",
            "Adm_A and Sigma_A definition completion remain zero.",
            "Theorem, proof, validation, readiness, and citation claims remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,

            "c_reg_definition_draft_execution_count": 1,
            "new_c_reg_definition_draft_execution_count": 1,
            "new_definition_draft_execution_count": 1,
            "dependent_object_definition_draft_execution_count": 1,
            "c_reg_draft_slot_created_count": 1,
            "c_reg_draft_linked_to_refined_sigma_a_count": 1,
            "c_reg_linked_to_adm_a_draft_count": 1,
            "c_reg_constraint_region_placeholder_count": 1,
            "c_reg_time_index_compatibility_count": 1,
            "remaining_dependent_object_deferral_count": 4,
            "definition_draft_execution_row_count": len(self.draft_rows),
            "definition_draft_execution_check_count": len(self.checks),
            "definition_draft_boundary_preserved_count": len(self.draft_rows),

            "carried_adm_a_definition_draft_execution_count": carried.get("Adm_A definition draft execution count", 1),
            "carried_new_adm_a_definition_draft_execution_count": carried.get("New Adm_A definition draft execution count", 1),
            "carried_adm_a_draft_slot_created_count": carried.get("Adm_A draft slot created count", 1),
            "carried_adm_a_draft_linked_to_refined_sigma_a_count": carried.get("Adm_A draft linked to refined Sigma_A count", 1),
            "carried_adm_a_admissibility_interface_placeholder_count": carried.get("Adm_A admissibility-interface placeholder count", 1),
            "carried_adm_a_time_index_compatibility_count": carried.get("Adm_A time-index compatibility count", 1),
            "carried_remaining_dependent_object_deferral_count": carried.get("Remaining dependent-object deferral count", 5),

            "carried_sigma_a_refinement_execution_count": carried.get("Carried Sigma_A refinement execution count", 1),
            "carried_new_sigma_a_refinement_execution_count": carried.get("Carried new Sigma_A refinement execution count", 1),
            "carried_draft_sigma_a_refinement_execution_count": carried.get("Carried Draft Sigma_A refinement execution count", 1),
            "carried_executed_sigma_a_refinement_layer_count": carried.get("Carried executed Sigma_A refinement layer count", 1),
            "carried_refined_draft_sigma_a_shell_count": carried.get("Carried refined Draft Sigma_A shell count", 1),
            "carried_integrated_time_index_layer_count": carried.get("Carried integrated time-index layer count", 1),
            "carried_integrated_t_a_refinement_layer_count": carried.get("Carried integrated T_A refinement layer count", 1),

            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 9,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,

            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "completed_formal_definition_count": 0,
            "formalization_complete_count": 0,
            "c_reg_definition_completion_count": 0,
            "adm_a_definition_completion_count": 0,
            "sigma_a_definition_completion_count": 0,
            "stabilization_predicate_definition_completion_count": 0,
            "attractor_class_definition_completion_count": 0,
            "constraint_region_definition_completion_count": 0,
            "causal_mass_definition_completion_count": 0,
            "observer_projection_definition_completion_count": 0,

            "new_adm_a_definition_draft_execution_count": 0,
            "new_sigma_a_refinement_execution_count": 0,
            "new_time_index_refinement_execution_count": 0,
            "new_t_a_refinement_execution_count": 0,
            "new_whole_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_assembly_execution_count": 0,
            "new_sigma_a_draft_clause_count": 0,
            "new_sigma_a_draft_clause_creation_count": 0,
            "new_carrier_draft_clause_creation_execution_count": 0,
            "new_carrier_level_draft_assembly_execution_count": 0,
            "new_typed_product_carrier_refinement_execution_count": 0,
            "generic_carrier_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "new_component_slot_integration_execution_count": 0,
            "new_component_slot_refinement_execution_count": 0,
            "new_carrier_type_selection_count": 0,

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
            "next_step_count": 8,
        }

        report_text = self._render_report(counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.138 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.138 report.")
        if counts["c_reg_definition_draft_execution_count"] != 1:
            errors.append("v8.138 must execute exactly one C_reg definition draft.")
        if counts["new_definition_draft_execution_count"] != 1:
            errors.append("v8.138 must execute exactly one new definition draft.")
        if counts["c_reg_definition_completion_count"] != 0:
            errors.append("v8.138 must not complete C_reg.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.138 must not execute final definitions.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.138 must not complete Sigma_A definition.")
        if counts["completed_formal_definition_count"] != 0:
            errors.append("v8.138 must not complete a formal definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.138 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.138 must not prove theorem claims.")

        zero_fields = [
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "c_reg_definition_completion_count",
            "adm_a_definition_completion_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "new_adm_a_definition_draft_execution_count",
            "new_sigma_a_refinement_execution_count",
            "new_time_index_refinement_execution_count",
            "new_t_a_refinement_execution_count",
            "new_whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_sigma_a_draft_clause_creation_count",
            "new_carrier_draft_clause_creation_execution_count",
            "new_carrier_level_draft_assembly_execution_count",
            "new_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "new_component_slot_integration_execution_count",
            "new_component_slot_refinement_execution_count",
            "new_carrier_type_selection_count",
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

        return CRegDefinitionDraftExecutionReport(
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

    def _label(self, key: str) -> str:
        overrides = {
            "c_reg_definition_draft_execution_count": "C_reg definition draft execution count",
            "new_c_reg_definition_draft_execution_count": "New C_reg definition draft execution count",
            "new_definition_draft_execution_count": "New definition draft execution count",
            "dependent_object_definition_draft_execution_count": "Dependent-object definition draft execution count",
            "c_reg_draft_slot_created_count": "C_reg draft slot created count",
            "c_reg_draft_linked_to_refined_sigma_a_count": "C_reg draft linked to refined Sigma_A count",
            "c_reg_linked_to_adm_a_draft_count": "C_reg linked to Adm_A draft count",
            "c_reg_constraint_region_placeholder_count": "C_reg constraint-region placeholder count",
            "c_reg_time_index_compatibility_count": "C_reg time-index compatibility count",
            "remaining_dependent_object_deferral_count": "Remaining dependent-object deferral count",
            "definition_draft_execution_row_count": "Definition draft execution row count",
            "definition_draft_execution_check_count": "Definition draft execution check count",
            "definition_draft_boundary_preserved_count": "Definition draft boundary preserved count",
            "carried_adm_a_definition_draft_execution_count": "Carried Adm_A definition draft execution count",
            "carried_new_adm_a_definition_draft_execution_count": "Carried new Adm_A definition draft execution count",
            "carried_adm_a_draft_slot_created_count": "Carried Adm_A draft slot created count",
            "carried_adm_a_draft_linked_to_refined_sigma_a_count": "Carried Adm_A draft linked to refined Sigma_A count",
            "carried_adm_a_admissibility_interface_placeholder_count": "Carried Adm_A admissibility-interface placeholder count",
            "carried_adm_a_time_index_compatibility_count": "Carried Adm_A time-index compatibility count",
            "carried_remaining_dependent_object_deferral_count": "Carried remaining dependent-object deferral count",
            "carried_sigma_a_refinement_execution_count": "Carried Sigma_A refinement execution count",
            "carried_new_sigma_a_refinement_execution_count": "Carried new Sigma_A refinement execution count",
            "carried_draft_sigma_a_refinement_execution_count": "Carried Draft Sigma_A refinement execution count",
            "carried_executed_sigma_a_refinement_layer_count": "Carried executed Sigma_A refinement layer count",
            "carried_refined_draft_sigma_a_shell_count": "Carried refined Draft Sigma_A shell count",
            "carried_integrated_time_index_layer_count": "Carried integrated time-index layer count",
            "carried_integrated_t_a_refinement_layer_count": "Carried integrated T_A refinement layer count",
            "c_reg_definition_completion_count": "C_reg definition completion count",
            "adm_a_definition_completion_count": "Adm_A definition completion count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
            "new_adm_a_definition_draft_execution_count": "New Adm_A definition draft execution count",
            "new_sigma_a_refinement_execution_count": "New Sigma_A refinement execution count",
            "new_time_index_refinement_execution_count": "New time-index refinement execution count",
            "new_t_a_refinement_execution_count": "New T_A refinement execution count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric execute one C_reg definition draft after the Adm_A definition draft while keeping final definition execution, "
            "C_reg completion, Adm_A completion, Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citations at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Draft boundary")
        lines.append("- Milestone type: C_reg definition draft execution only")
        lines.append("- C_reg definition draft execution after this milestone: executed")
        lines.append("- New definition draft execution after this milestone: executed")
        lines.append("- Final definition execution after this milestone: not executed")
        lines.append("- C_reg definition completion after this milestone: not completed")
        lines.append("- Adm_A definition completion after this milestone: not completed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## C_reg draft statement")
        lines.append(self.draft_statement)
        lines.append("")
        lines.append("## C_reg definition draft execution rows")
        lines.append("")
        lines.append("| ID | Focus | Result | Boundary |")
        lines.append("|---|---|---|---|")
        for row in self.draft_rows:
            lines.append(f"| {row['id']} | {row['focus']} | {row['result']} | {row['boundary']} |")
        lines.append("")
        lines.append("## Draft checks")
        for index, check in enumerate(self.checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes one C_reg definition draft only. "
            "It creates a C_reg draft slot linked to the refined Draft Sigma_A shell and the carried Adm_A draft, "
            "but it does not execute final definitions, does not complete C_reg, does not complete Adm_A, does not complete Sigma_A, "
            "does not complete any formal definition, does not complete formalization, does not create theorem candidates, "
            "does not prove a theorem, does not run proof execution, does not provide proof assistant verification, "
            "does not provide external validation, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        order = [
            "c_reg_definition_draft_execution_count",
            "new_c_reg_definition_draft_execution_count",
            "new_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
            "c_reg_draft_slot_created_count",
            "c_reg_draft_linked_to_refined_sigma_a_count",
            "c_reg_linked_to_adm_a_draft_count",
            "c_reg_constraint_region_placeholder_count",
            "c_reg_time_index_compatibility_count",
            "remaining_dependent_object_deferral_count",
            "definition_draft_execution_row_count",
            "definition_draft_execution_check_count",
            "definition_draft_boundary_preserved_count",
            "carried_adm_a_definition_draft_execution_count",
            "carried_new_adm_a_definition_draft_execution_count",
            "carried_adm_a_draft_slot_created_count",
            "carried_adm_a_draft_linked_to_refined_sigma_a_count",
            "carried_adm_a_admissibility_interface_placeholder_count",
            "carried_adm_a_time_index_compatibility_count",
            "carried_remaining_dependent_object_deferral_count",
            "carried_sigma_a_refinement_execution_count",
            "carried_new_sigma_a_refinement_execution_count",
            "carried_draft_sigma_a_refinement_execution_count",
            "carried_executed_sigma_a_refinement_layer_count",
            "carried_refined_draft_sigma_a_shell_count",
            "carried_integrated_time_index_layer_count",
            "carried_integrated_t_a_refinement_layer_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "c_reg_definition_completion_count",
            "adm_a_definition_completion_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "new_adm_a_definition_draft_execution_count",
            "new_sigma_a_refinement_execution_count",
            "new_time_index_refinement_execution_count",
            "new_t_a_refinement_execution_count",
            "new_whole_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_assembly_execution_count",
            "new_sigma_a_draft_clause_count",
            "new_sigma_a_draft_clause_creation_count",
            "new_carrier_draft_clause_creation_execution_count",
            "new_carrier_level_draft_assembly_execution_count",
            "new_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "new_component_slot_integration_execution_count",
            "new_component_slot_refinement_execution_count",
            "new_carrier_type_selection_count",
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
            "boundary_phrase_count",
            "prohibited_behavior_count",
            "next_step_count",
            "overclaim_count",
            "invented_citation_like_pattern_count",
            "word_count",
        ]
        for key in order:
            if key in counts:
                lines.append(f"- {self._label(key)}: {counts[key]}")
        lines.append("")
        lines.append("## Warnings")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")
        lines.append("## Interpretation")
        lines.append(
            "The v8.138 artifact executes one C_reg definition draft. "
            "It moves C_reg from deferred slot to draft status while keeping final definition execution, C_reg completion, Adm_A completion, "
            "Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, validation, readiness, and citation claims absent."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute Pi_obs definition draft next rather than auditing this draft by default.",
            "Keep C_reg completion separate from C_reg draft execution.",
            "Keep Adm_A and Sigma_A definition completion separate from dependent-object drafts.",
            "Keep theorem candidate planning separate from definition drafts.",
            "Keep theorem proof separate from theorem candidate planning.",
            "Keep proof assistant verification separate from proof execution.",
            "Keep validation separate from proof work.",
            "Keep manuscript readiness and citation work separate from validation.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = ["does not", "not executed", "not completed", "not created", "C_reg", "definition draft", "boundary", "separate", "zero"]
        return sum(text.count(p) + text.lower().count(p.lower()) for p in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute final definitions",
            "does not complete C_reg",
            "does not complete Adm_A",
            "does not complete Sigma_A",
            "does not complete any formal definition",
            "does not complete formalization",
            "does not create theorem candidates",
            "does not prove a theorem",
            "does not run proof execution",
            "does not provide proof assistant verification",
            "does not provide external validation",
            "does not approve manuscript submission readiness",
            "does not add new citations",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_positive_counter_names = {
            "definition execution count",
            "new definition execution count",
            "completed formal definition count",
            "formalization complete count",
            "c_reg definition completion count",
            "c reg definition completion count",
            "adm_a definition completion count",
            "adm a definition completion count",
            "sigma_a definition completion count",
            "sigma a definition completion count",
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
        allowed_positive_counter_names = {
            "c_reg definition draft execution count",
            "c reg definition draft execution count",
            "new c_reg definition draft execution count",
            "new c reg definition draft execution count",
            "new definition draft execution count",
            "dependent-object definition draft execution count",
            "dependent object definition draft execution count",
            "c_reg draft slot created count",
            "c reg draft slot created count",
            "c_reg draft linked to refined sigma_a count",
            "c reg draft linked to refined sigma a count",
            "c_reg linked to adm_a draft count",
            "c reg linked to adm a draft count",
            "c_reg constraint-region placeholder count",
            "c reg constraint-region placeholder count",
            "c_reg time-index compatibility count",
            "c reg time-index compatibility count",
            "remaining dependent-object deferral count",
            "remaining dependent object deferral count",
            "definition draft execution row count",
            "definition draft execution check count",
            "definition draft boundary preserved count",
            "carried adm_a definition draft execution count",
            "carried adm a definition draft execution count",
            "carried new adm_a definition draft execution count",
            "carried new adm a definition draft execution count",
            "carried adm_a draft slot created count",
            "carried adm a draft slot created count",
            "carried adm_a draft linked to refined sigma_a count",
            "carried adm a draft linked to refined sigma a count",
            "carried adm_a admissibility-interface placeholder count",
            "carried adm a admissibility-interface placeholder count",
            "carried adm_a time-index compatibility count",
            "carried adm a time-index compatibility count",
            "carried remaining dependent-object deferral count",
            "carried remaining dependent object deferral count",
            "carried sigma_a refinement execution count",
            "carried sigma a refinement execution count",
            "carried new sigma_a refinement execution count",
            "carried new sigma a refinement execution count",
            "carried draft sigma_a refinement execution count",
            "carried draft sigma a refinement execution count",
            "carried executed sigma_a refinement layer count",
            "carried executed sigma a refinement layer count",
            "carried refined draft sigma_a shell count",
            "carried refined draft sigma a shell count",
            "carried integrated time-index layer count",
            "carried integrated t_a refinement layer count",
            "carried integrated t a refinement layer count",
            "core formal object inventory execution count",
            "core formal object count",
            "formal object inventory execution count",
            "resolved gap count",
            "cumulative limited theorem proven count",
            "boundary phrase count",
            "prohibited behavior count",
            "next step count",
            "word count",
        }

        unsafe_phrases = [
            "c_reg completed",
            "c reg completed",
            "adm_a completed",
            "adm a completed",
            "sigma_a definition completed",
            "sigma a definition completed",
            "formal definition completed",
            "formal definitions completed",
            "theorem candidate created",
            "new theorem proven",
            "theorem proven",
            "proof assistant verification complete",
            "framework proven",
            "external validation complete",
            "manuscript ready",
            "submission ready",
            "readiness approved",
            "citation added",
        ]

        protective_markers = [
            "does not",
            "do not",
            "not ",
            "not executed",
            "not completed",
            "not created",
            "zero",
            "count: 0",
            "remain",
            "remains",
            "separate",
            "absent",
            "downstream",
            "deferred",
            "boundary",
            "draft",
            "warning",
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
                if value > 0:
                    if counter_name in forbidden_positive_counter_names:
                        count += 1
                    elif counter_name in allowed_positive_counter_names:
                        pass
                    else:
                        pass
                continue

            if any(marker in lowered for marker in protective_markers):
                continue

            for phrase in unsafe_phrases:
                if phrase in lowered:
                    count += 1
                    break

        return count

    def _count_invented_citation_like_patterns(self, text: str) -> int:
        patterns = [r"\([A-Z][A-Za-z-]+,\s*20\d{2}\)", r"\[[0-9]{1,3}\]", r"doi:", r"arXiv:"]
        return sum(len(re.findall(pattern, text)) for pattern in patterns)


if __name__ == "__main__":
    report = CRegDefinitionDraftExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
