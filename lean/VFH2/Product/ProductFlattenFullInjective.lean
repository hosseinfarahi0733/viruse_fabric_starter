import VFH2.Product.ProductFlattenInjective

/-!
# VF-H2 v11 Product Flatten Full Injectivity

This file proves full injectivity of the v11 product-to-width flatten map.

Boundary:
- This is still an index-level bridge.
- It proves injectivity of `ProductIndex.flatten`.
- It does not define `unflatten`.
- It does not prove surjectivity.
- It does not prove ledger equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductIndex

/--
Every `TimeLayer = Fin 3` is one of the three explicit VF-H2 layers.
This avoids relying on the unavailable `fin_cases` tactic.
-/
private theorem timeLayer_eq_t1_or_t2_or_t3 (t : TimeLayer) :
    t = TimeLayer.t1 ∨ t = TimeLayer.t2 ∨ t = TimeLayer.t3 := by
  rcases t with ⟨v, hv⟩
  have hv_cases : v = 0 ∨ v = 1 ∨ v = 2 := by
    omega
  rcases hv_cases with h0 | hrest
  · left
    apply Fin.ext
    simpa [TimeLayer.t1] using h0
  · rcases hrest with h1 | h2
    · right
      left
      apply Fin.ext
      simpa [TimeLayer.t2] using h1
    · right
      right
      apply Fin.ext
      simpa [TimeLayer.t3] using h2

/--
The product-to-width flatten map is injective.

If two explicit product indices flatten to the same v10 width index,
then the original product indices are equal.
-/
theorem flatten_injective {d : Nat} :
    Function.Injective (@flatten d) := by
  intro i j h
  rcases i with ⟨tᵢ, sᵢ⟩
  rcases j with ⟨tⱼ, sⱼ⟩

  rcases timeLayer_eq_t1_or_t2_or_t3 tᵢ with htᵢ1 | htᵢrest
  · cases htᵢ1
    rcases timeLayer_eq_t1_or_t2_or_t3 tⱼ with htⱼ1 | htⱼrest
    · cases htⱼ1
      exact flatten_t1_pair_injective h
    · rcases htⱼrest with htⱼ2 | htⱼ3
      · cases htⱼ2
        exfalso
        exact flatten_t1_ne_flatten_t2 sᵢ sⱼ h
      · cases htⱼ3
        exfalso
        exact flatten_t1_ne_flatten_t3 sᵢ sⱼ h

  · rcases htᵢrest with htᵢ2 | htᵢ3
    · cases htᵢ2
      rcases timeLayer_eq_t1_or_t2_or_t3 tⱼ with htⱼ1 | htⱼrest
      · cases htⱼ1
        exfalso
        exact flatten_t2_ne_flatten_t1 sᵢ sⱼ h
      · rcases htⱼrest with htⱼ2 | htⱼ3
        · cases htⱼ2
          exact flatten_t2_pair_injective h
        · cases htⱼ3
          exfalso
          exact flatten_t2_ne_flatten_t3 sᵢ sⱼ h

    · cases htᵢ3
      rcases timeLayer_eq_t1_or_t2_or_t3 tⱼ with htⱼ1 | htⱼrest
      · cases htⱼ1
        exfalso
        exact flatten_t3_ne_flatten_t1 sᵢ sⱼ h
      · rcases htⱼrest with htⱼ2 | htⱼ3
        · cases htⱼ2
          exfalso
          exact flatten_t3_ne_flatten_t2 sᵢ sⱼ h
        · cases htⱼ3
          exact flatten_t3_pair_injective h

/--
Equality of flattened width indices is equivalent to equality of the
original product indices.
-/
theorem flatten_eq_iff_eq {d : Nat} {i j : ProductIndex d} :
    flatten i = flatten j ↔ i = j := by
  constructor
  · intro h
    exact flatten_injective h
  · intro h
    cases h
    rfl

end ProductIndex

end VFH2
