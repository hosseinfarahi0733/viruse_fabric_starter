from __future__ import annotations

import hashlib
import json
import re
from datetime import date
from itertools import combinations
from typing import Any


MANIFEST_SCHEMA = "vfh2.c139.immport-metadata-audit-manifest.v1"
REPORT_SCHEMA = "vfh2.c139.immport-metadata-audit-report.v1"
ALGORITHM = "vfh2.c139.immport-metadata-audit.v1"
BASE_COMMIT = "3a107eb735bee8fc142f9b981e207aca506692ea"
_AUDIT_ID = "VFH2-C139-IMMPORT-PUBLIC-METADATA-2026-09-04"
_SNAPSHOT_DATE = "2026-09-04"

_EXPECTED_COHORT_IDS = (
    "SDY180_FLUZONE_2009_2010",
    "SDY269_TIV_2008",
    "SDY270_TIV_2009",
    "SDY400_TIV_2012",
    "SDY404_TIV_2011",
    "SDY520_TIV_2013",
    "SDY640_TIV_2014",
    "SDY1119_TIV_2011",
    "SDY56_TIV_2010",
)
_EXPECTED_COHORT_GEO = {
    "SDY180_FLUZONE_2009_2010": ("GSE48762",),
    "SDY269_TIV_2008": ("GSE29617",),
    "SDY270_TIV_2009": ("GSE74811",),
    "SDY400_TIV_2012": ("GSE59743",),
    "SDY404_TIV_2011": ("GSE59654",),
    "SDY520_TIV_2013": ("GSE101709",),
    "SDY640_TIV_2014": ("GSE101710",),
    "SDY1119_TIV_2011": ("GSE74816",),
    "SDY56_TIV_2010": ("GSE74813", "GSE74817"),
}
_REPLICATION_PRIORITY = (
    "SDY1119_TIV_2011",
    "SDY180_FLUZONE_2009_2010",
)
_EXPECTED_SOURCE_IDS = (
    "immport-search-metadata",
    "immport-download-guide",
    "immport-dmsp-guide",
    "immune-signatures-resource",
    "immport-design-sdy180",
    "immport-design-sdy269",
    "immport-design-sdy270",
    "immport-design-sdy400",
    "immport-design-sdy404",
    "immport-design-sdy520",
    "immport-design-sdy56",
    "immport-design-sdy640",
    "immport-design-sdy1119",
    "geo-gse48762",
    "geo-gse29617",
    "geo-gse74811",
    "geo-gse59743",
    "geo-gse59654",
    "geo-gse101709",
    "geo-gse101710",
    "geo-gse74816",
    "geo-gse74813",
    "geo-gse74817",
)
_STATIC_SOURCE_CONTRACTS = {
    "immport-search-metadata": (
        "IMMPORT_PUBLIC_METADATA",
        "CONFLICTING_LABELS",
        ["DR58", "study_mapping_common_dr67"],
        "https://www.immport.org/shared/search",
    ),
    "immport-download-guide": (
        "IMMPORT_PUBLIC_DOCUMENTATION",
        "NOT_APPLICABLE",
        [],
        "https://docs.immport.org/download/",
    ),
    "immport-dmsp-guide": (
        "IMMPORT_PUBLIC_DOCUMENTATION",
        "NOT_APPLICABLE",
        [],
        "https://docs.immport.org/documents/dmsp/"
        "ImmPort_Data_Management_and_Sharing_Plan_Template_v1.pdf",
    ),
    "immune-signatures-resource": (
        "PEER_REVIEWED_AGGREGATE_PUBLICATION",
        "CONSISTENT",
        ["PMC9584267"],
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC9584267/",
    ),
}
_GEO_SOURCE_LABELS = {
    "GSE48762": ["GSE48762"],
    "GSE29617": ["GSE29617"],
    "GSE74811": ["GSE74811", "PMC9584267-table-2-mapping"],
    "GSE59743": ["GSE59743"],
    "GSE59654": ["GSE59654"],
    "GSE101709": ["GSE101709", "PMC9584267-specimen-label"],
    "GSE101710": ["GSE101710", "PMC9584267-specimen-label"],
    "GSE74816": ["GSE74816"],
    "GSE74813": ["GSE74813", "GSE74817-superseries"],
    "GSE74817": ["GSE74817", "multi-season-superseries"],
}
_REQUIRED_CRITERIA = (
    "comparable_hai",
    "hai_d28_35",
    "human",
    "injectable_influenza_arm",
    "license_version_pinned",
    "platform_provenance_clear",
    "pooling_unambiguous",
    "public_deidentified_data_under_declared_terms",
    "same_subject_linkage",
    "subject_mapping_clear",
    "transcriptomics_d0",
    "transcriptomics_d1_3",
    "transcriptomics_d5_9",
    "whole_blood_or_pbmc",
)
_BOOL_EVIDENCE_STATES = {
    "CONFIRMED_FALSE",
    "CONFIRMED_TRUE",
    "UNRESOLVED",
}
_TEXT_EVIDENCE_STATES = {"CONFIRMED", "UNRESOLVED"}
_COUNT_EVIDENCE_STATES = {"CONFIRMED", "UNRESOLVED"}
_SOURCE_KINDS = {
    "IMMPORT_PUBLIC_DOCUMENTATION",
    "IMMPORT_PUBLIC_METADATA",
    "PEER_REVIEWED_AGGREGATE_PUBLICATION",
    "PUBLIC_REPOSITORY_METADATA",
}
_PROVENANCE_STATES = {
    "CONSISTENT",
    "CONFLICTING_LABELS",
    "NOT_APPLICABLE",
}
_EVIDENCE_FLAGS = {
    "ARM_FILTER_REQUIRED",
    "PUBLICATION_GEO_VS_IMMPORT_COUNT_DIFFERENCE",
    "GEO_MAPPING_CONFLICT",
    "MIXED_VACCINE_MODALITIES",
    "PLANNED_VISIT_RANGE_CROSSES_WINDOW",
    "SPECIMEN_LABEL_CONFLICT",
    "STUDY_LEVEL_OVERLAP_REPORTED",
    "SUPER_SERIES_COLLISION_RISK",
}
_ALLOWED_HOSTS = {
    "docs.immport.org",
    "pmc.ncbi.nlm.nih.gov",
    "www.immport.org",
    "www.ncbi.nlm.nih.gov",
}
_URL_RE = re.compile(r"^https://([^/?#]+)(/[^#\s]*)?$")
_DATE_RE = re.compile(r"^20[0-9]{2}-[01][0-9]-[0-3][0-9]$")
_ACCESSION_RE = re.compile(r"^SDY[1-9][0-9]*$")
_COHORT_ID_RE = re.compile(r"^SDY[1-9][0-9]*_[A-Z0-9_]+$")
_SOURCE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,79}$")
_GEO_RE = re.compile(r"^GSE[1-9][0-9]*$")
_HEX40_RE = re.compile(r"^[0-9a-f]{40}$")
_CREDENTIAL_RE = re.compile(
    r"(?i)(?:authorization\s*[:=]\s*bearer|"
    r"bearer\s+[A-Za-z0-9._~+/=-]+|"
    r"(?:api[_-]?key|aws[_-]?access[_-]?key[_-]?id|credential|password|"
    r"secret|signature|token|x-amz-[a-z0-9-]+)\s*[:=]|"
    r"begin\s+(?:rsa\s+|ec\s+|openssh\s+)?private\s+key)"
)
_IDENTIFIER_RE = re.compile(
    r"(?i)\b(?:SUB|GSM|SMP)[0-9]+\b|"
    r"\b(?:donor|individual|participant|patient|sample|subject)"
    r"[_ -]?(?:id|identifier)\b|"
    r"\bP[0-9]{4,}\b"
)
_MEASUREMENT_VALUE_RE = re.compile(
    r"(?i)(?:hai|outcome|titer|titre|measurement)[a-z_ -]{0,24}"
    r"(?:=|:|\s|\[)\s*\[?\s*[-+]?[0-9]"
)
_VALUE_BEFORE_MEASUREMENT_RE = re.compile(
    r"(?i)[-+]?[0-9]+(?:\.[0-9]+)?\s*"
    r"(?:hai|outcome|titer|titre|measurement)\b"
)
_INSTITUTION_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_BASE64_BLOB_RE = re.compile(r"[A-Za-z0-9+/]{160,}={0,2}")
_BASE64URL_BLOB_RE = re.compile(r"[A-Za-z0-9_-]{160,}={0,2}")
_JWT_RE = re.compile(
    r"eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}"
)
_CLOUD_KEY_RE = re.compile(
    r"(?:AKIA[0-9A-Z]{16}|(?:ghp_|github_pat_|sk-(?:proj-)?)[A-Za-z0-9_-]{12,})"
)


