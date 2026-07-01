import VFH2.Product.ProductLedger

/-!
# VF-H2 v11 Product Fixed-Zero Ledger Effect

This file proves the fixed-zero ledger-effect half for the v11 product-index
typed scaffold.

Boundary:
- This proves that product fixed states have zero product ledger effect.
- It does not prove positive product ledger effect for nonfixed states.
- It does not prove the product restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2

/--
For a product fixed state, the product update preserves the value list at each
explicit time layer.
-/
theorem productLedgerValuesAtTime_update_eq_of_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hfixed : ProductFixedSet p x)
    (t : TimeLayer) :
    productLedgerValuesAtTime p (productUpdateState p x) t =
      productLedgerValuesAtTime p x t := by
  unfold productLedgerValuesAtTime
  have hfun :
      (fun s : SpaceIndex p.d => (productUpdateState p x (t, s)).val) =
        (fun s : SpaceIndex p.d => (x (t, s)).val) := by
    funext s
    exact productUpdateState_val_eq_of_fixed hfixed (t, s)
  rw [hfun]

/--
For a product fixed state, the product update preserves the full product ledger
value list.
-/
theorem productLedgerValues_update_eq_of_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hfixed : ProductFixedSet p x) :
    productLedgerValues p (productUpdateState p x) =
      productLedgerValues p x := by
  unfold productLedgerValues
  rw [productLedgerValuesAtTime_update_eq_of_fixed hfixed TimeLayer.t1]
  rw [productLedgerValuesAtTime_update_eq_of_fixed hfixed TimeLayer.t2]
  rw [productLedgerValuesAtTime_update_eq_of_fixed hfixed TimeLayer.t3]

/--
For a product fixed state, the product update preserves the product ledger.
-/
theorem productLedger_update_eq_of_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hfixed : ProductFixedSet p x) :
    productLedger p (productUpdateState p x) =
      productLedger p x := by
  unfold productLedger
  rw [productLedgerValues_update_eq_of_fixed hfixed]

/--
Product fixed states have zero product ledger effect.
-/
theorem productLedgerEffect_zero_of_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hfixed : ProductFixedSet p x) :
    productLedgerEffect p x = 0 := by
  unfold productLedgerEffect
  rw [productLedger_update_eq_of_fixed hfixed]
  simp

/-- Fixed-zero target for the current v11 product-index typed scaffold. -/
def productFixedZeroLedgerEffectTarget
    (p : ProductRestrictedParams)
    (x : p.State) : Prop :=
  ProductFixedSet p x → productLedgerEffect p x = 0

/--
The current v11 product-index scaffold proves zero product ledger effect for
product fixed states.
-/
theorem productFixedZeroLedgerEffectTarget_proved
    (p : ProductRestrictedParams)
    (x : p.State) :
    productFixedZeroLedgerEffectTarget p x := by
  intro hfixed
  exact productLedgerEffect_zero_of_fixed hfixed

end VFH2
