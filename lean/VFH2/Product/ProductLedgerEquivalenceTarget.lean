import VFH2.Product.ProductLedgerTransport
import VFH2.Product.ProductParamsTransport
import VFH2.Typed.TypedLedger

/-!
# VF-H2 v11 Product/Typed Ledger Equivalence Target

This file states and partially prepares the ledger-equivalence bridge between
the v11 product ledger and the v10 typed ledger transported through the
v11.1/v11.2 equivalences.

Boundary:
- This file defines the exact transported typed ledger target.
- It proves definitional expansions needed for the future ledger equivalence.
- It does not yet prove full ledger equality.
- It does not prove ledger-effect equivalence.
- It does not prove update equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductLedgerEquivalenceTarget

/--
The typed ledger obtained by transporting product parameters and product state
into the v10 typed layer.
-/
def transportedTypedLedger
    (p : ProductRestrictedParams)
    (x : p.State) : Nat :=
  Typed.typedLedger
    (ProductParamsTransport.typedParamsOfProduct p)
    (ProductStateTransport.productToTyped x)

/--
The typed ledger values obtained after transporting product parameters and
product state into the v10 typed layer.
-/
def transportedTypedLedgerValues
    (p : ProductRestrictedParams)
    (x : p.State) : List Nat :=
  Typed.typedLedgerValues
    (ProductParamsTransport.typedParamsOfProduct p)
    (ProductStateTransport.productToTyped x)

/--
Definitional expansion of transported typed ledger values.
-/
theorem transportedTypedLedgerValues_def
    (p : ProductRestrictedParams)
    (x : p.State) :
    transportedTypedLedgerValues p x =
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          (ProductStateTransport.productToTyped x w).val) := by
  rfl

/--
Definitional expansion of the transported typed ledger.
-/
theorem transportedTypedLedger_def
    (p : ProductRestrictedParams)
    (x : p.State) :
    transportedTypedLedger p x =
      (transportedTypedLedgerValues p x).foldl
        (fun acc a => acc + a) 0 := by
  rfl

/--
The intended v11.3 ledger-equivalence target.

This is deliberately stated as a definition first, rather than immediately
claimed as a theorem, because the hard remaining step is decomposing
`List.ofFn` over `Typed.WidthIndex d = Fin (3*d)` into the three product
time blocks.
-/
def ledgerEquivalenceTarget
    (p : ProductRestrictedParams)
    (x : p.State) : Prop :=
  transportedTypedLedger p x = productLedger p x

/--
A sufficient list-level condition for the transported typed ledger to equal
the product ledger.

The hard future work is to prove the premise:
`transportedTypedLedgerValues p x = productLedgerValues p x`.
-/
theorem ledger_eq_of_values_eq
    (p : ProductRestrictedParams)
    (x : p.State)
    (hvalues : transportedTypedLedgerValues p x = productLedgerValues p x) :
    ledgerEquivalenceTarget p x := by
  unfold ledgerEquivalenceTarget transportedTypedLedger
  rw [Typed.typedLedger_def]
  unfold transportedTypedLedgerValues at hvalues
  rw [hvalues]
  rw [productLedger_def]

/--
A sufficient fold-level condition for the transported typed ledger to equal
the product ledger.

This avoids requiring literal list equality and may be easier than proving
that the two enumerations are definitionally the same list.
-/
theorem ledger_eq_of_fold_eq
    (p : ProductRestrictedParams)
    (x : p.State)
    (hfold :
      (transportedTypedLedgerValues p x).foldl
          (fun acc a => acc + a) 0 =
        productLedger p x) :
    ledgerEquivalenceTarget p x := by
  unfold ledgerEquivalenceTarget transportedTypedLedger
  rw [Typed.typedLedger_def]
  exact hfold

end ProductLedgerEquivalenceTarget

end VFH2
