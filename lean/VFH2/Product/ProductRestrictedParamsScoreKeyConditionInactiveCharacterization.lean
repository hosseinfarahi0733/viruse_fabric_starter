import VFH2.Product.ProductUpdateFiberCharacterization
import VFH2.Product.ProductRestrictedParamsActiveInsensitiveScore
import VFH2.Product.ProductRestrictedParamsScoreKeyConditionClassification
import VFH2.Product.ProductRestrictedParamsInactiveCoordScore

/-!
# Exact Score-Key Condition for the Restricted Product Update

For the concrete restricted Product update, the existing score-key preservation
condition is not an opaque extra policy assumption: it holds exactly when the
score depends only on coordinates that the update leaves inactive.

The reverse direction is substantive. Pointwise score preservation makes the
score constant on every update fiber, while the established fiber
characterization identifies those fibers exactly with agreement on inactive
coordinates.

Boundary:
- This theorem is specific to `ProductRestrictedParams` and
  `productUpdateState`.
- It classifies the score-preservation obligation; it does not claim that every
  score satisfies it.
- It introduces no new assumptions, score definition, compatibility API, or
  workflow.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace ProductRestrictedParamsScoreKeyConditionInactiveCharacterization

/--
For the concrete restricted Product update, the score-key preservation
condition is equivalent to inactive-coordinate score semantics.
-/
theorem restrictedParams_productUpdateState_scoreKeyCondition_iff_inactiveInsensitive
    (p : ProductRestrictedParams)
    (productScore : p.State → Int) :
    ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
          p
          (productUpdateState p)
          productScore
      ↔
    ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
      p productScore := by
  constructor
  · intro hScoreKey
    have hPreserved :
        ∀ y : p.State,
          productScore (productUpdateState p y) = productScore y :=
      (ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyCondition_iff_policyPoint
          p
          (productUpdateState p)
          productScore).mp hScoreKey
    intro x y hInactiveValues
    have hInactiveCoordinates :
        ∀ i : ProductIndex p.d,
          i ∉ p.active → x i = y i := by
      intro i hi
      have hval := hInactiveValues i hi
      cases hx : x i with
      | mk xv hxb =>
          cases hy : y i with
          | mk yv hyb =>
              simp only [hx, hy] at hval ⊢
              cases hval
              rfl
    have hUpdates :
        productUpdateState p x = productUpdateState p y :=
      (productUpdateState_eq_productUpdateState_iff_inactive_eq
        p x y).mpr hInactiveCoordinates
    calc
      productScore x =
          productScore (productUpdateState p x) := (hPreserved x).symm
      _ = productScore (productUpdateState p y) :=
        congrArg productScore hUpdates
      _ = productScore y := hPreserved y
  · intro hInactiveInsensitive
    have hPolicy :
        ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
            p
            (productUpdateState p)
            productScore :=
      ProductRestrictedParamsActiveInsensitiveScore.productUpdateState_scorePreservingPolicy_of_inactiveInsensitive
          p
          productScore
          hInactiveInsensitive
    exact
      (ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyCondition_iff_scorePreservingPolicy
          p
          (productUpdateState p)
          productScore).mpr hPolicy

/--
For a concrete coordinate score, the score-key condition holds exactly when
the selected coordinate is inactive, except for the degenerate bound-zero
model where every coordinate value is forced to zero.
-/
theorem restrictedParams_productUpdateState_inactiveCoordScore_scoreKeyCondition_iff
    (p : ProductRestrictedParams)
    (i : ProductIndex p.d) :
    ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
        p
        (productUpdateState p)
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore p i)
      ↔
    i ∉ p.active ∨ p.n = 0 := by
  rw [
    restrictedParams_productUpdateState_scoreKeyCondition_iff_inactiveInsensitive
  ]
  constructor
  · intro hInactiveInsensitive
    by_cases hi : i ∈ p.active
    · right
      have hPolicy :=
        ProductRestrictedParamsActiveInsensitiveScore.productUpdateState_scorePreservingPolicy_of_inactiveInsensitive
          p
          (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore p i)
          hInactiveInsensitive
      have hScore :=
        hPolicy (ProductTypedState.zero p.n p.d)
      unfold ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore at hScore
      rw [
        productUpdateState_active_val_eq_top p
          (ProductTypedState.zero p.n p.d) hi,
        ProductTypedState.zero_apply_val
      ] at hScore
      exact Int.ofNat.inj hScore
    · exact Or.inl hi
  · rintro (hi | hn)
    · exact
        ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore_inactiveInsensitive_of_inactive_index
          p i hi
    · intro x y _hInactiveValues
      unfold ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
      have hx : (x i).val = 0 := by
        have hxBound := (x i).bound
        omega
      have hy : (y i).val = 0 := by
        have hyBound := (y i).bound
        omega
      rw [hx, hy]

end ProductRestrictedParamsScoreKeyConditionInactiveCharacterization
end VFH2
