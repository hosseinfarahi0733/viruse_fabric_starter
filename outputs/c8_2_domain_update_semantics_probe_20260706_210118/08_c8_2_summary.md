# C8.2 Domain/Update Semantics Probe

## Baseline

C8.1 classified:

```lean
restrictedParamsScoreKeyPreservingUpdateCondition p productUpdate productScore
```

as equivalent to:

```lean
∀ y : p.State, productScore (productUpdate y) = productScore y
```

## C8.2 question

Can pointwise score preservation be derived from existing domain/update semantics?

## Allowed outcomes

### Outcome A

A concrete update/domain semantic layer derives pointwise score preservation.

### Outcome B

No such semantic layer currently exists; pointwise score preservation remains a fundamental domain/update assumption.

## Boundary

This probe does not claim full VF-H2.

This probe does not derive hFixed.

This probe does not claim empirical validation.

This probe should not create a scientific tag unless a fundamental assumption is actually derived.
