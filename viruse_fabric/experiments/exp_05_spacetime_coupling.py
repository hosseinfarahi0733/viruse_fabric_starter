from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.intervention import (
    compare_intervention,
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric
from viruse_fabric.geometry.spacetime_coupling import (
    add_biological_spacetime_couplings,
)

console = Console()


def main() -> None:
    base_fabric = build_demo_fabric()
    coupled_fabric = add_biological_spacetime_couplings(base_fabric)

    base_spatial = compare_intervention(
        name="B_spatial_displaced_without_coupling",
        description="Move B in space using the original MVP fabric.",
        base=base_fabric,
        intervened=shift_node_space(base_fabric, "B", dx=4.0, dy=2.0, dz=1.0),
    )

    coupled_spatial = compare_intervention(
        name="B_spatial_displaced_with_coupling",
        description="Move B in space after adding biological space-time coupling.",
        base=coupled_fabric,
        intervened=shift_node_space(coupled_fabric, "B", dx=4.0, dy=2.0, dz=1.0),
    )

    coupled_c_t2 = compare_intervention(
        name="C_t2_earlier_with_coupling",
        description="Move C earlier on informational time t2 after coupling.",
        base=coupled_fabric,
        intervened=shift_node_time(coupled_fabric, "C", dt2=-10.0),
    )

    coupled_d_t3 = compare_intervention(
        name="D_t3_earlier_with_coupling",
        description="Move D earlier on hereditary time t3 after coupling.",
        base=coupled_fabric,
        intervened=shift_node_time(coupled_fabric, "D", dt3=-9.0),
    )

    scenarios = [
        base_spatial,
        coupled_spatial,
        coupled_c_t2,
        coupled_d_t3,
    ]

    console.rule("Experiment 05: Space-Time Coupling Fix")
    console.print(
        "Question: Can explicit biological space-time coupling make spatial displacement matter?"
    )

    table = Table(title="Space-time coupling intervention report")
    table.add_column("Scenario")
    table.add_column("Base energy")
    table.add_column("New energy")
    table.add_column("ΔEnergy")
    table.add_column("Projection distance")
    table.add_column("Interpretation")

    for result in scenarios:
        table.add_row(
            result.name,
            f"{result.base_energy:.3f}",
            f"{result.new_energy:.3f}",
            f"{result.energy_delta:.3f}",
            f"{result.projection_distance:.3f}",
            result.interpretation,
        )

    console.print(table)

    console.rule("Comparison")
    console.print(
        f"Spatial displacement before coupling: ΔEnergy = {base_spatial.energy_delta:.3f}"
    )
    console.print(
        f"Spatial displacement after coupling:  ΔEnergy = {coupled_spatial.energy_delta:.3f}"
    )

    improvement = abs(coupled_spatial.energy_delta) - abs(base_spatial.energy_delta)
    console.print(f"Spatial sensitivity gain: {improvement:.3f}")

    console.rule("Theory note")
    console.print(
        "The original MVP treated space as almost decorative. "
        "Adding biological space-time coupling makes spatial coherence part of fabric stability. "
        "This directly responds to the Critical Engine warning about weak space coupling."
    )


if __name__ == "__main__":
    main()