def canonical_json_bytes(value: object) -> bytes:
    """Render the exact ASCII JSON representation used by C139."""

    rendered = json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        indent=2,
        sort_keys=True,
    )
    return (rendered + "\n").encode("ascii")


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number is forbidden: {value}")


def _reject_float(value: str) -> None:
    raise ValueError(f"floating-point JSON number is forbidden: {value}")


def _object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_manifest_bytes(raw: bytes) -> dict[str, object]:
    """Parse and validate one canonical C139 manifest byte string."""

    if type(raw) is not bytes:
        raise TypeError("manifest input must be built-in bytes")
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("UTF-8 BOM is forbidden")
    if b"\r" in raw:
        raise ValueError("CR characters are forbidden")
    if not raw.endswith(b"\n"):
        raise ValueError("manifest must end with one LF")
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise ValueError("manifest must be ASCII JSON") from error
    value = json.loads(
        text,
        object_pairs_hook=_object_pairs,
        parse_constant=_reject_constant,
        parse_float=_reject_float,
    )
    validate_manifest(value)
    if canonical_json_bytes(value) != raw:
        raise ValueError("manifest JSON is not canonical")
    return value


def _require_dict(
    value: object, expected_keys: set[str], label: str
) -> dict[str, object]:
    if type(value) is not dict:
        raise TypeError(f"{label} must be a built-in dict")
    actual_keys = set(value)
    if actual_keys != expected_keys:
        missing = sorted(expected_keys - actual_keys)
        unknown = sorted(actual_keys - expected_keys)
        raise ValueError(
            f"{label} key mismatch; missing={missing}, unknown={unknown}"
        )
    for key in value:
        if type(key) is not str:
            raise TypeError(f"{label} keys must be built-in str values")
    return value


def _require_list(
    value: object, label: str, *, maximum: int = 128
) -> list[object]:
    if type(value) is not list:
        raise TypeError(f"{label} must be a built-in list")
    if len(value) > maximum:
        raise ValueError(f"{label} contains too many entries")
    return value


def _require_str(
    value: object,
    label: str,
    *,
    maximum: int = 512,
    pattern: re.Pattern[str] | None = None,
) -> str:
    if type(value) is not str:
        raise TypeError(f"{label} must be a built-in str")
    if not value or len(value) > maximum or not value.isascii():
        raise ValueError(f"{label} must be nonempty bounded ASCII")
    if "\n" in value or "\r" in value or "\x00" in value:
        raise ValueError(f"{label} contains a forbidden control character")
    if pattern is not None and pattern.fullmatch(value) is None:
        raise ValueError(f"{label} has invalid syntax")
    return value


def _require_bool(value: object, label: str) -> bool:
    if type(value) is not bool:
        raise TypeError(f"{label} must be a built-in bool")
    return value


def _require_int(
    value: object, label: str, *, minimum: int = 0, maximum: int = 1_000_000
) -> int:
    if type(value) is not int:
        raise TypeError(f"{label} must be a built-in int")
    if value < minimum or value > maximum:
        raise ValueError(f"{label} is outside the permitted range")
    return value


