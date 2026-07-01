#!/usr/bin/env python3
"""Restricted bridge simulation sanity checks for VF-H2.

This is a computational sanity check only.

It checks finite restricted cases of:
    ledger_effect_size_R(x) = V_R(f_R(x)) - V_R(x)

Expected restricted behavior:
    x not in F_R => ledger_effect_size_R(x) > 0
    x in F_R     => ledger_effect_size_R(x) = 0

Boundary:
    - This is not a proof of the full Viruse Fabric theory.
    - This is not a proof of unrestricted TTP-VF-H2-004.
    - This is not empirical validation.
    - This is not biological validation.
"""

from __future__ import annotations

import csv
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


Coord = tuple[int, int]
State = tuple[int, ...]


@dataclass(frozen=True)
class SimulationCase:
    case_id: str
    n: int
    d: int
    active_coords: tuple[Coord, ...]
    h_mode: str


def coords_for_d(d: int) -> tuple[Coord, ...]:
    return tuple((t, i) for t in (1, 2, 3) for i in range(1, d + 1))


def make_h(n: int, mode: str) -> Callable[[int], int]:
    if mode == "increment_by_1":
        return lambda a: n if a >= n else a + 1
    if mode == "jump_to_top":
        return lambda a: n
    if mode == "increment_by_2_capped":
        return lambda a: n if a >= n else min(n, a + 2)
    raise ValueError(f"unknown h_mode: {mode}")


def state_space(n: int, d: int) -> list[State]:
    width = 3 * d
    return list(itertools.product(range(n + 1), repeat=width))


def fixed_set_membership(x: State, coords: tuple[Coord, ...], active: set[Coord], n: int) -> bool:
    index = {coord: idx for idx, coord in enumerate(coords)}
    return all(x[index[coord]] == n for coord in active)


def update_state(x: State, coords: tuple[Coord, ...], active: set[Coord], h: Callable[[int], int]) -> State:
    y = list(x)
    for idx, coord in enumerate(coords):
        if coord in active:
            y[idx] = h(x[idx])
    return tuple(y)


def v_r(x: State) -> int:
    return sum(x)


def run_case(case: SimulationCase) -> dict:
    coords = coords_for_d(case.d)
    active = set(case.active_coords)
    h = make_h(case.n, case.h_mode)

    total_states = 0
    fixed_states = 0
    nonfixed_states = 0
    positive_effect_count = 0
    zero_effect_count = 0
    violation_count = 0
    effect_values: list[int] = []
    violations: list[dict] = []

    for x in state_space(case.n, case.d):
        total_states += 1
        y = update_state(x, coords, active, h)
        effect = v_r(y) - v_r(x)
        in_fixed = fixed_set_membership(x, coords, active, case.n)

        effect_values.append(effect)

        if in_fixed:
            fixed_states += 1
            if effect == 0:
                zero_effect_count += 1
            else:
                violation_count += 1
                violations.append({
                    "state": x,
                    "updated_state": y,
                    "effect": effect,
                    "expected": "0 for fixed-set state",
                })
        else:
            nonfixed_states += 1
            if effect > 0:
                positive_effect_count += 1
            else:
                violation_count += 1
                violations.append({
                    "state": x,
                    "updated_state": y,
                    "effect": effect,
                    "expected": ">0 for non-fixed state",
                })

    return {
        "case_id": case.case_id,
        "n": case.n,
        "d": case.d,
        "active_coords": list(map(list, case.active_coords)),
        "h_mode": case.h_mode,
        "total_states": total_states,
        "fixed_states": fixed_states,
        "nonfixed_states": nonfixed_states,
        "positive_effect_count": positive_effect_count,
        "zero_effect_count": zero_effect_count,
        "min_effect": min(effect_values),
        "max_effect": max(effect_values),
        "violation_count": violation_count,
        "violations_sample": violations[:10],
        "passed": violation_count == 0,
    }


