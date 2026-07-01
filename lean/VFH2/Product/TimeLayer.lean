import VFH2.Typed.WidthIndex

namespace VFH2

/--
The explicit three-time layer index for the v11 product-index model.

This separates the VF-H2 three-time structure from the flattened
`WidthIndex d = Fin (3 * d)` representation used in v10.
-/
abbrev TimeLayer : Type :=
  Fin 3

/-- First time layer. -/
def TimeLayer.t1 : TimeLayer :=
  ⟨0, by decide⟩

/-- Second time layer. -/
def TimeLayer.t2 : TimeLayer :=
  ⟨1, by decide⟩

/-- Third time layer. -/
def TimeLayer.t3 : TimeLayer :=
  ⟨2, by decide⟩

@[simp]
theorem TimeLayer.t1_val : TimeLayer.t1.val = 0 := rfl

@[simp]
theorem TimeLayer.t2_val : TimeLayer.t2.val = 1 := rfl

@[simp]
theorem TimeLayer.t3_val : TimeLayer.t3.val = 2 := rfl

end VFH2
