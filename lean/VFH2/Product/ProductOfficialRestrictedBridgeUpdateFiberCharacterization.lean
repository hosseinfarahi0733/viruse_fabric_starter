import VFH2.Product.ProductOfficialRestrictedBridgeOneStepStabilization

/-!
# Official Restricted-Bridge Update Fiber Characterization

This module characterizes the fibers of the official list-backed restricted
update.  Two raw list states have the same update exactly when they have the
same length and agree at every inactive coordinate.  On the official
restricted state space, equal length is automatic and the characterization can
be stated directly with `getD`.

As a semantic consequence, an arbitrary score is preserved by the official
update on its restricted state space exactly when the score cannot distinguish
states that agree at every inactive coordinate.

Boundary:
- This concerns only the official finite list-backed restricted model.
- It introduces no parameter, state-space, score, or well-formedness
  assumption.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/--
Two official updates are equal exactly when the source lists have the same
length and agree at every inactive coordinate.
-/
theorem updateStateR_eq_updateStateR_iff_length_eq_and_inactive_getElem_eq
    (p : RestrictedParams)
    (x z : State) :
    updateStateR p x = updateStateR p z ↔
      x.length = z.length ∧
        ∀ i : Nat, i ∉ p.active → x[i]? = z[i]? := by
  constructor
  · intro hUpdate
    constructor
    · have hLength := congrArg List.length hUpdate
      simpa only [updateStateR_length] using hLength
    · intro i hi
      have hInactiveBool : isActiveIndex p i = false := by
        unfold isActiveIndex
        simp [hi]
      have hCoordinate :
          updateCoordinateR p i = id := by
        funext a
        exact updateCoordinateR_inactive p i a hInactiveBool
      have hGet :=
        congrArg (fun y : State => y[i]?) hUpdate
      rw [
        updateStateR_getElem?_eq_map,
        updateStateR_getElem?_eq_map
      ] at hGet
      rw [hCoordinate] at hGet
      simpa using hGet
  · rintro ⟨hLength, hInactive⟩
    apply List.ext_getElem?
    intro i
    rw [
      updateStateR_getElem?_eq_map,
      updateStateR_getElem?_eq_map
    ]
    by_cases hi : i ∈ p.active
    · have hActiveBool : isActiveIndex p i = true := by
        unfold isActiveIndex
        simp [hi]
      by_cases hxRange : i < x.length
      · have hzRange : i < z.length := by
          rw [← hLength]
          exact hxRange
        rw [
          List.getElem?_eq_getElem hxRange,
          List.getElem?_eq_getElem hzRange
        ]
        simp [updateCoordinateR, hActiveBool]
      · have hzRange : ¬ i < z.length := by
          intro hz
          apply hxRange
          rw [hLength]
          exact hz
        simp [
          Nat.le_of_not_gt hxRange,
          Nat.le_of_not_gt hzRange
        ]
    · have hInactiveBool : isActiveIndex p i = false := by
        unfold isActiveIndex
        simp [hi]
      have hCoordinate :
          updateCoordinateR p i = id := by
        funext a
        exact updateCoordinateR_inactive p i a hInactiveBool
      rw [hCoordinate]
      simpa using hInactive i hi

/--
Within the official restricted state space, two updates are equal exactly when
the source states have equal `getD` values at every inactive coordinate.
-/
theorem updateStateR_eq_updateStateR_iff_inactive_getD_eq_of_inRestrictedStateSpace
    {p : RestrictedParams}
    {x z : State}
    (hxSpace : inRestrictedStateSpace p x)
    (hzSpace : inRestrictedStateSpace p z) :
    updateStateR p x = updateStateR p z ↔
      ∀ i : Nat, i ∉ p.active → x.getD i 0 = z.getD i 0 := by
  constructor
  · intro hUpdate i hi
    have hFiber :=
      (updateStateR_eq_updateStateR_iff_length_eq_and_inactive_getElem_eq
        p x z).mp hUpdate
    rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD]
    rw [hFiber.2 i hi]
  · intro hInactive
    apply
      (updateStateR_eq_updateStateR_iff_length_eq_and_inactive_getElem_eq
        p x z).mpr
    have hLength : x.length = z.length :=
      hxSpace.1.trans hzSpace.1.symm
    refine ⟨hLength, ?_⟩
    intro i hi
    by_cases hxRange : i < x.length
    · have hzRange : i < z.length := by
        rw [← hLength]
        exact hxRange
      rw [
        List.getElem?_eq_getElem hxRange,
        List.getElem?_eq_getElem hzRange
      ]
      apply congrArg some
      simpa [
        List.getD_eq_getElem?_getD,
        List.getElem?_eq_getElem hxRange,
        List.getElem?_eq_getElem hzRange
      ] using hInactive i hi
    · have hzRange : ¬ i < z.length := by
        intro hz
        apply hxRange
        rw [hLength]
        exact hz
      simp [
        Nat.le_of_not_gt hxRange,
        Nat.le_of_not_gt hzRange
      ]

/--
On the official restricted state space, pointwise score preservation by
`updateStateR` is exactly inactive-coordinate score semantics.
-/
theorem updateStateR_score_preserved_on_stateSpace_iff_inactive_getD_insensitive
    {α : Type}
    (p : RestrictedParams)
    (score : State → α) :
    (∀ x : State,
      inRestrictedStateSpace p x →
        score (updateStateR p x) = score x)
      ↔
    (∀ x z : State,
      inRestrictedStateSpace p x →
      inRestrictedStateSpace p z →
      (∀ i : Nat, i ∉ p.active → x.getD i 0 = z.getD i 0) →
        score x = score z) := by
  constructor
  · intro hPreserved x z hxSpace hzSpace hInactive
    have hUpdates :
        updateStateR p x = updateStateR p z :=
      (updateStateR_eq_updateStateR_iff_inactive_getD_eq_of_inRestrictedStateSpace
        hxSpace hzSpace).mpr hInactive
    calc
      score x = score (updateStateR p x) :=
        (hPreserved x hxSpace).symm
      _ = score (updateStateR p z) := congrArg score hUpdates
      _ = score z := hPreserved z hzSpace
  · intro hInsensitive x hxSpace
    have hUpdatedSpace :
        inRestrictedStateSpace p (updateStateR p x) :=
      updateStateR_preserves_inRestrictedStateSpace hxSpace
    apply hInsensitive (updateStateR p x) x hUpdatedSpace hxSpace
    exact
      (updateStateR_eq_updateStateR_iff_inactive_getD_eq_of_inRestrictedStateSpace
        hUpdatedSpace hxSpace).mp
        (updateStateR_idempotent p x)

end RestrictedBridge
end VFH2
