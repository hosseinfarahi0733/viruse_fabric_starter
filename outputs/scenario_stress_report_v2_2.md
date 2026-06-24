# Scenario Stress Tests v2.2

## Purpose

This report stress-tests the internal logic of Viruse Fabric. It does not validate the model against external empirical data. Instead, it checks whether core relationships remain sane under disrupted, unsupported, and deliberately invalid scenarios.

## Stress Scenarios

| Scenario | Expected | Path | Targeting | Misreading | Constructive attractor | Tension well | Strained gateway |
|---|---|---|---:|---:|---|---|---|
| baseline_strained_gateway | valid | A → D → E | 8.70 | 40.44 | none | none | D |
| coherent_constructive_route | valid | A → B → C → D → E | 88.53 | 91.21 | D | none | none |
| constructive_attractor_removed | valid | A → B → C → D → E | 18.00 | 33.00 | none | none | none |
| spatial_tension_well_avoidance | valid | A → D → E | 0.00 | 13.95 | none | B | none |
| regulatory_tension_well_avoidance | valid | A → D → E | 0.00 | 13.95 | none | C | none |
| invalid_everything_looks_targeted | invalid | A → D → E | 95.00 | 92.00 | none | B | D |
| invalid_coherent_route_scores_zero | invalid | A → B → C → D → E | 0.00 | 0.00 | D | none | none |

## Findings

| Scenario | Severity | Code | Message |
|---|---|---|---|
| invalid_everything_looks_targeted | info | invalid_case_rejected | Invalid case rejected: high targeting without constructive attractor; tension well case given high targeting; strained gateway misread as strong target |
| invalid_coherent_route_scores_zero | info | invalid_case_rejected | Invalid case rejected: coherent constructive route scored near zero |

## Interpretation

A healthy model should not make everything look target-like. It should also not flatten every scenario into zero meaning. The useful region is between these failures: coherent constructive routes may appear target-like, while tension wells, unsupported routes, and strained gateways should not be automatically promoted to intention.

## Boundary

This stress test is conceptual and non-operational. It does not use real pathogens, real hosts, biological protocols, or executable interventions.
