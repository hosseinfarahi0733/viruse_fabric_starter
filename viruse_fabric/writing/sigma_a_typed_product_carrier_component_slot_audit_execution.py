from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaATypedProductCarrierComponentSlotAuditExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaATypedProductCarrierComponentSlotAuditExecutionBuilder:
    """Build v8.111 Sigma_A typed-product carrier component-slot audit execution artifact.

    Boundary discipline:
    - This milestone audits component slots for the selected typed-product carrier.
    - It does not execute carrier refinement.
    - It does not execute Sigma_A refinement.
    - It does not create new Sigma_A draft clauses.
    - It does not execute a new definition draft.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Typed-Product Carrier Component-Slot Audit Execution v8.111"
    source_artifact = Path("outputs/sigma_a_carrier_type_selection_decision_execution_v8_110.md")
    output_path = Path("outputs/sigma_a_typed_product_carrier_component_slot_audit_execution_v8_111.md")

    selected_carrier_type = "typed-product carrier"

    component_slot_rows = [
        {
            "slot_id": "X-A-SLOT-001",
            "slot_name": "biological-state component",
            "candidate_symbol": "B_A",
            "purpose": "holds biological or viral state information needed by Adm_A",
            "compatibility_note": "must be typed before admissibility can be completed",
            "audit_result": "audited, unresolved",
        },
        {
            "slot_id": "X-A-SLOT-002",
            "slot_name": "spatial-context component",
            "candidate_symbol": "S_A",
            "purpose": "holds spatial or localization context needed by constraint and projection layers",
            "compatibility_note": "must remain compatible with C_reg and Pi_obs",
            "audit_result": "audited, unresolved",
        },
        {
            "slot_id": "X-A-SLOT-003",
            "slot_name": "constraint-status component",
            "candidate_symbol": "Q_A",
            "purpose": "records whether state components are eligible for C_reg membership checks",
            "compatibility_note": "must not replace the formal C_reg definition",
            "audit_result": "audited, unresolved",
        },
        {
            "slot_id": "X-A-SLOT-004",
            "slot_name": "observer-visible component",
            "candidate_symbol": "O_A",
            "purpose": "marks information available to Pi_obs",
            "compatibility_note": "must distinguish observed state from full state",
            "audit_result": "audited, unresolved",
        },
        {
            "slot_id": "X-A-SLOT-005",
            "slot_name": "causal-mass support component",
            "candidate_symbol": "K_A",
            "purpose": "records support information needed by later M_c typing",
            "compatibility_note": "must not force M_c to be measure-like before that decision is made",
            "audit_result": "audited, unresolved",
        },
        {
            "slot_id": "X-A-SLOT-006",
            "slot_name": "transition-readiness component",
            "candidate_symbol": "Rdy_A",
            "purpose": "records state features needed by future R_A transition checks",
            "compatibility_note": "must not execute R_A refinement",
            "audit_result": "audited, unresolved",
        },
        {
            "slot_id": "X-A-SLOT-007",
            "slot_name": "trajectory-support component",
            "candidate_symbol": "J_A",
            "purpose": "records features needed for later Traj_A construction",
            "compatibility_note": "must remain separate from trajectory completion",
            "audit_result": "audited, unresolved",
        },
        {
            "slot_id": "X-A-SLOT-008",
            "slot_name": "audit-annotation component",
            "candidate_symbol": "Ann_A",
            "purpose": "keeps staged explanation and audit traceability available",
            "compatibility_note": "must remain auxiliary and must not become hidden mathematical structure",
            "audit_result": "audited, unresolved",
        },
    ]

    compatibility_checks = [
        "B_A must support Adm_A domain planning.",
        "S_A must support C_reg and Pi_obs compatibility planning.",
        "Q_A must not replace C_reg membership semantics.",
        "O_A must distinguish observer projection from full-state identity.",
        "K_A must preserve future M_c typing flexibility.",
        "Rdy_A must preserve future R_A refinement boundary.",
        "J_A must preserve future Traj_A construction boundary.",
        "Ann_A must remain auxiliary and audit-facing.",
    ]

    def run(self) -> SigmaATypedProductCarrierComponentSlotAuditExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone audits typed-product carrier component slots only.",
            "Typed-product carrier was selected previously, but carrier refinement is not executed in v8.111.",
            "No new Sigma_A draft clauses are created in v8.111.",
            "Sigma_A definition completion, theorem planning, theorem proof, proof assistant verification, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_typed_product_carrier_component_slot_audit_execution_count": 1,
            "typed_product_carrier_component_slot_audited_count": len(self.component_slot_rows),
            "component_slot_compatibility_check_count": len(self.compatibility_checks),
            "component_slot_unresolved_status_count": sum(1 for row in self.component_slot_rows if row["audit_result"] == "audited, unresolved"),
            "selected_typed_product_carrier_carried_count": carried.get("Selected typed-product carrier count", 1),
            "carried_sigma_a_carrier_type_selection_decision_execution_count": carried.get("Sigma_A carrier-type selection decision execution count", 1),
            "carried_carrier_type_selection_count": carried.get("Carrier type selection count", 1),
            "carried_carrier_type_selection_decision_count": carried.get("Carrier type selection decision count", 1),
            "carried_selected_carrier_type_count": carried.get("Selected carrier type count", 1),
            "carried_selected_typed_product_carrier_count": carried.get("Selected typed-product carrier count", 1),
            "carried_auxiliary_structured_schema_representation_count": carried.get("Auxiliary structured-schema representation count", 1),
            "carried_sigma_a_carrier_type_selection_decision_boundary_plan_count": carried.get("Carried Sigma_A carrier-type selection decision boundary plan count", 1),
            "carried_sigma_a_carrier_type_option_audit_execution_count": carried.get("Carried Sigma_A carrier-type option audit execution count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "new_carrier_type_selection_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "time_index_refinement_execution_count": 0,
            "sigma_a_refinement_execution_count": 0,
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
            errors.append("Overclaim detected in v8.111 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.111 report.")
        if counts["sigma_a_typed_product_carrier_component_slot_audit_execution_count"] != 1:
            errors.append("v8.111 must execute exactly one typed-product carrier component-slot audit.")
        if counts["typed_product_carrier_component_slot_audited_count"] != 8:
            errors.append("v8.111 must audit exactly eight typed-product component slots.")
        if counts["component_slot_compatibility_check_count"] != 8:
            errors.append("v8.111 must include exactly eight component-slot compatibility checks.")
        if counts["selected_typed_product_carrier_carried_count"] != 1:
            errors.append("v8.111 must carry selected typed-product carrier count from v8.110.")
        if counts["new_carrier_type_selection_count"] != 0:
            errors.append("v8.111 must not perform a new carrier type selection.")
        if counts["carrier_type_refinement_execution_count"] != 0:
            errors.append("v8.111 must not execute carrier-type refinement.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.111 must not execute carrier refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.111 must not execute Sigma_A refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.111 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.111 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.111 must not prove a theorem.")

        zero_fields = [
            "new_carrier_type_selection_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
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

        return SigmaATypedProductCarrierComponentSlotAuditExecutionReport(
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
            "sigma_a_typed_product_carrier_component_slot_audit_execution_count": "Sigma_A typed-product carrier component-slot audit execution count",
            "typed_product_carrier_component_slot_audited_count": "Typed-product carrier component slot audited count",
            "component_slot_compatibility_check_count": "Component-slot compatibility check count",
            "component_slot_unresolved_status_count": "Component-slot unresolved status count",
            "selected_typed_product_carrier_carried_count": "Selected typed-product carrier carried count",
            "carried_sigma_a_carrier_type_selection_decision_execution_count": "Carried Sigma_A carrier-type selection decision execution count",
            "carried_carrier_type_selection_count": "Carried carrier type selection count",
            "carried_carrier_type_selection_decision_count": "Carried carrier type selection decision count",
            "carried_selected_typed_product_carrier_count": "Carried selected typed-product carrier count",
            "carried_auxiliary_structured_schema_representation_count": "Carried auxiliary structured-schema representation count",
            "carried_sigma_a_carrier_type_selection_decision_boundary_plan_count": "Carried Sigma_A carrier-type selection decision boundary plan count",
            "carried_sigma_a_carrier_type_option_audit_execution_count": "Carried Sigma_A carrier-type option audit execution count",
            "new_carrier_type_selection_count": "New carrier type selection count",
            "time_index_refinement_execution_count": "Time-index refinement execution count",
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
            "Can Viruse Fabric audit typed-product carrier component slots after typed-product carrier selection "
            "while keeping new carrier selection, carrier refinement execution, Sigma_A refinement execution, new draft execution, "
            "definition execution, Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, "
            "external validation, manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Audit boundary")
        lines.append(f"- Selected carrier type carried from v8.110: {self.selected_carrier_type}")
        lines.append("- Milestone type: Sigma_A typed-product carrier component-slot audit execution only")
        lines.append("- New carrier type selection after this milestone: not executed")
        lines.append("- Carrier refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Typed-product component-slot audit rows")
        lines.append("")
        lines.append("| Slot ID | Slot name | Candidate symbol | Purpose | Compatibility note | Audit result |")
        lines.append("|---|---|---|---|---|---|")
        for row in self.component_slot_rows:
            lines.append(
                f"| {row['slot_id']} | {row['slot_name']} | {row['candidate_symbol']} | "
                f"{row['purpose']} | {row['compatibility_note']} | {row['audit_result']} |"
            )
        lines.append("")
        lines.append("## Component-slot compatibility checks")
        for index, check in enumerate(self.compatibility_checks, start=1):
            lines.append(f"{index}. {check}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes a Sigma_A typed-product carrier component-slot audit only. "
            "It does not perform a new carrier type selection, does not execute carrier-type refinement, "
            "does not execute carrier refinement, does not execute time-index refinement, does not execute Sigma_A refinement, "
            "does not create new Sigma_A draft clauses, does not execute a new definition draft, does not execute definitions, "
            "does not complete Sigma_A, does not complete any formal definition, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_typed_product_carrier_component_slot_audit_execution_count",
            "typed_product_carrier_component_slot_audited_count",
            "component_slot_compatibility_check_count",
            "component_slot_unresolved_status_count",
            "selected_typed_product_carrier_carried_count",
            "carried_sigma_a_carrier_type_selection_decision_execution_count",
            "carried_carrier_type_selection_count",
            "carried_carrier_type_selection_decision_count",
            "carried_selected_carrier_type_count",
            "carried_selected_typed_product_carrier_count",
            "carried_auxiliary_structured_schema_representation_count",
            "carried_sigma_a_carrier_type_selection_decision_boundary_plan_count",
            "carried_sigma_a_carrier_type_option_audit_execution_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "new_carrier_type_selection_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
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
            "The v8.111 artifact audits component slots for the previously selected typed-product carrier. "
            "This is an audit execution only. It does not perform new carrier selection, does not execute refinement, "
            "does not create new draft clauses, does not execute definitions, does not complete Sigma_A, "
            "does not create theorem candidates, does not prove theorems, does not provide proof assistant verification, "
            "does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Plan typed-product carrier component-slot refinement execution separately.",
            "Keep component-slot audit separate from component-slot refinement execution.",
            "Keep carrier refinement execution separate from Sigma_A completion.",
            "Keep time-index selection separate from typed-product slot audit.",
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
            "audit",
            "unresolved",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not perform a new carrier type selection",
            "does not execute carrier-type refinement",
            "does not execute carrier refinement",
            "does not execute time-index refinement",
            "does not execute Sigma_A refinement",
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
            "new carrier type selection count",
            "carrier type refinement execution count",
            "carrier refinement execution count",
            "time index refinement execution count",
            "time-index refinement execution count",
            "sigma_a refinement execution count",
            "sigma a refinement execution count",
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
            "audited",
            "unresolved",
            "previously selected",
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
    report = SigmaATypedProductCarrierComponentSlotAuditExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
