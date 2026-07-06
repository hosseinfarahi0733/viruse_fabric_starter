# VF-H2 / Viruse Fabric — Dependency Graph after v17.4.0

## Purpose

This file gives the current conceptual dependency graph.

It is intentionally conservative. It does not claim that full VF-H2 is proved.

## Main v17.4 route

```text
ProductRestrictedParams
        |
        v
canonicalRestrictedTypedUpdate
canonicalRestrictedTypedScore
        |
        v
natural base interval assumptions
        |
        +-- hThreshold
        +-- hFixed
        +-- restrictedParamsScoreKeyPreservingUpdateCondition
        |
        v
NaturalUpdatedBounds
        |
        v
BaseAndUpdatedScoreWindowTarget
        |
        v
ScorePreservingUpdateWindowTarget
        |
        v
ScorePreservationDischargeTarget
        |
        v
PolicyEndToEndScoreWindowTarget
        |
        v
restrictedProofSpineTarget
```

## Main theorem

```lean
VFH2.ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_scoreKeyCondition_naturalBase_to_restrictedProofSpineTarget
```

## Sanity route

```lean
VFH2.ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_identityLikeUpdate_naturalBase_to_restrictedProofSpineTarget
```

Interpretation:

```text
This is a weak sanity route, not the main scientific route.
```

## Legacy route

Legacy route shape:

```text
old canonical/base-effect route
+ strong reversed score-window assumptions
→ collapsed score window
→ proof-spine target
```

Problem:

```text
The old route proves a target under assumptions that force threshold collapse.
```

Therefore:

```text
legacy route = formally useful history / boundary evidence
main route   = full natural restricted proof-spine route
```

## Dependency risk ranking

```text
High risk:
- score-key preservation
- hFixed

Medium risk:
- natural base interval source
- threshold calibration

Low risk:
- hThreshold
- canonical typed update/score construction
```

## Candidate minimal core

Candidate core after v17.4.0:

```text
1. ProductRestrictedParamsFullNaturalProofSpine.lean
2. ProductRestrictedParamsNaturalUpdatedBounds.lean
3. ProductRestrictedParamsScorePreservingUpdate.lean
4. ProductRestrictedParamsScoreWindow.lean
5. ProductRestrictedParamsCanonicalRawEqualities.lean
```

This is only a candidate.

A real minimal core requires import-level and theorem-level dependency audit.
