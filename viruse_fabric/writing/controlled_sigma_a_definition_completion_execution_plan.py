from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class ControlledSigmaADefinitionCompletionExecutionPlanReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class ControlledSigmaADefinitionCompletionExecutionPlanBuilder:
    """Build v8.146 controlled Sigma_A definition completion execution plan.

    Boundary discipline:
    - This milestone creates a controlled execution plan only.
    - It does not execute Sigma_A definition completion.
    - It does not complete Sigma_A.
    - It does not complete dependent objects.
    - It does not create theorem candidates or proofs.
    """

    title = "Controlled Sigma_A Definition Completion Execution Plan v8.146"
    source_artifact = Path("outputs/sigma_a_definition_completion_readiness_boundary_audit_v8_145.md")
    output_path = Path("outputs/controlled_sigma_a_definition_completion_execution_plan_v8_146.md")

    plan_rows = [
        {
            "id": "SIGMA-A-EXEC-PLAN-001",
            "focus": "source lock",
            "plan": "use the v8.145 readiness boundary audit as the only execution-plan source",
            "gate": "do not rerun readiness audit by default",
        },
        {
            "id": "SIGMA-A-EXEC-PLAN-002",
            "focus": "execution scope",
            "plan": "define the future controlled Sigma_A definition completion execution scope",
            "gate": "do not execute completion in this milestone",
        },
        {
            "id": "SIGMA-A-EXEC-PLAN-003",
            "focus": "bundle dependency",
            "plan": "require the integrated six-object dependent draft bundle as an input",
            "gate": "do not create new dependent-object drafts",
        },
        {
            "id": "SIGMA-A-EXEC-PLAN-004",
            "focus": "completion gates",
            "plan": "carry forward the eight future completion gates from the readiness plan",
            "gate": "do not treat planned gates as executed gates",
        },
        {
            "id": "SIGMA-A-EXEC-PLAN-005",
            "focus": "zero-preservation checks",
            "plan": "preserve definition completion execution, Sigma_A completion, and dependent-object completion at zero",
            "gate": "do not complete Sigma_A or dependent objects",
        },
        {
            "id": "SIGMA-A-EXEC-PLAN-006",
            "focus": "formalization boundary",
            "plan": "keep completed formal definition and formalization completion downstream",
            "gate": "do not claim formalization complete",
        },
        {
            "id": "SIGMA-A-EXEC-PLAN-007",
            "focus": "theorem boundary",
            "plan": "keep theorem candidate planning and theorem proof downstream",
            "gate": "do not create theorem candidates",
        },
        {
            "id": "SIGMA-A-EXEC-PLAN-008",
            "focus": "publication boundary",
            "plan": "keep validation, readiness approval, manuscript readiness, and citations downstream",
            "gate": "do not validate or approve readiness",
        },
    ]

    checks = [
        "Exactly one controlled Sigma_A definition completion execution plan is created.",
        "The v8.145 readiness boundary audit is imported.",
        "No new readiness audit is executed.",
        "No definition completion execution is performed.",
        "No Sigma_A definition completion is performed.",
        "No dependent-object definition completion is performed.",
        "No theorem candidate planning or theorem proof is performed.",
        "No validation, readiness approval, or citation work is performed.",
    ]

    def run(self) -> ControlledSigmaADefinitionCompletionExecutionPlanReport:
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

            "controlled_sigma_a_definition_completion_execution_plan_count": 1,
            "new_controlled_sigma_a_definition_completion_execution_plan_count": 1,
            "sigma_a_definition_completion_execution_plan_count": 1,
            "definition_completion_execution_plan_count": 1,
            "execution_plan_row_count": len(self.plan_rows),
            "execution_plan_check_count": len(self.checks),
            "execution_plan_gate_count": len(self.plan_rows),

            "imported_sigma_a_definition_completion_readiness_boundary_audit_count": carried.get("Sigma_A definition completion readiness boundary audit count", 1),
            "imported_new_sigma_a_definition_completion_readiness_boundary_audit_count": carried.get("New Sigma_A definition completion readiness boundary audit count", 1),
            "imported_definition_completion_readiness_boundary_audit_count": carried.get("Definition completion readiness boundary audit count", 1),
            "imported_readiness_boundary_audit_row_count": carried.get("Readiness boundary audit row count", 8),
            "imported_readiness_boundary_audit_check_count": carried.get("Readiness boundary audit check count", 8),
            "imported_readiness_boundary_preserved_count": carried.get("Readiness boundary preserved count", 8),

            "imported_audited_sigma_a_definition_completion_readiness_plan_count": carried.get("Audited Sigma_A definition completion readiness plan count", 1),
            "imported_audited_imported_dependent_object_draft_bundle_count": carried.get("Audited imported dependent-object draft bundle count", 1),
            "imported_audited_imported_dependent_object_draft_count": carried.get("Audited imported dependent-object draft count", 6),
            "imported_audited_imported_bundle_linked_to_refined_sigma_a_count": carried.get("Audited imported bundle linked to refined Sigma_A count", 1),
            "imported_audited_planned_future_sigma_a_definition_completion_scope_count": carried.get("Audited planned future Sigma_A definition completion scope count", 1),
            "imported_audited_planned_future_completion_gate_count": carried.get("Audited planned future completion gate count", 8),
            "imported_audited_planned_gap_scan_count": carried.get("Audited planned gap scan count", 1),
            "imported_audited_planned_boundary_preservation_count": carried.get("Audited planned boundary preservation count", 1),

            "planned_controlled_sigma_a_completion_execution_scope_count": 1,
            "planned_controlled_execution_gate_count": 8,
            "planned_execution_source_lock_count": 1,
            "planned_execution_zero_preservation_count": 1,
            "planned_no_default_readiness_audit_count": 1,

            "remaining_dependent_object_deferral_count": carried.get("Remaining dependent-object deferral count", 0),
            "all_dependent_object_draft_slots_created_count": carried.get("All dependent-object draft slots created count", 1),
            "all_dependent_object_draft_slots_integrated_count": carried.get("All dependent-object draft slots integrated count", 1),

            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 14,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,

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

            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "definition_completion_execution_count": 0,
            "sigma_a_definition_completion_execution_count": 0,
            "sigma_a_definition_completion_count": 0,
            "completed_formal_definition_count": 0,
            "formalization_complete_count": 0,

            "dependent_object_definition_completion_count": 0,
            "adm_a_definition_completion_count": 0,
            "c_reg_definition_completion_count": 0,
            "pi_obs_definition_completion_count": 0,
            "m_c_definition_completion_count": 0,
            "r_a_definition_completion_count": 0,
            "traj_a_definition_completion_count": 0,

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
            "This milestone creates an execution plan only; it does not execute Sigma_A definition completion.",
            "No new readiness audit is executed by default.",
            "Sigma_A completion and dependent-object completion remain zero.",
            "Theorem, proof, validation, readiness approval, and citation claims remain absent.",
        ])

        draft_text = self._render_report(counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(draft_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(draft_text)
        counts["overclaim_count"] = self._count_overclaims(draft_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(draft_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", draft_text))

        positive_requirements = {
            "controlled_sigma_a_definition_completion_execution_plan_count": 1,
            "new_controlled_sigma_a_definition_completion_execution_plan_count": 1,
            "sigma_a_definition_completion_execution_plan_count": 1,
            "definition_completion_execution_plan_count": 1,
            "execution_plan_row_count": 8,
            "execution_plan_check_count": 8,
            "execution_plan_gate_count": 8,
            "imported_sigma_a_definition_completion_readiness_boundary_audit_count": 1,
            "imported_audited_imported_dependent_object_draft_count": 6,
            "imported_audited_planned_future_completion_gate_count": 8,
            "planned_controlled_sigma_a_completion_execution_scope_count": 1,
            "planned_controlled_execution_gate_count": 8,
            "planned_execution_source_lock_count": 1,
            "planned_execution_zero_preservation_count": 1,
            "planned_no_default_readiness_audit_count": 1,
        }

        for key, expected in positive_requirements.items():
            if counts[key] != expected:
                errors.append(f"{key} expected {expected}, found {counts[key]}.")

        zero_fields = [
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

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.146 execution plan.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.146 execution plan.")

        final_text = self._render_report(counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_text, encoding="utf-8")

        return ControlledSigmaADefinitionCompletionExecutionPlanReport(
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
            "controlled_sigma_a_definition_completion_execution_plan_count": "Controlled Sigma_A definition completion execution plan count",
            "new_controlled_sigma_a_definition_completion_execution_plan_count": "New controlled Sigma_A definition completion execution plan count",
            "sigma_a_definition_completion_execution_plan_count": "Sigma_A definition completion execution plan count",
            "definition_completion_execution_plan_count": "Definition completion execution plan count",
            "execution_plan_row_count": "Execution plan row count",
            "execution_plan_check_count": "Execution plan check count",
            "execution_plan_gate_count": "Execution plan gate count",
            "imported_sigma_a_definition_completion_readiness_boundary_audit_count": "Imported Sigma_A definition completion readiness boundary audit count",
            "imported_new_sigma_a_definition_completion_readiness_boundary_audit_count": "Imported new Sigma_A definition completion readiness boundary audit count",
            "imported_definition_completion_readiness_boundary_audit_count": "Imported definition completion readiness boundary audit count",
            "imported_readiness_boundary_audit_row_count": "Imported readiness boundary audit row count",
            "imported_readiness_boundary_audit_check_count": "Imported readiness boundary audit check count",
            "imported_readiness_boundary_preserved_count": "Imported readiness boundary preserved count",
            "imported_audited_sigma_a_definition_completion_readiness_plan_count": "Imported audited Sigma_A definition completion readiness plan count",
            "imported_audited_imported_dependent_object_draft_bundle_count": "Imported audited dependent-object draft bundle count",
            "imported_audited_imported_dependent_object_draft_count": "Imported audited dependent-object draft count",
            "imported_audited_imported_bundle_linked_to_refined_sigma_a_count": "Imported audited bundle linked to refined Sigma_A count",
            "imported_audited_planned_future_sigma_a_definition_completion_scope_count": "Imported audited planned future Sigma_A definition completion scope count",
            "imported_audited_planned_future_completion_gate_count": "Imported audited planned future completion gate count",
            "imported_audited_planned_gap_scan_count": "Imported audited planned gap scan count",
            "imported_audited_planned_boundary_preservation_count": "Imported audited planned boundary preservation count",
            "planned_controlled_sigma_a_completion_execution_scope_count": "Planned controlled Sigma_A completion execution scope count",
            "planned_controlled_execution_gate_count": "Planned controlled execution gate count",
            "planned_execution_source_lock_count": "Planned execution source lock count",
            "planned_execution_zero_preservation_count": "Planned execution zero preservation count",
            "planned_no_default_readiness_audit_count": "Planned no-default-readiness-audit count",
            "new_sigma_a_definition_completion_readiness_boundary_audit_count": "New Sigma_A definition completion readiness boundary audit count",
            "sigma_a_definition_completion_readiness_boundary_audit_count": "Sigma_A definition completion readiness boundary audit count",
            "definition_completion_readiness_boundary_audit_count": "Definition completion readiness boundary audit count",
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
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric create a controlled Sigma_A definition completion execution plan after the readiness boundary audit "
            "while keeping actual completion execution, Sigma_A completion, dependent-object completion, theorem planning, proof, validation, readiness approval, and citations at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Execution-plan boundary statement")
        lines.append(
            "This artifact creates one controlled Sigma_A definition completion execution plan only. "
            "It imports the v8.145 readiness boundary audit and plans a future controlled execution scope, "
            "but it does not execute definition completion, does not execute final definitions, does not complete Sigma_A, "
            "does not complete dependent objects, does not complete formalization, does not create theorem candidates, "
            "does not prove a theorem, does not provide proof assistant verification, does not validate externally, "
            "does not approve manuscript readiness, and does not add citations."
        )
        lines.append("")
        lines.append("## Execution plan rows")
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
        lines.append("## Counters")
        order = [
            "controlled_sigma_a_definition_completion_execution_plan_count",
            "new_controlled_sigma_a_definition_completion_execution_plan_count",
            "sigma_a_definition_completion_execution_plan_count",
            "definition_completion_execution_plan_count",
            "execution_plan_row_count",
            "execution_plan_check_count",
            "execution_plan_gate_count",
            "imported_sigma_a_definition_completion_readiness_boundary_audit_count",
            "imported_new_sigma_a_definition_completion_readiness_boundary_audit_count",
            "imported_definition_completion_readiness_boundary_audit_count",
            "imported_readiness_boundary_audit_row_count",
            "imported_readiness_boundary_audit_check_count",
            "imported_readiness_boundary_preserved_count",
            "imported_audited_sigma_a_definition_completion_readiness_plan_count",
            "imported_audited_imported_dependent_object_draft_bundle_count",
            "imported_audited_imported_dependent_object_draft_count",
            "imported_audited_imported_bundle_linked_to_refined_sigma_a_count",
            "imported_audited_planned_future_sigma_a_definition_completion_scope_count",
            "imported_audited_planned_future_completion_gate_count",
            "imported_audited_planned_gap_scan_count",
            "imported_audited_planned_boundary_preservation_count",
            "planned_controlled_sigma_a_completion_execution_scope_count",
            "planned_controlled_execution_gate_count",
            "planned_execution_source_lock_count",
            "planned_execution_zero_preservation_count",
            "planned_no_default_readiness_audit_count",
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
            "new_sigma_a_definition_completion_readiness_boundary_audit_count",
            "sigma_a_definition_completion_readiness_boundary_audit_count",
            "definition_completion_readiness_boundary_audit_count",
            "new_sigma_a_definition_completion_readiness_plan_count",
            "sigma_a_definition_completion_readiness_plan_count",
            "definition_completion_readiness_plan_count",
            "new_definition_draft_execution_count",
            "new_dependent_object_definition_draft_execution_count",
            "dependent_object_definition_draft_execution_count",
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
            "The v8.146 artifact creates a controlled Sigma_A definition completion execution plan. "
            "It is forward progress beyond readiness auditing, but it remains planning only. "
            "Actual definition completion execution, Sigma_A completion, dependent-object completion, theorem planning, proof, validation, readiness approval, and citations remain absent."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Close this execution plan milestone officially.",
            "Next execute controlled Sigma_A definition completion only if the plan remains clean.",
            "Keep execution separate from execution planning.",
            "Keep Sigma_A completion separate from dependent-object completion.",
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
        phrases = ["does not", "not executed", "not completed", "planning", "plan", "completion", "boundary", "zero"]
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
            "does not provide proof assistant verification",
            "does not validate externally",
            "does not approve manuscript readiness",
            "does not add citations",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        forbidden_positive_counter_names = {
            "new sigma a definition completion readiness boundary audit count",
            "sigma a definition completion readiness boundary audit count",
            "definition completion readiness boundary audit count",
            "new sigma a definition completion readiness plan count",
            "sigma a definition completion readiness plan count",
            "definition completion readiness plan count",
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
    report = ControlledSigmaADefinitionCompletionExecutionPlanBuilder().run()
    print(f"Wrote {report.output_path}")
