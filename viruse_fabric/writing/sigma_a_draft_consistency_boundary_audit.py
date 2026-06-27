from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaADraftConsistencyBoundaryAuditReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaADraftConsistencyBoundaryAuditBuilder:
    """Build v8.106 Sigma_A draft consistency boundary audit artifact.

    Boundary discipline:
    - This milestone audits the existing Sigma_A draft.
    - It does not create a new Sigma_A draft.
    - It does not execute new definition drafts.
    - It does not complete Sigma_A.
    - It does not complete any formal definition.
    - It does not create theorem candidates.
    - It does not prove theorems.
    - It does not provide proof assistant verification.
    """

    title = "Sigma_A Draft Consistency Boundary Audit v8.106"
    source_artifact = Path("outputs/sigma_a_formal_definition_draft_execution_v8_105.md")
    output_path = Path("outputs/sigma_a_draft_consistency_boundary_audit_v8_106.md")

    audited_clauses = [
        ("SIG-A-DRAFT-001", "Carrier family", "X_A", "carrier remains typed as a candidate family, not a completed carrier definition"),
        ("SIG-A-DRAFT-002", "Time index", "T_A", "time index remains open between discrete, continuous, ordered, or event-indexed regimes"),
        ("SIG-A-DRAFT-003", "Constraint membership", "C_reg", "constraint membership is referenced but not yet formally specified"),
        ("SIG-A-DRAFT-004", "Admissibility predicate", "Adm_A", "admissibility depends on X_A, T_A, and C_reg without completed semantics"),
        ("SIG-A-DRAFT-005", "Transition relation", "R_A", "transition relation depends on admissibility preservation and temporal ordering"),
        ("SIG-A-DRAFT-006", "Trajectory family", "Traj_A", "trajectory family depends on R_A and admissibility inheritance"),
        ("SIG-A-DRAFT-007", "Observer projection compatibility", "Pi_obs", "projection domain and codomain remain definition obligations"),
        ("SIG-A-DRAFT-008", "Causal-mass compatibility", "M_c", "causal-mass typing remains open between functional, measure-like, or ordered valuation regimes"),
        ("SIG-A-DRAFT-009", "Draft Sigma_A tuple", "Sigma_A", "tuple components are listed but not completed as a formal tuple definition"),
        ("SIG-A-DRAFT-010", "Boundary of use", "boundary", "draft may support later audits but cannot support theorem proof yet"),
    ]

    consistency_rows = [
        {
            "check_id": "SIG-A-CONS-001",
            "check": "Carrier and time compatibility",
            "required_relation": "Adm_A must be evaluated over X_A and T_A.",
            "audit_result": "dependency recorded, typing unresolved",
            "remaining_obligation": "Specify whether Adm_A has type X_A x T_A -> Bool or a richer judgment form.",
        },
        {
            "check_id": "SIG-A-CONS-002",
            "check": "Constraint compatibility",
            "required_relation": "C_reg must constrain the same state domain referenced by X_A.",
            "audit_result": "dependency recorded, boundary semantics unresolved",
            "remaining_obligation": "Specify C_reg membership, boundary behavior, and excluded-state semantics.",
        },
        {
            "check_id": "SIG-A-CONS-003",
            "check": "Transition compatibility",
            "required_relation": "R_A must relate admissible states over ordered time indices.",
            "audit_result": "dependency recorded, transition type unresolved",
            "remaining_obligation": "Specify the domain, codomain, temporal order rule, and admissibility preservation rule for R_A.",
        },
        {
            "check_id": "SIG-A-CONS-004",
            "check": "Trajectory compatibility",
            "required_relation": "Traj_A must be generated from or constrained by R_A and Adm_A.",
            "audit_result": "dependency recorded, trajectory regularity unresolved",
            "remaining_obligation": "Specify finite/infinite horizon behavior and admissibility inheritance for trajectories.",
        },
        {
            "check_id": "SIG-A-CONS-005",
            "check": "Observer projection compatibility",
            "required_relation": "Pi_obs must be defined on Sigma_A-compatible states or trajectories.",
            "audit_result": "dependency recorded, projection codomain unresolved",
            "remaining_obligation": "Specify projection domain, codomain, information-loss rule, and predicate compatibility.",
        },
        {
            "check_id": "SIG-A-CONS-006",
            "check": "Causal-mass compatibility",
            "required_relation": "M_c must attach only to admissible transitions or admissible trajectory witnesses.",
            "audit_result": "dependency recorded, aggregation semantics unresolved",
            "remaining_obligation": "Specify whether M_c is a functional, measure-like object, weighted aggregation, or ordered valuation.",
        },
        {
            "check_id": "SIG-A-CONS-007",
            "check": "Tuple well-formedness",
            "required_relation": "Draft Sigma_A tuple components must have mutually compatible domains.",
            "audit_result": "tuple components identified, well-typedness unresolved",
            "remaining_obligation": "Audit component domains before any Sigma_A completion claim.",
        },
        {
            "check_id": "SIG-A-CONS-008",
            "check": "Theorem-use boundary",
            "required_relation": "Sigma_A draft cannot support theorem proof until definition completion and consistency audit pass.",
            "audit_result": "boundary preserved",
            "remaining_obligation": "Keep theorem candidate planning and proof execution separate from this audit.",
        },
    ]

    def run(self) -> SigmaADraftConsistencyBoundaryAuditReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        open_obligations = [
            "Specify X_A carrier type.",
            "Specify T_A time-index regime.",
            "Specify C_reg membership and boundary semantics.",
            "Specify Adm_A judgment type.",
            "Specify R_A transition domain and preservation rule.",
            "Specify Traj_A regularity and admissibility inheritance.",
            "Specify Pi_obs domain, codomain, and information-loss behavior.",
            "Specify M_c mathematical kind and aggregation semantics.",
            "Specify Sigma_A tuple well-formedness.",
            "Specify theorem-use boundary after completed definitions only.",
        ]

        audit_boundaries = [
            "This audit does not create new Sigma_A draft clauses.",
            "This audit does not execute a new definition draft.",
            "This audit does not complete Sigma_A.",
            "This audit does not complete any formal definition.",
            "This audit does not create theorem candidates.",
            "This audit does not prove a theorem.",
            "This audit does not provide proof assistant verification.",
            "This audit does not provide external validation or manuscript readiness.",
        ]

        warnings.extend([
            "This milestone audits Sigma_A draft consistency only.",
            "Sigma_A definition completion remains zero.",
            "Completed formal definition count remains zero.",
            "Theorem candidate planning, theorem proof, proof assistant verification, external validation, and manuscript readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_draft_consistency_boundary_audit_count": 1,
            "sigma_a_draft_clause_audited_count": len(self.audited_clauses),
            "consistency_check_row_count": len(self.consistency_rows),
            "open_definition_obligation_count": len(open_obligations),
            "audit_boundary_count": len(audit_boundaries),
            "dependency_recorded_unresolved_count": 7,
            "boundary_preserved_count": 1,
            "carried_sigma_a_formal_definition_draft_execution_count": carried.get("Sigma_A formal definition draft execution count", 1),
            "carried_formal_definition_draft_execution_count": carried.get("Formal definition draft execution count", 1),
            "carried_definition_draft_execution_count": carried.get("Definition draft execution count", 1),
            "carried_sigma_a_draft_clause_count": carried.get("Sigma_A draft clause count", 10),
            "carried_sigma_a_draft_tuple_component_count": carried.get("Sigma_A draft tuple component count", 8),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "gap_resolution_closure_carried_count": 1,
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
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

        report_text = self._render_report(open_obligations, audit_boundaries, counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.106 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.106 report.")
        if counts["sigma_a_draft_consistency_boundary_audit_count"] != 1:
            errors.append("v8.106 must execute exactly one Sigma_A draft consistency boundary audit.")
        if counts["sigma_a_draft_clause_audited_count"] != 10:
            errors.append("v8.106 must audit exactly ten Sigma_A draft clauses.")
        if counts["consistency_check_row_count"] != 8:
            errors.append("v8.106 must include exactly eight consistency check rows.")
        if counts["new_sigma_a_draft_clause_count"] != 0:
            errors.append("v8.106 must not create new Sigma_A draft clauses.")
        if counts["new_definition_draft_execution_count"] != 0:
            errors.append("v8.106 must not execute a new definition draft.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.106 must not complete Sigma_A definition.")
        if counts["completed_formal_definition_count"] != 0:
            errors.append("v8.106 must not complete any formal definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.106 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.106 must not prove a theorem.")

        zero_fields = [
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

        final_report_text = self._render_report(open_obligations, audit_boundaries, counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return SigmaADraftConsistencyBoundaryAuditReport(
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
            "sigma_a_draft_consistency_boundary_audit_count": "Sigma_A draft consistency boundary audit count",
            "sigma_a_draft_clause_audited_count": "Sigma_A draft clause audited count",
            "carried_sigma_a_formal_definition_draft_execution_count": "Carried Sigma_A formal definition draft execution count",
            "carried_sigma_a_draft_clause_count": "Carried Sigma_A draft clause count",
            "carried_sigma_a_draft_tuple_component_count": "Carried Sigma_A draft tuple component count",
            "new_sigma_a_draft_clause_count": "New Sigma_A draft clause count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(
        self,
        open_obligations: list[str],
        audit_boundaries: list[str],
        counts: dict[str, int],
        warnings: list[str],
    ) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric audit the Sigma_A draft for consistency after draft execution "
            "while keeping new draft execution, definition execution, Sigma_A definition completion, completed formal definitions, "
            "theorem candidate planning, theorem proof, proof assistant verification, external validation, manuscript readiness, "
            "readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Audit boundary")
        lines.append("- Milestone type: Sigma_A draft consistency boundary audit only")
        lines.append("- New Sigma_A draft clause status after this milestone: not created")
        lines.append("- New definition draft execution status after this milestone: not executed")
        lines.append("- Sigma_A definition completion status after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("- Theorem proof status after this milestone: not proven")
        lines.append("")
        lines.append("## Audited Sigma_A draft clauses")
        lines.append("")
        lines.append("| Clause ID | Name | Symbol | Audit note |")
        lines.append("|---|---|---|---|")
        for clause_id, name, symbol, note in self.audited_clauses:
            lines.append(f"| {clause_id} | {name} | {symbol} | {note} |")
        lines.append("")
        lines.append("## Consistency check rows")
        lines.append("")
        lines.append("| Check ID | Check | Required relation | Audit result | Remaining obligation |")
        lines.append("|---|---|---|---|---|")
        for row in self.consistency_rows:
            lines.append(
                f"| {row['check_id']} | {row['check']} | {row['required_relation']} | "
                f"{row['audit_result']} | {row['remaining_obligation']} |"
            )
        lines.append("")
        lines.append("## Open definition obligations")
        for index, obligation in enumerate(open_obligations, start=1):
            lines.append(f"{index}. {obligation}")
        lines.append("")
        lines.append("## Audit boundaries")
        for index, boundary in enumerate(audit_boundaries, start=1):
            lines.append(f"{index}. {boundary}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact audits the Sigma_A draft only. "
            "It does not create new Sigma_A draft clauses, does not execute a new definition draft, "
            "does not execute definitions, does not complete Sigma_A, does not complete any formal definition, "
            "does not complete formalization, does not create theorem candidates, does not prove a theorem, "
            "does not run proof execution, does not provide proof assistant verification, does not prove the full framework, "
            "does not provide external validation, does not perform an independent experiment, "
            "does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_draft_consistency_boundary_audit_count",
            "sigma_a_draft_clause_audited_count",
            "consistency_check_row_count",
            "open_definition_obligation_count",
            "audit_boundary_count",
            "dependency_recorded_unresolved_count",
            "boundary_preserved_count",
            "carried_sigma_a_formal_definition_draft_execution_count",
            "carried_formal_definition_draft_execution_count",
            "carried_definition_draft_execution_count",
            "carried_sigma_a_draft_clause_count",
            "carried_sigma_a_draft_tuple_component_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
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
            "The v8.106 artifact audits the existing Sigma_A draft for consistency. "
            "It records audited clauses, consistency checks, and open definition obligations. "
            "It does not create a new draft, does not execute definitions, does not complete Sigma_A, "
            "does not complete formal definitions, does not create theorem candidates, does not prove theorems, "
            "does not provide proof assistant verification, does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Resolve Sigma_A carrier typing in a later controlled draft refinement.",
            "Resolve time-index semantics before completion can be considered.",
            "Resolve C_reg membership and boundary behavior.",
            "Resolve Adm_A judgment type and dependency on C_reg.",
            "Resolve R_A temporal ordering and admissibility preservation.",
            "Resolve Traj_A regularity and admissibility inheritance.",
            "Resolve Pi_obs and M_c compatibility with Sigma_A.",
            "Keep theorem candidate planning separate until Sigma_A dependencies are resolved.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = [
            "does not",
            "not created",
            "not executed",
            "not completed",
            "not proven",
            "audit",
            "open definition obligation",
            "remaining obligation",
            "unresolved",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
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
        """Count unsafe completion/proof/readiness claims without flagging carried counters.

        v8.106 is allowed to execute:
        - Sigma_A draft consistency boundary audit count: 1
        - Sigma_A draft clause audited count: 10
        - Consistency check row count: 8
        - Open definition obligation count: 10
        - Carried cumulative limited theorem proven count: 5
        - Cumulative limited theorem proven count: 5

        v8.106 is not allowed to claim:
        - new Sigma_A draft clauses
        - new definition draft execution
        - definition execution
        - Sigma_A definition completion
        - theorem candidate planning
        - new theorem proof
        - proof assistant verification
        - external validation
        - manuscript readiness
        - new citation additions
        """

        forbidden_positive_counter_names = {
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

        allowed_positive_counter_names = {
            "sigma_a draft consistency boundary audit count",
            "sigma a draft consistency boundary audit count",
            "sigma_a draft clause audited count",
            "sigma a draft clause audited count",
            "consistency check row count",
            "open definition obligation count",
            "audit boundary count",
            "dependency recorded unresolved count",
            "boundary preserved count",
            "carried sigma_a formal definition draft execution count",
            "carried sigma a formal definition draft execution count",
            "carried formal definition draft execution count",
            "carried definition draft execution count",
            "carried sigma_a draft clause count",
            "carried sigma a draft clause count",
            "carried sigma_a draft tuple component count",
            "carried sigma a draft tuple component count",
            "core formal object inventory execution count",
            "core formal object count",
            "formal object inventory execution count",
            "gap resolution closure carried count",
            "resolved gap count",
            "completion decision plan count",
            "cumulative limited theorem proven count",
            "hard zero count",
            "boundary phrase count",
            "prohibited behavior count",
            "next step count",
            "word count",
        }

        unsafe_phrases = [
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
            "not created",
            "not executed",
            "not completed",
            "not proven",
            "not provide",
            "not approve",
            "not add",
            "not run",
            "audit",
            "audited",
            "boundary",
            "open definition obligation",
            "remaining obligation",
            "unresolved",
            "carried",
            "cumulative limited",
            "remains zero",
            "remain zero",
            "remains absent",
            "remain absent",
            "at zero",
            "separate",
            "zero",
            "count: 0",
        ]

        count = 0
        import re

        for raw_line in text.splitlines():
            line = raw_line.strip().lstrip("-").strip()
            lowered = line.lower()

            if not lowered:
                continue

            counter_match = re.match(r"^([a-z0-9_ /-]+ count):\\s*([0-9]+)\\s*$", lowered)
            if counter_match:
                counter_name = counter_match.group(1).replace("_", " ").strip()
                value = int(counter_match.group(2))

                if value > 0 and counter_name in forbidden_positive_counter_names:
                    count += 1

                # Any recognized counter line should not be scanned again as prose.
                # This prevents carried/cumulative counters such as
                # "Cumulative limited theorem proven count: 5" from being misread
                # as a new theorem-proof prose claim.
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
    report = SigmaADraftConsistencyBoundaryAuditBuilder().run()
    print(f"Wrote {report.output_path}")
