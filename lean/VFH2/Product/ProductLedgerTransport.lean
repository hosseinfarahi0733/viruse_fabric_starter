import VFH2.Product.ProductLedger
import VFH2.Product.ProductStateTransport

/-!
# VF-H2 v11 Product Ledger Transport Blocks

This file starts the ledger-transport bridge from the v11 product-index
ledger to the v10 flattened typed ledger.

Boundary:
- This proves pointwise and block-level ledger transport facts.
- It does not prove full typed/product ledger equality.
- It does not prove update equivalence.
- It does not prove ledger-effect equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductLedgerTransport

/--
Reading a transported typed state at the flattened form of a product index
returns the original product-state coordinate.
-/
@[simp]
theorem productToTyped_flatten_apply
    {n d : Nat}
    (x : ProductTypedState n d)
    (i : ProductIndex d) :
    ProductStateTransport.productToTyped x (ProductIndex.flatten i) = x i := by
  unfold ProductStateTransport.productToTyped
  rw [ProductIndex.unflatten_flatten]

/--
Value-level form of `productToTyped_flatten_apply`.
-/
@[simp]
theorem productToTyped_flatten_apply_val
    {n d : Nat}
    (x : ProductTypedState n d)
    (i : ProductIndex d) :
    (ProductStateTransport.productToTyped x (ProductIndex.flatten i)).val =
      (x i).val := by
  rw [productToTyped_flatten_apply]

/--
The first product ledger block equals the transported typed state sampled
over the flattened first time block.
-/
theorem productToTyped_flatten_t1_values_eq_productLedgerValuesAtTime
    (p : ProductRestrictedParams)
    (x : p.State) :
    List.ofFn
        (fun s : SpaceIndex p.d =>
          (ProductStateTransport.productToTyped x
              (ProductIndex.flatten (TimeLayer.t1, s))).val)
      =
    productLedgerValuesAtTime p x TimeLayer.t1 := by
  unfold productLedgerValuesAtTime
  apply congrArg List.ofFn
  funext s
  rw [productToTyped_flatten_apply_val]

/--
The second product ledger block equals the transported typed state sampled
over the flattened second time block.
-/
theorem productToTyped_flatten_t2_values_eq_productLedgerValuesAtTime
    (p : ProductRestrictedParams)
    (x : p.State) :
    List.ofFn
        (fun s : SpaceIndex p.d =>
          (ProductStateTransport.productToTyped x
              (ProductIndex.flatten (TimeLayer.t2, s))).val)
      =
    productLedgerValuesAtTime p x TimeLayer.t2 := by
  unfold productLedgerValuesAtTime
  apply congrArg List.ofFn
  funext s
  rw [productToTyped_flatten_apply_val]

/--
The third product ledger block equals the transported typed state sampled
over the flattened third time block.
-/
theorem productToTyped_flatten_t3_values_eq_productLedgerValuesAtTime
    (p : ProductRestrictedParams)
    (x : p.State) :
    List.ofFn
        (fun s : SpaceIndex p.d =>
          (ProductStateTransport.productToTyped x
              (ProductIndex.flatten (TimeLayer.t3, s))).val)
      =
    productLedgerValuesAtTime p x TimeLayer.t3 := by
  unfold productLedgerValuesAtTime
  apply congrArg List.ofFn
  funext s
  rw [productToTyped_flatten_apply_val]

/--
Product ledger values can be represented as the three flattened typed-state
blocks sampled through `productToTyped`.
-/
theorem productLedgerValues_eq_productToTyped_flatten_blocks
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedgerValues p x =
      List.ofFn
        (fun s : SpaceIndex p.d =>
          (ProductStateTransport.productToTyped x
              (ProductIndex.flatten (TimeLayer.t1, s))).val)
      ++
      List.ofFn
        (fun s : SpaceIndex p.d =>
          (ProductStateTransport.productToTyped x
              (ProductIndex.flatten (TimeLayer.t2, s))).val)
      ++
      List.ofFn
        (fun s : SpaceIndex p.d =>
          (ProductStateTransport.productToTyped x
              (ProductIndex.flatten (TimeLayer.t3, s))).val) := by
  rw [productLedgerValues_def]
  rw [← productToTyped_flatten_t1_values_eq_productLedgerValuesAtTime p x]
  rw [← productToTyped_flatten_t2_values_eq_productLedgerValuesAtTime p x]
  rw [← productToTyped_flatten_t3_values_eq_productLedgerValuesAtTime p x]

end ProductLedgerTransport

end VFH2
