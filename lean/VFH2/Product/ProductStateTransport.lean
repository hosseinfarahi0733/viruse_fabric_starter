import VFH2.Product.ProductState
import VFH2.Product.ProductFlattenEquiv
import VFH2.Typed.TypedState

/-!
# VF-H2 v11 Product/Typed State Transport

This file lifts the v11.1 index-level equivalence

  ProductIndex d ↔ Typed.WidthIndex d

to a state-level transport between

  ProductTypedState n d

and

  Typed.TypedState n d.

Boundary:
- This is a state-level transport theorem.
- It uses the already-proven index-level round-trip laws.
- It does not prove ledger equivalence.
- It does not prove update equivalence.
- It does not prove the full VF-H2 theory.
- It does not prove unrestricted TTP-VF-H2-004.
-/

namespace VFH2

namespace ProductStateTransport

/--
Transport a v11 product-index typed state to the v10 flattened typed state.

A flattened width index is first unflattened back into a product index.
-/
def productToTyped
    {n d : Nat}
    (x : ProductTypedState n d) :
    Typed.TypedState n d :=
  fun w => x (ProductIndex.unflatten w)

/--
Transport a v10 flattened typed state to the v11 product-index typed state.

A product index is first flattened into a width index.
-/
def typedToProduct
    {n d : Nat}
    (x : Typed.TypedState n d) :
    ProductTypedState n d :=
  fun i => x (ProductIndex.flatten i)

/--
Application rule for product-to-typed state transport.
-/
@[simp]
theorem productToTyped_apply
    {n d : Nat}
    (x : ProductTypedState n d)
    (w : Typed.WidthIndex d) :
    productToTyped x w = x (ProductIndex.unflatten w) := by
  rfl

/--
Application rule for typed-to-product state transport.
-/
@[simp]
theorem typedToProduct_apply
    {n d : Nat}
    (x : Typed.TypedState n d)
    (i : ProductIndex d) :
    typedToProduct x i = x (ProductIndex.flatten i) := by
  rfl

/--
Transporting a product state to typed state and back returns the
original product state.
-/
theorem typedToProduct_productToTyped
    {n d : Nat}
    (x : ProductTypedState n d) :
    typedToProduct (productToTyped x) = x := by
  funext i
  unfold typedToProduct productToTyped
  rw [ProductIndex.unflatten_flatten]

/--
Transporting a typed state to product state and back returns the
original typed state.
-/
theorem productToTyped_typedToProduct
    {n d : Nat}
    (x : Typed.TypedState n d) :
    productToTyped (typedToProduct x) = x := by
  funext w
  unfold productToTyped typedToProduct
  rw [ProductIndex.flatten_unflatten]

/--
A local state-equivalence package between product-index states and
flattened typed states.

This mirrors the local index-equivalence package used in v11.1.
-/
structure ProductTypedStateEquiv (n d : Nat) where
  toTyped : ProductTypedState n d → Typed.TypedState n d
  toProduct : Typed.TypedState n d → ProductTypedState n d
  left_inv :
    ∀ x : ProductTypedState n d,
      toProduct (toTyped x) = x
  right_inv :
    ∀ x : Typed.TypedState n d,
      toTyped (toProduct x) = x

/--
The product-index typed state and the flattened typed state are equivalent
through `productToTyped` and `typedToProduct`.
-/
def stateEquiv (n d : Nat) : ProductTypedStateEquiv n d where
  toTyped := productToTyped
  toProduct := typedToProduct
  left_inv := typedToProduct_productToTyped
  right_inv := productToTyped_typedToProduct

/--
The state equivalence's forward map is `productToTyped`.
-/
@[simp]
theorem stateEquiv_toTyped
    {n d : Nat}
    (x : ProductTypedState n d) :
    (stateEquiv n d).toTyped x = productToTyped x := by
  rfl

/--
The state equivalence's inverse map is `typedToProduct`.
-/
@[simp]
theorem stateEquiv_toProduct
    {n d : Nat}
    (x : Typed.TypedState n d) :
    (stateEquiv n d).toProduct x = typedToProduct x := by
  rfl

/--
Left inverse law exposed through the local state-equivalence package.
-/
theorem stateEquiv_left_inv
    {n d : Nat}
    (x : ProductTypedState n d) :
    (stateEquiv n d).toProduct ((stateEquiv n d).toTyped x) = x := by
  exact (stateEquiv n d).left_inv x

/--
Right inverse law exposed through the local state-equivalence package.
-/
theorem stateEquiv_right_inv
    {n d : Nat}
    (x : Typed.TypedState n d) :
    (stateEquiv n d).toTyped ((stateEquiv n d).toProduct x) = x := by
  exact (stateEquiv n d).right_inv x

end ProductStateTransport

end VFH2
