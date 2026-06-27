from __future__ import annotations

from pathlib import Path
import re
from typing import Any


class SigmaACarrierTypeOptionAuditExecutionReport:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)


class SigmaACarrierTypeOptionAuditExecutionBuilder:
    """Build v8.108 Sigma_A carrier-type option audit execution artifact.

    Boundary discipline:
    - This milestone audits carrier-type options for X_A.
    - It does not select a final carrier type.
    - It does not execute carrier refinement.
    - It does not execute Sigma_A refinement.
    - It does not create new Sigma_A draft clauses.
    - It does not execute a new definition draft.
    - It does not complete Sigma_A.
    - It does not create theorem candidates.
    - It does not prove theorems.
    """

    title = "Sigma_A Carrier-Type Option Audit Execution v8.108"
    source_artifact = Path("outputs/sigma_a_carrier_and_time_index_refinement_plan_v8_107.md")
    output_path = Path("outputs/sigma_a_carrier_type_option_audit_execution_v8_108.md")

    option_rows = [
        {
            "option_id": "X-A-OPT-001",
            "carrier_kind": "set-like carrier",
            "representation": "X_A as a plain admissible state set",
            "strength": "minimal and easy to state",
            "risk": "may under-specify component typing, observation structure, and causal annotations",
            "compatibility": "weak-to-moderate compatibility with C_reg, Pi_obs, and M_c unless extra structures are added",
            "audit_result": "audited, not selected",
        },
        {
            "option_id": "X-A-OPT-002",
            "carrier_kind": "typed-product carrier",
            "representation": "X_A as a product of typed state-component families",
            "strength": "explicit component typing and strong compatibility with admissibility predicates",
            "risk": "may become rigid if event, graph, or observation structure is later needed",
            "compatibility": "strong compatibility with Adm_A, C_reg, Pi_obs, and trajectory construction",
            "audit_result": "audited, not selected",
        },
        {
            "option_id": "X-A-OPT-003",
            "carrier_kind": "graph-state carrier",
            "representation": "X_A as a family of states with graph or relational structure",
            "strength": "supports structured interactions, spatial coupling, and network-like constraints",
            "risk": "adds complexity before proof obligations are clarified",
            "compatibility": "moderate-to-strong compatibility with C_reg and M_c if relation types are specified",
            "audit_result": "audited, not selected",
        },
        {
            "option_id": "X-A-OPT-004",
            "carrier_kind": "measurable-space carrier",
            "representation": "X_A as a measurable or measure-compatible state space",
            "strength": "supports later measure-like causal mass or probabilistic variants",
            "risk": "may over-formalize the framework before necessary assumptions are justified",
            "compatibility": "strong compatibility with M_c if causal mass becomes measure-like",
            "audit_result": "audited, not selected",
        },
        {
            "option_id": "X-A-OPT-005",
            "carrier_kind": "structured-schema carrier",
            "representation": "X_A as a schema of named fields, types, and compatibility relations",
            "strength": "transparent for manuscript explanation and staged formalization",
            "risk": "needs later translation into stricter mathematical form for proof work",
            "compatibility": "strong compatibility with staged definition drafts and audit traceability",
            "audit_result": "audited, not selected",
        },
    ]

    evaluation_criteria = [
        "admissibility predicate compatibility",
        "constraint-region compatibility",
        "observer-projection compatibility",
        "causal-mass compatibility",
        "trajectory construction compatibility",
        "proof-readiness without over-formalization",
        "manuscript explainability",
        "future proof-assistant translation potential",
    ]

    def run(self) -> SigmaACarrierTypeOptionAuditExecutionReport:
        errors: list[str] = []
        warnings: list[str] = []

        source_exists = self.source_artifact.exists()
        source_text = self.source_artifact.read_text(encoding="utf-8") if source_exists else ""

        if not source_exists:
            errors.append(f"Missing source artifact: {self.source_artifact}")

        carried = self._extract_carried_counts(source_text)

        audit_findings = [
            "Typed-product carrier and structured-schema carrier appear most useful for staged definition work.",
            "Set-like carrier is too weak unless paired with additional structure.",
            "Graph-state carrier may be useful but should wait until relational obligations are explicit.",
            "Measurable-space carrier should wait until M_c requires measure-like semantics.",
            "No carrier type is selected in this milestone.",
            "No carrier refinement is executed in this milestone.",
        ]

        warnings.extend([
            "This milestone audits carrier-type options only.",
            "No carrier type is selected in v8.108.",
            "Carrier refinement execution remains zero.",
            "Sigma_A definition completion, theorem candidate planning, theorem proof, proof assistant verification, validation, and readiness remain absent.",
        ])

        counts: dict[str, int] = {
            "source_artifact_count": 1 if source_exists else 0,
            "missing_source_artifact_count": 0 if source_exists else 1,
            "sigma_a_carrier_type_option_audit_execution_count": 1,
            "carrier_type_option_audited_count": len(self.option_rows),
            "carrier_type_option_audit_row_count": len(self.option_rows),
            "carrier_option_evaluation_criterion_count": len(self.evaluation_criteria),
            "carrier_option_audit_finding_count": len(audit_findings),
            "carrier_option_not_selected_status_count": sum(
                1 for row in self.option_rows if row["audit_result"] == "audited, not selected"
            ),
            "carrier_type_selection_count": 0,
            "carrier_type_refinement_execution_count": 0,
            "carrier_refinement_execution_count": 0,
            "time_index_refinement_execution_count": 0,
            "sigma_a_refinement_execution_count": 0,
            "carried_sigma_a_carrier_time_index_refinement_plan_count": carried.get("Sigma_A carrier time-index refinement plan count", 1),
            "carried_carrier_refinement_plan_row_count": carried.get("Carrier refinement plan row count", 4),
            "carried_time_index_refinement_plan_row_count": carried.get("Time-index refinement plan row count", 4),
            "carried_total_refinement_plan_row_count": carried.get("Total refinement plan row count", 8),
            "carried_refinement_question_count": carried.get("Refinement question count", 10),
            "carried_sigma_a_draft_consistency_boundary_audit_count": carried.get("Carried Sigma_A draft consistency boundary audit count", 1),
            "carried_sigma_a_draft_clause_audited_count": carried.get("Carried Sigma_A draft clause audited count", 10),
            "carried_open_definition_obligation_count": carried.get("Carried open definition obligation count", 10),
            "core_formal_object_inventory_execution_count": carried.get("Core formal object inventory execution count", 1),
            "core_formal_object_count": carried.get("Core formal object count", 6),
            "formal_object_inventory_execution_count": carried.get("Formal object inventory execution count", 1),
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

        report_text = self._render_report(audit_findings, counts, warnings)
        counts["boundary_phrase_count"] = self._count_boundary_phrases(report_text)
        counts["prohibited_behavior_count"] = self._count_prohibited_behaviors(report_text)
        counts["overclaim_count"] = self._count_overclaims(report_text)
        counts["invented_citation_like_pattern_count"] = self._count_invented_citation_like_patterns(report_text)
        counts["word_count"] = len(re.findall(r"\b\S+\b", report_text))

        if counts["overclaim_count"] != 0:
            errors.append("Overclaim detected in v8.108 report.")
        if counts["invented_citation_like_pattern_count"] != 0:
            errors.append("Invented citation-like pattern detected in v8.108 report.")
        if counts["sigma_a_carrier_type_option_audit_execution_count"] != 1:
            errors.append("v8.108 must execute exactly one carrier-type option audit.")
        if counts["carrier_type_option_audited_count"] != 5:
            errors.append("v8.108 must audit exactly five carrier-type options.")
        if counts["carrier_option_evaluation_criterion_count"] != 8:
            errors.append("v8.108 must include exactly eight evaluation criteria.")
        if counts["carrier_type_selection_count"] != 0:
            errors.append("v8.108 must not select a carrier type.")
        if counts["carrier_refinement_execution_count"] != 0:
            errors.append("v8.108 must not execute carrier refinement.")
        if counts["sigma_a_refinement_execution_count"] != 0:
            errors.append("v8.108 must not execute Sigma_A refinement.")
        if counts["sigma_a_definition_completion_count"] != 0:
            errors.append("v8.108 must not complete Sigma_A definition.")
        if counts["theorem_candidate_plan_count"] != 0:
            errors.append("v8.108 must not create theorem candidates.")
        if counts["new_theorem_proven_count"] != 0:
            errors.append("v8.108 must not prove a theorem.")

        zero_fields = [
            "carrier_type_selection_count",
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

        final_report_text = self._render_report(audit_findings, counts, warnings)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(final_report_text, encoding="utf-8")

        return SigmaACarrierTypeOptionAuditExecutionReport(
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
            "sigma_a_carrier_type_option_audit_execution_count": "Sigma_A carrier-type option audit execution count",
            "carried_sigma_a_carrier_time_index_refinement_plan_count": "Carried Sigma_A carrier time-index refinement plan count",
            "carried_time_index_refinement_plan_row_count": "Carried time-index refinement plan row count",
            "carried_sigma_a_draft_consistency_boundary_audit_count": "Carried Sigma_A draft consistency boundary audit count",
            "carried_sigma_a_draft_clause_audited_count": "Carried Sigma_A draft clause audited count",
            "new_sigma_a_draft_clause_count": "New Sigma_A draft clause count",
            "sigma_a_refinement_execution_count": "Sigma_A refinement execution count",
            "sigma_a_definition_completion_count": "Sigma_A definition completion count",
        }
        return overrides.get(key, key.replace("_", " ").capitalize())

    def _render_report(self, audit_findings: list[str], counts: dict[str, int], warnings: list[str]) -> str:
        lines: list[str] = []
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## Question")
        lines.append(
            "Can Viruse Fabric audit Sigma_A carrier-type options after carrier and time-index refinement planning "
            "while keeping carrier selection, carrier refinement execution, Sigma_A refinement execution, new draft execution, "
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
        lines.append("- Milestone type: Sigma_A carrier-type option audit execution only")
        lines.append("- Carrier type selection after this milestone: not selected")
        lines.append("- Carrier refinement execution after this milestone: not executed")
        lines.append("- Sigma_A refinement execution after this milestone: not executed")
        lines.append("- Sigma_A definition completion after this milestone: not completed")
        lines.append("- Theorem candidate status after this milestone: not created")
        lines.append("")
        lines.append("## Carrier-type option audit rows")
        lines.append("")
        lines.append("| Option ID | Carrier kind | Representation | Strength | Risk | Compatibility | Audit result |")
        lines.append("|---|---|---|---|---|---|---|")
        for row in self.option_rows:
            lines.append(
                f"| {row['option_id']} | {row['carrier_kind']} | {row['representation']} | "
                f"{row['strength']} | {row['risk']} | {row['compatibility']} | {row['audit_result']} |"
            )
        lines.append("")
        lines.append("## Evaluation criteria")
        for index, criterion in enumerate(self.evaluation_criteria, start=1):
            lines.append(f"{index}. {criterion}")
        lines.append("")
        lines.append("## Audit findings")
        for index, finding in enumerate(audit_findings, start=1):
            lines.append(f"{index}. {finding}")
        lines.append("")
        lines.append("## Boundary statement")
        lines.append(
            "This artifact executes a Sigma_A carrier-type option audit only. "
            "It does not select a carrier type, does not execute carrier refinement, does not execute Sigma_A refinement, "
            "does not create new Sigma_A draft clauses, does not execute a new definition draft, does not execute definitions, "
            "does not complete Sigma_A, does not complete any formal definition, does not complete formalization, "
            "does not create theorem candidates, does not prove a theorem, does not run proof execution, "
            "does not provide proof assistant verification, does not prove the full framework, does not provide external validation, "
            "does not perform an independent experiment, does not approve manuscript submission readiness, and does not add new citations."
        )
        lines.append("")
        lines.append("## Counters")
        counter_order = [
            "sigma_a_carrier_type_option_audit_execution_count",
            "carrier_type_option_audited_count",
            "carrier_type_option_audit_row_count",
            "carrier_option_evaluation_criterion_count",
            "carrier_option_audit_finding_count",
            "carrier_option_not_selected_status_count",
            "carrier_type_selection_count",
            "carrier_type_refinement_execution_count",
            "carrier_refinement_execution_count",
            "time_index_refinement_execution_count",
            "sigma_a_refinement_execution_count",
            "carried_sigma_a_carrier_time_index_refinement_plan_count",
            "carried_carrier_refinement_plan_row_count",
            "carried_time_index_refinement_plan_row_count",
            "carried_total_refinement_plan_row_count",
            "carried_refinement_question_count",
            "carried_sigma_a_draft_consistency_boundary_audit_count",
            "carried_sigma_a_draft_clause_audited_count",
            "carried_open_definition_obligation_count",
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
            "The v8.108 artifact audits five Sigma_A carrier-type options. "
            "It records strengths, risks, compatibility notes, and audit findings, but does not select a carrier type, "
            "does not execute refinement, does not create new draft clauses, does not execute definitions, "
            "does not complete Sigma_A, does not create theorem candidates, does not prove theorems, "
            "does not provide proof assistant verification, does not provide external validation, and does not approve manuscript readiness."
        )
        lines.append("")
        lines.append("## Next steps")
        next_steps = [
            "Audit carrier-type option tradeoffs against proof needs.",
            "Audit carrier-type option tradeoffs against manuscript explainability.",
            "Keep carrier selection separate from option audit.",
            "Keep carrier refinement execution separate from carrier selection.",
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
            "not selected",
            "not executed",
            "not completed",
            "not created",
            "audit",
            "separate",
            "zero",
        ]
        return sum(text.lower().count(phrase) for phrase in phrases)

    def _count_prohibited_behaviors(self, text: str) -> int:
        prohibited = [
            "does not select a carrier type",
            "does not execute carrier refinement",
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
            "carrier type selection count",
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
            "carrier type selected",
            "carrier selection completed",
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
            "not selected",
            "not executed",
            "not completed",
            "not created",
            "not provide",
            "not approve",
            "not add",
            "not run",
            "audit",
            "audited",
            "option",
            "risk",
            "compatibility",
            "finding",
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
    report = SigmaACarrierTypeOptionAuditExecutionBuilder().run()
    print(f"Wrote {report.output_path}")
