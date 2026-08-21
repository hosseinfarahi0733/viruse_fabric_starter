import Std

/-!
# VF-H2 Countably Indexed Finite-Observation Scaffold

This file introduces a conservative next-layer scaffold with countably indexed
states and finite observation windows.

Boundary:
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This does not define a global infinite ledger.
- This is not empirical validation.
- This is not biological validation.
- This does not modify or weaken the existing restricted finite model.
-/

namespace VFH2
namespace UnrestrictedBridge

/-- A countably indexed state. -/
abbrev StateU := Nat → Nat

/-- Parameters for the countably indexed scaffold.

`top` is the coordinate upper bound and `active` lists the coordinates updated
to that top value.
-/
structure ParamsU where
  top : Nat
  active : List Nat
  deriving Repr

/-- Every coordinate of the state is bounded by `p.top`. -/
def inStateSpaceU (p : ParamsU) (x : StateU) : Prop :=
  ∀ i, x i ≤ p.top

/-- Every active coordinate is already at `p.top`. -/
def inFixedSetU (p : ParamsU) (x : StateU) : Prop :=
  ∀ i ∈ p.active, x i = p.top

/-- Set every active coordinate to `p.top` and leave all other coordinates unchanged. -/
def updateU (p : ParamsU) (x : StateU) : StateU :=
  fun i => if i ∈ p.active then p.top else x i

/-- A finite-observation ledger over a list of coordinate indices.

Repeated indices in `window` are intentionally counted repeatedly. This keeps
`window` as an observation list rather than silently quotienting it to a set.
-/
def ledgerOn (window : List Nat) (x : StateU) : Nat :=
  window.foldl (fun acc i => acc + x i) 0

/-- Integer ledger difference induced by one update on a finite observation window. -/
def ledgerEffectOn
    (p : ParamsU)
    (window : List Nat)
    (x : StateU) : Int :=
  (ledgerOn window (updateU p x) : Int) -
    (ledgerOn window x : Int)

/-- An active coordinate is updated to `p.top`. -/
theorem updateU_apply_of_mem
    (p : ParamsU)
    (x : StateU)
    {i : Nat}
    (hi : i ∈ p.active) :
    updateU p x i = p.top := by
  simp [updateU, hi]

/-- An inactive coordinate is unchanged. -/
theorem updateU_apply_of_not_mem
    (p : ParamsU)
    (x : StateU)
    {i : Nat}
    (hi : i ∉ p.active) :
    updateU p x i = x i := by
  simp [updateU, hi]

/-- The update preserves the pointwise upper-bound invariant. -/
theorem updateU_preserves_inStateSpaceU
    (p : ParamsU)
    (x : StateU)
    (hx : inStateSpaceU p x) :
    inStateSpaceU p (updateU p x) := by
  intro i
  by_cases hi : i ∈ p.active
  · simp [updateU, hi]
  · simpa [updateU, hi] using hx i

/-- One update places the state in the active-coordinate fixed set. -/
theorem updateU_inFixedSetU
    (p : ParamsU)
    (x : StateU) :
    inFixedSetU p (updateU p x) := by
  intro i hi
  simp [updateU, hi]

/-- The countably indexed update is idempotent. -/
theorem updateU_idempotent
    (p : ParamsU)
    (x : StateU) :
    updateU p (updateU p x) = updateU p x := by
  funext i
  by_cases hi : i ∈ p.active
  · simp [updateU, hi]
  · simp [updateU, hi]

/-- Definitional expansion of the finite-observation ledger effect. -/
theorem ledgerEffectOn_def
    (p : ParamsU)
    (window : List Nat)
    (x : StateU) :
    ledgerEffectOn p window x =
      (ledgerOn window (updateU p x) : Int) -
        (ledgerOn window x : Int) := by
  rfl

end UnrestrictedBridge
end VFH2
