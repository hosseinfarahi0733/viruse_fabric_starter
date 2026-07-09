import VFH2.Product.ProductRestrictedParamsActiveCustomEnumKernel
import VFH2.Product.ProductRestrictedParamsActiveNoncoverageCertificate

namespace VFH2
open ProductRestrictedParamsActiveCustomEnumKernel
namespace ProductRestrictedParamsActiveLengthLowerBound

/-- Convert a disequality into the corresponding `BEq` false branch.

This is local infrastructure because the current project environment does not expose the
standard helper names needed by the C34T route. -/
theorem beq_false_of_ne_local
    {α : Type} [BEq α] [LawfulBEq α]
    {x a : α} (hne : x ≠ a) :
    (x == a) = false := by
  cases h : (x == a)
  · rfl
  · exfalso
    apply hne
    simpa using h

/-- If `b ≠ a` and `b` occurs in a list, then `b` still occurs after erasing `a`.

This replaces unavailable `List.mem_erase_of_ne_of_mem`-style helpers in the current
Lean/Std environment. -/
theorem mem_erase_of_ne_of_mem_local
    {α : Type} [BEq α] [LawfulBEq α]
    {a b : α} {xs : List α}
    (hne : b ≠ a)
    (hmem : b ∈ xs) :
    b ∈ xs.erase a := by
  induction xs with
  | nil =>
      cases hmem
  | cons x xs ih =>
      rw [List.mem_cons] at hmem
      rcases hmem with hb_eq_x | hb_tail
      · subst b
        have hxFalse : (x == a) = false := beq_false_of_ne_local hne
        simp [List.erase, hxFalse]
      · by_cases hxa : x = a
        · subst a
          simp [List.erase, hb_tail]
        · have hxFalse : (x == a) = false := beq_false_of_ne_local hxa
          have hbErase : b ∈ xs.erase a := ih hb_tail
          simp [List.erase, hxFalse, hbErase]

/-- A local cardinality kernel: a noduplicate list whose elements all occur in another
list has length bounded by the second list.

This is the exact list theorem isolated by C34T and proved by the C34W BEq/erase route. -/
theorem length_le_of_nodup_and_mem_subset_beq
    {α : Type} [BEq α] [LawfulBEq α]
    {xs ys : List α}
    (hnd : xs.Nodup)
    (hmem : ∀ a : α, a ∈ xs → a ∈ ys) :
    xs.length ≤ ys.length := by
  induction xs generalizing ys with
  | nil =>
      simp
  | cons a xs ih =>
      have hparts := List.nodup_cons.mp hnd
      have ha_mem_ys : a ∈ ys := hmem a (by simp)
      have hmem_tail_erase : ∀ b : α, b ∈ xs → b ∈ ys.erase a := by
        intro b hb
        have hb_mem_ys : b ∈ ys := hmem b (by simp [hb])
        have hb_ne_a : b ≠ a := by
          intro hba
          have ha_in_xs : a ∈ xs := by
            simpa [hba] using hb
          exact hparts.left ha_in_xs
        exact mem_erase_of_ne_of_mem_local hb_ne_a hb_mem_ys
      have htail : xs.length ≤ (ys.erase a).length :=
        ih hparts.right hmem_tail_erase
      have hlenErase : (ys.erase a).length = ys.length - 1 :=
        List.length_erase_of_mem ha_mem_ys
      have hpos : 0 < ys.length := by
        cases ys with
        | nil => cases ha_mem_ys
        | cons _ _ => simp
      change xs.length.succ ≤ ys.length
      omega

/-- Structural source: the active list is strictly shorter than the full flattened
product-width enumeration. -/
structure ActiveLengthLtTypedWidthSource (p : ProductRestrictedParams) : Type where
  active_length_lt_typedWidth : p.active.length < Typed.typedWidth p.d

/-- If every product index is active, the active list must be at least as long as the
complete noduplicate product-index enumeration. -/
theorem typedWidth_le_active_length_of_all_active
    (p : ProductRestrictedParams)
    (hAll : ∀ i : ProductIndex p.d, i ∈ p.active) :
    Typed.typedWidth p.d ≤ p.active.length := by
  have hle : (productIndexEnum p.d).length ≤ p.active.length :=
    length_le_of_nodup_and_mem_subset_beq
      (productIndexEnum_nodup p.d)
      (fun i _hi => hAll i)
  rw [productIndexEnum_length_typedWidth] at hle
  exact hle

/-- Strict active-length deficit implies not all product indices are active. -/
theorem not_all_active_of_active_length_lt_typedWidth
    (p : ProductRestrictedParams)
    (src : ActiveLengthLtTypedWidthSource p) :
    ¬ ∀ i : ProductIndex p.d, i ∈ p.active := by
  intro hAll
  have hle : Typed.typedWidth p.d ≤ p.active.length :=
    typedWidth_le_active_length_of_all_active p hAll
  exact (Nat.not_lt_of_ge hle) src.active_length_lt_typedWidth

/-- Build the existing active noncoverage certificate from the structural active-length
source, removing the need to assume `¬ ∀ i, i ∈ p.active` directly on this route. -/
def activeNoncoverageCertificate_of_active_length_lt_typedWidth
    (p : ProductRestrictedParams)
    (src : ActiveLengthLtTypedWidthSource p) :
    ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate p :=
  ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate.of_not_all_active p
    (not_all_active_of_active_length_lt_typedWidth p src)

#check beq_false_of_ne_local
#check mem_erase_of_ne_of_mem_local
#check length_le_of_nodup_and_mem_subset_beq
#check ActiveLengthLtTypedWidthSource
#check typedWidth_le_active_length_of_all_active
#check not_all_active_of_active_length_lt_typedWidth
#check activeNoncoverageCertificate_of_active_length_lt_typedWidth

end ProductRestrictedParamsActiveLengthLowerBound
end VFH2
