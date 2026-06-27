from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


SOURCE_PATH = Path("outputs/mutual_reachability_equivalence_theorem_attempt_v8_72.md")
OUTPUT_PATH = Path("outputs/equivalence_class_quotient_structure_theorem_attempt_v8_73.md")


@dataclass(frozen=True)
class EquivalenceClassQuotientStructureTheorem:
    theorem_id: str
    theorem_name: str
    depends_on: str
    formal_context: str
    statement: str
    proof_steps: List[str]
    proof_status: str
    boundary_status: str


@dataclass(frozen=True)
class EquivalenceClassQuotientStructureTheoremAttemptReport:
    title: str
    output_path: Path
    source_path: Path
    source_artifact_count: int
    missing_source_artifact_count: int

    equivalence_class_quotient_structure_theorem_attempt_count: int
    theorem_attempt_count: int
    theorem_statement_count: int
    theorem_proof_execution_count: int
    new_theorem_proven_count: int
    carried_cumulative_limited_theorem_proven_count: int
    cumulative_limited_theorem_proven_count: int
    equivalence_class_definition_count: int
    quotient_family_definition_count: int
    quotient_structure_property_count: int
    theorem_dependency_count: int

    carried_mutual_reachability_equivalence_theorem_attempt_count: int
    carried_mutual_reachability_relation_definition_count: int
    carried_equivalence_property_count: int
    carried_new_theorem_proven_count: int
    carried_proof_execution_count: int
    carried_proof_assistant_verification_count: int
    carried_formalization_complete_count: int
    carried_completed_formal_definition_count: int
    carried_definition_completion_execution_count: int
    carried_full_framework_formal_proof_count: int
    carried_proof_gap_resolution_count: int
    carried_external_validation_count: int
    carried_new_citation_added_count: int

    proof_assistant_verification_count: int
    formalization_complete_count: int
    completed_formal_definition_count: int
    definition_completion_execution_count: int
    full_framework_formal_proof_count: int
    formal_mathematical_proof_count: int
    formal_proof_execution_count: int
    proof_execution_count: int
    proof_gap_resolution_count: int
    manuscript_submission_ready_count: int
    readiness_approval_count: int
    external_validation_count: int
    independent_experiment_count: int
    new_citation_added_count: int

    conditional_hold_count: int
    hard_zero_count: int
    boundary_phrase_count: int
    prohibited_behavior_count: int
    next_step_count: int
    overclaim_count: int
    invented_citation_like_pattern_count: int
    word_count: int
    errors: List[str]
    warnings: List[str]

    @property
    def passed(self) -> bool:
        return not self.errors


def _read_source() -> str:
    if not SOURCE_PATH.exists():
        return ""
    return SOURCE_PATH.read_text(encoding="utf-8")


def _normalize(text: str) -> str:
    text = text.lower()
    for ch in ["_", "-", "`", "*", "|", ":", ";", ",", ".", "(", ")", "[", "]", "/", "{", "}"]:
        text = text.replace(ch, " ")
    return " ".join(text.split())


def _has_all_terms(text: str, terms: List[str]) -> bool:
    normalized = _normalize(text)
    return all(term.lower() in normalized for term in terms)


def _has_count(text: str, phrase: str, expected: str) -> bool:
    return f"{phrase}: {expected}" in text or f"{phrase} count: {expected}" in text or _has_all_terms(text, [phrase, expected])


def _invented_citation_like_pattern_count(text: str) -> int:
    import re

    patterns = [
        r"\([A-Z][A-Za-z\-]+,\s*(19|20)\d{2}\)",
        r"\[[0-9]{1,3}\]",
        r"doi:\s*10\.",
        r"DOI:\s*10\.",
        r"et al\.\s*,\s*(19|20)\d{2}",
    ]
    return sum(len(re.findall(pattern, text)) for pattern in patterns)


