import VFH2.Product.ProductFixedSetGeneralization
import VFH2.Product.ProductUpdateTransport

namespace VFH2

namespace ProductUpdateGeneralization

/--
General product-side active-list update.

This definition is independent of `ProductRestrictedParams`: it updates an
arbitrary product-typed state at an arbitrary active product-index list by
assigning the top bounded coordinate.
-/
def generalizedProductUpdateState
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d) :
    ProductTypedState n d :=
  fun i =>
    if i ∈ active then
      Typed.BoundedCoord.top n
    else
      x i

/--
General typed-side active-list update.

This is the typed counterpart of `generalizedProductUpdateState`, stated over
an arbitrary typed active-list.
-/
def generalizedTypedUpdateState
    {n d : Nat}
    (active : List (Typed.WidthIndex d))
    (x : Typed.TypedState n d) :
    Typed.TypedState n d :=
  fun w =>
    if w ∈ active then
      Typed.BoundedCoord.top n
    else
      x w

/--
Generalized active-update transport.

Updating a product state over an arbitrary product active-list and then
transporting to the typed representation is equal to first transporting the
state and then applying the typed update over the flattened active-list.
-/
theorem productToTyped_generalizedProductUpdateState_eq_generalizedTypedUpdateState
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d) :
    ProductStateTransport.productToTyped
        (generalizedProductUpdateState active x)
      =
    generalizedTypedUpdateState
        (List.map ProductIndex.flatten active)
        (ProductStateTransport.productToTyped x) := by
  funext w
  have hiff :=
    ProductActiveSetGeneralization.mem_map_flatten_iff_unflatten_mem
      active w
  by_cases hprod : ProductIndex.unflatten w ∈ active
  · have htyped : w ∈ List.map ProductIndex.flatten active :=
      hiff.mpr hprod
    simp [
      ProductStateTransport.productToTyped,
      generalizedProductUpdateState,
      generalizedTypedUpdateState,
      hprod,
      htyped
    ]
  · have htyped : w ∉ List.map ProductIndex.flatten active := by
      intro hw
      exact hprod (hiff.mp hw)
    simp [
      ProductStateTransport.productToTyped,
      generalizedProductUpdateState,
      generalizedTypedUpdateState,
      hprod,
      htyped
    ]

/--
Product-first restatement of generalized active-update transport.
-/
theorem generalizedTypedUpdateState_eq_productToTyped_generalizedProductUpdateState
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d) :
    generalizedTypedUpdateState
        (List.map ProductIndex.flatten active)
        (ProductStateTransport.productToTyped x)
      =
    ProductStateTransport.productToTyped
        (generalizedProductUpdateState active x) := by
  exact
    (productToTyped_generalizedProductUpdateState_eq_generalizedTypedUpdateState
      active x).symm

/--
The restricted product update is recovered from the generalized product
active-list update.
-/
theorem generalizedProductUpdateState_eq_productUpdateState
    (p : ProductRestrictedParams)
    (x : p.State) :
    generalizedProductUpdateState p.active x =
      productUpdateState p x := by
  funext i
  by_cases hi : i ∈ p.active
  · simp [
      generalizedProductUpdateState,
      productUpdateState,
      ProductRestrictedParams.topCoord,
      hi
    ]
  · simp [
      generalizedProductUpdateState,
      productUpdateState,
      hi
    ]

/--
The v11 restricted Product/Typed update transport is retained as the restricted
instance associated with the generalized active-list update layer.

This theorem deliberately reuses the previously checked restricted theorem
instead of relying on fragile definitional rewriting.
-/
theorem restricted_update_transport_from_general
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductStateTransport.productToTyped (productUpdateState p x)
      =
    Typed.typedUpdateState
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x) := by
  exact
    ProductUpdateTransport.productToTyped_productUpdateState_eq_typedUpdateState
      p x

/--
Product-first restricted restatement.
-/
theorem restricted_typedUpdateState_eq_productToTyped_update_from_general
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.typedUpdateState
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
      =
    ProductStateTransport.productToTyped (productUpdateState p x) := by
  exact
    ProductUpdateTransport.typedUpdateState_eq_productToTyped_productUpdateState
      p x

end ProductUpdateGeneralization

end VFH2
