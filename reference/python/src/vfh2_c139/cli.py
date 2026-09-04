from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .core import audit_manifest, canonical_json_bytes, load_manifest_bytes


def render_report_bytes(manifest_path: Path) -> bytes:
    raw = manifest_path.read_bytes()
    manifest = load_manifest_bytes(raw)
    return canonical_json_bytes(audit_manifest(manifest, manifest_bytes=raw))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Replay the outcome-free VFH2 C139 ImmPort metadata audit."
    )
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    rendered = render_report_bytes(args.manifest)
    if args.output is None:
        sys.stdout.buffer.write(rendered)
    else:
        args.output.write_bytes(rendered)
    return 0
