from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.writing.theory_chapter_exporter import TheoryChapterExporter

console = Console()


def main() -> None:
    exporter = TheoryChapterExporter()

    result = exporter.export(
        output_path="outputs/theory_chapter_v1_7.md",
        title="Apparent Targeting Without Intention",
    )

    console.rule("Experiment 17: Theory Chapter Exporter")
    console.print(
        "Question: Can the simulator export a readable theory chapter from its results?"
    )

    table = Table(title="Chapter export result")
    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Title", result.title)
    table.add_row("Output path", str(result.output_path))
    table.add_row("Scenario count", str(result.scenario_count))
    table.add_row("Safety status", result.safety_status)
    table.add_row("Total findings", str(result.total_findings))
    table.add_row("Word count", str(result.word_count))
    table.add_row("Interpretation", result.interpretation)

    console.print(table)

    console.rule("Theory note")
    console.print(
        "The exporter converts computational results into a chapter draft. "
        "This creates the first bridge from runnable model to manuscript text."
    )


if __name__ == "__main__":
    main()
