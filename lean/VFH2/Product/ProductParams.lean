import VFH2.Product.ProductState

/-!
# VF-H2 v11 Product Restricted Parameters Scaffold

This file adds the restricted parameter structure for the v11 product-index
typed model.

Boundary:
- This is a typed-formalization scaffold component.
- It does not define product fixed-set semantics.
- It does not define product update semantics.
- It does not define product ledger semantics.
- It does not prove the product restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2

/--
Restricted parameters for the v11 product-index typed model.

The active set is now typed over the explicit product index

  TimeLayer × SpaceIndex d

instead of the flattened v10 width index

  Fin (3 * d).

Thus, out-of-product-domain active indices are ruled out by construction.
-/
structure ProductRestrictedParams where
  n : Nat
  d : Nat
  active : List (ProductIndex d)

namespace ProductRestrictedParams

/-- The state type associated with a product restricted parameter object. -/
abbrev State (p : ProductRestrictedParams) : Type :=
  ProductTypedState p.n p.d

/-- The top coordinate for the parameter object's bound. -/
def topCoord (p : ProductRestrictedParams) : Typed.BoundedCoord p.n :=
  Typed.BoundedCoord.top p.n

/-- The zero coordinate for the parameter object's bound. -/
def zeroCoord (p : ProductRestrictedParams) : Typed.BoundedCoord p.n :=
  Typed.BoundedCoord.zero p.n

@[simp]
theorem topCoord_val (p : ProductRestrictedParams) :
    (topCoord p).val = p.n := by
  rfl

@[simp]
theorem zeroCoord_val (p : ProductRestrictedParams) :
    (zeroCoord p).val = 0 := by
  rfl

end ProductRestrictedParams

end VFH2
