# VF-H2 v12.0.0 — Controlled Generalization Roadmap

## Status

This roadmap starts from the clean v11.9.0 restricted scaffold audit.
The v11 line established and audited a Lean-machine-checked Product/Typed
transport ladder for the current restricted VF-H2 scaffold.

Baseline tag:

```text
v11.9.0
```

Baseline audited certificate:

```lean
VFH2.ProductTransportLadderCertificate.transportLadder_certificate
```

## What v12.0.0 claims

v12.0.0 records a controlled generalization roadmap and gap register for moving
beyond the current restricted VF-H2 scaffold.

It is a planning and audit milestone. It does not claim that the unrestricted
VF-H2 theory has been proven.

## What v12.0.0 does not claim

```text
Full VF-H2 theory proven: no
Unrestricted theorem proven: no
Empirical validation proven: no
Biological validation proven: no
Biological interpretation validated: no
Manuscript-ready full theory: no
```

## Generalization principle

The v12 line should generalize one restriction at a time. Each new theorem must
be tied to an already audited v11 theorem whenever possible. The preferred proof
style is transport-preserving reuse, not theorem duplication.

The rule is:

```text
Keep the Product/Typed transport ladder intact while relaxing exactly one
well-named restriction per milestone.
```

## Candidate restrictions to inspect

The following restriction families should be inspected before any proof attempt:

1. Shape restrictions on the Product index space.
2. Active-set restrictions in ProductRestrictedParams and TypedRestrictedParams.
3. Top-coordinate update restriction.
4. Ledger aggregation restriction.
5. Fixed-set predicate restriction.
6. Restricted bridge-target definition.

## Recommended v12 sequence

### v12.1.0 — Restriction inventory in Lean-facing form

Goal:
Record the exact definitions that make the current scaffold restricted.

Expected outputs:

```text
outputs/v12_1_restriction_inventory.md
outputs/v12_1_definition_surface.txt
```

No new theorem claim unless definitions are also wrapped in a checkable target.

### v12.2.0 — First reusable abstraction boundary

Goal:
Identify the first restriction that can be abstracted without changing the
transport ladder.

Candidate target:
abstract active-set membership transport into a reusable interface or lemma
family.

### v12.3.0 — Generalized active-set transport

Goal:
Prove a controlled generalization of active-set membership transport.

Safety rule:
Do not change update, ledger, fixed-set, or bridge claims in this milestone.

### v12.4.0 — Generalized update transport

Goal:
Extend update-state transport after the active-set generalization is stable.

### v12.5.0 — Generalized ledger/effect transport

Goal:
Lift ledger and ledger-effect transport to the newly generalized layer.

### v12.6.0 — Generalized fixed-set and bridge transport

Goal:
Only after update and ledger-effect are stable, lift fixed-set and bridge target.

## Proof hygiene requirements

Every v12 milestone must pass:

```bash
lake build
grep -RInE '\bsorry\b|\badmit\b|\baxiom\b|\bunsafe\b' lean/VFH2/Product lean/VFH2/Typed || true
```

A milestone is not considered valid if the proof is replaced by report-only
language or by an alias theorem that does not add the claimed generalization.

## Manuscript-safe contribution wording

Safe wording:

```text
The v11 line establishes a Lean-machine-checked restricted Product/Typed
transport ladder. The v12 line begins a controlled roadmap for generalizing the
restricted scaffold while preserving this transport structure.
```

Unsafe wording:

```text
The unrestricted VF-H2 theory is proven.
```

## Decision

The team decision for v12 is controlled generalization, not claim inflation.
The next implementation milestone should be v12.1.0: a Lean-facing restriction
inventory and definition-surface audit.
