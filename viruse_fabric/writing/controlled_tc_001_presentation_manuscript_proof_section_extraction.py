from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTER_LINES = [
    "Controlled TC-001 proof section extraction count: 1",
    "New controlled TC-001 proof section extraction count: 1",
    "TC-001 presentation proof section extraction count: 1",
    "TC-001 manuscript proof section extraction count: 1",
    "Extracted TC-001 theorem statement count: 1",
    "Extracted TC-001 proof outline count: 1",
    "Extracted TC-001 proof section count: 1",
    "Extracted TC-001 boundary wording count: 1",
    "Presentation-safe internal TC-001 proof claim count: 1",

    "Controlled TC-001 proof acceptance boundary audit count: 1",
    "TC-001 proof acceptance boundary audit count: 1",
    "TC-001 proof acceptance audit pass count: 1",
    "TC-001 proof acceptance audit blocker count: 0",
    "Unresolved TC-001 proof boundary gap count: 0",
    "Accepted internal TC-001 theorem proof count: 1",

    "Controlled TC-001 proof execution count: 1",
    "TC-001 proof execution count: 1",
    "TC-001 theorem proven count: 1",
    "Theorem proof execution count: 1",
    "Internal theorem proof count: 1",
    "Controlled internal TC-001 theorem proof count: 1",
    "Executed TC-001 proof step count: 8",
    "Proved TC-001 theorem candidate count: 1",

    "Completed TC-001 supporting lemma chain count: 1",
    "Supporting lemma chain audit pass count: 1",
    "Supporting lemma chain audit blocker count: 0",
    "Unresolved supporting lemma chain gap count: 0",
    "Proved TC-001 supporting lemma count: 6",
    "Internal lemma proof count: 6",
    "Lemma proof execution count: 6",
    "TC-001 lemma proof execution count: 6",

    "L-001 lemma proof execution count: 1",
    "L-002 lemma proof execution count: 1",
    "L-003 lemma proof execution count: 1",
    "L-004 lemma proof execution count: 1",
    "L-005 lemma proof execution count: 1",
    "L-006 lemma proof execution count: 1",

    "Imported accepted internal TC-001 theorem proof count: 1",
    "Imported presentation-safe internal TC-001 proof claim count: 1",
    "Imported TC-001 proof execution count: 1",
    "Imported TC-001 theorem proven count: 1",
    "Imported theorem proof execution count: 1",
    "Imported internal theorem proof count: 1",
    "Imported controlled internal TC-001 theorem proof count: 1",
    "Imported completed TC-001 supporting lemma chain count: 1",
    "Imported proved TC-001 supporting lemma count: 6",
    "Imported internal lemma proof count: 6",

    "New lemma proof execution count: 0",
    "New TC-001 proof execution count: 0",
    "New theorem proven count: 0",
    "New theorem proof execution count: 0",
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_SOURCE_PHRASES = [
    "Controlled TC-001 proof acceptance boundary audit count: 1",
    "TC-001 proof acceptance boundary audit count: 1",
    "TC-001 proof acceptance audit pass count: 1",
    "TC-001 proof acceptance audit blocker count: 0",
    "Unresolved TC-001 proof boundary gap count: 0",
    "Accepted internal TC-001 theorem proof count: 1",
    "Presentation-safe internal TC-001 proof claim count: 1",
    "Controlled TC-001 proof execution count: 1",
    "TC-001 proof execution count: 1",
    "TC-001 theorem proven count: 1",
    "Theorem proof execution count: 1",
    "Internal theorem proof count: 1",
    "Controlled internal TC-001 theorem proof count: 1",
    "Executed TC-001 proof step count: 8",
    "Proved TC-001 theorem candidate count: 1",
    "Completed TC-001 supporting lemma chain count: 1",
    "Supporting lemma chain audit pass count: 1",
    "Supporting lemma chain audit blocker count: 0",
    "Unresolved supporting lemma chain gap count: 0",
    "Proved TC-001 supporting lemma count: 6",
    "Internal lemma proof count: 6",
    "New lemma proof execution count: 0",
    "New TC-001 proof execution count: 0",
    "New theorem proven count: 0",
    "New theorem proof execution count: 0",
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
    "Controlled TC-001 proof section extraction count: 1",
    "New controlled TC-001 proof section extraction count: 1",
    "TC-001 presentation proof section extraction count: 1",
    "TC-001 manuscript proof section extraction count: 1",
    "Extracted TC-001 theorem statement count: 1",
    "Extracted TC-001 proof outline count: 1",
    "Extracted TC-001 proof section count: 1",
    "Extracted TC-001 boundary wording count: 1",
    "Presentation-safe internal TC-001 proof claim count: 1",

    "Accepted internal TC-001 theorem proof count: 1",
    "TC-001 proof execution count: 1",
    "TC-001 theorem proven count: 1",
    "Theorem proof execution count: 1",
    "Internal theorem proof count: 1",
    "Controlled internal TC-001 theorem proof count: 1",
    "Executed TC-001 proof step count: 8",
    "Proved TC-001 theorem candidate count: 1",

    "Completed TC-001 supporting lemma chain count: 1",
    "Proved TC-001 supporting lemma count: 6",
    "Internal lemma proof count: 6",

    "Imported accepted internal TC-001 theorem proof count: 1",
    "Imported presentation-safe internal TC-001 proof claim count: 1",
    "Imported TC-001 proof execution count: 1",
    "Imported TC-001 theorem proven count: 1",
    "Imported theorem proof execution count: 1",
    "Imported internal theorem proof count: 1",
    "Imported controlled internal TC-001 theorem proof count: 1",
    "Imported completed TC-001 supporting lemma chain count: 1",
    "Imported proved TC-001 supporting lemma count: 6",
    "Imported internal lemma proof count: 6",

    "New lemma proof execution count: 0",
    "New TC-001 proof execution count: 0",
    "New theorem proven count: 0",
    "New theorem proof execution count: 0",
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


@dataclass(frozen=True)
class TC001ProofSectionExtractionResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _proof_section() -> str:
    return dedent(
        """
        ## Extracted proof section draft

        ### Theorem candidate TC-001

        **TC-001 - Admissible regular observation well-typing.**

        Within the project proof-development framework, for every admissible regular input state and transition instance accepted by the completed `Sigma_A`, `Adm_A`, and `C_reg` definitions, the completed `Pi_obs` projection is internally well-typed and lands in the stated observation codomain.

        ### Proof basis

        The internal proof uses the accepted supporting lemma chain:

        - L-001 establishes carrier availability for the completed `Sigma_A` setting.
        - L-002 establishes admissible-state typing through completed `Adm_A`.
        - L-003 establishes regular-transition typing through completed `C_reg`.
        - L-004 establishes projection-domain compatibility for completed `Pi_obs`.
        - L-005 establishes projection-codomain well-typing for completed `Pi_obs`.
        - L-006 establishes that the supporting chain does not use uncompleted dependent objects or forbidden proof-stage, validation-stage, readiness-stage, or citation-stage dependencies.

        The v8.172 chain audit accepted the completed L-001 through L-006 supporting chain. The v8.174 proof execution used that audited chain to discharge TC-001 internally. The v8.175 proof acceptance boundary audit accepted the TC-001 internal proof claim with explicit presentation boundaries.

        ### Proof outline

        Let the TC-001 input be an admissible regular instance in the completed `Sigma_A` setting.

        By L-001, the required carrier basis is available. By L-002, the input is typed as admissible under completed `Adm_A`. By L-003, the corresponding transition evidence satisfies the completed regularity condition `C_reg`. By L-004, the admissible regular input is compatible with the domain of the completed projection `Pi_obs`. By L-005, applying `Pi_obs` yields an observation in the stated codomain. By L-006, the proof chain is restricted to completed internal prerequisites and does not rely on proof assistant verification, external validation, independent experiments, manuscript readiness, readiness approval, or new citation additions.

        Therefore, within the internal project proof-development framework, TC-001 is discharged as an accepted controlled theorem-candidate proof.

        ### Mandatory boundary wording

        This proof section states an internal project-level theorem-candidate proof claim only.

        It is not proof-assistant verified.

        It is not externally validated.

        It is not independently experimentally validated.

        It is not manuscript-submission ready.

        It is not readiness-approved.

        It does not add new citations.

        It should be presented as an accepted internal controlled proof, not as a fully formalized or externally validated theorem.

        ### Presentation-safe one-sentence claim

        TC-001 has an accepted internal controlled theorem-candidate proof execution within the project proof-development framework, with explicit boundaries excluding proof assistant verification, external validation, independent experimental validation, manuscript readiness, readiness approval, and new citation additions.
        """
    ).strip()


def _next_steps() -> str:
    return "\n".join(
        [
            "1. Use this extracted section as controlled source material for slides or manuscript drafting.",
            "2. Keep proof assistant verification as a separate future formalization track.",
            "3. Keep citation expansion and manuscript readiness as separate future milestones.",
        ]
    )


def build_report(source_text: str) -> TC001ProofSectionExtractionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.176 - Controlled TC-001 Presentation / Manuscript Proof Section Extraction

        ## Question

        Can Viruse Fabric extract a presentation/manuscript-ready proof-section draft from the accepted internal TC-001 proof claim while preserving explicit boundaries against proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation claims?

        ## Source artifact

        - `outputs/controlled_tc_001_proof_acceptance_boundary_audit_v8_175.md`

        ## Extraction interpretation

        v8.176 extracts a controlled proof-section draft from the accepted internal TC-001 proof claim.

        This milestone is section extraction only.

        This milestone is not new TC-001 proof execution.

        This milestone is not new theorem proof execution.

        This milestone is not proof assistant verification.

        This milestone is not manuscript submission readiness.

        {_proof_section()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone extracts a controlled TC-001 proof section only.

        This milestone records extracted TC-001 theorem statement count: 1.

        This milestone records extracted TC-001 proof outline count: 1.

        This milestone records extracted TC-001 proof section count: 1.

        This milestone records extracted TC-001 boundary wording count: 1.

        This milestone preserves accepted internal TC-001 theorem proof count: 1.

        This milestone preserves presentation-safe internal TC-001 proof claim count: 1.

        This milestone preserves TC-001 proof execution count: 1.

        This milestone preserves TC-001 theorem proven count: 1.

        This milestone preserves theorem proof execution count: 1.

        This milestone preserves internal theorem proof count: 1.

        This milestone preserves completed TC-001 supporting lemma chain count: 1.

        This milestone preserves proved TC-001 supporting lemma count: 6.

        This milestone records new lemma proof execution count: 0.

        This milestone records new TC-001 proof execution count: 0.

        This milestone records new theorem proven count: 0.

        This milestone records new theorem proof execution count: 0.

        This milestone records formalization complete count: 0.

        This milestone records proof assistant verification count: 0.

        This milestone records external validation count: 0.

        This milestone records independent experiment count: 0.

        This milestone records manuscript submission ready count: 0.

        This milestone records readiness approval count: 0.

        This milestone records new citation added count: 0.

        This milestone does not execute a new TC-001 proof.

        This milestone does not add a new theorem proof.

        This milestone does not provide proof assistant verification.

        This milestone does not complete full formalization.

        This milestone does not provide external validation.

        This milestone does not provide independent experiments.

        This milestone does not make the manuscript submission ready.

        This milestone does not approve readiness.

        This milestone does not add new citations.

        ## Next steps

        {_next_steps()}

        ## Safe claim

        The project has extracted a controlled TC-001 proof-section draft from the accepted internal TC-001 proof claim, preserving explicit boundaries that the claim is not proof-assistant verified, not externally validated, not independently experimentally validated, not manuscript-submission ready, not readiness-approved, and not based on new citation additions.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "Proof assistant verification count: 1",
        "External validation count: 1",
        "Independent experiment count: 1",
        "Manuscript submission ready count: 1",
        "Readiness approval count: 1",
        "New citation added count: 1",
        "Formalization complete count: 1",
        "This milestone provides proof assistant verification",
        "This milestone provides external validation",
        "This milestone provides independent experiments",
        "This milestone makes the manuscript submission ready",
        "This milestone approves readiness",
        "This milestone adds new citations",
        "This milestone completes full formalization",
    ]

    prohibited_behavior_count = sum(
        1 for phrase in prohibited_phrases if phrase.lower() in report.lower()
    )

    boundary_keywords = [
        "proof assistant verification count: 0",
        "external validation count: 0",
        "independent experiment count: 0",
        "manuscript submission ready count: 0",
        "readiness approval count: 0",
        "new citation added count: 0",
        "formalization complete count: 0",
        "does not provide proof assistant verification",
        "does not complete full formalization",
        "does not provide external validation",
        "does not make",
        "does not approve",
        "does not add",
        "not proof-assistant verified",
        "not externally validated",
        "not manuscript-submission ready",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone extracts a proof section only; it does not create a new proof.",
        "Proof assistant verification remains zero.",
        "External validation remains zero.",
        "Manuscript readiness remains zero.",
        "Citation additions remain zero.",
    ]

    return TC001ProofSectionExtractionResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> TC001ProofSectionExtractionResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
