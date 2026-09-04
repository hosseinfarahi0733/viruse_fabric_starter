from __future__ import annotations

import ast
import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from itertools import combinations
from pathlib import Path

from vfh2_c139.cli import render_report_bytes
from vfh2_c139.core import (
    ALGORITHM,
    BASE_COMMIT,
    MANIFEST_SCHEMA,
    REPORT_SCHEMA,
    audit_manifest,
    canonical_json_bytes,
    load_manifest_bytes,
    validate_manifest,
)


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
C139 = ROOT / "c139"
MANIFEST = C139 / "c139_immport_metadata_audit_manifest.v1.json"
REPORT = C139 / "c139_immport_metadata_audit_report.v1.json"
CHECKSUMS = C139 / "SHA256SUMS"


def _manifest() -> dict[str, object]:
    return json.loads(MANIFEST.read_text(encoding="ascii"))


def _cohort(manifest: dict[str, object], cohort_id: str) -> dict[str, object]:
    return next(
        cohort
        for cohort in manifest["cohorts"]
        if cohort["cohort_id"] == cohort_id
    )


def _make_all_metadata_confirmed(
    manifest: dict[str, object],
) -> dict[str, object]:
    result = copy.deepcopy(manifest)
    institutions = ("site-a", "site-b", "site-c")
    for index, cohort in enumerate(result["cohorts"]):
        cohort["complete_subject_upper_bound"] = {
            "count": 60,
            "source_ids": ["immune-signatures-resource"],
            "status": "CONFIRMED",
        }
        cohort["same_subject_complete_count"] = {
            "count": 60,
            "source_ids": ["immune-signatures-resource"],
            "status": "CONFIRMED",
        }
        cohort["recruitment_institution"] = {
            "source_ids": ["immune-signatures-resource"],
            "status": "CONFIRMED",
            "value": institutions[index % len(institutions)],
        }
        for evidence in cohort["criteria"].values():
            evidence["status"] = "CONFIRMED_TRUE"
    cohort_ids = sorted(cohort["cohort_id"] for cohort in result["cohorts"])
    result["overlap_evidence"] = [
        {
            "left_cohort_id": left,
            "right_cohort_id": right,
            "shared_subject_count": None,
            "source_ids": ["immune-signatures-resource"],
            "status": "CONFIRMED_DISJOINT",
        }
        for left, right in combinations(cohort_ids, 2)
    ]
    validate_manifest(result)
    return result


def _strategy(report: dict[str, object], replication_id: str) -> dict[str, object]:
    return next(
        strategy
        for strategy in report["confirmed_gate"]["strategies"]
        if strategy["replication_cohort_id"] == replication_id
    )


