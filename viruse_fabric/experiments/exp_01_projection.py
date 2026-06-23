from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table

from viruse_fabric.core.node import Coord6D, EventNode
from viruse_fabric.core.constraint import Constraint
from viruse_fabric.core.fabric import Fabric
from viruse_fabric.causal.causal_mass import compute_causal_mass
from viruse_fabric.simulation.projection import ObserverProjection
from viruse_fabric.theory.axioms import AXIOMS

console = Console()


def build_demo_fabric() -> Fabric:
    f = Fabric()

    # The exact labels are conceptual. This is not a real pathogen model.
    nodes = [
        EventNode("A", "contact-like physical event", Coord6D(0, 0, 0, 1.0, 6.0, 0.2), "physical"),
        EventNode("B", "cell-state transition", Coord6D(1, 0, 0, 2.0, 4.0, 0.4), "informational"),
        EventNode("C", "regulatory recontextualization", Coord6D(1, 1, 0, 3.0, 8.0, 2.5), "informational"),
        EventNode("D", "hereditary stabilization", Coord6D(2, 1, 1, 2.5, 9.0, 8.0), "hereditary"),
        EventNode("E", "observer-visible phenotype", Coord6D(2, 2, 1, 5.0, 7.0, 4.5), "projection"),
    ]
    for n in nodes:
        f.add_node(n)

    # Mixed directions create projection ambiguity but fabric-level coherence.
    f.add_constraint(Constraint("A", "B", "compatibility", weight=1.2, preferred_interval=1.5, tolerance=2.0, omega=(0.7, 0.2, 0.1)))
    f.add_constraint(Constraint("B", "C", "necessity", weight=1.8, preferred_interval=6.0, tolerance=2.5, omega=(0.2, 0.7, 0.1)))
    f.add_constraint(Constraint("C", "D", "necessity", weight=2.4, preferred_interval=35.0, tolerance=8.0, omega=(0.1, 0.2, 0.7)))
    f.add_constraint(Constraint("D", "E", "projection", weight=1.5, preferred_interval=8.0, tolerance=3.0, omega=(0.4, 0.2, 0.4)))
    f.add_constraint(Constraint("A", "D", "tension", weight=1.0, preferred_interval=45.0, tolerance=12.0, omega=(0.2, 0.1, 0.7)))
    return f


def print_axioms() -> None:
    console.rule("Viruse Fabric: axioms")
    for i, axiom in enumerate(AXIOMS, start=1):
        console.print(f"[bold]{i}.[/bold] {axiom}")


def print_projection(fabric: Fabric) -> None:
    projection = ObserverProjection(axis=(0.70, 0.20, 0.10)).project(fabric)
    table = Table(title="Observer projection: one perceived timeline")
    table.add_column("Order")
    table.add_column("Node")
    table.add_column("Event")
    table.add_column("Kind")
    table.add_column("Perceived time")
    for i, e in enumerate(projection, start=1):
        table.add_row(str(i), e.node_id, e.label, e.kind, f"{e.perceived_time:.3f}")
    console.print(table)


def print_causal_mass(fabric: Fabric) -> None:
    report = compute_causal_mass(fabric)
    table = Table(title=f"Causal mass report | base FabricEnergy = {report.base_energy:.3f}")
    table.add_column("Node")
    table.add_column("Causal mass")
    table.add_column("Interpretation")
    for node_id, mass in report.sorted():
        interp = "stabilizing / central" if mass > 0 else "tension/noise removing"
        table.add_row(node_id, f"{mass:.3f}", interp)
    console.print(table)


def save_plots(fabric: Fabric) -> None:
    out = Path("outputs")
    out.mkdir(exist_ok=True)

    projection = ObserverProjection(axis=(0.70, 0.20, 0.10)).project(fabric)
    plt.figure()
    y = list(range(len(projection)))
    x = [e.perceived_time for e in projection]
    labels = [e.node_id for e in projection]
    plt.scatter(x, y)
    for xi, yi, label in zip(x, y, labels):
        plt.text(xi, yi, f" {label}")
    plt.yticks([])
    plt.xlabel("Perceived one-time projection")
    plt.title("Projection compresses 3 times into one narrative")
    plt.tight_layout()
    plt.savefig(out / "projection_timeline.png", dpi=160)
    plt.close()

    mass = compute_causal_mass(fabric)
    items = mass.sorted()
    plt.figure()
    plt.bar([i[0] for i in items], [i[1] for i in items])
    plt.xlabel("Node")
    plt.ylabel("Causal mass")
    plt.title("Causal mass by node deletion")
    plt.tight_layout()
    plt.savefig(out / "causal_mass.png", dpi=160)
    plt.close()


def main() -> None:
    print_axioms()
    fabric = build_demo_fabric()
    console.rule("Fabric energy")
    console.print(f"FabricEnergy = [bold]{fabric.energy():.3f}[/bold]")
    print_projection(fabric)
    print_causal_mass(fabric)
    save_plots(fabric)
    console.print("\nSaved plots to [bold]outputs/[/bold]")


if __name__ == "__main__":
    main()
