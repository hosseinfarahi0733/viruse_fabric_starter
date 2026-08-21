import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyAdjacentCoverCharacterization

/-!
# Product finite-observation greedy successor characterization

This module identifies the exact terminal boundary for semantic canonical
left-greedy Product-window states. A canonical state has a unique canonical
successor with a unique active capacity-crossing unit coordinate exactly when
its signed Product-window ledger effect is strictly below the canonical active
capacity.

Existence is substantive: the next effect level is realized in the typed
Product model, embedded into the countably indexed state space, and replaced
by the globally unique canonical representative of its effect fiber. The
preceding adjacent-cover theorem then supplies the unique crossing coordinate.
Conversely, any claimed successor raises the effect by one, while the signed
formula bounds that successor by active capacity.

Both uniqueness claims are written explicitly in the repository's existing
style because no `ExistsUnique` notation import is added. All canonical,
effect, quota, capacity-prefix, successor, and crossing predicates remain
theorem-local. No public definition, alias, order structure, compatibility API,
or model assumption is introduced.

Only the canonical finite Product observation window is involved. This does
not define a global successor relation or infinite ledger, is not unrestricted
`TTP-VF-H2-004`, and makes no full-theory, empirical, physical, medical,
causal, or biological validation claim.
-/

namespace VFH2
namespace UnrestrictedBridge