def _require_string_list(
    value: object,
    label: str,
    *,
    maximum: int = 64,
    pattern: re.Pattern[str] | None = None,
) -> list[str]:
    raw = _require_list(value, label, maximum=maximum)
    checked = [
        _require_str(item, f"{label}[{index}]", pattern=pattern)
        for index, item in enumerate(raw)
    ]
    if len(set(checked)) != len(checked):
        raise ValueError(f"{label} contains duplicates")
    return checked


def _require_source_ids(
    value: object, label: str, known_sources: set[str]
) -> list[str]:
    checked = _require_string_list(value, label, pattern=_SOURCE_ID_RE)
    if not checked:
        raise ValueError(f"{label} must cite at least one source")
    dangling = sorted(set(checked) - known_sources)
    if dangling:
        raise ValueError(f"{label} has dangling source references: {dangling}")
    return checked


def _require_scoped_evidence_sources(
    evidence: dict[str, object], label: str, allowed: set[str]
) -> None:
    source_ids = evidence["source_ids"]
    assert type(source_ids) is list
    outside_scope = sorted(set(source_ids) - allowed)
    if outside_scope:
        raise ValueError(
            f"{label}.source_ids cite sources outside this evidence scope: "
            f"{outside_scope}"
        )


def _validate_url(value: object, label: str) -> str:
    url = _require_str(value, label, maximum=2048)
    match = _URL_RE.fullmatch(url)
    if match is None or match.group(1).lower() not in _ALLOWED_HOSTS:
        raise ValueError(f"{label} is not an approved HTTPS source URL")
    if "@" in match.group(1) or _CREDENTIAL_RE.search(url):
        raise ValueError(f"{label} contains credential-like material")
    if "#" in url or "\\" in url or "%" in url or "/../" in url or "/./" in url:
        raise ValueError(f"{label} contains a forbidden URL component")
    base, separator, query = url.partition("?")
    if separator:
        if not (
            match.group(1).lower() == "www.ncbi.nlm.nih.gov"
            and base == "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi"
            and re.fullmatch(r"acc=GSE[1-9][0-9]*", query) is not None
        ):
            raise ValueError(f"{label} has an unapproved query string")
    return url


def _require_date(value: object, label: str) -> str:
    checked = _require_str(value, label, pattern=_DATE_RE)
    try:
        parsed = date.fromisoformat(checked)
    except ValueError as error:
        raise ValueError(f"{label} is not a real calendar date") from error
    if parsed.isoformat() != checked:
        raise ValueError(f"{label} is not canonical")
    return checked


def _validate_bool_evidence(
    value: object, label: str, known_sources: set[str]
) -> dict[str, object]:
    evidence = _require_dict(value, {"source_ids", "status"}, label)
    _require_source_ids(evidence["source_ids"], f"{label}.source_ids", known_sources)
    status = _require_str(evidence["status"], f"{label}.status")
    if status not in _BOOL_EVIDENCE_STATES:
        raise ValueError(f"{label}.status is not a Boolean evidence state")
    return evidence


def _validate_count_evidence(
    value: object, label: str, known_sources: set[str]
) -> dict[str, object]:
    evidence = _require_dict(value, {"count", "source_ids", "status"}, label)
    _require_source_ids(evidence["source_ids"], f"{label}.source_ids", known_sources)
    status = _require_str(evidence["status"], f"{label}.status")
    if status not in _COUNT_EVIDENCE_STATES:
        raise ValueError(f"{label}.status is not a count evidence state")
    count = evidence["count"]
    if status == "CONFIRMED":
        _require_int(count, f"{label}.count")
    elif count is not None:
        raise ValueError(f"{label}.count must be null while unresolved")
    return evidence


def _validate_text_evidence(
    value: object, label: str, known_sources: set[str]
) -> dict[str, object]:
    evidence = _require_dict(
        value, {"source_ids", "status", "value"}, label
    )
    _require_source_ids(evidence["source_ids"], f"{label}.source_ids", known_sources)
    status = _require_str(evidence["status"], f"{label}.status")
    if status not in _TEXT_EVIDENCE_STATES:
        raise ValueError(f"{label}.status is not a text evidence state")
    text = evidence["value"]
    if status == "CONFIRMED":
        checked = _require_str(text, f"{label}.value")
        if _IDENTIFIER_RE.search(checked):
            raise ValueError(f"{label}.value contains an individual identifier")
    elif text is not None:
        raise ValueError(f"{label}.value must be null while unresolved")
    return evidence


def _validate_source(value: object, index: int) -> dict[str, object]:
    label = f"sources[{index}]"
    source = _require_dict(
        value,
        {
            "kind",
            "payload_archived",
            "provenance_status",
            "release_labels",
            "retrieved_on",
            "source_id",
            "url",
        },
        label,
    )
    source_id = _require_str(
        source["source_id"], f"{label}.source_id", pattern=_SOURCE_ID_RE
    )
    kind = _require_str(source["kind"], f"{label}.kind")
    if kind not in _SOURCE_KINDS:
        raise ValueError(f"{label}.kind is not permitted")
    _validate_url(source["url"], f"{label}.url")
    _require_date(source["retrieved_on"], f"{label}.retrieved_on")
    labels = _require_string_list(
        source["release_labels"], f"{label}.release_labels", maximum=8
    )
    provenance = _require_str(
        source["provenance_status"], f"{label}.provenance_status"
    )
    if provenance not in _PROVENANCE_STATES:
        raise ValueError(f"{label}.provenance_status is not permitted")
    if provenance == "CONFLICTING_LABELS" and len(labels) < 2:
        raise ValueError(f"{label} needs two labels for a provenance conflict")
    if provenance == "CONSISTENT" and len(labels) != 1:
        raise ValueError(f"{label} needs exactly one consistent release label")
    if provenance == "NOT_APPLICABLE" and labels:
        raise ValueError(f"{label} cannot carry release labels")
    if _require_bool(
        source["payload_archived"], f"{label}.payload_archived"
    ):
        raise ValueError("C139 does not archive upstream payload bytes")
    return {**source, "source_id": source_id}


