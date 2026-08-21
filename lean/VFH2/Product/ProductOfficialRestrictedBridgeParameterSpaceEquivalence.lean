import VFH2.Product.ProductOfficialRestrictedBridgeStateTransport

/-!
# Product/Official Restricted-Bridge Parameter-Space Equivalence

Canonical parameter serialization reaches exactly the official well-formed
restricted parameters.  Active-list order and repetitions are preserved:
every official active index is converted to its typed width index and then
unflattened to the corresponding Product index.

Boundary:
- This connects only the parameter spaces of the two current restricted
  formalizations.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
- It introduces no new assumptions, dynamics, compatibility API, or workflow.
- Raw official parameters whose active indices are outside the declared width
  remain outside this equivalence.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeParameterSpaceEquivalence

open ProductOfficialRestrictedBridgeStateTransport

private def productActiveOfOfficial
    {d : Nat}
    (active : List Nat)
    (hwidth :
      ∀ k : Nat, k ∈ active → k < Typed.typedWidth d) :
    List (ProductIndex d) :=
  match active with
  | [] => []
  | k :: ks =>
      ProductIndex.unflatten
          ⟨k, hwidth k (by simp)⟩ ::
        productActiveOfOfficial ks (by
          intro j hj
          exact hwidth j (by simp [hj]))

private theorem map_flatten_val_productActiveOfOfficial
    {d : Nat}
    (active : List Nat)
    (hwidth :
      ∀ k : Nat, k ∈ active → k < Typed.typedWidth d) :
    (productActiveOfOfficial active hwidth).map
        (fun i => (ProductIndex.flatten i).val) =
      active := by
  induction active with
  | nil =>
      rfl
  | cons k ks ih =>
      simp only [productActiveOfOfficial, List.map_cons]
      rw [List.cons.injEq]
      constructor
      · exact congrArg Fin.val
          (ProductIndex.flatten_unflatten
            ⟨k, hwidth k (by simp)⟩)
      · exact ih (by
          intro j hj
          exact hwidth j (by simp [hj]))

private theorem productActiveOfOfficial_map_flatten_val
    {d : Nat}
    (active : List (ProductIndex d))
    (hwidth :
      ∀ k : Nat,
        k ∈ active.map (fun i => (ProductIndex.flatten i).val) →
          k < Typed.typedWidth d) :
    productActiveOfOfficial
        (active.map (fun i => (ProductIndex.flatten i).val))
        hwidth =
      active := by
  induction active with
  | nil =>
      rfl
  | cons i is ih =>
      simp only [List.map_cons, productActiveOfOfficial]
      rw [List.cons.injEq]
      constructor
      · exact ProductIndex.unflatten_flatten i
      · exact ih (by
          intro k hk
          exact hwidth k (List.mem_cons_of_mem _ hk))

/--
Decode well-formed official parameters into Product parameters.

The official active-width invariant supplies the bound required to unflatten
every entry without adding a default index.
-/
def productParamsOfOfficialWellFormed
    (wp : RestrictedBridge.WellFormedRestrictedParams) :
    ProductRestrictedParams :=
  { n := wp.params.n
    d := wp.params.d
    active :=
      productActiveOfOfficial wp.params.active (by
        intro k hk
        have h := wp.activeWithinWidth k hk
        simpa [RestrictedBridge.expectedWidth, Typed.typedWidth] using h) }

/--
Serializing decoded well-formed official parameters returns the original
official parameter record, including the exact active-list order and
multiplicity.
-/
private theorem officialRestrictedParams_productParamsOfOfficialWellFormed
    (wp : RestrictedBridge.WellFormedRestrictedParams) :
    officialRestrictedParams
        (productParamsOfOfficialWellFormed wp) =
      wp.params := by
  cases wp with
  | mk params hwidth =>
      cases params with
      | mk n d active =>
          simp only [productParamsOfOfficialWellFormed,
            officialRestrictedParams,
            ProductParamsTransport.typedParamsOfProduct, List.map_map]
          apply congrArg
            (fun xs : List Nat =>
              RestrictedBridge.RestrictedParams.mk n d xs)
          simpa [Function.comp_def] using
            map_flatten_val_productActiveOfOfficial active (by
              intro k hk
              have h := hwidth k hk
              simpa [RestrictedBridge.expectedWidth, Typed.typedWidth]
                using h)

/--
Canonical well-formed serialization after decoding is the identity on official
well-formed parameters.
-/
theorem officialWellFormedRestrictedParams_productParamsOfOfficialWellFormed
    (wp : RestrictedBridge.WellFormedRestrictedParams) :
    officialWellFormedRestrictedParams
        (productParamsOfOfficialWellFormed wp) =
      wp := by
  cases wp with
  | mk params hwidth =>
      have hparams :
          officialRestrictedParams
              (productParamsOfOfficialWellFormed
                ⟨params, hwidth⟩) =
            params :=
        officialRestrictedParams_productParamsOfOfficialWellFormed
          ⟨params, hwidth⟩
      unfold officialWellFormedRestrictedParams
      rw [RestrictedBridge.WellFormedRestrictedParams.mk.injEq]
      exact hparams

/--
Decoding the canonical well-formed serialization of Product parameters returns
the original Product parameter record.
-/
theorem productParamsOfOfficialWellFormed_officialWellFormedRestrictedParams
    (p : ProductRestrictedParams) :
    productParamsOfOfficialWellFormed
        (officialWellFormedRestrictedParams p) = p := by
  cases p with
  | mk n d active =>
      simp only [productParamsOfOfficialWellFormed,
        officialWellFormedRestrictedParams, officialRestrictedParams,
        ProductParamsTransport.typedParamsOfProduct, List.map_map]
      apply congrArg
        (fun xs : List (ProductIndex d) =>
          ProductRestrictedParams.mk n d xs)
      simpa [Function.comp_def] using
        productActiveOfOfficial_map_flatten_val active (by
          intro k hk
          rcases List.mem_map.mp hk with ⟨i, _hi, rfl⟩
          exact (ProductIndex.flatten i).isLt)

end ProductOfficialRestrictedBridgeParameterSpaceEquivalence
end VFH2
