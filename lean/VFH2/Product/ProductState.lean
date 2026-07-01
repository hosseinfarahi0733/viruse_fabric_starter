import VFH2.Product.ProductIndex
import VFH2.Typed.BoundedCoord

/-!
# VF-H2 v11 Product Typed State Scaffold

This file starts the v11 product-index state layer.

Boundary:
- This is a typed-formalization scaffold component.
- It does not define product ledger semantics.
- It does not prove the product restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2

/--
A product-index typed state for the v11 model.

Compared with the v10 flattened state

  WidthIndex d → Typed.BoundedCoord n

this state is indexed by the explicit product index

  TimeLayer × SpaceIndex d.

This is still a restricted scaffold layer. It does not define ledger
semantics or the full VF-H2 dynamics.
-/
abbrev ProductTypedState (n d : Nat) : Type :=
  ProductIndex d → Typed.BoundedCoord n

namespace ProductTypedState

/-- Get a coordinate from a product-index typed state. -/
def get
    {n d : Nat}
    (x : ProductTypedState n d)
    (i : ProductIndex d) :
    Typed.BoundedCoord n :=
  x i

/-- A product typed state's coordinate value is bounded by top by construction. -/
theorem get_val_le_top
    {n d : Nat}
    (x : ProductTypedState n d)
    (i : ProductIndex d) :
    (get x i).val ≤ n := by
  exact (get x i).bound

/-- Direct application form of coordinate boundedness. -/
theorem apply_val_le_top
    {n d : Nat}
    (x : ProductTypedState n d)
    (i : ProductIndex d) :
    (x i).val ≤ n := by
  exact (x i).bound

/-- Constant product typed state. -/
def const
    (n d : Nat)
    (c : Typed.BoundedCoord n) :
    ProductTypedState n d :=
  fun _ => c

/-- Zero product typed state. -/
def zero
    (n d : Nat) :
    ProductTypedState n d :=
  fun _ => Typed.BoundedCoord.zero n

/-- Top product typed state. -/
def top
    (n d : Nat) :
    ProductTypedState n d :=
  fun _ => Typed.BoundedCoord.top n

/-- Constant state returns the given coordinate at every product index. -/
theorem const_apply
    {n d : Nat}
    (c : Typed.BoundedCoord n)
    (i : ProductIndex d) :
    const n d c i = c := by
  rfl

/-- Constant state value projection. -/
theorem const_apply_val
    {n d : Nat}
    (c : Typed.BoundedCoord n)
    (i : ProductIndex d) :
    (const n d c i).val = c.val := by
  rfl

/-- Zero product state has value zero at every product index. -/
theorem zero_apply_val
    (n d : Nat)
    (i : ProductIndex d) :
    (zero n d i).val = 0 := by
  rfl

/-- Top product state has value `n` at every product index. -/
theorem top_apply_val
    (n d : Nat)
    (i : ProductIndex d) :
    (top n d i).val = n := by
  rfl

end ProductTypedState

end VFH2