def _validate_cohort(
    value: object, index: int, known_sources: set[str]
) -> dict[str, object]:
    label = f"cohorts[{index}]"
    cohort = _require_dict(
        value,
        {
            "arm_label",
            "candidate_roles",
            "cohort_id",
            "complete_subject_upper_bound",
            "criteria",
            "evidence_flags",
            "geo_series",
            "platform",
            "recruitment_institution",
            "reported_site_region",
            "same_subject_complete_count",
            "season",
            "specimen",
            "study_accession",
        },
        label,
    )
    cohort_id = _require_str(
        cohort["cohort_id"], f"{label}.cohort_id", pattern=_COHORT_ID_RE
    )
    accession = _require_str(
        cohort["study_accession"],
        f"{label}.study_accession",
        pattern=_ACCESSION_RE,
    )
    if not cohort_id.startswith(accession + "_"):
        raise ValueError(f"{label}.cohort_id must start with its accession")
    _require_str(cohort["arm_label"], f"{label}.arm_label")
    _require_str(cohort["season"], f"{label}.season")
    roles = _require_string_list(
        cohort["candidate_roles"], f"{label}.candidate_roles", maximum=3
    )
    if not roles or set(roles) - {
        "DISCOVERY",
        "REPLICATION_FALLBACK",
        "REPLICATION_PREFERRED",
    }:
        raise ValueError(f"{label}.candidate_roles is invalid")
    if "DISCOVERY" not in roles:
        raise ValueError(f"{label} must remain auditable for discovery")
    geo_series = _require_string_list(
        cohort["geo_series"],
        f"{label}.geo_series",
        maximum=8,
        pattern=_GEO_RE,
    )
    if not geo_series:
        raise ValueError(f"{label}.geo_series must not be empty")
    if tuple(geo_series) != _EXPECTED_COHORT_GEO.get(cohort_id):
        raise ValueError(f"{label}.geo_series changed its frozen cohort mapping")
    flags = _require_string_list(
        cohort["evidence_flags"], f"{label}.evidence_flags", maximum=16
    )
    if set(flags) - _EVIDENCE_FLAGS:
        raise ValueError(f"{label}.evidence_flags contains an unknown code")

    upper = _validate_count_evidence(
        cohort["complete_subject_upper_bound"],
        f"{label}.complete_subject_upper_bound",
        known_sources,
    )
    complete = _validate_count_evidence(
        cohort["same_subject_complete_count"],
        f"{label}.same_subject_complete_count",
        known_sources,
    )
    if upper["status"] == "CONFIRMED" and complete["status"] == "CONFIRMED":
        if complete["count"] > upper["count"]:
            raise ValueError(f"{label} complete count exceeds its upper bound")

    _validate_text_evidence(
        cohort["platform"], f"{label}.platform", known_sources
    )
    _validate_text_evidence(
        cohort["specimen"], f"{label}.specimen", known_sources
    )
    _validate_text_evidence(
        cohort["reported_site_region"],
        f"{label}.reported_site_region",
        known_sources,
    )
    institution = _validate_text_evidence(
        cohort["recruitment_institution"],
        f"{label}.recruitment_institution",
        known_sources,
    )
    if institution["status"] == "CONFIRMED":
        _require_str(
            institution["value"],
            f"{label}.recruitment_institution.value",
            maximum=80,
            pattern=_INSTITUTION_ID_RE,
        )

    criteria = _require_dict(
        cohort["criteria"], set(_REQUIRED_CRITERIA), f"{label}.criteria"
    )
    for criterion in _REQUIRED_CRITERIA:
        _validate_bool_evidence(
            criteria[criterion], f"{label}.criteria.{criterion}", known_sources
        )

    cohort_data_sources = {
        "immport-search-metadata",
        "immune-signatures-resource",
        f"immport-design-{accession.lower()}",
        *(f"geo-{series.lower()}" for series in geo_series),
    }
    policy_sources = {"immport-download-guide", "immport-dmsp-guide"}
    for field in (
        "complete_subject_upper_bound",
        "same_subject_complete_count",
        "platform",
        "specimen",
        "reported_site_region",
        "recruitment_institution",
    ):
        _require_scoped_evidence_sources(
            cohort[field], f"{label}.{field}", cohort_data_sources
        )
    for criterion in _REQUIRED_CRITERIA:
        allowed = (
            policy_sources
            if criterion
            in {
                "license_version_pinned",
                "public_deidentified_data_under_declared_terms",
            }
            else cohort_data_sources
        )
        _require_scoped_evidence_sources(
            criteria[criterion], f"{label}.criteria.{criterion}", allowed
        )
    return cohort


def _validate_overlap(
    value: object,
    index: int,
    known_sources: set[str],
    known_cohorts: dict[str, dict[str, object]],
) -> tuple[str, str]:
    label = f"overlap_evidence[{index}]"
    record = _require_dict(
        value,
        {"left_cohort_id", "right_cohort_id", "shared_subject_count", "source_ids", "status"},
        label,
    )
    left = _require_str(
        record["left_cohort_id"], f"{label}.left_cohort_id", pattern=_COHORT_ID_RE
    )
    right = _require_str(
        record["right_cohort_id"], f"{label}.right_cohort_id", pattern=_COHORT_ID_RE
    )
    if left not in known_cohorts or right not in known_cohorts:
        raise ValueError(f"{label} names an unknown cohort")
    if left >= right:
        raise ValueError(f"{label} pair must be strictly lexicographically ordered")
    status = _require_str(record["status"], f"{label}.status")
    if status not in {
        "CONFIRMED_DISJOINT",
        "CONFIRMED_OVERLAP",
        "UNRESOLVED",
    }:
        raise ValueError(f"{label}.status is invalid")
    count = record["shared_subject_count"]
    if status == "CONFIRMED_OVERLAP":
        checked_count = _require_int(
            count, f"{label}.shared_subject_count", minimum=1
        )
        for cohort_id in (left, right):
            upper = known_cohorts[cohort_id]["complete_subject_upper_bound"]
            assert type(upper) is dict
            if upper["status"] == "CONFIRMED" and checked_count > upper["count"]:
                raise ValueError(
                    f"{label}.shared_subject_count exceeds {cohort_id}'s upper bound"
                )
    elif count is not None:
        raise ValueError(
            f"{label}.shared_subject_count must be null unless overlap is confirmed"
        )
    source_ids = _require_source_ids(
        record["source_ids"], f"{label}.source_ids", known_sources
    )
    allowed_sources = {
        "immport-search-metadata",
        "immune-signatures-resource",
    }
    for cohort_id in (left, right):
        cohort = known_cohorts[cohort_id]
        accession = cohort["study_accession"]
        allowed_sources.add(f"immport-design-{str(accession).lower()}")
        for series in cohort["geo_series"]:
            allowed_sources.add(f"geo-{str(series).lower()}")
    if set(source_ids) - allowed_sources:
        raise ValueError(f"{label}.source_ids cite an unrelated cohort source")
    return left, right


