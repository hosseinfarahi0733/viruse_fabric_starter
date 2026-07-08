# VF-H2 Theory Statement

## Purpose

VF-H2 / Viruse Fabric is a formal Lean 4 project that studies a restricted product-index update model and proves a restricted proof-spine target under explicit assumptions.

The current project should be read as a conditional formal theory, not as a fully discharged domain theorem.

## Central question

Given a product-index state, update rule, score function, active coordinate set, and threshold interval, under what assumptions can the restricted proof-spine target be established?

## Current formal model

The current product model is centered on:

- `ProductRestrictedParams`
- `ProductIndex p.d`
- `p.State`
- `p.active`
- `productUpdateState`
- `ProductFixedSet p x`
- score-preserving policy conditions
- natural base bounds
- restricted proof-spine target

## Fixed-state predicate

The fixed-state predicate is:

`ProductFixedSet p x`

meaning:

For every active product-index coordinate `i`, if `i ∈ p.active`, then `(x i).val = p.n`.

This is currently a concrete but undischarged assumption.

## Main result, current status

The strongest current result proves the restricted proof-spine target from:

1. score preservation or an identity-like update route,
2. fixed-state evidence,
3. natural base interval bounds.

The result is conditional. The remaining assumptions are not yet derived from domain semantics.

## What the project is not yet proving

The current repository does not prove:

- that score preservation follows from product update semantics,
- that `ProductFixedSet p x` follows from product update, ledger, or domain semantics,
- that natural base bounds follow from initialization or domain semantics,
- that the full VF-H2 theory is assumption-free,
- that the model is empirically or biologically validated.

## Scientific success criterion

The project becomes scientifically stronger only when it reduces or derives fundamental assumptions, clarifies unavoidable assumptions, simplifies the proof architecture, or strengthens formal guarantees.

Counting theorem wrappers, files, or version numbers is not scientific progress.
