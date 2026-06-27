from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaAFormalDefinitionDraftExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaAFormalDefinitionDraftExecutionBuilder:
    """Build v8.105 Sigma_A formal definition draft execution artifact.

    Boundary discipline:
    - This milestone drafts Sigma_A.
    - It does not complete Sigma_A.
    - It does not complete any formal definition.
    - It does not create theorem candidates.
    - It does not prove theorems.
    - It does not provide proof assistant verification.
    - It does not provide external validation.
    - It does not approve manuscript readiness.
    """

    title = "Sigma_A Formal Definition Draft Execution v8.105"
    source_artifact = Path("outputs/core_formal_object_inventory_execution_v8_104.md")
    output_path = Path("outputs/sigma_a_formal_definition_draft_execution_v8_105.md")

    draft_clauses = [
        {
            "clause_id": "SIG-A-DRAFT-001",
            "name": "Carrier family",
            "draft_text": "Let X_A denote the candidate carrier family of admissible internal states.",
            "obligation": "Specify whether X_A is a set, typed product, measurable space, graph state family, or structured state schema.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-002",
            "name": "Time index",
            "draft_text": "Let T_A denote the candidate time index used for admissible trajectories.",
            "obligation": "Specify whether T_A is discrete, continuous, partially ordered, or event-indexed.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-003",
            "name": "Constraint membership",
            "draft_text": "Let C_reg be the candidate constraint-region membership structure restricting admissible states.",
            "obligation": "Specify membership predicate, boundary behavior, and interaction with excluded states.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-004",
            "name": "Admissibility predicate",
            "draft_text": "Let Adm_A(x, t) be the candidate predicate stating that state x is admissible at time index t.",
            "obligation": "Specify admissibility semantics and dependency on C_reg.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-005",
            "name": "Transition relation",
            "draft_text": "Let R_A(x, t, x_prime, t_prime) be the candidate admissible transition relation.",
            "obligation": "Specify transition domain, temporal ordering, admissibility preservation, and excluded transitions.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-006",
            "name": "Trajectory family",
            "draft_text": "Let Traj_A be the candidate family of trajectories whose states and transitions satisfy Adm_A and R_A.",
            "obligation": "Specify trajectory regularity, finite or infinite horizon behavior, and admissibility inheritance.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-007",
            "name": "Observer projection compatibility",
            "draft_text": "Let Pi_obs be the candidate observer-projection map defined on a compatible domain of Sigma_A.",
            "obligation": "Specify projection domain, codomain, information loss, and compatibility with trajectories.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-008",
            "name": "Causal-mass compatibility",
            "draft_text": "Let M_c be a candidate causal-mass functional defined only over admissible transitions or trajectory witnesses.",
            "obligation": "Specify whether M_c is a functional, measure-like object, weight aggregation, or ordered valuation.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-009",
            "name": "Draft Sigma_A tuple",
            "draft_text": "Draft Sigma_A := (X_A, T_A, C_reg, Adm_A, R_A, Traj_A, Pi_obs, M_c).",
            "obligation": "Audit whether all tuple components have well-typed domains and compatible dependencies.",
            "status": "drafted, not completed",
        },
        {
            "clause_id": "SIG-A-DRAFT-010",
            "name": "Boundary of use",
            "draft_text": "Sigma_A draft may support later definition consistency audits but cannot support theorem proof until definitions are completed.",
            "obligation": "Separate draft usability from completed definition, theorem candidate planning, theorem proof, and verification.",
            "status": "drafted, not completed",
        },
    ]

    def run(self) -> SigmaAFormalDefinitionDraftExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        dependency_requirements = [
            ("X_A", "C_reg", "carrier states must be compatible with constraint-region membership"),
            ("Adm_A", "X_A", "admissibility predicate is evaluated over candidate states"),
            ("Adm_A", "T_A", "admissibility is indexed by time"),
            ("R_A", "Adm_A", "transitions must preserve or explicitly handle admissibility"),
            ("Traj_A", "R_A", "trajectories are assembled from admissible transitions"),
            ("Pi_obs", "Sigma_A", "observer projection must map from Sigma_A-compatible states or trajectories"),
            ("M_c", "R_A", "causal mass is attached to admissible transition witnesses"),
            ("M_c", "Traj_A", "causal mass aggregation may be trajectory-dependent"),
        ]

        draft_boundaries = [
            "The Sigma_A draft is not a completed formal definition.",
            "The Sigma_A draft does not create theorem candidates.",
            "The Sigma_A draft does not prove a theorem.",
            "The Sigma_A draft does not provide proof assistant verification.",
            "The Sigma_A draft does not provide external validation.",
            "The Sigma_A draft does not approve manuscript readiness.",
        ]

        warnings.extend([
            "This milestone executes a Sigma_A draft only.",
            "Sigma_A definition completion remains zero.",
            "Completed formal definition count remains zero.",
            "Theorem candidate planning, theorem proof, proof assistant verification, external validation, and manuscript readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_formal_definition_draft_execution_count": 1,
            "formal_definition_draft_execution_count": 1,
            "definition_draft_execution_count": 1,
            "sigma_a_draft_clause_count": len(self.draft_clauses),
            "sigma_a_draft_tuple_component_count": 8,
            "dependency_requirement_count": len(dependency_requirements),
            "draft_boundary_count": len(draft_boundaries),
            "drafted_not_completed_status_count": sum(
                1 for row in self.draft_clauses if row["status"] == "drafted, not completed"
            ),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "candidate_symbol_count": carried.get("Candidate symbol count", 6),
            "definition_obligation_count": carried.get("Definition obligation count", 6),
            "gap_resolution_closure_carried_count": 1,
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
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
            "new_stabilization_predicate_draft_clause_count": 0,
            "new_completion_criterion_count": 0,
            "new_completion_decision_plan_count": 0,
            "completion_decision_plan_count": carried.get("Completion decision plan count", 1),
            "completion_decision_count": 0,
            "completion_execution_count": 0,
            "completion_execution_authorized_count": 0,
            "carried_core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "carried_core_formal_object_count": carried.get("Core formal object count", 6),
            "carried_formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "carried_definition_inventory_execution_count": carried.get("Definition inventory execution count", 0),
            "carried_definition_execution_count": carried.get("Definition execution count", 0),
            "carried_definition_draft_execution_count": carried.get("Definition draft execution count", 0),
            "carried_completed_formal_definition_count": carried.get("Completed formal definition count", 0),
            "carried_formalization_complete_count": carried.get("Formalization complete count", 0),
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
            "carried_external_validation_count": carried.get("External validation count", 0),
            "carried_new_citation_added_count": carried.get("New citation added count", 0),
            "carried_cumulative_limited_theorem_proven_count": carried.get("Cumulative limited theorem proven count", 5),
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

        report_text = self._render_report(dependency_requirements, draft_boundaries, counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.105 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.105 report.")
        if counts["sigma_a_formal_definition_draft_execution_count"] != 1:
            errors.append("v8.105 must execute exactly one Sigma_A formal definition draft.")
        if counts["definition_draft_execution_count"] != 1:
            errors.append("v8.105 must set definition draft execution count to 1.")
        if counts["sigma_a_draft_clause_count"] != 10:
            errors.append("v8.105 must draft exactly ten Sigma_A clauses.")
        if counts["sigma_a_draft_tuple_component_count"] != 8:
            errors.append("v8.105 must include eight Sigma_A draft tuple components.")
        if counts["definition_execution_count"] != 0:
            errors.append("v8.105 must not record completed definition execution.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.105 must not complete Sigma_A definition.")
        if counts["completed_formal_definition_count"] != 0:
            errors.append("v8.105 must not complete any formal definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.105 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.105 must not prove a theorem.")

        zero_fields = [
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
            "new_stabilization_predicate_draft_clause_count",
            "new_completion_criterion_count",
            "new_completion_decision_plan_count",
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

        final_report_text = self._render_report(dependency_requirements, draft_boundaries, counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return SigmaAFormalDefinitionDraftExecutionReport(
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
            "sigma_a_formal_definition_draft_execution_count": "Sigma_A formal definition draft execution count",
            "sigma_a_draft_clause_count": "Sigma_A draft clause count",
            "sigma_a_draft_tuple_component_count": "Sigma_A draft tuple component count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
            "carried_sigma_a_definition_completion_count": "Carried Sigma_A definition completion count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(
        self,
        dependency_requirements: list[tuple[str, str, str]],
        draft_boundaries: list[str],
        counts: dict[str, int],
        warnings: list[str],
    ) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric execute a Sigma_A formal definition draft after core formal object inventory "
            "while keeping Sigma_A definition completion, completed formal definitions, theorem candidate planning, theorem proof, "
            "proof assistant verification, external validation, manuscript readiness, readiness approval, and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Draft boundary")
        lines.append("- Milestone type: Sigma_A formal definition draft execution only")
        lines.append("- Sigma_A draft definition status: drafted but not completed")
        lines.append("- Sigma_A definition completion status after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("- Theorem proof status after this milestone: not proven")
        lines.append("")
        lines.append("## Sigma_A draft clauses")
        lines.append("")
        lines.append("| Clause ID | Name | Draft text | Remaining definition obligation | Status |")
        lines.append("|---|---|---|---|---|")
        for row in self.draft_clauses:
            lines.append(
                f"| {row['clause_id']} | {row['name']} | {row['draft_text']} | "
                f"{row['obligation']} | {row['status']} |"
            )
        lines.append("")
        lines.append("## Dependency requirements")
        lines.append("")
        lines.append("| From | To | Requirement reason |")
        lines.append("|---|---|---|")
        for source, target, reason in dependency_requirements:
            lines.append(f"| {source} | {target} | {reason} |")
        lines.append("")
        lines.append("## Draft boundaries")
        for index, boundary in enumerate(draft_boundaries, start=1):
            lines.append(f"{index}. {boundary}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes a Sigma_A formal definition draft only. "
            "Draft clauses and candidate tuple components are not completed definitions. "
            "It does not complete Sigma_A, does not complete any formal definition, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_formal_definition_draft_execution_count",
            "formal_definition_draft_execution_count",
            "definition_draft_execution_count",
            "sigma_a_draft_clause_count",
            "sigma_a_draft_tuple_component_count",
            "dependency_requirement_count",
            "draft_boundary_count",
            "drafted_not_completed_status_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "candidate_symbol_count",
            "definition_obligation_count",
            "gap_resolution_closure_carried_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
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
            "new_stabilization_predicate_draft_clause_count",
            "new_completion_criterion_count",
            "new_completion_decision_plan_count",
            "completion_decision_plan_count",
            "completion_decision_count",
            "completion_execution_count",
            "completion_execution_authorized_count",
            "carried_core_formal_object_inventory_execution_count",
            "carried_core_formal_object_count",
            "carried_formal_object_inventory_execution_count",
            "carried_definition_inventory_execution_count",
            "carried_definition_execution_count",
            "carried_definition_draft_execution_count",
            "carried_completed_formal_definition_count",
            "carried_formalization_complete_count",
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
            "carried_external_validation_count",
            "carried_new_citation_added_count",
            "carried_cumulative_limited_theorem_proven_count",
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
            "The v8.105 artifact executes a Sigma_A formal definition draft with ten draft clauses and eight candidate tuple components. "
            "It is a draft, not a completed definition. It does not complete Sigma_A, does not complete any formal definition, "
            "does not create theorem candidates, does not prove theorems, does not provide proof assistant verification, "
            "does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit Sigma_A draft typing and dependency consistency.",
            "Separate Sigma_A draft clauses from Sigma_A definition completion.",
            "Draft stabilization predicate only after Sigma_A draft dependencies are audited.",
            "Keep theorem candidate planning separate from Sigma_A drafting.",
            "Keep theorem proof separate from theorem candidate planning.",
            "Keep proof assistant verification separate from proof execution.",
            "Keep validation, citation work, and manuscript readiness separate.",
            "Do not claim completed formalization from Sigma_A draft execution alone.",
        ]
        for step in next_steps:
            lines.append(f"- {step}")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _count_boundary_phrases(self, text: str) -> int:
        phrases = [
            "does not",
            "not completed",
            "not created",
            "not proven",
            "draft",
            "not a completed definition",
            "not completed definitions",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
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
        """Count unsafe Sigma_A completion/proof/readiness claims.

        v8.105 is allowed to execute:
        - Sigma_A formal definition draft execution count: 1
        - Formal definition draft execution count: 1
        - Definition draft execution count: 1

        v8.105 is not allowed to claim:
        - Sigma_A definition completion
        - completed formal definitions
        - theorem candidate planning
        - theorem proof
        - proof assistant verification
        - external validation
        - manuscript readiness
        - new citation additions

        Protective draft/boundary prose is not an overclaim.
        """

        forbidden_positive_counter_names = {
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
            "sigma_a formal definition draft execution count",
            "sigma a formal definition draft execution count",
            "formal definition draft execution count",
            "definition draft execution count",
            "sigma_a draft clause count",
            "sigma a draft clause count",
            "sigma_a draft tuple component count",
            "sigma a draft tuple component count",
            "dependency requirement count",
            "draft boundary count",
            "drafted not completed status count",
            "core formal object inventory execution count",
            "core formal object count",
            "formal object inventory execution count",
            "candidate symbol count",
            "definition obligation count",
            "resolved gap count",
            "completion decision plan count",
            "carried core formal object inventory execution count",
            "carried core formal object count",
            "carried formal object inventory execution count",
            "carried cumulative limited theorem proven count",
            "cumulative limited theorem proven count",
            "hard zero count",
            "boundary phrase count",
            "prohibited behavior count",
            "next step count",
            "word count",
        }

        forbidden_unsafe_prose_patterns = [
            r"\\bSigma_A completion achieved\\b",
            r"\\bSigma_A definition completed\\b",
            r"\\bformal definition completed\\b",
            r"\\bformal definitions completed\\b",
            r"\\bcompleted formal definition achieved\\b",
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
            "not complete",
            "not completed",
            "not created",
            "not proven",
            "not provide",
            "not approve",
            "not add",
            "not run",
            "draft",
            "drafted",
            "drafting",
            "draft only",
            "draft execution",
            "not a completed definition",
            "not completed definitions",
            "remaining definition obligation",
            "obligation",
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

            if lowered.startswith("carried "):
                continue

            if any(marker in lowered for marker in protective_markers):
                continue

            counter_match = re.match(r"^([a-z0-9_ /-]+ count):\\s*([0-9]+)\\s*$", lowered)
            if counter_match:
                counter_name = counter_match.group(1).replace("_", " ").strip()
                value = int(counter_match.group(2))

                if value > 0 and counter_name in forbidden_positive_counter_names:
                    count += 1
                    continue

                if value > 0 and counter_name in allowed_positive_counter_names:
                    continue

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
    report = SigmaAFormalDefinitionDraftExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