def validate_manifest(value: object) -> dict[str, object]:
    """Fail closed unless ``value`` is the exact C139 evidence contract."""

    manifest = _require_dict(
        value,
        {
            "artifact_contract",
            "audit_id",
            "base_commit",
            "cohorts",
            "gate_contract",
            "overlap_evidence",
            "power_assessment",
            "schema",
            "snapshot_date",
            "sources",
        },
        "manifest",
    )
    if _require_str(manifest["schema"], "manifest.schema") != MANIFEST_SCHEMA:
        raise ValueError("unexpected manifest schema")
    if _require_str(
        manifest["audit_id"], "manifest.audit_id", maximum=128
    ) != _AUDIT_ID:
        raise ValueError("C139 audit identity has changed")
    if _require_str(
        manifest["base_commit"], "manifest.base_commit", pattern=_HEX40_RE
    ) != BASE_COMMIT:
        raise ValueError("C139 must be rooted at the exact green C138 commit")
    if _require_date(
        manifest["snapshot_date"], "manifest.snapshot_date"
    ) != _SNAPSHOT_DATE:
        raise ValueError("C139 snapshot date has changed")

    artifact = _require_dict(
        manifest["artifact_contract"],
        {
            "content_scope",
            "immport_authenticated_download_performed_by_c139_implementation",
            "model_fitting_in_implementation",
            "network_required_for_replay",
            "outcome_measurements_in_artifact",
            "raw_or_individual_data_in_artifact",
        },
        "manifest.artifact_contract",
    )
    if _require_str(
        artifact["content_scope"], "manifest.artifact_contract.content_scope"
    ) != "PUBLIC_AGGREGATE_METADATA_ONLY":
        raise ValueError("C139 content scope must remain aggregate metadata only")
    for key in (
        "immport_authenticated_download_performed_by_c139_implementation",
        "model_fitting_in_implementation",
        "network_required_for_replay",
        "outcome_measurements_in_artifact",
        "raw_or_individual_data_in_artifact",
    ):
        if _require_bool(artifact[key], f"manifest.artifact_contract.{key}"):
            raise ValueError(f"manifest.artifact_contract.{key} must be false")

    gate = _require_dict(
        manifest["gate_contract"],
        {
            "minimum_complete_subjects_per_cohort",
            "minimum_discovery_cohorts",
            "minimum_discovery_complete_subjects",
            "minimum_discovery_institutions",
            "minimum_replication_complete_subjects",
            "minimum_simulated_power_basis_points",
            "replication_priority",
            "target_mse_improvement_basis_points",
            "windows",
        },
        "manifest.gate_contract",
    )
    expected_ints = {
        "minimum_complete_subjects_per_cohort": 25,
        "minimum_discovery_cohorts": 5,
        "minimum_discovery_complete_subjects": 250,
        "minimum_discovery_institutions": 3,
        "minimum_replication_complete_subjects": 50,
        "minimum_simulated_power_basis_points": 8000,
        "target_mse_improvement_basis_points": 500,
    }
    for key, expected in expected_ints.items():
        if _require_int(gate[key], f"manifest.gate_contract.{key}") != expected:
            raise ValueError(f"manifest.gate_contract.{key} must remain {expected}")
    priority = _require_string_list(
        gate["replication_priority"],
        "manifest.gate_contract.replication_priority",
        maximum=2,
        pattern=_COHORT_ID_RE,
    )
    if tuple(priority) != _REPLICATION_PRIORITY:
        raise ValueError("replication priority has changed")
    windows = _require_dict(
        gate["windows"], {"baseline", "early", "middle", "outcome"}, "manifest.gate_contract.windows"
    )
    expected_windows = {
        "baseline": ([0, 0], 0),
        "early": ([1, 3], 1),
        "middle": ([5, 9], 7),
        "outcome": ([28, 35], 28),
    }
    for key, (expected_range, expected_target) in expected_windows.items():
        window = _require_dict(
            windows[key],
            {"allowed_day_range", "target_day", "tie_break"},
            f"manifest.gate_contract.windows.{key}",
        )
        actual = _require_list(
            window["allowed_day_range"],
            f"manifest.gate_contract.windows.{key}.allowed_day_range",
            maximum=2,
        )
        if len(actual) != 2:
            raise ValueError(f"window {key} must have exactly two endpoints")
        checked = [
            _require_int(
                item,
                f"manifest.gate_contract.windows.{key}.allowed_day_range[{index}]",
            )
            for index, item in enumerate(actual)
        ]
        if checked != expected_range:
            raise ValueError(f"window {key} has changed")
        if _require_int(
            window["target_day"],
            f"manifest.gate_contract.windows.{key}.target_day",
        ) != expected_target:
            raise ValueError(f"window {key} target day has changed")
        if _require_str(
            window["tie_break"],
            f"manifest.gate_contract.windows.{key}.tie_break",
        ) != "EARLIER_DAY_THEN_ACCESSION":
            raise ValueError(f"window {key} tie break has changed")

    source_values = _require_list(manifest["sources"], "manifest.sources", maximum=64)
    if not source_values:
        raise ValueError("manifest.sources must not be empty")
    sources = [_validate_source(item, index) for index, item in enumerate(source_values)]
    source_ids = [source["source_id"] for source in sources]
    source_urls = [source["url"] for source in sources]
    if tuple(source_ids) != _EXPECTED_SOURCE_IDS:
        raise ValueError("C139 source inventory or order changed")
    if len(set(source_ids)) != len(source_ids):
        raise ValueError("source IDs must be unique")
    if len(set(source_urls)) != len(source_urls):
        raise ValueError("source URLs must be unique")
    known_sources = set(source_ids)
    for source in sources:
        expected_retrieval_date = (
            "2026-09-04"
            if source["source_id"] in {
                "immport-design-sdy180",
                "immport-design-sdy400",
                "immport-design-sdy1119",
                "geo-gse48762",
                "geo-gse29617",
            }
            else "2026-09-03"
        )
        if source["retrieved_on"] != expected_retrieval_date:
            raise ValueError("C139 source retrieval date changed from its frozen value")
    sources_by_id = {source["source_id"]: source for source in sources}
    for source_id, expected in _STATIC_SOURCE_CONTRACTS.items():
        source = sources_by_id[source_id]
        actual = (
            source["kind"],
            source["provenance_status"],
            source["release_labels"],
            source["url"],
        )
        if actual != expected:
            raise ValueError(f"{source_id} no longer matches its frozen source contract")

    cohort_values = _require_list(manifest["cohorts"], "manifest.cohorts", maximum=16)
    cohorts = [
        _validate_cohort(item, index, known_sources)
        for index, item in enumerate(cohort_values)
    ]
    cohort_ids = [cohort["cohort_id"] for cohort in cohorts]
    if tuple(cohort_ids) != _EXPECTED_COHORT_IDS:
        raise ValueError("C139 candidate cohort inventory or order changed")
    if len({cohort["study_accession"] for cohort in cohorts}) != len(cohorts):
        raise ValueError("each C139 cohort must use a distinct study accession")
    for cohort in cohorts:
        accession = cohort["study_accession"]
        design_id = f"immport-design-{accession.lower()}"
        design_source = sources_by_id.get(design_id)
        expected_design_url = (
            f"https://www.immport.org/data/query/ui/study/design/{accession}"
        )
        if (
            design_source is None
            or design_source["kind"] != "IMMPORT_PUBLIC_METADATA"
            or design_source["provenance_status"] != "CONSISTENT"
            or design_source["release_labels"] != ["DR58"]
            or design_source["url"] != expected_design_url
        ):
            raise ValueError(f"{cohort['cohort_id']} lacks its matching ImmPort design source")
        for geo_series in cohort["geo_series"]:
            geo_source = sources_by_id.get(f"geo-{geo_series.lower()}")
            expected_geo_labels = _GEO_SOURCE_LABELS.get(geo_series)
            expected_geo_url = (
                "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi"
                f"?acc={geo_series}"
            )
            if (
                expected_geo_labels is None
                or geo_source is None
                or geo_source["kind"] != "PUBLIC_REPOSITORY_METADATA"
                or geo_source["release_labels"] != expected_geo_labels
                or geo_source["provenance_status"]
                != (
                    "CONSISTENT"
                    if len(expected_geo_labels) == 1
                    else "CONFLICTING_LABELS"
                )
                or geo_source["url"] != expected_geo_url
            ):
                raise ValueError(
                    f"{cohort['cohort_id']} lacks one exact source for {geo_series}"
                )
    role_counts = {
        role: sum(role in cohort["candidate_roles"] for cohort in cohorts)
        for role in ("REPLICATION_PREFERRED", "REPLICATION_FALLBACK")
    }
    if role_counts != {"REPLICATION_PREFERRED": 1, "REPLICATION_FALLBACK": 1}:
        raise ValueError("replication roles must be unique")
    for role, cohort_id in zip(
        ("REPLICATION_PREFERRED", "REPLICATION_FALLBACK"),
        _REPLICATION_PRIORITY,
    ):
        cohort = next(item for item in cohorts if item["cohort_id"] == cohort_id)
        if role not in cohort["candidate_roles"]:
            raise ValueError(f"{cohort_id} does not carry its declared replication role")

    overlap_values = _require_list(
        manifest["overlap_evidence"], "manifest.overlap_evidence", maximum=36
    )
    cohorts_by_id = {cohort["cohort_id"]: cohort for cohort in cohorts}
    pairs = [
        _validate_overlap(item, index, known_sources, cohorts_by_id)
        for index, item in enumerate(overlap_values)
    ]
    if len(set(pairs)) != len(pairs):
        raise ValueError("overlap pairs must be unique")

    power = _require_dict(
        manifest["power_assessment"],
        {"estimated_power_basis_points", "status"},
        "manifest.power_assessment",
    )
    power_status = _require_str(power["status"], "manifest.power_assessment.status")
    power_value = power["estimated_power_basis_points"]
    if power_status != "NOT_EVALUATED" or power_value is not None:
        raise ValueError(
            "C139 metadata-only v1 requires unevaluated power with a null estimate"
        )
    _reject_sensitive_strings(manifest, "manifest")
    return manifest


