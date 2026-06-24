from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math

import matplotlib.pyplot as plt


@dataclass(frozen=True)
class VisualNode:
    key: str
    label: str
    x: float
    y: float
    role: str


@dataclass(frozen=True)
class VisualEdge:
    source: str
    target: str
    label: str


@dataclass(frozen=True)
class ScenarioVisualSummary:
    scenario_name: str
    path: tuple[str, ...]
    apparent_targeting_score: float
    observer_misreading_score: float
    constructive_attractor: str | None
    tension_well: str | None
    strained_gateway: str | None
    interpretation: str


@dataclass(frozen=True)
class FabricDiagramResult:
    title: str
    image_path: str
    report_path: str
    scenario_count: int
    node_count: int
    edge_count: int
    interpretation: str


class FabricDiagramRenderer:
    title = "Viruse Fabric Visual Explanation v2.1"

    nodes: tuple[VisualNode, ...] = (
        VisualNode("A", "A\ncontact-like\nrole", 0.0, 0.0, "start"),
        VisualNode("B", "B\ncompatibility\ntransition", 1.2, 0.8, "transition"),
        VisualNode("C", "C\nregulatory\ncontext", 2.4, 0.8, "context"),
        VisualNode("D", "D\npersistence\nstabilization", 3.6, 0.0, "attractor"),
        VisualNode("E", "E\nvisible\noutcome", 4.8, 0.0, "outcome"),
    )

    edges: tuple[VisualEdge, ...] = (
        VisualEdge("A", "B", "possible transition"),
        VisualEdge("B", "C", "context alignment"),
        VisualEdge("C", "D", "stabilization route"),
        VisualEdge("D", "E", "visible projection"),
        VisualEdge("A", "D", "shortcut / forced passage"),
    )

    scenarios: tuple[ScenarioVisualSummary, ...] = (
        ScenarioVisualSummary(
            scenario_name="abstract_baseline",
            path=("A", "D", "E"),
            apparent_targeting_score=8.70,
            observer_misreading_score=40.44,
            constructive_attractor=None,
            tension_well=None,
            strained_gateway="D",
            interpretation=(
                "The visible route is structured but costly. D acts as a strained gateway, "
                "not as evidence of intention."
            ),
        ),
        ScenarioVisualSummary(
            scenario_name="coherent_viral_pattern",
            path=("A", "B", "C", "D", "E"),
            apparent_targeting_score=88.53,
            observer_misreading_score=91.21,
            constructive_attractor="D",
            tension_well=None,
            strained_gateway=None,
            interpretation=(
                "The full route becomes target-like because a constructive attractor stabilizes the path. "
                "This is route coherence, not intention."
            ),
        ),
        ScenarioVisualSummary(
            scenario_name="spatial_context_break",
            path=("A", "D", "E"),
            apparent_targeting_score=0.00,
            observer_misreading_score=13.95,
            constructive_attractor=None,
            tension_well="B",
            strained_gateway=None,
            interpretation=(
                "B becomes a tension well. The path avoids the crisis node instead of selecting it as a target."
            ),
        ),
        ScenarioVisualSummary(
            scenario_name="regulatory_time_disruption",
            path=("A", "D", "E"),
            apparent_targeting_score=0.00,
            observer_misreading_score=13.95,
            constructive_attractor=None,
            tension_well="C",
            strained_gateway=None,
            interpretation=(
                "C becomes a tension well. Crisis concentration should not be misread as causal intention."
            ),
        ),
    )

    def __init__(
        self,
        image_path: Path | None = None,
        report_path: Path | None = None,
    ) -> None:
        self.image_path = image_path or Path("outputs/fabric_diagram_v2_1.png")
        self.report_path = report_path or Path("outputs/visual_explanation_report_v2_1.md")

    def render(self) -> FabricDiagramResult:
        self.image_path.parent.mkdir(parents=True, exist_ok=True)
        self.report_path.parent.mkdir(parents=True, exist_ok=True)

        self._render_diagram()
        self.report_path.write_text(self.render_report_markdown(), encoding="utf-8")

        return FabricDiagramResult(
            title=self.title,
            image_path=str(self.image_path),
            report_path=str(self.report_path),
            scenario_count=len(self.scenarios),
            node_count=len(self.nodes),
            edge_count=len(self.edges),
            interpretation=(
                "The project now has a visual explanation layer connecting paths, "
                "attractor roles, apparent targeting, and observer misreading."
            ),
        )

    def _render_diagram(self) -> None:
        fig, ax = plt.subplots(figsize=(14, 8))

        node_by_key = {node.key: node for node in self.nodes}

        for edge in self.edges:
            source = node_by_key[edge.source]
            target = node_by_key[edge.target]
            self._draw_arrow(ax, source.x, source.y, target.x, target.y)
            self._draw_edge_label(ax, source, target, edge.label)

        for node in self.nodes:
            marker_size = self._marker_size_for(node.key)
            ax.scatter([node.x], [node.y], s=marker_size)
            ax.text(
                node.x,
                node.y + 0.18,
                node.label,
                ha="center",
                va="bottom",
                fontsize=10,
            )

        self._draw_path(ax, ("A", "B", "C", "D", "E"), y_offset=0.13, label="coherent route")
        self._draw_path(ax, ("A", "D", "E"), y_offset=-0.13, label="shortcut / disrupted route")

        self._draw_role_annotations(ax)

        ax.set_title(self.title)
        ax.set_xlim(-0.5, 5.3)
        ax.set_ylim(-0.8, 1.85)
        ax.set_xlabel("abstract causal route position")
        ax.set_ylabel("constraint alignment level")
        ax.grid(True, alpha=0.25)

        fig.tight_layout()
        fig.savefig(self.image_path, dpi=160)
        plt.close(fig)

    def _draw_arrow(
        self,
        ax,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
    ) -> None:
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops={"arrowstyle": "->", "lw": 1.2},
        )

    def _draw_edge_label(
        self,
        ax,
        source: VisualNode,
        target: VisualNode,
        label: str,
    ) -> None:
        mx = (source.x + target.x) / 2
        my = (source.y + target.y) / 2
        ax.text(mx, my - 0.12, label, ha="center", va="top", fontsize=8)

    def _draw_path(
        self,
        ax,
        path: tuple[str, ...],
        y_offset: float,
        label: str,
    ) -> None:
        node_by_key = {node.key: node for node in self.nodes}
        xs = [node_by_key[key].x for key in path]
        ys = [node_by_key[key].y + y_offset for key in path]

        ax.plot(xs, ys, linewidth=2.0, marker="o")
        if label == "coherent route":
            ax.text(4.55, 0.32, label, ha="center", va="center", fontsize=9)
        elif label == "shortcut / disrupted route":
            ax.text(4.25, -0.34, label, ha="center", va="center", fontsize=9)
        else:
            ax.text(xs[-1], ys[-1] + y_offset, label, ha="right", va="center", fontsize=9)

    def _draw_role_annotations(self, ax) -> None:
        ax.text(
            3.85,
            1.58,
            "D: constructive attractor in coherent pattern\nD: strained gateway in baseline",
            ha="center",
            va="center",
            fontsize=9,
        )
        ax.text(
            1.15,
            1.58,
            "B can become a tension well\nunder spatial context break",
            ha="center",
            va="center",
            fontsize=9,
        )
        ax.text(
            2.45,
            1.58,
            "C can become a tension well\nunder regulatory time disruption",
            ha="center",
            va="center",
            fontsize=9,
        )

    def _marker_size_for(self, node_key: str) -> float:
        # D is visually larger because it is the main constructive attractor / gateway in the examples.
        if node_key == "D":
            return 900.0
        if node_key in {"B", "C"}:
            return 650.0
        return 520.0

    def render_report_markdown(self) -> str:
        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This report connects the visual diagram to the computational story of Viruse Fabric. "
                "The figure is not decorative: it summarizes the same abstract route structure used in "
                "the apparent targeting and observer misreading experiments."
            ),
            "",
            f"![Fabric Diagram]({self.image_path.name})",
            "",
            "## Nodes",
            "",
            "| Node | Role | Diagram label |",
            "|---|---|---|",
        ]

        for node in self.nodes:
            clean_label = node.label.replace("\n", " / ")
            lines.append(f"| {node.key} | {node.role} | {clean_label} |")

        lines.extend(
            [
                "",
                "## Scenarios",
                "",
                "| Scenario | Path | Apparent targeting | Observer misreading | Constructive attractor | Tension well | Strained gateway |",
                "|---|---|---:|---:|---|---|---|",
            ]
        )

        for scenario in self.scenarios:
            lines.append(
                "| "
                f"{scenario.scenario_name} | "
                f"{' → '.join(scenario.path)} | "
                f"{scenario.apparent_targeting_score:.2f} | "
                f"{scenario.observer_misreading_score:.2f} | "
                f"{scenario.constructive_attractor or 'none'} | "
                f"{scenario.tension_well or 'none'} | "
                f"{scenario.strained_gateway or 'none'} |"
            )

        lines.extend(
            [
                "",
                "## Interpretation",
                "",
            ]
        )

        for scenario in self.scenarios:
            lines.extend(
                [
                    f"### {scenario.scenario_name}",
                    "",
                    scenario.interpretation,
                    "",
                ]
            )

        lines.extend(
            [
                "## Boundary",
                "",
                (
                    "The diagram is conceptual and non-operational. It does not describe real pathogens, "
                    "real hosts, laboratory protocols, biological mechanisms, or executable interventions."
                ),
                "",
                "## Theory Note",
                "",
                (
                    "A visual layer is useful only if it remains connected to computed paths, scores, and classifications. "
                    "Otherwise it becomes ornament. This version keeps the visual explanation tied to the earlier scenario results."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def approximate_visual_complexity(self) -> float:
        return math.log1p(len(self.nodes) * len(self.edges) * len(self.scenarios))
