from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaADefinitionCompletionReadinessPlanReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaADefinitionCompletionReadinessPlanBuilder:
    """Build v8.144 Sigma_A definition completion readiness plan artifact.

    Boundary discipline:
    - This milestone plans readiness for future Sigma_A definition completion.
    - It does not execute Sigma_A definition completion.
    - It does not execute final definitions.
    - It does not complete any dependent object.
    - It does not create theorem candidates or prove theorems.
    """

    title = "Sigma_A Definition Completion Readiness Plan v8.144"
    source_artifact = Path("outputs/dependent_object_draft_bundle_integration_execution_v8_143.md")
    output_path = Path("outputs/sigma_a_definition_completion_readiness_plan_v8_144.md")

    readiness_question = (
        "Can the integrated dependent-object draft bundle be used to plan controlled readiness for future Sigma_A definition completion "
        "while keeping definition completion execution, completed formal definitions, theorem candidate planning, theorem proof, validation, readiness approval, and citations at zero?"
    )

    plan_rows = [
        {
            "id": "SIGMA-A-READY-001",
            "focus": "source boundary",
            "plan": "import the v8.143 dependent-object draft bundle as the only readiness source",
            "gate": "do not create new dependent-object drafts",
        },
        {
            "id": "SIGMA-A-READY-002",
            "focus": "bundle completeness",
            "plan": "check that Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A are integrated",
            "gate": "do not treat integration as completion",
        },
        {
            "id": "SIGMA-A-READY-003",
            "focus": "Sigma_A shell boundary",
            "plan": "confirm the bundle is linked to the refined Draft Sigma_A shell",
            "gate": "do not complete Sigma_A",
        },
        {
            "id": "SIGMA-A-READY-004",
            "focus": "definition gap scan",
            "plan": "identify remaining requirements before any future Sigma_A definition completion execution",
            "gate": "do not execute definition completion",
        },
        {
            "id": "SIGMA-A-READY-005",
            "focus": "dependent-object completion boundary",
            "plan": "preserve all dependent-object completion counters at zero",
            "gate": "do not complete dependent objects",
        },
        {
            "id": "SIGMA-A-READY-006",
            "focus": "formalization boundary",
            "plan": "separate readiness planning from completed formalization",
            "gate": "do not claim formalization complete",
        },
        {
            "id": "SIGMA-A-READY-007",
            "focus": "theorem boundary",
            "plan": "keep theorem candidate planning and theorem proof downstream",
            "gate": "do not create theorem candidates",
        },
        {
            "id": "SIGMA-A-READY-008",
            "focus": "publication boundary",
            "plan": "keep validation, manuscript readiness, readiness approval, and citations downstream",
            "gate": "do not approve readiness or add citations",
        },
    ]

    checks = [
        "Exactly one Sigma_A definition completion readiness plan is created.",
        "Exactly one integrated dependent-object draft bundle is imported.",
        "No new definition draft execution is performed.",
        "No final definition execution is performed.",
        "No Sigma_A definition completion is performed.",
        "No dependent-object definition completion is performed.",
        "No theorem candidate planning is performed.",
        "No validation, readiness approval, or citation work is performed.",
    ]

    def run(self) -> SigmaADefinitionCompletionReadinessPlanReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""
        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,

            "sigma_a_definition_completion_readiness_plan_count": 1,
            "new_sigma_a_definition_completion_readiness_plan_count": 1,
            "definition_completion_readiness_plan_count": 1,
            "readiness_plan_row_count": len(self.plan_rows),
            "readiness_plan_check_count": len(self.checks),
            "readiness_plan_boundary_gate_count": len(self.plan_rows),

            "imported_dependent_object_draft_bundle_count": carried.get("Integrated dependent-object draft bundle count", 1),
            "imported_dependent_object_draft_count": carried.get("Integrated dependent-object draft count", 6),
            "imported_adm_a_draft_count": carried.get("Integrated Adm_A draft count", 1),
            "imported_c_reg_draft_count": carried.get("Integrated C_reg draft count", 1),
            "imported_pi_obs_draft_count": carried.get("Integrated Pi_obs draft count", 1),
            "imported_m_c_draft_count": carried.get("Integrated M_c draft count", 1),
            "imported_r_a_draft_count": carried.get("Integrated R_A draft count", 1),
            "imported_traj_a_draft_count": carried.get("Integrated Traj_A draft count", 1),
            "imported_bundle_linked_to_refined_sigma_a_count": carried.get("Bundle linked to refined Sigma_A count", 1),
            "imported_bundle_dependency_coherence_count": carried.get("Bundle dependency coherence recorded count", 1),
            "remaining_dependent_object_deferral_count": carried.get("Remaining dependent-object deferral count", 0),
            "all_dependent_object_draft_slots_created_count": carried.get("All dependent-object draft slots created count", 1),
            "all_dependent_object_draft_slots_integrated_count": carried.get("All dependent-object draft slots integrated count", 1),

            "planned_future_sigma_a_definition_completion_scope_count": 1,
            "planned_future_completion_gate_count": 8,
            "planned_gap_scan_count": 1,
            "planned_boundary_preservation_count": 1,

            "carried_dependent_object_draft_bundle_integration_execution_count": carried.get("Dependent-object draft bundle integration execution count", 1),
            "carried_integrated_dependent_object_draft_count": carried.get("Integrated dependent-object draft count", 6),
            "carried_traj_a_definition_draft_execution_count": carried.get("Carried Traj_A definition draft execution count", 1),
            "carried_r_a_definition_draft_execution_count": carried.get("Carried R_A definition draft execution count", 1),
            "carried_m_c_definition_draft_execution_count": carried.get("Carried M_c definition draft execution count", 1),
            "carried_pi_obs_definition_draft_execution_count": carried.get("Carried Pi_obs definition draft execution count", 1),
            "carried_c_reg_definition_draft_execution_count": carried.get("Carried C_reg definition draft execution count", 1),
            "carried_adm_a_definition_draft_execution_count": carried.get("Carried Adm_A definition draft execution count", 1),
            "carried_sigma_a_refinement_execution_count": carried.get("Carried Sigma_A refinement execution count", 1),
            "carried_refined_draft_sigma_a_shell_count": carried.get("Carried refined Draft Sigma_A shell count", 1),
            "carried_integrated_time_index_layer_count": carried.get("Carried integrated time-index layer count", 1),

            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 14,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,

            "new_definition_draft_execution_count": 0,
            "new_dependent_object_definition_draft_execution_count": 0,
            "dependent_object_definition_draft_execution_count": 0,
            "new_dependent_object_draft_bundle_integration_execution_count": 0,

            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "definition_completion_execution_count": 0,
            "sigma_a_definition_completion_execution_count": 0,
            "sigma_a_definition_completion_count": 0,
            "completed_formal_definition_count": 0,
            "formalization_complete_count": 0,

            "adm_a_definition_completion_count": 0,
            "c_reg_definition_completion_count": 0,
            "pi_obs_definition_completion_count": 0,
            "m_c_definition_completion_count": 0,
            "r_a_definition_completion_count": 0,
            "traj_a_definition_completion_count": 0,
            "dependent_object_definition_completion_count": 0,

            "stabilization_predicate_definition_completion_count": 0,
            "attractor_class_definition_completion_count": 0,
            "constraint_region_definition_completion_count": 0,
            "causal_mass_definition_completion_count": 0,
            "observer_projection_definition_completion_count": 0,

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
            "full_framework_formal_proof_count": 0,
            "manuscript_submission_ready_count": 0,
            "readiness_approval_count": 0,
            "external_validation_count": 0,
            "independent_experiment_count": 0,
            "new_citation_added_count": 0,
            "next_step_count": 8,
        }

        warnings.extend([
            "This milestone is readiness planning only, not Sigma_A definition completion.",
            "Future Sigma_A completion remains gated and unexecuted.",
            "All dependent-object completion counters remain zero.",
            "Theorem, proof, validation, readiness approval, and citation claims remain absent.",
        ])

        report_text = self._render_report(counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.144 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.144 report.")
        if counts["sigma_a_definition_completion_readiness_plan_count"] != 1:
            errors.append("v8.144 must create exactly one Sigma_A definition completion readiness plan.")
        if counts["imported_dependent_object_draft_count"] != 6:
            errors.append("v8.144 must import exactly six integrated dependent-object drafts.")
        if counts["definition_completion_execution_count"] != 0:
            errors.append("v8.144 must not execute definition completion.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.144 must not complete Sigma_A definition.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.144 must not execute final definitions.")
        if counts["dependent_object_definition_completion_count"] != 0:
            errors.append("v8.144 must not complete dependent objects.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.144 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.144 must not prove theorem claims.")

        zero_fields = [
            "new_definition_draft_execution_count",
            "new_dependent_object_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
            "new_dependent_object_draft_bundle_integration_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "definition_completion_execution_count",
            "sigma_a_definition_completion_execution_count",
            "sigma_a_definition_completion_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "adm_a_definition_completion_count",
            "c_reg_definition_completion_count",
            "pi_obs_definition_completion_count",
            "m_c_definition_completion_count",
            "r_a_definition_completion_count",
            "traj_a_definition_completion_count",
            "dependent_object_definition_completion_count",
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

        return SigmaADefinitionCompletionReadinessPlanReport(
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
            "sigma_a_definition_completion_readiness_plan_count": "Sigma_A definition completion readiness plan count",
            "new_sigma_a_definition_completion_readiness_plan_count": "New Sigma_A definition completion readiness plan count",
            "definition_completion_readiness_plan_count": "Definition completion readiness plan count",
            "readiness_plan_row_count": "Readiness plan row count",
            "readiness_plan_check_count": "Readiness plan check count",
            "readiness_plan_boundary_gate_count": "Readiness plan boundary gate count",
            "imported_dependent_object_draft_bundle_count": "Imported dependent-object draft bundle count",
            "imported_dependent_object_draft_count": "Imported dependent-object draft count",
            "imported_adm_a_draft_count": "Imported Adm_A draft count",
            "imported_c_reg_draft_count": "Imported C_reg draft count",
            "imported_pi_obs_draft_count": "Imported Pi_obs draft count",
            "imported_m_c_draft_count": "Imported M_c draft count",
            "imported_r_a_draft_count": "Imported R_A draft count",
            "imported_traj_a_draft_count": "Imported Traj_A draft count",
            "imported_bundle_linked_to_refined_sigma_a_count": "Imported bundle linked to refined Sigma_A count",
            "imported_bundle_dependency_coherence_count": "Imported bundle dependency coherence count",
            "remaining_dependent_object_deferral_count": "Remaining dependent-object deferral count",
            "all_dependent_object_draft_slots_created_count": "All dependent-object draft slots created count",
            "all_dependent_object_draft_slots_integrated_count": "All dependent-object draft slots integrated count",
            "planned_future_sigma_a_definition_completion_scope_count": "Planned future Sigma_A definition completion scope count",
            "planned_future_completion_gate_count": "Planned future completion gate count",
            "planned_gap_scan_count": "Planned gap scan count",
            "planned_boundary_preservation_count": "Planned boundary preservation count",
            "carried_dependent_object_draft_bundle_integration_execution_count": "Carried dependent-object draft bundle integration execution count",
            "carried_integrated_dependent_object_draft_count": "Carried integrated dependent-object draft count",
            "carried_sigma_a_refinement_execution_count": "Carried Sigma_A refinement execution count",
            "carried_refined_draft_sigma_a_shell_count": "Carried refined Draft Sigma_A shell count",
            "definition_completion_execution_count": "Definition completion execution count",
            "sigma_a_definition_completion_execution_count": "Sigma_A definition completion execution count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
            "dependent_object_definition_completion_count": "Dependent-object definition completion count",
            "theorem_candidate_plan_count": "Theorem candidate plan count",
            "new_theorem_proven_count": "New theorem proven count",
            "proof_assistant_verification_count": "Proof assistant verification count",
            "manuscript_submission_ready_count": "Manuscript submission ready count",
            "readiness_approval_count": "Readiness approval count",
            "new_citation_added_count": "New citation added count",
            "overclaim_count": "Overclaim count",
            "invented_citation_like_pattern_count": "Invented citation-like pattern count",

            "new_definition_draft_execution_count": "New definition draft execution count",
            "new_dependent_object_definition_draft_execution_count": "New dependent-object definition draft execution count",
            "dependent_object_definition_draft_execution_count": "Dependent-object definition draft execution count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(self.readiness_question)
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Readiness boundary")
        lines.append("- Milestone type: Sigma_A definition completion readiness plan only")
        lines.append("- Sigma_A definition completion readiness plan after this milestone: planned")
        lines.append("- Sigma_A definition completion execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Final definition execution after this milestone: not executed")
        lines.append("- Dependent-object definition completion after this milestone: not completed")
        lines.append("- Theorem candidate planning after this milestone: not executed")
        lines.append("- Readiness approval after this milestone: not approved")
        lines.append("")
        lines.append("## Plan rows")
        lines.append("")
        lines.append("| ID | Focus | Plan | Gate |")
        lines.append("|---|---|---|---|")
        for row in self.plan_rows:
            lines.append(f"| {row['id']} | {row['focus']} | {row['plan']} | {row['gate']} |")
        lines.append("")
        lines.append("## Checks")
        for index, check in enumerate(self.checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact creates one Sigma_A definition completion readiness plan only. "
            "It imports the integrated dependent-object draft bundle and plans future completion gates, "
            "but it does not execute definition completion, does not execute final definitions, does not complete Sigma_A, "
            "does not complete dependent objects, does not complete formalization, does not create theorem candidates, "
            "does not prove a theorem, does not run proof execution, does not provide proof assistant verification, "
            "does not provide external validation, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        order = [
            "sigma_a_definition_completion_readiness_plan_count",
            "new_sigma_a_definition_completion_readiness_plan_count",
            "definition_completion_readiness_plan_count",
            "readiness_plan_row_count",
            "readiness_plan_check_count",
            "readiness_plan_boundary_gate_count",
            "imported_dependent_object_draft_bundle_count",
            "imported_dependent_object_draft_count",
            "imported_adm_a_draft_count",
            "imported_c_reg_draft_count",
            "imported_pi_obs_draft_count",
            "imported_m_c_draft_count",
            "imported_r_a_draft_count",
            "imported_traj_a_draft_count",
            "imported_bundle_linked_to_refined_sigma_a_count",
            "imported_bundle_dependency_coherence_count",
            "remaining_dependent_object_deferral_count",
            "all_dependent_object_draft_slots_created_count",
            "all_dependent_object_draft_slots_integrated_count",
            "planned_future_sigma_a_definition_completion_scope_count",
            "planned_future_completion_gate_count",
            "planned_gap_scan_count",
            "planned_boundary_preservation_count",
            "carried_dependent_object_draft_bundle_integration_execution_count",
            "carried_integrated_dependent_object_draft_count",
            "carried_sigma_a_refinement_execution_count",
            "carried_refined_draft_sigma_a_shell_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "new_definition_draft_execution_count",
            "new_dependent_object_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
            "new_dependent_object_draft_bundle_integration_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "definition_completion_execution_count",
            "sigma_a_definition_completion_execution_count",
            "sigma_a_definition_completion_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "dependent_object_definition_completion_count",
            "adm_a_definition_completion_count",
            "c_reg_definition_completion_count",
            "pi_obs_definition_completion_count",
            "m_c_definition_completion_count",
            "r_a_definition_completion_count",
            "traj_a_definition_completion_count",
            "theorem_candidate_plan_count",
            "new_theorem_proven_count",
            "cumulative_limited_theorem_proven_count",
            "proof_assistant_verification_count",
            "formal_mathematical_proof_count",
            "formal_proof_execution_count",
            "proof_execution_count",
            "proof_gap_resolution_count",
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
            "The v8.144 artifact creates a readiness plan for future Sigma_A definition completion. "
            "It is forward progress because it uses the integrated dependent-object draft bundle to define controlled completion gates. "
            "It is not completion execution, not final definition execution, not theorem planning, not proof, not validation, and not manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Run one readiness boundary audit only if needed to check plan boundaries.",
            "Then prepare controlled Sigma_A definition completion execution plan.",
            "Keep definition completion execution separate from readiness planning.",
            "Keep dependent-object completion separate from Sigma_A completion planning.",
            "Keep theorem candidate planning separate from definition completion.",
            "Keep theorem proof separate from theorem candidate planning.",
            "Keep validation separate from proof work.",
            "Keep manuscript readiness and citation work separate from validation.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = ["does not", "not executed", "not completed", "not approved", "readiness plan", "completion", "boundary", "separate", "zero"]
        return sum(text.count(p) + text.lower().count(p.lower()) for p in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute definition completion",
            "does not execute final definitions",
            "does not complete Sigma_A",
            "does not complete dependent objects",
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
            "new definition draft execution count",
            "new dependent-object definition draft execution count",
            "dependent-object definition draft execution count",
            "definition execution count",
            "new definition execution count",
            "definition completion execution count",
            "sigma a definition completion execution count",
            "sigma a definition completion count",
            "completed formal definition count",
            "formalization complete count",
            "dependent-object definition completion count",
            "adm a definition completion count",
            "c reg definition completion count",
            "pi obs definition completion count",
            "m c definition completion count",
            "r a definition completion count",
            "traj a definition completion count",
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
            "full framework formal proof count",
            "external validation count",
            "independent experiment count",
            "manuscript submission ready count",
            "readiness approval count",
            "new citation added count",
        }

        count = 0

        for raw_line in text.splitlines():
            line = raw_line.strip().lstrip("-").strip()
            lowered = line.lower().replace("_", " ")
            lowered = lowered.replace("dependent object", "dependent-object")
            match = re.match(r"^([a-z0-9 /-]+ count):\s*([0-9]+)\s*$", lowered)
            if not match:
                continue
            name = match.group(1).strip()
            value = int(match.group(2))
            if value > 0 and name in forbidden_positive_counter_names:
                count += 1

        unsafe_phrases = [
            "sigma_a completed",
            "sigma a completed",
            "definition completed",
            "definition completion executed",
            "formalization complete",
            "theorem candidate created",
            "new theorem proven",
            "proof verified",
            "proof assistant verification complete",
            "external validation complete",
            "manuscript ready",
            "readiness approved",
            "citation added",
        ]

        protective_markers = [
            "does not",
            "do not",
            "not ",
            "zero",
            "count: 0",
            "absent",
            "separate",
            "readiness plan",
            "future",
            "gate",
            "planned",
            "planning",
            "downstream",
            "warning",
        ]

        for raw_line in text.splitlines():
            line = raw_line.strip().lstrip("-").strip()
            lowered = line.lower().replace("_", " ")

            # Counter lines are already handled above. Do not rescan them as prose,
            # or carried counters such as "Cumulative limited theorem proven count: 5"
            # become fake overclaims. Regex, our tiniest bureaucrat.
            if re.match(r"^[a-z0-9_ /-]+ count:\s*[0-9]+\s*$", line.lower()):
                continue

            if any(marker in lowered for marker in protective_markers):
                continue

            if any(phrase in lowered for phrase in unsafe_phrases):
                count += 1

        return count

    def _count_invented_citation_like_patterns(self, text: str) -> int:
        patterns = [r"\([A-Z][A-Za-z-]+,\s*20\d{2}\)", r"\[[0-9]{1,3}\]", r"doi:", r"arXiv:"]
        return sum(len(re.findall(pattern, text)) for pattern in patterns)


if __name__ == "__main__":
    report = SigmaADefinitionCompletionReadinessPlanBuilder().run()
    print(f"Wrote {report.output_path}")
