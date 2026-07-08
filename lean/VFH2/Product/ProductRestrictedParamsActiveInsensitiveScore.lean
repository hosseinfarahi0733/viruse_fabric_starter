import VFH2.Product.ProductUpdate
import VFH2.Product.ProductRestrictedParamsScorePreservationDischarge

/-!
# C12 — Active-insensitive score semantics

This file introduces a semantic score condition for the restricted product model.

Scientific role:
- It does not assume pointwise score preservation directly.
- It defines a meaningful sufficient condition for score preservation:
  the score depends only on inactive coordinates.
- Since `productUpdateState` preserves inactive coordinates, such a score is
  preserved by the concrete product update.

Boundary:
- This does not prove all scores are preserved.
- This does not discharge score preservation unconditionally.
- This does not derive ProductFixedSet.
- This does not discharge natural base bounds.
- This is not a new scientific tag by itself unless integrated into the main
  proof spine as an actual assumption reduction.
-/

namespace VFH2

namespace ProductRestrictedParamsActiveInsensitiveScore

/--
A product score is inactive-insensitive when any two states with the same
inactive-coordinate values have the same score.

This is a semantic condition: the score may depend on inactive coordinates, but
not on active coordinates.
-/
def productScoreInactiveInsensitive
    (p : ProductRestrictedParams)
    (productScore : p.State → Int) : Prop :=
  ∀ x y : p.State,
    (∀ i : ProductIndex p.d,
      i ∉ p.active → (x i).val = (y i).val) →
    productScore x = productScore y

/--
The concrete product update preserves inactive-coordinate values.
-/
theorem productUpdateState_preserves_inactive_values
    (p : ProductRestrictedParams)
    (x : p.State) :
    ∀ i : ProductIndex p.d,
      i ∉ p.active →
      (productUpdateState p x i).val = (x i).val := by
  intro i hi
  exact productUpdateState_inactive_val_eq p x hi

/--
If a score is inactive-insensitive, then the concrete product update preserves
that score pointwise.

This is the C12 assumption-reduction theorem for the score-preservation
obligation, specialized to `productUpdateState`.
-/
theorem productUpdateState_scorePreservingPolicy_of_inactiveInsensitive
    (p : ProductRestrictedParams)
    (productScore : p.State → Int)
    (hScoreInactive :
      productScoreInactiveInsensitive p productScore) :
    ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p
      (productUpdateState p)
      productScore := by
  intro y
  unfold productScoreInactiveInsensitive at hScoreInactive
  exact
    hScoreInactive
      (productUpdateState p y)
      y
      (productUpdateState_preserves_inactive_values p y)

end ProductRestrictedParamsActiveInsensitiveScore

end VFH2
