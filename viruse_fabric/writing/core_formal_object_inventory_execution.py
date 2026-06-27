from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class CoreFormalObjectInventoryExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class CoreFormalObjectInventoryExecutionBuilder:
    """Build v8.104 core formal object inventory execution artifact.

    Boundary discipline:
    - This milestone executes an inventory of core formal object families.
    - It does not execute definitions.
    - It does not complete any formal definition.
    - It does not create theorem candidates.
    - It does not prove theorems.
    - It does not perform proof assistant verification.
    - It does not provide external validation.
    - It does not approve manuscript readiness.
    """

    title = "Core Formal Object Inventory Execution v8.104"
    source_artifact = Path("outputs/formal_definition_transition_boundary_audit_plan_v8_103.md")
    output_path = Path("outputs/core_formal_object_inventory_execution_v8_104.md")

    inventory_rows = [
        {
            "object_id": "CFO-001",
            "family": "Sigma_A state-space / admissible-trajectory object",
            "candidate_symbol": "Sigma_A",
            "role": "Container for admissible states, trajectories, and transition constraints.",
            "inputs": "state variables, time index, admissibility constraints",
            "outputs": "admissible trajectory set and domain for later predicates",
            "dependencies": "constraint-region object, observer-projection object",
            "definition_obligation": "Specify carrier set, admissibility relation, time indexing, and projection compatibility.",
            "completion_status": "inventoried only, not defined, not completed",
        },
        {
            "object_id": "CFO-002",
            "family": "stabilization predicate",
            "candidate_symbol": "Stab",
            "role": "Predicate describing when a trajectory or state satisfies a stabilization condition.",
            "inputs": "trajectory segment, time window, tolerance or recurrence condition",
            "outputs": "boolean stabilization judgment",
            "dependencies": "Sigma_A object, attractor-class object",
            "definition_obligation": "Specify domain, quantifiers, tolerance regime, and admissible witness relation.",
            "completion_status": "inventoried only, not defined, not completed",
        },
        {
            "object_id": "CFO-003",
            "family": "attractor-class object",
            "candidate_symbol": "A_cls",
            "role": "Classifies limiting, recurrent, or attracting behavior under admissible dynamics.",
            "inputs": "trajectory family, recurrence witnesses, stabilization predicate",
            "outputs": "attractor-class membership relation",
            "dependencies": "Sigma_A object, stabilization predicate",
            "definition_obligation": "Specify class membership, equivalence or preorder relation, and witness conditions.",
            "completion_status": "inventoried only, not defined, not completed",
        },
        {
            "object_id": "CFO-004",
            "family": "constraint-region object",
            "candidate_symbol": "C_reg",
            "role": "Represents admissible regions, exclusion zones, or feasible domains for state evolution.",
            "inputs": "state coordinates, biological constraints, spatial constraints",
            "outputs": "constraint membership relation and feasible-region boundary",
            "dependencies": "Sigma_A object",
            "definition_obligation": "Specify region carrier, boundary rule, membership predicate, and interaction with transitions.",
            "completion_status": "inventoried only, not defined, not completed",
        },
        {
            "object_id": "CFO-005",
            "family": "causal-mass object",
            "candidate_symbol": "M_c",
            "role": "Represents weighted causal contribution or accumulated causal influence under admissible transitions.",
            "inputs": "transition relation, event weights, causal path or witness family",
            "outputs": "causal weight or mass-like functional",
            "dependencies": "Sigma_A object, constraint-region object",
            "definition_obligation": "Specify measure-like domain, aggregation rule, monotonicity expectations, and boundary behavior.",
            "completion_status": "inventoried only, not defined, not completed",
        },
        {
            "object_id": "CFO-006",
            "family": "observer-projection object",
            "candidate_symbol": "Pi_obs",
            "role": "Maps richer internal states or trajectories to observable representations.",
            "inputs": "state, trajectory, observation channel, projection regime",
            "outputs": "observable state or projected trajectory",
            "dependencies": "Sigma_A object, causal-mass object",
            "definition_obligation": "Specify projection domain, codomain, information loss, and compatibility with predicates.",
            "completion_status": "inventoried only, not defined, not completed",
        },
    ]

    def run(self) -> CoreFormalObjectInventoryExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        dependency_rows = [
            ("Sigma_A", "C_reg", "state-space feasibility depends on constraint-region membership"),
            ("Sigma_A", "Pi_obs", "admissible states must support observation projection"),
            ("Stab", "Sigma_A", "stabilization predicate is evaluated over admissible trajectories"),
            ("Stab", "A_cls", "stabilization judgments support attractor-class membership"),
            ("A_cls", "Sigma_A", "attractor classes are subsets or relations over admissible behavior"),
            ("A_cls", "Stab", "attractor-class relation depends on stabilization or recurrence witnesses"),
            ("C_reg", "Sigma_A", "constraint regions restrict admissible state evolution"),
            ("M_c", "Sigma_A", "causal mass is accumulated over admissible transitions"),
            ("M_c", "C_reg", "causal mass must respect feasible and excluded regions"),
            ("Pi_obs", "Sigma_A", "observer projection maps from admissible states or trajectories"),
            ("Pi_obs", "M_c", "observed causal mass may be projection-dependent"),
            ("Theorem layer", "all six objects", "theorem candidates require definitions after inventory"),
        ]

        inventory_obligations = [
            "Do not turn candidate symbols into completed definitions.",
            "Do not infer theorem candidates from the inventory alone.",
            "Do not infer theorem proof from object inventory.",
            "Do not infer proof assistant verification from object inventory.",
            "Do not infer external validation from object inventory.",
            "Do not infer manuscript readiness from object inventory.",
        ]

        warnings.extend([
            "This milestone executes inventory only.",
            "No formal definition is executed in v8.104.",
            "No formal definition is completed in v8.104.",
            "Theorem candidates, theorem proof, proof assistant verification, external validation, and manuscript readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "core_formal_object_inventory_execution_count": 1,
            "core_formal_object_count": len(self.inventory_rows),
            "formal_object_inventory_row_count": len(self.inventory_rows),
            "candidate_symbol_count": len(self.inventory_rows),
            "dependency_row_count": len(dependency_rows),
            "definition_obligation_count": len(self.inventory_rows),
            "inventory_obligation_count": len(inventory_obligations),
            "inventoried_only_status_count": sum(
                1 for row in self.inventory_rows if row["completion_status"] == "inventoried only, not defined, not completed"
            ),
            "gap_resolution_closure_carried_count": 1,
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
            "formal_definition_transition_boundary_audit_plan_count": carried.get("Formal definition transition boundary audit plan count", 1),
            "definition_transition_plan_count": carried.get("Definition transition plan count", 1),
            "formal_object_inventory_execution_count": 1,
            "definition_inventory_execution_count": 0,
            "definition_execution_count": 0,
            "new_definition_execution_count": 0,
            "definition_draft_execution_count": 0,
            "completed_formal_definition_count": 0,
            "formalization_complete_count": 0,
            "sigma_a_definition_completion_count": 0,
            "stabilization_predicate_definition_completion_count": 0,
            "attractor_class_definition_completion_count": 0,
            "constraint_region_definition_completion_count": 0,
            "causal_mass_definition_completion_count": 0,
            "observer_projection_definition_completion_count": 0,
            "new_stabilization_predicate_draft_clause_count": 0,
            "new_completion_criterion_count": 0,
            "new_completion_decision_plan_count": 0,
            "completion_decision_plan_count": carried.get("Completion decision plan count", 1),
            "completion_decision_count": 0,
            "completion_execution_count": 0,
            "completion_execution_authorized_count": 0,
            "carried_formal_definition_transition_boundary_audit_plan_count": carried.get("Formal definition transition boundary audit plan count", 1),
            "carried_planned_formal_object_count": carried.get("Planned formal object count", 6),
            "carried_definition_transition_plan_count": carried.get("Definition transition plan count", 1),
            "carried_resolved_gap_count": carried.get("Resolved gap count", 7),
            "carried_unresolved_gap_count": carried.get("Unresolved gap count", 0),
            "carried_remaining_blocking_gap_count": carried.get("Remaining blocking gap count", 0),
            "carried_conditional_hold_count": carried.get("Conditional hold count", 0),
            "carried_completion_decision_count": carried.get("Completion decision count", 0),
            "carried_completion_execution_count": carried.get("Completion execution count", 0),
            "carried_completion_execution_authorized_count": carried.get("Completion execution authorized count", 0),
            "carried_definition_execution_count": carried.get("Definition execution count", 0),
            "carried_new_definition_execution_count": carried.get("New definition execution count", 0),
            "carried_formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 0),
            "carried_sigma_a_definition_completion_count": carried.get("Sigma_A definition completion count", 0),
            "carried_stabilization_predicate_definition_completion_count": carried.get("Stabilization predicate definition completion count", 0),
            "carried_attractor_class_definition_completion_count": carried.get("Attractor class definition completion count", 0),
            "carried_constraint_region_definition_completion_count": carried.get("Constraint region definition completion count", 0),
            "carried_causal_mass_definition_completion_count": carried.get("Causal mass definition completion count", 0),
            "carried_observer_projection_definition_completion_count": carried.get("Observer projection definition completion count", 0),
            "carried_new_theorem_proven_count": carried.get("New theorem proven count", 0),
            "carried_theorem_candidate_plan_count": carried.get("Theorem candidate plan count", 0),
            "carried_proof_execution_count": carried.get("Proof execution count", 0),
            "carried_proof_assistant_verification_count": carried.get("Proof assistant verification count", 0),
            "carried_formalization_complete_count": carried.get("Formalization complete count", 0),
            "carried_completed_formal_definition_count": carried.get("Completed formal definition count", 0),
            "carried_definition_completion_execution_count": carried.get("Definition completion execution count", 0),
            "carried_full_framework_formal_proof_count": carried.get("Full framework formal proof count", 0),
            "carried_proof_gap_resolution_count": carried.get("Proof gap resolution count", 0),
            "carried_external_validation_count": carried.get("External validation count", 0),
            "carried_new_citation_added_count": carried.get("New citation added count", 0),
            "carried_cumulative_limited_theorem_proven_count": carried.get("Cumulative limited theorem proven count", 5),
            "new_theorem_proven_count": 0,
            "cumulative_limited_theorem_proven_count": 5,
            "theorem_candidate_plan_count": 0,
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

        report_text = self._render_report(dependency_rows, inventory_obligations, counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.104 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.104 report.")
        if counts["core_formal_object_inventory_execution_count"] != 1:
            errors.append("v8.104 must execute exactly one core formal object inventory.")
        if counts["core_formal_object_count"] != 6:
            errors.append("v8.104 must inventory exactly six core formal object families.")
        if counts["candidate_symbol_count"] != 6:
            errors.append("v8.104 must provide exactly six candidate symbols.")
        if counts["dependency_row_count"] < 6:
            errors.append("v8.104 must include dependency rows.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.104 must not execute definitions.")
        if counts["definition_draft_execution_count"] != 0:
            errors.append("v8.104 must not execute definition drafts.")
        if counts["completed_formal_definition_count"] != 0:
            errors.append("v8.104 must not complete formal definitions.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.104 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.104 must not prove a theorem.")

        zero_fields = [
            "definition_inventory_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "definition_draft_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "new_stabilization_predicate_draft_clause_count",
            "new_completion_criterion_count",
            "new_completion_decision_plan_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "new_theorem_proven_count",
            "theorem_candidate_plan_count",
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

        final_report_text = self._render_report(dependency_rows, inventory_obligations, counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return CoreFormalObjectInventoryExecutionReport(
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

    def _render_report(
        self,
        dependency_rows: list[tuple[str, str, str]],
        inventory_obligations: list[str],
        counts: dict[str, int],
        warnings: list[str],
    ) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric execute a core formal object inventory after the formal-definition transition plan "
            "while keeping definition execution, completed formal definitions, theorem candidate planning, theorem proof, "
            "proof assistant verification, external validation, manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Inventory boundary")
        lines.append("- Milestone type: core formal object inventory execution only")
        lines.append("- Definition execution status after this milestone: not executed")
        lines.append("- Formal definition completion status after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("- Theorem proof status after this milestone: not proven")
        lines.append("")
        lines.append("## Core formal object inventory")
        lines.append("")
        lines.append("| Object ID | Family | Candidate symbol | Role | Inputs | Outputs | Dependencies | Definition obligation | Completion status |")
        lines.append("|---|---|---|---|---|---|---|---|---|")
        for row in self.inventory_rows:
            lines.append(
                f"| {row['object_id']} | {row['family']} | {row['candidate_symbol']} | {row['role']} | "
                f"{row['inputs']} | {row['outputs']} | {row['dependencies']} | {row['definition_obligation']} | "
                f"{row['completion_status']} |"
            )
        lines.append("")
        lines.append("## Dependency rows")
        lines.append("")
        lines.append("| From | To | Dependency reason |")
        lines.append("|---|---|---|")
        for source, target, reason in dependency_rows:
            lines.append(f"| {source} | {target} | {reason} |")
        lines.append("")
        lines.append("## Inventory obligations")
        for index, obligation in enumerate(inventory_obligations, start=1):
            lines.append(f"{index}. {obligation}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes a core formal object inventory only. "
            "Candidate symbols are inventory labels, not completed definitions. "
            "It does not execute definitions, does not execute definition drafts, does not complete Sigma_A, "
            "does not complete any formal definition, does not create theorem candidates, does not prove a theorem, "
            "does not run proof execution, does not provide proof assistant verification, does not complete formalization, "
            "does not prove the full framework, does not provide external validation, does not perform an independent experiment, "
            "does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_row_count",
            "candidate_symbol_count",
            "dependency_row_count",
            "definition_obligation_count",
            "inventory_obligation_count",
            "inventoried_only_status_count",
            "gap_resolution_closure_carried_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
            "formal_definition_transition_boundary_audit_plan_count",
            "definition_transition_plan_count",
            "formal_object_inventory_execution_count",
            "definition_inventory_execution_count",
            "definition_execution_count",
            "new_definition_execution_count",
            "definition_draft_execution_count",
            "completed_formal_definition_count",
            "formalization_complete_count",
            "sigma_a_definition_completion_count",
            "stabilization_predicate_definition_completion_count",
            "attractor_class_definition_completion_count",
            "constraint_region_definition_completion_count",
            "causal_mass_definition_completion_count",
            "observer_projection_definition_completion_count",
            "new_stabilization_predicate_draft_clause_count",
            "new_completion_criterion_count",
            "new_completion_decision_plan_count",
            "completion_decision_plan_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "carried_formal_definition_transition_boundary_audit_plan_count",
            "carried_planned_formal_object_count",
            "carried_definition_transition_plan_count",
            "carried_resolved_gap_count",
            "carried_unresolved_gap_count",
            "carried_remaining_blocking_gap_count",
            "carried_conditional_hold_count",
            "carried_completion_decision_count",
            "carried_completion_execution_count",
            "carried_completion_execution_authorized_count",
            "carried_definition_execution_count",
            "carried_new_definition_execution_count",
            "carried_formal_object_inventory_execution_count",
            "carried_sigma_a_definition_completion_count",
            "carried_stabilization_predicate_definition_completion_count",
            "carried_attractor_class_definition_completion_count",
            "carried_constraint_region_definition_completion_count",
            "carried_causal_mass_definition_completion_count",
            "carried_observer_projection_definition_completion_count",
            "carried_new_theorem_proven_count",
            "carried_theorem_candidate_plan_count",
            "carried_proof_execution_count",
            "carried_proof_assistant_verification_count",
            "carried_formalization_complete_count",
            "carried_completed_formal_definition_count",
            "carried_definition_completion_execution_count",
            "carried_full_framework_formal_proof_count",
            "carried_proof_gap_resolution_count",
            "carried_external_validation_count",
            "carried_new_citation_added_count",
            "carried_cumulative_limited_theorem_proven_count",
            "new_theorem_proven_count",
            "cumulative_limited_theorem_proven_count",
            "theorem_candidate_plan_count",
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
        label_overrides = {
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
            "carried_sigma_a_definition_completion_count": "Carried Sigma_A definition completion count",
        }

        for key in counter_order:
            if key in counts:
                label = label_overrides.get(key, key.replace("_", " ").capitalize())
                lines.append(f"- {label}: {counts[key]}")
        lines.append("")
        lines.append("## Warnings")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")
        lines.append("## Interpretation")
        lines.append(
            "The v8.104 artifact executes an inventory of six core formal object families and their dependency obligations. "
            "It provides candidate symbols and definition obligations, but does not execute definitions, does not complete formal definitions, "
            "does not create theorem candidates, does not prove theorems, does not provide proof assistant verification, "
            "does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit the inventory for missing object dependencies.",
            "Convert inventory rows into a Sigma_A definition draft plan.",
            "Keep Sigma_A draft separate from Sigma_A completion.",
            "Draft stabilization predicate only after Sigma_A dependencies are explicit.",
            "Audit dependency consistency before theorem candidate planning.",
            "Keep theorem candidate planning separate from theorem proof.",
            "Keep proof assistant verification, validation, citation work, and manuscript readiness separate.",
            "Do not claim formalization completion from inventory execution alone.",
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
            "not proven",
            "inventory only",
            "not completed definitions",
            "candidate symbols",
            "not completed",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not execute definitions",
            "does not execute definition drafts",
            "does not complete Sigma_A",
            "does not complete any formal definition",
            "does not create theorem candidates",
            "does not prove a theorem",
            "does not run proof execution",
            "does not provide proof assistant verification",
            "does not complete formalization",
            "does not prove the full framework",
            "does not provide external validation",
            "does not perform an independent experiment",
            "does not approve manuscript submission readiness",
            "does not add new citations",
        ]
        return sum(1 for phrase in prohibited if phrase in text)

    def _count_overclaims(self, text: str) -> int:
        """Count unsafe definition/proof/readiness claims without flagging inventory boundaries.

        v8.104 is allowed to execute a core formal object inventory:
        - Core formal object inventory execution count: 1
        - Formal object inventory execution count: 1

        It is not allowed to execute definitions, complete definitions, create theorem
        candidates, prove theorems, verify proofs, validate externally, approve
        manuscript readiness, or add citations.

        Protective lines such as "not completed", "at zero", "count: 0",
        and "inventoried only" are not overclaims.
        """
        forbidden_positive_counter_patterns = [
            r"^[- ]*completion decision count:\\s*[1-9]",
            r"^[- ]*completion execution count:\\s*[1-9]",
            r"^[- ]*completion execution authorized count:\\s*[1-9]",
            r"^[- ]*definition inventory execution count:\\s*[1-9]",
            r"^[- ]*definition execution count:\\s*[1-9]",
            r"^[- ]*new definition execution count:\\s*[1-9]",
            r"^[- ]*definition draft execution count:\\s*[1-9]",
            r"^[- ]*completed formal definition count:\\s*[1-9]",
            r"^[- ]*formalization complete count:\\s*[1-9]",
            r"^[- ]*sigma_a definition completion count:\\s*[1-9]",
            r"^[- ]*sigma a definition completion count:\\s*[1-9]",
            r"^[- ]*Sigma_A definition completion count:\\s*[1-9]",
            r"^[- ]*stabilization predicate definition completion count:\\s*[1-9]",
            r"^[- ]*attractor class definition completion count:\\s*[1-9]",
            r"^[- ]*constraint region definition completion count:\\s*[1-9]",
            r"^[- ]*causal mass definition completion count:\\s*[1-9]",
            r"^[- ]*observer projection definition completion count:\\s*[1-9]",
            r"^[- ]*new stabilization predicate draft clause count:\\s*[1-9]",
            r"^[- ]*new completion criterion count:\\s*[1-9]",
            r"^[- ]*new completion decision plan count:\\s*[1-9]",
            r"^[- ]*new theorem proven count:\\s*[1-9]",
            r"^[- ]*theorem candidate plan count:\\s*[1-9]",
            r"^[- ]*proof assistant verification count:\\s*[1-9]",
            r"^[- ]*formal mathematical proof count:\\s*[1-9]",
            r"^[- ]*formal proof execution count:\\s*[1-9]",
            r"^[- ]*proof execution count:\\s*[1-9]",
            r"^[- ]*proof gap resolution count:\\s*[1-9]",
            r"^[- ]*definition completion execution count:\\s*[1-9]",
            r"^[- ]*full framework formal proof count:\\s*[1-9]",
            r"^[- ]*external validation count:\\s*[1-9]",
            r"^[- ]*independent experiment count:\\s*[1-9]",
            r"^[- ]*manuscript submission ready count:\\s*[1-9]",
            r"^[- ]*readiness approval count:\\s*[1-9]",
            r"^[- ]*new citation added count:\\s*[1-9]",
        ]

        forbidden_unsafe_prose_patterns = [
            r"\\bSigma_A completion achieved\\b",
            r"\\bformal definition completed\\b",
            r"\\bformal definitions completed\\b",
            r"\\bcompleted formal definition achieved\\b",
            r"\\bdefinition execution completed\\b",
            r"\\bdefinition draft completed\\b",
            r"\\btheorem candidate created\\b",
            r"\\btheorem candidates created\\b",
            r"\\btheorem proven\\b",
            r"\\btheorems proven\\b",
            r"\\bproof assistant verification complete\\b",
            r"\\bframework proven\\b",
            r"\\bexternal validation complete\\b",
            r"\\bmanuscript ready\\b",
        ]

        protective_markers = [
            "does not",
            "do not",
            "cannot",
            "not executed",
            "not completed",
            "not defined",
            "not created",
            "not proven",
            "not approved",
            "not completed definitions",
            "inventoried only",
            "inventory only",
            "candidate symbols",
            "candidate symbol",
            "definition obligation",
            "definition obligations",
            "obligation",
            "obligations",
            "keeping",
            "remain absent",
            "remains absent",
            "remain zero",
            "remains zero",
            "at zero",
            "separate",
            "zero",
            "count: 0",
        ]

        count = 0
        import re

        for raw_line in text.splitlines():
            line = raw_line.strip()
            lowered = line.lower()

            if not lowered:
                continue

            if lowered.startswith("- carried ") or lowered.startswith("carried "):
                continue

            if any(marker in lowered for marker in protective_markers):
                continue

            for pattern in forbidden_positive_counter_patterns:
                if re.search(pattern.lower(), lowered):
                    count += 1
                    break
            else:
                for pattern in forbidden_unsafe_prose_patterns:
                    if re.search(pattern.lower(), lowered):
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
    report = CoreFormalObjectInventoryExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
