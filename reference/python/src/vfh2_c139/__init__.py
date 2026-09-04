"""Fail-closed public-metadata feasibility audit for the C139 gate."""

from .core import (
    ALGORITHM,
    BASE_COMMIT,
    MANIFEST_SCHEMA,
    REPORT_SCHEMA,
    audit_manifest,
    canonical_json_bytes,
    load_manifest_bytes,
    validate_manifest,
)

__all__ = [
    "ALGORITHM",
    "BASE_COMMIT",
    "MANIFEST_SCHEMA",
    "REPORT_SCHEMA",
    "audit_manifest",
    "canonical_json_bytes",
    "load_manifest_bytes",
    "validate_manifest",
]