class MetadataAuditTests(unittest.TestCase):
    def test_frozen_manifest_and_report_contract(self) -> None:
        raw = MANIFEST.read_bytes()
        manifest = load_manifest_bytes(raw)
        report = audit_manifest(manifest, manifest_bytes=raw)
        self.assertEqual(manifest["schema"], MANIFEST_SCHEMA)
        self.assertEqual(manifest["base_commit"], BASE_COMMIT)
        self.assertEqual(report["schema"], REPORT_SCHEMA)
        self.assertEqual(report["algorithm"], ALGORITHM)
        self.assertEqual(
            report["manifest_sha256"], hashlib.sha256(raw).hexdigest()
        )
        self.assertEqual(report["final_gate"]["status"], "INSUFFICIENT_EVIDENCE")
        self.assertFalse(report["final_gate"]["fitting_authorized"])
        self.assertFalse(report["final_gate"]["thresholds_lowered"])

    def test_frozen_classification_and_capacity_are_hand_checked(self) -> None:
        bounds = {
            cohort["study_accession"]: cohort["complete_subject_upper_bound"]["count"]
            for cohort in _manifest()["cohorts"]
        }
        self.assertEqual(
            bounds,
            {"SDY180": 12, "SDY269": 28, "SDY270": 27, "SDY400": 31,
             "SDY404": 39, "SDY520": 23, "SDY640": 19, "SDY1119": 34,
             "SDY56": 52},
        )
        report = audit_manifest(_manifest())
        records = {
            record["cohort_id"]: record["classification"]
            for record in report["cohort_audit"]["records"]
        }
        self.assertEqual(
            records,
            {
                "SDY1119_TIV_2011": "UNRESOLVED",
                "SDY180_FLUZONE_2009_2010": "EXCLUDED",
                "SDY269_TIV_2008": "UNRESOLVED",
                "SDY270_TIV_2009": "UNRESOLVED",
                "SDY400_TIV_2012": "UNRESOLVED",
                "SDY404_TIV_2011": "UNRESOLVED",
                "SDY520_TIV_2013": "EXCLUDED",
                "SDY56_TIV_2010": "UNRESOLVED",
                "SDY640_TIV_2014": "EXCLUDED",
            },
        )
        optimistic = {
            item["replication_cohort_id"]: item
            for item in report["optimistic_capacity_audit"]["strategies"]
        }
        self.assertEqual(
            optimistic["SDY1119_TIV_2011"]["discovery_complete_subject_upper_bound"],
            177,
        )
        self.assertEqual(
            optimistic["SDY180_FLUZONE_2009_2010"]["discovery_complete_subject_upper_bound"],
            211,
        )
        self.assertTrue(
            optimistic["SDY1119_TIV_2011"]["replication_threshold_impossible"]
        )
        self.assertTrue(
            optimistic["SDY180_FLUZONE_2009_2010"]["replication_threshold_impossible"]
        )
        self.assertTrue(
            all(item["discovery_upper_bound_complete"] for item in optimistic.values())
        )

    def test_unknown_size_never_becomes_a_numeric_optimistic_upper_bound(self) -> None:
        manifest = _manifest()
        evidence = _cohort(manifest, "SDY56_TIV_2010")[
            "complete_subject_upper_bound"
        ]
        evidence["status"] = "UNRESOLVED"
        evidence["count"] = None
        report = audit_manifest(manifest)
        preferred = next(
            item
            for item in report["optimistic_capacity_audit"]["strategies"]
            if item["replication_cohort_id"] == "SDY1119_TIV_2011"
        )
        self.assertFalse(preferred["discovery_upper_bound_complete"])
        self.assertIsNone(preferred["discovery_complete_subject_upper_bound"])
        self.assertIn(
            "SDY56_TIV_2010",
            preferred["missing_discovery_upper_bound_cohort_ids"],
        )
        self.assertNotIn(
            "OPTIMISTIC_DISCOVERY_BOUND_BELOW_250",
            report["final_gate"]["reason_codes"],
        )

    def test_artifact_firewall_is_explicit_and_false_only(self) -> None:
        contract = _manifest()["artifact_contract"]
        self.assertEqual(contract["content_scope"], "PUBLIC_AGGREGATE_METADATA_ONLY")
        self.assertTrue(all(value is False for key, value in contract.items() if key != "content_scope"))
        mutated = _manifest()
        mutated["artifact_contract"]["outcome_measurements_in_artifact"] = True
        with self.assertRaises(ValueError):
            validate_manifest(mutated)

    def test_duplicate_json_keys_are_rejected_at_every_depth(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            load_manifest_bytes(b'{"schema":1,"schema":2}\n')
        raw = MANIFEST.read_bytes()
        needle = b'"content_scope": "PUBLIC_AGGREGATE_METADATA_ONLY"'
        replacement = needle + b',\n    "content_scope": "PUBLIC_AGGREGATE_METADATA_ONLY"'
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            load_manifest_bytes(raw.replace(needle, replacement, 1))

    def test_noncanonical_encodings_and_numbers_are_rejected(self) -> None:
        raw = MANIFEST.read_bytes()
        for bad in (b"\xef\xbb\xbf" + raw, raw.replace(b"\n", b"\r\n"), raw[:-1]):
            with self.assertRaises(ValueError):
                load_manifest_bytes(bad)
        for token in (b"NaN", b"Infinity", b"25.0"):
            with self.assertRaises(ValueError):
                load_manifest_bytes(b'{"x":' + token + b'}\n')
        noncanonical = raw.replace(b'  "audit_id"', b'    "audit_id"', 1)
        with self.assertRaisesRegex(ValueError, "not canonical"):
            load_manifest_bytes(noncanonical)

    def test_missing_unknown_and_outcome_fields_are_rejected(self) -> None:
        missing = _manifest()
        del missing["power_assessment"]
        with self.assertRaises(ValueError):
            validate_manifest(missing)
        unknown = _manifest()
        unknown["outcome_values"] = [1, 2, 3]
        with self.assertRaises(ValueError):
            validate_manifest(unknown)
        nested = _manifest()
        nested["cohorts"][0]["gene_expression"] = [1, 2]
        with self.assertRaises(ValueError):
            validate_manifest(nested)

    def test_builtin_types_are_required_without_bool_as_int(self) -> None:
        class DictSubclass(dict):
            pass

        class ListSubclass(list):
            pass

        with self.assertRaises(TypeError):
            validate_manifest(DictSubclass(_manifest()))
        mutated = _manifest()
        mutated["cohorts"] = ListSubclass(mutated["cohorts"])
        with self.assertRaises(TypeError):
            validate_manifest(mutated)
        mutated = _manifest()
        mutated["gate_contract"]["minimum_complete_subjects_per_cohort"] = True
        with self.assertRaises(TypeError):
            validate_manifest(mutated)
        with self.assertRaises(TypeError):
            load_manifest_bytes(bytearray(MANIFEST.read_bytes()))

    def test_bad_dates_accessions_urls_and_secret_material_are_rejected(self) -> None:
        bad_date = _manifest()
        bad_date["snapshot_date"] = "2026-19-39"
        with self.assertRaises(ValueError):
            validate_manifest(bad_date)
        bad_accession = _manifest()
        bad_accession["cohorts"][0]["study_accession"] = "../SDY180"
        with self.assertRaises(ValueError):
            validate_manifest(bad_accession)
        for url in (
            "http://www.immport.org/shared/search",
            "https://evil.example/data",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?" + "token" + "=secret",
            "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE29617&row=1",
            "https://www.immport.org/data/../private",
            "https://user@example.com/data",
        ):
            mutated = _manifest()
            mutated["sources"][0]["url"] = url
            with self.assertRaises(ValueError):
                validate_manifest(mutated)

    def test_source_dates_and_exact_accession_sources_are_enforced(self) -> None:
        future_source = _manifest()
        future_source["sources"][0]["retrieved_on"] = "2026-09-05"
        with self.assertRaises(ValueError):
            validate_manifest(future_source)
        backdated_source = _manifest()
        backdated_source["sources"][0]["retrieved_on"] = "2026-09-02"
        with self.assertRaises(ValueError):
            validate_manifest(backdated_source)

        wrong_design = _manifest()
        source = next(
            item
            for item in wrong_design["sources"]
            if item["source_id"] == "immport-design-sdy180"
        )
        source["url"] = "https://www.immport.org/data/query/ui/study/design/SDY181"
        with self.assertRaises(ValueError):
            validate_manifest(wrong_design)

        for replacement in (
            "https://pmc.ncbi.nlm.nih.gov/study/design/SDY180",
            "https://docs.immport.org/study/design/SDY180",
        ):
            wrong_origin = _manifest()
            source = next(
                item
                for item in wrong_origin["sources"]
                if item["source_id"] == "immport-design-sdy180"
            )
            source["url"] = replacement
            with self.assertRaises(ValueError):
                validate_manifest(wrong_origin)

        wrong_kind = _manifest()
        source = next(
            item
            for item in wrong_kind["sources"]
            if item["source_id"] == "immport-design-sdy180"
        )
        source["kind"] = "IMMPORT_PUBLIC_DOCUMENTATION"
        source["provenance_status"] = "NOT_APPLICABLE"
        source["release_labels"] = []
        with self.assertRaises(ValueError):
            validate_manifest(wrong_kind)

        wrong_geo = _manifest()
        source = next(
            item
            for item in wrong_geo["sources"]
            if item["source_id"] == "geo-gse29617"
        )
        source["release_labels"] = ["GSE99999"]
        source["url"] = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99999"
        with self.assertRaises(ValueError):
            validate_manifest(wrong_geo)

        wrong_mapping = _manifest()
        _cohort(wrong_mapping, "SDY269_TIV_2008")["geo_series"] = ["GSE74816"]
        with self.assertRaises(ValueError):
            validate_manifest(wrong_mapping)

        swapped_mapping = _manifest()
        sdy180 = _cohort(swapped_mapping, "SDY180_FLUZONE_2009_2010")
        sdy269 = _cohort(swapped_mapping, "SDY269_TIV_2008")
        sdy180["geo_series"], sdy269["geo_series"] = (
            sdy269["geo_series"],
            sdy180["geo_series"],
        )
        with self.assertRaises(ValueError):
            validate_manifest(swapped_mapping)

    def test_source_provenance_cardinality_is_exact(self) -> None:
        conflicting = _manifest()
        conflicting["sources"][0]["release_labels"] = ["DR58"]
        with self.assertRaises(ValueError):
            validate_manifest(conflicting)

        not_applicable = _manifest()
        not_applicable["sources"][1]["release_labels"] = ["DR58"]
        with self.assertRaises(ValueError):
            validate_manifest(not_applicable)

        consistent = _manifest()
        consistent["sources"][3]["release_labels"] = []
        with self.assertRaises(ValueError):
            validate_manifest(consistent)

    def test_recursive_artifact_firewall_rejects_sensitive_strings(self) -> None:
        mutations = []

        arm_identifier = _manifest()
        arm_identifier["cohorts"][0]["arm_label"] = (
            "participant_id SUB" + "12345 HAI=640"
        )
        mutations.append(arm_identifier)

        outcome_value = _manifest()
        outcome_value["cohorts"][0]["season"] = "2010-2011; HAI outcome=640"
        mutations.append(outcome_value)

        repository_identifier = _manifest()
        repository_identifier["cohorts"][0]["arm_label"] = "GSM" + "123"
        mutations.append(repository_identifier)

        sample_identifier = _manifest()
        sample_identifier["cohorts"][0]["arm_label"] = "SMP" + "123456"
        mutations.append(sample_identifier)

        patient_identifier = _manifest()
        patient_identifier["cohorts"][0]["arm_label"] = (
            "patient_id P" + "0001"
        )
        mutations.append(patient_identifier)

        donor_identifier = _manifest()
        donor_identifier["cohorts"][0]["arm_label"] = "donor_id D12345"
        mutations.append(donor_identifier)

        bracketed_measurement = _manifest()
        bracketed_measurement["cohorts"][0]["arm_label"] = "HAI values [640]"
        mutations.append(bracketed_measurement)

        reversed_measurement = _manifest()
        reversed_measurement["cohorts"][0]["arm_label"] = "640 HAI titer"
        mutations.append(reversed_measurement)

        encoded_blob = _manifest()
        encoded_blob["cohorts"][0]["arm_label"] = "prefix-" + "A" * 160
        mutations.append(encoded_blob)

        encoded_urlsafe_blob = _manifest()
        encoded_urlsafe_blob["cohorts"][0]["arm_label"] = "A_" * 80
        mutations.append(encoded_urlsafe_blob)

        credential_case = _manifest()
        credential_case["cohorts"][0]["arm_label"] = "token" + "=private-value"
        mutations.append(credential_case)

        cloud_key = _manifest()
        cloud_key["cohorts"][0]["arm_label"] = (
            "aws_access_" + "key_id=private-value"
        )
        mutations.append(cloud_key)

        access_key = _manifest()
        access_key["cohorts"][0]["arm_label"] = "AKIA" + "A" * 16
        mutations.append(access_key)

        api_key_case = _manifest()
        api_key_case["cohorts"][0]["arm_label"] = "sk" + "-proj-" + "A" * 20
        mutations.append(api_key_case)

        jwt = _manifest()
        jwt["cohorts"][0]["arm_label"] = (
            "eyJ" + "A" * 10 + "." + "B" * 10 + "." + "C" * 10
        )
        mutations.append(jwt)

        bearer_case = _manifest()
        bearer_case["cohorts"][0]["arm_label"] = "Bearer" + " " + "private-value"
        mutations.append(bearer_case)

        signature_case = _manifest()
        signature_case["cohorts"][0]["arm_label"] = "signature" + "=private-value"
        mutations.append(signature_case)

        for mutation in mutations:
            with self.subTest(mutation=mutation):
                with self.assertRaises(ValueError):
                    validate_manifest(mutation)

    def test_recruitment_institution_is_a_canonical_slug(self) -> None:
        for value in ("Yale", "yale ", "yale_university"):
            mutated = _make_all_metadata_confirmed(_manifest())
            mutated["cohorts"][0]["recruitment_institution"]["value"] = value
            with self.assertRaises(ValueError):
                validate_manifest(mutated)

        accepted = _make_all_metadata_confirmed(_manifest())
        accepted["cohorts"][0]["recruitment_institution"]["value"] = (
            "yale-university"
        )
        validate_manifest(accepted)

    def test_duplicate_and_dangling_evidence_is_rejected(self) -> None:
        duplicate_source = _manifest()
        duplicate_source["sources"][1]["source_id"] = duplicate_source["sources"][0]["source_id"]
        with self.assertRaises(ValueError):
            validate_manifest(duplicate_source)
        dangling = _manifest()
        dangling["cohorts"][0]["criteria"]["human"]["source_ids"] = ["missing-source"]
        with self.assertRaises(ValueError):
            validate_manifest(dangling)
        duplicate_cohort = _manifest()
        duplicate_cohort["cohorts"][1]["cohort_id"] = duplicate_cohort["cohorts"][0]["cohort_id"]
        with self.assertRaises(ValueError):
            validate_manifest(duplicate_cohort)

    def test_evidence_sources_cannot_cross_study_or_use_only_policy_docs(self) -> None:
        cross_study = _manifest()
        _cohort(cross_study, "SDY180_FLUZONE_2009_2010")[
            "complete_subject_upper_bound"
        ]["source_ids"] = ["immport-design-sdy269"]
        with self.assertRaises(ValueError):
            validate_manifest(cross_study)

        policy_for_count = _manifest()
        _cohort(policy_for_count, "SDY180_FLUZONE_2009_2010")[
            "complete_subject_upper_bound"
        ]["source_ids"] = ["immport-download-guide"]
        with self.assertRaises(ValueError):
            validate_manifest(policy_for_count)

        data_for_policy = _manifest()
        _cohort(data_for_policy, "SDY180_FLUZONE_2009_2010")["criteria"][
            "license_version_pinned"
        ]["source_ids"] = ["immune-signatures-resource"]
        with self.assertRaises(ValueError):
            validate_manifest(data_for_policy)

    def test_counts_are_consistent_and_bounded(self) -> None:
        excessive = _manifest()
        cohort = _cohort(excessive, "SDY270_TIV_2009")
        cohort["same_subject_complete_count"] = {
            "count": 28,
            "source_ids": ["geo-gse74811"],
            "status": "CONFIRMED",
        }
        with self.assertRaises(ValueError):
            validate_manifest(excessive)
        unresolved_with_count = _manifest()
        _cohort(unresolved_with_count, "SDY270_TIV_2009")["same_subject_complete_count"]["count"] = 1
        with self.assertRaises(ValueError):
            validate_manifest(unresolved_with_count)

    def test_confirmed_overlap_count_cannot_exceed_either_cohort(self) -> None:
        mutated = _manifest()
        record = mutated["overlap_evidence"][0]
        record["status"] = "CONFIRMED_OVERLAP"
        record["shared_subject_count"] = min(
            _cohort(mutated, record[key])["complete_subject_upper_bound"]["count"]
            for key in ("left_cohort_id", "right_cohort_id")
        ) + 1
        with self.assertRaises(ValueError):
            validate_manifest(mutated)

    def test_unknown_evidence_never_becomes_eligible(self) -> None:
        manifest = _manifest()
        cohort = _cohort(manifest, "SDY270_TIV_2009")
        cohort["same_subject_complete_count"] = {
            "count": 27,
            "source_ids": ["geo-gse74811"],
            "status": "CONFIRMED",
        }
        report = audit_manifest(manifest)
        record = next(
            item for item in report["cohort_audit"]["records"]
            if item["cohort_id"] == "SDY270_TIV_2009"
        )
        self.assertEqual(record["classification"], "UNRESOLVED")

    def test_cohort_size_boundary_is_exactly_25(self) -> None:
        manifest = _make_all_metadata_confirmed(_manifest())
        cohort = _cohort(manifest, "SDY270_TIV_2009")
        for value, expected in ((24, "EXCLUDED"), (25, "ELIGIBLE")):
            cohort["complete_subject_upper_bound"]["count"] = value
            cohort["same_subject_complete_count"]["count"] = value
            record = next(
                item for item in audit_manifest(manifest)["cohort_audit"]["records"]
                if item["cohort_id"] == cohort["cohort_id"]
            )
            self.assertEqual(record["classification"], expected)

    def test_metadata_capacity_cannot_authorize_fitting_without_power(self) -> None:
        report = audit_manifest(_make_all_metadata_confirmed(_manifest()))
        strategy = report["confirmed_gate"]["strategies"][0]
        self.assertTrue(strategy["metadata_capacity_passes"])
        self.assertFalse(strategy["checks"]["power"])
        self.assertFalse(strategy["passes"])
        self.assertEqual(report["final_gate"]["status"], "INSUFFICIENT_EVIDENCE")
        self.assertFalse(report["final_gate"]["fitting_authorized"])

    def test_power_is_unevaluated_and_non_authorizing_in_v1(self) -> None:
        for status, value in (("CONFIRMED", 8000), ("NOT_EVALUATED", 8000)):
            mutated = _manifest()
            mutated["power_assessment"] = {
                "estimated_power_basis_points": value,
                "status": status,
            }
            with self.assertRaises(ValueError):
                validate_manifest(mutated)

    def test_replication_boundary_is_49_then_50(self) -> None:
        manifest = _make_all_metadata_confirmed(_manifest())
        cohort = _cohort(manifest, "SDY1119_TIV_2011")
        for value, expected in ((49, False), (50, True)):
            cohort["complete_subject_upper_bound"]["count"] = value
            cohort["same_subject_complete_count"]["count"] = value
            report = audit_manifest(manifest)
            strategy = _strategy(report, "SDY1119_TIV_2011")
            self.assertEqual(strategy["checks"]["replication_complete_subjects"], expected)

    def test_discovery_total_boundary_is_249_then_250(self) -> None:
        manifest = _make_all_metadata_confirmed(_manifest())
        discovery_ids = [
            "SDY180_FLUZONE_2009_2010",
            "SDY269_TIV_2008",
            "SDY270_TIV_2009",
            "SDY400_TIV_2012",
            "SDY404_TIV_2011",
        ]
        for cohort in manifest["cohorts"]:
            if cohort["cohort_id"] not in discovery_ids and cohort["cohort_id"] != "SDY1119_TIV_2011":
                cohort["complete_subject_upper_bound"]["count"] = 24
                cohort["same_subject_complete_count"]["count"] = 24
        for total, expected in ((249, False), (250, True)):
            values = [49, 50, 50, 50, total - 199]
            for cohort_id, value in zip(discovery_ids, values):
                cohort = _cohort(manifest, cohort_id)
                cohort["complete_subject_upper_bound"]["count"] = value
                cohort["same_subject_complete_count"]["count"] = value
            strategy = _strategy(audit_manifest(manifest), "SDY1119_TIV_2011")
            self.assertEqual(strategy["confirmed_discovery_complete_subjects"], total)
            self.assertEqual(strategy["checks"]["discovery_complete_subjects"], expected)

    def test_institution_boundary_is_two_then_three(self) -> None:
        manifest = _make_all_metadata_confirmed(_manifest())
        for count, expected in ((2, False), (3, True)):
            for index, cohort in enumerate(manifest["cohorts"]):
                cohort["recruitment_institution"]["value"] = f"site-{index % count}"
            strategy = _strategy(audit_manifest(manifest), "SDY1119_TIV_2011")
            self.assertEqual(strategy["checks"]["discovery_institutions"], expected)

    def test_missing_or_unknown_overlap_never_counts_as_disjoint(self) -> None:
        manifest = _make_all_metadata_confirmed(_manifest())
        manifest["overlap_evidence"] = [
            record
            for record in manifest["overlap_evidence"]
            if "SDY1119_TIV_2011"
            not in (record["left_cohort_id"], record["right_cohort_id"])
        ]
        strategy = _strategy(audit_manifest(manifest), "SDY1119_TIV_2011")
        self.assertFalse(strategy["checks"]["pairwise_disjoint"])
        manifest = _make_all_metadata_confirmed(_manifest())
        for record in manifest["overlap_evidence"]:
            if "SDY1119_TIV_2011" in (
                record["left_cohort_id"],
                record["right_cohort_id"],
            ):
                record["status"] = "UNRESOLVED"
        strategy = _strategy(audit_manifest(manifest), "SDY1119_TIV_2011")
        self.assertFalse(strategy["checks"]["pairwise_disjoint"])

    def test_valid_discovery_subset_excludes_an_overlapping_surplus_cohort(self) -> None:
        manifest = _make_all_metadata_confirmed(_manifest())
        overlap = next(
            record
            for record in manifest["overlap_evidence"]
            if record["left_cohort_id"] == "SDY1119_TIV_2011"
            and record["right_cohort_id"] == "SDY180_FLUZONE_2009_2010"
        )
        overlap["status"] = "CONFIRMED_OVERLAP"
        overlap["shared_subject_count"] = 1
        report = audit_manifest(manifest)
        strategy = _strategy(report, "SDY1119_TIV_2011")
        self.assertTrue(strategy["metadata_capacity_passes"])
        self.assertNotIn(
            "SDY180_FLUZONE_2009_2010",
            strategy["confirmed_discovery_cohort_ids"],
        )
        self.assertEqual(len(strategy["confirmed_discovery_cohort_ids"]), 5)
        self.assertFalse(strategy["passes"])

    def test_visit_windows_fix_target_and_tie_break(self) -> None:
        windows = _manifest()["gate_contract"]["windows"]
        self.assertEqual(
            windows,
            {
                "baseline": {
                    "allowed_day_range": [0, 0],
                    "target_day": 0,
                    "tie_break": "EARLIER_DAY_THEN_ACCESSION",
                },
                "early": {
                    "allowed_day_range": [1, 3],
                    "target_day": 1,
                    "tie_break": "EARLIER_DAY_THEN_ACCESSION",
                },
                "middle": {
                    "allowed_day_range": [5, 9],
                    "target_day": 7,
                    "tie_break": "EARLIER_DAY_THEN_ACCESSION",
                },
                "outcome": {
                    "allowed_day_range": [28, 35],
                    "target_day": 28,
                    "tie_break": "EARLIER_DAY_THEN_ACCESSION",
                },
            },
        )
        for field, value in (
            ("target_day", 2),
            ("tie_break", "LATER_DAY"),
            ("allowed_day_range", [1, 4]),
        ):
            mutated = _manifest()
            mutated["gate_contract"]["windows"]["early"][field] = value
            with self.assertRaises(ValueError):
                validate_manifest(mutated)
    def test_thresholds_and_candidate_inventory_cannot_drift(self) -> None:
        for key, value in (
            ("minimum_complete_subjects_per_cohort", 24),
            ("minimum_discovery_complete_subjects", 249),
            ("minimum_replication_complete_subjects", 49),
            ("minimum_simulated_power_basis_points", 7999),
        ):
            mutated = _manifest()
            mutated["gate_contract"][key] = value
            with self.assertRaises(ValueError):
                validate_manifest(mutated)
        mutated = _manifest()
        mutated["cohorts"].reverse()
        with self.assertRaises(ValueError):
            validate_manifest(mutated)
        mutated = _manifest()
        mutated["sources"].reverse()
        with self.assertRaises(ValueError):
            validate_manifest(mutated)
        mutated = _manifest()
        mutated["audit_id"] = "VFH2-C139-CHANGED"
        with self.assertRaises(ValueError):
            validate_manifest(mutated)

    def test_manifest_mutation_changes_digest_and_derived_result(self) -> None:
        original = _manifest()
        mutated = copy.deepcopy(original)
        _cohort(mutated, "SDY180_FLUZONE_2009_2010")["complete_subject_upper_bound"]["count"] = 13
        original_report = audit_manifest(original)
        mutated_report = audit_manifest(mutated)
        self.assertNotEqual(original_report["manifest_sha256"], mutated_report["manifest_sha256"])
        original_record = original_report["cohort_audit"]["records"][0]
        mutated_record = mutated_report["cohort_audit"]["records"][0]
        self.assertNotEqual(
            original_record["complete_subject_upper_bound"],
            mutated_record["complete_subject_upper_bound"],
        )

    def test_frozen_report_and_cli_are_byte_stable(self) -> None:
        expected = REPORT.read_bytes()
        self.assertEqual(render_report_bytes(MANIFEST), expected)
        base_env = {
            **os.environ,
            "PYTHONPATH": str(ROOT / "src"),
            "PYTHONDONTWRITEBYTECODE": "1",
        }
        outputs = []
        for seed, timezone in (("1", "UTC"), ("8675309", "Pacific/Honolulu")):
            env = {**base_env, "PYTHONHASHSEED": seed, "TZ": timezone, "LC_ALL": "C"}
            outputs.append(
                subprocess.run(
                    [sys.executable, "-m", "vfh2_c139", "--manifest", str(MANIFEST)],
                    cwd=REPO,
                    env=env,
                    check=True,
                    capture_output=True,
                ).stdout
            )
        self.assertEqual(outputs, [expected, expected])
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.json"
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "vfh2_c139",
                    "--manifest",
                    str(MANIFEST),
                    "--output",
                    str(output),
                ],
                cwd=REPO,
                env=base_env,
                check=True,
                capture_output=True,
            )
            self.assertEqual(output.read_bytes(), expected)

    def test_core_and_cli_have_no_network_ml_or_fixture_dependency(self) -> None:
        banned = {
            "aiohttp",
            "boto3",
            "ftplib",
            "http",
            "httpx",
            "joblib",
            "numpy",
            "os",
            "pandas",
            "paramiko",
            "pickle",
            "requests",
            "scipy",
            "sklearn",
            "socket",
            "sqlite3",
            "subprocess",
            "tensorflow",
            "torch",
            "urllib",
        }
        for relative in ("core.py", "cli.py"):
            path = ROOT / "src" / "vfh2_c139" / relative
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("c139_immport_metadata_audit_report", text)
            tree = ast.parse(text)
            imports = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split(".")[0])
            self.assertFalse(imports & banned)

    def test_checksum_inventory_is_exact_and_valid(self) -> None:
        expected_paths = sorted(
            [
                "reference/python/c139/README.md",
                "reference/python/c139/c139_immport_metadata_audit_manifest.v1.json",
                "reference/python/c139/c139_immport_metadata_audit_report.v1.json",
                "reference/python/src/vfh2_c139/__init__.py",
                "reference/python/src/vfh2_c139/__main__.py",
                "reference/python/src/vfh2_c139/cli.py",
                "reference/python/src/vfh2_c139/core.py",
                "reference/python/tests/test_c139_immport_metadata_audit.py",
                "scripts/verify_c139.sh",
            ]
        )
        lines = CHECKSUMS.read_text(encoding="ascii").splitlines()
        actual_paths = [line.split("  ", 1)[1] for line in lines]
        self.assertEqual(actual_paths, expected_paths)
        for line in lines:
            digest, relative = line.split("  ", 1)
            self.assertEqual(len(digest), 64)
            self.assertEqual(
                hashlib.sha256((REPO / relative).read_bytes()).hexdigest(), digest
            )


if __name__ == "__main__":
    unittest.main()
