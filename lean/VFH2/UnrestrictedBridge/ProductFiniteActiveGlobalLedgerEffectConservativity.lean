import VFH2.UnrestrictedBridge.CountableFiniteActiveGlobalLedgerEffect

/-!
# Product Finite-Active Global Ledger-Effect Conservativity

This module gives the first direct numerical transport from the C100
window-free finite-active global effect to the native restricted Product
ledger effect. After the canonical Product embedding, summing the signed
change over every distinct active natural coordinate agrees exactly with
`productLedgerEffect`.

The proof is deliberately duplicate-safe. Product activity is membership
based, so a coordinate is updated and counted once even when `p.active`
contains repeated entries. The countable side first applies `List.eraseDups`;
the proof then identifies that sum with the membership mask on the canonical
Product width enumeration. No `Nodup` premise is introduced.

Boundary:
- The ambient `StateU` is countably indexed, but the complete active support
  transported from Product remains finite.
- The left side has no observation-window argument, but it is still a finite
  sum rather than an infinite series.
- This does not define genuinely infinite active support or a global state
  ledger over every natural coordinate.
- This is not unrestricted `TTP-VF-H2-004` and makes no full-theory,
  empirical, physical, or biological claim.
- Proof-spine and trajectory restatements are intentionally not added here;
  this milestone establishes the substantive numerical conservativity fact.
- No compatibility namespace, model assumption, or new front door is added.
-/

namespace VFH2
namespace UnrestrictedBridge

open ProductOfficialRestrictedBridgeStateTransport

private theorem c101_sum_map_zero
    (support : List Nat) :
    (support.map fun _ => (0 : Int)).sum = 0 := by
  induction support with
  | nil =>
      rfl
  | cons _ support ih =>
      simp only [List.map_cons, List.sum_cons]
      rw [ih]
      rfl

private theorem c101_map_eq_map_of_forall_mem
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

private theorem c101_sum_range_mask_cons_eq_add_filter
    (n a : Nat)
    (tail : List Nat)
    (f : Nat → Int)
    (ha : a < n) :
    ((List.range n).map fun i =>
        if i ∈ a :: tail then f i else 0).sum =
      f a +
        ((List.range n).map fun i =>
          if i ∈ tail.filter (fun b => !b == a) then f i else 0).sum := by
  induction n with
  | zero =>
      omega
  | succ n ih =>
      rw [List.range_succ, List.map_append, List.map_append]
      simp only [List.sum_append, List.map_singleton, List.sum_singleton]
      by_cases han : a = n
      · subst a
        have hprefix :
            (List.range n).map (fun i =>
                if i ∈ n :: tail then f i else 0) =
              (List.range n).map (fun i =>
                if i ∈ tail.filter (fun b => !b == n) then f i else 0) := by
          apply c101_map_eq_map_of_forall_mem
          intro i hi
          have hin : i < n := List.mem_range.mp hi
          have hne : i ≠ n := by omega
          simp [hne]
        rw [hprefix]
        simp
        omega
      · have ha' : a < n := by omega
        have hrec := ih ha'
        have hlast :
            (if n ∈ a :: tail then f n else 0) =
              (if n ∈ tail.filter (fun b => !b == a) then f n else 0) := by
          simp [Ne.symm han]
        omega

private theorem c101_sum_eraseDups_eq_sum_range_mask_fuel
    (fuel : Nat)
    (support : List Nat)
    (n : Nat)
    (f : Nat → Int)
    (hlen : support.length ≤ fuel)
    (hbound : ∀ i : Nat, i ∈ support → i < n) :
    (support.eraseDups.map f).sum =
      ((List.range n).map fun i =>
        if i ∈ support then f i else 0).sum := by
  induction fuel generalizing support with
  | zero =>
      have hzero : support.length = 0 := by omega
      have hs : support = [] := List.eq_nil_of_length_eq_zero hzero
      subst support
      simp only [List.eraseDups_nil, List.map_nil, List.sum_nil,
        List.not_mem_nil, ↓reduceIte]
      exact (c101_sum_map_zero (List.range n)).symm
  | succ fuel ih =>
      cases support with
      | nil =>
          simp only [List.eraseDups_nil, List.map_nil, List.sum_nil,
            List.not_mem_nil, ↓reduceIte]
          exact (c101_sum_map_zero (List.range n)).symm
      | cons a tail =>
          rw [List.eraseDups_cons, List.map_cons, List.sum_cons]
          have hlenFilter :
              (tail.filter (fun b => !b == a)).length ≤ fuel := by
            have hfilter :=
              List.length_filter_le (fun b => !b == a) tail
            simp only [List.length_cons] at hlen
            omega
          have hboundFilter :
              ∀ i : Nat,
                i ∈ tail.filter (fun b => !b == a) →
                i < n := by
            intro i hi
            exact hbound i (by
              have hitail : i ∈ tail := (List.mem_filter.mp hi).1
              simp [hitail])
          rw [ih
            (tail.filter (fun b => !b == a))
            hlenFilter
            hboundFilter]
          exact
            (c101_sum_range_mask_cons_eq_add_filter
              n
              a
              tail
              f
              (hbound a (by simp))).symm

