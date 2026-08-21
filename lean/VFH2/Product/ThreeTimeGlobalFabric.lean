import VFH2.Product.ProductState

/-!
# C112: Three-Time Global Fabric

This module identifies the existing product state with one global state over
three explicit time layers and proves exact decomposition and reconstruction.

The word "one" means one common global state with three distinct projections;
it does not identify the three time indices or assert equality of their values.

Boundary: these are structural theorems for the stated finite typed model. They
are not empirical evidence and do not prove a physical theory of time.
-/

namespace VFH2
namespace ThreeTime

/-- One global state indexed by explicit time and space. -/
abbrev GlobalFabricState (n d : Nat) : Type :=
  ProductTypedState n d

/-- The state visible on one spatial slice. -/
abbrev SpatialSlice (n d : Nat) : Type :=
  SpaceIndex d → Typed.BoundedCoord n

/-- Every three-valued time index is one of the named layers. -/
theorem timeLayer_eq_t1_or_t2_or_t3 (t : TimeLayer) :
    t = TimeLayer.t1 ∨ t = TimeLayer.t2 ∨ t = TimeLayer.t3 := by
  rcases t with ⟨v, hv⟩
  have hv_cases : v = 0 ∨ v = 1 ∨ v = 2 := by
    omega
  rcases hv_cases with h0 | hrest
  · left
    apply Fin.ext
    simpa [TimeLayer.t1] using h0
  · rcases hrest with h1 | h2
    · right
      left
      apply Fin.ext
      simpa [TimeLayer.t2] using h1
    · right
      right
      apply Fin.ext
      simpa [TimeLayer.t3] using h2

@[simp] theorem t1_ne_t2 : TimeLayer.t1 ≠ TimeLayer.t2 := by decide
@[simp] theorem t2_ne_t1 : TimeLayer.t2 ≠ TimeLayer.t1 := by decide
@[simp] theorem t1_ne_t3 : TimeLayer.t1 ≠ TimeLayer.t3 := by decide
@[simp] theorem t3_ne_t1 : TimeLayer.t3 ≠ TimeLayer.t1 := by decide
@[simp] theorem t2_ne_t3 : TimeLayer.t2 ≠ TimeLayer.t3 := by decide
@[simp] theorem t3_ne_t2 : TimeLayer.t3 ≠ TimeLayer.t2 := by decide

/-- The past, present, and future indices are pairwise distinct. -/
theorem named_timeLayers_pairwise_distinct :
    TimeLayer.t1 ≠ TimeLayer.t2 ∧
      TimeLayer.t1 ≠ TimeLayer.t3 ∧
      TimeLayer.t2 ≠ TimeLayer.t3 :=
  ⟨t1_ne_t2, t1_ne_t3, t2_ne_t3⟩

/-- Project one time slice from the common global fabric. -/
def slice
    {n d : Nat}
    (x : GlobalFabricState n d)
    (t : TimeLayer) : SpatialSlice n d :=
  fun s => x (t, s)

/-- First named projection (past). -/
def pastSlice {n d : Nat} (x : GlobalFabricState n d) : SpatialSlice n d :=
  slice x TimeLayer.t1

/-- Second named projection (present). -/
def presentSlice {n d : Nat} (x : GlobalFabricState n d) : SpatialSlice n d :=
  slice x TimeLayer.t2

/-- Third named projection (future). -/
def futureSlice {n d : Nat} (x : GlobalFabricState n d) : SpatialSlice n d :=
  slice x TimeLayer.t3

/-- Assemble three named slices into one common global state. -/
def assemble
    {n d : Nat}
    (past present future : SpatialSlice n d) : GlobalFabricState n d :=
  fun i =>
    if i.1 = TimeLayer.t1 then
      past i.2
    else if i.1 = TimeLayer.t2 then
      present i.2
    else
      future i.2

@[simp]
theorem pastSlice_assemble
    {n d : Nat}
    (past present future : SpatialSlice n d) :
    pastSlice (assemble past present future) = past := by
  funext s
  simp [pastSlice, slice, assemble]

@[simp]
theorem presentSlice_assemble
    {n d : Nat}
    (past present future : SpatialSlice n d) :
    presentSlice (assemble past present future) = present := by
  funext s
  simp [presentSlice, slice, assemble]

@[simp]
theorem futureSlice_assemble
    {n d : Nat}
    (past present future : SpatialSlice n d) :
    futureSlice (assemble past present future) = future := by
  funext s
  simp [futureSlice, slice, assemble]

/-- Projecting all three slices and reassembling loses no global information. -/
theorem assemble_namedSlices
    {n d : Nat}
    (x : GlobalFabricState n d) :
    assemble (pastSlice x) (presentSlice x) (futureSlice x) = x := by
  funext i
  rcases i with ⟨t, s⟩
  rcases timeLayer_eq_t1_or_t2_or_t3 t with ht1 | htRest
  · subst t
    simp [assemble, pastSlice, slice]
  · rcases htRest with ht2 | ht3
    · subst t
      simp [assemble, presentSlice, slice]
    · subst t
      simp [assemble, futureSlice, slice]

/-- Equality of the three named projections determines the whole state. -/
theorem ext_namedSlices
    {n d : Nat}
    {x y : GlobalFabricState n d}
    (hpast : pastSlice x = pastSlice y)
    (hpresent : presentSlice x = presentSlice y)
    (hfuture : futureSlice x = futureSlice y) :
    x = y := by
  calc
    x = assemble (pastSlice x) (presentSlice x) (futureSlice x) :=
      (assemble_namedSlices x).symm
    _ = assemble (pastSlice y) (presentSlice y) (futureSlice y) := by
      rw [hpast, hpresent, hfuture]
    _ = y := assemble_namedSlices y

/-- The named three-slice representation. -/
structure NamedSlices (n d : Nat) where
  past : SpatialSlice n d
  present : SpatialSlice n d
  future : SpatialSlice n d

/-- Project a global state to its three named components. -/
def projectNamedSlices
    {n d : Nat}
    (x : GlobalFabricState n d) : NamedSlices n d where
  past := pastSlice x
  present := presentSlice x
  future := futureSlice x

/-- Assemble a named three-slice record. -/
def assembleNamedSlices
    {n d : Nat}
    (s : NamedSlices n d) : GlobalFabricState n d :=
  assemble s.past s.present s.future

/-- The exact two-sided correspondence, local to this dependency-light project. -/
structure GlobalFabricNamedSlicesEquiv (n d : Nat) where
  toSlices : GlobalFabricState n d → NamedSlices n d
  toGlobal : NamedSlices n d → GlobalFabricState n d
  left_inv : ∀ x, toGlobal (toSlices x) = x
  right_inv : ∀ s, toSlices (toGlobal s) = s

/-- Global states and named triples are exactly equivalent representations. -/
def globalFabricEquivNamedSlices (n d : Nat) :
    GlobalFabricNamedSlicesEquiv n d where
  toSlices := projectNamedSlices
  toGlobal := assembleNamedSlices
  left_inv := assemble_namedSlices
  right_inv := by
    intro s
    cases s
    simp [projectNamedSlices, assembleNamedSlices]

end ThreeTime
end VFH2
