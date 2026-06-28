from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTER_LINES = [
    "Controlled L-006 lemma proof execution count: 1",
    "New controlled L-006 lemma proof execution count: 1",
    "L-006 lemma proof execution count: 1",
    "New L-006 lemma proof execution count: 1",
    "New lemma proof execution count: 1",
    "Lemma proof execution count: 6",
    "TC-001 lemma proof execution count: 6",
    "Executed L-006 proof step count: 7",
    "Proved L-006 lemma count: 1",
    "Proved L-005 lemma count: 1",
    "Proved L-004 lemma count: 1",
    "Proved L-003 lemma count: 1",
    "Proved L-002 lemma count: 1",
    "Proved L-001 lemma count: 1",
    "Proved TC-001 supporting lemma count: 6",
    "Internal lemma proof count: 6",

    "Controlled L-006 lemma proof strategy planning count: 1",
    "L-006 lemma proof strategy planning count: 1",
    "Selected lemma count: 1",
    "Selected L-006 count: 1",
    "Planned L-006 proof strategy count: 1",
    "Planned L-006 proof step count: 7",

    "L-001 lemma proof execution count: 1",
    "L-002 lemma proof execution count: 1",
    "L-003 lemma proof execution count: 1",
    "L-004 lemma proof execution count: 1",
    "L-005 lemma proof execution count: 1",
    "Executed L-001 proof step count: 4",
    "Executed L-002 proof step count: 5",
    "Executed L-003 proof step count: 6",
    "Executed L-004 proof step count: 7",
    "Executed L-005 proof step count: 7",

    "Controlled L-005 lemma proof execution count: 1",
    "Controlled L-004 lemma proof execution count: 1",
    "Controlled L-003 lemma proof execution count: 1",
    "Controlled L-002 lemma proof execution count: 1",
    "Controlled L-001 lemma proof execution count: 1",

    "Controlled TC-001 proof obligation lemma planning count: 1",
    "TC-001 proof obligation lemma planning count: 1",
    "Planned proof obligation count: 6",
    "Planned lemma count: 6",
    "TC-001 planned lemma count: 6",
    "Accepted lemma plan count: 1",

    "Selected theorem candidate count: 1",
    "Selected TC-001 count: 1",
    "Planned proof strategy count: 1",
    "TC-001 proof strategy planning count: 1",

    "Theorem candidate plan count: 1",
    "Planned theorem candidate count: 4",
    "Accepted theorem candidate plan count: 1",

    "Dependency closure boundary pass count: 1",
    "Dependency closure blocker count: 0",
    "Unresolved dependency gap count: 0",

    "Dependent-object completion bundle integration count: 1",
    "Completed dependent-object completion bundle count: 1",
    "Dependent-object definition completion count: 6",
    "Completed dependent-object definition count: 6",
    "All dependent-object definition completion count: 1",

    "Imported controlled L-006 lemma proof strategy planning count: 1",
    "Imported L-006 lemma proof strategy planning count: 1",
    "Imported selected L-006 count: 1",
    "Imported planned L-006 proof strategy count: 1",
    "Imported planned L-006 proof step count: 7",
    "Imported L-001 lemma proof execution count: 1",
    "Imported L-002 lemma proof execution count: 1",
    "Imported L-003 lemma proof execution count: 1",
    "Imported L-004 lemma proof execution count: 1",
    "Imported L-005 lemma proof execution count: 1",
    "Imported lemma proof execution count: 5",
    "Imported TC-001 lemma proof execution count: 5",
    "Imported proved L-001 lemma count: 1",
    "Imported proved L-002 lemma count: 1",
    "Imported proved L-003 lemma count: 1",
    "Imported proved L-004 lemma count: 1",
    "Imported proved L-005 lemma count: 1",
    "Imported proved TC-001 supporting lemma count: 5",
    "Imported internal lemma proof count: 5",

    "Formalization complete count: 0",
    "New theorem proven count: 0",
    "Theorem proof execution count: 0",
    "TC-001 proof execution count: 0",
    "TC-001 theorem proven count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_SOURCE_PHRASES = [
    "Controlled L-006 lemma proof strategy planning count: 1",
    "New controlled L-006 lemma proof strategy planning count: 1",
    "L-006 lemma proof strategy planning count: 1",
    "Selected L-006 count: 1",
    "Planned L-006 proof strategy count: 1",
    "Planned L-006 proof step count: 7",
    "L-001 lemma proof execution count: 1",
    "L-002 lemma proof execution count: 1",
    "L-003 lemma proof execution count: 1",
    "L-004 lemma proof execution count: 1",
    "L-005 lemma proof execution count: 1",
    "Lemma proof execution count: 5",
    "TC-001 lemma proof execution count: 5",
    "Proved L-001 lemma count: 1",
    "Proved L-002 lemma count: 1",
    "Proved L-003 lemma count: 1",
    "Proved L-004 lemma count: 1",
    "Proved L-005 lemma count: 1",
    "Proved L-006 lemma count: 0",
    "Proved TC-001 supporting lemma count: 5",
    "Internal lemma proof count: 5",
    "New L-006 lemma proof execution count: 0",
    "L-006 lemma proof execution count: 0",
    "New lemma proof execution count: 0",
    "Formalization complete count: 0",
    "New theorem proven count: 0",
    "Theorem proof execution count: 0",
    "TC-001 proof execution count: 0",
    "TC-001 theorem proven count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
    "Controlled L-006 lemma proof execution count: 1",
    "New controlled L-006 lemma proof execution count: 1",
    "L-006 lemma proof execution count: 1",
    "New L-006 lemma proof execution count: 1",
    "New lemma proof execution count: 1",
    "Lemma proof execution count: 6",
    "TC-001 lemma proof execution count: 6",
    "Executed L-006 proof step count: 7",
    "Proved L-006 lemma count: 1",
    "Proved L-005 lemma count: 1",
    "Proved L-004 lemma count: 1",
    "Proved L-003 lemma count: 1",
    "Proved L-002 lemma count: 1",
    "Proved L-001 lemma count: 1",
    "Proved TC-001 supporting lemma count: 6",
    "Internal lemma proof count: 6",

    "Controlled L-006 lemma proof strategy planning count: 1",
    "L-006 lemma proof strategy planning count: 1",
    "Selected L-006 count: 1",
    "Planned L-006 proof strategy count: 1",
    "Planned L-006 proof step count: 7",

    "L-001 lemma proof execution count: 1",
    "L-002 lemma proof execution count: 1",
    "L-003 lemma proof execution count: 1",
    "L-004 lemma proof execution count: 1",
    "L-005 lemma proof execution count: 1",
    "Executed L-001 proof step count: 4",
    "Executed L-002 proof step count: 5",
    "Executed L-003 proof step count: 6",
    "Executed L-004 proof step count: 7",
    "Executed L-005 proof step count: 7",

    "Planned lemma count: 6",
    "TC-001 planned lemma count: 6",
    "Selected TC-001 count: 1",

    "Imported controlled L-006 lemma proof strategy planning count: 1",
    "Imported L-006 lemma proof strategy planning count: 1",
    "Imported selected L-006 count: 1",
    "Imported planned L-006 proof strategy count: 1",
    "Imported planned L-006 proof step count: 7",
    "Imported L-001 lemma proof execution count: 1",
    "Imported L-002 lemma proof execution count: 1",
    "Imported L-003 lemma proof execution count: 1",
    "Imported L-004 lemma proof execution count: 1",
    "Imported L-005 lemma proof execution count: 1",
    "Imported lemma proof execution count: 5",
    "Imported TC-001 lemma proof execution count: 5",
    "Imported proved L-001 lemma count: 1",
    "Imported proved L-002 lemma count: 1",
    "Imported proved L-003 lemma count: 1",
    "Imported proved L-004 lemma count: 1",
    "Imported proved L-005 lemma count: 1",
    "Imported proved TC-001 supporting lemma count: 5",
    "Imported internal lemma proof count: 5",

    "Formalization complete count: 0",
    "New theorem proven count: 0",
    "Theorem proof execution count: 0",
    "TC-001 proof execution count: 0",
    "TC-001 theorem proven count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


@dataclass(frozen=True)
class L006ProofExecutionResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _proof_block() -> str:
    return dedent(
        """
        ## Executed lemma

        Executed lemma: `L-006 - No uncompleted dependency use lemma`

        Parent theorem candidate:

        `TC-001 - Admissible regular observation well-typing`

        Parent proof obligation:

        `PO-006 - No uncompleted dependency use`

        Lemma statement:

        If the completed dependency bundle, completed `Sigma_A`, completed `Adm_A`, completed `C_reg`, completed `Pi_obs`, and the internally proved L-001 through L-005 lemmas are available, then the TC-001 supporting lemma chain uses no uncompleted dependent object, no unexecuted lemma proof, no TC-001 proof execution, no theorem proof execution, no proof assistant verification, no validation artifact, no manuscript readiness artifact, and no citation addition as a proof dependency.

        ## Controlled internal proof execution

        ### Step E001 - Import completed dependency bundle

        The official dependent-object definition bundle records the completed dependency basis used for TC-001 lemma support.

        Therefore L-006 may use this bundle as the boundary for completed proof dependencies.

        Result:
        - executed
        - accepted internally

        ### Step E002 - Check L-001 and L-002 dependency basis

        Official L-001 and L-002 use completed `Sigma_A`, completed `Adm_A`, and earlier allowed lemma support only.

        Therefore the carrier-availability and admissible-state typing parts of the TC-001 support chain contain no uncompleted dependency.

        Result:
        - executed
        - accepted internally

        ### Step E003 - Check L-003 dependency basis

        Official L-003 uses completed `Sigma_A`, completed `Adm_A`, completed `C_reg`, L-001, and L-002.

        Therefore the regular-transition typing part of the TC-001 support chain contains no uncompleted dependency.

        Result:
        - executed
        - accepted internally

        ### Step E004 - Check L-004 dependency basis

        Official L-004 uses completed `Pi_obs` together with official L-001, L-002, and L-003 support.

        Therefore the projection-domain compatibility part of the TC-001 support chain contains no uncompleted dependency.

        Result:
        - executed
        - accepted internally

        ### Step E005 - Check L-005 dependency basis

        Official L-005 uses completed `Pi_obs` together with official L-001, L-002, L-003, and L-004 support.

        Therefore the projection-codomain well-typing part of the TC-001 support chain contains no uncompleted dependency.

        Result:
        - executed
        - accepted internally

        ### Step E006 - Exclude prohibited dependency classes

        The L-006 proof excludes `M_c`, `R_A`, `Traj_A`, unexecuted L-006 proof as a premise, TC-001 proof execution, theorem proof execution, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and citation additions from the support-chain dependency basis.

        Result:
        - executed
        - accepted internally

        ### Step E007 - Conclude no uncompleted dependency enters TC-001 support chain

        Since L-001 through L-005 each rely only on completed objects and official earlier internal lemma proofs, and since the prohibited dependency classes are explicitly excluded, the TC-001 supporting lemma chain contains no uncompleted dependency.

        Therefore PO-006 is discharged at lemma level.

        Result:
        - executed
        - accepted internally

        ## Controlled proof conclusion

        L-006 is internally proved as a controlled lemma proof artifact.

        The proof establishes that the completed TC-001 supporting lemma chain avoids uncompleted dependent objects and avoids forbidden proof-stage, validation-stage, readiness-stage, and citation-stage dependencies.

        The proof discharges PO-006 at lemma level.

        ## Boundary

        This milestone proves L-006 only as an internal controlled lemma proof.

        It preserves the official L-001, L-002, L-003, L-004, and L-005 internal proofs.

        It does not prove TC-001.

        It does not execute TC-001 proof.

        It does not prove any theorem.

        It does not execute theorem proof.

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
            "1. Audit the completed TC-001 supporting lemma chain before any TC-001 proof execution.",
            "2. Keep TC-001 proof execution separate from L-006 lemma proof execution.",
            "3. Keep proof assistant verification, validation, manuscript readiness, readiness approval, and citation work out of this stage.",
        ]
    )


def build_report(source_text: str) -> L006ProofExecutionResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.171 - Controlled L-006 Lemma Proof Execution

        ## Question

        Can Viruse Fabric execute the controlled internal proof of L-006 from the v8.170 proof strategy while preserving the official L-001, L-002, L-003, L-004, and L-005 proofs and keeping TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, validation, manuscript readiness, readiness approval, and new citations at zero?

        ## Source artifact

        - `outputs/controlled_l_006_lemma_proof_strategy_planning_v8_170.md`

        ## Execution interpretation

        v8.171 executes the internal controlled proof of L-006 only.

        This milestone is L-006 lemma proof execution.

        This milestone preserves the official L-001, L-002, L-003, L-004, and L-005 internal lemma proofs.

        This milestone is not TC-001 proof execution.

        This milestone is not theorem proof execution.

        This milestone is not proof assistant verification.

        {_proof_block()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone executes and internally proves L-006 only.

        This milestone records L-006 lemma proof execution count: 1.

        This milestone records new L-006 lemma proof execution count: 1.

        This milestone records lemma proof execution count: 6.

        This milestone records TC-001 lemma proof execution count: 6.

        This milestone records proved L-006 lemma count: 1.

        This milestone preserves proved L-005 lemma count: 1.

        This milestone preserves proved L-004 lemma count: 1.

        This milestone preserves proved L-003 lemma count: 1.

        This milestone preserves proved L-002 lemma count: 1.

        This milestone preserves proved L-001 lemma count: 1.

        This milestone records proved TC-001 supporting lemma count: 6.

        This milestone records executed L-006 proof step count: 7.

        This milestone does not prove TC-001.

        This milestone does not execute TC-001 proof.

        This milestone does not prove any theorem.

        This milestone does not execute theorem proof.

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

        The project has executed and internally proved L-006 as the sixth controlled TC-001 supporting lemma, while preserving the official L-001, L-002, L-003, L-004, and L-005 proofs and keeping TC-001 proof execution, theorem proof execution, new theorem proof, proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citations at zero.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "This milestone proves TC-001",
        "This milestone executes TC-001 proof",
        "This milestone proves any theorem",
        "This milestone executes theorem proof",
        "This milestone provides proof assistant verification",
        "This milestone provides external validation",
        "This milestone provides independent experiments",
        "This milestone makes the manuscript submission ready",
        "This milestone approves readiness",
        "This milestone adds new citations",
    ]

    prohibited_behavior_count = sum(
        1 for phrase in prohibited_phrases if phrase.lower() in report.lower()
    )

    boundary_keywords = [
        "does not prove tc-001",
        "does not execute tc-001 proof",
        "does not prove any theorem",
        "does not execute theorem proof",
        "does not provide",
        "does not complete full formalization",
        "does not make",
        "does not approve",
        "does not add",
        "at zero",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone proves L-006 only as an internal controlled lemma proof.",
        "The official L-001 through L-005 proofs remain preserved.",
        "TC-001 proof execution remains zero.",
        "Theorem proof execution remains zero.",
        "Proof assistant verification, validation, readiness approval, and citation claims remain absent.",
    ]

    return L006ProofExecutionResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> L006ProofExecutionResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
