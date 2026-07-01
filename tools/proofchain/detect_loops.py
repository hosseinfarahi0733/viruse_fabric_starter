#!/usr/bin/env python3
"""Detect plan/execute/audit/final-status loops in git history.

Default behavior is warning-only. Use --fail-on-loop only when you are emotionally
prepared for CI to judge the commit history. Which, honestly, is what it deserves.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from typing import Any

from common import write_json_report

PATTERNS = {
    "plan": re.compile(r"\bplan\b", re.I),
    "execute": re.compile(r"\bexecute\b|\bexecution\b", re.I),
    "audit": re.compile(r"\baudit\b", re.I),
    "final_status": re.compile(r"\bfinal[-\s]?status\b", re.I),
}


def git_subjects(limit: int) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "log", f"-n{limit}", "--pretty=%s"],
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception as exc:  # noqa: BLE001
        return [f"GIT_LOG_UNAVAILABLE: {type(exc).__name__}: {exc}"]
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def classify(subject: str) -> set[str]:
    return {name for name, pattern in PATTERNS.items() if pattern.search(subject)}


def detect(subjects: list[str]) -> dict[str, Any]:
    classified = [{"subject": subject, "classes": sorted(classify(subject))} for subject in subjects]
    counts = {name: sum(1 for item in classified if name in item["classes"]) for name in PATTERNS}

    # git log returns newest first; reverse to chronological order for sequence checks.
    chronological = list(reversed(classified))
    class_sequence = [item["classes"][0] for item in chronological if item["classes"]]
    sequence_text = " > ".join(class_sequence)

    loop_signals: list[dict[str, Any]] = []
    if re.search(r"plan > execute > audit > execute", sequence_text):
        loop_signals.append({"type": "plan_execute_audit_execute_sequence", "sequence": sequence_text})
    if re.search(r"plan > execute > audit > final_status > execute", sequence_text):
        loop_signals.append({"type": "plan_execute_audit_final_status_execute_sequence", "sequence": sequence_text})

    total_loopish = counts["plan"] + counts["execute"] + counts["audit"] + counts["final_status"]
    if total_loopish >= 8 and counts["execute"] >= 2 and counts["audit"] >= 1:
        loop_signals.append({"type": "high_loopish_commit_density", "counts": counts})

    report = {
        "tool": "detect_loops.py",
        "checked_commit_subjects": len(subjects),
        "counts": counts,
        "loop_signal_count": len(loop_signals),
        "loop_signals": loop_signals,
        "classified_subjects": classified,
    }
    write_json_report("proofchain_loop_report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--warn-only", action="store_true", help="Always exit 0, even when loop signals are found.")
    mode.add_argument("--fail-on-loop", action="store_true", help="Exit 1 when loop signals are found.")
    parser.add_argument("--limit", type=int, default=200)
    args = parser.parse_args()

    report = detect(git_subjects(args.limit))
    print(f"loop signals={report['loop_signal_count']} counts={report['counts']}")
    for signal in report["loop_signals"]:
        print(f"WARNING: loop signal: {signal}")

    if args.fail_on_loop and report["loop_signal_count"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
