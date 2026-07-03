import VFH2.Product.ProductFlattenBlocks

/-!
# VF-H2 v11 Product Flatten Injectivity Lemmas

This file proves same-layer injectivity facts for the product-to-width
flatten map.

Boundary:
- This is still an index-level bridge.
- It proves same-layer injectivity only.
- It does not yet prove full injectivity of `flatten`.
- It does not define `unflatten`.
- It does not prove ledger equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductIndex

/--
Within the first time layer, flattening is injective on the spatial index.
-/
theorem flatten_t1_injective {d : Nat}
    {s₁ s₂ : SpaceIndex d}
    (h : flatten (TimeLayer.t1, s₁) = flatten (TimeLayer.t1, s₂)) :
    s₁ = s₂ := by
  apply Fin.ext
  have hv := congrArg Fin.val h
  simpa using hv

/--
Within the second time layer, flattening is injective on the spatial index.
-/
theorem flatten_t2_injective {d : Nat}
    {s₁ s₂ : SpaceIndex d}
    (h : flatten (TimeLayer.t2, s₁) = flatten (TimeLayer.t2, s₂)) :
    s₁ = s₂ := by
  apply Fin.ext
  have hv : d + s₁.val = d + s₂.val := by
    have hv0 := congrArg Fin.val h
    simpa using hv0
  omega

/--
Within the third time layer, flattening is injective on the spatial index.
-/
theorem flatten_t3_injective {d : Nat}
    {s₁ s₂ : SpaceIndex d}
    (h : flatten (TimeLayer.t3, s₁) = flatten (TimeLayer.t3, s₂)) :
    s₁ = s₂ := by
  apply Fin.ext
  have hv : 2 * d + s₁.val = 2 * d + s₂.val := by
    have hv0 := congrArg Fin.val h
    simpa using hv0
  omega

/--
Pair-level injectivity in the first time layer.
-/
theorem flatten_t1_pair_injective {d : Nat}
    {s₁ s₂ : SpaceIndex d}
    (h : flatten (TimeLayer.t1, s₁) = flatten (TimeLayer.t1, s₂)) :
    (TimeLayer.t1, s₁) = (TimeLayer.t1, s₂) := by
  have hs : s₁ = s₂ := flatten_t1_injective h
  cases hs
  rfl

/--
Pair-level injectivity in the second time layer.
-/
theorem flatten_t2_pair_injective {d : Nat}
    {s₁ s₂ : SpaceIndex d}
    (h : flatten (TimeLayer.t2, s₁) = flatten (TimeLayer.t2, s₂)) :
    (TimeLayer.t2, s₁) = (TimeLayer.t2, s₂) := by
  have hs : s₁ = s₂ := flatten_t2_injective h
  cases hs
  rfl

/--
Pair-level injectivity in the third time layer.
-/
theorem flatten_t3_pair_injective {d : Nat}
    {s₁ s₂ : SpaceIndex d}
    (h : flatten (TimeLayer.t3, s₁) = flatten (TimeLayer.t3, s₂)) :
    (TimeLayer.t3, s₁) = (TimeLayer.t3, s₂) := by
  have hs : s₁ = s₂ := flatten_t3_injective h
  cases hs
  rfl

/--
The second and first flattened blocks do not overlap.
-/
theorem flatten_t2_ne_flatten_t1 {d : Nat}
    (s₂ s₁ : SpaceIndex d) :
    flatten (TimeLayer.t2, s₂) ≠ flatten (TimeLayer.t1, s₁) := by
  intro h
  exact flatten_t1_ne_flatten_t2 s₁ s₂ h.symm

/--
The third and first flattened blocks do not overlap.
-/
theorem flatten_t3_ne_flatten_t1 {d : Nat}
    (s₃ s₁ : SpaceIndex d) :
    flatten (TimeLayer.t3, s₃) ≠ flatten (TimeLayer.t1, s₁) := by
  intro h
  exact flatten_t1_ne_flatten_t3 s₁ s₃ h.symm

/--
The third and second flattened blocks do not overlap.
-/
theorem flatten_t3_ne_flatten_t2 {d : Nat}
    (s₃ s₂ : SpaceIndex d) :
    flatten (TimeLayer.t3, s₃) ≠ flatten (TimeLayer.t2, s₂) := by
  intro h
  exact flatten_t2_ne_flatten_t3 s₂ s₃ h.symm

end ProductIndex

end VFH2