def _reject_sensitive_strings(value: object, label: str) -> None:
    if type(value) is str:
        if (
            _IDENTIFIER_RE.search(value)
            or _MEASUREMENT_VALUE_RE.search(value)
            or _VALUE_BEFORE_MEASUREMENT_RE.search(value)
            or _BASE64_BLOB_RE.search(value)
            or _BASE64URL_BLOB_RE.search(value)
            or _JWT_RE.search(value)
            or _CLOUD_KEY_RE.search(value)
        ):
            raise ValueError(f"{label} contains individual or measurement-level content")
        if _CREDENTIAL_RE.search(value):
            raise ValueError(f"{label} contains credential-like content")
        return
    if type(value) is list:
        for index, item in enumerate(value):
            _reject_sensitive_strings(item, f"{label}[{index}]")
        return
    if type(value) is dict:
        for key, item in value.items():
            _reject_sensitive_strings(item, f"{label}.{key}")


def _count_value(evidence: dict[str, object]) -> int | None:
    if evidence["status"] == "CONFIRMED":
        return evidence["count"]  # type: ignore[return-value]
    return None


def _text_value(evidence: dict[str, object]) -> str | None:
    if evidence["status"] == "CONFIRMED":
        return evidence["value"]  # type: ignore[return-value]
    return None


