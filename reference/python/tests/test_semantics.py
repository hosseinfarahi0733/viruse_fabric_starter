from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from itertools import product
from pathlib import Path

from vfh2_c133.core import (
    BOOLEAN_DOMAIN,
    PARITY_SCM,
    adjacent_chain_relation,
    all_rectangle_defects_zero,
    candidate_pasts,
    do_future,
    do_present,
    even_parity,
    even_parity_evidence,
    evidence_refines,
    flip_relation,
    full_semantic_report,
    middle_rectangle_closed,
    natural_rectangle_defect,
    realize,
    unconstrained_evidence,
)


ROOT = Path(__file__).resolve().parents[1]


class StructuralSemanticsTests(unittest.TestCase):
    def test_downstream_interventions_do_not_rewrite_past(self) -> None:
        for past, value in product(BOOLEAN_DOMAIN, repeat=2):
            self.assertEqual(do_present(PARITY_SCM, past, value).past, past)
            self.assertEqual(do_future(PARITY_SCM, past, value).past, past)

    def test_future_intervention_preserves_generated_present(self) -> None:
        for past, future in product(BOOLEAN_DOMAIN, repeat=2):
            self.assertEqual(
                do_future(PARITY_SCM, past, future).present,
                realize(PARITY_SCM, past).present,
            )

    def test_strict_candidate_past_refinement(self) -> None:
        weak = candidate_pasts(unconstrained_evidence, False, False)
        strong = candidate_pasts(even_parity_evidence, False, False)
        self.assertEqual(weak, (False, True))
        self.assertEqual(strong, (False,))
        self.assertLess(set(strong), set(weak))
        self.assertTrue(evidence_refines(even_parity_evidence, unconstrained_evidence))

    def test_parity_has_nonzero_rectangle_defect(self) -> None:
        defects = [
            natural_rectangle_defect(
                even_parity, past_one, past_two, present, future_one, future_two
            )
            for past_one, past_two, present, future_one, future_two in product(
                BOOLEAN_DOMAIN, repeat=5
            )
        ]
        self.assertIn(1, defects)
        self.assertFalse(all_rectangle_defects_zero(even_parity))
        self.assertFalse(middle_rectangle_closed(even_parity))

    def test_adjacent_chain_has_zero_rectangle_defect(self) -> None:
        self.assertTrue(all_rectangle_defects_zero(adjacent_chain_relation))
        self.assertTrue(middle_rectangle_closed(adjacent_chain_relation))

    def test_all_boolean_relations_satisfy_defect_equivalence(self) -> None:
        triples = list(product(BOOLEAN_DOMAIN, repeat=3))
        for mask in range(1 << len(triples)):
            table = {
                triple: bool(mask & (1 << index))
                for index, triple in enumerate(triples)
            }
            relation = lambda past, present, future, table=table: table[
                (past, present, future)
            ]
            self.assertEqual(
                all_rectangle_defects_zero(relation),
                middle_rectangle_closed(relation),
            )

    def test_bijective_boolean_renaming_preserves_defect_count(self) -> None:
        renamed = flip_relation(even_parity)
        original_count = 0
        renamed_count = 0
        for args in product(BOOLEAN_DOMAIN, repeat=5):
            original_count += natural_rectangle_defect(even_parity, *args)
            renamed_count += natural_rectangle_defect(renamed, *args)
        self.assertEqual(original_count, renamed_count)

    def test_report_matches_frozen_fixture(self) -> None:
        fixture = json.loads(
            (ROOT / "fixtures" / "c133_semantic_report.json").read_text("utf-8")
        )
        self.assertEqual(full_semantic_report(), fixture)

    def test_cli_roundtrip(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-m", "vfh2_c133"],
            cwd=ROOT,
            env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(json.loads(completed.stdout), full_semantic_report())


if __name__ == "__main__":
    unittest.main()
