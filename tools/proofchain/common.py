#!/usr/bin/env python3
"""Shared helpers for VF-H2 proof-chain tooling.

These scripts are intentionally dependency-free. The point is to make the
repository check its own proof artifacts without installing half the internet,
because apparently even proofs need plumbing now.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

ROOT = Path.cwd()
OUTPUTS_DIR = ROOT / "outputs"
REPORTS_DIR = OUTPUTS_DIR / "reports"

THEOREM_ID_RE = re.compile(
    r"\b[A-Z][A-Z0-9_]*(?:-[A-Z0-9_]+)*-VF-H2-\d{3,4}(?:-[A-Z0-9_]+)?\b"
)
MARKER_OK_RE = re.compile(r"\b[A-Z][A-Z0-9_]*_OK\b")

BOUNDARY_FALSE_KEYS = {
    "full_viruse_fabric_theory_proved",
    "original_unrestricted_ttp_vf_h2_004_proved",
    "empirical_validation",
    "biological_validation",
    "manuscript_ready",
    "submission_ready",
}

PROVED_KEYS = {
    "target_theorem_proved",
    "target_artifact_proved",
    "proved",
    "theorem_proved",
    "lemma_proved",
}

TARGET_KEYS = {
    "target_theorem",
    "target_artifact",
    "theorem_id",
    "lemma_id",
    "artifact_id",
    "id",
}

DEPENDENCY_KEYS = {
    "prior_anchors",
    "dependencies",
    "uses",
    "required_inputs",
    "inputs_verified",
    "frozen_anchor",
    "frozen_anchors",
    "anchors",
}

BOUNDARY_PHRASES = [
    "restricted finite",
    "restricted bridge",
    "finite restricted",
    "full theory remains not proved",
    "full viruse fabric theory proved false",
    "\"full_viruse_fabric_theory_proved\": false",
    "unrestricted ttp-vf-h2-004 proved false",
    "\"original_unrestricted_ttp_vf_h2_004_proved\": false",
    "empirical validation remains false",
    "\"empirical_validation\": false",
    "biological validation remains false",
    "\"biological_validation\": false",
    "\"manuscript_ready\": false",
    "\"submission_ready\": false",
    "not empirical validation",
    "not biological validation",
    "not prove the unrestricted",
    "unrestricted theory not proved",
]

# Positive claims that are unsafe unless clearly negated nearby.
FORBIDDEN_CLAIM_PATTERNS = [
    ("full_theory_proved", re.compile(r"\bfull\s+(?:viruse\s+fabric\s+)?theory\s+(?:is\s+)?proved\b", re.I)),
    ("unrestricted_vf_h2_proved", re.compile(r"\bunrestricted\s+(?:vf-h2|ttp-vf-h2-004|theory)\s+(?:is\s+)?proved\b", re.I)),
    ("empirically_validated", re.compile(r"\bempirically\s+validated\b|\bempirical\s+validation\s+(?:is\s+)?(?:true|complete|proved|confirmed)\b", re.I)),
    ("biologically_validated", re.compile(r"\bbiologically\s+validated\b|\bbiological\s+validation\s+(?:is\s+)?(?:true|complete|proved|confirmed)\b", re.I)),
    ("manuscript_ready", re.compile(r"\bmanuscript[-\s]+ready\b|\bmanuscript\s+readiness\s+(?:is\s+)?(?:true|complete|confirmed)\b", re.I)),
    ("submission_ready", re.compile(r"\bsubmission[-\s]+ready\b|\bsubmission\s+readiness\s+(?:is\s+)?(?:true|complete|confirmed)\b", re.I)),
    ("q1_ready", re.compile(r"\bQ1[-\s]+ready\b", re.I)),
    ("real_biological_dataset_validated", re.compile(r"\breal\s+biological\s+dataset\s+validated\b", re.I)),
    ("real_pathogen_simulation_validated", re.compile(r"\breal\s+pathogen\s+simulation\s+validated\b", re.I)),
]

NEGATION_HINTS = {
    "not",
    "no",
    "never",
    "false",
    "without",
    "fails",
    "failed",
    "unproved",
    "not-proved",
    "not_proved",
    "remains",
    "remain",
    "isn't",
    "isnt",
    "cannot",
    "can't",
    "cant",
    "does not",
    "doesn't",
    "doesnt",
    "نیست",
    "نشده",
    "نشد",
    "ندارد",
    "غیر",
}

@dataclass
class SourceFile:
    path: Path
    relpath: str
    text: str
    json_data: Any | None = None
    json_error: str | None = None


def ensure_reports_dir() -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def iter_artifact_files(include_reports: bool = False) -> list[Path]:
    if not OUTPUTS_DIR.exists():
        return []
    paths: list[Path] = []
    for path in OUTPUTS_DIR.rglob("*"):
        if not path.is_file():
            continue
        if not include_reports and REPORTS_DIR in path.parents:
            continue
        if path.suffix.lower() not in {".json", ".md", ".txt", ".yaml", ".yml"}:
            continue
        paths.append(path)
    return sorted(paths)


def read_source(path: Path) -> SourceFile:
    relpath = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")
    json_data = None
    json_error = None
    if path.suffix.lower() == ".json":
        try:
            json_data = json.loads(text)
        except Exception as exc:  # noqa: BLE001 - report exact parse failure
            json_error = f"{type(exc).__name__}: {exc}"
    return SourceFile(path=path, relpath=relpath, text=text, json_data=json_data, json_error=json_error)


def all_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield str(key)
            yield from all_strings(item)
    elif isinstance(value, (list, tuple, set)):
        for item in value:
            yield from all_strings(item)
    elif value is not None:
        yield str(value)


def walk_json(value: Any, prefix: tuple[str, ...] = ()) -> Iterable[tuple[tuple[str, ...], Any]]:
    yield prefix, value
    if isinstance(value, dict):
        for key, item in value.items():
            yield from walk_json(item, prefix + (str(key),))
    elif isinstance(value, list):
        for idx, item in enumerate(value):
            yield from walk_json(item, prefix + (str(idx),))


def extract_ids_from_text(text: str) -> list[str]:
    return sorted(set(THEOREM_ID_RE.findall(text)))


def extract_ok_markers(text: str) -> list[str]:
    return sorted(set(MARKER_OK_RE.findall(text)))


def normalized_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def has_boundary_signal(source: SourceFile) -> bool:
    text = normalized_text(source.text)
    if any(phrase in text for phrase in BOUNDARY_PHRASES):
        return True
    if isinstance(source.json_data, dict):
        for key in BOUNDARY_FALSE_KEYS:
            if source.json_data.get(key) is False:
                return True
    if source.json_data is not None:
        for path, value in walk_json(source.json_data):
            if path and path[-1] in BOUNDARY_FALSE_KEYS and value is False:
                return True
    return False


def is_proof_like(source: SourceFile) -> bool:
    rel = source.relpath.lower()
    if any(token in rel for token in ("proof", "theorem", "bridge", "lemma")):
        return True
    if source.json_data is not None:
        for path, _value in walk_json(source.json_data):
            if path and path[-1] in TARGET_KEYS.union(PROVED_KEYS):
                return True
    text = source.text.lower()
    return bool(re.search(r"\b(theorem|lemma|proof|bridge)\b", text))


def is_positive_claim_negated(text: str, match_start: int) -> bool:
    window = text[max(0, match_start - 140):match_start].lower()
    compact = re.sub(r"\s+", " ", window)
    if any(hint in compact[-80:] for hint in NEGATION_HINTS):
        return True
    # Common structured boundary claims.
    if re.search(r"(?:proved|validation|ready)\s*[:=]\s*false\s*$", compact):
        return True
    return False




def is_nonassertive_claim_context(text: str, match_start: int, match_end: int) -> bool:
    """Return True when a forbidden-looking phrase is not a positive claim.

    This is intentionally conservative around local context:
    it ignores negated claims, blocked-language inventories, zero counters,
    prohibited-phrase lists, and instructions like "avoid X" or "do not call X".
    """
    before = re.sub(r"\s+", " ", text[max(0, match_start - 900):match_start].lower())
    after = re.sub(r"\s+", " ", text[match_end:match_end + 500].lower())
    around = re.sub(
        r"\s+",
        " ",
        text[max(0, match_start - 900):min(len(text), match_end + 900)].lower(),
    )

    # Zero counters and dashboard fields.
    zero_counter_patterns = (
        r'count"?\s*[:=]\s*0\b',
        r'claim count"?\s*[:=]\s*0\b',
        r'created count"?\s*[:=]\s*0\b',
        r'readiness claim count"?\s*[:=]\s*0\b',
        r'submission ready manuscript created count"?\s*[:=]\s*0\b',
        r'submission readiness claim count"?\s*[:=]\s*0\b',
        r'manuscript submission ready count\s*[:=]\s*0\b',
    )
    if any(re.search(pattern, after) or re.search(pattern, around) for pattern in zero_counter_patterns):
        return True

    # The phrase is being used as a label, row, field, inventory item, or metric.
    if re.match(
        r'\s*(?:count|counts|row|rows|field|fields|flag|flags|phrase|phrases|term|terms|token|tokens|keyword|keywords|metric|metrics)\b',
        after,
    ):
        return True

    # Explicit local negation/prohibition before the matched phrase.
    safe_before_markers = (
        "avoid ",
        "do not ",
        "don't ",
        "not ",
        "not a ",
        "not an ",
        "no ",
        "never ",
        "must not ",
        "should not ",
        "cannot ",
        "can not ",
        "without ",
        "is not ",
        "are not ",
        "was not ",
        "were not ",
        "remains false",
        "remain false",
        "remains zero",
        "remain zero",
        "until ",
        "blocked claim",
        "blocked language",
        "blocked phrase",
        "safe allowed",
        "prohibited",
        "forbidden",
        "disallowed",
        "unsafe phrase",
        "unsafe claim",
        "hard gate",
        "boundary",
        "not called",
        "not call",
        "not making",
        "not marked",
        "not classified",
        "not supported",
        "not externally",
        "not independently",
        "not readiness",
        "not manuscript",
        "not submission",
    )
    if any(marker in before[-500:] for marker in safe_before_markers):
        return True

    # Questions are not positive readiness claims.
    if "## question" in around and ("can " in around or "could " in around or "whether " in around):
        return True
    if re.search(r"\bcan\s+[^?]{0,260}(?:manuscript[- ]ready|submission[- ]ready|empirically validated|biologically validated|externally validated)", around):
        return True

    # Explicit safe patterns around the phrase.
    safe_around_patterns = (
        r"avoid\s+[^.]{0,240}submission[- ]ready",
        r"do not\s+[^.]{0,240}submission[- ]ready",
        r"not\s+(?:a|an)?\s*[^.]{0,240}submission[- ]ready",
        r"without\s+[^.]{0,240}submission[- ]ready",
        r"blocked claim\s+[^.]{0,260}submission[- ]ready",
        r"blocked language\s*[:=]\s*[^.]{0,260}",
        r"safe allowed\s+[^.]{0,260}submission[- ]ready",
        r"readiness approval and manuscript submission ready counters remain zero",
        r"submission ready counters remain zero",
        r"submission readiness claim count",
        r"submission ready manuscript created count",
        r"manuscript submission ready count",
        r"making the manuscript submission[- ]ready",
        r"not a\s+[^.]{0,120}submission[- ]ready manuscript",
        r"not\s+[^.]{0,120}submission[- ]ready manuscript",
        r"not\s+[^.]{0,120}externally validated",
        r"not\s+[^.]{0,120}empirically validated",
        r"not\s+[^.]{0,120}biologically validated",
        r"not\s+[^.]{0,120}manuscript[- ]ready",
    )
    if any(re.search(pattern, around) for pattern in safe_around_patterns):
        return True

    # Inventories of bad phrases often list many prohibited claims together.
    inventory_terms = (
        "operational intervention system",
        "externally validated theory",
        "submission-ready manuscript",
        "universal theory of causality",
        "replacement for existing",
        "clinical relevance",
        "laboratory guidance",
        "operational readiness",
        "final paper",
        "peer-reviewed",
        "accepted scientific theory",
        "biological prediction",
        "independently experimentally validated",
    )
    if sum(term in around for term in inventory_terms) >= 2:
        return True

    return False

def find_unsafe_text_claims(source: SourceFile) -> list[dict[str, Any]]:
    claims: list[dict[str, Any]] = []
    text = source.text
    for claim_type, pattern in FORBIDDEN_CLAIM_PATTERNS:
        for match in pattern.finditer(text):
            if is_positive_claim_negated(text, match.start()) or is_nonassertive_claim_context(text, match.start(), match.end()):
                continue
            snippet_start = max(0, match.start() - 80)
            snippet_end = min(len(text), match.end() + 80)
            claims.append(
                {
                    "claim_type": claim_type,
                    "match": match.group(0),
                    "snippet": text[snippet_start:snippet_end].replace("\n", " "),
                }
            )
    return claims


def find_unsafe_json_claims(source: SourceFile) -> list[dict[str, Any]]:
    claims: list[dict[str, Any]] = []
    if source.json_data is None:
        return claims
    for path, value in walk_json(source.json_data):
        if not path:
            continue
        key = path[-1]
        if key in BOUNDARY_FALSE_KEYS and value is True:
            claims.append(
                {
                    "claim_type": f"unsafe_true_boolean:{key}",
                    "json_path": ".".join(path),
                    "value": value,
                }
            )
    return claims


def write_json_report(name: str, data: Any) -> Path:
    ensure_reports_dir()
    path = REPORTS_DIR / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def infer_id_type(identifier: str) -> str:
    if identifier.startswith("RBRIDGE-"):
        return "restricted bridge theorem"
    if identifier.startswith("TTP-"):
        return "theorem target"
    if "LYAP" in identifier:
        return "lyapunov lemma"
    if identifier.startswith(("P_R-", "ORD-", "RUMAP-", "FSP-", "FFP-")):
        return "restricted anchor"
    return "artifact"
