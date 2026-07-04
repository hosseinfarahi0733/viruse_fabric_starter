# VF-H2 v12.8.0 — Generalized Certificate Release Audit

## Purpose

This milestone is an audit and release-correction record. It does not add a new
mathematical theorem. Its purpose is to preserve a clear, manuscript-safe record
after the generalized transport certificate required two failed tagged attempts
before the clean build was established.

## Current clean release-bearing certificate

- Clean certificate tag: `v12.7.2`
- Clean certificate commit: `94b265a`
- Baseline branch at audit start: `master`
- Baseline HEAD at audit start: `94b265a`
- Baseline `lake build`: passed

## Correction record

| Tag | Commit | Status | Release-bearing? | Claim policy |
|---|---:|---|---:|---|
| `v12.7.0` | `f737dec` | build-failing attempt | no | do not cite as clean theorem milestone |
| `v12.7.1` | `9b95454` | build-failing attempt | no | do not cite as clean theorem milestone |
| `v12.7.2` | `94b265a` | clean build release | yes | cite as generalized transport certificate milestone |

## Tag policy

No tag was moved. No failed tag was rewritten. The correction was recorded by
creating a new patch tag, `v12.7.2`, after a successful full `lake build`.

## Allowed claim for `v12.7.2`

`v12.7.2` proves a Lean-machine-checked generalized transport ladder certificate
collecting active-set membership, pointwise predicate transport, fixed-set
generalization, active-update generalization, generic effect transport, and
generic bridge-target transport.

## Allowed claim for `v12.8.0`

`v12.8.0` records a release-correction audit and manifest for the generalized
transport certificate, marking `v12.7.2` as the clean release-bearing certificate
tag and preserving `v12.7.0`/`v12.7.1` as non-release-bearing failed attempts
without moving tags.

## Explicit non-claims

This audit does not claim:

- full VF-H2 theory;
- unrestricted VF-H2 theorem;
- empirical validation;
- biological validation;
- manuscript-ready full theory;
- clean release status for `v12.7.0` or `v12.7.1`.

## Manuscript-safe ledger line

`v12.7.2 clean generalized transport certificate; v12.8.0 release-correction audit and manifest.`
