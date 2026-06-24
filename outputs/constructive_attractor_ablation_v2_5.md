# Constructive Attractor Ablation v2.5

## Purpose

This ablation test asks whether the constructive attractor is doing real explanatory work. If removing constructive support does not reduce apparent targeting, the model is too flexible.

## Thresholds

- Minimum targeting drop: 50.00%
- Minimum observer misreading drop: 40.00%
- Maximum unsupported targeting: 45.00
- Maximum shortcut targeting: 25.00
- Maximum tension well targeting: 20.00

## Cases

| Case | Role | Path | Constructive support | Tension penalty | Gateway penalty | Targeting | Misreading |
|---|---|---|---:|---:|---:|---:|---:|
| coherent_with_constructive_attractor | positive control | A → B → C → D → E | 0.95 | 0.00 | 0.00 | 92.75 | 87.65 |
| coherent_without_constructive_attractor | ablation case | A → B → C → D → E | 0.05 | 0.00 | 0.00 | 37.25 | 30.35 |
| shortcut_with_strained_gateway | gateway control | A → D → E | 0.10 | 0.00 | 0.60 | 16.25 | 14.75 |
| tension_well_injected | negative control | A → D → E | 0.05 | 0.80 | 0.00 | 0.00 | 0.00 |

## Ablation result

- Apparent targeting drop after removing constructive attractor: 59.84%
- Observer misreading drop after removing constructive attractor: 65.37%

## Findings

| Severity | Code | Message |
|---|---|---|
| info | ablation_passed | Constructive attractor removal reduced both apparent targeting and observer misreading beyond the required thresholds. |

## Interpretation

The constructive attractor passes this ablation test only if removing it causes a large drop in apparent targeting and observer misreading. This prevents the model from treating route shape alone as sufficient evidence of target-like organization.

## Boundary

This ablation test is conceptual and non-operational. It does not use real pathogens, real hosts, biological protocols, laboratory procedures, or executable interventions.
