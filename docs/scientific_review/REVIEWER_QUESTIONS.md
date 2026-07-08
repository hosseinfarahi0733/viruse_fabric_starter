# Reviewer Questions for VF-H2

Use these prompts for a serious external-style review.

## Main reviewer prompt

Assume you are Reviewer #2 for a top-tier Formal Methods conference. Ignore my intentions and evaluate this repository exactly as you would evaluate a paper submission. Identify every scientific weakness, every architectural weakness, every unjustified assumption, every overclaim, every hidden dependency, and every place where the proof architecture can be fundamentally improved. Do not optimize for politeness; optimize for correctness and scientific rigor.

## Mathematics

Are the remaining assumptions mathematically meaningful, or are they so strong that the main theorem becomes nearly tautological?

Can score preservation realistically be derived from the update semantics?

Can `ProductFixedSet p x` realistically be derived from a domain or initialization condition?

Are the natural bounds domain facts, score-construction facts, or arbitrary hypotheses?

## Type theory

Is the proof architecture natural in Lean?

Are transport lemmas used appropriately, or are they hiding semantic debt?

Are there unnecessary abstraction layers?

Is the product/typed representation split justified?

## Formal verification

Does the project establish a theory, or only a conditional proof spine?

What would be required to turn the current conditional theorem into a stronger verified result?

Are the proof obligations stated explicitly enough for peer review?

## Software architecture

Are the layers cleanly separated?

Are theorem names and namespaces maintainable?

Are audit files and proof files separated properly?

Are wrapper-only theorem layers creating noise?

## Scientific review

If this were submitted to ITP, CPP, POPL, or CAV, what are the strongest reasons to reject it?

What is the minimal set of changes needed before the project has a defensible scientific contribution?

What should be removed or renamed to avoid overclaim?
