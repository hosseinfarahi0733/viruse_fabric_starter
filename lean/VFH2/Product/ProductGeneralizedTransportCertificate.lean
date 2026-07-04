import VFH2.Product.ProductBridgeGeneralization

namespace VFH2

namespace ProductGeneralizedTransportCertificate

universe u v

/--
Certificate structure for the generalized v12 Product/Typed transport ladder.

The certificate collects the generalized active-set, pointwise, fixed-set,
active-update, generic effect, and generic bridge-target transport layers.
It is intentionally stated for the generalized v12 layer and does not claim
unrestricted VF-H2.
-/
structure GeneralizedTransportLadderCertificate
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    (P : ProductIndex d → Prop) : Prop where
  activeSet :
    ∀ w : Typed.WidthIndex d,
      w ∈ List.map ProductIndex.flatten active ↔
        ProductIndex.unflatten w ∈ active
  pointwise :
    (∀ w : Typed.WidthIndex d, P (ProductIndex.unflatten w)) ↔
      (∀ i : ProductIndex d, P i)
  activePointwise :
    (∀ w : Typed.WidthIndex d,
        w ∈ List.map ProductIndex.flatten active →
          P (ProductIndex.unflatten w)) ↔
      (∀ i : ProductIndex d, i ∈ active → P i)
  fixedSet :
    (∀ w : Typed.WidthIndex d,
        w ∈ List.map ProductIndex.flatten active →
          ((ProductStateTransport.productToTyped x) w).val = n) ↔
      (∀ i : ProductIndex d, i ∈ active → (x i).val = n)
  updateTransport :
    ProductStateTransport.productToTyped
        (ProductUpdateGeneralization.generalizedProductUpdateState active x)
      =
    ProductUpdateGeneralization.generalizedTypedUpdateState
        (List.map ProductIndex.flatten active)
        (ProductStateTransport.productToTyped x)
  effectPattern :
    ∀ {PState : Type u} {TState : Type v}
      (transport : PState → TState)
      (productUpdate : PState → PState)
      (typedUpdate : TState → TState)
      (productScore : PState → Int)
      (typedScore : TState → Int)
      (y : PState),
      transport (productUpdate y) =
          typedUpdate (transport y) →
      typedScore (transport y) =
          productScore y →
      typedScore (transport (productUpdate y)) =
          productScore (productUpdate y) →
      ProductEffectTransportGeneralization.genericEffect
          typedUpdate typedScore (transport y)
        =
      ProductEffectTransportGeneralization.genericEffect
          productUpdate productScore y
  bridgePattern :
    ∀ {typedFixed productFixed typedCondition productCondition : Prop},
      (typedFixed ↔ productFixed) →
      (typedCondition ↔ productCondition) →
      ProductBridgeGeneralization.genericBridgeTarget
          typedFixed typedCondition
        ↔
      ProductBridgeGeneralization.genericBridgeTarget
          productFixed productCondition

/--
Main v12 generalized transport ladder certificate theorem.
-/
theorem generalizedTransportLadder_certificate
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    (P : ProductIndex d → Prop) :
    GeneralizedTransportLadderCertificate active x P := by
  refine {
    activeSet := ?_,
    pointwise := ?_,
    activePointwise := ?_,
    fixedSet := ?_,
    updateTransport := ?_,
    effectPattern := ?_,
    bridgePattern := ?_
  }
  · intro w
    exact
      ProductActiveSetGeneralization.mem_map_flatten_iff_unflatten_mem
        active w
  · exact
      ProductPointwiseTransportGeneralization.forall_width_iff_forall_product P
  · exact
      ProductPointwiseTransportGeneralization.forall_width_mem_map_iff_forall_product_mem
        active P
  · exact
      ProductFixedSetGeneralization.generalized_fixedSet_transport active x
  · exact
      ProductUpdateGeneralization.productToTyped_generalizedProductUpdateState_eq_generalizedTypedUpdateState
        active x
  · intro PState TState transport productUpdate typedUpdate productScore typedScore y
      hUpdate hBase hUpdated
    exact
      ProductEffectTransportGeneralization.genericEffect_transport
        transport productUpdate typedUpdate productScore typedScore
        y hUpdate hBase hUpdated
  · intro typedFixed productFixed typedCondition productCondition hFixed hCondition
    exact
      ProductBridgeGeneralization.genericBridgeTarget_transport
        hFixed hCondition

/--
Restricted-instance certificate structure for the current restricted VF-H2
scaffold. This records how the restricted theorem surface sits under the v12
generalized layer.
-/
structure RestrictedTransportInstanceCertificate
    (p : ProductRestrictedParams)
    (x : p.State) : Prop where
  activeSet :
    ∀ w : Typed.WidthIndex p.d,
      w ∈ (ProductParamsTransport.typedParamsOfProduct p).active ↔
        ProductIndex.unflatten w ∈ p.active
  fixedSet :
    Typed.TypedFixedSet
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      ↔
    ProductFixedSet p x
  updateTransport :
    ProductStateTransport.productToTyped (productUpdateState p x)
      =
    Typed.typedUpdateState
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
  ledgerEffect :
    Typed.typedLedgerEffect
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      =
    productLedgerEffect p x
  bridgeTarget :
    Typed.typedRestrictedBridgeTarget
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      ↔
    productRestrictedBridgeTarget p x

/--
Restricted-instance certificate theorem for the current restricted VF-H2
scaffold.
-/
theorem restrictedTransportInstance_certificate
    (p : ProductRestrictedParams)
    (x : p.State) :
    RestrictedTransportInstanceCertificate p x := by
  refine {
    activeSet := ?_,
    fixedSet := ?_,
    updateTransport := ?_,
    ledgerEffect := ?_,
    bridgeTarget := ?_
  }
  · intro w
    exact
      ProductActiveSetGeneralization.restricted_mem_typed_active_iff_unflatten_mem
        p w
  · exact
      ProductFixedSetGeneralization.restricted_fixedSet_transport_from_general
        p x
  · exact
      ProductUpdateGeneralization.restricted_update_transport_from_general
        p x
  · exact
      ProductEffectTransportGeneralization.restricted_ledgerEffect_transport_instance
        p x
  · exact
      ProductBridgeGeneralization.restricted_bridgeTarget_transport_instance
        p x

end ProductGeneralizedTransportCertificate

end VFH2
