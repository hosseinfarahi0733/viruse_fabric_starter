from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import full_interventional_conformance_report


def _render_report_bytes() -> bytes:
    rendered = json.dumps(
        full_interventional_conformance_report(),
        indent=2,
        sort_keys=True,
        ensure_ascii=True,
    )
    return (rendered + "\n").encode("ascii")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Emit the exhaustive VFH2 C138 conformance report."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args(argv)
    rendered = _render_report_bytes()
    if args.output is None:
        sys.stdout.buffer.write(rendered)
    else:
        args.output.write_bytes(rendered)
    return 0
