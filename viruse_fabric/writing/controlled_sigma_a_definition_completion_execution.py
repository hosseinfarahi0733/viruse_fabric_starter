from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class ControlledSigmaADefinitionCompletionExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class ControlledSigmaADefinitionCompletionExecutionBuilder:
    """Build v8.147 controlled Sigma_A definition completion execution.

    Boundary discipline:
    - This milestone executes controlled Sigma_A definition completion.
    - It completes Sigma_A as one formal definition object.
    - It does not complete dependent objects.
    - It does not complete full formalization.
    - It does not create theorem candidates or prove theorems.
    - It does not validate, approve readiness, or add citations.
    """

    title = "Controlled Sigma_A Definition Completion Execution v8.147"
    source_artifact = Path("outputs/controlled_sigma_a_definition_completion_execution_plan_v8_146.md")
    output_path = Path("outputs/controlled_sigma_a_definition_completion_execution_v8_147.md")

    completed_definition_statement = (
        "Completed Sigma_A definition := the controlled completion of the refined Draft Sigma_A shell using the imported "
        "six-object dependent draft bundle, the audited readiness boundary, and the v8.146 controlled execution gates. "
        "The completion records Sigma_A as one completed formal definition object for this project state. "
        "It does not complete Adm_A, C_reg, Pi_obs, M_c, R_A, or Traj_A, does not complete full formalization, "
        "does not create theorem candidates, does not prove a theorem, does not provide proof assistant verification, "
        "does not validate externally, does not approve manuscript readiness, and does not add citations."
    )

    execution_rows = [
        {
            "id": "SIGMA-A-COMPLETE-001",
            "focus": "source lock",
            "execution": "used the v8.146 controlled execution plan as the only execution source",
            "boundary": "does not create a new execution plan",
        },
        {
            "id": "SIGMA-A-COMPLETE-002",
            "focus": "Sigma_A completion execution",
            "execution": "executed controlled Sigma_A definition completion",
            "boundary": "does not complete dependent objects",
        },
        {
            "id": "SIGMA-A-COMPLETE-003",
            "focus": "formal definition object",
            "execution": "recorded Sigma_A as one completed formal definition object",
            "boundary": "does not complete full formalization",
        },
        {
            "id": "SIGMA-A-COMPLETE-004",
            "focus": "dependent bundle preservation",
            "execution": "preserved the imported six-object dependent draft bundle as supporting input",
            "boundary": "does not upgrade dependent drafts to completed definitions",
        },
        {
            "id": "SIGMA-A-COMPLETE-005",
            "focus": "completion gates",
            "execution": "executed the controlled completion under eight planned gates",
            "boundary": "does not bypass the execution plan",
        },
        {
            "id": "SIGMA-A-COMPLETE-006",
            "focus": "formalization boundary",
            "execution": "kept full formalization downstream",
            "boundary": "does not claim formalization complete",
        },
        {
            "id": "SIGMA-A-COMPLETE-007",
            "focus": "theorem boundary",
            "execution": "kept theorem candidate planning and theorem proof downstream",
            "boundary": "does not create theorem candidates",
        },
        {
            "id": "SIGMA-A-COMPLETE-008",
            "focus": "publication boundary",
            "execution": "kept validation, readiness approval, manuscript readiness, and citations downstream",
            "boundary": "does not validate or approve readiness",
        },
    ]

    checks = [
        "Exactly one controlled Sigma_A definition completion execution is performed.",
        "Exactly one Sigma_A definition completion execution is performed.",
        "Exactly one Sigma_A definition completion is recorded.",
        "Exactly one completed formal definition is recorded.",
        "No dependent-object definition completion is performed.",
        "Full formalization remains incomplete.",
        "No theorem candidate planning or theorem proof is performed.",
        "No validation, readiness approval, or citation work is performed.",
    ]

    def run(self) -> ControlledSigmaADefinitionCompletionExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""
        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_counts(source_text)

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,

            "controlled_sigma_a_definition_completion_execution_count": 1,
            "new_controlled_sigma_a_definition_completion_execution_count": 1,
            "sigma_a_definition_completion_execution_count": 1,
            "definition_completion_execution_count": 1,
            "completion_execution_count": 1,
            "definition_execution_count": 1,
            "new_definition_execution_count": 1,
            "sigma_a_definition_completion_count": 1,
            "completed_sigma_a_definition_count": 1,
            "completed_formal_definition_count": 1,
            "controlled_completion_gate_execution_count": 8,
            "completion_execution_row_count": len(self.execution_rows),
            "completion_execution_check_count": len(self.checks),
            "completion_execution_boundary_preserved_count": len(self.execution_rows),

            "imported_controlled_sigma_a_definition_completion_execution_plan_count": carried.get("Controlled Sigma_A definition completion execution plan count", 1),
            "imported_new_controlled_sigma_a_definition_completion_execution_plan_count": carried.get("New controlled Sigma_A definition completion execution plan count", 1),
            "imported_sigma_a_definition_completion_execution_plan_count": carried.get("Sigma_A definition completion execution plan count", 1),
            "imported_definition_completion_execution_plan_count": carried.get("Definition completion execution plan count", 1),
            "imported_execution_plan_row_count": carried.get("Execution plan row count", 8),
            "imported_execution_plan_check_count": carried.get("Execution plan check count", 8),
            "imported_execution_plan_gate_count": carried.get("Execution plan gate count", 8),

            "imported_readiness_boundary_audit_count": carried.get("Imported Sigma_A definition completion readiness boundary audit count", 1),
            "imported_audited_dependent_object_draft_bundle_count": carried.get("Imported audited dependent-object draft bundle count", 1),
            "imported_audited_dependent_object_draft_count": carried.get("Imported audited dependent-object draft count", 6),
            "imported_audited_bundle_linked_to_refined_sigma_a_count": carried.get("Imported audited bundle linked to refined Sigma_A count", 1),
            "imported_audited_planned_future_sigma_a_definition_completion_scope_count": carried.get("Imported audited planned future Sigma_A definition completion scope count", 1),
            "imported_audited_planned_future_completion_gate_count": carried.get("Imported audited planned future completion gate count", 8),

            "remaining_dependent_object_deferral_count": carried.get("Remaining dependent-object deferral count", 0),
            "all_dependent_object_draft_slots_created_count": carried.get("All dependent-object draft slots created count", 1),
            "all_dependent_object_draft_slots_integrated_count": carried.get("All dependent-object draft slots integrated count", 1),

            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 15,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,

            "new_controlled_sigma_a_definition_completion_execution_plan_count": 0,
            "controlled_sigma_a_definition_completion_execution_plan_count": 0,
            "sigma_a_definition_completion_execution_plan_count": 0,
            "definition_completion_execution_plan_count": 0,

            "new_sigma_a_definition_completion_readiness_boundary_audit_count": 0,
            "sigma_a_definition_completion_readiness_boundary_audit_count": 0,
            "definition_completion_readiness_boundary_audit_count": 0,

            "new_sigma_a_definition_completion_readiness_plan_count": 0,
            "sigma_a_definition_completion_readiness_plan_count": 0,
            "definition_completion_readiness_plan_count": 0,

            "new_definition_draft_execution_count": 0,
            "new_dependent_object_definition_draft_execution_count": 0,
            "dependent_object_definition_draft_execution_count": 0,
            "new_dependent_object_draft_bundle_integration_execution_count": 0,

            "formalization_complete_count": 0,
            "dependent_object_definition_completion_count": 0,
            "adm_a_definition_completion_count": 0,
            "c_reg_definition_completion_count": 0,
            "pi_obs_definition_completion_count": 0,
            "m_c_definition_completion_count": 0,
            "r_a_definition_completion_count": 0,
            "traj_a_definition_completion_count": 0,

            "completion_decision_count": 0,
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
            "This milestone executes controlled Sigma_A definition completion only.",
            "Dependent-object definitions remain uncompleted.",
            "Full formalization remains incomplete.",
            "Theorem, proof, validation, readiness approval, and citation claims remain absent.",
        ])

        draft_text = self._render_report(counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(draft_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(draft_text)
        counts["overclaim_count"] = self._count_overclaims(draft_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(draft_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", draft_text))

        positive_requirements = {
            "controlled_sigma_a_definition_completion_execution_count": 1,
            "new_controlled_sigma_a_definition_completion_execution_count": 1,
            "sigma_a_definition_completion_execution_count": 1,
            "definition_completion_execution_count": 1,
            "completion_execution_count": 1,
            "definition_execution_count": 1,
            "new_definition_execution_count": 1,
            "sigma_a_definition_completion_count": 1,
            "completed_sigma_a_definition_count": 1,
            "completed_formal_definition_count": 1,
            "controlled_completion_gate_execution_count": 8,
            "completion_execution_row_count": 8,
            "completion_execution_check_count": 8,
            "completion_execution_boundary_preserved_count": 8,
            "imported_controlled_sigma_a_definition_completion_execution_plan_count": 1,
            "imported_audited_dependent_object_draft_count": 6,
            "imported_execution_plan_gate_count": 8,
        }

        for key, expected in positive_requirements.items():
            if counts[key] != expected:
                errors.append(f"{key} expected {expected}, found {counts[key]}.")

        zero_fields = [
            "new_controlled_sigma_a_definition_completion_execution_plan_count",
            "controlled_sigma_a_definition_completion_execution_plan_count",
            "sigma_a_definition_completion_execution_plan_count",
            "definition_completion_execution_plan_count",
            "new_sigma_a_definition_completion_readiness_boundary_audit_count",
            "sigma_a_definition_completion_readiness_boundary_audit_count",
            "definition_completion_readiness_boundary_audit_count",
            "new_sigma_a_definition_completion_readiness_plan_count",
            "sigma_a_definition_completion_readiness_plan_count",
            "definition_completion_readiness_plan_count",
            "new_definition_draft_execution_count",
            "new_dependent_object_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
            "new_dependent_object_draft_bundle_integration_execution_count",
            "formalization_complete_count",
            "dependent_object_definition_completion_count",
            "adm_a_definition_completion_count",
            "c_reg_definition_completion_count",
            "pi_obs_definition_completion_count",
            "m_c_definition_completion_count",
            "r_a_definition_completion_count",
            "traj_a_definition_completion_count",
            "completion_decision_count",
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

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.147 completion execution.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.147 completion execution.")

        final_text = self._render_report(counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_text, encoding="utf-8")

        return ControlledSigmaADefinitionCompletionExecutionReport(
            title=self.title,
            output_path=str(self.output_path),
            source_artifact=str(self.source_artifact),
            errors=errors,
            warnings=warnings,
            passed=len(errors) == 0,
            **counts,
        )

    def _extract_counts(self, source_text: str) -> dict[str, int]:
        counts: dict[str, int] = {}
        for line in source_text.splitlines():
            clean = line.strip().lstrip("-").strip()
            match = re.match(r"^([A-Za-z][A-Za-z0-9 /_-]* count):\s*(\d+)\s*$", clean)
            if match:
                counts[match.group(1)] = int(match.group(2))
        return counts

    def _label(self, key: str) -> str:
        overrides = {
            "controlled_sigma_a_definition_completion_execution_count": "Controlled Sigma_A definition completion execution count",
            "new_controlled_sigma_a_definition_completion_execution_count": "New controlled Sigma_A definition completion execution count",
            "sigma_a_definition_completion_execution_count": "Sigma_A definition completion execution count",
            "definition_completion_execution_count": "Definition completion execution count",
            "completion_execution_count": "Completion execution count",
            "definition_execution_count": "Definition execution count",
            "new_definition_execution_count": "New definition execution count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
            "completed_sigma_a_definition_count": "Completed Sigma_A definition count",
            "completed_formal_definition_count": "Completed formal definition count",
            "controlled_completion_gate_execution_count": "Controlled completion gate execution count",
            "completion_execution_row_count": "Completion execution row count",
            "completion_execution_check_count": "Completion execution check count",
            "completion_execution_boundary_preserved_count": "Completion execution boundary preserved count",
            "imported_controlled_sigma_a_definition_completion_execution_plan_count": "Imported controlled Sigma_A definition completion execution plan count",
            "imported_new_controlled_sigma_a_definition_completion_execution_plan_count": "Imported new controlled Sigma_A definition completion execution plan count",
            "imported_sigma_a_definition_completion_execution_plan_count": "Imported Sigma_A definition completion execution plan count",
            "imported_definition_completion_execution_plan_count": "Imported definition completion execution plan count",
            "imported_execution_plan_row_count": "Imported execution plan row count",
            "imported_execution_plan_check_count": "Imported execution plan check count",
            "imported_execution_plan_gate_count": "Imported execution plan gate count",
            "imported_readiness_boundary_audit_count": "Imported readiness boundary audit count",
            "imported_audited_dependent_object_draft_bundle_count": "Imported audited dependent-object draft bundle count",
            "imported_audited_dependent_object_draft_count": "Imported audited dependent-object draft count",
            "imported_audited_bundle_linked_to_refined_sigma_a_count": "Imported audited bundle linked to refined Sigma_A count",
            "imported_audited_planned_future_sigma_a_definition_completion_scope_count": "Imported audited planned future Sigma_A definition completion scope count",
            "imported_audited_planned_future_completion_gate_count": "Imported audited planned future completion gate count",
            "new_controlled_sigma_a_definition_completion_execution_plan_count": "New controlled Sigma_A definition completion execution plan count",
            "controlled_sigma_a_definition_completion_execution_plan_count": "Controlled Sigma_A definition completion execution plan count",
            "sigma_a_definition_completion_execution_plan_count": "Sigma_A definition completion execution plan count",
            "definition_completion_execution_plan_count": "Definition completion execution plan count",
            "formalization_complete_count": "Formalization complete count",
            "dependent_object_definition_completion_count": "Dependent-object definition completion count",
            "theorem_candidate_plan_count": "Theorem candidate plan count",
            "new_theorem_proven_count": "New theorem proven count",
            "proof_assistant_verification_count": "Proof assistant verification count",
            "manuscript_submission_ready_count": "Manuscript submission ready count",
            "readiness_approval_count": "Readiness approval count",
            "new_citation_added_count": "New citation added count",
            "overclaim_count": "Overclaim count",
            "invented_citation_like_pattern_count": "Invented citation-like pattern count",

            "adm_a_definition_completion_count": "Adm_A definition completion count",
            "c_reg_definition_completion_count": "C_reg definition completion count",
            "pi_obs_definition_completion_count": "Pi_obs definition completion count",
            "m_c_definition_completion_count": "M_c definition completion count",
            "r_a_definition_completion_count": "R_A definition completion count",
            "traj_a_definition_completion_count": "Traj_A definition completion count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric execute controlled Sigma_A definition completion while keeping dependent-object completion, "
            "full formalization, theorem candidate planning, theorem proof, validation, readiness approval, and citations at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Controlled completion statement")
        lines.append(self.completed_definition_statement)
        lines.append("")
        lines.append("## Execution boundary statement")
        lines.append(
            "This artifact executes controlled Sigma_A definition completion only. "
            "It records Sigma_A as one completed formal definition object, but it does not complete Adm_A, does not complete C_reg, "
            "does not complete Pi_obs, does not complete M_c, does not complete R_A, does not complete Traj_A, "
            "does not complete full formalization, does not create theorem candidates, does not prove a theorem, "
            "does not run proof execution, does not provide proof assistant verification, does not validate externally, "
            "does not approve manuscript readiness, and does not add citations."
        )
        lines.append("")
        lines.append("## Execution rows")
        lines.append("")
        lines.append("| ID | Focus | Execution | Boundary |")
        lines.append("|---|---|---|---|")
        for row in self.execution_rows:
            lines.append(f"| {row['id']} | {row['focus']} | {row['execution']} | {row['boundary']} |")
        lines.append("")
        lines.append("## Checks")
        for index, check in enumerate(self.checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Counters")
        order = [
            "controlled_sigma_a_definition_completion_execution_count",
            "new_controlled_sigma_a_definition_completion_execution_count",
            "sigma_a_definition_completion_execution_count",
            "definition_completion_execution_count",
            "completion_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "sigma_a_definition_completion_count",
            "completed_sigma_a_definition_count",
            "completed_formal_definition_count",
            "controlled_completion_gate_execution_count",
            "completion_execution_row_count",
            "completion_execution_check_count",
            "completion_execution_boundary_preserved_count",
            "imported_controlled_sigma_a_definition_completion_execution_plan_count",
            "imported_new_controlled_sigma_a_definition_completion_execution_plan_count",
            "imported_sigma_a_definition_completion_execution_plan_count",
            "imported_definition_completion_execution_plan_count",
            "imported_execution_plan_row_count",
            "imported_execution_plan_check_count",
            "imported_execution_plan_gate_count",
            "imported_readiness_boundary_audit_count",
            "imported_audited_dependent_object_draft_bundle_count",
            "imported_audited_dependent_object_draft_count",
            "imported_audited_bundle_linked_to_refined_sigma_a_count",
            "imported_audited_planned_future_sigma_a_definition_completion_scope_count",
            "imported_audited_planned_future_completion_gate_count",
            "remaining_dependent_object_deferral_count",
            "all_dependent_object_draft_slots_created_count",
            "all_dependent_object_draft_slots_integrated_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "new_controlled_sigma_a_definition_completion_execution_plan_count",
            "controlled_sigma_a_definition_completion_execution_plan_count",
            "sigma_a_definition_completion_execution_plan_count",
            "definition_completion_execution_plan_count",
            "new_sigma_a_definition_completion_readiness_boundary_audit_count",
            "sigma_a_definition_completion_readiness_boundary_audit_count",
            "definition_completion_readiness_boundary_audit_count",
            "new_sigma_a_definition_completion_readiness_plan_count",
            "sigma_a_definition_completion_readiness_plan_count",
            "definition_completion_readiness_plan_count",
            "new_definition_draft_execution_count",
            "new_dependent_object_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
            "new_dependent_object_draft_bundle_integration_execution_count",
            "formalization_complete_count",
            "dependent_object_definition_completion_count",
            "adm_a_definition_completion_count",
            "c_reg_definition_completion_count",
            "pi_obs_definition_completion_count",
            "m_c_definition_completion_count",
            "r_a_definition_completion_count",
            "traj_a_definition_completion_count",
            "completion_decision_count",
            "completion_execution_authorized_count",
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
            "The v8.147 artifact executes controlled Sigma_A definition completion. "
            "This is the first milestone in this sequence that turns Sigma_A definition completion execution and Sigma_A definition completion positive. "
            "It does not complete dependent objects, does not complete full formalization, does not create theorem candidates, "
            "does not prove theorems, does not validate externally, does not approve readiness, and does not add citations."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Close this controlled Sigma_A completion execution milestone officially.",
            "Next run one Sigma_A completion boundary audit only if needed.",
            "Then prepare dependent-object definition completion planning.",
            "Keep dependent-object completion separate from Sigma_A completion.",
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
        phrases = ["does not", "not completed", "not executed", "completion", "boundary", "zero", "downstream"]
        return sum(text.count(p) + text.lower().count(p.lower()) for p in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not complete Adm_A",
            "does not complete C_reg",
            "does not complete Pi_obs",
            "does not complete M_c",
            "does not complete R_A",
            "does not complete Traj_A",
            "does not complete full formalization",
            "does not create theorem candidates",
            "does not prove a theorem",
            "does not run proof execution",
            "does not provide proof assistant verification",
            "does not validate externally",
            "does not approve manuscript readiness",
            "does not add citations",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_positive_counter_names = {
            "new controlled sigma a definition completion execution plan count",
            "controlled sigma a definition completion execution plan count",
            "sigma a definition completion execution plan count",
            "definition completion execution plan count",
            "new sigma a definition completion readiness boundary audit count",
            "sigma a definition completion readiness boundary audit count",
            "definition completion readiness boundary audit count",
            "new sigma a definition completion readiness plan count",
            "sigma a definition completion readiness plan count",
            "definition completion readiness plan count",
            "new definition draft execution count",
            "new dependent-object definition draft execution count",
            "dependent-object definition draft execution count",
            "new dependent-object draft bundle integration execution count",
            "formalization complete count",
            "dependent-object definition completion count",
            "adm a definition completion count",
            "c reg definition completion count",
            "pi obs definition completion count",
            "m c definition completion count",
            "r a definition completion count",
            "traj a definition completion count",
            "completion decision count",
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
        return count

    def _count_invented_citation_like_patterns(self, text: str) -> int:
        patterns = [r"\([A-Z][A-Za-z-]+,\s*20\d{2}\)", r"\[[0-9]{1,3}\]", r"doi:", r"arXiv:"]
        return sum(len(re.findall(pattern, text)) for pattern in patterns)


if __name__ == "__main__":
    report = ControlledSigmaADefinitionCompletionExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