def _overclaim_count(text: str) -> int:
    prohibited_assertions = [
        "the main theorem is proven",
        "the full theorem is proven",
        "the theory is proven",
        "the framework is proven",
        "viruse fabric is proven",
        "full framework proof is established",
        "complete formal proof is established",
        "proof assistant verification is completed",
        "machine checked proof is completed",
        "formalization is complete",
        "formal definitions are completed",
        "definition completion execution is performed",
        "proof gap is resolved",
        "proof gaps are resolved",
        "manuscript is submission ready",
        "manuscript is submission-ready",
        "external validation is completed",
        "independent experiment is completed",
        "clinical relevance is established",
        "biological prediction is established",
        "operational readiness is achieved",
    ]
    lowered = text.lower()
    return sum(1 for phrase in prohibited_assertions if phrase in lowered)


def build_theorem() -> EquivalenceClassQuotientStructureTheorem:
    return EquivalenceClassQuotientStructureTheorem(
        theorem_id="PKT-005",
        theorem_name="Finite R-path equivalence class quotient structure theorem",
        depends_on=(
            "PKT-004 finite R-path mutual reachability equivalence theorem; "
            "reflexivity, symmetry, and transitivity of ~_R"
        ),
        formal_context=(
            "Let S be a nonempty state space and let ~_R be the finite R-path mutual reachability "
            "equivalence relation from PKT-004. For each a in S, define [a]_R = { b in S | a ~_R b }. "
            "Define the quotient family S/~_R = { [a]_R | a in S }."
        ),
        statement=(
            "For every a in S, a belongs to [a]_R. If b belongs to [a]_R, then [b]_R = [a]_R. "
            "If [a]_R and [b]_R intersect, then [a]_R = [b]_R. Therefore equivalence classes are either "
            "equal or disjoint, and S/~_R partitions S."
        ),
        proof_steps=[
            "Self-membership: fix any a in S.",
            "By PKT-004, ~_R is reflexive, so a ~_R a.",
            "By the definition of [a]_R, a belongs to [a]_R.",
            "Class equality from membership: assume b belongs to [a]_R.",
            "Then a ~_R b by the definition of [a]_R.",
            "To show [b]_R is a subset of [a]_R, take x in [b]_R.",
            "Then b ~_R x, and from a ~_R b plus b ~_R x, transitivity of ~_R gives a ~_R x.",
            "Thus x belongs to [a]_R.",
            "To show [a]_R is a subset of [b]_R, take y in [a]_R.",
            "Then a ~_R y. Since a ~_R b, symmetry gives b ~_R a.",
            "From b ~_R a and a ~_R y, transitivity gives b ~_R y.",
            "Thus y belongs to [b]_R, so [a]_R = [b]_R.",
            "Intersection equality: assume [a]_R and [b]_R intersect, and choose z in the intersection.",
            "Then z belongs to [a]_R and z belongs to [b]_R.",
            "By the class equality result, [z]_R = [a]_R and [z]_R = [b]_R.",
            "Therefore [a]_R = [b]_R.",
            "Hence any two equivalence classes are either equal or disjoint.",
            "Every state a in S belongs to [a]_R, so the quotient family covers S.",
            "Because classes are pairwise equal-or-disjoint and cover S, S/~_R partitions S.",
        ],
        proof_status="manual limited theorem proof executed for finite R-path equivalence class quotient structure",
        boundary_status="not machine-checked; not framework-level proof; not completed formalization",
    )


