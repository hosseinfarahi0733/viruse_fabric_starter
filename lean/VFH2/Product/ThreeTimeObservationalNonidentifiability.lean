import VFH2.Product.ThreeTimeGeometryCausalityIndependence

/-!
# C137: Observational Nonidentifiability of Present Causality

The two Boolean countermodels from C136 generate exactly the same complete
observational trajectory at every past value.  Nevertheless, one has no
present-to-future causal effect and the other has a concrete present
intervention effect.

Claim boundary: this is an explicit finite semantic counterexample showing
that complete observational trajectories do not determine the intervention
semantics in this model class.  It is not a statistical identifiability result,
a causal discovery procedure, or empirical, biological, or physical evidence.
-/

namespace VFH2
namespace ThreeTime

/--
Past-driven and present-driven Boolean SCMs agree field-by-field on every
realized observation but disagree on whether present interventions can change
the future.
-/
theorem pastDriven_presentDriven_same_completeObservations_different_presentCausality :
    (∀ past : Bool,
      (pastDrivenBooleanSCM.realize past).past =
          (presentDrivenBooleanSCM.realize past).past ∧
        (pastDrivenBooleanSCM.realize past).present =
          (presentDrivenBooleanSCM.realize past).present ∧
        (pastDrivenBooleanSCM.realize past).future =
          (presentDrivenBooleanSCM.realize past).future) ∧
      ¬ PresentHasCausalEffectOnFuture pastDrivenBooleanSCM ∧
      PresentHasCausalEffectOnFuture presentDrivenBooleanSCM := by
  refine ⟨?_,
    pastDrivenBooleanSCM_nonChain_without_presentCausalEffect.2.2,
    presentDrivenBooleanSCM_chain_with_presentCausalEffect.2.2⟩
  intro past
  cases past <;> exact ⟨rfl, rfl, rfl⟩

end ThreeTime
end VFH2
