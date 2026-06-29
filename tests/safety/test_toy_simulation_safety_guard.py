from __future__ import annotations

import unittest

from viruse_fabric.safety.toy_simulation_safety_guard import (
    PROHIBITED_CATEGORY_MARKERS,
    PROHIBITED_PHRASE_MARKERS,
    REQUIRED_SAFE_MARKERS,
    assert_text_safe,
    build_safe_toy_fixture,
    check_fixture_safety,
    check_text_safety,
    collect_guard_summary,
    normalize_text,
)


class TestToySimulationSafetyGuard(unittest.TestCase):
    def test_safe_text_passes(self) -> None:
        text = "toy synthetic abstract unitless non-operational content"
        result = check_text_safety(text)
        self.assertTrue(result.passed)
        self.assertEqual(result.blocked_markers, ())
        self.assertEqual(result.missing_safe_markers, ())

    def test_safe_fixture_passes(self) -> None:
        fixture = build_safe_toy_fixture()
        result = check_fixture_safety(fixture)
        self.assertTrue(result.passed)
        self.assertEqual(result.blocked_markers, ())
        self.assertEqual(result.missing_safe_markers, ())

    def test_required_safe_markers_are_enforced(self) -> None:
        text = "toy synthetic abstract"
        result = check_text_safety(text)
        self.assertFalse(result.passed)
        self.assertIn("unitless", result.missing_safe_markers)
        self.assertIn("non-operational", result.missing_safe_markers)

    def test_prohibited_category_markers_are_blocked(self) -> None:
        for marker in PROHIBITED_CATEGORY_MARKERS:
            with self.subTest(marker=marker):
                text = f"{marker} toy synthetic abstract unitless non-operational"
                result = check_text_safety(text)
                self.assertFalse(result.passed)
                self.assertIn(marker, result.blocked_markers)

    def test_prohibited_phrase_markers_are_blocked(self) -> None:
        for marker in PROHIBITED_PHRASE_MARKERS:
            with self.subTest(marker=marker):
                text = f"{marker} toy synthetic abstract unitless non-operational"
                result = check_text_safety(text)
                self.assertFalse(result.passed)
                self.assertIn(marker, result.blocked_markers)

    def test_assert_text_safe_accepts_safe_text(self) -> None:
        assert_text_safe("toy synthetic abstract unitless non-operational content")

    def test_assert_text_safe_rejects_blocked_text(self) -> None:
        with self.assertRaises(ValueError):
            assert_text_safe(
                "operational_host_targeting toy synthetic abstract unitless non-operational"
            )

    def test_normalization_handles_underscores_and_case(self) -> None:
        normalized = normalize_text("Toy_SYNTHETIC Abstract")
        self.assertIn("toy synthetic", normalized)
        self.assertIn("abstract", normalized)

    def test_guard_summary_is_consistent(self) -> None:
        summary = collect_guard_summary()
        self.assertEqual(summary["prohibited_category_marker_count"], 11)
        self.assertEqual(summary["prohibited_phrase_marker_count"], 8)
        self.assertEqual(summary["required_safe_marker_count"], 5)
        self.assertTrue(summary["safe_fixture_passed"])
        self.assertEqual(summary["safe_fixture_blocked_markers"], ())
        self.assertEqual(summary["safe_fixture_missing_safe_markers"], ())

    def test_required_safe_marker_set_is_stable(self) -> None:
        self.assertEqual(
            set(REQUIRED_SAFE_MARKERS),
            {"toy", "synthetic", "abstract", "unitless", "non-operational"},
        )


if __name__ == "__main__":
    unittest.main()
