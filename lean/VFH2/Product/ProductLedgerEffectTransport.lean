import VFH2.Product.ProductLedgerTypedValuesDecomposition
import VFH2.Product.ProductUpdateTransport
import VFH2.Product.ProductLedger
import VFH2.Product.ProductUpdate
import VFH2.Typed.TypedLedger

namespace VFH2

namespace ProductLedgerEffectTransport

/--
The transported Typed ledger agrees with the Product ledger for a Product state.
This is the v11.3 ledger equivalence exposed under the effect-transport namespace.
-/
theorem transportedTypedLedger_eq_productLedger
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductLedgerEquivalenceTarget.transportedTypedLedger p x =
      productLedger p x := by
  exact ProductLedgerTypedValuesDecomposition.ledgerEquivalenceTarget p x

/--
The Typed ledger of the transported Product state agrees with the Product ledger.
-/
theorem typedLedger_eq_transport_of_product
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.typedLedger
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      =
    productLedger p x := by
  exact transportedTypedLedger_eq_productLedger p x

/--
Updating on the Typed side after state transport yields the same ledger value as
updating on the Product side and then reading the Product ledger.
-/
theorem typedLedger_update_eq_productLedger_update
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.typedLedger
        (ProductParamsTransport.typedParamsOfProduct p)
        (Typed.typedUpdateState
          (ProductParamsTransport.typedParamsOfProduct p)
          (ProductStateTransport.productToTyped x))
      =
    productLedger p (productUpdateState p x) := by
  rw [ProductUpdateTransport.typedUpdateState_eq_productToTyped_productUpdateState p x]
  exact typedLedger_eq_transport_of_product p (productUpdateState p x)

/--
Main v11.5 target: Product and Typed ledger effects agree under the current
restricted Product-to-Typed transport path.
-/
theorem typedLedgerEffect_eq_productLedgerEffect
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.typedLedgerEffect
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      =
    productLedgerEffect p x := by
  unfold Typed.typedLedgerEffect
  unfold productLedgerEffect
  rw [typedLedger_update_eq_productLedger_update p x]
  rw [typedLedger_eq_transport_of_product p x]

end ProductLedgerEffectTransport

end VFH2
