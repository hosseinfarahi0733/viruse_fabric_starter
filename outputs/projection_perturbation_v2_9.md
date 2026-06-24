# Projection Perturbation v2.9

## Purpose

This projection perturbation test changes observer projection profiles while keeping intrinsic fabric scoring fixed. It tests whether apparent targeting and observer misreading remain distinguishable.

## Decision rule

- Target-like threshold: 60.00
- False-intention threshold: 60.00
- Minimum supported intrinsic margin: 25.00
- Minimum observer false-intention events: 4
- Maximum corrected false-intention events: 6
- Minimum correction drop percent: 50.00%

## Summary

- Cases tested: 6
- Projection profiles tested: 6
- Runs tested: 36
- Intrinsic false positives: 0
- Observer false-intention events: 22
- Corrected false-intention events: 3
- Correction drop percent: 86.36%
- Supported intrinsic margin: 46.50

## Case-level intrinsic scores

| Case | Expected label | Intrinsic score | Expected role |
|---|---|---:|---|
| supported_constructive_route | target_like | 92.75 | should remain intrinsically target-like |
| ablated_same_shape_route | negative_control | 38.45 | same shape without constructive support should not be intrinsically target-like |
| high_salience_decoy | projection_trap | 46.25 | should trigger observer misreading under salience-biased projections |
| smooth_story_shortcut | projection_trap | 44.60 | should test narrative smoothness as a false-intention source |
| tension_well_decoy | projection_trap | 34.75 | should test whether penalty blindness creates false attractors |
| strained_gateway_shortcut | negative_control | 15.00 | should stay low even under perturbed projection |

## Projection runs

| Case | Projection profile | Intrinsic | Observer misreading | Corrected misreading | False intention | Corrected false intention |
|---|---|---:|---:|---:|---|---|
| supported_constructive_route | balanced_observer | 92.75 | 92.50 | 90.70 | False | False |
| supported_constructive_route | salience_biased_observer | 92.75 | 100.00 | 98.31 | False | False |
| supported_constructive_route | shape_biased_observer | 92.75 | 100.00 | 98.31 | False | False |
| supported_constructive_route | story_biased_observer | 92.75 | 100.00 | 98.42 | False | False |
| supported_constructive_route | penalty_blind_observer | 92.75 | 97.62 | 95.71 | False | False |
| supported_constructive_route | constructive_blind_observer | 92.75 | 100.00 | 97.97 | False | False |
| ablated_same_shape_route | balanced_observer | 38.45 | 55.62 | 21.42 | False | False |
| ablated_same_shape_route | salience_biased_observer | 38.45 | 66.93 | 34.87 | True | False |
| ablated_same_shape_route | shape_biased_observer | 38.45 | 80.36 | 48.29 | True | False |
| ablated_same_shape_route | story_biased_observer | 38.45 | 78.65 | 48.72 | True | False |
| ablated_same_shape_route | penalty_blind_observer | 38.45 | 65.06 | 28.73 | True | False |
| ablated_same_shape_route | constructive_blind_observer | 38.45 | 73.04 | 34.56 | True | False |
| high_salience_decoy | balanced_observer | 46.25 | 71.96 | 37.40 | True | False |
| high_salience_decoy | salience_biased_observer | 46.25 | 100.00 | 67.60 | True | True |
| high_salience_decoy | shape_biased_observer | 46.25 | 91.80 | 59.40 | True | False |
| high_salience_decoy | story_biased_observer | 46.25 | 100.00 | 69.76 | True | True |
| high_salience_decoy | penalty_blind_observer | 46.25 | 86.33 | 49.61 | True | False |
| high_salience_decoy | constructive_blind_observer | 46.25 | 95.21 | 56.33 | True | False |
| smooth_story_shortcut | balanced_observer | 44.60 | 63.85 | 28.14 | True | False |
| smooth_story_shortcut | salience_biased_observer | 44.60 | 85.94 | 52.46 | True | False |
| smooth_story_shortcut | shape_biased_observer | 44.60 | 86.22 | 52.74 | True | False |
| smooth_story_shortcut | story_biased_observer | 44.60 | 92.80 | 61.55 | True | True |
| smooth_story_shortcut | penalty_blind_observer | 44.60 | 79.87 | 41.92 | True | False |
| smooth_story_shortcut | constructive_blind_observer | 44.60 | 86.14 | 45.97 | True | False |
| tension_well_decoy | balanced_observer | 34.75 | 53.42 | 14.18 | False | False |
| tension_well_decoy | salience_biased_observer | 34.75 | 80.07 | 43.28 | True | False |
| tension_well_decoy | shape_biased_observer | 34.75 | 71.20 | 34.41 | True | False |
| tension_well_decoy | story_biased_observer | 34.75 | 78.39 | 44.06 | True | False |
| tension_well_decoy | penalty_blind_observer | 34.75 | 72.50 | 30.81 | True | False |
| tension_well_decoy | constructive_blind_observer | 34.75 | 76.32 | 32.18 | True | False |
| strained_gateway_shortcut | balanced_observer | 15.00 | 25.42 | 0.00 | False | False |
| strained_gateway_shortcut | salience_biased_observer | 15.00 | 39.56 | 0.00 | False | False |
| strained_gateway_shortcut | shape_biased_observer | 15.00 | 41.73 | 1.91 | False | False |
| strained_gateway_shortcut | story_biased_observer | 15.00 | 40.18 | 3.01 | False | False |
| strained_gateway_shortcut | penalty_blind_observer | 15.00 | 43.16 | 0.00 | False | False |
| strained_gateway_shortcut | constructive_blind_observer | 15.00 | 42.11 | 0.00 | False | False |

## Findings

| Severity | Code | Message |
|---|---|---|
| warning | observer_false_intention_detected | Projection perturbation produced 22 observer false-intention events. |
| warning | residual_false_intention_after_correction | Correction left 3 residual false-intention events. |

## Interpretation

The test passes only if intrinsic fabric scoring avoids false positives while projection shifts can still produce observer false-intention events. The correction layer should then reduce those false readings.

## Boundary

This projection perturbation analysis is conceptual and non-operational. It does not use real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions.
