import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedySuccessorCharacterization

/-!
# Complete finite greedy successor-chain realization

This module packages every semantically canonical left-greedy active-support state
of a finite Product observation into one unique complete chain, indexed by its
exact signed ledger effect.  Every adjacent edge is certified by the C93
successor characterization together with its unique active-capacity-crossing
unit coordinate, and the chain exhaustively and uniquely ranks all such states.

The chain is only a theorem-local witness selected with `Classical.choose`.
This does not define an executable normalizer, a global successor operation, an
update trajectory, or an infinite ledger construction.  It remains inside the
finite restricted Product observation model; it is not unrestricted
TTP-VF-H2-004 and is not full-theory, empirical, or biological validation.
-/


namespace VFH2
namespace UnrestrictedBridge

private theorem c94_existsUnique_canonicalLeftGreedyActiveSupport_of_effect
    (p : ProductRestrictedParams)
    (e : Int)
    (heRange :
      0 ≤ e ∧
      e ≤
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then p.n else 0)).sum : Int)) :
    ∃ y : StateU,
      (((∀ j : Nat,
          j ∉ (paramsUOfProduct p).active → y j = 0) ∧
        inStateSpaceU (paramsUOfProduct p) y ∧
        ∀ u v : Typed.WidthIndex p.d,
          u.val < v.val →
          ProductIndex.unflatten u ∈ p.active →
          ProductIndex.unflatten v ∈ p.active →
          y u.val < p.n → y v.val = 0) ∧
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          y = e) ∧
      ∀ y' : StateU,
        (((∀ j : Nat,
            j ∉ (paramsUOfProduct p).active → y' j = 0) ∧
          inStateSpaceU (paramsUOfProduct p) y' ∧
          ∀ u v : Typed.WidthIndex p.d,
            u.val < v.val →
            ProductIndex.unflatten u ∈ p.active →
            ProductIndex.unflatten v ∈ p.active →
            y' u.val < p.n → y' v.val = 0) ∧
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            y' = e) →
        y' = y := by
  obtain ⟨u, huEffect⟩ :=
    (exists_productLedgerEffect_eq_iff_nonneg_and_le_activeCapacity
      p
      e).mpr heRange
  let s : StateU := stateUOfProduct p u
  have hsSpace :
      inStateSpaceU
        (paramsUOfProduct p)
        s := by
    simpa [s] using stateUOfProduct_inStateSpaceU p u
  have hsEffect :
      ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          s =
        e := by
    calc
      ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          s =
        productLedgerEffect p u := by
          simpa [s] using
            ledgerEffectOn_productWindowU_stateUOfProduct p u
      _ = e := huEffect
  have hCanonicalFiber :=
    existsUnique_canonicalLeftGreedyActiveSupport_in_productWindowUFiber_and_levelSet
      p
      s
      hsSpace
  dsimp only at hCanonicalFiber
  rcases hCanonicalFiber with
    ⟨y, ⟨⟨⟨hyCanonical, hyFiber⟩, hyUnique⟩, _⟩⟩
  refine ⟨y, ⟨hyCanonical, hyFiber.trans hsEffect⟩, ?_⟩
  intro y' hy'
  apply hyUnique
  exact ⟨hy'.1, hy'.2.trans hsEffect.symm⟩

theorem existsUnique_completeCanonicalLeftGreedySuccessorChain_with_unique_activeCapacityCrossingUnitCoordinates
    (p : ProductRestrictedParams) :
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
          s u.val < p.n →
          s v.val = 0
    let IsActiveCapacityCrossingUnitCoordinate :
        StateU → StateU → Typed.WidthIndex p.d → Prop :=
      fun x z w =>
        ProductIndex.unflatten w ∈ p.active ∧
        capacityPrefix w.val < quota x ∧
        quota x ≤ capacityPrefix (w.val + 1) ∧
        x w.val = z w.val + 1 ∧
        ∀ j : Nat,
          j ≠ w.val → x j = z j
    let HasUniqueActiveCapacityCrossingUnitCoordinate :
        StateU → StateU → Prop :=
      fun x z =>
        ∃ w : Typed.WidthIndex p.d,
          IsActiveCapacityCrossingUnitCoordinate x z w ∧
          ∀ w' : Typed.WidthIndex p.d,
            IsActiveCapacityCrossingUnitCoordinate x z w' →
              w' = w
    let IsCompleteCanonicalSuccessorChain :
        (Fin (activeCapacity + 1) → StateU) → Prop :=
      fun chain =>
        (∀ e : Fin (activeCapacity + 1),
          IsCanonicalLeftGreedy (chain e) ∧
          effect (chain e) = (e.val : Int)) ∧
        (∀ e : Fin activeCapacity,
          ((IsCanonicalLeftGreedy (chain e.succ) ∧
              HasUniqueActiveCapacityCrossingUnitCoordinate
                (chain e.castSucc)
                (chain e.succ)) ∧
            ∀ z : StateU,
              (IsCanonicalLeftGreedy z ∧
                HasUniqueActiveCapacityCrossingUnitCoordinate
                  (chain e.castSucc)
                  z) →
                z = chain e.succ)) ∧
        ∀ s : StateU,
          IsCanonicalLeftGreedy s →
            ∃ e : Fin (activeCapacity + 1),
              chain e = s ∧
              ∀ e' : Fin (activeCapacity + 1),
                chain e' = s → e' = e
    ∃ chain : Fin (activeCapacity + 1) → StateU,
      IsCompleteCanonicalSuccessorChain chain ∧
      ∀ chain' : Fin (activeCapacity + 1) → StateU,
        IsCompleteCanonicalSuccessorChain chain' →
          chain' = chain := by
  classical
  dsimp only
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
        s u.val < p.n →
        s v.val = 0
  let IsActiveCapacityCrossingUnitCoordinate :
      StateU → StateU → Typed.WidthIndex p.d → Prop :=
    fun x z w =>
      ProductIndex.unflatten w ∈ p.active ∧
      capacityPrefix w.val < quota x ∧
      quota x ≤ capacityPrefix (w.val + 1) ∧
      x w.val = z w.val + 1 ∧
      ∀ j : Nat,
        j ≠ w.val → x j = z j
  let HasUniqueActiveCapacityCrossingUnitCoordinate :
      StateU → StateU → Prop :=
    fun x z =>
      ∃ w : Typed.WidthIndex p.d,
        IsActiveCapacityCrossingUnitCoordinate x z w ∧
        ∀ w' : Typed.WidthIndex p.d,
          IsActiveCapacityCrossingUnitCoordinate x z w' →
            w' = w
  let IsCompleteCanonicalSuccessorChain :
      (Fin (activeCapacity + 1) → StateU) → Prop :=
    fun chain =>
      (∀ e : Fin (activeCapacity + 1),
        IsCanonicalLeftGreedy (chain e) ∧
        effect (chain e) = (e.val : Int)) ∧
      (∀ e : Fin activeCapacity,
        ((IsCanonicalLeftGreedy (chain e.succ) ∧
            HasUniqueActiveCapacityCrossingUnitCoordinate
              (chain e.castSucc)
              (chain e.succ)) ∧
          ∀ z : StateU,
            (IsCanonicalLeftGreedy z ∧
              HasUniqueActiveCapacityCrossingUnitCoordinate
                (chain e.castSucc)
                z) →
              z = chain e.succ)) ∧
      ∀ s : StateU,
        IsCanonicalLeftGreedy s →
          ∃ e : Fin (activeCapacity + 1),
            chain e = s ∧
            ∀ e' : Fin (activeCapacity + 1),
              chain e' = s → e' = e
  change
    ∃ chain : Fin (activeCapacity + 1) → StateU,
      IsCompleteCanonicalSuccessorChain chain ∧
      ∀ chain' : Fin (activeCapacity + 1) → StateU,
        IsCompleteCanonicalSuccessorChain chain' →
          chain' = chain
  have hAtRank :
      ∀ e : Fin (activeCapacity + 1),
        ∃ y : StateU,
          ((IsCanonicalLeftGreedy y ∧
            effect y = (e.val : Int)) ∧
          ∀ y' : StateU,
            (IsCanonicalLeftGreedy y' ∧
              effect y' = (e.val : Int)) →
            y' = y) := by
    intro e
    apply
      c94_existsUnique_canonicalLeftGreedyActiveSupport_of_effect
        p
        (e.val : Int)
    constructor
    · exact Int.natCast_nonneg e.val
    · change (e.val : Int) ≤ (activeCapacity : Int)
      exact_mod_cast (show e.val ≤ activeCapacity by omega)
  let chain : Fin (activeCapacity + 1) → StateU :=
    fun e => Classical.choose (hAtRank e)
  have hChainSpec :
      ∀ e : Fin (activeCapacity + 1),
        ((IsCanonicalLeftGreedy (chain e) ∧
          effect (chain e) = (e.val : Int)) ∧
        ∀ y' : StateU,
          (IsCanonicalLeftGreedy y' ∧
            effect y' = (e.val : Int)) →
          y' = chain e) := by
    intro e
    exact Classical.choose_spec (hAtRank e)
  have hProfile :
      ∀ e : Fin (activeCapacity + 1),
        IsCanonicalLeftGreedy (chain e) ∧
        effect (chain e) = (e.val : Int) := by
    intro e
    exact (hChainSpec e).1
  have hEdges :
      ∀ e : Fin activeCapacity,
        ((IsCanonicalLeftGreedy (chain e.succ) ∧
            HasUniqueActiveCapacityCrossingUnitCoordinate
              (chain e.castSucc)
              (chain e.succ)) ∧
          ∀ z : StateU,
            (IsCanonicalLeftGreedy z ∧
              HasUniqueActiveCapacityCrossingUnitCoordinate
                (chain e.castSucc)
                z) →
              z = chain e.succ) := by
    intro e
    have hxProfile := hProfile e.castSucc
    have hxBelowTop :
        effect (chain e.castSucc) < (activeCapacity : Int) := by
      rw [hxProfile.2]
      exact_mod_cast e.isLt
    have hSuccessorRaw :=
      (existsUnique_canonicalLeftGreedySuccessor_with_unique_activeCapacityCrossingUnitCoordinate_iff_effect_lt_activeCapacity
        p
        (chain e.castSucc)
        hxProfile.1).mpr
        (by
          simpa [activeCapacity, capacities, effect] using hxBelowTop)
    have hSuccessor :
        ∃ z : StateU,
          ((IsCanonicalLeftGreedy z ∧
            HasUniqueActiveCapacityCrossingUnitCoordinate
              (chain e.castSucc)
              z) ∧
          ∀ z' : StateU,
            (IsCanonicalLeftGreedy z' ∧
              HasUniqueActiveCapacityCrossingUnitCoordinate
                (chain e.castSucc)
                z') →
            z' = z) := by
      simpa [
        IsCanonicalLeftGreedy,
        HasUniqueActiveCapacityCrossingUnitCoordinate,
        IsActiveCapacityCrossingUnitCoordinate,
        capacityPrefix,
        quota,
        activeCapacity,
        capacities,
        effect
      ] using hSuccessorRaw
    rcases hSuccessor with
      ⟨z, ⟨⟨hzCanonical, hzCrossing⟩, hzUnique⟩⟩
    have hzAdjacentRaw :=
      (ledgerEffectOn_productWindowU_eq_add_one_iff_existsUnique_activeCapacityCrossingUnitCoordinate_of_canonicalLeftGreedy
        p
        (chain e.castSucc)
        z
        hxProfile.1
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
    have hzAdjacent :
        effect z = effect (chain e.castSucc) + 1 := by
      change effect z = effect (chain e.castSucc) + 1 at hzAdjacentRaw
      exact hzAdjacentRaw
    have hzRank :
        effect z = (e.succ.val : Int) := by
      rw [hzAdjacent, hxProfile.2]
      rfl
    have hzEq : z = chain e.succ :=
      (hChainSpec e.succ).2 z ⟨hzCanonical, hzRank⟩
    subst z
    exact ⟨⟨hzCanonical, hzCrossing⟩, hzUnique⟩
  have hExhaustive :
      ∀ s : StateU,
        IsCanonicalLeftGreedy s →
          ∃ e : Fin (activeCapacity + 1),
            chain e = s ∧
            ∀ e' : Fin (activeCapacity + 1),
              chain e' = s → e' = e := by
    intro s hsCanonical
    have hsNonnegative : 0 ≤ effect s := by
      dsimp [effect]
      exact
        ledgerEffectOn_nonneg
          (paramsUOfProduct p)
          (productWindowU p)
          s
          hsCanonical.2.1
    have hsFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        s
    have hsUpper : effect s ≤ (activeCapacity : Int) := by
      dsimp [effect, activeCapacity, capacities]
      rw [hsFormula]
      omega
    have hRankCast :
        (Int.toNat (effect s) : Int) = effect s :=
      Int.toNat_of_nonneg hsNonnegative
    let e : Fin (activeCapacity + 1) :=
      ⟨Int.toNat (effect s), by omega⟩
    have hsRank : effect s = (e.val : Int) := by
      dsimp [e]
      omega
    have hsEq : s = chain e :=
      (hChainSpec e).2 s ⟨hsCanonical, hsRank⟩
    refine ⟨e, hsEq.symm, ?_⟩
    intro e' he'
    have he'Profile := (hProfile e').2
    rw [he'] at he'Profile
    apply Fin.ext
    dsimp [e]
    omega
  refine
    ⟨chain,
      ⟨hProfile, hEdges, hExhaustive⟩,
      ?_⟩
  intro chain' hChain'
  funext e
  exact
    (hChainSpec e).2
      (chain' e)
      (hChain'.1 e)

end UnrestrictedBridge
end VFH2
