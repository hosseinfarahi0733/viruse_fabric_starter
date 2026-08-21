import VFH2.Product.ProductRestrictedParamsProofSpineScoreWindowCharacterization

/-!
# Exact After-One-Update Proof-Spine Characterization

This module identifies the exact remaining score-side condition for every
restricted Product state to enter the current proof spine after one concrete
update.  It is neither a global score-preservation assumption nor a condition
on arbitrary nonfixed states: the score must, and need only, lie in the chosen
window on the Product fixed set.

The reverse implication uses one-step stabilization.  The forward implication
uses the fact that every fixed state is its own preimage under the update.
Thus the theorem characterizes the full image of the concrete update rather
than merely specializing the proof spine at one state.

Boundary:
- This is specific to `ProductRestrictedParams` and `productUpdateState`.
- It introduces no score-invariance, fixedness, or boundedness assumption.
- It does not claim that an arbitrary score is bounded on the fixed set.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace ProductRestrictedParamsAfterOneUpdateProofSpineCharacterization

/--
Every initial state enters the canonical restricted proof spine after one
update exactly when the score is bounded by the requested window on every
Product fixed state.
-/
theorem restrictedParams_all_after_one_update_proofSpineTarget_iff_scoreBoundedOnFixedSet
    (p : ProductRestrictedParams)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    (∀ x : p.State,
      ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        (productUpdateState p x)
        (productUpdateState p)
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          (productUpdateState p x)
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          (productUpdateState p x)
          (productUpdateState p)
          productScore)
        (ProductFixedSet p (productUpdateState p x))
        thresholdLo
        thresholdHi
        hThreshold)
      ↔
    (∀ y : p.State,
      ProductFixedSet p y →
        thresholdLo ≤ productScore y ∧
        productScore y ≤ thresholdHi) := by
  constructor
  · intro hAll y hFixed
    have hUpdate :
        productUpdateState p y = y :=
      (productFixedSet_iff_productUpdateState_eq_self p y).mp hFixed
    have hAtUpdate :=
      (ProductRestrictedParamsProofSpineScoreWindowCharacterization.restrictedParams_restrictedProofSpineTarget_iff_fixedSet_and_baseScoreBounds
        p
        (productUpdateState p y)
        productScore
        thresholdLo
        thresholdHi
        hThreshold).mp
        (hAll y)
    rw [hUpdate] at hAtUpdate
    exact ⟨hAtUpdate.2.1, hAtUpdate.2.2⟩
  · intro hBounded x
    apply
      (ProductRestrictedParamsProofSpineScoreWindowCharacterization.restrictedParams_restrictedProofSpineTarget_iff_fixedSet_and_baseScoreBounds
        p
        (productUpdateState p x)
        productScore
        thresholdLo
        thresholdHi
        hThreshold).mpr
    have hFixed :
        ProductFixedSet p (productUpdateState p x) :=
      productUpdateState_ProductFixedSet p x
    have hBounds := hBounded (productUpdateState p x) hFixed
    exact ⟨hFixed, hBounds.1, hBounds.2⟩

end ProductRestrictedParamsAfterOneUpdateProofSpineCharacterization
end VFH2
