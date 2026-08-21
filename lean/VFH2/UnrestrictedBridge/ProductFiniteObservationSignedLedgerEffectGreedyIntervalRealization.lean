import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyRecurrenceCharacterization

/-!
# Product finite-observation semantic greedy interval realization

This module upgrades semantic canonical effect-order reflection to exact
interval realization. Between any two semantic canonical Product-window
states, every integer between their signed ledger effects has a canonical
representative in the corresponding reverse pointwise interval. That
representative is unique among all canonical states with the chosen effect,
not merely among states already known to lie between the endpoints.

Existence starts in the bounded typed Product model, uses its exact effect
range, embeds the witness into `StateU`, and applies the semantic canonical
fiber theorem. The two endpoint inequalities are then reflected into the two
pointwise bounds. Conversely, those bounds recover the effect inequalities.
No endpoint-order assumption is needed: when the endpoint effect interval is
empty, the canonical pointwise interval is empty as well.

The canonical, effect, and interval predicates remain theorem-local. No
normalizer, order isomorphism, compatibility namespace, alias, public
definition, or model assumption is introduced.

Only the canonical finite Product observation window is involved. This does
not define a global infinite ledger, is not unrestricted `TTP-VF-H2-004`, and
makes no full-theory, empirical, physical, medical, causal, or biological
validation claim.
-/

namespace VFH2
namespace UnrestrictedBridge

/--
The signed ledger effect realizes exactly every integer between the effects of
two semantic canonical endpoints, with a globally unique canonical state in
their reverse pointwise interval.
-/
theorem existsUnique_canonicalLeftGreedyActiveSupport_in_reversePointwiseInterval_iff_mem_ledgerEffectInterval
    (p : ProductRestrictedParams)
    (x z : StateU) :
    let IsCanonicalLeftGreedy : StateU → Prop :=
      fun s =>
        (∀ j : Nat,
          j ∉ (paramsUOfProduct p).active →
            s j = 0) ∧
        inStateSpaceU
          (paramsUOfProduct p)
          s ∧
        ∀ u v : Typed.WidthIndex p.d,
          u.val < v.val →
          ProductIndex.unflatten u ∈ p.active →
          ProductIndex.unflatten v ∈ p.active →
          s u.val < p.n →
            s v.val = 0
    let effect : StateU → Int :=
      fun s =>
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          s
    let InReversePointwiseInterval : StateU → Prop :=
      fun y =>
        ∀ j : Nat,
          z j ≤ y j ∧ y j ≤ x j
    IsCanonicalLeftGreedy x →
    IsCanonicalLeftGreedy z →
    ∀ e : Int,
      ((∃ y : StateU,
          ((IsCanonicalLeftGreedy y ∧
            effect y = e ∧
            InReversePointwiseInterval y) ∧
          ∀ y' : StateU,
            (IsCanonicalLeftGreedy y' ∧
              effect y' = e) →
                y' = y)) ↔
        effect x ≤ e ∧ e ≤ effect z) := by
  dsimp only
  intro hxCanonical hzCanonical e
  constructor
  case mpr =>
    intro heInterval
    have hxNonneg :=
      ledgerEffectOn_nonneg
        (paramsUOfProduct p)
        (productWindowU p)
        x
        hxCanonical.2.1
    have hzFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        z
    have heRange :
        0 ≤ e ∧
          e ≤
            ((List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  p.n
                else
                  0)).sum : Int) := by
      constructor <;> omega
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
    have hcanonical :=
      existsUnique_canonicalLeftGreedyActiveSupport_in_productWindowUFiber_and_levelSet
        p
        s
        hsSpace
    dsimp only at hcanonical
    rcases hcanonical with
      ⟨y, ⟨⟨⟨hyCanonical, hyFiber⟩, hyUnique⟩, _⟩⟩
    have hyEffect :
        ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            y =
          e :=
      hyFiber.trans hsEffect
    have hxyEffect :
        ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            x ≤
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            y := by
      rw [hyEffect]
      exact heInterval.1
    have hyzEffect :
        ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            y ≤
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            z := by
      rw [hyEffect]
      exact heInterval.2
    have hyLeX :
        ∀ j : Nat,
          y j ≤ x j :=
      (ledgerEffectOn_productWindowU_le_iff_forall_reverse_le_of_canonicalLeftGreedy
        p
        x
        y
        hxCanonical
        hyCanonical).mp hxyEffect
    have hzLeY :
        ∀ j : Nat,
          z j ≤ y j :=
      (ledgerEffectOn_productWindowU_le_iff_forall_reverse_le_of_canonicalLeftGreedy
        p
        y
        z
        hyCanonical
        hzCanonical).mp hyzEffect
    refine
      ⟨y,
        ⟨⟨hyCanonical, hyEffect, ?_⟩,
          ?_⟩⟩
    · intro j
      exact ⟨hzLeY j, hyLeX j⟩
    · intro y' hy'
      apply hyUnique
      exact
        ⟨hy'.1,
          hy'.2.trans hsEffect.symm⟩
  case mp =>
    rintro ⟨y, ⟨⟨hyCanonical, hyEffect, hyBetween⟩, _⟩⟩
    have hxyEffect :=
      (ledgerEffectOn_productWindowU_le_iff_forall_reverse_le_of_canonicalLeftGreedy
        p
        x
        y
        hxCanonical
        hyCanonical).mpr
        (fun j => (hyBetween j).2)
    have hyzEffect :=
      (ledgerEffectOn_productWindowU_le_iff_forall_reverse_le_of_canonicalLeftGreedy
        p
        y
        z
        hyCanonical
        hzCanonical).mpr
        (fun j => (hyBetween j).1)
    constructor
    · simpa only [hyEffect] using hxyEffect
    · simpa only [hyEffect] using hyzEffect

end UnrestrictedBridge
end VFH2
