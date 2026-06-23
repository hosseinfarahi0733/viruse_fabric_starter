from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Severity = Literal["low", "medium", "high"]


@dataclass
class CriticalFinding:
    code: str
    severity: Severity
    title: str
    evidence: str
    interpretation: str
    recommendation: str


class CriticalEngine:
    """A small self-critique engine for Viruse Fabric.

    This does not decide whether the theory is true.
    It only points at places where the current model might be fooling us.
    Which is rude, but useful. Like a good reviewer with fewer coffee stains.
    """

    def __init__(self) -> None:
        self.findings: list[CriticalFinding] = []

    def add(
        self,
        *,
        code: str,
        severity: Severity,
        title: str,
        evidence: str,
        interpretation: str,
        recommendation: str,
    ) -> None:
        self.findings.append(
            CriticalFinding(
                code=code,
                severity=severity,
                title=title,
                evidence=evidence,
                interpretation=interpretation,
                recommendation=recommendation,
            )
        )

    def evaluate_counterfactuals(self, results) -> None:
        high_structural_negative_energy = [
            r for r in results
            if r.raw_energy_delta < 0 and r.structural_loss >= 7
        ]

        if high_structural_negative_energy:
            nodes = ", ".join(r.deleted_node for r in high_structural_negative_energy)
            self.add(
                code="CF-RAW-ENERGY-TRAP",
                severity="high",
                title="Raw energy decrease can hide structural importance",
                evidence=(
                    f"Deleting node(s) {nodes} reduced raw FabricEnergy, "
                    "but structural loss remained high."
                ),
                interpretation=(
                    "A lower energy after deletion does not necessarily mean the deleted node was unimportant. "
                    "It may mean the model erased constraints together with the node."
                ),
                recommendation=(
                    "Continue reporting structural loss and projection distortion alongside raw energy. "
                    "Never interpret FabricEnergy alone."
                ),
            )

        low_impact_projection_nodes = [
            r for r in results
            if r.counterfactual_impact < 3 and r.projection_distance <= 0.25
        ]

        if low_impact_projection_nodes:
            nodes = ", ".join(r.deleted_node for r in low_impact_projection_nodes)
            self.add(
                code="CF-PROJECTION-NOISE",
                severity="medium",
                title="Some observer-visible nodes may be weakly structural",
                evidence=(
                    f"Node(s) {nodes} had low counterfactual impact and low projection distortion."
                ),
                interpretation=(
                    "A node may appear in the observer timeline while contributing little to the deeper fabric."
                ),
                recommendation=(
                    "Mark these nodes as projection-level or phenotype-level until stronger constraints justify them."
                ),
            )

    def evaluate_interventions(self, results) -> None:
        hidden_fabric_changes = [
            r for r in results
            if abs(r.energy_delta) >= 10 and r.projection_distance <= 0.15
        ]

        if hidden_fabric_changes:
            names = ", ".join(r.name for r in hidden_fabric_changes)
            self.add(
                code="INT-HIDDEN-FABRIC-CHANGE",
                severity="high",
                title="Large fabric change with small observer projection change",
                evidence=(
                    f"Intervention(s) {names} strongly changed FabricEnergy but barely changed projected order."
                ),
                interpretation=(
                    "The observer timeline may hide deep changes in the full 3-time fabric."
                ),
                recommendation=(
                    "Add non-order projection metrics, such as perceived intensity, causal tension, or curvature."
                ),
            )

        spatially_weak = [
            r for r in results
            if "spatial" in r.name.lower() and abs(r.energy_delta) < 0.1
        ]

        if spatially_weak:
            names = ", ".join(r.name for r in spatially_weak)
            self.add(
                code="INT-WEAK-SPACE-COUPLING",
                severity="high",
                title="Spatial coupling appears under-modeled",
                evidence=(
                    f"Spatial intervention(s) {names} produced almost no fabric effect."
                ),
                interpretation=(
                    "The MVP currently gives more causal weight to time-like coordinates than to physical space."
                ),
                recommendation=(
                    "Strengthen space-time coupling, tissue geometry, and biology-space constraints in the next version."
                ),
            )

        stabilizing_relation_changes = [
            r for r in results
            if r.energy_delta < -1 and "weaker" in r.name.lower()
        ]

        if stabilizing_relation_changes:
            names = ", ".join(r.name for r in stabilizing_relation_changes)
            self.add(
                code="INT-TENSION-RELATION",
                severity="medium",
                title="Some relations may add tension rather than structure",
                evidence=(
                    f"Weakening relation intervention(s) {names} reduced FabricEnergy."
                ),
                interpretation=(
                    "Not every relation should be treated as causal support. Some relations may be unstable, over-weighted, or poorly typed."
                ),
                recommendation=(
                    "Separate compatibility, necessity, tension, and projection constraints more strictly."
                ),
            )

    def evaluate_model_balance(self, *, intervention_results) -> None:
        time_effects = [
            abs(r.energy_delta)
            for r in intervention_results
            if "_t2_" in r.name or "_t3_" in r.name
        ]

        space_effects = [
            abs(r.energy_delta)
            for r in intervention_results
            if "spatial" in r.name.lower()
        ]

        if time_effects and space_effects:
            avg_time = sum(time_effects) / len(time_effects)
            avg_space = sum(space_effects) / len(space_effects)

            if avg_time > 100 * max(avg_space, 1e-9):
                self.add(
                    code="MODEL-TIME-DOMINANCE",
                    severity="high",
                    title="The current MVP is dominated by time-axis interventions",
                    evidence=(
                        f"Average time intervention effect ≈ {avg_time:.3f}, "
                        f"average spatial intervention effect ≈ {avg_space:.3f}."
                    ),
                    interpretation=(
                        "The model may be proving that we coded time strongly, not that time truly dominates the theory."
                    ),
                    recommendation=(
                        "Introduce stronger spatial constraints before making strong theoretical claims about time dominance."
                    ),
                )

    def summary_score(self) -> float:
        weight = {"low": 1.0, "medium": 2.0, "high": 3.0}
        return sum(weight[f.severity] for f in self.findings)

    def verdict(self) -> str:
        score = self.summary_score()

        if score >= 9:
            return "model needs revision before strong theoretical claims"
        if score >= 5:
            return "model is promising but requires targeted correction"
        if score > 0:
            return "model has minor cautions"
        return "no major critical warnings detected"