theorem existsUnique_canonicalLeftGreedySuccessor_with_unique_activeCapacityCrossingUnitCoordinate_iff_effect_lt_activeCapacity
    (p : ProductRestrictedParams)
    (x : StateU) :
    let capacities : List Nat :=
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then p.n else 0)
    let activeCapacity : Nat := capacities.sum
    let effect : StateU → Int :=
      fun s =>
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          s
    let quota : StateU → Nat :=
      fun s =>
        Int.toNat ((activeCapacity : Int) - effect s)
    let capacityPrefix : Nat → Nat :=
      fun k => (capacities.take k).sum
    let IsCanonicalLeftGreedy : StateU → Prop :=
      fun s =>
        (∀ j : Nat,
          j ∉ (paramsUOfProduct p).active → s j = 0) ∧
        inStateSpaceU (paramsUOfProduct p) s ∧
        ∀ u v : Typed.WidthIndex p.d,
          u.val < v.val →
          ProductIndex.unflatten u ∈ p.active →
          ProductIndex.unflatten v ∈ p.active →
          s u.val < p.n → s v.val = 0
    let IsActiveCapacityCrossingUnitCoordinate :
        StateU → Typed.WidthIndex p.d → Prop :=
      fun z w =>
        ProductIndex.unflatten w ∈ p.active ∧
        capacityPrefix w.val < quota x ∧
        quota x ≤ capacityPrefix (w.val + 1) ∧
        x w.val = z w.val + 1 ∧
        ∀ j : Nat,
          j ≠ w.val → x j = z j
    let HasUniqueActiveCapacityCrossingUnitCoordinate : StateU → Prop :=
      fun z =>
        ∃ w : Typed.WidthIndex p.d,
          IsActiveCapacityCrossingUnitCoordinate z w ∧
          ∀ w' : Typed.WidthIndex p.d,
            IsActiveCapacityCrossingUnitCoordinate z w' → w' = w
    IsCanonicalLeftGreedy x →
      ((∃ z : StateU,
          ((IsCanonicalLeftGreedy z ∧
            HasUniqueActiveCapacityCrossingUnitCoordinate z) ∧
          ∀ z' : StateU,
            (IsCanonicalLeftGreedy z' ∧
              HasUniqueActiveCapacityCrossingUnitCoordinate z') →
            z' = z)) ↔
        effect x < (activeCapacity : Int)) := by
  dsimp only
  intro hxCanonical
  let capacities : List Nat :=
    List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then p.n else 0)
  let activeCapacity : Nat := capacities.sum
  let effect : StateU → Int :=
    fun s =>
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        s
  let quota : StateU → Nat :=
    fun s =>
      Int.toNat ((activeCapacity : Int) - effect s)
  let capacityPrefix : Nat → Nat :=
    fun k => (capacities.take k).sum
  let IsActiveCapacityCrossingUnitCoordinate :
      StateU → Typed.WidthIndex p.d → Prop :=
    fun z w =>
      ProductIndex.unflatten w ∈ p.active ∧
      capacityPrefix w.val < quota x ∧
      quota x ≤ capacityPrefix (w.val + 1) ∧
      x w.val = z w.val + 1 ∧
      ∀ j : Nat,
        j ≠ w.val → x j = z j
  let HasUniqueActiveCapacityCrossingUnitCoordinate : StateU → Prop :=
    fun z =>
      ∃ w : Typed.WidthIndex p.d,
        IsActiveCapacityCrossingUnitCoordinate z w ∧
        ∀ w' : Typed.WidthIndex p.d,
          IsActiveCapacityCrossingUnitCoordinate z w' → w' = w
  change
    (∃ z : StateU,
      ((((∀ j : Nat,
            j ∉ (paramsUOfProduct p).active → z j = 0) ∧
          inStateSpaceU (paramsUOfProduct p) z ∧
          ∀ u v : Typed.WidthIndex p.d,
            u.val < v.val →
            ProductIndex.unflatten u ∈ p.active →
            ProductIndex.unflatten v ∈ p.active →
            z u.val < p.n → z v.val = 0) ∧
        HasUniqueActiveCapacityCrossingUnitCoordinate z) ∧
      ∀ z' : StateU,
        (((∀ j : Nat,
              j ∉ (paramsUOfProduct p).active → z' j = 0) ∧
            inStateSpaceU (paramsUOfProduct p) z' ∧
            ∀ u v : Typed.WidthIndex p.d,
              u.val < v.val →
              ProductIndex.unflatten u ∈ p.active →
              ProductIndex.unflatten v ∈ p.active →
              z' u.val < p.n → z' v.val = 0) ∧
          HasUniqueActiveCapacityCrossingUnitCoordinate z') →
        z' = z)) ↔
      effect x < (activeCapacity : Int)
  constructor
  · rintro ⟨z, ⟨⟨hzCanonical, hzCrossing⟩, _⟩⟩
    have hAdjacent :=
      (ledgerEffectOn_productWindowU_eq_add_one_iff_existsUnique_activeCapacityCrossingUnitCoordinate_of_canonicalLeftGreedy
        p
        x
        z
        hxCanonical
        hzCanonical).mpr
        (by
          simpa [
            HasUniqueActiveCapacityCrossingUnitCoordinate,
            IsActiveCapacityCrossingUnitCoordinate,
            capacityPrefix,
            quota,
            activeCapacity,
            capacities,
            effect
          ] using hzCrossing)
    change effect z = effect x + 1 at hAdjacent
    have hzFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        z
    have hzUpper : effect z ≤ (activeCapacity : Int) := by
      dsimp [effect, activeCapacity, capacities]
      rw [hzFormula]
      omega
    omega
  · intro hxBelowTop
    have hxNonnegative : 0 ≤ effect x := by
      dsimp [effect]
      exact
        ledgerEffectOn_nonneg
          (paramsUOfProduct p)
          (productWindowU p)
          x
          hxCanonical.2.1
    have hSuccessorRange :
        0 ≤ effect x + 1 ∧
          effect x + 1 ≤ (activeCapacity : Int) := by
      omega
    obtain ⟨u, huEffect⟩ :=
      (exists_productLedgerEffect_eq_iff_nonneg_and_le_activeCapacity
        p
        (effect x + 1)).mpr
        (by
          simpa [activeCapacity, capacities] using hSuccessorRange)
    let s : StateU := stateUOfProduct p u
    have hsSpace :
        inStateSpaceU
          (paramsUOfProduct p)
          s := by
      simpa [s] using stateUOfProduct_inStateSpaceU p u
    have hsEffect : effect s = effect x + 1 := by
      calc
        effect s = productLedgerEffect p u := by
          simpa [effect, s] using
            ledgerEffectOn_productWindowU_stateUOfProduct p u
        _ = effect x + 1 := huEffect
    have hCanonicalFiber :=
      existsUnique_canonicalLeftGreedyActiveSupport_in_productWindowUFiber_and_levelSet
        p
        s
        hsSpace
    dsimp only at hCanonicalFiber
    rcases hCanonicalFiber with
      ⟨y, ⟨⟨⟨hyCanonical, hyFiber⟩, hyUnique⟩, _⟩⟩
    have hyEffect : effect y = effect x + 1 := by
      exact hyFiber.trans hsEffect
    have hyCrossing :
        HasUniqueActiveCapacityCrossingUnitCoordinate y := by
      have hCrossing :=
        (ledgerEffectOn_productWindowU_eq_add_one_iff_existsUnique_activeCapacityCrossingUnitCoordinate_of_canonicalLeftGreedy
          p
          x
          y
          hxCanonical
          hyCanonical).mp
          hyEffect
      simpa [
        HasUniqueActiveCapacityCrossingUnitCoordinate,
        IsActiveCapacityCrossingUnitCoordinate,
        capacityPrefix,
        quota,
        activeCapacity,
        capacities,
        effect
      ] using hCrossing
    refine ⟨y, ⟨⟨hyCanonical, hyCrossing⟩, ?_⟩⟩
    intro y' hy'
    apply hyUnique
    refine ⟨hy'.1, ?_⟩
    have hy'Effect : effect y' = effect x + 1 :=
      (ledgerEffectOn_productWindowU_eq_add_one_iff_existsUnique_activeCapacityCrossingUnitCoordinate_of_canonicalLeftGreedy
        p
        x
        y'
        hxCanonical
        hy'.1).mpr
        (by
          simpa [
            HasUniqueActiveCapacityCrossingUnitCoordinate,
            IsActiveCapacityCrossingUnitCoordinate,
            capacityPrefix,
            quota,
            activeCapacity,
            capacities,
            effect
          ] using hy'.2)
    exact hy'Effect.trans hsEffect.symm

end UnrestrictedBridge
end VFH2
