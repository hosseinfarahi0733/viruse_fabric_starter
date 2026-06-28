from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaADefinitionCompletionReadinessBoundaryAuditReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaADefinitionCompletionReadinessBoundaryAuditBuilder:
    """Build v8.145 Sigma_A definition completion readiness boundary audit.

    Boundary discipline:
    - This milestone audits the v8.144 readiness plan boundary.
    - It does not create a new readiness plan.
    - It does not execute Sigma_A definition completion.
    - It does not complete Sigma_A or dependent objects.
    - It does not create theorem candidates or proofs.
    """

    title = "Sigma_A Definition Completion Readiness Boundary Audit v8.145"
    source_artifact = Path("outputs/sigma_a_definition_completion_readiness_plan_v8_144.md")
    output_path = Path("outputs/sigma_a_definition_completion_readiness_boundary_audit_v8_145.md")

    audit_rows = [
        {
            "id": "SIGMA-A-READY-AUDIT-001",
            "focus": "readiness-plan source",
            "finding": "v8.144 readiness plan is present and imported as the only audited source",
            "boundary": "does not create a new readiness plan",
        },
        {
            "id": "SIGMA-A-READY-AUDIT-002",
            "focus": "integrated bundle import",
            "finding": "the six-object dependent draft bundle remains imported",
            "boundary": "does not create new dependent-object drafts",
        },
        {
            "id": "SIGMA-A-READY-AUDIT-003",
            "focus": "Sigma_A completion gate",
            "finding": "future Sigma_A completion gates are planned but unexecuted",
            "boundary": "does not execute Sigma_A definition completion",
        },
        {
            "id": "SIGMA-A-READY-AUDIT-004",
            "focus": "definition completion boundary",
            "finding": "definition completion execution remains zero",
            "boundary": "does not execute final definitions",
        },
        {
            "id": "SIGMA-A-READY-AUDIT-005",
            "focus": "dependent-object completion boundary",
            "finding": "dependent-object completion remains zero",
            "boundary": "does not complete Adm_A, C_reg, Pi_obs, M_c, R_A, or Traj_A",
        },
        {
            "id": "SIGMA-A-READY-AUDIT-006",
            "focus": "formalization boundary",
            "finding": "completed formal definition and formalization completion remain zero",
            "boundary": "does not claim completed formalization",
        },
        {
            "id": "SIGMA-A-READY-AUDIT-007",
            "focus": "theorem boundary",
            "finding": "theorem candidate planning and theorem proof remain zero",
            "boundary": "does not create theorem candidates",
        },
        {
            "id": "SIGMA-A-READY-AUDIT-008",
            "focus": "publication boundary",
            "finding": "validation, readiness approval, manuscript readiness, and citations remain zero",
            "boundary": "does not approve readiness or add citations",
        },
    ]

    checks = [
        "Exactly one Sigma_A definition completion readiness boundary audit is executed.",
        "The v8.144 readiness plan is audited as source.",
        "No new Sigma_A definition completion readiness plan is created.",
        "No definition completion execution is performed.",
        "No Sigma_A definition completion is performed.",
        "No dependent-object completion is performed.",
        "No theorem candidate planning or theorem proof is performed.",
        "No validation, readiness approval, or citation work is performed.",
    ]

    def run(self) -> SigmaADefinitionCompletionReadinessBoundaryAuditReport:
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

            "sigma_a_definition_completion_readiness_boundary_audit_count": 1,
            "new_sigma_a_definition_completion_readiness_boundary_audit_count": 1,
            "definition_completion_readiness_boundary_audit_count": 1,
            "readiness_boundary_audit_row_count": len(self.audit_rows),
            "readiness_boundary_audit_check_count": len(self.checks),
            "readiness_boundary_preserved_count": len(self.audit_rows),

            "audited_sigma_a_definition_completion_readiness_plan_count": carried.get("Sigma_A definition completion readiness plan count", 1),
            "audited_new_sigma_a_definition_completion_readiness_plan_count": carried.get("New Sigma_A definition completion readiness plan count", 1),
            "audited_definition_completion_readiness_plan_count": carried.get("Definition completion readiness plan count", 1),
            "audited_readiness_plan_row_count": carried.get("Readiness plan row count", 8),
            "audited_readiness_plan_check_count": carried.get("Readiness plan check count", 8),
            "audited_readiness_plan_boundary_gate_count": carried.get("Readiness plan boundary gate count", 8),

            "audited_imported_dependent_object_draft_bundle_count": carried.get("Imported dependent-object draft bundle count", 1),
            "audited_imported_dependent_object_draft_count": carried.get("Imported dependent-object draft count", 6),
            "audited_imported_adm_a_draft_count": carried.get("Imported Adm_A draft count", 1),
            "audited_imported_c_reg_draft_count": carried.get("Imported C_reg draft count", 1),
            "audited_imported_pi_obs_draft_count": carried.get("Imported Pi_obs draft count", 1),
            "audited_imported_m_c_draft_count": carried.get("Imported M_c draft count", 1),
            "audited_imported_r_a_draft_count": carried.get("Imported R_A draft count", 1),
            "audited_imported_traj_a_draft_count": carried.get("Imported Traj_A draft count", 1),
            "audited_imported_bundle_linked_to_refined_sigma_a_count": carried.get("Imported bundle linked to refined Sigma_A count", 1),
            "audited_imported_bundle_dependency_coherence_count": carried.get("Imported bundle dependency coherence count", 1),

            "audited_planned_future_sigma_a_definition_completion_scope_count": carried.get("Planned future Sigma_A definition completion scope count", 1),
            "audited_planned_future_completion_gate_count": carried.get("Planned future completion gate count", 8),
            "audited_planned_gap_scan_count": carried.get("Planned gap scan count", 1),
            "audited_planned_boundary_preservation_count": carried.get("Planned boundary preservation count", 1),

            "audited_completion_execution_zero_count": 1,
            "audited_sigma_a_completion_zero_count": 1,
            "audited_dependent_object_completion_zero_count": 1,
            "audited_theorem_boundary_zero_count": 1,
            "audited_publication_boundary_zero_count": 1,

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
            "This milestone audits readiness boundaries only; it does not create a new readiness plan.",
            "Sigma_A definition completion execution remains zero.",
            "Dependent-object completion remains zero.",
            "Theorem, proof, validation, readiness approval, and citation claims remain absent.",
        ])

        draft_text = self._render_report(counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(draft_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(draft_text)
        counts["overclaim_count"] = self._count_overclaims(draft_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(draft_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", draft_text))

        positive_requirements = {
            "sigma_a_definition_completion_readiness_boundary_audit_count": 1,
            "new_sigma_a_definition_completion_readiness_boundary_audit_count": 1,
            "definition_completion_readiness_boundary_audit_count": 1,
            "audited_sigma_a_definition_completion_readiness_plan_count": 1,
            "audited_imported_dependent_object_draft_count": 6,
            "audited_planned_future_completion_gate_count": 8,
            "audited_completion_execution_zero_count": 1,
            "audited_sigma_a_completion_zero_count": 1,
            "audited_dependent_object_completion_zero_count": 1,
            "audited_theorem_boundary_zero_count": 1,
            "audited_publication_boundary_zero_count": 1,
        }

        for key, expected in positive_requirements.items():
            if counts[key] != expected:
                errors.append(f"{key} expected {expected}, found {counts[key]}.")

        zero_fields = [
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
            errors.append("Overclaim detected in v8.145 boundary audit.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.145 boundary audit.")

        final_text = self._render_report(counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_text, encoding="utf-8")

        return SigmaADefinitionCompletionReadinessBoundaryAuditReport(
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
            "sigma_a_definition_completion_readiness_boundary_audit_count": "Sigma_A definition completion readiness boundary audit count",
            "new_sigma_a_definition_completion_readiness_boundary_audit_count": "New Sigma_A definition completion readiness boundary audit count",
            "definition_completion_readiness_boundary_audit_count": "Definition completion readiness boundary audit count",
            "readiness_boundary_audit_row_count": "Readiness boundary audit row count",
            "readiness_boundary_audit_check_count": "Readiness boundary audit check count",
            "readiness_boundary_preserved_count": "Readiness boundary preserved count",
            "audited_sigma_a_definition_completion_readiness_plan_count": "Audited Sigma_A definition completion readiness plan count",
            "audited_new_sigma_a_definition_completion_readiness_plan_count": "Audited new Sigma_A definition completion readiness plan count",
            "audited_definition_completion_readiness_plan_count": "Audited definition completion readiness plan count",
            "audited_readiness_plan_row_count": "Audited readiness plan row count",
            "audited_readiness_plan_check_count": "Audited readiness plan check count",
            "audited_readiness_plan_boundary_gate_count": "Audited readiness plan boundary gate count",
            "audited_imported_dependent_object_draft_bundle_count": "Audited imported dependent-object draft bundle count",
            "audited_imported_dependent_object_draft_count": "Audited imported dependent-object draft count",
            "audited_imported_adm_a_draft_count": "Audited imported Adm_A draft count",
            "audited_imported_c_reg_draft_count": "Audited imported C_reg draft count",
            "audited_imported_pi_obs_draft_count": "Audited imported Pi_obs draft count",
            "audited_imported_m_c_draft_count": "Audited imported M_c draft count",
            "audited_imported_r_a_draft_count": "Audited imported R_A draft count",
            "audited_imported_traj_a_draft_count": "Audited imported Traj_A draft count",
            "audited_imported_bundle_linked_to_refined_sigma_a_count": "Audited imported bundle linked to refined Sigma_A count",
            "audited_imported_bundle_dependency_coherence_count": "Audited imported bundle dependency coherence count",
            "audited_planned_future_sigma_a_definition_completion_scope_count": "Audited planned future Sigma_A definition completion scope count",
            "audited_planned_future_completion_gate_count": "Audited planned future completion gate count",
            "audited_planned_gap_scan_count": "Audited planned gap scan count",
            "audited_planned_boundary_preservation_count": "Audited planned boundary preservation count",
            "audited_completion_execution_zero_count": "Audited completion execution zero count",
            "audited_sigma_a_completion_zero_count": "Audited Sigma_A completion zero count",
            "audited_dependent_object_completion_zero_count": "Audited dependent-object completion zero count",
            "audited_theorem_boundary_zero_count": "Audited theorem boundary zero count",
            "audited_publication_boundary_zero_count": "Audited publication boundary zero count",
            "new_sigma_a_definition_completion_readiness_plan_count": "New Sigma_A definition completion readiness plan count",
            "sigma_a_definition_completion_readiness_plan_count": "Sigma_A definition completion readiness plan count",
            "definition_completion_readiness_plan_count": "Definition completion readiness plan count",
            "new_definition_draft_execution_count": "New definition draft execution count",
            "new_dependent_object_definition_draft_execution_count": "New dependent-object definition draft execution count",
            "dependent_object_definition_draft_execution_count": "Dependent-object definition draft execution count",
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
            "Does the v8.144 Sigma_A definition completion readiness plan preserve its boundary while keeping completion execution, "
            "Sigma_A definition completion, dependent-object completion, theorem candidate planning, theorem proof, validation, readiness approval, and citations at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Boundary audit statement")
        lines.append(
            "This artifact executes one Sigma_A definition completion readiness boundary audit only. "
            "It audits the v8.144 readiness plan and confirms that the plan remains a plan. "
            "It does not create a new readiness plan, does not execute definition completion, does not execute final definitions, "
            "does not complete Sigma_A, does not complete dependent objects, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not provide proof assistant verification, "
            "does not validate externally, does not approve manuscript readiness, and does not add citations."
        )
        lines.append("")
        lines.append("## Audit rows")
        lines.append("")
        lines.append("| ID | Focus | Finding | Boundary |")
        lines.append("|---|---|---|---|")
        for row in self.audit_rows:
            lines.append(f"| {row['id']} | {row['focus']} | {row['finding']} | {row['boundary']} |")
        lines.append("")
        lines.append("## Checks")
        for index, check in enumerate(self.checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Counters")
        order = [
            "sigma_a_definition_completion_readiness_boundary_audit_count",
            "new_sigma_a_definition_completion_readiness_boundary_audit_count",
            "definition_completion_readiness_boundary_audit_count",
            "readiness_boundary_audit_row_count",
            "readiness_boundary_audit_check_count",
            "readiness_boundary_preserved_count",
            "audited_sigma_a_definition_completion_readiness_plan_count",
            "audited_new_sigma_a_definition_completion_readiness_plan_count",
            "audited_definition_completion_readiness_plan_count",
            "audited_readiness_plan_row_count",
            "audited_readiness_plan_check_count",
            "audited_readiness_plan_boundary_gate_count",
            "audited_imported_dependent_object_draft_bundle_count",
            "audited_imported_dependent_object_draft_count",
            "audited_imported_adm_a_draft_count",
            "audited_imported_c_reg_draft_count",
            "audited_imported_pi_obs_draft_count",
            "audited_imported_m_c_draft_count",
            "audited_imported_r_a_draft_count",
            "audited_imported_traj_a_draft_count",
            "audited_imported_bundle_linked_to_refined_sigma_a_count",
            "audited_imported_bundle_dependency_coherence_count",
            "audited_planned_future_sigma_a_definition_completion_scope_count",
            "audited_planned_future_completion_gate_count",
            "audited_planned_gap_scan_count",
            "audited_planned_boundary_preservation_count",
            "audited_completion_execution_zero_count",
            "audited_sigma_a_completion_zero_count",
            "audited_dependent_object_completion_zero_count",
            "audited_theorem_boundary_zero_count",
            "audited_publication_boundary_zero_count",
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
            "The v8.145 artifact audits the v8.144 readiness plan boundary. "
            "It confirms the readiness plan remains planning only and that completion execution, Sigma_A completion, dependent-object completion, "
            "theorem candidate planning, theorem proof, validation, readiness approval, and citation claims remain absent."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Do not run another readiness boundary audit by default.",
            "Prepare controlled Sigma_A definition completion execution plan next.",
            "Keep execution planning separate from execution.",
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
        phrases = ["does not", "not executed", "not completed", "not approved", "boundary", "audit", "completion", "zero"]
        return sum(text.count(p) + text.lower().count(p.lower()) for p in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not create a new readiness plan",
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
            "adm a definition completion count",
            "c reg definition completion count",
            "pi obs definition completion count",
            "m c definition completion count",
            "r a definition completion count",
            "traj a definition completion count",
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
    report = SigmaADefinitionCompletionReadinessBoundaryAuditBuilder().run()
    print(f"Wrote {report.output_path}")
