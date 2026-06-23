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
        "how much does the projected causal story change?"
    )

    table = Table(title="Counterfactual deletion report")
    table.add_column("Deleted node")
    table.add_column("Base energy")
    table.add_column("New energy")
    table.add_column("Energy delta")
    table.add_column("Projection distance")
    table.add_column("Base order")
    table.add_column("New order")
    table.add_column("Interpretation")

    for node_id in fabric.nodes:
        result = counterfactual_delete(fabric, node_id)

        table.add_row(
            result.deleted_node,
            f"{result.base_energy:.3f}",
            f"{result.new_energy:.3f}",
            f"{result.energy_delta:.3f}",
            f"{result.order_distance:.3f}",
            " → ".join(result.base_order),
            " → ".join(result.new_order),
            result.interpretation,
        )

    console.print(table)

    console.rule("Theory note")
    console.print(
        "A node is not only important because it appears early in the projected timeline. "
        "It is important when deleting it destabilizes the fabric or changes the observer's story."
    )


if __name__ == "__main__":
    main()
