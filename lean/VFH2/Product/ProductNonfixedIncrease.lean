import VFH2.Product.ProductUpdate

/-!
# VF-H2 v11 Product Nonfixed Increase Lemma

This file proves the first product-index increase witness lemma.

Boundary:
- This is a restricted product-index lemma.
- It proves existence of one active coordinate whose value strictly increases
  under the product update when the state is not fixed.
- It does not define product ledger semantics.
- It does not prove positive product ledger effect.
- It does not prove the product restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2

/--
If a product-index state is not fixed on the active set, then some active
coordinate is not already at top value.

This proof avoids `push_neg` and `by_contra`, keeping it compatible with the
current project environment.
-/
theorem product_exists_active_not_top_of_not_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ ProductFixedSet p x) :
    ∃ i : ProductIndex p.d,
      i ∈ p.active ∧
      (x i).val ≠ p.n := by
  classical
  by_cases hex :
      ∃ i : ProductIndex p.d,
        i ∈ p.active ∧
        (x i).val ≠ p.n
  · exact hex
  · have hfixed : ProductFixedSet p x := by
      unfold ProductFixedSet
      intro i hi
      by_cases hval : (x i).val = p.n
      · exact hval
      · have hw :
            ∃ j : ProductIndex p.d,
              j ∈ p.active ∧
              (x j).val ≠ p.n := by
          exact ⟨i, hi, hval⟩
        exact False.elim (hex hw)
    exact False.elim (hnotfixed hfixed)

/--
If a product-index state is not fixed on the active set, then the product update
strictly increases at least one active coordinate.

This is the product-index analogue of the v10 nonfixed coordinate increase
witness, now over

  ProductIndex d = TimeLayer × SpaceIndex d.
-/
theorem product_exists_active_update_val_lt_of_not_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ ProductFixedSet p x) :
    ∃ i : ProductIndex p.d,
      i ∈ p.active ∧
      (x i).val < (productUpdateState p x i).val := by
  classical
  have hex := product_exists_active_not_top_of_not_fixed hnotfixed
  cases hex with
  | intro i hpair =>
      cases hpair with
      | intro hi_active hi_not_top =>
          refine ⟨i, hi_active, ?_⟩
          rw [productUpdateState_active_val_eq_top p x hi_active]
          exact Nat.lt_of_le_of_ne (x i).bound hi_not_top

end VFH2
