# VF-H2 / Viruse Fabric — Milestone Value Policy after v17.4.0

## Old metric

The old implicit metric was:

```text
more theorem count = more progress
```

This is no longer acceptable.

## New metric

A milestone has scientific value only if it does at least one of the following:

```text
1. removes a fundamental assumption
2. derives a fundamental assumption from a semantic layer
3. sharply classifies a fundamental assumption
4. discovers and documents a meaningful negative result
5. reduces the trusted core
6. clarifies the theory boundary in a reviewer-relevant way
```

## Documentation milestone

The reviewer-response documentation pack is valuable because it clarifies:

```text
- theory target
- assumptions
- dependency graph
- proof debt
- limits
- negative results
- milestone policy
```

But it should not be presented as a scientific proof milestone.

## Scientific milestone candidates

### Candidate S1 — Score-key derivation

```text
Derive restrictedParamsScoreKeyPreservingUpdateCondition from update/score/domain semantics.
```

Value:

```text
very high
```

### Candidate S2 — Fixedness derivation

```text
Derive hFixed from fixed-set/update semantics.
```

Value:

```text
very high
```

### Candidate S3 — Natural interval source

```text
Derive or justify the natural base interval assumptions from calibration/domain constraints.
```

Value:

```text
high
```

### Candidate S4 — Minimal core

```text
Produce a verified minimal core dependency graph.
```

Value:

```text
medium to high
```

## Tag policy

Allowed scientific tag:

```text
Only after assumption reduction, derivation, or sharp classification.
```

Not allowed:

```text
tag for documentation-only commit
tag for wrapper theorem
tag for failed probe unless it is documented as a negative result with clear value
```