private theorem c101_sum_eraseDups_eq_sum_range_mask
    (support : List Nat)
    (n : Nat)
    (f : Nat → Int)
    (hbound : ∀ i : Nat, i ∈ support → i < n) :
    (support.eraseDups.map f).sum =
      ((List.range n).map fun i =>
        if i ∈ support then f i else 0).sum := by
  exact
    c101_sum_eraseDups_eq_sum_range_mask_fuel
      support.length
      support
      n
      f
      (Nat.le_refl _)
      hbound

private theorem c101_sum_activeSignedDeficits_eq_natCastDeficits
    (p : ParamsU)
    (window : List Nat)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    (window.map fun i =>
        if i ∈ p.active then
          (p.top : Int) - (x i : Int)
        else
          0).sum =
      ((window.map fun i =>
        if i ∈ p.active then p.top - x i else 0).sum : Int) := by
  induction window with
  | nil =>
      rfl
  | cons i window ih =>
      simp only [List.map_cons, List.sum_cons, Int.natCast_add]
      rw [ih]
      by_cases hi : i ∈ p.active
      · simp only [hi, ↓reduceIte]
        have hle : x i ≤ p.top := hspace i
        omega
      · simp [hi]

/--
The complete deduplicated finite-active effect of the canonical Product
embedding is exactly the native Product ledger effect. Repeated active entries
cannot multiply a contribution, and no additional hypothesis is required.
-/
theorem finiteActiveGlobalLedgerEffectU_paramsUOfProduct_stateUOfProduct
    (p : ProductRestrictedParams)
    (x : p.State) :
    finiteActiveGlobalLedgerEffectU
        (paramsUOfProduct p)
        (stateUOfProduct p x) =
      productLedgerEffect p x := by
  have hspace :
      inStateSpaceU
        (paramsUOfProduct p)
        (stateUOfProduct p x) :=
    stateUOfProduct_inStateSpaceU p x

  have hbound :
      ∀ i : Nat,
        i ∈ (paramsUOfProduct p).active →
        i < RestrictedBridge.expectedWidth (officialRestrictedParams p) := by
    intro i hi
    exact
      List.mem_range.mp
        (show
          i ∈ List.range
            (RestrictedBridge.expectedWidth (officialRestrictedParams p))
          from productWindowU_covers_active p i hi)

  calc
    finiteActiveGlobalLedgerEffectU
          (paramsUOfProduct p)
          (stateUOfProduct p x) =
        ((paramsUOfProduct p).active.eraseDups.map fun i =>
          ((paramsUOfProduct p).top : Int) -
            (stateUOfProduct p x i : Int)).sum :=
      finiteActiveGlobalLedgerEffectU_eq_sum_activeSignedDeficits
        (paramsUOfProduct p)
        (stateUOfProduct p x)

    _ =
        ((List.range
          (RestrictedBridge.expectedWidth (officialRestrictedParams p))).map
          fun i =>
            if i ∈ (paramsUOfProduct p).active then
              ((paramsUOfProduct p).top : Int) -
                (stateUOfProduct p x i : Int)
            else
              0).sum :=
      c101_sum_eraseDups_eq_sum_range_mask
        (paramsUOfProduct p).active
        (RestrictedBridge.expectedWidth (officialRestrictedParams p))
        (fun i =>
          ((paramsUOfProduct p).top : Int) -
            (stateUOfProduct p x i : Int))
        hbound

    _ =
        (((productWindowU p).map fun i =>
          if i ∈ (paramsUOfProduct p).active then
            (paramsUOfProduct p).top - stateUOfProduct p x i
          else
            0).sum : Int) := by
      change
        ((productWindowU p).map fun i =>
          if i ∈ (paramsUOfProduct p).active then
            ((paramsUOfProduct p).top : Int) -
              (stateUOfProduct p x i : Int)
          else
            0).sum = _
      exact
        c101_sum_activeSignedDeficits_eq_natCastDeficits
          (paramsUOfProduct p)
          (productWindowU p)
          (stateUOfProduct p x)
          hspace

    _ =
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          (stateUOfProduct p x) :=
      (ledgerEffectOn_eq_sum_activeDeficits
        (paramsUOfProduct p)
        (productWindowU p)
        (stateUOfProduct p x)
        hspace).symm

    _ = productLedgerEffect p x :=
      ledgerEffectOn_productWindowU_stateUOfProduct p x

end UnrestrictedBridge
end VFH2
