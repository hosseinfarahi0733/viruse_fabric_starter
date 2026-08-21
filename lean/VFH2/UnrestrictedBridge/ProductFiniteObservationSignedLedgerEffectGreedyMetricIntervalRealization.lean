import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyMetricCharacterization

/-!
# Canonical active-coordinate L1 geodesic interval realization

This module proves that between any two semantic canonical left-greedy states
of one finite Product observation, every natural radius up to their intrinsic
active-coordinate L1 distance selects a unique canonical state on an additive
L1 geodesic between the endpoints.

The proof uses the signed-effect interval realization to construct and uniquely
identify the intermediate state, and the canonical metric characterization to
transport all three pairwise distances.  Both endpoint orientations are handled
directly; this is not a wrapper around the complete successor chain.

The distance and canonical predicates remain theorem-local and the sole
arithmetic helper is private.  No public metric or isometry structure,
normalizer, global order or successor API, update trajectory, ledger mutation,
or infinite ledger is introduced.  This remains a finite restricted Product
observation result, not unrestricted TTP-VF-H2-004 and not full-theory,
empirical, physical, medical, causal, or biological validation.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c97_natDistance_additive_iff_between
    (a b c : Nat) :
    (a - b) + (b - a) =
        ((a - c) + (c - a)) + ((c - b) + (b - c)) ↔
      (a ≤ c ∧ c ≤ b) ∨ (b ≤ c ∧ c ≤ a) := by
  omega

