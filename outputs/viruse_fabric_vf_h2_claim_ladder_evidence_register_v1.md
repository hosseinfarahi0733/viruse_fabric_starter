# VF-H2 Claim Ladder and Experiment Evidence Register v1

Action:
execute_vf_h2_claim_ladder_and_experiment_evidence_register_no_claim_validation

Scope:
safe abstract toy VF-H2 only.

Purpose:
Connect the proved restricted theorem and the existing experiment history to explicit claims, so experiments do not remain disconnected code artifacts.

This document does not introduce a new theorem.
This document does not prove the full Viruse Fabric theory.
This document does not claim empirical validation.
This document does not claim biological validation.
This document does not claim manuscript readiness.
This document does not claim submission readiness.

## Claim Ladder

| Claim ID | Claim | Current status | Evidence type |
|---|---|---|---|
| CLAIM-VF-H2-A | In the restricted finite coordinatewise safe abstract toy domain, RSW-VF-H2-001 through RSW-VF-H2-007 imply ledger_effect_size > 0. | proved | TTP-VF-H2-004-R + 4 lemmas |
| CLAIM-VF-H2-B | Synthetic toy experiments are consistent with CLAIM-VF-H2-A under matching assumptions. | not yet consolidated | requires experiment classification |
| CLAIM-VF-H2-C | The result extends to the original unrestricted TTP-VF-H2-004. | not proved | no proof |
| CLAIM-VF-H2-D | The result extends to a generalized ordered-domain theorem. | not ready / not proved | no proof |
| CLAIM-VF-H2-E | VF-H2 is empirically validated. | false / not established | no empirical validation |
| CLAIM-VF-H2-F | VF-H2 has biological validation. | false / not established | no biological validation |
| CLAIM-VF-H2-G | Full Viruse Fabric theory is proved. | not proved | no proof |

## Experiment Evidence Register Schema

Each past experiment must be classified into exactly one primary bucket:

| Bucket | Meaning |
|---|---|
| SUPPORTS_ASSUMPTIONS | The experiment checks or illustrates assumptions used by the restricted toy theorem. |
| SUPPORTS_CLAIM_B | The experiment is consistent with synthetic toy behavior expected from CLAIM-VF-H2-A. |
| TESTS_BOUNDARY | The experiment probes where the restricted assumptions fail. |
| COUNTEREXAMPLE_CANDIDATE | The experiment may contradict a claimed toy behavior and requires inspection. |
| SENSITIVITY_CHECK | The experiment varies toy parameters/topology to test stability. |
| ROBUSTNESS_CHECK | The experiment repeats or perturbs previous toy setups. |
| IRRELEVANT_OR_UNUSABLE | The experiment cannot be mapped to a clear claim. |

## Minimum fields per experiment

| Field | Required |
|---|---|
| experiment_id | yes |
| script_or_artifact | yes |
| synthetic_or_real | yes, must be synthetic/toy only |
| linked_claim | yes |
| evidence_bucket | yes |
| assumptions_matched | yes |
| result_summary | yes |
| supports_or_weakens | yes |
| usable_for_report | yes |
| notes | optional |

## Initial status

The 400 experiments are not yet counted as evidence for the theory.

They become useful only after classification against this register.

## Current proved anchor

TTP-VF-H2-004-R is the current proved anchor.

Statement:
In the finite coordinatewise safe abstract toy domain,
if RSW-VF-H2-001 through RSW-VF-H2-007 hold,
then ledger_effect_size > 0.

Preserved lemmas:
- RSWL-VF-H2-001
- RSWL-VF-H2-002
- RSWL-VF-H2-003
- RSWL-VF-H2-004

## Explicit boundaries

Still not proved:
- original unrestricted TTP-VF-H2-004
- generalized ordered-domain theorem
- full Viruse Fabric theory
- VF-H2 empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Next allowed action

classify_vf_h2_existing_experiments_against_claim_ladder_no_claim_validation

VF_H2_CLAIM_LADDER_EVIDENCE_REGISTER_CREATED_OK
VF_H2_PROVED_ANCHOR_TTP_004_R_PRESERVED_OK
VF_H2_EXPERIMENTS_NOT_ASSUMED_VALID_UNTIL_CLASSIFIED_OK
VF_H2_FULL_THEORY_REMAINS_NOT_PROVED_OK
VF_H2_EMPIRICAL_VALIDATION_REMAINS_FALSE_OK
NEXT_ALLOWED_CLASSIFY_EXISTING_EXPERIMENTS_AGAINST_CLAIM_LADDER_OK
