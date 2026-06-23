from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.biology.viral_scenarios import build_viral_pattern_scenarios
from viruse_fabric.simulation.observer_misreading import ObserverMisreadingEngine

console = Console()


def main() -> None:
    engine = ObserverMisreadingEngine()
    scenarios = build_viral_pattern_scenarios()

    results = [
        engine.analyze(scenario.fabric, case_name=scenario.name)
        for scenario in scenarios
    ]

    console.rule("Experiment 15: Observer Misreading Engine")
    console.print(
        "Question: When does an observer mistake route coherence for intention?"
    )

    table = Table(title="Observer misreading risk")
    table.add_column("Scenario")
    table.add_column("Path")
    table.add_column("Targeting score")
    table.add_column("Misreading score")
    table.add_column("Path visibility")
    table.add_column("Compression")
    table.add_column("Attractor bias")
    table.add_column("Intention projection")
    table.add_column("Interpretation")

    for result in results:
        table.add_row(
            result.case_name,
            " → ".join(result.path),
            f"{result.apparent_targeting_score:.2f}",
            f"{result.misreading_score:.2f}",
            f"{result.pathway_visibility:.3f}",
            f"{result.narrative_compression:.3f}",
            f"{result.dominant_attractor_bias:.3f}",
            f"{result.intention_projection:.3f}",
            result.interpretation,
        )

    console.print(table)

    detail = Table(title="Narrative correction")
    detail.add_column("Scenario")
    detail.add_column("Inferred story")
    detail.add_column("Corrected reading")
    detail.add_column("Crisis penalty")
    detail.add_column("Strained penalty")

    for result in results:
        detail.add_row(
            result.case_name,
            result.inferred_story,
            result.corrected_reading,
            f"{result.crisis_confusion_penalty:.3f}",
            f"{result.strained_route_penalty:.3f}",
        )

    console.print(detail)

    console.rule("Theory note")
    console.print(
        "Observer misreading occurs when route coherence, endpoint visibility, "
        "and dominant attractors are compressed into a story of intention. "
        "The correction is to read intention-like behavior as constraint-filtered path selection."
    )


if __name__ == "__main__":
    main()
