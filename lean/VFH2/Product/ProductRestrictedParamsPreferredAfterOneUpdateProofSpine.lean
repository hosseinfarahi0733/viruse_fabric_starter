import VFH2.Product.ProductRestrictedParamsInactiveCoordAfterOneUpdateProofSpine
import VFH2.Product.ProductRestrictedParamsPreferredFrontDoor

/-!
# VF-H2 Preferred Construction After One Product Update

This file connects the preferred restricted-parameter construction to the
after-one-update restricted proof spine.

Scientific role:
- The initial product state is arbitrary.
- Parameters enter through the preferred construction API.
- Active noncoverage is derived by that API.
- An inactive-index certificate is derived from the preferred certificate.
- The inactive-coordinate score, natural bounds, one-step fixedness, and final
  restricted proof-spine target are all derived rather than assumed.

Architecture:
- Raw erase-construction declarations are not used downstream.
- The route passes only through
  `ProductRestrictedParamsPreferredFrontDoor`.
-/

namespace VFH2

namespace ProductRestrictedParamsPreferredAfterOneUpdateProofSpine

/--
Inactive-index certificate obtained from the preferred construction API.
-/
noncomputable def preferredInactiveIndexCertificate
    (n d : Nat)
    (missing : ProductIndex d) :
    ProductRestrictedParamsInactiveCoordScore.InactiveIndexCertificate
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing) :=
  ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate.toInactiveIndexCertificate
    (ProductRestrictedParamsPreferredFrontDoor.preferredParams
      n d missing)
    (ProductRestrictedParamsPreferredFrontDoor.preferredActiveNoncoverageCertificate
      n d missing)

/--
Every initial state for preferred constructed parameters enters the current
restricted proof spine after one concrete product update.

The inactive coordinate, score semantics, natural score bounds, and one-step
fixedness are all derived.
-/
theorem restrictedParams_preferredParams_after_one_update_to_currentBestMainTheorem
    (n d : Nat)
    (missing : ProductIndex d)
    (x :
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing).State) :
    let p :=
      ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing
    let cert :=
      preferredInactiveIndexCertificate n d missing
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p
      (productUpdateState p x)
      (productUpdateState p)
      (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
        p cert.i)
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p
        (productUpdateState p x)
        (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p
        (productUpdateState p x)
        (productUpdateState p)
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i))
      (ProductFixedSet p (productUpdateState p x))
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n) := by
  dsimp only

  exact
    ProductRestrictedParamsInactiveCoordAfterOneUpdateProofSpine.restrictedParams_inactiveCoordScore_after_one_update_to_currentBestMainTheorem
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing)
      x
      (preferredInactiveIndexCertificate n d missing).i
      (preferredInactiveIndexCertificate n d missing).inactive

end ProductRestrictedParamsPreferredAfterOneUpdateProofSpine

end VFH2