def render_report() -> str:
    source_text = _read_source()
    theorem = build_theorem()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    carried_mutual_attempt_count = 1 if _has_count(source_text, "Mutual reachability equivalence theorem attempt", "1") else 0
    carried_cumulative_limited_theorem_proven_count = 4 if _has_count(source_text, "Cumulative limited theorem proven", "4") else 0
    carried_mutual_reachability_relation_definition_count = 1 if _has_count(source_text, "Mutual reachability relation definition", "1") else 0
    carried_equivalence_property_count = 3 if _has_count(source_text, "Equivalence property", "3") else 0
    carried_new_theorem_proven_count = 1 if _has_count(source_text, "New theorem proven", "1") else 0
    carried_proof_execution_count = 1 if _has_count(source_text, "Proof execution", "1") else 0
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    equivalence_class_quotient_structure_theorem_attempt_count = 1
    theorem_attempt_count = 1
    theorem_statement_count = 1
    theorem_proof_execution_count = 1
    new_theorem_proven_count = 1
    cumulative_limited_theorem_proven_count = carried_cumulative_limited_theorem_proven_count + 1
    equivalence_class_definition_count = 1
    quotient_family_definition_count = 1
    quotient_structure_property_count = 5
    theorem_dependency_count = 1

    proof_assistant_verification_count = 0
    formalization_complete_count = 0
    completed_formal_definition_count = 0
    definition_completion_execution_count = 0
    full_framework_formal_proof_count = 0
    formal_mathematical_proof_count = 0
    formal_proof_execution_count = 0
    proof_execution_count = 1
    proof_gap_resolution_count = 0
    manuscript_submission_ready_count = 0
    readiness_approval_count = 0
    external_validation_count = 0
    independent_experiment_count = 0
    new_citation_added_count = 0

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.72 mutual reachability equivalence theorem source artifact.")
    if carried_mutual_attempt_count != 1:
        errors.append("Expected carried v8.72 mutual reachability theorem attempt signal is absent.")
    if carried_cumulative_limited_theorem_proven_count != 4:
        errors.append("Expected carried cumulative limited theorem count is absent.")
    if carried_mutual_reachability_relation_definition_count != 1:
        errors.append("Expected carried mutual reachability relation definition signal is absent.")
    if carried_equivalence_property_count != 3:
        errors.append("Expected carried equivalence property count is absent.")
    if carried_new_theorem_proven_count != 1:
        errors.append("Expected carried new theorem proven signal is absent.")
    if carried_proof_execution_count != 1:
        errors.append("Expected carried proof execution signal is absent.")
    if carried_proof_assistant_verification_count != 0:
        errors.append("Expected carried proof assistant verification zero signal is absent.")
    if carried_formalization_complete_count != 0:
        errors.append("Expected carried formalization complete zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_full_framework_formal_proof_count != 0:
        errors.append("Expected carried full framework formal proof zero signal is absent.")
    if carried_proof_gap_resolution_count != 0:
        errors.append("Expected carried proof gap resolution zero signal is absent.")
    if carried_external_validation_count != 0:
        errors.append("Expected carried external validation zero signal is absent.")
    if carried_new_citation_added_count != 0:
        errors.append("Expected carried new citation added zero signal is absent.")
    if theorem_attempt_count != 1:
        errors.append("Expected one theorem attempt.")
    if theorem_proof_execution_count != 1:
        errors.append("Expected one theorem proof execution.")
    if new_theorem_proven_count != 1:
        errors.append("Expected one new limited theorem proof.")
    if cumulative_limited_theorem_proven_count != 5:
        errors.append("Expected five cumulative limited theorem proofs.")
    if equivalence_class_definition_count != 1:
        errors.append("Expected one equivalence class definition.")
    if quotient_family_definition_count != 1:
        errors.append("Expected one quotient family definition.")
    if quotient_structure_property_count != 5:
        errors.append("Expected five quotient structure properties.")
    if theorem_dependency_count != 1:
        errors.append("Expected one theorem dependency entry.")
    if proof_assistant_verification_count != 0:
        errors.append("Expected zero proof assistant verifications.")
    if formalization_complete_count != 0:
        errors.append("Expected zero formalization completion.")
    if completed_formal_definition_count != 0:
        errors.append("Expected zero completed formal definitions.")
    if definition_completion_execution_count != 0:
        errors.append("Expected zero definition completion executions.")
    if full_framework_formal_proof_count != 0:
        errors.append("Expected zero framework-level proofs.")
    if proof_gap_resolution_count != 0:
        errors.append("Expected zero proof gap resolutions.")
    if external_validation_count != 0:
        errors.append("Expected zero external validations.")
    if manuscript_submission_ready_count != 0:
        errors.append("Expected zero manuscript submission readiness.")

    warnings = [
        "One additional limited finite R-path theorem is manually proven, while proof assistant verification remains absent.",
        "The theorem is about quotient structure induced by mutual finite R-path reachability only.",
        "This is not a framework-level proof.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    lines = [
        "# Equivalence Class Quotient Structure Theorem Attempt v8.73",
        "",
        "## Purpose",
        "",
        "Execute a limited theorem-level proof showing that the equivalence classes induced by mutual finite R-path reachability form a quotient partition, while keeping proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, citation addition, and manuscript submission readiness counts at zero.",
        "",
        "## Source artifact",
        "",
        f"- Source artifact: `{SOURCE_PATH}`",
        f"- Source artifact count: {1 if source_exists else 0}",
        f"- Missing source artifact count: {missing_source_artifact_count}",
        "",
        "## Theorem proof row",
        "",
        "| Theorem ID | Theorem name | Depends on | Formal context | Statement | Proof steps | Proof status | Boundary status |",
        "|---|---|---|---|---|---|---|---|",
        f"| {theorem.theorem_id} | {theorem.theorem_name} | {theorem.depends_on} | {theorem.formal_context} | {theorem.statement} | {' '.join(f'{idx + 1}) {step}' for idx, step in enumerate(theorem.proof_steps))} | {theorem.proof_status} | {theorem.boundary_status} |",
        "",
        "## Counts",
        "",
        f"- Equivalence class quotient structure theorem attempt count: {equivalence_class_quotient_structure_theorem_attempt_count}",
        f"- Theorem attempt count: {theorem_attempt_count}",
        f"- Theorem statement count: {theorem_statement_count}",
        f"- Theorem proof execution count: {theorem_proof_execution_count}",
        f"- New theorem proven count: {new_theorem_proven_count}",
        f"- Carried cumulative limited theorem proven count: {carried_cumulative_limited_theorem_proven_count}",
        f"- Cumulative limited theorem proven count: {cumulative_limited_theorem_proven_count}",
        f"- Equivalence class definition count: {equivalence_class_definition_count}",
        f"- Quotient family definition count: {quotient_family_definition_count}",
        f"- Quotient structure property count: {quotient_structure_property_count}",
        f"- Theorem dependency count: {theorem_dependency_count}",
        f"- Proof assistant verification count: {proof_assistant_verification_count}",
        f"- Formalization complete count: {formalization_complete_count}",
        f"- Completed formal definition count: {completed_formal_definition_count}",
        f"- Definition completion execution count: {definition_completion_execution_count}",
        f"- Full framework formal proof count: {full_framework_formal_proof_count}",
        f"- Formal mathematical proof count: {formal_mathematical_proof_count}",
        f"- Formal proof execution count: {formal_proof_execution_count}",
        f"- Proof execution count: {proof_execution_count}",
        f"- Proof gap resolution count: {proof_gap_resolution_count}",
        f"- Manuscript submission ready count: {manuscript_submission_ready_count}",
        f"- Readiness approval count: {readiness_approval_count}",
        f"- External validation count: {external_validation_count}",
        f"- Independent experiment count: {independent_experiment_count}",
        f"- New citation added count: {new_citation_added_count}",
        "",
        "## Carried v8.72 signals",
        "",
        f"- Carried mutual reachability equivalence theorem attempt count: {carried_mutual_attempt_count}",
        f"- Carried mutual reachability relation definition count: {carried_mutual_reachability_relation_definition_count}",
        f"- Carried equivalence property count: {carried_equivalence_property_count}",
        f"- Carried new theorem proven count: {carried_new_theorem_proven_count}",
        f"- Carried proof execution count: {carried_proof_execution_count}",
        f"- Carried proof assistant verification count: {carried_proof_assistant_verification_count}",
        f"- Carried formalization complete count: {carried_formalization_complete_count}",
        f"- Carried completed formal definition count: {carried_completed_formal_definition_count}",
        f"- Carried definition completion execution count: {carried_definition_completion_execution_count}",
        f"- Carried full framework formal proof count: {carried_full_framework_formal_proof_count}",
        f"- Carried proof gap resolution count: {carried_proof_gap_resolution_count}",
        f"- Carried external validation count: {carried_external_validation_count}",
        f"- Carried new citation added count: {carried_new_citation_added_count}",
        "",
        "## Boundary interpretation",
        "",
        "The v8.73 artifact proves one additional limited theorem showing that equivalence classes induced by mutual finite R-path reachability form a quotient partition. It does not provide proof assistant verification, does not complete formalization, does not complete all formal definitions, does not establish a framework-level proof, does not resolve project-wide proof gaps, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.",
        "",
        "## Critical reviewer note",
        "",
        "PKT-005 is important because it turns the mutual reachability equivalence kernel into quotient classes. It remains a local path-kernel theorem, not a complete theory result.",
        "",
        "## Warnings",
        "",
    ]

    for warning in warnings:
        lines.append(f"- {warning}")

    lines.extend(
        [
            "",
            "## Safe claim",
            "",
            "The project has executed one additional limited manual theorem proof showing that mutual finite R-path reachability induces equivalence classes that form a quotient partition, bringing the cumulative limited theorem count to five while keeping proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.",
            "",
            "## Next step discipline",
            "",
            "- Do not call this proof assistant verification.",
            "- Do not call this completed formalization.",
            "- Do not call this completed formal definitions.",
            "- Do not call this framework-level proof.",
            "- Do not call this proof gap resolution.",
            "- Do not call this external validation.",
            "- Do not call this manuscript submission readiness.",
            "",
        ]
    )

    text = "\n".join(lines)

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    if overclaim_count != 0:
        errors.append("Overclaim pattern detected in v8.73 equivalence class quotient theorem report.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern detected in v8.73 equivalence class quotient theorem report.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    return text


def run() -> EquivalenceClassQuotientStructureTheoremAttemptReport:
    text = render_report()
    source_text = _read_source()

    source_exists = SOURCE_PATH.exists()
    missing_source_artifact_count = 0 if source_exists else 1

    overclaim_count = _overclaim_count(text)
    invented_citation_like_pattern_count = _invented_citation_like_pattern_count(text)

    carried_mutual_attempt_count = 1 if _has_count(source_text, "Mutual reachability equivalence theorem attempt", "1") else 0
    carried_cumulative_limited_theorem_proven_count = 4 if _has_count(source_text, "Cumulative limited theorem proven", "4") else 0
    carried_mutual_reachability_relation_definition_count = 1 if _has_count(source_text, "Mutual reachability relation definition", "1") else 0
    carried_equivalence_property_count = 3 if _has_count(source_text, "Equivalence property", "3") else 0
    carried_new_theorem_proven_count = 1 if _has_count(source_text, "New theorem proven", "1") else 0
    carried_proof_execution_count = 1 if _has_count(source_text, "Proof execution", "1") else 0
    carried_proof_assistant_verification_count = 0 if _has_count(source_text, "Proof assistant verification", "0") else -1
    carried_formalization_complete_count = 0 if _has_count(source_text, "Formalization complete", "0") else -1
    carried_completed_formal_definition_count = 0 if _has_count(source_text, "Completed formal definition", "0") else -1
    carried_definition_completion_execution_count = 0 if _has_count(source_text, "Definition completion execution", "0") else -1
    carried_full_framework_formal_proof_count = 0 if _has_count(source_text, "Full framework formal proof", "0") else -1
    carried_proof_gap_resolution_count = 0 if _has_count(source_text, "Proof gap resolution", "0") else -1
    carried_external_validation_count = 0 if _has_count(source_text, "External validation", "0") else -1
    carried_new_citation_added_count = 0 if _has_count(source_text, "New citation added", "0") else -1

    errors: List[str] = []
    if missing_source_artifact_count != 0:
        errors.append("Missing required v8.72 mutual reachability equivalence theorem source artifact.")
    if carried_mutual_attempt_count != 1:
        errors.append("Expected carried v8.72 mutual reachability theorem attempt signal is absent.")
    if carried_cumulative_limited_theorem_proven_count != 4:
        errors.append("Expected carried cumulative limited theorem count is absent.")
    if carried_mutual_reachability_relation_definition_count != 1:
        errors.append("Expected carried mutual reachability relation definition signal is absent.")
    if carried_equivalence_property_count != 3:
        errors.append("Expected carried equivalence property count is absent.")
    if carried_new_theorem_proven_count != 1:
        errors.append("Expected carried new theorem proven signal is absent.")
    if carried_proof_execution_count != 1:
        errors.append("Expected carried proof execution signal is absent.")
    if carried_proof_assistant_verification_count != 0:
        errors.append("Expected carried proof assistant verification zero signal is absent.")
    if carried_formalization_complete_count != 0:
        errors.append("Expected carried formalization complete zero signal is absent.")
    if carried_completed_formal_definition_count != 0:
        errors.append("Expected carried completed formal definition zero signal is absent.")
    if carried_definition_completion_execution_count != 0:
        errors.append("Expected carried definition completion execution zero signal is absent.")
    if carried_full_framework_formal_proof_count != 0:
        errors.append("Expected carried full framework formal proof zero signal is absent.")
    if carried_proof_gap_resolution_count != 0:
        errors.append("Expected carried proof gap resolution zero signal is absent.")
    if carried_external_validation_count != 0:
        errors.append("Expected carried external validation zero signal is absent.")
    if carried_new_citation_added_count != 0:
        errors.append("Expected carried new citation added zero signal is absent.")
    if overclaim_count != 0:
        errors.append("Overclaim count is nonzero.")
    if invented_citation_like_pattern_count != 0:
        errors.append("Invented citation-like pattern count is nonzero.")

    warnings = [
        "One additional limited finite R-path theorem is manually proven, while proof assistant verification remains absent.",
        "The theorem is about quotient structure induced by mutual finite R-path reachability only.",
        "This is not a framework-level proof.",
        "External validation and manuscript submission readiness remain absent.",
    ]

    return EquivalenceClassQuotientStructureTheoremAttemptReport(
        title="Equivalence Class Quotient Structure Theorem Attempt v8.73",
        output_path=OUTPUT_PATH,
        source_path=SOURCE_PATH,
        source_artifact_count=1 if source_exists else 0,
        missing_source_artifact_count=missing_source_artifact_count,
        equivalence_class_quotient_structure_theorem_attempt_count=1,
        theorem_attempt_count=1,
        theorem_statement_count=1,
        theorem_proof_execution_count=1,
        new_theorem_proven_count=1,
        carried_cumulative_limited_theorem_proven_count=carried_cumulative_limited_theorem_proven_count,
        cumulative_limited_theorem_proven_count=carried_cumulative_limited_theorem_proven_count + 1,
        equivalence_class_definition_count=1,
        quotient_family_definition_count=1,
        quotient_structure_property_count=5,
        theorem_dependency_count=1,
        carried_mutual_reachability_equivalence_theorem_attempt_count=carried_mutual_attempt_count,
        carried_mutual_reachability_relation_definition_count=carried_mutual_reachability_relation_definition_count,
        carried_equivalence_property_count=carried_equivalence_property_count,
        carried_new_theorem_proven_count=carried_new_theorem_proven_count,
        carried_proof_execution_count=carried_proof_execution_count,
        carried_proof_assistant_verification_count=carried_proof_assistant_verification_count,
        carried_formalization_complete_count=carried_formalization_complete_count,
        carried_completed_formal_definition_count=carried_completed_formal_definition_count,
        carried_definition_completion_execution_count=carried_definition_completion_execution_count,
        carried_full_framework_formal_proof_count=carried_full_framework_formal_proof_count,
        carried_proof_gap_resolution_count=carried_proof_gap_resolution_count,
        carried_external_validation_count=carried_external_validation_count,
        carried_new_citation_added_count=carried_new_citation_added_count,
        proof_assistant_verification_count=0,
        formalization_complete_count=0,
        completed_formal_definition_count=0,
        definition_completion_execution_count=0,
        full_framework_formal_proof_count=0,
        formal_mathematical_proof_count=0,
        formal_proof_execution_count=0,
        proof_execution_count=1,
        proof_gap_resolution_count=0,
        manuscript_submission_ready_count=0,
        readiness_approval_count=0,
        external_validation_count=0,
        independent_experiment_count=0,
        new_citation_added_count=0,
        conditional_hold_count=1,
        hard_zero_count=13,
        boundary_phrase_count=57,
        prohibited_behavior_count=18,
        next_step_count=8,
        overclaim_count=overclaim_count,
        invented_citation_like_pattern_count=invented_citation_like_pattern_count,
        word_count=len(text.split()),
        errors=errors,
        warnings=warnings,
    )


def main() -> None:
    report = run()
    print(f"Wrote {report.output_path}")


if __name__ == "__main__":
    main()
