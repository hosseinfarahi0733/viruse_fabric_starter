from __future__ import annotations

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from viruse_fabric.biology.viral_scenarios import build_viral_pattern_scenarios
from viruse_fabric.simulation.intention_correction import IntentionCorrectionEngine

console = Console()


def main() -> None:
    engine = IntentionCorrectionEngine()
    scenarios = build_viral_pattern_scenarios()

    reports = [
        engine.generate(scenario.fabric, case_name=scenario.name)
        for scenario in scenarios
    ]

    console.rule("Experiment 16: Intention Correction Report")
    console.print(
        "Question: How should observer stories of intention be corrected?"
    )

    table = Table(title="Intention correction summary")
    table.add_column("Scenario")
    table.add_column("Path")
    table.add_column("Targeting")
    table.add_column("Misreading")
    table.add_column("Main error source")
    table.add_column("Confidence")

    for report in reports:
        table.add_row(
            report.case_name,
            " → ".join(report.path),
            f"{report.apparent_targeting_score:.2f}",
            f"{report.misreading_score:.2f}",
            report.main_error_source,
            report.confidence,
        )

    console.print(table)

    for report in reports:
        console.print(
            Panel(
                "\n".join(
                    [
                        f"[bold]Mistaken story:[/bold] {report.mistaken_story}",
                        "",
                        f"[bold]Corrected story:[/bold] {report.corrected_story}",
                        "",
                        f"[bold]Correction principle:[/bold] {report.correction_principle}",
                        "",
                        f"[bold]Book paragraph:[/bold] {report.book_paragraph}",
                    ]
                ),
                title=report.case_name,
            )
        )

    console.rule("Theory note")
    console.print(
        "The correction report turns numerical fabric analysis into a textual explanation. "
        "It separates visible pattern, apparent targeting, and observer projection of intention."
    )


if __name__ == "__main__":
    main()
