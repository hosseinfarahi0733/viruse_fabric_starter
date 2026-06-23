from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.counterfactual import counterfactual_delete
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric

console = Console()


def main() -> None:
    fabric = build_demo_fabric()

    console.rule("Experiment 02: Counterfactual Deletion")
    console.print(
        "Question: If a node is removed from the full fabric, "
        "does it merely reduce raw tension, or does it damage the structure?"
    )

    table = Table(title="Counterfactual deletion report")
    table.add_column("Deleted")
    table.add_column("Raw ΔEnergy")
    table.add_column("Structural loss")
    table.add_column("Projection distance")
    table.add_column("Removed constraints")
    table.add_column("Impact")
    table.add_column("Interpretation")

    for node_id in fabric.nodes:
        result = counterfactual_delete(fabric, node_id)

        table.add_row(
            result.deleted_node,
            f"{result.raw_energy_delta:.3f}",
            f"{result.structural_loss:.3f}",
            f"{result.projection_distance:.3f}",
            str(result.removed_constraints),
            f"{result.counterfactual_impact:.3f}",
            result.interpretation,
        )

    console.print(table)

    console.rule("Theory note")
    console.print(
        "Raw energy can fall after deletion because constraints disappear. "
        "That does not mean the deleted node was unimportant. "
        "Counterfactual importance must combine tension relief, structural loss, "
        "and projection distortion."
    )


if __name__ == "__main__":
    main()
