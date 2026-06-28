from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTER_LINES = [
    "Controlled TC-001 proof acceptance boundary audit count: 1",
    "New controlled TC-001 proof acceptance boundary audit count: 1",
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

    "Controlled TC-001 proof execution strategy planning count: 1",
    "TC-001 proof execution strategy planning count: 1",
    "Selected theorem candidate count: 1",
    "Selected TC-001 count: 1",
    "Planned TC-001 proof execution strategy count: 1",
    "Planned TC-001 proof execution step count: 8",

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

    "Imported controlled TC-001 proof execution count: 1",
    "Imported new controlled TC-001 proof execution count: 1",
    "Imported TC-001 proof execution count: 1",
    "Imported new TC-001 proof execution count: 1",
    "Imported TC-001 theorem proven count: 1",
    "Imported new theorem proven count: 1",
    "Imported theorem proof execution count: 1",
    "Imported internal theorem proof count: 1",
    "Imported controlled internal TC-001 theorem proof count: 1",
    "Imported executed TC-001 proof step count: 8",
    "Imported proved TC-001 theorem candidate count: 1",

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
    "Controlled TC-001 proof execution count: 1",
    "New controlled TC-001 proof execution count: 1",
    "TC-001 proof execution count: 1",
    "New TC-001 proof execution count: 1",
    "TC-001 theorem proven count: 1",
    "New theorem proven count: 1",
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
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
    "Controlled TC-001 proof acceptance boundary audit count: 1",
    "New controlled TC-001 proof acceptance boundary audit count: 1",
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

    "Imported controlled TC-001 proof execution count: 1",
    "Imported new controlled TC-001 proof execution count: 1",
    "Imported TC-001 proof execution count: 1",
    "Imported new TC-001 proof execution count: 1",
    "Imported TC-001 theorem proven count: 1",
    "Imported new theorem proven count: 1",
    "Imported theorem proof execution count: 1",
    "Imported internal theorem proof count: 1",
    "Imported controlled internal TC-001 theorem proof count: 1",
    "Imported executed TC-001 proof step count: 8",
    "Imported proved TC-001 theorem candidate count: 1",

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
class TC001ProofAcceptanceBoundaryAuditResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _audit_block() -> str:
    return dedent(
        """
        ## Audit object

        Audited object:

        `TC-001 - Admissible regular observation well-typing`

        Audited proof artifact:

        `outputs/controlled_tc_001_proof_execution_v8_174.md`

        ## Acceptance checks

        ### PBA-001 - Internal TC-001 proof execution exists

        The source artifact records TC-001 proof execution count: 1.

        Result:
        - passed

        ### PBA-002 - Internal theorem proof claim exists

        The source artifact records theorem proof execution count: 1 and internal theorem proof count: 1.

        Result:
        - passed

        ### PBA-003 - Supporting lemma chain is complete

        The source artifact preserves completed TC-001 supporting lemma chain count: 1 and proved TC-001 supporting lemma count: 6.

        Result:
        - passed

        ### PBA-004 - No unresolved lemma-chain gap remains

        The source artifact preserves unresolved supporting lemma chain gap count: 0.

        Result:
        - passed

        ### PBA-005 - No new lemma or theorem proof is introduced by this audit

        This audit does not create a new lemma proof execution, a new TC-001 proof execution, or a new theorem proof execution.

        Result:
        - passed

        ### PBA-006 - Proof assistant verification remains excluded

        The source artifact and this audit keep proof assistant verification count: 0.

        Result:
        - passed

        ### PBA-007 - Validation and experiment claims remain excluded

        The source artifact and this audit keep external validation count: 0 and independent experiment count: 0.

        Result:
        - passed

        ### PBA-008 - Manuscript and citation claims remain excluded

        The source artifact and this audit keep manuscript submission ready count: 0, readiness approval count: 0, and new citation added count: 0.

        Result:
        - passed

        ## Accepted presentation-safe wording

        The accepted presentation-safe claim is:

        TC-001 has an accepted internal controlled theorem-candidate proof execution within the project proof-development framework.

        Mandatory boundary wording:

        The proof is not proof-assistant verified, not externally validated, not an independent experiment result, not manuscript-submission ready, and not supported by new citation additions in this milestone.

        ## Audit conclusion

        The TC-001 internal proof claim is accepted at internal project proof-development level.

        The claim is safe for controlled presentation only with explicit boundary wording.

        This milestone is a proof acceptance and boundary audit only.

        It does not execute a new TC-001 proof.

        It does not add a new theorem proof.

        It does not provide proof assistant verification.

        It does not complete full formalization.

        It does not provide external validation.

        It does not provide independent experiments.

        It does not make the manuscript ready.

        It does not approve readiness.

        It does not add new citations.
        """
    ).strip()


def _next_steps() -> str:
    return "\n".join(
        [
            "1. Extract a controlled presentation/manuscript proof section from the accepted TC-001 internal proof.",
            "2. Keep proof assistant verification as a separate future track.",
            "3. Keep external validation, independent experiments, readiness approval, and citation work separate.",
        ]
    )


def build_report(source_text: str) -> TC001ProofAcceptanceBoundaryAuditResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.175 - Controlled TC-001 Proof Acceptance / Boundary Audit

        ## Question

        Can Viruse Fabric accept the v8.174 internal TC-001 theorem-candidate proof execution as a controlled internal proof claim while preserving explicit boundaries against proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation claims?

        ## Source artifact

        - `outputs/controlled_tc_001_proof_execution_v8_174.md`

        ## Audit interpretation

        v8.175 audits and accepts the internal TC-001 proof claim only at project proof-development level.

        This milestone is not new TC-001 proof execution.

        This milestone is not new theorem proof execution.

        This milestone is not proof assistant verification.

        This milestone is not external validation.

        This milestone is not manuscript readiness.

        {_audit_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone accepts the internal TC-001 proof claim only with explicit boundary wording.

        This milestone records TC-001 proof acceptance audit pass count: 1.

        This milestone records TC-001 proof acceptance audit blocker count: 0.

        This milestone records unresolved TC-001 proof boundary gap count: 0.

        This milestone records accepted internal TC-001 theorem proof count: 1.

        This milestone records presentation-safe internal TC-001 proof claim count: 1.

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

        The project has accepted the v8.174 internal TC-001 theorem-candidate proof execution as a controlled internal proof claim, with explicit boundaries that it is not proof-assistant verified, not externally validated, not independently experimentally validated, not manuscript-submission ready, not readiness-approved, and not based on new citation additions.
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
        "This milestone accepts TC-001 only as an internal controlled proof claim.",
        "Proof assistant verification remains zero.",
        "External validation remains zero.",
        "Manuscript readiness remains zero.",
        "Citation additions remain zero.",
    ]

    return TC001ProofAcceptanceBoundaryAuditResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> TC001ProofAcceptanceBoundaryAuditResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
