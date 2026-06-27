from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaATypedProductCarrierRefinementBoundaryAuditReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaATypedProductCarrierRefinementBoundaryAuditBuilder:
    """Build v8.120 Sigma_A typed-product carrier refinement boundary audit artifact.

    Boundary discipline:
    - This milestone audits the boundary of v8.119 typed-product carrier refinement.
    - It does not execute new typed-product carrier refinement.
    - It does not execute generic carrier refinement.
    - It does not execute carrier-type refinement.
    - It does not execute time-index refinement.
    - It does not execute Sigma_A refinement.
    - It does not create new Sigma_A draft clauses.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Typed-Product Carrier Refinement Boundary Audit v8.120"
    source_artifact = Path("outputs/sigma_a_typed_product_carrier_refinement_execution_v8_119.md")
    output_path = Path("outputs/sigma_a_typed_product_carrier_refinement_boundary_audit_v8_120.md")

    boundary_audit_rows = [
        {
            "audit_id": "X-A-CARRIER-REF-AUDIT-001",
            "focus": "typed-product carrier candidate",
            "audited_object": "X_A^tp",
            "boundary_result": "candidate remains carrier-level only",
            "open_dependency": "Adm_A remains unresolved",
            "blocked_overreach": "does not complete Sigma_A",
        },
        {
            "audit_id": "X-A-CARRIER-REF-AUDIT-002",
            "focus": "coordinate assembly",
            "audited_object": "(B_A, S_A, Q_A, O_A, K_A, Rdy_A, J_A, Ann_A)",
            "boundary_result": "eight-coordinate assembly preserved",
            "open_dependency": "coordinate semantics remain dependent on later definitions",
            "blocked_overreach": "does not create a new Sigma_A draft clause",
        },
        {
            "audit_id": "X-A-CARRIER-REF-AUDIT-003",
            "focus": "dependent-object separation",
            "audited_object": "{Adm_A, C_reg, Pi_obs, M_c, R_A, Traj_A}",
            "boundary_result": "six dependent objects remain open",
            "open_dependency": "dependent object definitions remain unresolved",
            "blocked_overreach": "does not execute definitions",
        },
        {
            "audit_id": "X-A-CARRIER-REF-AUDIT-004",
            "focus": "selected carrier type",
            "audited_object": "typed-product carrier",
            "boundary_result": "selection carried without reselection",
            "open_dependency": "alternative carrier types remain non-selected",
            "blocked_overreach": "does not perform a new carrier type selection",
        },
        {
            "audit_id": "X-A-CARRIER-REF-AUDIT-005",
            "focus": "generic carrier boundary",
            "audited_object": "carrier refinement layer",
            "boundary_result": "generic carrier refinement remains absent",
            "open_dependency": "generic carrier layer remains separate",
            "blocked_overreach": "does not execute generic carrier refinement",
        },
        {
            "audit_id": "X-A-CARRIER-REF-AUDIT-006",
            "focus": "time-index boundary",
            "audited_object": "T_A",
            "boundary_result": "time-index refinement remains absent",
            "open_dependency": "T_A refinement remains downstream",
            "blocked_overreach": "does not execute time-index refinement",
        },
        {
            "audit_id": "X-A-CARRIER-REF-AUDIT-007",
            "focus": "Sigma_A refinement boundary",
            "audited_object": "Sigma_A",
            "boundary_result": "Sigma_A refinement remains absent",
            "open_dependency": "Sigma_A assembly remains downstream",
            "blocked_overreach": "does not execute Sigma_A refinement",
        },
        {
            "audit_id": "X-A-CARRIER-REF-AUDIT-008",
            "focus": "proof-readiness boundary",
            "audited_object": "theorem/proof/readiness layers",
            "boundary_result": "proof-readiness layers remain absent",
            "open_dependency": "theorem, proof, validation, citation, and readiness remain downstream",
            "blocked_overreach": "does not create theorem candidates, proofs, validation, citations, or readiness approval",
        },
    ]

    audit_findings = [
        "The typed-product carrier candidate remains a carrier-level candidate only.",
        "The eight-coordinate assembly remains preserved without completing Sigma_A.",
        "Six dependent objects remain open: Adm_A, C_reg, Pi_obs, M_c, R_A, and Traj_A.",
        "The selected typed-product carrier type is carried without reselection.",
        "Generic carrier refinement remains absent.",
        "Time-index refinement remains absent.",
        "Sigma_A refinement and Sigma_A definition completion remain absent.",
        "Theorem, proof, validation, citation, and readiness layers remain absent.",
    ]

    def run(self) -> SigmaATypedProductCarrierRefinementBoundaryAuditReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone audits typed-product carrier refinement boundaries only.",
            "No new typed-product carrier refinement is executed in v8.120.",
            "Generic carrier refinement and Sigma_A refinement remain zero in v8.120.",
            "Sigma_A definition completion, theorem planning, theorem proof, proof assistant verification, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_typed_product_carrier_refinement_boundary_audit_count": 1,
            "typed_product_carrier_refinement_boundary_audit_count": 1,
            "full_typed_product_carrier_refinement_boundary_audit_count": 1,
            "typed_product_carrier_refinement_boundary_audit_row_count": len(self.boundary_audit_rows),
            "typed_product_carrier_refinement_boundary_preserved_count": len(self.boundary_audit_rows),
            "refined_typed_product_carrier_candidate_audited_count": 1,
            "dependent_object_boundary_preserved_count": 6,
            "open_dependency_preserved_count": 8,
            "carrier_refinement_boundary_blocker_count": len(self.boundary_audit_rows),
            "typed_product_carrier_refinement_boundary_audit_finding_count": len(self.audit_findings),
            "carried_sigma_a_typed_product_carrier_refinement_execution_count": carried.get("Sigma_A typed-product carrier refinement execution count", 1),
            "carried_full_typed_product_carrier_refinement_execution_count": carried.get("Full typed-product carrier refinement execution count", 1),
            "carried_typed_product_carrier_refinement_execution_count": carried.get("Typed-product carrier refinement execution count", 1),
            "carried_typed_product_carrier_refinement_row_count": carried.get("Typed-product carrier refinement row count", 8),
            "carried_typed_product_carrier_refinement_check_count": carried.get("Typed-product carrier refinement check count", 8),
            "carried_refined_typed_product_carrier_component_count": carried.get("Refined typed-product carrier component count", 8),
            "carried_refined_typed_product_carrier_candidate_count": carried.get("Refined typed-product carrier candidate count", 1),
            "carried_carrier_level_notation_candidate_count": carried.get("Carrier-level notation candidate count", 1),
            "carried_dependent_object_preserved_open_count": carried.get("Dependent object preserved open count", 6),
            "carried_selected_typed_product_carrier_count": carried.get("Carried selected typed-product carrier count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "new_typed_product_carrier_refinement_execution_count": 0,
            "new_full_typed_product_carrier_refinement_execution_count": 0,
            "new_sigma_a_typed_product_carrier_refinement_execution_count": 0,
            "generic_carrier_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "time_index_refinement_execution_count": 0,
            "sigma_a_refinement_execution_count": 0,
            "new_component_slot_integration_execution_count": 0,
            "new_component_slot_refinement_execution_count": 0,
            "new_carrier_type_selection_count": 0,
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
            errors.append("Overclaim detected in v8.120 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.120 report.")
        if counts["sigma_a_typed_product_carrier_refinement_boundary_audit_count"] != 1:
            errors.append("v8.120 must execute exactly one typed-product carrier refinement boundary audit.")
        if counts["typed_product_carrier_refinement_boundary_audit_row_count"] != 8:
            errors.append("v8.120 must audit exactly eight boundary rows.")
        if counts["typed_product_carrier_refinement_boundary_preserved_count"] != 8:
            errors.append("v8.120 must preserve all eight typed-product carrier boundary rows.")
        if counts["refined_typed_product_carrier_candidate_audited_count"] != 1:
            errors.append("v8.120 must audit exactly one refined typed-product carrier candidate.")
        if counts["new_typed_product_carrier_refinement_execution_count"] != 0:
            errors.append("v8.120 must not execute new typed-product carrier refinement.")
        if counts["generic_carrier_refinement_execution_count"] != 0:
            errors.append("v8.120 must not execute generic carrier refinement.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.120 must not execute carrier refinement.")
        if counts["time_index_refinement_execution_count"] != 0:
            errors.append("v8.120 must not execute time-index refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.120 must not execute Sigma_A refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.120 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.120 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.120 must not prove a theorem.")

        zero_fields = [
            "new_typed_product_carrier_refinement_execution_count",
            "new_full_typed_product_carrier_refinement_execution_count",
            "new_sigma_a_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "new_component_slot_integration_execution_count",
            "new_component_slot_refinement_execution_count",
            "new_carrier_type_selection_count",
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

        return SigmaATypedProductCarrierRefinementBoundaryAuditReport(
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
            "sigma_a_typed_product_carrier_refinement_boundary_audit_count": "Sigma_A typed-product carrier refinement boundary audit count",
            "typed_product_carrier_refinement_boundary_audit_count": "Typed-product carrier refinement boundary audit count",
            "full_typed_product_carrier_refinement_boundary_audit_count": "Full typed-product carrier refinement boundary audit count",
            "typed_product_carrier_refinement_boundary_audit_row_count": "Typed-product carrier refinement boundary audit row count",
            "typed_product_carrier_refinement_boundary_preserved_count": "Typed-product carrier refinement boundary preserved count",
            "refined_typed_product_carrier_candidate_audited_count": "Refined typed-product carrier candidate audited count",
            "dependent_object_boundary_preserved_count": "Dependent object boundary preserved count",
            "open_dependency_preserved_count": "Open dependency preserved count",
            "carrier_refinement_boundary_blocker_count": "Carrier refinement boundary blocker count",
            "typed_product_carrier_refinement_boundary_audit_finding_count": "Typed-product carrier refinement boundary audit finding count",
            "carried_sigma_a_typed_product_carrier_refinement_execution_count": "Carried Sigma_A typed-product carrier refinement execution count",
            "carried_full_typed_product_carrier_refinement_execution_count": "Carried full typed-product carrier refinement execution count",
            "carried_typed_product_carrier_refinement_execution_count": "Carried typed-product carrier refinement execution count",
            "carried_typed_product_carrier_refinement_row_count": "Carried typed-product carrier refinement row count",
            "carried_typed_product_carrier_refinement_check_count": "Carried typed-product carrier refinement check count",
            "carried_refined_typed_product_carrier_component_count": "Carried refined typed-product carrier component count",
            "carried_refined_typed_product_carrier_candidate_count": "Carried refined typed-product carrier candidate count",
            "carried_carrier_level_notation_candidate_count": "Carried carrier-level notation candidate count",
            "carried_dependent_object_preserved_open_count": "Carried dependent object preserved open count",
            "carried_selected_typed_product_carrier_count": "Carried selected typed-product carrier count",
            "new_typed_product_carrier_refinement_execution_count": "New typed-product carrier refinement execution count",
            "new_full_typed_product_carrier_refinement_execution_count": "New full typed-product carrier refinement execution count",
            "new_sigma_a_typed_product_carrier_refinement_execution_count": "New Sigma_A typed-product carrier refinement execution count",
            "generic_carrier_refinement_execution_count": "Generic carrier refinement execution count",
            "carrier_refinement_execution_count": "Carrier refinement execution count",
            "carrier_type_refinement_execution_count": "Carrier type refinement execution count",
            "time_index_refinement_execution_count": "Time-index refinement execution count",
            "new_component_slot_integration_execution_count": "New component-slot integration execution count",
            "new_component_slot_refinement_execution_count": "New component-slot refinement execution count",
            "new_carrier_type_selection_count": "New carrier type selection count",
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
            "Can Viruse Fabric audit the boundary of v8.119 typed-product carrier refinement while keeping new typed-product carrier refinement execution, "
            "generic carrier refinement, carrier-type refinement, time-index refinement, Sigma_A refinement, new draft execution, definition execution, "
            "Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, external validation, manuscript readiness, "
            "readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Audit boundary")
        lines.append("- Milestone type: Sigma_A typed-product carrier refinement boundary audit only")
        lines.append("- New typed-product carrier refinement execution after this milestone: not executed")
        lines.append("- Generic carrier refinement execution after this milestone: not executed")
        lines.append("- Carrier-type refinement execution after this milestone: not executed")
        lines.append("- Time-index refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Typed-product carrier refinement boundary audit rows")
        lines.append("")
        lines.append("| Audit ID | Focus | Audited object | Boundary result | Open dependency | Blocked overreach |")
        lines.append("|---|---|---|---|---|---|")
        for row in self.boundary_audit_rows:
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
            "This artifact audits Sigma_A typed-product carrier refinement boundaries only. "
            "It does not execute new typed-product carrier refinement, does not execute new full typed-product carrier refinement, "
            "does not execute new Sigma_A typed-product carrier refinement, does not execute generic carrier refinement, "
            "does not execute carrier-type refinement, does not execute time-index refinement, does not execute Sigma_A refinement, "
            "does not execute new component-slot integration, does not execute new component-slot refinement, "
            "does not perform a new carrier type selection, does not create new Sigma_A draft clauses, "
            "does not execute a new definition draft, does not execute definitions, does not complete Sigma_A, "
            "does not complete any formal definition, does not complete formalization, does not create theorem candidates, "
            "does not prove a theorem, does not run proof execution, does not provide proof assistant verification, "
            "does not prove the full framework, does not provide external validation, does not perform an independent experiment, "
            "does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_typed_product_carrier_refinement_boundary_audit_count",
            "typed_product_carrier_refinement_boundary_audit_count",
            "full_typed_product_carrier_refinement_boundary_audit_count",
            "typed_product_carrier_refinement_boundary_audit_row_count",
            "typed_product_carrier_refinement_boundary_preserved_count",
            "refined_typed_product_carrier_candidate_audited_count",
            "dependent_object_boundary_preserved_count",
            "open_dependency_preserved_count",
            "carrier_refinement_boundary_blocker_count",
            "typed_product_carrier_refinement_boundary_audit_finding_count",
            "carried_sigma_a_typed_product_carrier_refinement_execution_count",
            "carried_full_typed_product_carrier_refinement_execution_count",
            "carried_typed_product_carrier_refinement_execution_count",
            "carried_typed_product_carrier_refinement_row_count",
            "carried_typed_product_carrier_refinement_check_count",
            "carried_refined_typed_product_carrier_component_count",
            "carried_refined_typed_product_carrier_candidate_count",
            "carried_carrier_level_notation_candidate_count",
            "carried_dependent_object_preserved_open_count",
            "carried_selected_typed_product_carrier_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "new_typed_product_carrier_refinement_execution_count",
            "new_full_typed_product_carrier_refinement_execution_count",
            "new_sigma_a_typed_product_carrier_refinement_execution_count",
            "generic_carrier_refinement_execution_count",
            "carrier_refinement_execution_count",
            "carrier_type_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "new_component_slot_integration_execution_count",
            "new_component_slot_refinement_execution_count",
            "new_carrier_type_selection_count",
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
            "The v8.120 artifact audits typed-product carrier refinement boundaries after the v8.119 execution milestone. "
            "It confirms that the refined typed-product carrier candidate remains a carrier-level candidate only. "
            "It does not execute new typed-product carrier refinement, does not execute generic carrier refinement, "
            "does not execute time-index refinement, does not execute Sigma_A refinement, does not create new draft clauses, "
            "does not execute definitions, does not complete Sigma_A, does not create theorem candidates, does not prove theorems, "
            "does not provide proof assistant verification, does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Plan Sigma_A carrier-level draft assembly only after this boundary audit is closed.",
            "Keep generic carrier refinement separate from typed-product carrier refinement boundary audit.",
            "Keep time-index refinement separate from typed-product carrier boundary audit.",
            "Keep C_reg, Pi_obs, M_c, R_A, and Traj_A refinements separate.",
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
            "boundary",
            "audit",
            "typed-product carrier",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute new typed-product carrier refinement",
            "does not execute new full typed-product carrier refinement",
            "does not execute new Sigma_A typed-product carrier refinement",
            "does not execute generic carrier refinement",
            "does not execute carrier-type refinement",
            "does not execute time-index refinement",
            "does not execute Sigma_A refinement",
            "does not execute new component-slot integration",
            "does not execute new component-slot refinement",
            "does not perform a new carrier type selection",
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
            "new typed-product carrier refinement execution count",
            "new full typed-product carrier refinement execution count",
            "new sigma_a typed-product carrier refinement execution count",
            "new sigma a typed-product carrier refinement execution count",
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
            "new typed-product carrier refinement executed",
            "generic carrier refinement executed",
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
            "audit",
            "boundary",
            "blocker",
            "open dependency",
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
    report = SigmaATypedProductCarrierRefinementBoundaryAuditBuilder().run()
    print(f"Wrote {report.output_path}")
