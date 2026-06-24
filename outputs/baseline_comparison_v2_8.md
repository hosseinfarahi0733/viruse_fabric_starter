# Baseline Comparison v2.8

## Purpose

This baseline comparison asks whether Viruse Fabric does more explanatory work than a simple route-shape baseline, observer-salience baseline, efficiency baseline, or reduced linear baseline.

## Decision rule

- Target-like threshold: 60.00
- Minimum Viruse Fabric separation margin: 25.00
- Minimum weaker-baseline count: 2
- Negative controls should not cross the target-like threshold.

## Model summary

| Model | Top case | Supported score | Strongest rival | Separation margin | False positive count | Passed discrimination |
|---|---|---:|---:|---:|---:|---|
| viruse_fabric | supported_constructive_route | 92.75 | 48.60 | 44.15 | 0 | True |
| route_shape_baseline | supported_constructive_route | 94.10 | 83.00 | 11.10 | 4 | False |
| observer_salience_baseline | high_salience_ablated_decoy | 92.40 | 96.20 | -3.80 | 3 | False |
| efficiency_baseline | supported_constructive_route | 91.50 | 77.00 | 14.50 | 4 | False |
| reduced_linear_baseline | supported_constructive_route | 64.25 | 49.50 | 14.75 | 0 | False |

## Case scores

| Case | Expected label | Viruse Fabric | Route-shape baseline | Observer-salience baseline | Efficiency baseline | Reduced linear baseline |
|---|---|---:|---:|---:|---:|---:|
| supported_constructive_route | target_like | 92.75 | 94.10 | 92.40 | 91.50 | 64.25 |
| ablated_route | negative_control | 37.25 | 79.10 | 50.40 | 66.50 | 35.75 |
| shortcut_gateway_route | negative_control | 16.25 | 47.50 | 44.50 | 42.50 | 28.25 |
| tension_well_route | negative_control | 0.00 | 34.00 | 36.50 | 30.00 | 18.50 |
| high_salience_ablated_decoy | negative_control | 47.85 | 80.90 | 96.20 | 73.50 | 46.65 |
| high_path_shortcut_decoy | negative_control | 48.60 | 83.00 | 78.00 | 77.00 | 49.50 |
| low_penalty_tension_decoy | negative_control | 39.55 | 70.40 | 78.20 | 68.00 | 46.80 |

## Findings

| Severity | Code | Message |
|---|---|---|
| warning | route_shape_baseline_weaker_than_fabric | route_shape_baseline failed discrimination: top=supported_constructive_route, false positives=4, margin=11.10. |
| warning | observer_salience_baseline_weaker_than_fabric | observer_salience_baseline failed discrimination: top=high_salience_ablated_decoy, false positives=3, margin=-3.80. |
| warning | efficiency_baseline_weaker_than_fabric | efficiency_baseline failed discrimination: top=supported_constructive_route, false positives=4, margin=14.50. |
| warning | reduced_linear_baseline_weaker_than_fabric | reduced_linear_baseline failed discrimination: top=supported_constructive_route, false positives=0, margin=14.75. |

## Interpretation

Viruse Fabric passes this comparison only if it ranks the supported constructive route highest, keeps negative controls below the target-like threshold, and preserves a clear separation margin. A useful baseline test should expose false positive behavior in simpler models.

## Boundary

This baseline comparison is conceptual and non-operational. It does not use real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions.
