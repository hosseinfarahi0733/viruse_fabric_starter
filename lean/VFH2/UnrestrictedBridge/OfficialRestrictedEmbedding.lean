import VFH2.UnrestrictedBridge.Scaffold
import VFH2.RestrictedBridge.WellFormedParams
import VFH2.Product.ProductOfficialRestrictedBridgeOneStepStabilization

/-!
# Official Restricted to Countably Indexed Embedding

This module embeds the existing official list-backed restricted model into the
countably indexed, finite-observation scaffold.

The embedding extends a finite list state by zero outside its represented
coordinates.

Boundary:
- This only connects the existing restricted model to the new scaffold.
- It does not establish unrestricted `TTP-VF-H2-004`.
- It does not define a global infinite ledger.
- It introduces no empirical or biological claim.
-/

namespace VFH2
namespace UnrestrictedBridge

/-- Embed official restricted parameters into the countably indexed scaffold. -/
def paramsUOfRestricted
    (p : RestrictedBridge.RestrictedParams) :
    ParamsU :=
  {
    top := p.n
    active := p.active
  }

/-- Extend an official finite list state by zero outside its represented width. -/
def stateUOfRestricted
    (x : RestrictedBridge.State) :
    StateU :=
  fun i => x.getD i 0

/-- The canonical finite observation window of official restricted parameters. -/
def restrictedWindow
    (p : RestrictedBridge.RestrictedParams) :
    List Nat :=
  List.range (RestrictedBridge.expectedWidth p)

/-- Parameter embedding preserves the top value. -/
theorem paramsUOfRestricted_top
    (p : RestrictedBridge.RestrictedParams) :
    (paramsUOfRestricted p).top = p.n := by
  rfl

/-- Parameter embedding preserves the active list exactly. -/
theorem paramsUOfRestricted_active
    (p : RestrictedBridge.RestrictedParams) :
    (paramsUOfRestricted p).active = p.active := by
  rfl

/-- The observation window has the official expected width. -/
theorem restrictedWindow_length
    (p : RestrictedBridge.RestrictedParams) :
    (restrictedWindow p).length =
      RestrictedBridge.expectedWidth p := by
  simp [restrictedWindow]

/--
Coordinate lookup through the recursive official restricted update.

This helper is local to the new embedding layer and does not alter the
existing restricted declarations.
-/
private theorem restrictedUpdateStateAuxR_getElem?
    (p : RestrictedBridge.RestrictedParams)
    (x : RestrictedBridge.State)
    (base i : Nat) :
    (RestrictedBridge.updateStateAuxR p base x)[i]? =
      x[i]?.map
        (RestrictedBridge.updateCoordinateR p (base + i)) := by
  induction x generalizing base i with
  | nil =>
      simp [RestrictedBridge.updateStateAuxR]
  | cons a xs ih =>
      cases i with
      | zero =>
          simp [RestrictedBridge.updateStateAuxR]
      | succ i =>
          simpa [
            RestrictedBridge.updateStateAuxR,
            Nat.succ_eq_add_one,
            Nat.add_assoc,
            Nat.add_comm,
            Nat.add_left_comm
          ] using ih (base := base + 1) (i := i)

/-- Coordinate lookup through the official list-backed update. -/
theorem restrictedUpdateStateR_getElem?_eq_map
    (p : RestrictedBridge.RestrictedParams)
    (x : RestrictedBridge.State)
    (i : Nat) :
    (RestrictedBridge.updateStateR p x)[i]? =
      x[i]?.map (RestrictedBridge.updateCoordinateR p i) := by
  simpa [RestrictedBridge.updateStateR] using
    restrictedUpdateStateAuxR_getElem? p x 0 i

/--
For well-formed restricted parameters and an in-space finite state, embedding
commutes exactly with one update.
-/
theorem stateUOfRestricted_updateStateR
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (x : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params x) :
    stateUOfRestricted
        (RestrictedBridge.updateStateR wp.params x) =
      updateU
        (paramsUOfRestricted wp.params)
        (stateUOfRestricted x) := by
  funext i
  change
    (RestrictedBridge.updateStateR wp.params x).getD i 0 =
      if i ∈ wp.params.active then
        wp.params.n
      else
        x.getD i 0
  simp only [List.getD_eq_getElem?_getD]
  rw [restrictedUpdateStateR_getElem?_eq_map]
  by_cases hi : i ∈ wp.params.active
  · have hirange : i < x.length := by
      have hiwidth :
          i < RestrictedBridge.expectedWidth wp.params :=
        wp.activeWithinWidth i hi
      rw [hspace.1]
      exact hiwidth
    rw [List.getElem?_eq_getElem hirange]
    simp [
      RestrictedBridge.updateCoordinateR,
      RestrictedBridge.isActiveIndex,
      hi
    ]
  · rw [if_neg hi]
    cases hxi : x[i]? with
    | none =>
        simp
    | some a =>
        have hInactive :
            RestrictedBridge.isActiveIndex wp.params i = false := by
          simp [RestrictedBridge.isActiveIndex, hi]
        simp [
          RestrictedBridge.updateCoordinateR_inactive
            wp.params i a hInactive
        ]

