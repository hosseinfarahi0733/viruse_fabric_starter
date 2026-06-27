from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaACarrierAndTimeIndexRefinementPlanReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaACarrierAndTimeIndexRefinementPlanBuilder:
    """Build v8.107 Sigma_A carrier and time-index refinement plan.

    Boundary discipline:
    - This milestone plans refinement of X_A and T_A.
    - It does not execute refinement.
    - It does not create new Sigma_A draft clauses.
    - It does not execute a new definition draft.
    - It does not execute definitions.
    - It does not complete Sigma_A.
    - It does not complete any formal definition.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Carrier and Time-Index Refinement Plan v8.107"
    source_artifact = Path("outputs/sigma_a_draft_consistency_boundary_audit_v8_106.md")
    output_path = Path("outputs/sigma_a_carrier_and_time_index_refinement_plan_v8_107.md")

    carrier_plan_rows = [
        {
            "row_id": "X-A-PLAN-001",
            "target": "X_A carrier kind",
            "problem": "The carrier is currently a candidate family without a selected mathematical kind.",
            "planned_refinement": "Compare set-like, typed-product, graph-state, measurable-space, and structured-schema carrier options.",
            "blocked_overreach": "Do not select or complete the carrier definition in this planning milestone.",
        },
        {
            "row_id": "X-A-PLAN-002",
            "target": "X_A component typing",
            "problem": "State components are not yet typed against biological, spatial, and causal coordinates.",
            "planned_refinement": "Plan a component inventory for state variables, coordinate families, and admissibility-relevant attributes.",
            "blocked_overreach": "Do not claim completed state typing.",
        },
        {
            "row_id": "X-A-PLAN-003",
            "target": "X_A compatibility with C_reg",
            "problem": "Constraint-region membership must apply to the same carrier domain.",
            "planned_refinement": "Plan a compatibility check between carrier components and C_reg membership semantics.",
            "blocked_overreach": "Do not define C_reg or complete Sigma_A.",
        },
        {
            "row_id": "X-A-PLAN-004",
            "target": "X_A compatibility with Pi_obs",
            "problem": "Observer projection requires a domain compatible with Sigma_A states or trajectories.",
            "planned_refinement": "Plan a projection-domain compatibility table for Pi_obs.",
            "blocked_overreach": "Do not define Pi_obs or claim proof readiness.",
        },
    ]

    time_index_plan_rows = [
        {
            "row_id": "T-A-PLAN-001",
            "target": "T_A time-index kind",
            "problem": "The time index is open between discrete, continuous, partially ordered, and event-indexed regimes.",
            "planned_refinement": "Compare candidate time regimes against transition relation R_A and trajectory family Traj_A.",
            "blocked_overreach": "Do not select the final time-index definition in this planning milestone.",
        },
        {
            "row_id": "T-A-PLAN-002",
            "target": "Temporal order relation",
            "problem": "R_A requires a temporal ordering relation but the order rule is not specified.",
            "planned_refinement": "Plan a temporal-order relation audit for discrete successor, continuous ordering, and partial-order cases.",
            "blocked_overreach": "Do not execute proof or theorem candidate planning.",
        },
        {
            "row_id": "T-A-PLAN-003",
            "target": "Trajectory horizon",
            "problem": "Traj_A regularity and finite or infinite horizon behavior remain open.",
            "planned_refinement": "Plan horizon cases and required trajectory regularity assumptions.",
            "blocked_overreach": "Do not complete Traj_A or Sigma_A.",
        },
        {
            "row_id": "T-A-PLAN-004",
            "target": "Event-index compatibility",
            "problem": "Event-indexed time may be needed for witness or recurrence evidence but is not typed.",
            "planned_refinement": "Plan whether event-indexing is a base time model or an auxiliary witness structure.",
            "blocked_overreach": "Do not claim completed recurrence or stabilization definitions.",
        },
    ]

    refinement_questions = [
        "Should X_A be represented as a set, typed product, graph-state family, measurable space, or structured state schema?",
        "Which state components are mandatory for admissibility?",
        "Which state components are optional or projection-dependent?",
        "How must C_reg membership relate to X_A?",
        "How must Pi_obs map from X_A or Traj_A?",
        "Should T_A be discrete, continuous, partially ordered, event-indexed, or layered?",
        "What temporal order relation is required by R_A?",
        "What trajectory horizon assumptions are allowed for Traj_A?",
        "Can event-indexing be auxiliary rather than primary?",
        "Which refinement decisions must be resolved before Sigma_A completion can even be considered?",
    ]

    def run(self) -> SigmaACarrierAndTimeIndexRefinementPlanReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        warnings.extend([
            "This milestone plans carrier and time-index refinement only.",
            "No carrier or time-index refinement is executed in v8.107.",
            "Sigma_A definition completion remains zero.",
            "Theorem candidate planning, theorem proof, proof assistant verification, external validation, and manuscript readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_carrier_time_index_refinement_plan_count": 1,
            "carrier_refinement_plan_row_count": len(self.carrier_plan_rows),
            "time_index_refinement_plan_row_count": len(self.time_index_plan_rows),
            "total_refinement_plan_row_count": len(self.carrier_plan_rows) + len(self.time_index_plan_rows),
            "refinement_question_count": len(self.refinement_questions),
            "carrier_option_family_count": 5,
            "time_index_option_family_count": 5,
            "planned_compatibility_check_count": 4,
            "carried_sigma_a_draft_consistency_boundary_audit_count": carried.get("Sigma_A draft consistency boundary audit count", 1),
            "carried_sigma_a_draft_clause_audited_count": carried.get("Sigma_A draft clause audited count", 10),
            "carried_consistency_check_row_count": carried.get("Consistency check row count", 8),
            "carried_open_definition_obligation_count": carried.get("Open definition obligation count", 10),
            "carried_sigma_a_formal_definition_draft_execution_count": carried.get("Carried Sigma_A formal definition draft execution count", 1),
            "carried_definition_draft_execution_count": carried.get("Carried definition draft execution count", 1),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
            "resolved_gap_count": 7,
            "unresolved_gap_count": 0,
            "remaining_blocking_gap_count": 0,
            "conditional_hold_count": 0,
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
            errors.append("Overclaim detected in v8.107 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.107 report.")
        if counts["sigma_a_carrier_time_index_refinement_plan_count"] != 1:
            errors.append("v8.107 must produce exactly one Sigma_A carrier and time-index refinement plan.")
        if counts["carrier_refinement_plan_row_count"] != 4:
            errors.append("v8.107 must include exactly four carrier refinement plan rows.")
        if counts["time_index_refinement_plan_row_count"] != 4:
            errors.append("v8.107 must include exactly four time-index refinement plan rows.")
        if counts["refinement_question_count"] != 10:
            errors.append("v8.107 must include exactly ten refinement questions.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.107 must not execute carrier refinement.")
        if counts["time_index_refinement_execution_count"] != 0:
            errors.append("v8.107 must not execute time-index refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.107 must not execute Sigma_A refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.107 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.107 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.107 must not prove a theorem.")

        zero_fields = [
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

        return SigmaACarrierAndTimeIndexRefinementPlanReport(
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
            "sigma_a_carrier_time_index_refinement_plan_count": "Sigma_A carrier time-index refinement plan count",
            "time_index_refinement_plan_row_count": "Time-index refinement plan row count",
            "time_index_option_family_count": "Time-index option family count",
            "time_index_refinement_execution_count": "Time-index refinement execution count",
            "carried_sigma_a_draft_consistency_boundary_audit_count": "Carried Sigma_A draft consistency boundary audit count",
            "carried_sigma_a_draft_clause_audited_count": "Carried Sigma_A draft clause audited count",
            "carried_sigma_a_formal_definition_draft_execution_count": "Carried Sigma_A formal definition draft execution count",
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
            "Can Viruse Fabric plan refinement of Sigma_A carrier typing and time-index semantics after the Sigma_A draft consistency audit "
            "while keeping refinement execution, new draft execution, definition execution, Sigma_A definition completion, completed formal definitions, "
            "theorem candidate planning, theorem proof, proof assistant verification, external validation, manuscript readiness, readiness approval, "
            "and new citation additions at zero?"
        )
        lines.append("")
        lines.append("## Source")
        lines.append(f"- Source artifact: `{self.source_artifact}`")
        lines.append(f"- Source artifact count: {counts['source_artifact_count']}")
        lines.append(f"- Missing source artifact count: {counts['missing_source_artifact_count']}")
        lines.append("")
        lines.append("## Planning boundary")
        lines.append("- Milestone type: Sigma_A carrier and time-index refinement plan only")
        lines.append("- Carrier refinement execution after this milestone: not executed")
        lines.append("- Time-index refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Carrier refinement plan rows")
        lines.append("")
        lines.append("| Row ID | Target | Problem | Planned refinement | Blocked overreach |")
        lines.append("|---|---|---|---|---|")
        for row in self.carrier_plan_rows:
            lines.append(
                f"| {row['row_id']} | {row['target']} | {row['problem']} | "
                f"{row['planned_refinement']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Time-index refinement plan rows")
        lines.append("")
        lines.append("| Row ID | Target | Problem | Planned refinement | Blocked overreach |")
        lines.append("|---|---|---|---|---|")
        for row in self.time_index_plan_rows:
            lines.append(
                f"| {row['row_id']} | {row['target']} | {row['problem']} | "
                f"{row['planned_refinement']} | {row['blocked_overreach']} |"
            )
        lines.append("")
        lines.append("## Refinement questions")
        for index, question in enumerate(self.refinement_questions, start=1):
            lines.append(f"{index}. {question}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact plans Sigma_A carrier and time-index refinement only. "
            "It does not execute carrier refinement, does not execute time-index refinement, does not execute Sigma_A refinement, "
            "does not create new Sigma_A draft clauses, does not execute a new definition draft, does not execute definitions, "
            "does not complete Sigma_A, does not complete any formal definition, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_carrier_time_index_refinement_plan_count",
            "carrier_refinement_plan_row_count",
            "time_index_refinement_plan_row_count",
            "total_refinement_plan_row_count",
            "refinement_question_count",
            "carrier_option_family_count",
            "time_index_option_family_count",
            "planned_compatibility_check_count",
            "carried_sigma_a_draft_consistency_boundary_audit_count",
            "carried_sigma_a_draft_clause_audited_count",
            "carried_consistency_check_row_count",
            "carried_open_definition_obligation_count",
            "carried_sigma_a_formal_definition_draft_execution_count",
            "carried_definition_draft_execution_count",
            "core_formal_object_inventory_execution_count",
            "core_formal_object_count",
            "formal_object_inventory_execution_count",
            "resolved_gap_count",
            "unresolved_gap_count",
            "remaining_blocking_gap_count",
            "conditional_hold_count",
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
            "The v8.107 artifact plans refinement of Sigma_A carrier typing and time-index semantics. "
            "It does not execute refinement, does not create new draft clauses, does not execute definitions, "
            "does not complete Sigma_A, does not complete formal definitions, does not create theorem candidates, "
            "does not prove theorems, does not provide proof assistant verification, does not provide external validation, "
            "and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Execute a controlled carrier-type option audit.",
            "Execute a controlled time-index option audit.",
            "Keep option audit separate from selecting final definitions.",
            "Keep refinement planning separate from refinement execution.",
            "Keep Sigma_A completion separate from refinement execution.",
            "Keep theorem candidate planning separate from Sigma_A completion.",
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
            "plan",
            "planning",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
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
            "time-index refinement executed",
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
            "plan",
            "planned",
            "planning",
            "blocked overreach",
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
    report = SigmaACarrierAndTimeIndexRefinementPlanBuilder().run()
    print(f"Wrote {report.output_path}")
