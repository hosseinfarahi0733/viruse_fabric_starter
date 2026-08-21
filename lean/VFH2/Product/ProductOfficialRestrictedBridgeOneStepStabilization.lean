import VFH2.RestrictedBridge.WellFormedParams

/-!
# VF-H2 Product/Official Restricted-Bridge One-Step Stabilization

This Product-track module proves intrinsic one-step semantics for the official
list-backed restricted model.  It shows that the update preserves the
restricted state space, characterizes fixed points when active indices are in
range, and is idempotent for arbitrary raw parameters and states.

The active-index range hypothesis in the reverse fixed-point direction is
necessary for the list-backed model: an active index outside a short list is
not visited by the update.

This is restricted finite-model formalization.  It is not unrestricted
`TTP-VF-H2-004`, and it is not full-theory, empirical, or biological
validation.
-/

namespace VFH2
namespace RestrictedBridge

private theorem updateCoordinateR_le_top
    (p : RestrictedParams)
    (i a : Nat)
    (ha : a ≤ p.n) :
    updateCoordinateR p i a ≤ p.n := by
  unfold updateCoordinateR
  split
  · exact Nat.le_refl p.n
  · exact ha

private theorem updateStateAuxR_preserves_hasLnBounds
    (p : RestrictedParams)
    (base : Nat)
    (x : State)
    (hb : hasLnBounds p x) :
    hasLnBounds p (updateStateAuxR p base x) := by
  unfold hasLnBounds at hb ⊢
  induction x generalizing base with
  | nil =>
      simp [updateStateAuxR]
  | cons a xs ih =>
      intro b hbmem
      simp only [updateStateAuxR, List.mem_cons] at hbmem
      rcases hbmem with hhead | htail
      · subst b
        exact updateCoordinateR_le_top p base a (hb a (by simp))
      · exact ih
          (base := base + 1)
          (fun c hc => hb c (by simp [hc]))
          b
          htail

/-- The official update preserves coordinate bounds without any active-range
or width assumption.
-/
theorem updateStateR_preserves_hasLnBounds
    {p : RestrictedParams}
    {x : State}
    (hb : hasLnBounds p x) :
    hasLnBounds p (updateStateR p x) := by
  unfold updateStateR
  exact updateStateAuxR_preserves_hasLnBounds p 0 x hb

/-- The official update is closed on the restricted state space. -/
theorem updateStateR_preserves_inRestrictedStateSpace
    {p : RestrictedParams}
    {x : State}
    (hspace : inRestrictedStateSpace p x) :
    inRestrictedStateSpace p (updateStateR p x) := by
  exact
    ⟨updateStateR_preserves_expected_width hspace.1,
      updateStateR_preserves_hasLnBounds hspace.2⟩

/-- Every official fixed-set state is unchanged by the official update. -/
theorem updateStateR_eq_self_of_inFixedSetR
    (p : RestrictedParams)
    (x : State)
    (hfixed : inFixedSetR p x) :
    updateStateR p x = x := by
  exact
    updateStateR_eq_self_of_membershipTopForUpdate
      p
      x
      (activeIndexSound_of_isActiveIndex p)
      (membershipTopForUpdate_of_inFixedSetR p x hfixed)

private theorem updateCoordinateR_idempotent
    (p : RestrictedParams)
    (i a : Nat) :
    updateCoordinateR p i (updateCoordinateR p i a) =
      updateCoordinateR p i a := by
  unfold updateCoordinateR
  split <;> simp_all

private theorem updateStateAuxR_idempotent
    (p : RestrictedParams)
    (base : Nat)
    (x : State) :
    updateStateAuxR p base (updateStateAuxR p base x) =
      updateStateAuxR p base x := by
  induction x generalizing base with
  | nil =>
      simp [updateStateAuxR]
  | cons a xs ih =>
      simp only [updateStateAuxR]
      rw [updateCoordinateR_idempotent]
      rw [ih]

/-- Applying the official update twice is the same as applying it once.

This holds for arbitrary raw restricted parameters and arbitrary list states;
no width, bounds, or active-range assumption is required.
-/
theorem updateStateR_idempotent
    (p : RestrictedParams)
    (x : State) :
    updateStateR p (updateStateR p x) = updateStateR p x := by
  unfold updateStateR
  exact updateStateAuxR_idempotent p 0 x