def main() -> int:
    out_dir = Path("outputs/simulations")
    out_dir.mkdir(parents=True, exist_ok=True)

    cases = [
        SimulationCase(
            case_id="RBSC-001-small-single-active",
            n=1,
            d=1,
            active_coords=((1, 1),),
            h_mode="increment_by_1",
        ),
        SimulationCase(
            case_id="RBSC-002-all-time-active",
            n=2,
            d=1,
            active_coords=((1, 1), (2, 1), (3, 1)),
            h_mode="increment_by_1",
        ),
        SimulationCase(
            case_id="RBSC-003-two-space-mixed-active",
            n=2,
            d=2,
            active_coords=((1, 1), (2, 1), (3, 2)),
            h_mode="jump_to_top",
        ),
        SimulationCase(
            case_id="RBSC-004-two-space-capped-increment",
            n=3,
            d=2,
            active_coords=((1, 1), (1, 2), (3, 1)),
            h_mode="increment_by_2_capped",
        ),
    ]

    case_results = [run_case(case) for case in cases]

    total_states_checked = sum(r["total_states"] for r in case_results)
    total_violations = sum(r["violation_count"] for r in case_results)

    result = {
        "artifact": "restricted_bridge_simulation_sanity_check",
        "scope": "restricted finite computational sanity check only",
        "theorem_checked": "RBRIDGE-VF-H2-001-R",
        "claim_checked": "x notin F_R => ledger_effect_size_R(x)>0; x in F_R => ledger_effect_size_R(x)=0",
        "not_full_viruse_fabric_theory_proof": True,
        "not_unrestricted_ttp_vf_h2_004_proof": True,
        "not_empirical_validation": True,
        "not_biological_validation": True,
        "total_cases": len(case_results),
        "total_states_checked": total_states_checked,
        "total_violations": total_violations,
        "passed": total_violations == 0,
        "cases": case_results,
    }

    json_path = out_dir / "restricted_bridge_simulation_results.json"
    csv_path = out_dir / "restricted_bridge_summary.csv"
    md_path = out_dir / "restricted_bridge_report.md"

    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "case_id",
                "n",
                "d",
                "h_mode",
                "total_states",
                "fixed_states",
                "nonfixed_states",
                "positive_effect_count",
                "zero_effect_count",
                "min_effect",
                "max_effect",
                "violation_count",
                "passed",
            ],
        )
        writer.writeheader()
        for r in case_results:
            writer.writerow({k: r[k] for k in writer.fieldnames})

    lines = [
        "# Restricted Bridge Simulation Sanity Check",
        "",
        "## Boundary",
        "",
        "This artifact is a restricted finite computational sanity check only.",
        "",
        "It is not a proof of the full Viruse Fabric theory.",
        "It is not a proof of unrestricted TTP-VF-H2-004.",
        "It is not empirical validation.",
        "It is not biological validation.",
        "",
        "## Checked restricted claim",
        "",
        "`ledger_effect_size_R(x)=V_R(f_R(x))-V_R(x)`",
        "",
        "- `x notin F_R => ledger_effect_size_R(x)>0`",
        "- `x in F_R => ledger_effect_size_R(x)=0`",
        "",
        "## Summary",
        "",
        f"- Total cases: {result['total_cases']}",
        f"- Total states checked: {result['total_states_checked']}",
        f"- Total violations: {result['total_violations']}",
        f"- Passed: {result['passed']}",
        "",
        "## Case table",
        "",
        "| Case | n | d | h_mode | states | fixed | nonfixed | violations | passed |",
        "|---|---:|---:|---|---:|---:|---:|---:|---|",
    ]

    for r in case_results:
        lines.append(
            f"| {r['case_id']} | {r['n']} | {r['d']} | {r['h_mode']} | "
            f"{r['total_states']} | {r['fixed_states']} | {r['nonfixed_states']} | "
            f"{r['violation_count']} | {r['passed']} |"
        )

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"restricted bridge simulation cases={len(case_results)} states={total_states_checked} violations={total_violations}")
    print(f"wrote {json_path}")
    print(f"wrote {csv_path}")
    print(f"wrote {md_path}")

    return 0 if total_violations == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
