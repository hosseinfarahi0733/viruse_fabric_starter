import VFH2.Product.ProductStateTransport

/-!
# VF-H2 v11 Unflatten Block Lemmas

This file proves block-specific facts about `ProductIndex.unflatten`.

Boundary:
- This is an index/state-transport helper layer.
- It does not prove ledger equivalence.
- It does not prove ledger-effect equivalence.
- It does not prove update equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductUnflattenBlocks

/--
If a flattened width index is in the first block `[0, d)`,
then `unflatten` maps it to the first time layer.
-/
theorem unflatten_of_lt_d
    {d : Nat}
    (w : Typed.WidthIndex d)
    (h : w.val < d) :
    ProductIndex.unflatten w = (TimeLayer.t1, ⟨w.val, h⟩) := by
  simp [ProductIndex.unflatten, h]

/--
If a flattened width index is in the second block `[d, 2*d)`,
then `unflatten` maps it to the second time layer.
-/
theorem unflatten_of_ge_d_lt_two_mul
    {d : Nat}
    (w : Typed.WidthIndex d)
    (hge : d ≤ w.val)
    (hlt : w.val < 2 * d) :
    ProductIndex.unflatten w =
      (TimeLayer.t2, ⟨w.val - d, by omega⟩) := by
  have hnot : ¬ w.val < d := by
    omega
  simp [ProductIndex.unflatten, hnot, hlt]

/--
If a flattened width index is in the third block `[2*d, 3*d)`,
then `unflatten` maps it to the third time layer.
-/
theorem unflatten_of_ge_two_mul
    {d : Nat}
    (w : Typed.WidthIndex d)
    (hge : 2 * d ≤ w.val) :
    ProductIndex.unflatten w =
      (TimeLayer.t3, ⟨w.val - 2 * d, by
        have hw : w.val < 3 * d := w.isLt
        omega⟩) := by
  have hnot1 : ¬ w.val < d := by
    omega
  have hnot2 : ¬ w.val < 2 * d := by
    omega
  simp [ProductIndex.unflatten, hnot1, hnot2]

/--
Value read through `productToTyped` in the first width block.
-/
theorem productToTyped_val_of_lt_d
    {n d : Nat}
    (x : ProductTypedState n d)
    (w : Typed.WidthIndex d)
    (h : w.val < d) :
    (ProductStateTransport.productToTyped x w).val =
      (x (TimeLayer.t1, ⟨w.val, h⟩)).val := by
  unfold ProductStateTransport.productToTyped
  rw [unflatten_of_lt_d w h]

/--
Value read through `productToTyped` in the second width block.
-/
theorem productToTyped_val_of_ge_d_lt_two_mul
    {n d : Nat}
    (x : ProductTypedState n d)
    (w : Typed.WidthIndex d)
    (hge : d ≤ w.val)
    (hlt : w.val < 2 * d) :
    (ProductStateTransport.productToTyped x w).val =
      (x (TimeLayer.t2, ⟨w.val - d, by omega⟩)).val := by
  unfold ProductStateTransport.productToTyped
  rw [unflatten_of_ge_d_lt_two_mul w hge hlt]

/--
Value read through `productToTyped` in the third width block.
-/
theorem productToTyped_val_of_ge_two_mul
    {n d : Nat}
    (x : ProductTypedState n d)
    (w : Typed.WidthIndex d)
    (hge : 2 * d ≤ w.val) :
    (ProductStateTransport.productToTyped x w).val =
      (x (TimeLayer.t3, ⟨w.val - 2 * d, by
        have hw : w.val < 3 * d := w.isLt
        omega⟩)).val := by
  unfold ProductStateTransport.productToTyped
  rw [unflatten_of_ge_two_mul w hge]

end ProductUnflattenBlocks

end VFH2
