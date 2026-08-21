import VFH2.Product.ProductRestrictedParamsProofSpineScoreWindowCharacterization

/-!
# Restricted Product Ledger-Effect Proof-Spine Characterization

This module instantiates the current restricted proof spine with its concrete
one-step ledger-effect score and the exact zero window.  On that semantic
instantiation, the entire frozen proof-spine target holds exactly at the
Product fixed set.  Consequently neither a separate score-preservation
assumption nor separate score bounds remain in the theorem statement.

Boundary:
- This concerns only the current `ProductRestrictedParams` model.
- The score is the existing `productLedgerEffect`; no score or update is
  introduced.
- The zero window is exact rather than an arbitrary threshold specialization.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace ProductRestrictedParamsLedgerEffectProofSpineCharacterization

/--
With product ledger effect as the score and `[0, 0]` as the score window, the
current restricted proof-spine target is equivalent to Product fixedness.
-/
theorem restrictedParams_productLedgerEffect_proofSpineTarget_iff_productFixedSet
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        x
        (productUpdateState p)
        (productLedgerEffect p)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          x
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          x
          (productUpdateState p)
          (productLedgerEffect p))
        (ProductFixedSet p x)
        0
        0
        (Int.le_refl 0)
      ↔
    ProductFixedSet p x := by
  rw [
    ProductRestrictedParamsProofSpineScoreWindowCharacterization.restrictedParams_restrictedProofSpineTarget_iff_fixedSet_and_baseScoreBounds
  ]
  constructor
  · intro hTarget
    exact hTarget.1
  · intro hFixed
    have hEffectZero :
        productLedgerEffect p x = 0 :=
      (productLedgerEffect_eq_zero_iff_productFixedSet p x).2 hFixed
    rw [hEffectZero]
    exact ⟨hFixed, Int.le_refl 0, Int.le_refl 0⟩

end ProductRestrictedParamsLedgerEffectProofSpineCharacterization
end VFH2
