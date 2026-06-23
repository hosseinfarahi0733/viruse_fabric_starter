from __future__ import annotations

from dataclasses import dataclass

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.intervention import (
    compare_intervention,
    shift_node_space,
    shift_node_time,
)
from viruse_fabric.experiments.exp_01_projection import build_demo_fabric
from viruse_fabric.geometry.spacetime_coupling import add_biological_spacetime_couplings
from viruse_fabric.simulation.projection import ObserverProjection
from viruse_fabric.simulation.rich_projection import (
    RichObserverProjection,
    rich_projection_distance,
)

console = Console()


@dataclass
class RichCriticalResult:
    name: str
    energy_delta: float
    simple_distance: float
    rich_distance: float

    @property
    def interpretation(self) -> str:
        if abs(self.energy_delta) >= 10 and self.simple_distance <= 0.15 and self.rich_distance >= 1.0:
            return "hidden fabric change resolved by rich projection"
        if abs(self.energy_delta) >= 10 and self.rich_distance < 0.5:
            return "fabric change still poorly projected"
        if self.rich_distance >= 1.0:
            return "rich projection detects meaningful observer-level change"
        return "limited visible change"


def simple_order(fabric):
    return [event.node_id for event in ObserverProjection().project(fabric)]


def simple_order_distance(base_order, new_order) -> float:
    common = [node for node in base_order if node in new_order]

    if len(common) <= 1:
        return 1.0

    base_rank = {node: i for i, node in enumerate(base_order)}
    new_rank = {node: i for i, node in enumerate(new_order)}

    total = 0.0
    max_possible = max(len(base_order) - 1, 1)

    for node in common:
        total += abs(base_rank[node] - new_rank[node])

    missing_penalty = len(set(base_order) - set(new_order)) / max(len(base_order), 1)

    return (total / (len(common) * max_possible)) + missing_penalty


def compare_rich_projection(base_fabric, new_fabric, name: str) -> RichCriticalResult:
    simple_base = simple_order(base_fabric)
    simple_new = simple_order(new_fabric)
    simple_distance = simple_order_distance(simple_base, simple_new)

    rich_projector = RichObserverProjection()
    rich_base = rich_projector.project(base_fabric)
    rich_new = rich_projector.project(new_fabric)
    rich_distance = rich_projection_distance(rich_base, rich_new)

    comparison = compare_intervention(
        name=name,
        description=name,
        base=base_fabric,
        intervened=new_fabric,
    )

    return RichCriticalResult(
        name=name,
        energy_delta=comparison.energy_delta,
        simple_distance=simple_distance,
        rich_distance=rich_distance,
    )


def main() -> None:
    fabric = add_biological_spacetime_couplings(build_demo_fabric())

    scenarios = [
        compare_rich_projection(
            fabric,
            shift_node_space(fabric, "B", dx=4.0, dy=2.0, dz=1.0),
            "B_spatial_displaced_with_coupling",
        ),
        compare_rich_projection(
            fabric,
            shift_node_time(fabric, "C", dt2=-10.0),
            "C_t2_earlier_with_coupling",
        ),
        compare_rich_projection(
            fabric,
            shift_node_time(fabric, "D", dt3=-9.0),
            "D_t3_earlier_with_coupling",
        ),
    ]

    console.rule("Experiment 08: Rich Critical Review")
    console.print(
        "Question: Does rich projection resolve the hidden-fabric-change warning?"
    )

    table = Table(title="Rich critical projection review")
    table.add_column("Scenario")
    table.add_column("ΔEnergy")
    table.add_column("Simple distance")
    table.add_column("Rich distance")
    table.add_column("Interpretation")

    resolved = 0
    unresolved = 0

    for result in scenarios:
        if result.interpretation == "hidden fabric change resolved by rich projection":
            resolved += 1
        elif abs(result.energy_delta) >= 10 and result.rich_distance < 0.5:
            unresolved += 1

        table.add_row(
            result.name,
            f"{result.energy_delta:.3f}",
            f"{result.simple_distance:.3f}",
            f"{result.rich_distance:.3f}",
            result.interpretation,
        )

    console.print(table)

    console.rule("Rich projection verdict")

    if unresolved == 0 and resolved > 0:
        verdict = "rich projection resolves the main hidden-change warning"
        score = 2.0
    elif unresolved > 0:
        verdict = "rich projection helps but does not fully resolve hidden changes"
        score = 5.0
    else:
        verdict = "no strong hidden-change cases detected"
        score = 1.0

    console.print(f"Resolved cases: {resolved}")
    console.print(f"Unresolved cases: {unresolved}")
    console.print(f"Score: {score:.1f}")
    console.print(f"Verdict: {verdict}")

    console.rule("Theory note")
    console.print(
        "The hidden-fabric-change warning is not necessarily a failure of the fabric model. "
        "It may be a failure of an impoverished observer projection. "
        "Rich projection turns hidden changes into measurable observer-level pressure."
    )


if __name__ == "__main__":
    main()
