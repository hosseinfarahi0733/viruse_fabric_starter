#!/usr/bin/env python3
"""Extract proof artifact IDs, target fields, proved booleans, and OK markers."""
from __future__ import annotations

from typing import Any

from common import (
    BOUNDARY_FALSE_KEYS,
    PROVED_KEYS,
    TARGET_KEYS,
    extract_ids_from_text,
    extract_ok_markers,
    has_boundary_signal,
    iter_artifact_files,
    read_source,
    walk_json,
    write_json_report,
)


def scalar(value: Any) -> bool:
    return isinstance(value, (str, int, float, bool)) or value is None


def extract_from_json(data: Any) -> dict[str, Any]:
    targets: dict[str, Any] = {}
    proved_fields: dict[str, Any] = {}
    boundary_fields: dict[str, Any] = {}
    markers: list[str] = []

    for path, value in walk_json(data):
        if not path:
            continue
        key = path[-1]
        dotted = ".".join(path)
        if key in TARGET_KEYS and scalar(value):
            targets[dotted] = value
        if key in PROVED_KEYS and scalar(value):
            proved_fields[dotted] = value
        if key in BOUNDARY_FALSE_KEYS and scalar(value):
            boundary_fields[dotted] = value
        if isinstance(value, str) and value.endswith("_OK"):
            markers.append(value)
    return {
        "targets": targets,
        "proved_fields": proved_fields,
        "boundary_fields": boundary_fields,
        "ok_markers": sorted(set(markers)),
    }


def build_index() -> dict[str, Any]:
    artifacts: list[dict[str, Any]] = []
    all_ids: set[str] = set()
    all_markers: set[str] = set()

    for path in iter_artifact_files(include_reports=False):
        source = read_source(path)
        ids = extract_ids_from_text(source.text)
        ok_markers = extract_ok_markers(source.text)
        all_ids.update(ids)
        all_markers.update(ok_markers)

        json_summary: dict[str, Any] = {}
        if source.json_data is not None:
            json_summary = extract_from_json(source.json_data)
            for value in json_summary["targets"].values():
                if isinstance(value, str):
                    all_ids.update(extract_ids_from_text(value))
            all_markers.update(json_summary.get("ok_markers", []))

        artifacts.append(
            {
                "file": source.relpath,
                "json_valid": source.json_error is None,
                "json_error": source.json_error,
                "ids": ids,
                "ok_markers": ok_markers,
                "boundary_signal": has_boundary_signal(source),
                "json_summary": json_summary,
            }
        )

    index = {
        "tool": "extract_artifacts.py",
        "artifact_count": len(artifacts),
        "unique_id_count": len(all_ids),
        "unique_marker_count": len(all_markers),
        "unique_ids": sorted(all_ids),
        "unique_ok_markers": sorted(all_markers),
        "artifacts": artifacts,
    }
    write_json_report("proof_artifacts_index.json", index)
    return index


def main() -> int:
    index = build_index()
    print(
        f"indexed {index['artifact_count']} files; "
        f"unique_ids={index['unique_id_count']} ok_markers={index['unique_marker_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
