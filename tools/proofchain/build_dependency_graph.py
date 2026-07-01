#!/usr/bin/env python3
"""Build a lightweight dependency graph for VF-H2 proof artifacts."""
from __future__ import annotations

import re
from typing import Any

from common import (
    DEPENDENCY_KEYS,
    TARGET_KEYS,
    extract_ids_from_text,
    iter_artifact_files,
    read_source,
    walk_json,
    write_json_report,
)

SECTION_HINT_RE = re.compile(
    r"(?:prior anchors?|dependencies|uses|required inputs?|inputs verified|frozen anchors?)",
    re.I,
)


def ids_from_value(value: Any) -> set[str]:
    ids: set[str] = set()
    if isinstance(value, str):
        ids.update(extract_ids_from_text(value))
    elif isinstance(value, dict):
        for item in value.values():
            ids.update(ids_from_value(item))
    elif isinstance(value, list):
        for item in value:
            ids.update(ids_from_value(item))
    return ids


def json_targets_and_deps(data: Any) -> tuple[set[str], set[str]]:
    targets: set[str] = set()
    deps: set[str] = set()
    for path, value in walk_json(data):
        if not path:
            continue
        key = path[-1]
        if key in TARGET_KEYS:
            targets.update(ids_from_value(value))
        if key in DEPENDENCY_KEYS:
            deps.update(ids_from_value(value))
    return targets, deps


def text_section_deps(text: str) -> set[str]:
    deps: set[str] = set()
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if SECTION_HINT_RE.search(line):
            block = "\n".join(lines[idx : idx + 25])
            deps.update(extract_ids_from_text(block))
    return deps


def build_graph() -> dict[str, Any]:
    nodes: set[str] = set()
    edges: set[tuple[str, str, str]] = set()
    file_records: list[dict[str, Any]] = []

    for path in iter_artifact_files(include_reports=False):
        source = read_source(path)
        ids = set(extract_ids_from_text(source.text))
        targets: set[str] = set()
        deps: set[str] = set()

        if source.json_data is not None:
            json_targets, json_deps = json_targets_and_deps(source.json_data)
            targets.update(json_targets)
            deps.update(json_deps)

        deps.update(text_section_deps(source.text))
        nodes.update(ids | targets | deps)

        if not targets and ids:
            # Conservative fallback: use the first ID as artifact target only when no structured target exists.
            targets.add(sorted(ids)[0])

        for target in targets:
            for dep in deps:
                if dep != target:
                    edges.add((dep, target, source.relpath))

        file_records.append(
            {
                "file": source.relpath,
                "targets": sorted(targets),
                "dependencies": sorted(deps),
                "ids": sorted(ids),
            }
        )

    graph = {
        "tool": "build_dependency_graph.py",
        "node_count": len(nodes),
        "edge_count": len(edges),
        "nodes": sorted(nodes),
        "edges": [
            {"from": src, "to": dst, "source_file": file}
            for src, dst, file in sorted(edges)
        ],
        "files": file_records,
    }
    write_json_report("proof_dependency_graph.json", graph)
    write_dot(graph)
    return graph


def dot_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def write_dot(graph: dict[str, Any]) -> None:
    from common import REPORTS_DIR

    lines = ["digraph proof_dependency_graph {", "  rankdir=LR;"]
    for node in graph["nodes"]:
        lines.append(f'  "{dot_escape(node)}";')
    for edge in graph["edges"]:
        label = dot_escape(edge["source_file"])
        lines.append(f'  "{dot_escape(edge["from"])}" -> "{dot_escape(edge["to"])}" [label="{label}"];')
    lines.append("}")
    (REPORTS_DIR / "proof_dependency_graph.dot").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    graph = build_graph()
    print(f"dependency graph nodes={graph['node_count']} edges={graph['edge_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
