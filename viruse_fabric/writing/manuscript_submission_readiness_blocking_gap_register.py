"""Build the v8.5 manuscript submission readiness blocking gap register.

This milestone records the unresolved blockers that explain why the v8.4
readiness decision execution returned not_ready. It does not resolve any gap,
does not approve submission readiness, and does not add new citations.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent


OUTPUT_PATH = Path("outputs/manuscript_submission_readiness_blocking_gap_register_v8_5.md")

SOURCE_ARTIFACT_COUNT = 35

REQUIRED_SOURCE_PATHS = [
    Path("outputs/manuscript_submission_readiness_decision_execution_v8_4.md"),
]

GAP_ROWS = [
    {
        "id": "MSRBG-ROW-0001",
        "gap_type": "formal_mathematical_proof_gap",
        "source_decision_row": "MSRDE-ROW-0001",
        "severity": "hard_blocker",
        "status": "unresolved",
        "readiness_effect": "prevents_submission_ready_claim",
        "allowed_next_step": "plan formal proof requirements without claiming proof existence",
    },
    {
        "id": "MSRBG-ROW-0002",
        "gap_type": "independent_experiment_gap",
        "source_decision_row": "MSRDE-ROW-0001",
        "severity": "hard_blocker",
        "status": "unresolved",
        "readiness_effect": "prevents_external_confidence_claim",
        "allowed_next_step": "plan independent experiment requirements without executing them",
    },
    {
        "id": "MSRBG-ROW-0003",
        "gap_type": "external_validation_gap",
        "source_decision_row": "MSRDE-ROW-0002",
        "severity": "hard_blocker",
        "status": "unresolved",
        "readiness_effect": "prevents_external_validation_claim",
        "allowed_next_step": "plan external validation requirements without claiming validation",
    },
    {
        "id": "MSRBG-ROW-0004",
        "gap_type": "CAND_0003_retention_boundary_gap",
        "source_decision_row": "MSRDE-ROW-0002",
        "severity": "citation_boundary_hold",
        "status": "conditional_hold_unresolved",
        "readiness_effect": "prevents_using_CAND_0003_in_retained_or_submission_claims",
        "allowed_next_step": "keep CAND-0003 on hold until a dedicated retention decision exists",
    },
]

BOUNDARY_PHRASES = [
    "blocking gap register exists",
    "gap resolution does not exist",
    "manuscript submission-ready status does not exist",
    "readiness approval does not exist",
    "formal mathematical proof does not exist",
    "independent experiment does not exist",
    "external validation does not exist",
    "new citation additions remain zero",
    "CAND-0003 remains conditional hold",
    "research prototype with internal validation",
]

PROHIBITED_BEHAVIORS = [
    "Do not claim gap resolution.",
    "Do not claim submission readiness.",
    "Do not claim readiness approval.",
    "Do not claim formal mathematical proof.",
    "Do not claim independent experiment.",
    "Do not claim external validation.",
    "Do not claim biological prediction.",
    "Do not claim clinical relevance.",
    "Do not claim laboratory guidance.",
    "Do not claim operational readiness.",
    "Do not claim final paper.",
    "Do not claim peer-reviewed manuscript.",
    "Do not claim venue acceptance.",
    "Do not add new citation records.",
    "Do not move CAND-0003 out of conditional hold.",
]

NEXT_STEPS = [
    "Plan a formal proof requirements layer.",
    "Plan an independent experiment requirements layer.",
    "Plan an external validation requirements layer.",
    "Plan a CAND-0003 retention re-check only in a dedicated source-retention milestone.",
    "Keep manuscript status not submission-ready.",
    "Keep all project claims bounded to internal validation.",
    "Avoid new citation additions until source-retention and citation-record milestones exist.",
    "Use a future gap-resolution milestone before any readiness re-decision.",
]

HARD_ZERO_FIELDS = [
    "gap_resolution_count: 0",
    "manuscript_submission_ready_count: 0",
    "readiness_approval_count: 0",
    "formal_mathematical_proof_count: 0",
    "independent_experiment_count: 0",
    "external_validation_count: 0",
    "new_citation_added_count: 0",
]


def _list_block(items: list[str], prefix: str) -> str:
    return "\n".join(f"- {prefix}: {item}" for item in items)


def _gap_row_block(row: dict[str, str]) -> str:
    return dedent(
        f"""
        ### {row['id']}

        gap_type: {row['gap_type']}
        source_decision_row: {row['source_decision_row']}
        severity: {row['severity']}
        status: {row['status']}
        readiness_effect: {row['readiness_effect']}
        allowed_next_step: {row['allowed_next_step']}
        gap_resolved: no
        manuscript_submission_ready: no
        readiness_approval: no
        formal_mathematical_proof: no
        independent_experiment: no
        external_validation: no
        new_citation_added: no

        Interpretation:
        This row records an unresolved blocker. It does not resolve the blocker,
        does not approve manuscript submission readiness, and does not expand the citation set.
        """
    ).strip()


def build_report() -> str:
    rows = "\n\n".join(_gap_row_block(row) for row in GAP_ROWS)

    report = dedent(
        f"""
        # Manuscript Submission Readiness Blocking Gap Register v8.5

        Experiment: 85
        Milestone: v8.5 — Manuscript Submission Readiness Blocking Gap Register
        Status: research prototype with internal validation

        ## Question

        Can Viruse Fabric register the blockers that explain the v8.4 not-ready decision while keeping gap resolution, manuscript submission readiness, formal proof, independent experiment, external validation, and new citation additions at zero?

        ## Answer

        Yes. This artifact creates a blocking gap register from the v8.4 not-ready decision execution.
        It records unresolved blockers. It does not resolve them.

        blocking_gap_register_count: 1
        blocking_gap_row_count: 4
        primary_submission_blocker_count: 3
        citation_boundary_gap_count: 1
        gap_resolution_count: 0
        manuscript_submission_ready_count: 0
        readiness_approval_count: 0
        formal_mathematical_proof_count: 0
        independent_experiment_count: 0
        external_validation_count: 0
        new_citation_added_count: 0
        CAND_0003_conditional_hold_count: 1

        ## Required Source Artifact

        Required source artifact count: {SOURCE_ARTIFACT_COUNT}

        {Path(REQUIRED_SOURCE_PATHS[0])}

        ## Blocking Gap Rows

        {rows}

        ## Hard Zero Fields

        {_list_block(HARD_ZERO_FIELDS, "hard_zero")}

        ## Boundary Phrases

        {_list_block(BOUNDARY_PHRASES, "boundary_phrase")}

        ## Prohibited Behaviors

        {_list_block(PROHIBITED_BEHAVIORS, "prohibited_behavior")}

        ## Next Steps

        {_list_block(NEXT_STEPS, "next_step")}

        ## CAND-0003 Boundary

        CAND-0003 remains conditional hold.
        CAND-0003 remains outside retained rows, citation rows, marker rows, revision rows,
        package rows, readiness rows, decision-plan rows, decision-execution rows, and gap-resolution rows.

        ## Interpretation

        The v8.5 artifact registers four unresolved blocking gaps after the v8.4 not-ready decision execution.
        Three are primary submission-readiness blockers: formal mathematical proof, independent experiment, and external validation.
        One is a citation-boundary hold: CAND-0003 remains conditional hold.

        The correct project status after this artifact is:
        Viruse Fabric is a research prototype with internal validation that includes a manuscript submission readiness blocking gap register.

        ## Still Disallowed

        proven theory
        resolved blocking gaps
        formal mathematical proof
        independent experiment
        external validation
        biological prediction
        clinical relevance
        laboratory guidance
        operational readiness
        submission-ready manuscript
        readiness approval
        accepted scientific theory
        final paper
        peer-reviewed manuscript
        venue acceptance
        """
    ).strip() + "\n"

    return report


def write_report(path: Path = OUTPUT_PATH) -> str:
    report = build_report()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
    return report


def main() -> None:
    write_report()
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
