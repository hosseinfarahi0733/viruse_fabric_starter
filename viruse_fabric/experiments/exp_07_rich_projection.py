from __future__ import annotations

from rich.console import Console
from rich.table import Table

from viruse_fabric.causal.intervention import (
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


def print_rich_projection(title: str, events) -> None:
    table = Table(title=title)
    table.add_column("Node")
    table.add_column("Kind")
    table.add_column("Perceived time")
    table.add_column("Local tension")
    table.add_column("Intensity")
    table.add_column("Pressure")
    table.add_column("Curvature hint")
    table.add_column("Degree")

    for event in events:
        table.add_row(
            event.node_id,
            event.kind,
            f"{event.perceived_time:.3f}",
            f"{event.local_tension:.3f}",
            f"{event.perceived_intensity:.3f}",
            f"{event.fabric_pressure:.3f}",
            f"{event.curvature_hint:.3f}",
            str(event.degree),
        )

    console.print(table)


def compare_projection(base_fabric, new_fabric, label: str) -> None:
    simple_base = simple_order(base_fabric)
    simple_new = simple_order(new_fabric)
    simple_distance = simple_order_distance(simple_base, simple_new)

    rich_projector = RichObserverProjection()
    rich_base = rich_projector.project(base_fabric)
    rich_new = rich_projector.project(new_fabric)
    rich_distance = rich_projection_distance(rich_base, rich_new)

    console.rule(label)

    summary = Table(title="Simple vs rich projection distance")
    summary.add_column("Projection type")
    summary.add_column("Distance")
    summary.add_column("Interpretation")

    summary.add_row(
        "Simple order projection",
        f"{simple_distance:.3f}",
        "only checks whether perceived order changed",
    )
    summary.add_row(
        "Rich observer projection",
        f"{rich_distance:.3f}",
        "also detects tension, intensity, pressure, and curvature shifts",
    )

    console.print(summary)
    console.print(f"Simple order: {' → '.join(simple_base)}")
    console.print(f"New order:    {' → '.join(simple_new)}")

    print_rich_projection("Base rich projection", rich_base)
    print_rich_projection("New rich projection", rich_new)


def main() -> None:
    base_fabric = add_biological_spacetime_couplings(build_demo_fabric())

    spatial_intervention = shift_node_space(
        base_fabric,
        "B",
        dx=4.0,
        dy=2.0,
        dz=1.0,
    )

    t2_intervention = shift_node_time(
        base_fabric,
        "C",
        dt2=-10.0,
    )

    console.rule("Experiment 07: Rich Observer Projection")
    console.print(
        "Question: Can a richer observer projection reveal hidden fabric changes "
        "that simple event order fails to show?"
    )

    compare_projection(
        base_fabric,
        spatial_intervention,
        "Case 01: Spatial displacement of B",
    )

    compare_projection(
        base_fabric,
        t2_intervention,
        "Case 02: C shifted earlier on t2",
    )

    console.rule("Theory note")
    console.print(
        "Simple projection hides deep fabric changes when event order remains stable. "
        "Rich projection reveals that the observer's world should include intensity, "
        "pressure, tension, and curvature-like hints, not just sequence."
    )


if __name__ == "__main__":
    main()