def _classify_cohort(
    cohort: dict[str, object], minimum: int
) -> dict[str, object]:
    criteria = cohort["criteria"]
    assert type(criteria) is dict
    false_criteria = sorted(
        key for key, evidence in criteria.items()
        if evidence["status"] == "CONFIRMED_FALSE"
    )
    unresolved_criteria = sorted(
        key for key, evidence in criteria.items()
        if evidence["status"] == "UNRESOLVED"
    )
    upper_evidence = cohort["complete_subject_upper_bound"]
    complete_evidence = cohort["same_subject_complete_count"]
    assert type(upper_evidence) is dict and type(complete_evidence) is dict
    upper = _count_value(upper_evidence)
    complete = _count_value(complete_evidence)

    reasons: list[str] = []
    if false_criteria:
        reasons.extend(f"CONFIRMED_FALSE_{name.upper()}" for name in false_criteria)
    if upper is not None and upper < minimum:
        reasons.append("COMPLETE_SUBJECT_UPPER_BOUND_BELOW_25")
    if complete is not None and complete < minimum:
        reasons.append("CONFIRMED_COMPLETE_SUBJECT_COUNT_BELOW_25")

    if reasons:
        classification = "EXCLUDED"
    elif not unresolved_criteria and complete is not None and complete >= minimum:
        classification = "ELIGIBLE"
    else:
        classification = "UNRESOLVED"
        if complete is None:
            reasons.append("SAME_SUBJECT_COMPLETE_COUNT_UNRESOLVED")
        reasons.extend(f"UNRESOLVED_{name.upper()}" for name in unresolved_criteria)

    return {
        "candidate_roles": cohort["candidate_roles"],
        "classification": classification,
        "cohort_id": cohort["cohort_id"],
        "complete_subject_upper_bound": upper,
        "confirmed_complete_subject_count": complete,
        "evidence_flags": cohort["evidence_flags"],
        "reason_codes": sorted(set(reasons)),
        "recruitment_institution": _text_value(cohort["recruitment_institution"]),
        "study_accession": cohort["study_accession"],
        "unresolved_criteria": unresolved_criteria,
    }


def _strategy_report(
    replication_id: str,
    records: list[dict[str, object]],
    overlap: dict[tuple[str, str], str],
    gate: dict[str, object],
) -> dict[str, object]:
    by_id = {record["cohort_id"]: record for record in records}
    replication = by_id[replication_id]
    discovery = sorted(
        [
        record
        for record in records
        if record["cohort_id"] != replication_id
        and "DISCOVERY" in record["candidate_roles"]
        and record["classification"] == "ELIGIBLE"
        ],
        key=lambda record: record["cohort_id"],
    )
    replication_count = replication["confirmed_complete_subject_count"]
    replication_pass = (
        replication["classification"] == "ELIGIBLE"
        and replication_count is not None
        and replication_count >= gate["minimum_replication_complete_subjects"]
    )
    selections = [
        list(selection)
        for size in range(gate["minimum_discovery_cohorts"], len(discovery) + 1)
        for selection in combinations(discovery, size)
    ]
    if not selections:
        selections = [discovery]

    evaluations: list[dict[str, object]] = []
    for selection in selections:
        discovery_subjects = sum(
            record["confirmed_complete_subject_count"] for record in selection
        )
        institutions = {
            record["recruitment_institution"]
            for record in selection
            if record["recruitment_institution"] is not None
        }
        selected_ids = sorted(
            [replication_id] + [record["cohort_id"] for record in selection]
        )
        selected_pairs = [tuple(pair) for pair in combinations(selected_ids, 2)]
        disjoint = bool(selected_pairs) and all(
            overlap.get(pair) == "CONFIRMED_DISJOINT" for pair in selected_pairs
        )
        checks = {
            "discovery_complete_subjects": discovery_subjects
            >= gate["minimum_discovery_complete_subjects"],
            "discovery_cohorts": len(selection) >= gate["minimum_discovery_cohorts"],
            "discovery_institutions": len(institutions)
            >= gate["minimum_discovery_institutions"],
            "pairwise_disjoint": disjoint,
            # C139 v1 is metadata-only.  Power has no executable evidence
            # contract here, so this gate is intentionally non-authorizing.
            "power": False,
            "replication_complete_subjects": replication_pass,
        }
        metadata_checks = {
            key: value for key, value in checks.items() if key != "power"
        }
        evaluations.append(
            {
                "checks": checks,
                "confirmed_discovery_complete_subjects": discovery_subjects,
                "confirmed_discovery_cohort_ids": [
                    record["cohort_id"] for record in selection
                ],
                "confirmed_discovery_institutions": sorted(institutions),
                "metadata_capacity_passes": all(metadata_checks.values()),
                "passes": all(checks.values()),
            }
        )
    metadata_passing = [
        evaluation
        for evaluation in evaluations
        if evaluation["metadata_capacity_passes"]
    ]
    if metadata_passing:
        chosen = min(
            metadata_passing,
            key=lambda evaluation: (
                len(evaluation["confirmed_discovery_cohort_ids"]),
                tuple(evaluation["confirmed_discovery_cohort_ids"]),
            ),
        )
    else:
        # Preserve a useful deterministic diagnostic when no subset satisfies
        # the non-power metadata gate.  This choice can never authorize fitting.
        chosen = min(
            evaluations,
            key=lambda evaluation: (
                -sum(
                    value
                    for key, value in evaluation["checks"].items()
                    if key != "power"
                ),
                -evaluation["confirmed_discovery_complete_subjects"],
                -len(evaluation["confirmed_discovery_institutions"]),
                len(evaluation["confirmed_discovery_cohort_ids"]),
                tuple(evaluation["confirmed_discovery_cohort_ids"]),
            ),
        )
    return {
        "checks": chosen["checks"],
        "confirmed_discovery_complete_subjects": chosen["confirmed_discovery_complete_subjects"],
        "confirmed_discovery_cohort_ids": chosen["confirmed_discovery_cohort_ids"],
        "confirmed_discovery_institutions": chosen["confirmed_discovery_institutions"],
        "confirmed_replication_complete_subjects": replication_count,
        "metadata_capacity_passes": chosen["metadata_capacity_passes"],
        "passes": chosen["passes"],
        "replication_cohort_id": replication_id,
    }


