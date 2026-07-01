import VFH2.Product.ProductPositiveLedger

/-!
# VF-H2 v11 Product Restricted Bridge Theorem

This file proves the restricted bridge theorem for the current v11
product-index typed scaffold.

Boundary:
- This proves the restricted bridge theorem for the v11 product-index typed
  scaffold.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Result:
For the current product-index typed restricted model:

1. product fixed states have zero product ledger effect;
2. product nonfixed states have positive product ledger effect.

The index domain is now explicitly structured as

  ProductIndex d = TimeLayer × SpaceIndex d

rather than the v10 flattened

  WidthIndex d = Fin (3 * d).
-/

namespace VFH2

/-- Product restricted bridge target for the current v11 scaffold. -/
def productRestrictedBridgeTarget
    (p : ProductRestrictedParams)
    (x : p.State) : Prop :=
  (ProductFixedSet p x → productLedgerEffect p x = 0) ∧
  (¬ ProductFixedSet p x → 0 < productLedgerEffect p x)

/--
The current v11 product-index typed scaffold proves the product restricted
bridge target.
-/
theorem productRestrictedBridgeTarget_proved
    (p : ProductRestrictedParams)
    (x : p.State) :
    productRestrictedBridgeTarget p x := by
  constructor
  · intro hfixed
    exact productLedgerEffect_zero_of_fixed hfixed
  · intro hnotfixed
    exact productLedgerEffect_pos_of_not_fixed hnotfixed

/-- Fixed product states have zero product ledger effect. -/
theorem productRestrictedBridge_fixed_zero
    {p : ProductRestrictedParams}
    {x : p.State}
    (hfixed : ProductFixedSet p x) :
    productLedgerEffect p x = 0 := by
  exact productLedgerEffect_zero_of_fixed hfixed

/-- Nonfixed product states have positive product ledger effect. -/
theorem productRestrictedBridge_nonfixed_positive
    {p : ProductRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ ProductFixedSet p x) :
    0 < productLedgerEffect p x := by
  exact productLedgerEffect_pos_of_not_fixed hnotfixed

/--
Product restricted bridge dichotomy.

A product-index state is either fixed on active coordinates and has zero ledger
effect, or it is nonfixed and has positive ledger effect.
-/
theorem productRestrictedBridge_dichotomy
    (p : ProductRestrictedParams)
    (x : p.State) :
    (ProductFixedSet p x ∧ productLedgerEffect p x = 0)
    ∨
    (¬ ProductFixedSet p x ∧ 0 < productLedgerEffect p x) := by
  by_cases hfixed : ProductFixedSet p x
  · left
    constructor
    · exact hfixed
    · exact productLedgerEffect_zero_of_fixed hfixed
  · right
    constructor
    · exact hfixed
    · exact productLedgerEffect_pos_of_not_fixed hfixed

end VFH2
