import VFH2.UnrestrictedBridge.ProductFiniteActiveGlobalLedgerEffectConservativity

/-!
# Product Finite-Active Global Ledger-Effect Trajectory Conservativity

This module strengthens the C101 numerical conservativity theorem from the
canonical embedded Product state at one instant to the complete discrete
trajectory. The initial countably indexed state may have an arbitrary inactive
tail; only pointwise agreement with the embedded Product state on the finite
active support is required.

The proof first records that the finite-active global effect is extensional on
active coordinates. It then transports the initial active-coordinate agreement
through the countable and Product trajectories and finishes by applying C101 to
the Product state at the requested time.

Boundary:
- The ambient `StateU` is countably indexed, but the ledger still sums only the
  deduplicated finite active support.
- The inactive tail is unrestricted and is neither reconstructed nor compared.
- No genuinely infinite active support or infinite ledger series is defined.
- This is not unrestricted `TTP-VF-H2-004` and makes no full-theory,
  empirical, physical, or biological claim.
- No proof-spine wrapper, public corollary, compatibility namespace, score, or
  additional assumption is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c102_map_eq_map_of_forall_mem
    {α β : Type}
    (support : List α)
    (f g : α → β)
    (h : ∀ a : α, a ∈ support → f a = g a) :
    support.map f = support.map g := by
  induction support with
  | nil =>
      rfl
  | cons a support ih =>
      have ha : f a = g a := h a (by simp)
      have htail : ∀ b : α, b ∈ support → f b = g b := by
        intro b hb
        exact h b (by simp [hb])
      simp only [List.map_cons, ha]
      rw [ih htail]

private theorem c102_finiteActiveGlobalLedgerEffectU_congr_on_active
    (q : ParamsU)
    (x z : StateU)
    (hActive : ∀ i : Nat, i ∈ q.active → x i = z i) :
    finiteActiveGlobalLedgerEffectU q x =
      finiteActiveGlobalLedgerEffectU q z := by
  have hUpdated :
      (q.active.eraseDups.map fun i => updateU q x i) =
        (q.active.eraseDups.map fun i => updateU q z i) := by
    apply c102_map_eq_map_of_forall_mem
    intro i hi
    have hiActive : i ∈ q.active :=
      List.mem_eraseDups.mp hi
    rw [
      updateU_apply_of_mem q x hiActive,
      updateU_apply_of_mem q z hiActive
    ]

  have hState :
      (q.active.eraseDups.map fun i => x i) =
        (q.active.eraseDups.map fun i => z i) := by
    apply c102_map_eq_map_of_forall_mem
    intro i hi
    exact hActive i (List.mem_eraseDups.mp hi)

  unfold finiteActiveGlobalLedgerEffectU
  rw [hUpdated, hState]

private theorem c102_stateUOfProduct_productUpdateTrajectory
    (p : ProductRestrictedParams)
    (y : p.State)
    (t : Nat) :
    stateUOfProduct p (productUpdateTrajectory p y t) =
      updateUTrajectory
        (paramsUOfProduct p)
        (stateUOfProduct p y)
        t := by
  induction t with
  | zero =>
      rfl
  | succ t ih =>
      rw [productUpdateTrajectory_succ]
      rw [stateUOfProduct_productUpdateState]
      simp only [updateUTrajectory]
      rw [ih]

private theorem c102_updateUTrajectory_eq_on_active_of_eq_on_active
    (q : ParamsU)
    (x z : StateU)
    (hActive : ∀ i : Nat, i ∈ q.active → x i = z i) :
    ∀ t i : Nat,
      i ∈ q.active →
        updateUTrajectory q x t i =
          updateUTrajectory q z t i := by
  intro t
  cases t with
  | zero =>
      exact hActive
  | succ t =>
      intro i hi
      simp [updateUTrajectory, updateU, hi]

/--
If a countably indexed initial state agrees with an embedded Product state on
every active coordinate, then their complete finite-active global ledger
effects agree at every trajectory time. The inactive countable tail is
arbitrary and contributes neither to the hypothesis nor to the ledger sum.
-/
theorem finiteActiveGlobalLedgerEffectU_updateUTrajectory_eq_productLedgerEffect_productUpdateTrajectory_of_eq_on_active
    (p : ProductRestrictedParams)
    (x : StateU)
    (y : p.State)
    (hActive : ∀ i : Nat,
      i ∈ (paramsUOfProduct p).active →
        x i = stateUOfProduct p y i)
    (t : Nat) :
    finiteActiveGlobalLedgerEffectU
        (paramsUOfProduct p)
        (updateUTrajectory (paramsUOfProduct p) x t) =
      productLedgerEffect p (productUpdateTrajectory p y t) := by
  have hTrajectory :
      ∀ i : Nat,
        i ∈ (paramsUOfProduct p).active →
          updateUTrajectory (paramsUOfProduct p) x t i =
            stateUOfProduct p (productUpdateTrajectory p y t) i := by
    intro i hi
    calc
      updateUTrajectory (paramsUOfProduct p) x t i =
          updateUTrajectory
            (paramsUOfProduct p)
            (stateUOfProduct p y)
            t
            i :=
        c102_updateUTrajectory_eq_on_active_of_eq_on_active
          (paramsUOfProduct p)
          x
          (stateUOfProduct p y)
          hActive
          t
          i
          hi
      _ = stateUOfProduct p (productUpdateTrajectory p y t) i :=
        (congrFun
          (c102_stateUOfProduct_productUpdateTrajectory p y t)
          i).symm

  calc
    finiteActiveGlobalLedgerEffectU
          (paramsUOfProduct p)
          (updateUTrajectory (paramsUOfProduct p) x t) =
        finiteActiveGlobalLedgerEffectU
          (paramsUOfProduct p)
          (stateUOfProduct p (productUpdateTrajectory p y t)) :=
      c102_finiteActiveGlobalLedgerEffectU_congr_on_active
        (paramsUOfProduct p)
        (updateUTrajectory (paramsUOfProduct p) x t)
        (stateUOfProduct p (productUpdateTrajectory p y t))
        hTrajectory
    _ = productLedgerEffect p (productUpdateTrajectory p y t) :=
      finiteActiveGlobalLedgerEffectU_paramsUOfProduct_stateUOfProduct
        p
        (productUpdateTrajectory p y t)

end UnrestrictedBridge
end VFH2