private theorem updateStateAuxR_getElem?
    (p : RestrictedParams)
    (x : State)
    (base i : Nat) :
    (updateStateAuxR p base x)[i]? =
      x[i]?.map (updateCoordinateR p (base + i)) := by
  induction x generalizing base i with
  | nil =>
      simp [updateStateAuxR]
  | cons a xs ih =>
      cases i with
      | zero =>
          simp [updateStateAuxR]
      | succ i =>
          simpa [
            updateStateAuxR,
            Nat.succ_eq_add_one,
            Nat.add_assoc,
            Nat.add_comm,
            Nat.add_left_comm
          ] using ih (base := base + 1) (i := i)

/-- Coordinate lookup through the official list-backed update. -/
theorem updateStateR_getElem?_eq_map
    (p : RestrictedParams)
    (x : State)
    (i : Nat) :
    (updateStateR p x)[i]? =
      x[i]?.map (updateCoordinateR p i) := by
  simpa [updateStateR] using updateStateAuxR_getElem? p x 0 i

/--
For states whose active indices are actually represented in the list, the
official fixed-set predicate is exactly the fixed-point predicate of the
official update.
-/
theorem inFixedSetR_iff_updateStateR_eq_self_of_activeIndicesInRange
    {p : RestrictedParams}
    {x : State}
    (hrange : activeIndicesInRange p x) :
    inFixedSetR p x ↔ updateStateR p x = x := by
  constructor
  · exact updateStateR_eq_self_of_inFixedSetR p x
  · intro hupdate
    intro i hi
    have hirange : i < x.length := hrange i hi
    have hget :
        (updateStateR p x)[i]? = x[i]? :=
      congrArg (fun y : State => y[i]?) hupdate
    rw [updateStateR_getElem?_eq_map] at hget
    rw [List.getElem?_eq_getElem hirange] at hget
    simp only [Option.map_some, Option.some.injEq] at hget
    have hactive : isActiveIndex p i = true := by
      simp [isActiveIndex, hi]
    have htop :
        updateCoordinateR p i x[i] = p.n :=
      updateCoordinateR_active p i x[i] hactive
    have hx : x[i] = p.n := by
      calc
        x[i] = updateCoordinateR p i x[i] := hget.symm
        _ = p.n := htop
    rw [List.getD_eq_getElem?_getD]
    rw [List.getElem?_eq_getElem hirange]
    exact hx

/-- If all active indices are represented, one official update lands in the
official fixed set.
-/
theorem updateStateR_inFixedSetR_of_activeIndicesInRange
    {p : RestrictedParams}
    {x : State}
    (hrange : activeIndicesInRange p x) :
    inFixedSetR p (updateStateR p x) := by
  have hrangeUpdate :
      activeIndicesInRange p (updateStateR p x) := by
    intro i hi
    rw [updateStateR_length]
    exact hrange i hi
  exact
    (inFixedSetR_iff_updateStateR_eq_self_of_activeIndicesInRange
      hrangeUpdate).2
      (updateStateR_idempotent p x)

/-- Over well-formed parameters and an official state-space input, fixed-set
membership is exactly the official fixed-point condition.
-/
theorem inFixedSetR_iff_updateStateR_eq_self_of_WellFormedRestrictedParams
    (wp : WellFormedRestrictedParams)
    {x : State}
    (hspace : inRestrictedStateSpace wp.params x) :
    inFixedSetR wp.params x ↔ updateStateR wp.params x = x := by
  exact
    inFixedSetR_iff_updateStateR_eq_self_of_activeIndicesInRange
      (activeIndicesInRange_of_WellFormedRestrictedParams hspace)

/-- One update of a well-formed official input lands in the official fixed
set.
-/
theorem updateStateR_inFixedSetR_of_WellFormedRestrictedParams
    (wp : WellFormedRestrictedParams)
    {x : State}
    (hspace : inRestrictedStateSpace wp.params x) :
    inFixedSetR wp.params (updateStateR wp.params x) := by
  exact
    updateStateR_inFixedSetR_of_activeIndicesInRange
      (activeIndicesInRange_of_WellFormedRestrictedParams hspace)

end RestrictedBridge
end VFH2
