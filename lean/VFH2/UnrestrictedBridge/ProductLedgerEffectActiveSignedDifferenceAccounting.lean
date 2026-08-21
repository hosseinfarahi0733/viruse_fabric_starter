import VFH2.UnrestrictedBridge.ProductLedgerEffectQuantitativeCharacterization

/-!
# Signed Two-State Product Ledger-Effect Accounting

This module compares the remaining ledger effects of two arbitrary Product
states. The total signed change from the first state to the second state on
active coordinates accounts exactly for the change in remaining effect.

The canonical `WidthIndex` enumeration visits every Product coordinate once.
Activity is tested by membership, so repeated entries in `p.active` do not
multiply a coordinate's contribution.

Boundary:
- This concerns the existing finite restricted Product model.
- It uses only the canonical finite Product coordinate enumeration.
- It does not define or use a global infinite ledger.
- It is not unrestricted `TTP-VF-H2-004`.
- It makes no full-theory, empirical, or biological claim.
- It introduces no new assumptions.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem natCast_sum_ofFn_eq_add_sum_ofFn
    (n : Nat)
    (f g : Fin n → Nat)
    (delta : Fin n → Int)
    (hpointwise :
      ∀ i : Fin n,
        (f i : Int) = (g i : Int) + delta i) :
    ((List.ofFn f).sum : Int) =
      ((List.ofFn g).sum : Int) +
        (List.ofFn delta).sum := by
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
For any two Product states, the remaining effect at `x` is the remaining
effect at `z` plus the sum of the signed active-coordinate changes from `x`
to `z`.
-/
theorem productLedgerEffect_eq_add_sum_activeSignedDifferences
    (p : ProductRestrictedParams)
    (x z : p.State) :
    productLedgerEffect p x =
      productLedgerEffect p z +
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              ((z (ProductIndex.unflatten w)).val : Int) -
                ((x (ProductIndex.unflatten w)).val : Int)
            else
              0)).sum := by
  rw [
    productLedgerEffect_eq_sum_activeDeficits p x,
    productLedgerEffect_eq_sum_activeDeficits p z
  ]

  apply
    natCast_sum_ofFn_eq_add_sum_ofFn
      (Typed.typedWidth p.d)
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          p.n - (x (ProductIndex.unflatten w)).val
        else
          0)
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          p.n - (z (ProductIndex.unflatten w)).val
        else
          0)
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          ((z (ProductIndex.unflatten w)).val : Int) -
            ((x (ProductIndex.unflatten w)).val : Int)
        else
          0)

  intro w
  by_cases hw : ProductIndex.unflatten w ∈ p.active
  · simp only [hw, ↓reduceIte]
    have hx :
        (x (ProductIndex.unflatten w)).val ≤ p.n :=
      (x (ProductIndex.unflatten w)).bound
    have hz :
        (z (ProductIndex.unflatten w)).val ≤ p.n :=
      (z (ProductIndex.unflatten w)).bound
    omega
  · simp [hw]

end UnrestrictedBridge
end VFH2
