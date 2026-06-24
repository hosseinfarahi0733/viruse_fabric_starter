# Parameter Sensitivity Sweep v2.6

## Purpose

This sensitivity sweep tests whether the main validation result depends on one fragile weight setting. A useful model should remain stable under moderate scoring-weight perturbations.

## Thresholds

- Minimum stability rate: 80.00%
- Maximum ablated route score: 50.00
- Maximum shortcut route score: 35.00
- Maximum tension well route score: 25.00

## Summary

- Profiles tested: 729
- Stable profiles: 729
- Unstable profiles: 0
- Stability rate: 100.00%

## Representative stable runs

| Profile | Top case | Supported | Ablated | Shortcut | Tension well | Stable |
|---|---|---:|---:|---:|---:|---|
| profile_001 | supported_constructive_route | 74.20 | 29.80 | 13.00 | 0.00 | True |
| profile_002 | supported_constructive_route | 74.20 | 29.80 | 10.00 | 0.00 | True |
| profile_003 | supported_constructive_route | 74.20 | 29.80 | 7.00 | 0.00 | True |
| profile_004 | supported_constructive_route | 76.00 | 30.40 | 13.80 | 0.00 | True |
| profile_005 | supported_constructive_route | 76.00 | 30.40 | 10.80 | 0.00 | True |
| profile_006 | supported_constructive_route | 76.00 | 30.40 | 7.80 | 0.00 | True |
| profile_007 | supported_constructive_route | 77.80 | 31.00 | 14.60 | 0.00 | True |
| profile_008 | supported_constructive_route | 77.80 | 31.00 | 11.60 | 0.00 | True |
| profile_009 | supported_constructive_route | 77.80 | 31.00 | 8.60 | 0.00 | True |
| profile_010 | supported_constructive_route | 76.75 | 30.85 | 13.90 | 0.00 | True |
| profile_011 | supported_constructive_route | 76.75 | 30.85 | 10.90 | 0.00 | True |
| profile_012 | supported_constructive_route | 76.75 | 30.85 | 7.90 | 0.00 | True |

## Findings

| Severity | Code | Message |
|---|---|---|
| info | sensitivity_passed | The scenario ranking and key thresholds remained stable across all tested weight profiles. |

## Interpretation

The sensitivity sweep passes only if the supported constructive route remains dominant and disrupted or unsupported cases do not become strongly target-like under moderate perturbations.

## Boundary

This sensitivity analysis is conceptual and non-operational. It does not use real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions.