def _optimistic_strategy(
    replication_id: str,
    records: list[dict[str, object]],
    replication_threshold: int,
) -> dict[str, object]:
    by_id = {record["cohort_id"]: record for record in records}
    replication = by_id[replication_id]
    possible_discovery = [
        record
        for record in records
        if record["cohort_id"] != replication_id
        and "DISCOVERY" in record["candidate_roles"]
        and record["classification"] != "EXCLUDED"
    ]
    missing_upper_ids = [
        record["cohort_id"]
        for record in possible_discovery
        if record["complete_subject_upper_bound"] is None
    ]
    upper = (
        None
        if missing_upper_ids
        else sum(
            record["complete_subject_upper_bound"]
            for record in possible_discovery
        )
    )
    replication_upper = replication["complete_subject_upper_bound"]
    return {
        "discovery_cohort_ids": [record["cohort_id"] for record in possible_discovery],
        "discovery_cohort_upper_bound": len(possible_discovery),
        "discovery_complete_subject_upper_bound": upper,
        "discovery_upper_bound_complete": not missing_upper_ids,
        "ignores_unknown_criteria_and_overlap": True,
        "missing_discovery_upper_bound_cohort_ids": missing_upper_ids,
        "replication_cohort_id": replication_id,
        "replication_complete_subject_upper_bound": replication_upper,
        "replication_upper_bound_complete": replication_upper is not None,
        "replication_threshold_impossible": (
            replication_upper is not None and replication_upper < replication_threshold
        ),
    }


def audit_manifest(
    manifest: dict[str, object], *, manifest_bytes: bytes | None = None
) -> dict[str, object]:
    """Derive the C139 fail-closed audit report from evidence only."""

    checked = validate_manifest(manifest)
    canonical = canonical_json_bytes(checked)
    if manifest_bytes is not None:
        if type(manifest_bytes) is not bytes:
            raise TypeError("manifest_bytes must be built-in bytes")
        if manifest_bytes != canonical:
            raise ValueError("manifest_bytes do not match the canonical manifest")

    gate = checked["gate_contract"]
    assert type(gate) is dict
    records = [
        _classify_cohort(cohort, gate["minimum_complete_subjects_per_cohort"])
        for cohort in checked["cohorts"]
    ]
    status_counts = {
        status: sum(record["classification"] == status for record in records)
        for status in ("ELIGIBLE", "EXCLUDED", "UNRESOLVED")
    }

    overlap = {
        (record["left_cohort_id"], record["right_cohort_id"]): record["status"]
        for record in checked["overlap_evidence"]
    }
    power = checked["power_assessment"]
    assert type(power) is dict
    strategies = [
        _strategy_report(
            replication_id,
            records,
            overlap,
            gate,
        )
        for replication_id in gate["replication_priority"]
    ]
    optimistic = [
        _optimistic_strategy(
            replication_id,
            records,
            gate["minimum_replication_complete_subjects"],
        )
        for replication_id in gate["replication_priority"]
    ]
    any_pass = any(strategy["passes"] for strategy in strategies)

    reason_codes: list[str] = []
    if not any_pass:
        reason_codes.append("NO_CONFIRMED_STRATEGY_PASSES")
    if all(
        item["discovery_upper_bound_complete"]
        and item["discovery_complete_subject_upper_bound"]
        < gate["minimum_discovery_complete_subjects"]
        for item in optimistic
    ):
        reason_codes.append("OPTIMISTIC_DISCOVERY_BOUND_BELOW_250")
    if all(item["replication_threshold_impossible"] for item in optimistic):
        reason_codes.append("BOTH_REPLICATION_BOUNDS_BELOW_50")
    if power["status"] != "CONFIRMED":
        reason_codes.append("POWER_NOT_EVALUATED")
    if not any(record["classification"] == "ELIGIBLE" for record in records):
        reason_codes.append("NO_ELIGIBLE_COHORTS")
    if not any(
        strategy["checks"]["pairwise_disjoint"] for strategy in strategies
    ):
        reason_codes.append("OVERLAP_NOT_CONFIRMED_DISJOINT")

    return {
        "algorithm": ALGORITHM,
        "declared_artifact_contract": checked["artifact_contract"],
        "base_commit": checked["base_commit"],
        "cohort_audit": {
            "records": records,
            "status_counts": status_counts,
        },
        "confirmed_gate": {
            "power_assessment": power,
            "strategies": strategies,
        },
        "final_gate": {
            "fitting_authorized": False,
            "reason_codes": sorted(reason_codes),
            "status": "INSUFFICIENT_EVIDENCE",
            "thresholds_lowered": False,
        },
        "limitations": [
            "NO_CAUSAL_OR_BIOLOGICAL_CLAIM",
            "NO_COMPLETE_CASE_OR_OUTCOME_VALUE_AUDIT",
            "NO_EMPIRICAL_MODEL_FIT",
            "NO_HUMAN_OUTCOME_BLINDNESS_ATTESTATION",
            "UPSTREAM_PAYLOAD_BYTES_NOT_ARCHIVED",
        ],
        "manifest_schema": checked["schema"],
        "manifest_sha256": hashlib.sha256(canonical).hexdigest(),
        "optimistic_capacity_audit": {
            "diagnostic_only": True,
            "strategies": optimistic,
        },
        "schema": REPORT_SCHEMA,
    }
