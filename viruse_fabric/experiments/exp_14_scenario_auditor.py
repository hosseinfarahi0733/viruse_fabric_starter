from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.biology.scenario_auditor import ScenarioSafetyConsistencyAuditor
from viruse_fabric.biology.viral_scenarios import build_viral_pattern_scenarios

console = Console()


def main() -> None:
    auditor = ScenarioSafetyConsistencyAuditor()
    scenarios = build_viral_pattern_scenarios()
    report = auditor.audit(scenarios)

    console.rule("Experiment 14: Scenario Safety & Consistency Auditor")
    console.print(
        "Question: Does the viral-pattern scenario layer remain safe, non-operational, "
        "and internally consistent?"
    )

    summary = Table(title="Scenario audit summary")
    summary.add_column("Scenario")
    summary.add_column("Status")
    summary.add_column("Score")
    summary.add_column("Path")
    summary.add_column("Constructive")
    summary.add_column("Tension wells")
    summary.add_column("Strained gateways")
    summary.add_column("Findings")

    for result in report.results:
        summary.add_row(
            result.scenario_name,
            result.status,
            f"{result.score:.2f}",
            " → ".join(result.path),
            ", ".join(result.constructive_nodes) or "none",
            ", ".join(result.tension_wells) or "none",
            ", ".join(result.strained_gateways) or "none",
            str(result.finding_count),
        )

    console.print(summary)

    findings_table = Table(title="Audit findings")
    findings_table.add_column("Scenario")
    findings_table.add_column("Category")
    findings_table.add_column("Severity")
    findings_table.add_column("Message")
    findings_table.add_column("Evidence")
    findings_table.add_column("Recommendation")

    all_findings = [
        finding
        for result in report.results
        for finding in result.findings
    ] + report.global_findings

    if all_findings:
        for finding in all_findings:
            findings_table.add_row(
                finding.scenario_name,
                finding.category,
                finding.severity,
                finding.message,
                finding.evidence,
                finding.recommendation,
            )
    else:
        findings_table.add_row(
            "all",
            "audit",
            "info",
            "No safety or consistency findings.",
            "none",
            "No correction needed.",
        )

    console.print(findings_table)

    console.rule("Audit verdict")
    console.print(f"Overall status: {report.status}")
    console.print(f"Total findings: {report.total_findings}")
    console.print(f"Interpretation: {report.interpretation}")

    console.rule("Theory note")
    console.print(
        "The scenario auditor acts as a boundary check between abstract causal modeling "
        "and biological-facing language. It helps ensure the theory remains conceptual, "
        "non-operational, and internally consistent."
    )


if __name__ == "__main__":
    main()
