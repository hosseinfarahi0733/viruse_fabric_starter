# Viruse Fabric Validation Protocol v2.4

## Purpose

This document defines how Viruse Fabric should be tested before it is presented as anything stronger than a conceptual-computational research prototype.

The goal is not to make the project look impressive. The goal is to identify what would make it fail.

## Current status

**Presentation status:** research prototype only

Viruse Fabric is currently suitable as a conceptual-computational research prototype. It is not yet suitable for strong public claims, empirical claims, or biological prediction.

## Validation criteria

| Criterion | Category | Priority | Question | Method | Pass signal | Fail signal |
|---|---|---|---|---|---|---|
| Constructive attractor ablation | ablation | high | Does apparent targeting drop when the constructive attractor is removed? | Compare a coherent constructive route against the same route after removing constructive support. | Apparent targeting and observer misreading decrease substantially. | The model still reports high targeting without a constructive attractor. |
| Tension well injection | stress test | high | Does the model avoid treating crisis concentration as intention? | Inject a tension well into B or C and check whether the path avoids it instead of promoting it to a target. | Targeting remains low and the path avoids the tension well. | The model turns a tension well into a strong target-like explanation. |
| Strained gateway penalty | stress test | high | Does the model distinguish forced passage from target-like organization? | Evaluate shortcut routes that pass through a strained gateway and compare them with coherent supported routes. | Shortcut routes remain low-targeting relative to coherent supported routes. | A costly gateway is misread as a constructive target. |
| Parameter sensitivity sweep | sensitivity | high | Are conclusions stable under reasonable changes in weights and thresholds? | Sweep scoring weights for path coverage, gravity alignment, constructive support, and penalties. | Rank ordering of core scenarios remains broadly stable. | Small parameter changes reverse the main interpretation. |
| Baseline comparison | baseline | high | Does the model outperform a trivial rule-based explanation? | Compare Viruse Fabric scoring against a simple baseline that labels any complete path as target-like. | Viruse Fabric rejects invalid and disrupted cases better than the trivial baseline. | The baseline performs equally well or better on stress scenarios. |
| Projection perturbation | observer model | medium | Can the same causal fabric produce different observer-facing readings under different projections? | Perturb observer visibility and salience assumptions while keeping the underlying path fixed. | Observer misreading changes while causal structure remains stable. | Observer misreading is insensitive to projection changes. |
| Negative control scenarios | negative control | high | Can the model avoid finding target-like structure where none should exist? | Generate incoherent routes with no constructive attractor and no stable path support. | Targeting and misreading remain low. | The model reports high targeting for incoherent unsupported routes. |
| External validation boundary | external validation | high | What kind of evidence would be needed before making stronger claims? | Define external datasets, competing models, or expert-coded scenario sets that could challenge the model. | The project clearly states that external validation is not yet complete. | The project presents internal simulations as empirical proof. |

## Failure conditions

- The model makes almost every scenario look target-like.
- The model makes no scenario look target-like, including coherent constructive routes.
- Removing constructive attractors does not reduce apparent targeting.
- Adding a tension well increases targeting instead of triggering avoidance or penalty.
- Small parameter changes reverse the main scenario ranking.
- A trivial baseline performs as well as the full model.
- Observer misreading does not respond to projection changes.
- The project claims empirical proof without external validation.

## Minimum bar before stronger presentation

Before the project deserves stronger public presentation, it should pass:

1. ablation tests;
2. parameter sensitivity sweeps;
3. negative control scenarios;
4. baseline comparison;
5. projection perturbation tests;
6. a clearly documented external validation plan.

## What would count as progress

Progress means the model becomes harder to fool. It should reject broken scenarios, remain stable under reasonable parameter variation, and outperform trivial baselines.

## What would count as failure

Failure means the model is too flexible. If it can explain every pattern after the fact, it explains nothing. If it cannot distinguish coherent constructive routes from crisis concentration, its central claim is not yet useful.

## Safety boundary

This validation protocol remains conceptual and non-operational. It does not use real pathogens, real hosts, doses, receptors, laboratory protocols, executable biological procedures, or deployable interventions.

## Interpretation

Viruse Fabric has internal structure, manuscript outputs, visual explanation, and internal stress tests. The next serious step is validation pressure: sensitivity, ablation, negative controls, and baselines.