theorem existsUnique_canonicalLeftGreedyActiveSupport_on_activeCoordinateL1Geodesic_iff_le_endpointDistance
    (p : ProductRestrictedParams)
    (x z : StateU) :
    let natDistance : Nat → Nat → Nat :=
      fun a b => (a - b) + (b - a)
    let activeCoordinateL1Distance : StateU → StateU → Nat :=
      fun s t =>
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              natDistance (s w.val) (t w.val)
            else
              0)).sum
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
    IsCanonicalLeftGreedy x →
    IsCanonicalLeftGreedy z →
    ∀ r : Nat,
      ((∃ y : StateU,
          ((IsCanonicalLeftGreedy y ∧
            activeCoordinateL1Distance x y = r ∧
            activeCoordinateL1Distance x z =
              activeCoordinateL1Distance x y +
                activeCoordinateL1Distance y z) ∧
          ∀ y' : StateU,
            (IsCanonicalLeftGreedy y' ∧
              activeCoordinateL1Distance x y' = r ∧
              activeCoordinateL1Distance x z =
                activeCoordinateL1Distance x y' +
                  activeCoordinateL1Distance y' z) →
              y' = y)) ↔
        r ≤ activeCoordinateL1Distance x z) := by
  dsimp only
  intro hxCanonical hzCanonical r
  let effect : StateU → Int :=
    fun s =>
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        s
  let effectRank : StateU → Nat :=
    fun s => Int.toNat (effect s)
  let natDistance : Nat → Nat → Nat :=
    fun a b => (a - b) + (b - a)
  let activeCoordinateL1Distance : StateU → StateU → Nat :=
    fun s t =>
      (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            natDistance (s w.val) (t w.val)
          else
            0)).sum
  have hxNonneg : 0 ≤ effect x := by
    exact
      ledgerEffectOn_nonneg
        (paramsUOfProduct p)
        (productWindowU p)
        x
        hxCanonical.2.1
  have hzNonneg : 0 ≤ effect z := by
    exact
      ledgerEffectOn_nonneg
        (paramsUOfProduct p)
        (productWindowU p)
        z
        hzCanonical.2.1
  have hxRankCast : (effectRank x : Int) = effect x := by
    dsimp [effectRank]
    exact Int.toNat_of_nonneg hxNonneg
  have hzRankCast : (effectRank z : Int) = effect z := by
    dsimp [effectRank]
    exact Int.toNat_of_nonneg hzNonneg
  have hxzMetric :
      activeCoordinateL1Distance x z =
        natDistance (effectRank x) (effectRank z) := by
    simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
      activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
        p
        x
        z
        hxCanonical
        hzCanonical
  constructor
  · rintro ⟨y, ⟨⟨_, hyr, hgeodesic⟩, _⟩⟩
    omega
  · intro hr
    have hrRankDistance :
        r ≤ natDistance (effectRank x) (effectRank z) := by
      rw [← hxzMetric]
      exact hr
    dsimp [natDistance] at hrRankDistance
    by_cases hxzEffect : effect x ≤ effect z
    · have hxzRank : effectRank x ≤ effectRank z := by
        exact Int.toNat_le_toNat hxzEffect
      have heInterval :
          effect x ≤ effect x + (r : Int) ∧
            effect x + (r : Int) ≤ effect z := by
        constructor <;> omega
      have hC90 :=
        existsUnique_canonicalLeftGreedyActiveSupport_in_reversePointwiseInterval_iff_mem_ledgerEffectInterval
          p
          x
          z
      dsimp only at hC90
      obtain ⟨y, ⟨⟨hyCanonical, hyEffect, _hyBetween⟩, hyUnique⟩⟩ :=
        (hC90 hxCanonical hzCanonical (effect x + (r : Int))).mpr
          heInterval
      change effect y = effect x + (r : Int) at hyEffect
      have hyNonneg : 0 ≤ effect y := by
        exact
          ledgerEffectOn_nonneg
            (paramsUOfProduct p)
            (productWindowU p)
            y
            hyCanonical.2.1
      have hyRankCast : (effectRank y : Int) = effect y := by
        dsimp [effectRank]
        exact Int.toNat_of_nonneg hyNonneg
      have hxyMetric :
          activeCoordinateL1Distance x y =
            natDistance (effectRank x) (effectRank y) := by
        simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
          activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
            p
            x
            y
            hxCanonical
            hyCanonical
      have hyzMetric :
          activeCoordinateL1Distance y z =
            natDistance (effectRank y) (effectRank z) := by
        simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
          activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
            p
            y
            z
            hyCanonical
            hzCanonical
      have hyRank : effectRank y = effectRank x + r := by
        omega
      have hyRankBetween :
          effectRank x ≤ effectRank y ∧ effectRank y ≤ effectRank z := by
        constructor <;> omega
      have hxyRadius : activeCoordinateL1Distance x y = r := by
        rw [hxyMetric]
        dsimp [natDistance]
        omega
      have hmetricGeodesic :
          activeCoordinateL1Distance x z =
            activeCoordinateL1Distance x y +
              activeCoordinateL1Distance y z := by
        rw [hxzMetric, hxyMetric, hyzMetric]
        dsimp [natDistance]
        exact
          (c97_natDistance_additive_iff_between
            (effectRank x)
            (effectRank z)
            (effectRank y)).mpr
              (Or.inl hyRankBetween)
      refine
        ⟨y,
          ⟨⟨hyCanonical, hxyRadius, hmetricGeodesic⟩,
            ?_⟩⟩
      intro y' hy'
      have hy'Nonneg : 0 ≤ effect y' := by
        exact
          ledgerEffectOn_nonneg
            (paramsUOfProduct p)
            (productWindowU p)
            y'
            hy'.1.2.1
      have hy'RankCast : (effectRank y' : Int) = effect y' := by
        dsimp [effectRank]
        exact Int.toNat_of_nonneg hy'Nonneg
      have hxy'Metric :
          activeCoordinateL1Distance x y' =
            natDistance (effectRank x) (effectRank y') := by
        simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
          activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
            p
            x
            y'
            hxCanonical
            hy'.1
      have hy'zMetric :
          activeCoordinateL1Distance y' z =
            natDistance (effectRank y') (effectRank z) := by
        simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
          activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
            p
            y'
            z
            hy'.1
            hzCanonical
      have hy'RankGeodesic :
          natDistance (effectRank x) (effectRank z) =
            natDistance (effectRank x) (effectRank y') +
              natDistance (effectRank y') (effectRank z) := by
        rw [← hxzMetric, ← hxy'Metric, ← hy'zMetric]
        exact hy'.2.2
      have hy'RankBetweenDisj :
          (effectRank x ≤ effectRank y' ∧ effectRank y' ≤ effectRank z) ∨
            (effectRank z ≤ effectRank y' ∧ effectRank y' ≤ effectRank x) := by
        exact
          (c97_natDistance_additive_iff_between
            (effectRank x)
            (effectRank z)
            (effectRank y')).mp
              (by simpa [natDistance] using hy'RankGeodesic)
      have hy'RankBetween :
          effectRank x ≤ effectRank y' ∧ effectRank y' ≤ effectRank z := by
        rcases hy'RankBetweenDisj with h | h
        · exact h
        · constructor <;> omega
      have hy'Rank : effectRank y' = effectRank x + r := by
        have hyrankDistance :
            natDistance (effectRank x) (effectRank y') = r := by
          rw [← hxy'Metric]
          exact hy'.2.1
        dsimp [natDistance] at hyrankDistance
        omega
      apply hyUnique
      refine ⟨hy'.1, ?_⟩
      change effect y' = effect x + (r : Int)
      omega
    · have hzxEffect : effect z ≤ effect x := by
        omega
      have hzxRank : effectRank z ≤ effectRank x := by
        exact Int.toNat_le_toNat hzxEffect
      have heInterval :
          effect z ≤ effect x - (r : Int) ∧
            effect x - (r : Int) ≤ effect x := by
        constructor <;> omega
      have hC90 :=
        existsUnique_canonicalLeftGreedyActiveSupport_in_reversePointwiseInterval_iff_mem_ledgerEffectInterval
          p
          z
          x
      dsimp only at hC90
      obtain ⟨y, ⟨⟨hyCanonical, hyEffect, _hyBetween⟩, hyUnique⟩⟩ :=
        (hC90 hzCanonical hxCanonical (effect x - (r : Int))).mpr
          heInterval
      change effect y = effect x - (r : Int) at hyEffect
      have hyNonneg : 0 ≤ effect y := by
        exact
          ledgerEffectOn_nonneg
            (paramsUOfProduct p)
            (productWindowU p)
            y
            hyCanonical.2.1
      have hyRankCast : (effectRank y : Int) = effect y := by
        dsimp [effectRank]
        exact Int.toNat_of_nonneg hyNonneg
      have hxyMetric :
          activeCoordinateL1Distance x y =
            natDistance (effectRank x) (effectRank y) := by
        simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
          activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
            p
            x
            y
            hxCanonical
            hyCanonical
      have hyzMetric :
          activeCoordinateL1Distance y z =
            natDistance (effectRank y) (effectRank z) := by
        simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
          activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
            p
            y
            z
            hyCanonical
            hzCanonical
      have hyRankBetween :
          effectRank z ≤ effectRank y ∧ effectRank y ≤ effectRank x := by
        constructor <;> omega
      have hxyRadius : activeCoordinateL1Distance x y = r := by
        rw [hxyMetric]
        dsimp [natDistance]
        omega
      have hmetricGeodesic :
          activeCoordinateL1Distance x z =
            activeCoordinateL1Distance x y +
              activeCoordinateL1Distance y z := by
        rw [hxzMetric, hxyMetric, hyzMetric]
        dsimp [natDistance]
        exact
          (c97_natDistance_additive_iff_between
            (effectRank x)
            (effectRank z)
            (effectRank y)).mpr
              (Or.inr hyRankBetween)
      refine
        ⟨y,
          ⟨⟨hyCanonical, hxyRadius, hmetricGeodesic⟩,
            ?_⟩⟩
      intro y' hy'
      have hy'Nonneg : 0 ≤ effect y' := by
        exact
          ledgerEffectOn_nonneg
            (paramsUOfProduct p)
            (productWindowU p)
            y'
            hy'.1.2.1
      have hy'RankCast : (effectRank y' : Int) = effect y' := by
        dsimp [effectRank]
        exact Int.toNat_of_nonneg hy'Nonneg
      have hxy'Metric :
          activeCoordinateL1Distance x y' =
            natDistance (effectRank x) (effectRank y') := by
        simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
          activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
            p
            x
            y'
            hxCanonical
            hy'.1
      have hy'zMetric :
          activeCoordinateL1Distance y' z =
            natDistance (effectRank y') (effectRank z) := by
        simpa [effect, effectRank, natDistance, activeCoordinateL1Distance] using
          activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
            p
            y'
            z
            hy'.1
            hzCanonical
      have hy'RankGeodesic :
          natDistance (effectRank x) (effectRank z) =
            natDistance (effectRank x) (effectRank y') +
              natDistance (effectRank y') (effectRank z) := by
        rw [← hxzMetric, ← hxy'Metric, ← hy'zMetric]
        exact hy'.2.2
      have hy'RankBetweenDisj :
          (effectRank x ≤ effectRank y' ∧ effectRank y' ≤ effectRank z) ∨
            (effectRank z ≤ effectRank y' ∧ effectRank y' ≤ effectRank x) := by
        exact
          (c97_natDistance_additive_iff_between
            (effectRank x)
            (effectRank z)
            (effectRank y')).mp
              (by simpa [natDistance] using hy'RankGeodesic)
      have hy'RankBetween :
          effectRank z ≤ effectRank y' ∧ effectRank y' ≤ effectRank x := by
        rcases hy'RankBetweenDisj with h | h
        · constructor <;> omega
        · exact h
      have hy'Rank : effectRank y' + r = effectRank x := by
        have hyrankDistance :
            natDistance (effectRank x) (effectRank y') = r := by
          rw [← hxy'Metric]
          exact hy'.2.1
        dsimp [natDistance] at hyrankDistance
        omega
      apply hyUnique
      refine ⟨hy'.1, ?_⟩
      change effect y' = effect x - (r : Int)
      omega

end UnrestrictedBridge
end VFH2
