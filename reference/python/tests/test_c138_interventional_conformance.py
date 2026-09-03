from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from itertools import product
from pathlib import Path

from vfh2_c138.cli import _render_report_bytes
from vfh2_c138.core import (
    BOOLEAN_DOMAIN,
    PAST_COPY_SCM,
    PRESENT_COPY_SCM,
    SCHEMA,
    BooleanTriTemporalSCM,
    _all_constraints,
    _all_models,
    _constraint_from_mask,
    _constraint_global_witness_exists,
    _constraint_mask,
    _model_from_masks,
    constraint_characterizes_future_law,
    constraint_contrast_witness_exists,
    do_present,
    full_interventional_conformance_report,
    law_graph,
    observationally_equivalent,
    present_causal_contrast_at,
    present_has_causal_effect_on_future,
    realize,
)


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "c138_interventional_conformance_report.json"


class InterventionalConformanceTests(unittest.TestCase):
    def test_canonical_order_and_named_models(self) -> None:
        self.assertEqual(SCHEMA, "vfh2.c138.interventional-conformance.v1")
        self.assertEqual(BOOLEAN_DOMAIN, (False, True))
        self.assertEqual(PAST_COPY_SCM.present_table, (False, True))
        self.assertEqual(
            PAST_COPY_SCM.future_table, (False, False, True, True)
        )
        self.assertEqual(PRESENT_COPY_SCM.present_table, (False, True))
        self.assertEqual(
            PRESENT_COPY_SCM.future_table, (False, True, False, True)
        )
        self.assertEqual(_constraint_mask(law_graph(PAST_COPY_SCM)), 0xA5)
        self.assertEqual(_constraint_mask(law_graph(PRESENT_COPY_SCM)), 0x99)

    def test_all_models_recover_one_graph_and_all_pointwise_cases(self) -> None:
        constraints = tuple(_all_constraints())
        qualified_pairs = 0
        qualified_cases = 0
        true_cases = 0
        for _, _, _, model in _all_models():
            graph = law_graph(model)
            matching = [
                (mask, constraint)
                for mask, constraint in constraints
                if constraint_characterizes_future_law(model, constraint)
            ]
            self.assertEqual(matching, [(_constraint_mask(graph), graph)])
            qualified_pairs += len(matching)
            for _, constraint in matching:
                for past, present_one, present_two in product(
                    BOOLEAN_DOMAIN, repeat=3
                ):
                    contrast = present_causal_contrast_at(
                        model, past, present_one, present_two
                    )
                    witness = constraint_contrast_witness_exists(
                        constraint, past, present_one, present_two
                    )
                    self.assertEqual(contrast, witness)
                    qualified_cases += 1
                    true_cases += int(contrast)
        self.assertEqual(qualified_pairs, 64)
        self.assertEqual(qualified_cases, 512)
        self.assertEqual(true_cases, 128)

    def test_all_qualified_global_cases_match(self) -> None:
        effectful = 0
        effectless = 0
        for _, _, _, model in _all_models():
            graph = law_graph(model)
            effect = present_has_causal_effect_on_future(model)
            self.assertEqual(effect, _constraint_global_witness_exists(graph))
            effectful += int(effect)
            effectless += int(not effect)
        self.assertEqual(effectful, 48)
        self.assertEqual(effectless, 16)

    def test_c134_parity_fixture(self) -> None:
        parity = _model_from_masks(2, 6)
        self.assertEqual(_constraint_mask(law_graph(parity)), 0x69)
        self.assertTrue(present_has_causal_effect_on_future(parity))
        for past, present_one, present_two in product(
            BOOLEAN_DOMAIN, repeat=3
        ):
            self.assertEqual(
                present_causal_contrast_at(
                    parity, past, present_one, present_two
                ),
                present_one is not present_two,
            )

    def test_c136_geometry_causality_fixtures(self) -> None:
        self.assertFalse(present_has_causal_effect_on_future(PAST_COPY_SCM))
        self.assertTrue(present_has_causal_effect_on_future(PRESENT_COPY_SCM))
        self.assertFalse(
            present_causal_contrast_at(PAST_COPY_SCM, False, False, True)
        )
        self.assertTrue(
            present_causal_contrast_at(PRESENT_COPY_SCM, False, False, True)
        )

    def test_c137_observational_nonidentifiability_fixture(self) -> None:
        self.assertTrue(
            observationally_equivalent(PAST_COPY_SCM, PRESENT_COPY_SCM)
        )
        for past in BOOLEAN_DOMAIN:
            self.assertEqual(realize(PAST_COPY_SCM, past), realize(PRESENT_COPY_SCM, past))
        self.assertEqual(do_present(PAST_COPY_SCM, False, True).future, False)
        self.assertEqual(
            do_present(PRESENT_COPY_SCM, False, True).future, True
        )
        self.assertEqual(do_present(PAST_COPY_SCM, True, False).future, True)
        self.assertEqual(
            do_present(PRESENT_COPY_SCM, True, False).future, False
        )

    def test_characterization_premise_is_necessary(self) -> None:
        empty = _constraint_from_mask(0)
        universal = _constraint_from_mask(255)
        self.assertFalse(
            constraint_characterizes_future_law(PRESENT_COPY_SCM, empty)
        )
        self.assertTrue(
            present_has_causal_effect_on_future(PRESENT_COPY_SCM)
        )
        self.assertFalse(_constraint_global_witness_exists(empty))
        self.assertFalse(
            constraint_characterizes_future_law(PAST_COPY_SCM, universal)
        )
        self.assertFalse(present_has_causal_effect_on_future(PAST_COPY_SCM))
        self.assertTrue(_constraint_global_witness_exists(universal))

    def test_equal_present_values_never_create_a_qualified_contrast(self) -> None:
        checked = 0
        for _, _, _, model in _all_models():
            graph = law_graph(model)
            for past, present in product(BOOLEAN_DOMAIN, repeat=2):
                self.assertFalse(
                    present_causal_contrast_at(
                        model, past, present, present
                    )
                )
                self.assertFalse(
                    constraint_contrast_witness_exists(
                        graph, past, present, present
                    )
                )
                checked += 1
        self.assertEqual(checked, 256)

    def test_exhaustive_report_has_frozen_coverage(self) -> None:
        report = full_interventional_conformance_report()
        audit = report["exhaustive_conformance"]
        self.assertTrue(audit["all_checks_pass"])
        self.assertEqual(audit["failures"], [])
        self.assertEqual(audit["counts"], audit["expected_counts"])
        self.assertEqual(
            audit["constraint_rectangle_defect_histogram"],
            {"0": 100, "1": 80, "2": 56, "3": 16, "4": 4},
        )
        self.assertEqual(
            audit["observation_class_size_histogram"], {"4": 16}
        )

    def test_frozen_report_is_byte_stable(self) -> None:
        self.assertEqual(_render_report_bytes(), FIXTURE.read_bytes())

    def test_cli_stdout_and_output_file_are_byte_stable(self) -> None:
        expected = FIXTURE.read_bytes()
        env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
        stdout = subprocess.run(
            [sys.executable, "-m", "vfh2_c138"],
            cwd=ROOT,
            env=env,
            check=True,
            capture_output=True,
        ).stdout
        self.assertEqual(stdout, expected)
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "report.json"
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "vfh2_c138",
                    "--output",
                    str(output),
                ],
                cwd=ROOT,
                env=env,
                check=True,
                capture_output=True,
            )
            self.assertEqual(output.read_bytes(), expected)

    def test_non_boolean_and_wrong_width_tables_are_rejected(self) -> None:
        with self.assertRaises(TypeError):
            BooleanTriTemporalSCM("bad-list", [False, True], (False,) * 4)
        with self.assertRaises(TypeError):
            BooleanTriTemporalSCM("bad-int", (False, 1), (False,) * 4)
        with self.assertRaises(ValueError):
            BooleanTriTemporalSCM("bad-width", (False,), (False,) * 4)
        with self.assertRaises(TypeError):
            constraint_characterizes_future_law(
                PAST_COPY_SCM, (False, False, False, False, False, False, False, 0)
            )
        with self.assertRaises(TypeError):
            present_causal_contrast_at(PAST_COPY_SCM, 0, False, True)


if __name__ == "__main__":
    unittest.main()
