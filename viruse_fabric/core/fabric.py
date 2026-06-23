from __future__ import annotations

from dataclasses import dataclass, field
import copy
import networkx as nx

from viruse_fabric.core.node import EventNode
from viruse_fabric.core.constraint import Constraint


@dataclass
class Fabric:
    nodes: dict[str, EventNode] = field(default_factory=dict)
    constraints: list[Constraint] = field(default_factory=list)

    def add_node(self, node: EventNode) -> None:
        if node.node_id in self.nodes:
            raise ValueError(f"Duplicate node id: {node.node_id}")
        self.nodes[node.node_id] = node

    def add_constraint(self, constraint: Constraint) -> None:
        if constraint.source not in self.nodes or constraint.target not in self.nodes:
            raise KeyError("Constraint references missing node")
        self.constraints.append(constraint)

    def energy(self) -> float:
        total = 0.0
        for c in self.constraints:
            a = self.nodes[c.source]
            b = self.nodes[c.target]
            total += c.penalty(a, b)
        return total

    def without_node(self, node_id: str) -> "Fabric":
        f = copy.deepcopy(self)
        f.nodes.pop(node_id, None)
        f.constraints = [c for c in f.constraints if c.source != node_id and c.target != node_id]
        return f

    def to_networkx(self) -> nx.DiGraph:
        g = nx.DiGraph()
        for node in self.nodes.values():
            g.add_node(node.node_id, label=node.label, kind=node.kind)
        for c in self.constraints:
            g.add_edge(c.source, c.target, weight=c.weight, kind=c.kind)
        return g
