import VFH2.Product.ProductIndex
import VFH2.Typed.WidthIndex

/-!
# VF-H2 v11 Product-to-Width Flattening

This file introduces the first formal bridge from the v11 explicit
product index

  TimeLayer × SpaceIndex d

to the v10 flattened width index

  WidthIndex d = Fin (3 * d).

Boundary:
- This is an index-level bridge only.
- It does not prove ledger equivalence.
- It does not prove product/typed state equivalence.
- It does not prove the full VF-H2 theory.
- It does not prove unrestricted TTP-VF-H2-004.
-/

namespace VFH2

namespace ProductIndex

/--
Flatten a v11 explicit product index into the v10 flattened width index.

The encoding is row-major by time layer:

  (t, s) ↦ t.val * d + s.val

where `t : Fin 3` and `s : Fin d`.

The bound is proved without case-splitting on the three time layers:
since `s < d`, we have

  t*d + s < t*d + d = (t+1)*d,

and since `t < 3`, we have `(t+1)*d ≤ 3*d`.
-/
def flatten {d : Nat} (i : ProductIndex d) : Typed.WidthIndex d :=
  ⟨i.1.val * d + i.2.val, by
    have ht : i.1.val < 3 := i.1.isLt
    have hs : i.2.val < d := i.2.isLt

    have hblock : i.1.val + 1 ≤ 3 := by
      omega

    have hstep :
        i.1.val * d + i.2.val < i.1.val * d + d :=
      Nat.add_lt_add_left hs (i.1.val * d)

    have hnext :
        i.1.val * d + d = (i.1.val + 1) * d := by
      simp [Nat.add_mul]

    have hupper :
        (i.1.val + 1) * d ≤ 3 * d :=
      Nat.mul_le_mul_right d hblock

    exact Nat.lt_of_lt_of_le (by simpa [hnext] using hstep) hupper⟩

/--
The numeric value of the flattened index is exactly the row-major
time-space encoding.
-/
@[simp]
theorem flatten_val {d : Nat} (i : ProductIndex d) :
    (flatten i).val = i.1.val * d + i.2.val := by
  rfl

/--
Constructor form of `flatten_val`.
-/
@[simp]
theorem flatten_mk_val {d : Nat} (t : TimeLayer) (s : SpaceIndex d) :
    (flatten (t, s)).val = t.val * d + s.val := by
  rfl

/--
A flattened product index is always inside the v10 width domain.
-/
theorem flatten_lt_width {d : Nat} (i : ProductIndex d) :
    (flatten i).val < 3 * d := by
  exact (flatten i).isLt

/--
The first explicit time layer occupies the first spatial block.
-/
@[simp]
theorem flatten_t1_val {d : Nat} (s : SpaceIndex d) :
    (flatten (TimeLayer.t1, s)).val = s.val := by
  simp [flatten]

/--
The second explicit time layer occupies the second spatial block.
-/
@[simp]
theorem flatten_t2_val {d : Nat} (s : SpaceIndex d) :
    (flatten (TimeLayer.t2, s)).val = d + s.val := by
  simp [flatten]

/--
The third explicit time layer occupies the third spatial block.
-/
@[simp]
theorem flatten_t3_val {d : Nat} (s : SpaceIndex d) :
    (flatten (TimeLayer.t3, s)).val = 2 * d + s.val := by
  simp [flatten]

end ProductIndex

end VFH2
