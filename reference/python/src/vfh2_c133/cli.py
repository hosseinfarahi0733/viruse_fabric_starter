from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import full_semantic_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Emit the exact VFH2 C133 semantic witness report."
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args(argv)
    rendered = json.dumps(full_semantic_report(), indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.write_text(rendered, encoding="utf-8")
    return 0
