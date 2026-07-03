import VFH2.Product.ProductFlatten

/-!
# VF-H2 v11 Product Flatten Block Lemmas

This file proves simple range facts for the product-to-width flatten map.

Boundary:
- This is still an index-level bridge.
- It does not prove injectivity.
- It does not define unflatten.
- It does not prove ledger equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductIndex

/--
The first time layer is flattened into the first block `[0, d)`.
-/
theorem flatten_t1_lt_d {d : Nat} (s : SpaceIndex d) :
    (flatten (TimeLayer.t1, s)).val < d := by
  rw [flatten_t1_val]
  exact s.isLt

/--
The second time layer is flattened into the second block `[d, 2*d)`.
-/
theorem flatten_t2_block {d : Nat} (s : SpaceIndex d) :
    d ≤ (flatten (TimeLayer.t2, s)).val ∧
      (flatten (TimeLayer.t2, s)).val < 2 * d := by
  constructor
  · rw [flatten_t2_val]
    omega
  · rw [flatten_t2_val]
    have hs : s.val < d := s.isLt
    omega

/--
The third time layer is flattened into the third block `[2*d, 3*d)`.
-/
theorem flatten_t3_block {d : Nat} (s : SpaceIndex d) :
    2 * d ≤ (flatten (TimeLayer.t3, s)).val ∧
      (flatten (TimeLayer.t3, s)).val < 3 * d := by
  constructor
  · rw [flatten_t3_val]
    omega
  · exact flatten_lt_width (TimeLayer.t3, s)

/--
The first and second flattened blocks do not overlap.
-/
theorem flatten_t1_ne_flatten_t2 {d : Nat}
    (s₁ s₂ : SpaceIndex d) :
    flatten (TimeLayer.t1, s₁) ≠ flatten (TimeLayer.t2, s₂) := by
  intro h
  have hlt : (flatten (TimeLayer.t1, s₁)).val < d :=
    flatten_t1_lt_d s₁
  have hge : d ≤ (flatten (TimeLayer.t2, s₂)).val :=
    (flatten_t2_block s₂).1
  have hv :
      (flatten (TimeLayer.t1, s₁)).val =
        (flatten (TimeLayer.t2, s₂)).val :=
    congrArg Fin.val h
  omega

/--
The first and third flattened blocks do not overlap.
-/
theorem flatten_t1_ne_flatten_t3 {d : Nat}
    (s₁ s₃ : SpaceIndex d) :
    flatten (TimeLayer.t1, s₁) ≠ flatten (TimeLayer.t3, s₃) := by
  intro h
  have hlt : (flatten (TimeLayer.t1, s₁)).val < d :=
    flatten_t1_lt_d s₁
  have hge : 2 * d ≤ (flatten (TimeLayer.t3, s₃)).val :=
    (flatten_t3_block s₃).1
  have hv :
      (flatten (TimeLayer.t1, s₁)).val =
        (flatten (TimeLayer.t3, s₃)).val :=
    congrArg Fin.val h
  omega

/--
The second and third flattened blocks do not overlap.
-/
theorem flatten_t2_ne_flatten_t3 {d : Nat}
    (s₂ s₃ : SpaceIndex d) :
    flatten (TimeLayer.t2, s₂) ≠ flatten (TimeLayer.t3, s₃) := by
  intro h
  have hlt : (flatten (TimeLayer.t2, s₂)).val < 2 * d :=
    (flatten_t2_block s₂).2
  have hge : 2 * d ≤ (flatten (TimeLayer.t3, s₃)).val :=
    (flatten_t3_block s₃).1
  have hv :
      (flatten (TimeLayer.t2, s₂)).val =
        (flatten (TimeLayer.t3, s₃)).val :=
    congrArg Fin.val h
  omega

end ProductIndex

end VFH2
