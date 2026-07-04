import VFH2.Product.ProductLedgerEquivalenceTarget
import VFH2.Product.ProductLedgerTransport

/-!
# VF-H2 v11 Transported Typed Ledger Blocks

This file packages the transported typed-state samples into the same
three-block layout used by the v11 product ledger.

Boundary:
- This proves that the transported typed-state block fold equals the product ledger.
- It does not yet prove that `Typed.typedLedgerValues` over `Fin (3*d)`
  decomposes into these three blocks.
- It does not prove full ledger equivalence.
- It does not prove ledger-effect equivalence.
- It does not prove update equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductLedgerTypedBlocks

/--
Transported typed-state values sampled over one explicit product time layer.

This is not `Typed.typedLedgerValues`; it is the block-level view obtained
by sampling the transported typed state at flattened product indices.
-/
def transportedTypedLedgerValuesAtTime
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : TimeLayer) : List Nat :=
  List.ofFn
    (fun s : SpaceIndex p.d =>
      (ProductStateTransport.productToTyped x
        (ProductIndex.flatten (t, s))).val)

/--
The three transported typed-state blocks in the same order as the product
ledger: `t1`, then `t2`, then `t3`.
-/
def transportedTypedLedgerBlockValues
    (p : ProductRestrictedParams)
    (x : p.State) : List Nat :=
  transportedTypedLedgerValuesAtTime p x TimeLayer.t1 ++
  transportedTypedLedgerValuesAtTime p x TimeLayer.t2 ++
  transportedTypedLedgerValuesAtTime p x TimeLayer.t3

/--
At every explicit time layer, the transported typed-state block equals the
corresponding product ledger block.
-/
theorem transportedTypedLedgerValuesAtTime_eq_productLedgerValuesAtTime
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : TimeLayer) :
    transportedTypedLedgerValuesAtTime p x t =
      productLedgerValuesAtTime p x t := by
  unfold transportedTypedLedgerValuesAtTime
  unfold productLedgerValuesAtTime
  apply congrArg List.ofFn
  funext s
  rw [ProductLedgerTransport.productToTyped_flatten_apply_val]

/--
The three transported typed-state blocks equal the product ledger values.
-/
theorem transportedTypedLedgerBlockValues_eq_productLedgerValues
    (p : ProductRestrictedParams)
    (x : p.State) :
    transportedTypedLedgerBlockValues p x = productLedgerValues p x := by
  unfold transportedTypedLedgerBlockValues
  rw [transportedTypedLedgerValuesAtTime_eq_productLedgerValuesAtTime p x TimeLayer.t1]
  rw [transportedTypedLedgerValuesAtTime_eq_productLedgerValuesAtTime p x TimeLayer.t2]
  rw [transportedTypedLedgerValuesAtTime_eq_productLedgerValuesAtTime p x TimeLayer.t3]
  rw [productLedgerValues_def]

/--
The fold-sum of the transported typed-state blocks equals the product ledger.
-/
theorem transportedTypedLedgerBlockFold_eq_productLedger
    (p : ProductRestrictedParams)
    (x : p.State) :
    (transportedTypedLedgerBlockValues p x).foldl
        (fun acc a => acc + a) 0 =
      productLedger p x := by
  rw [transportedTypedLedgerBlockValues_eq_productLedgerValues]
  rw [productLedger_def]

/--
If the actual transported typed ledger values decompose into the transported
typed block values, then the transported typed ledger equals the product ledger.

This isolates the hard remaining v11.3 step:
decomposing `Typed.typedLedgerValues` over `Typed.WidthIndex d = Fin (3*d)`.
-/
theorem ledger_eq_of_transport_values_eq_blocks
    (p : ProductRestrictedParams)
    (x : p.State)
    (hvalues :
      ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x =
        transportedTypedLedgerBlockValues p x) :
    ProductLedgerEquivalenceTarget.ledgerEquivalenceTarget p x := by
  apply ProductLedgerEquivalenceTarget.ledger_eq_of_fold_eq
  rw [hvalues]
  exact transportedTypedLedgerBlockFold_eq_productLedger p x

end ProductLedgerTypedBlocks

end VFH2
