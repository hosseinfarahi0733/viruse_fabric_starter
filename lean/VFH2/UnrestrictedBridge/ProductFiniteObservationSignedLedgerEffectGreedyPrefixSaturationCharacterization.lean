import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyIntervalRealization

/-!
# Product finite-observation greedy prefix-saturation characterization

This module replaces the state-dependent prefix recurrence of the semantic
canonical class by an exact static closed form. For every bounded Product
prefix, the accumulated state is the minimum of the ledger-effect-derived
quota and the corresponding accumulated active capacity.

The reverse implication is substantive: global active support together with
the static prefix equations reconstructs both the Product-window state-space
bounds and relational left-greediness. The finite algebraic core proves that
the coordinate recurrence is equivalent to simultaneous saturation of every
bounded prefix.

The preceding interval-realization module is imported to preserve the
historical proof spine; its public theorem is not used as a wrapper. All
finite-list machinery remains private, and all semantic predicates remain
theorem-local.

Only prefixes inside the canonical finite Product observation window are
characterized. This does not define a global infinite ledger, is not
unrestricted `TTP-VF-H2-004`, and makes no full-theory, empirical, physical,
medical, causal, or biological validation claim.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c91_prefixSum_succ
    (a : Nat → Nat)
    (k : Nat) :
    (List.ofFn
        (fun v : Fin (k + 1) =>
          a v.val)).sum =
      (List.ofFn
          (fun v : Fin k =>
            a v.val)).sum +
        a k := by
  rw [List.ofFn_succ_last, List.sum_append]
  simp

private theorem c91_takeSum_succ_of_lt
    (capacities : List Nat)
    (k : Nat)
    (hk : k < capacities.length) :
    (capacities.take (k + 1)).sum =
      (capacities.take k).sum +
        capacities.get ⟨k, hk⟩ := by
  rw [
    List.take_add_one,
    List.getElem?_eq_getElem hk,
    List.sum_append
  ]
  simp

private theorem c91_min_prefix_step
    (q capacityPrefix coordinateCapacity : Nat) :
    min q capacityPrefix +
        min coordinateCapacity
          (q - min q capacityPrefix) =
      min q (capacityPrefix + coordinateCapacity) := by
  omega

private theorem c91_recurrence_iff_prefixSaturation
    (a : Nat → Nat)
    (capacities : List Nat)
    (q n : Nat)
    (hLength : capacities.length = n) :
    (∀ (k : Nat) (hk : k < n),
      a k =
        min
          (capacities.get ⟨k, by omega⟩)
          (q -
            (List.ofFn
              (fun v : Fin k =>
                a v.val)).sum)) ↔
    (∀ k : Nat,
      k ≤ n →
        (List.ofFn
            (fun v : Fin k =>
              a v.val)).sum =
          min q (capacities.take k).sum) := by
  constructor
  · intro hRecurrence k
    induction k with
    | zero =>
        intro _
        simp
    | succ k ih =>
        intro hk
        have hkLt : k < n := by
          omega
        have hkLength : k < capacities.length := by
          omega
        rw [
          c91_prefixSum_succ,
          hRecurrence k hkLt,
          ih (by omega),
          c91_takeSum_succ_of_lt capacities k hkLength,
          c91_min_prefix_step
        ]
  · intro hSaturation k hk
    have hkLength : k < capacities.length := by
      omega
    have hkPrefix := hSaturation k (by omega)
    have hkSuccPrefix := hSaturation (k + 1) (by omega)
    rw [
      c91_prefixSum_succ,
      c91_takeSum_succ_of_lt capacities k hkLength
    ] at hkSuccPrefix
    rw [hkPrefix] at hkSuccPrefix
    have hStep :=
      c91_min_prefix_step
        q
        (capacities.take k).sum
        (capacities.get ⟨k, hkLength⟩)
    omega

