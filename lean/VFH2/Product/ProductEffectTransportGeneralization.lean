import VFH2.Product.ProductUpdateGeneralization
import VFH2.Product.ProductLedgerEffectTransport

namespace VFH2

namespace ProductEffectTransportGeneralization

universe u v

/--
Generic effect of an update under an integer-valued score/measure.

This definition is intentionally representation-agnostic. It is the reusable
abstraction behind ledger-effect transport: an effect is the post-update
score minus the pre-update score.
-/
def genericEffect {S : Type u}
    (update : S → S)
    (score : S → Int)
    (x : S) :
    Int :=
  score (update x) - score x

/--
Generic transport theorem for update effects.

If a state transport commutes with update, and if the score/measure is
preserved both at the base state and at the updated state, then the induced
update effect is transported as well.
-/
theorem genericEffect_transport
    {PState : Type u}
    {TState : Type v}
    (transport : PState → TState)
    (productUpdate : PState → PState)
    (typedUpdate : TState → TState)
    (productScore : PState → Int)
    (typedScore : TState → Int)
    (x : PState)
    (hUpdate :
      transport (productUpdate x) =
        typedUpdate (transport x))
    (hBase :
      typedScore (transport x) =
        productScore x)
    (hUpdated :
      typedScore (transport (productUpdate x)) =
        productScore (productUpdate x)) :
    genericEffect typedUpdate typedScore (transport x) =
      genericEffect productUpdate productScore x := by
  unfold genericEffect
  rw [← hUpdate]
  rw [hUpdated]
  rw [hBase]

/--
A variant that accepts the updated-score preservation after rewriting the
typed update directly, which is sometimes more convenient in proof scripts.
-/
theorem genericEffect_transport_direct
    {PState : Type u}
    {TState : Type v}
    (transport : PState → TState)
    (productUpdate : PState → PState)
    (typedUpdate : TState → TState)
    (productScore : PState → Int)
    (typedScore : TState → Int)
    (x : PState)
    (hBase :
      typedScore (transport x) =
        productScore x)
    (hUpdatedDirect :
      typedScore (typedUpdate (transport x)) =
        productScore (productUpdate x)) :
    genericEffect typedUpdate typedScore (transport x) =
      genericEffect productUpdate productScore x := by
  unfold genericEffect
  rw [hUpdatedDirect]
  rw [hBase]

/--
Product-first restatement of the generic effect transport theorem.
-/
theorem genericEffect_transport_product_first
    {PState : Type u}
    {TState : Type v}
    (transport : PState → TState)
    (productUpdate : PState → PState)
    (typedUpdate : TState → TState)
    (productScore : PState → Int)
    (typedScore : TState → Int)
    (x : PState)
    (hUpdate :
      transport (productUpdate x) =
        typedUpdate (transport x))
    (hBase :
      typedScore (transport x) =
        productScore x)
    (hUpdated :
      typedScore (transport (productUpdate x)) =
        productScore (productUpdate x)) :
    genericEffect productUpdate productScore x =
      genericEffect typedUpdate typedScore (transport x) := by
  exact
    (genericEffect_transport
      transport productUpdate typedUpdate productScore typedScore
      x hUpdate hBase hUpdated).symm

/--
Existing restricted ledger-effect transport retained as the VF-H2 ledger
instance associated with the generic effect-transport abstraction.

This theorem does not claim unrestricted VF-H2. It exposes the already
machine-checked restricted ledger-effect result at the v12 effect layer.
-/
theorem restricted_ledgerEffect_transport_instance
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.typedLedgerEffect
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      =
    productLedgerEffect p x := by
  exact
    ProductLedgerEffectTransport.typedLedgerEffect_eq_productLedgerEffect p x

/--
Product-first restatement of the restricted ledger-effect instance.
-/
theorem restricted_productLedgerEffect_eq_typedLedgerEffect_instance
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedgerEffect p x =
    Typed.typedLedgerEffect
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x) := by
  exact
    (restricted_ledgerEffect_transport_instance p x).symm

end ProductEffectTransportGeneralization

end VFH2
