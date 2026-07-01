#!/usr/bin/env python3
"""Validate VF-H2 proof artifacts.

What this catches:
- malformed JSON in outputs/
- unsafe positive claims such as "full theory proved"
- JSON booleans that incorrectly mark empirical/biological/full validation as true
- proof-like artifacts that lack boundary signals, reported as warnings by default

Boundary warnings are intentionally not fatal unless --strict-boundary is used.
The validator should stop real overclaim, not punish sentences like
"not empirically validated". Humanity has invented enough brittle greps already.
"""
from __future__ import annotations

import argparse
import sys
from typing import Any

from common import (
    find_unsafe_json_claims,
    find_unsafe_text_claims,
    has_boundary_signal,
    is_proof_like,
    iter_artifact_files,
    read_source,
    write_json_report,
)


def validate(strict_boundary: bool = False) -> tuple[int, dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    file_reports: list[dict[str, Any]] = []

    paths = iter_artifact_files(include_reports=False)
    for path in paths:
        source = read_source(path)
        source_report: dict[str, Any] = {
            "file": source.relpath,
            "json_valid": source.json_error is None,
            "proof_like": is_proof_like(source),
            "boundary_signal": has_boundary_signal(source),
            "unsafe_claims": [],
        }

        if source.json_error:
            errors.append({"file": source.relpath, "error_type": "invalid_json", "detail": source.json_error})

        unsafe_claims = find_unsafe_text_claims(source) + find_unsafe_json_claims(source)
        source_report["unsafe_claims"] = unsafe_claims
        for claim in unsafe_claims:
            errors.append({"file": source.relpath, "error_type": "unsafe_claim", **claim})

        if source_report["proof_like"] and not source_report["boundary_signal"]:
            issue = {
                "file": source.relpath,
                "warning_type": "missing_boundary_signal",
                "detail": "Proof-like artifact lacks an explicit restricted/not-full/not-validated boundary signal.",
            }
            if strict_boundary:
                errors.append({"error_type": "strict_boundary_failure", **issue})
            else:
                warnings.append(issue)

        file_reports.append(source_report)

    report = {
        "tool": "validate_artifacts.py",
        "artifact_file_count": len(paths),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "passed": len(errors) == 0,
        "strict_boundary": strict_boundary,
        "errors": errors,
        "warnings": warnings,
        "files": file_reports,
    }
    write_json_report("boundary_claims_report.json", report)
    return (0 if len(errors) == 0 else 1), report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-boundary", action="store_true", help="Fail when proof-like files lack boundary signals.")
    args = parser.parse_args()

    code, report = validate(strict_boundary=args.strict_boundary)
    print(
        f"validated {report['artifact_file_count']} artifact files; "
        f"errors={report['error_count']} warnings={report['warning_count']}"
    )
    if report["errors"]:
        for error in report["errors"][:20]:
            print(f"ERROR: {error}", file=sys.stderr)
    if report["warnings"]:
        for warning in report["warnings"][:20]:
            print(f"WARNING: {warning}", file=sys.stderr)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
