#!/usr/bin/env python3
"""Generate proof status summary from the artifact index."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from common import REPORTS_DIR, ensure_reports_dir, infer_id_type, write_json_report
from extract_artifacts import build_index


def bool_to_status(value: Any) -> str:
    if value is True:
        return "proved"
    if value is False:
        return "not proved"
    if value is None:
        return "unknown"
    return str(value)


def first_bool(values: list[Any]) -> Any:
    for value in values:
        if isinstance(value, bool):
            return value
    return None


def generate() -> dict[str, Any]:
    ensure_reports_dir()
    index_path = REPORTS_DIR / "proof_artifacts_index.json"
    if index_path.exists():
        index = json.loads(index_path.read_text(encoding="utf-8"))
    else:
        index = build_index()

    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    for artifact in index.get("artifacts", []):
        source_file = artifact["file"]
        boundary_ok = bool(artifact.get("boundary_signal"))
        json_summary = artifact.get("json_summary") or {}
        targets = json_summary.get("targets") or {}
        proved_values = list((json_summary.get("proved_fields") or {}).values())
        proved_value = first_bool(proved_values)

        target_ids = [value for value in targets.values() if isinstance(value, str) and "VF-H2" in value]
        if not target_ids:
            target_ids = artifact.get("ids") or []

        for identifier in sorted(set(target_ids)):
            key = (identifier, source_file)
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "id": identifier,
                    "type": infer_id_type(identifier),
                    "proved": bool_to_status(proved_value),
                    "source": "json-target" if targets else "text-scan",
                    "boundary_ok": boundary_ok,
                    "file": source_file,
                }
            )

    rows.sort(key=lambda row: (row["id"], row["file"]))

    summary = {
        "tool": "generate_summary.py",
        "row_count": len(rows),
        "proved_count": sum(1 for row in rows if row["proved"] == "proved"),
        "not_proved_count": sum(1 for row in rows if row["proved"] == "not proved"),
        "unknown_count": sum(1 for row in rows if row["proved"] == "unknown"),
        "rows": rows,
    }
    write_json_report("proof_status_summary.json", summary)
    write_markdown(summary, REPORTS_DIR / "proof_status_summary.md")
    return summary


def write_markdown(summary: dict[str, Any], path: Path) -> None:
    lines = [
        "# Proof Status Summary",
        "",
        "Machine-generated summary. This is a consistency aid, not a new theorem. Because apparently files also need adult supervision.",
        "",
        f"- Rows: {summary['row_count']}",
        f"- Proved: {summary['proved_count']}",
        f"- Not proved: {summary['not_proved_count']}",
        f"- Unknown: {summary['unknown_count']}",
        "",
        "| ID | Type | Proved | Source | Boundary OK | File |",
        "|---|---|---:|---|---:|---|",
    ]
    for row in summary["rows"]:
        lines.append(
            "| {id} | {type} | {proved} | {source} | {boundary_ok} | `{file}` |".format(**row)
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary = generate()
    print(
        f"summary rows={summary['row_count']} proved={summary['proved_count']} "
        f"not_proved={summary['not_proved_count']} unknown={summary['unknown_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
