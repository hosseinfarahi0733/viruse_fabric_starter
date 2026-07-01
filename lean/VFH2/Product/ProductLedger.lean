import VFH2.Product.ProductNonfixedIncrease

/-!
# VF-H2 v11 Product Ledger Scaffold

This file defines the product-index ledger and product ledger effect for the
v11 restricted typed model.

Boundary:
- This defines product ledger values, product ledger, and product ledger effect.
- It does not prove product fixed-zero ledger effect.
- It does not prove positive product ledger effect.
- It does not prove the product restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Design note:
The v10 ledger enumerates a flattened finite index

  WidthIndex d = Fin (3 * d).

The v11 model separates the index into

  ProductIndex d = TimeLayer × SpaceIndex d.

To avoid prematurely proving a full product-index enumeration theorem, this
ledger enumerates the three time layers explicitly and uses `List.ofFn` only
over the spatial `Fin d` component.
-/

namespace VFH2

/-- Values of a product-index typed state at a fixed time layer. -/
def productLedgerValuesAtTime
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : TimeLayer) : List Nat :=
  List.ofFn (fun s : SpaceIndex p.d => (x (t, s)).val)

/--
Values of a product-index typed state over all three explicit time layers.

The order is `t1`, then `t2`, then `t3`. This is a scaffold enumeration choice,
not yet a theorem identifying the product index with the old flattened index.
-/
def productLedgerValues
    (p : ProductRestrictedParams)
    (x : p.State) : List Nat :=
  productLedgerValuesAtTime p x TimeLayer.t1 ++
  productLedgerValuesAtTime p x TimeLayer.t2 ++
  productLedgerValuesAtTime p x TimeLayer.t3

/-- Product ledger over a product-index typed restricted state. -/
def productLedger
    (p : ProductRestrictedParams)
    (x : p.State) : Nat :=
  (productLedgerValues p x).foldl (fun acc a => acc + a) 0

/-- Product ledger effect induced by the product update map. -/
def productLedgerEffect
    (p : ProductRestrictedParams)
    (x : p.State) : Int :=
  (productLedger p (productUpdateState p x) : Int) -
    (productLedger p x : Int)

/-- Definitional expansion of product ledger values at a fixed time layer. -/
theorem productLedgerValuesAtTime_def
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : TimeLayer) :
    productLedgerValuesAtTime p x t =
      List.ofFn (fun s : SpaceIndex p.d => (x (t, s)).val) := by
  rfl

/-- Definitional expansion of product ledger values. -/
theorem productLedgerValues_def
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedgerValues p x =
      productLedgerValuesAtTime p x TimeLayer.t1 ++
      productLedgerValuesAtTime p x TimeLayer.t2 ++
      productLedgerValuesAtTime p x TimeLayer.t3 := by
  rfl

/-- Definitional expansion of product ledger. -/
theorem productLedger_def
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedger p x =
      (productLedgerValues p x).foldl (fun acc a => acc + a) 0 := by
  rfl

/-- Definitional expansion of product ledger effect. -/
theorem productLedgerEffect_def
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedgerEffect p x =
      (productLedger p (productUpdateState p x) : Int) -
        (productLedger p x : Int) := by
  rfl

/-- Product ledger values are natural numbers, so the ledger is nonnegative. -/
theorem productLedger_zero_le
    (p : ProductRestrictedParams)
    (x : p.State) :
    0 ≤ productLedger p x := by
  exact Nat.zero_le (productLedger p x)

/-- Every product coordinate value used by the ledger is bounded by top. -/
theorem productLedger_coordinate_val_le_top
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : ProductIndex p.d) :
    (x i).val ≤ p.n := by
  exact (x i).bound

/-- Every updated product coordinate value used by the ledger is bounded by top. -/
theorem productLedger_updated_coordinate_val_le_top
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : ProductIndex p.d) :
    (productUpdateState p x i).val ≤ p.n := by
  exact (productUpdateState p x i).bound

end VFH2
