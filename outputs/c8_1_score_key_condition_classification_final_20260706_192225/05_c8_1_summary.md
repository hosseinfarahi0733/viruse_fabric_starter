# C8.1 Score-Key Condition Classification

## Result

C8.1 proves that restrictedParamsScoreKeyPreservingUpdateCondition is equivalent to pointwise score preservation.

Pointwise score preservation:

```lean
∀ y : p.State, productScore (productUpdate y) = productScore y
```

## Interpretation

This is an assumption-classification result.

The existential score-key condition is not stronger than pointwise score preservation; it is a factorized representation of it.

## Boundary

This does not derive score preservation from domain dynamics.

## Allowed claim

C8.1 classifies the score-key preservation assumption by proving equivalence with pointwise score preservation.

## Forbidden claim

C8.1 does not prove that score-key preservation follows from domain/update semantics.
