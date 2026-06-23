from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.intervention import (
    compare_intervention,
    scale_constraint_weight,
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric

console = Console()


def main() -> None:
    fabric = build_demo_fabric()

    scenarios = [
        compare_intervention(
            name="C_t2_earlier",
            description="Move regulatory recontextualization earlier on t2.",
            base=fabric,
            intervened=shift_node_time(fabric, "C", dt2=-10.0),
        ),
        compare_intervention(
            name="D_t3_earlier",
            description="Move hereditary stabilization earlier on t3.",
            base=fabric,
            intervened=shift_node_time(fabric, "D", dt3=-9.0),
        ),
        compare_intervention(
            name="A_D_tension_weaker",
            description="Weaken the long A→D tension constraint.",
            base=fabric,
            intervened=scale_constraint_weight(
                fabric,
                source="A",
                target="D",
                kind="tension",
                factor=0.20,
            ),
        ),
        compare_intervention(
            name="B_spatial_displaced",
            description="Move B away in physical space without changing time.",
            base=fabric,
            intervened=shift_node_space(fabric, "B", dx=4.0, dy=2.0, dz=1.0),
        ),
    ]

    console.rule("Experiment 03: Intervention Engine")
    console.print(
        "Question: If we intervene on a node or relation without deleting it, "
        "does the fabric or observer projection reorganize?"
    )

    table = Table(title="Intervention report")
    table.add_column("Intervention")
    table.add_column("ΔEnergy")
    table.add_column("Projection distance")
    table.add_column("Base order")
    table.add_column("New order")
    table.add_column("Interpretation")

    for result in scenarios:
        table.add_row(
            result.name,
            f"{result.energy_delta:.3f}",
            f"{result.projection_distance:.3f}",
            " → ".join(result.base_order),
            " → ".join(result.new_order),
            result.interpretation,
        )

    console.print(table)

    console.rule("Theory note")
    console.print(
        "Deletion asks whether a node is necessary. "
        "Intervention asks whether changing a coordinate or relation reorganizes the fabric. "
        "This is closer to causal testing than simply observing a projected timeline."
    )


if __name__ == "__main__":
    main()