/--
Semantic canonical left-greediness is equivalent to saturating every bounded
state prefix against its static active-capacity prefix, with the quota
recovered directly from the signed Product-window ledger effect.
-/
theorem canonicalLeftGreedyActiveSupport_iff_ledgerEffect_capacityPrefixSaturation
    (p : ProductRestrictedParams)
    (s : StateU) :
    let capacities : List Nat :=
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            p.n
          else
            0)
    let activeCapacity : Nat := capacities.sum
    let effect : Int :=
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        s
    let quota : Nat :=
      Int.toNat ((activeCapacity : Int) - effect)
    let statePrefix : Nat → Nat :=
      fun k =>
        (List.ofFn
          (fun v : Fin k =>
            s v.val)).sum
    let capacityPrefix : Nat → Nat :=
      fun k =>
        (capacities.take k).sum
    let HasGlobalActiveSupport : Prop :=
      (∀ j : Nat,
        j ∉ (paramsUOfProduct p).active →
          s j = 0)
    let IsRelationalLeftGreedy : Prop :=
      (∀ u v : Typed.WidthIndex p.d,
        u.val < v.val →
        ProductIndex.unflatten u ∈ p.active →
        ProductIndex.unflatten v ∈ p.active →
        s u.val < p.n →
          s v.val = 0)
    let HasLedgerEffectCapacityPrefixSaturation : Prop :=
      (∀ k : Nat,
        k ≤ Typed.typedWidth p.d →
          statePrefix k =
            min quota (capacityPrefix k))
    (HasGlobalActiveSupport ∧
      inStateSpaceU (paramsUOfProduct p) s ∧
      IsRelationalLeftGreedy) ↔
    (HasGlobalActiveSupport ∧
      HasLedgerEffectCapacityPrefixSaturation) := by
  dsimp only
  let capacities : List Nat :=
    List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          p.n
        else
          0)
  let activeSum : Nat :=
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          s w.val
        else
          0)).sum
  have hLength :
      capacities.length =
        Typed.typedWidth p.d := by
    simp [capacities]
  have hQuota :
      Int.toNat
          ((capacities.sum : Int) -
            ledgerEffectOn
              (paramsUOfProduct p)
              (productWindowU p)
              s) =
        activeSum := by
    dsimp [capacities, activeSum]
    rw [
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
    ]
    omega
  have hCanonical :=
    canonicalLeftGreedyActiveSupport_iff_activeSum_prefixRecurrence
      p
      s
  dsimp only at hCanonical
  constructor
  · intro hSemantic
    have hRecurrence := hCanonical.mp hSemantic
    refine ⟨hRecurrence.1, ?_⟩
    have hGenericRecurrence :
        ∀ (k : Nat) (hk : k < Typed.typedWidth p.d),
          s k =
            min
              (capacities.get ⟨k, by omega⟩)
              (activeSum -
                (List.ofFn
                  (fun v : Fin k =>
                    s v.val)).sum) := by
      intro k hk
      let w : Typed.WidthIndex p.d := ⟨k, hk⟩
      simpa [capacities, w] using hRecurrence.2 w
    have hSaturation :=
      (c91_recurrence_iff_prefixSaturation
        s
        capacities
        activeSum
        (Typed.typedWidth p.d)
        hLength).mp hGenericRecurrence
    intro k hk
    change
      (List.ofFn
          (fun v : Fin k =>
            s v.val)).sum =
        min
          (Int.toNat
            ((capacities.sum : Int) -
              ledgerEffectOn
                (paramsUOfProduct p)
                (productWindowU p)
                s))
          (capacities.take k).sum
    rw [hQuota]
    exact hSaturation k hk
  · intro hSaturation
    apply hCanonical.mpr
    refine ⟨hSaturation.1, ?_⟩
    have hGenericSaturation :
        ∀ k : Nat,
          k ≤ Typed.typedWidth p.d →
            (List.ofFn
                (fun v : Fin k =>
                  s v.val)).sum =
              min activeSum (capacities.take k).sum := by
      intro k hk
      have hkSaturation := hSaturation.2 k hk
      change
        (List.ofFn
            (fun v : Fin k =>
              s v.val)).sum =
          min
            (Int.toNat
              ((capacities.sum : Int) -
                ledgerEffectOn
                  (paramsUOfProduct p)
                  (productWindowU p)
                  s))
            (capacities.take k).sum at hkSaturation
      rw [hQuota] at hkSaturation
      exact hkSaturation
    have hGenericRecurrence :=
      (c91_recurrence_iff_prefixSaturation
        s
        capacities
        activeSum
        (Typed.typedWidth p.d)
        hLength).mpr hGenericSaturation
    intro w
    simpa [capacities] using
      hGenericRecurrence w.val w.isLt

end UnrestrictedBridge
end VFH2
