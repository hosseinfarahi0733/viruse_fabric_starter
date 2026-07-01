import VFH2.RestrictedBridge.MembershipTopBridge

/-!
# VF-H2 Restricted Bridge Fixed-Set to Membership-Top Bridge

This file adds proof-bearing Lean lemmas connecting the scaffold fixed-set
predicate `inFixedSetR` to the membership-top update predicate.

Boundary:
- This proves a scaffold-level fixed-set-to-zero-effect bridge under the
  explicit `activeIndexSound p` assumption.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

Remaining future proof obligations:
- prove or eliminate the `activeIndexSound p` assumption;
- prove nonfixed witness;
- prove positive ledger effect;
- combine the final restricted bridge theorem.
-/

namespace VFH2
namespace RestrictedBridge

/-- Local getD-top condition along a traversal starting at global index `base`.

For a suffix state `x`, local offset `offset` corresponds to global index
`base + offset`.
-/
def localGetDTopFrom (p : RestrictedParams) (base : Nat) (x : State) : Prop :=
  ∀ offset : Nat, base + offset ∈ p.active → x.getD offset 0 = p.n

/-- Local getD-top condition implies membership-top along the same traversal. -/
theorem membershipTopForUpdate_of_localGetDTopFrom
    (p : RestrictedParams) (x : State) (base : Nat)
    (h : localGetDTopFrom p base x) :
    membershipTopForUpdate p base x := by
  induction x generalizing base with
  | nil =>
      simp [membershipTopForUpdate]
  | cons a xs ih =>
      have hhead : base ∈ p.active → a = p.n := by
        intro hbase
        have hv : (a :: xs).getD 0 0 = p.n := by
          simpa using h 0 (by simpa using hbase)
        simpa using hv
      have htail : localGetDTopFrom p (base + 1) xs := by
        intro offset hoff
        have hoff' : base + (offset + 1) ∈ p.active := by
          have heq : base + (offset + 1) = base + 1 + offset := by
            omega
          rwa [heq]
        have hv : (a :: xs).getD (offset + 1) 0 = p.n := h (offset + 1) hoff'
        simpa using hv
      exact And.intro hhead (ih (base + 1) htail)

/-- The original scaffold fixed-set predicate implies membership-top from index zero. -/
theorem membershipTopForUpdate_of_inFixedSetR
    (p : RestrictedParams) (x : State)
    (hfixed : inFixedSetR p x) :
    membershipTopForUpdate p 0 x := by
  apply membershipTopForUpdate_of_localGetDTopFrom p x 0
  intro offset hoff
  simpa using hfixed offset (by simpa using hoff)

/-- Fixed-set states have zero scaffold ledger effect under active-index soundness.

This proves the fixed-set zero-effect half for the current scaffold update path,
modulo the explicit Boolean-membership soundness assumption.
-/
theorem ledgerEffectR_zero_of_inFixedSetR
    (p : RestrictedParams) (x : State)
    (hsound : activeIndexSound p)
    (hfixed : inFixedSetR p x) :
    ledgerEffectR p x = 0 := by
  exact ledgerEffectR_zero_of_membershipTopForUpdate
    p x hsound
    (membershipTopForUpdate_of_inFixedSetR p x hfixed)

/-- Fixed-set states satisfy the fixed-zero-effect target under active-index soundness. -/
theorem updateFixedZeroEffectTarget_of_inFixedSetR
    (p : RestrictedParams) (x : State)
    (hsound : activeIndexSound p) :
    updateFixedZeroEffectTarget p x := by
  intro _hspace hfixed
  exact ledgerEffectR_zero_of_inFixedSetR p x hsound hfixed

end RestrictedBridge
end VFH2
