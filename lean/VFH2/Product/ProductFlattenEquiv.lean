import VFH2.Product.ProductFlattenFullInjective

/-!
# VF-H2 v11 Product/Width Index Equivalence

This file defines an inverse map from the v10 flattened width index

  WidthIndex d = Fin (3 * d)

back to the v11 explicit product index

  TimeLayer × SpaceIndex d

and proves the two round-trip laws.

Boundary:
- This is an index-level equivalence only.
- It does not prove ledger equivalence.
- It does not prove state equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductIndex

/--
Unflatten a v10 width index into the v11 explicit product index.

The inverse uses the same three-block layout as `flatten`:

  [0, d)     ↦ t1
  [d, 2*d)   ↦ t2
  [2*d, 3*d) ↦ t3

This definition is total. For `d = 0`, the input type `WidthIndex 0`
is empty, so the impossible branches are discharged by arithmetic.
-/
def unflatten {d : Nat} (w : Typed.WidthIndex d) : ProductIndex d :=
  if h1 : w.val < d then
    (TimeLayer.t1, ⟨w.val, h1⟩)
  else if h2 : w.val < 2 * d then
    (TimeLayer.t2, ⟨w.val - d, by
      have hd : d ≤ w.val := Nat.le_of_not_gt h1
      omega⟩)
  else
    (TimeLayer.t3, ⟨w.val - 2 * d, by
      have h2le : 2 * d ≤ w.val := Nat.le_of_not_gt h2
      have hw : w.val < 3 * d := w.isLt
      omega⟩)

/--
Flattening after unflattening returns the original width index.
-/
theorem flatten_unflatten {d : Nat}
    (w : Typed.WidthIndex d) :
    flatten (unflatten w) = w := by
  apply Fin.ext
  by_cases h1 : w.val < d
  · simp [unflatten, h1]
  · by_cases h2 : w.val < 2 * d
    · have hd : d ≤ w.val := Nat.le_of_not_gt h1
      simp [unflatten, h1, h2]
      omega
    · have h2le : 2 * d ≤ w.val := Nat.le_of_not_gt h2
      have hw : w.val < 3 * d := w.isLt
      simp [unflatten, h1, h2]
      omega

/--
Unflattening after flattening returns the original product index.
-/
theorem unflatten_flatten {d : Nat}
    (i : ProductIndex d) :
    unflatten (flatten i) = i := by
  apply flatten_injective
  exact flatten_unflatten (flatten i)

/--
A local equivalence package between the explicit product index and
the flattened width index.

We define this locally instead of relying on a global `Equiv` type,
because the current project import set does not expose `Equiv`.
-/
structure ProductWidthIndexEquiv (d : Nat) where
  toWidth : ProductIndex d → Typed.WidthIndex d
  toProduct : Typed.WidthIndex d → ProductIndex d
  left_inv : ∀ i : ProductIndex d, toProduct (toWidth i) = i
  right_inv : ∀ w : Typed.WidthIndex d, toWidth (toProduct w) = w

/--
The explicit product index and the flattened width index are equivalent
through `flatten` and `unflatten`.
-/
def flattenEquiv (d : Nat) : ProductWidthIndexEquiv d where
  toWidth := flatten
  toProduct := unflatten
  left_inv := unflatten_flatten
  right_inv := flatten_unflatten

/--
The equivalence's forward map is the product-to-width flatten map.
-/
@[simp]
theorem flattenEquiv_toWidth {d : Nat} (i : ProductIndex d) :
    (flattenEquiv d).toWidth i = flatten i := by
  rfl

/--
The equivalence's inverse map is the width-to-product unflatten map.
-/
@[simp]
theorem flattenEquiv_toProduct {d : Nat} (w : Typed.WidthIndex d) :
    (flattenEquiv d).toProduct w = unflatten w := by
  rfl

/--
Left inverse law exposed through the local equivalence package.
-/
theorem flattenEquiv_left_inv {d : Nat} (i : ProductIndex d) :
    (flattenEquiv d).toProduct ((flattenEquiv d).toWidth i) = i := by
  exact (flattenEquiv d).left_inv i

/--
Right inverse law exposed through the local equivalence package.
-/
theorem flattenEquiv_right_inv {d : Nat} (w : Typed.WidthIndex d) :
    (flattenEquiv d).toWidth ((flattenEquiv d).toProduct w) = w := by
  exact (flattenEquiv d).right_inv w

end ProductIndex

end VFH2
