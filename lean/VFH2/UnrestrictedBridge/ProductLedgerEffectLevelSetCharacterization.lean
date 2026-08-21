import VFH2.UnrestrictedBridge.ProductLedgerEffectActiveSignedDifferenceAccounting

/-!
# Product Ledger-Effect Level-Set Characterization

For fixed restricted Product parameters, this module characterizes every fiber
of `productLedgerEffect`: two states have the same remaining effect exactly
when their canonical totals of active-coordinate values agree. Inactive
coordinates are irrelevant to this observable, while pointwise agreement on
active coordinates is sufficient but not necessary.

The canonical `WidthIndex` enumeration visits every Product coordinate once.
Activity is tested by membership, so repeated entries in `p.active` do not
multiply a coordinate's contribution.

Boundary:
- This concerns only the existing finite restricted Product model.
- It uses only the canonical finite Product coordinate enumeration.
- It does not define or use a global infinite ledger.
- It is not unrestricted `TTP-VF-H2-004`.
- It makes no full-theory, empirical, or biological validation claim.
- It introduces no new assumptions.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem sum_ofFn_signed_eq_sub_natCast_sums
    (n : Nat)
    (f g : Fin n → Nat)
    (delta : Fin n → Int)
    (hpointwise :
      ∀ i : Fin n,
        delta i = (g i : Int) - (f i : Int)) :
    (List.ofFn delta).sum =
      ((List.ofFn g).sum : Int) -
        ((List.ofFn f).sum : Int) := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp only [List.ofFn_succ, List.sum_cons, Int.natCast_add]
      rw [
        ih
          (fun i => f i.succ)
          (fun i => g i.succ)
          (fun i => delta i.succ)
          (fun i => hpointwise i.succ)
      ]
      have hzero := hpointwise (0 : Fin (n + 1))
      omega

/--
For fixed Product parameters, equality of remaining ledger effects is
equivalent to equality of the canonical totals of active-coordinate values.
-/
theorem productLedgerEffect_eq_productLedgerEffect_iff_sum_activeValues_eq
    (p : ProductRestrictedParams)
    (x z : p.State) :
    productLedgerEffect p x = productLedgerEffect p z ↔
      (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            (x (ProductIndex.unflatten w)).val
          else
            0)).sum =
      (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            (z (ProductIndex.unflatten w)).val
          else
            0)).sum := by
  have hsigned :
      (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            ((z (ProductIndex.unflatten w)).val : Int) -
              ((x (ProductIndex.unflatten w)).val : Int)
          else
            0)).sum =
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              (z (ProductIndex.unflatten w)).val
            else
              0)).sum : Int) -
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              (x (ProductIndex.unflatten w)).val
            else
              0)).sum : Int) := by
    apply
      sum_ofFn_signed_eq_sub_natCast_sums
        (Typed.typedWidth p.d)
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            (x (ProductIndex.unflatten w)).val
          else
            0)
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            (z (ProductIndex.unflatten w)).val
          else
            0)
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            ((z (ProductIndex.unflatten w)).val : Int) -
              ((x (ProductIndex.unflatten w)).val : Int)
          else
            0)
    intro w
    by_cases hw : ProductIndex.unflatten w ∈ p.active <;> simp [hw]

  have haccount :=
    productLedgerEffect_eq_add_sum_activeSignedDifferences p x z
  rw [hsigned] at haccount

  constructor
  · intro heffect
    have hcast :
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              (x (ProductIndex.unflatten w)).val
            else
              0)).sum : Int) =
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              (z (ProductIndex.unflatten w)).val
            else
              0)).sum : Int) := by
      omega
    exact Int.ofNat.inj hcast
  · intro hsum
    have hcast :=
      congrArg (fun n : Nat => (n : Int)) hsum
    omega

end UnrestrictedBridge
end VFH2
