from __future__ import annotations

from copy import deepcopy
import unittest

from viruse_fabric.safety.toy_fixture_catalog import get_fixture_catalog_payloads
from viruse_fabric.simulation.safe_abstract_toy_dynamics_kernel import (
    ToyKernelConfig,
    clamp01,
    run_toy_kernel,
    run_toy_kernel_catalog,
    summarize_kernel_results,
)


class TestSafeAbstractToyDynamicsKernel(unittest.TestCase):
    def test_clamp01_bounds_values(self) -> None:
        self.assertEqual(clamp01(-0.25), 0.0)
        self.assertEqual(clamp01(1.25), 1.0)
        self.assertEqual(clamp01(0.5), 0.5)

    def test_default_config_is_positive_step_count(self) -> None:
        config = ToyKernelConfig()
        self.assertGreater(config.step_count, 0)

    def test_single_fixture_kernel_result_is_in_range(self) -> None:
        fixture = get_fixture_catalog_payloads()[0]
        result = run_toy_kernel(fixture)
        self.assertTrue(result.passed_safety_guard)
        self.assertGreaterEqual(result.final_observation_score, 0.0)
        self.assertLessEqual(result.final_observation_score, 1.0)
        self.assertGreaterEqual(result.targeted_looking_pattern_score, 0.0)
        self.assertLessEqual(result.targeted_looking_pattern_score, 1.0)

    def test_catalog_execution_returns_three_results(self) -> None:
        fixtures = get_fixture_catalog_payloads()
        results = run_toy_kernel_catalog(fixtures)
        self.assertEqual(len(results), 3)

    def test_catalog_execution_all_pass_safety_guard(self) -> None:
        fixtures = get_fixture_catalog_payloads()
        results = run_toy_kernel_catalog(fixtures)
        self.assertTrue(all(result.passed_safety_guard for result in results))

    def test_summary_reports_three_results(self) -> None:
        fixtures = get_fixture_catalog_payloads()
        results = run_toy_kernel_catalog(fixtures)
        summary = summarize_kernel_results(results)
        self.assertEqual(summary["toy_kernel_result_count"], 3)
        self.assertTrue(summary["toy_kernel_all_safety_passed"])

    def test_summary_empty_results_is_safe_false(self) -> None:
        summary = summarize_kernel_results(())
        self.assertEqual(summary["toy_kernel_result_count"], 0)
        self.assertFalse(summary["toy_kernel_all_safety_passed"])

    def test_unsafe_fixture_is_rejected(self) -> None:
        fixture = deepcopy(get_fixture_catalog_payloads()[0])
        fixture["unsafe_marker"] = "operational_host_targeting toy synthetic abstract unitless non-operational"
        with self.assertRaises(ValueError):
            run_toy_kernel(fixture)

    def test_unknown_synthetic_location_is_rejected(self) -> None:
        fixture = deepcopy(get_fixture_catalog_payloads()[0])
        fixture["agents"][0]["location"] = "toy_unknown_node"
        with self.assertRaises(ValueError):
            run_toy_kernel(fixture)

    def test_kernel_execution_is_deterministic_for_same_fixture(self) -> None:
        fixture = get_fixture_catalog_payloads()[1]
        first = run_toy_kernel(fixture)
        second = run_toy_kernel(fixture)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