/--
Official restricted fixed-set membership is definitionally identical to
fixed-set membership after embedding.
-/
theorem inFixedSetU_stateUOfRestricted_iff
    (p : RestrictedBridge.RestrictedParams)
    (x : RestrictedBridge.State) :
    inFixedSetU
        (paramsUOfRestricted p)
        (stateUOfRestricted x)
      ↔
    RestrictedBridge.inFixedSetR p x := by
  rfl

/--
An embedded official update is in the countably indexed fixed set whenever
the official parameters are well formed and the initial state is in space.
-/
theorem stateUOfRestricted_updateStateR_inFixedSetU
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (x : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params x) :
    inFixedSetU
      (paramsUOfRestricted wp.params)
      (stateUOfRestricted
        (RestrictedBridge.updateStateR wp.params x)) := by
  rw [stateUOfRestricted_updateStateR wp x hspace]
  exact
    updateU_inFixedSetU
      (paramsUOfRestricted wp.params)
      (stateUOfRestricted x)


/--
Enumerating the canonical restricted window and reading the zero-extended
state reconstructs the original finite list exactly.
-/
private theorem map_restrictedWindow_stateUOfRestricted_eq
    (p : RestrictedBridge.RestrictedParams)
    (x : RestrictedBridge.State)
    (hwidth : RestrictedBridge.hasExpectedWidth p x) :
    (restrictedWindow p).map (stateUOfRestricted x) = x := by
  have hlen :
      x.length = RestrictedBridge.expectedWidth p := by
    exact hwidth

  apply List.ext_getElem?
  intro i
  by_cases hi : i < x.length

  · have hiw :
        i < RestrictedBridge.expectedWidth p := by
      rw [← hlen]
      exact hi

    simp [
      restrictedWindow,
      stateUOfRestricted,
      hi,
      hiw
    ]

  · have hiw :
        ¬ i < RestrictedBridge.expectedWidth p := by
      intro h
      apply hi
      rw [hlen]
      exact h

    simp [
      restrictedWindow,
      hi,
      hiw
    ]

/--
The finite-observation ledger of an embedded restricted state is exactly the
existing official restricted ledger.
-/
theorem ledgerOn_restrictedWindow_stateUOfRestricted
    (p : RestrictedBridge.RestrictedParams)
    (x : RestrictedBridge.State)
    (hwidth : RestrictedBridge.hasExpectedWidth p x) :
    ledgerOn
        (restrictedWindow p)
        (stateUOfRestricted x) =
      RestrictedBridge.ledgerVR x := by
  unfold ledgerOn RestrictedBridge.ledgerVR
  rw [← List.foldl_map]
  rw [map_restrictedWindow_stateUOfRestricted_eq p x hwidth]


/--
The finite-observation ledger effect of an embedded official restricted state
is exactly the existing official restricted ledger effect.
-/
theorem ledgerEffectOn_restrictedWindow_stateUOfRestricted
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (x : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params x) :
    ledgerEffectOn
        (paramsUOfRestricted wp.params)
        (restrictedWindow wp.params)
        (stateUOfRestricted x) =
      RestrictedBridge.ledgerEffectR wp.params x := by
  have hspaceUpdate :
      RestrictedBridge.inRestrictedStateSpace
        wp.params
        (RestrictedBridge.updateStateR wp.params x) :=
    RestrictedBridge.updateStateR_preserves_inRestrictedStateSpace
      hspace

  unfold ledgerEffectOn RestrictedBridge.ledgerEffectR

  rw [
    ← stateUOfRestricted_updateStateR
        wp
        x
        hspace
  ]

  rw [
    ledgerOn_restrictedWindow_stateUOfRestricted
      wp.params
      (RestrictedBridge.updateStateR wp.params x)
      hspaceUpdate.1
  ]

  rw [
    ledgerOn_restrictedWindow_stateUOfRestricted
      wp.params
      x
      hspace.1
  ]

  rfl

end UnrestrictedBridge
end VFH2
