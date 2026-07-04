import VFH2.Product.ProductParamsTransport
import VFH2.Product.ProductStateTransport
import VFH2.Product.ProductUpdate
import VFH2.Typed.TypedUpdate

/-!
# VF-H2 v11 Product/Typed Update Transport

This file proves that the product-index update and the flattened typed update
are compatible under the already-proven product/typed parameter and state
transports.

Boundary:
- This proves update-state transport compatibility for the current restricted
  scaffold.
- It does not prove ledger-effect equivalence.
- It does not prove bridge equivalence.
- It does not prove unrestricted VF-H2.
- It does not prove empirical or biological validation.
-/

namespace VFH2

namespace ProductUpdateTransport

/--
A flattened typed index is active in the transported typed parameters exactly
when its unflattened product index is active in the original product parameters.
-/
theorem mem_typed_active_iff_unflatten_mem_product_active
    (p : ProductRestrictedParams)
    (w : Typed.WidthIndex p.d) :
    w ∈ (ProductParamsTransport.typedParamsOfProduct p).active ↔
      ProductIndex.unflatten w ∈ p.active := by
  constructor
  · intro hw
    rcases
      (ProductParamsTransport.mem_typed_active_iff_exists_product_active
        (p := p)
        (w := w)).mp hw with
      ⟨i, hi, hflat⟩
    have hi_eq : i = ProductIndex.unflatten w := by
      apply ProductIndex.flatten_injective
      rw [hflat]
      exact (ProductIndex.flatten_unflatten w).symm
    cases hi_eq
    exact hi
  · intro hprod
    exact
      (ProductParamsTransport.mem_typed_active_iff_exists_product_active
        (p := p)
        (w := w)).mpr
        ⟨ProductIndex.unflatten w, hprod, ProductIndex.flatten_unflatten w⟩

/--
Transporting the product update equals applying the typed update after
transporting parameters and state.
-/
theorem productToTyped_productUpdateState_eq_typedUpdateState
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductStateTransport.productToTyped (productUpdateState p x) =
      Typed.typedUpdateState
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x) := by
  funext w
  by_cases hprod : ProductIndex.unflatten w ∈ p.active
  · have htyped :
        w ∈ (ProductParamsTransport.typedParamsOfProduct p).active :=
      (mem_typed_active_iff_unflatten_mem_product_active p w).mpr hprod

    rw [Typed.typedUpdateState_apply]
    rw [Typed.typedUpdateCoord_active
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
      htyped]

    unfold ProductStateTransport.productToTyped
    rw [productUpdateState_active p x hprod]
    simp [ProductRestrictedParams.topCoord, ProductParamsTransport.typedParamsOfProduct]

  · have htyped :
        ¬ w ∈ (ProductParamsTransport.typedParamsOfProduct p).active := by
      intro hw
      exact hprod
        ((mem_typed_active_iff_unflatten_mem_product_active p w).mp hw)

    rw [Typed.typedUpdateState_apply]
    rw [Typed.typedUpdateCoord_inactive
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
      htyped]

    unfold ProductStateTransport.productToTyped
    rw [productUpdateState_inactive p x hprod]
    rfl

/--
Symmetric spelling of update transport compatibility.
-/
theorem typedUpdateState_eq_productToTyped_productUpdateState
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.typedUpdateState
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x) =
      ProductStateTransport.productToTyped (productUpdateState p x) := by
  exact (productToTyped_productUpdateState_eq_typedUpdateState p x).symm

end ProductUpdateTransport

end VFH2
