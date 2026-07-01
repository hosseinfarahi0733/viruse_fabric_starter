import VFH2.Product.TimeLayer

namespace VFH2

/--
The explicit spatial index for the v11 product-index model.
-/
abbrev SpaceIndex (d : Nat) : Type :=
  Fin d

/--
The v11 structured index: an explicit time layer paired with
an explicit spatial coordinate.

This is intentionally not yet connected to ledger enumeration.
The first v11 step is domain separation only.
-/
abbrev ProductIndex (d : Nat) : Type :=
  TimeLayer × SpaceIndex d

/-- Extract the time component of a product index. -/
def ProductIndex.time {d : Nat} (i : ProductIndex d) : TimeLayer :=
  i.1

/-- Extract the space component of a product index. -/
def ProductIndex.space {d : Nat} (i : ProductIndex d) : SpaceIndex d :=
  i.2

@[simp]
theorem ProductIndex.time_mk {d : Nat} (t : TimeLayer) (s : SpaceIndex d) :
    ProductIndex.time (t, s) = t := rfl

@[simp]
theorem ProductIndex.space_mk {d : Nat} (t : TimeLayer) (s : SpaceIndex d) :
    ProductIndex.space (t, s) = s := rfl

end VFH2
