import VFH2.Product.ThreeTimeConstraintGeometry

/-!
# C115: Temporal Unity Under Shared Constraints

Past, present, and future remain distinct indices, yet their three complete
slices are the components of exactly one global state.  A family of constraints
is evaluated on that one state, and compatibility of the three slices is proved
equivalent to existence—and uniqueness—of a common constrained realizer.

Thus "the three times are one" receives a precise, non-contradictory meaning:
not equality of time labels, but unique joint realization in one fabric.
-/

namespace VFH2
namespace ThreeTime

/-- A predicate on the complete three-time fabric. -/
abbrev GlobalConstraint (n d : Nat) : Type :=
  GlobalFabricState n d → Prop

/-- A state satisfies every constraint in an indexed geometry. -/
def SatisfiesConstraintGeometry
    {ι : Type}
    {n d : Nat}
    (constraints : ι → GlobalConstraint n d)
    (x : GlobalFabricState n d) : Prop :=
  ∀ i : ι, constraints i x

/-- Three slices are compatible when their common assembly obeys the geometry. -/
def CompatibleNamedSlices
    {ι : Type}
    {n d : Nat}
    (constraints : ι → GlobalConstraint n d)
    (past present future : SpatialSlice n d) : Prop :=
  SatisfiesConstraintGeometry constraints
    (assemble past present future)

/-- Every triple of complete slices has exactly one common global realizer. -/
theorem namedSlices_have_unique_global_realizer
    {n d : Nat}
    (past present future : SpatialSlice n d) :
    ∃ x : GlobalFabricState n d,
      (pastSlice x = past ∧
        presentSlice x = present ∧
        futureSlice x = future) ∧
      ∀ y : GlobalFabricState n d,
        (pastSlice y = past ∧
          presentSlice y = present ∧
          futureSlice y = future) →
        y = x := by
  let x := assemble past present future
  refine ⟨x, ?_, ?_⟩
  · exact ⟨
      pastSlice_assemble past present future,
      presentSlice_assemble past present future,
      futureSlice_assemble past present future
    ⟩
  · intro y hy
    apply ext_namedSlices
    · calc
        pastSlice y = past := hy.1
        _ = pastSlice x :=
          (pastSlice_assemble past present future).symm
    · calc
        presentSlice y = present := hy.2.1
        _ = presentSlice x :=
          (presentSlice_assemble past present future).symm
    · calc
        futureSlice y = future := hy.2.2
        _ = futureSlice x :=
          (futureSlice_assemble past present future).symm

/--
Compatibility is exactly existence of one global state satisfying the shared
constraint geometry and realizing all three named slices.
-/
theorem compatibleNamedSlices_iff_exists_common_global_realizer
    {ι : Type}
    {n d : Nat}
    (constraints : ι → GlobalConstraint n d)
    (past present future : SpatialSlice n d) :
    CompatibleNamedSlices constraints past present future ↔
      ∃ x : GlobalFabricState n d,
        SatisfiesConstraintGeometry constraints x ∧
          pastSlice x = past ∧
          presentSlice x = present ∧
          futureSlice x = future := by
  constructor
  · intro hcompatible
    exact ⟨
      assemble past present future,
      hcompatible,
      pastSlice_assemble past present future,
      presentSlice_assemble past present future,
      futureSlice_assemble past present future
    ⟩
  · rintro ⟨x, hsatisfies, hpast, hpresent, hfuture⟩
    have hx : x = assemble past present future := by
      apply ext_namedSlices
      · simpa using hpast
      · simpa using hpresent
      · simpa using hfuture
    unfold CompatibleNamedSlices
    rw [← hx]
    exact hsatisfies

/--
A compatible triple has one and only one common realizer satisfying the shared
geometry.  No equality between the three time indices is assumed.
-/
theorem compatibleNamedSlices_unique_constrained_realizer
    {ι : Type}
    {n d : Nat}
    (constraints : ι → GlobalConstraint n d)
    (past present future : SpatialSlice n d)
    (hcompatible :
      CompatibleNamedSlices constraints past present future) :
    ∃ x : GlobalFabricState n d,
      (SatisfiesConstraintGeometry constraints x ∧
        pastSlice x = past ∧
        presentSlice x = present ∧
        futureSlice x = future) ∧
      ∀ y : GlobalFabricState n d,
        (SatisfiesConstraintGeometry constraints y ∧
          pastSlice y = past ∧
          presentSlice y = present ∧
          futureSlice y = future) →
        y = x := by
  let x := assemble past present future
  refine ⟨x, ?_, ?_⟩
  · exact ⟨
      hcompatible,
      pastSlice_assemble past present future,
      presentSlice_assemble past present future,
      futureSlice_assemble past present future
    ⟩
  · intro y hy
    apply ext_namedSlices
    · calc
        pastSlice y = past := hy.2.1
        _ = pastSlice x :=
          (pastSlice_assemble past present future).symm
    · calc
        presentSlice y = present := hy.2.2.1
        _ = presentSlice x :=
          (presentSlice_assemble past present future).symm
    · calc
        futureSlice y = future := hy.2.2.2
        _ = futureSlice x :=
          (futureSlice_assemble past present future).symm

/--
The exact temporal-unity statement: distinct layer labels coexist with lossless
reconstruction of every state from the three components of that one state.
-/
theorem distinct_named_times_form_one_reconstructible_fabric
    (n d : Nat) :
    (TimeLayer.t1 ≠ TimeLayer.t2 ∧
      TimeLayer.t1 ≠ TimeLayer.t3 ∧
      TimeLayer.t2 ≠ TimeLayer.t3) ∧
      ∀ x : GlobalFabricState n d,
        assemble (pastSlice x) (presentSlice x) (futureSlice x) = x := by
  exact ⟨named_timeLayers_pairwise_distinct, assemble_namedSlices⟩

end ThreeTime
end VFH2
