from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class AuditFinding:
    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class ManuscriptQualityAuditReport:
    title: str
    output_path: str
    manuscript_path: str
    section_count: int
    word_count: int
    required_section_count: int
    missing_required_section_count: int
    boundary_phrase_count: int
    missing_boundary_phrase_count: int
    validation_metric_count: int
    overclaim_count: int
    weak_phrase_count: int
    recommendation_count: int
    finding_count: int
    error_count: int
    warning_count: int
    passed: bool
    interpretation: str


class ManuscriptQualityAuditor:
    title = "Manuscript Quality Audit v3.3"

    minimum_word_count = 2500
    maximum_word_count = 4500
    minimum_validation_metric_count = 9
    maximum_overclaim_count = 0

    required_sections: tuple[str, ...] = (
        "Manuscript Status",
        "Working Title",
        "Abstract",
        "Introduction",
        "Core Thesis",
        "Formal Model",
        "Validation Sequence",
        "Results",
        "Limitations",
        "Allowed and Disallowed Claims",
        "Future Work",
        "Human-AI Work Note",
        "Source Artifact Inventory",
        "Research Boundary",
        "Conclusion",
    )

    boundary_phrases: tuple[str, ...] = (
        "research prototype with internal validation",
        "not a final paper",
        "not an external validation report",
        "not support strong public claims",
        "not externally validated",
        "real pathogens",
        "real hosts",
        "biological protocols",
        "laboratory procedures",
        "executable interventions",
        "external validation",
        "operational intervention",
    )

    validation_metrics: tuple[str, ...] = (
        "59.84%",
        "65.37%",
        "729",
        "100.00%",
        "8640",
        "81.06%",
        "44.15",
        "zero false positives",
        "22",
        "3",
        "86.36%",
        "readiness score of 68",
    )

    risky_claim_patterns: tuple[str, ...] = (
        "proves a universal law",
        "predicts real biological",
        "has external biological validation",
        "supports laboratory procedures",
        "ready for strong public claims",
        "establishes a universal theory",
        "proves the theory",
    )

    weak_phrases: tuple[str, ...] = (
        "obviously",
        "undeniably",
        "clearly proves",
        "revolutionary breakthrough",
        "paradigm-shifting proof",
    )

    recommendations: tuple[str, ...] = (
        "Add a related-work section before external review.",
        "Introduce formal notation for intrinsic scoring, observer projection, and correction.",
        "Convert validation results into a compact table for manuscript readability.",
        "Add a failure taxonomy for fragile regions from adversarial sensitivity.",
        "Separate manuscript voice from project-log voice before submission.",
        "Keep external validation boundaries visible in the abstract, limitations, and conclusion.",
    )

    def __init__(
        self,
        manuscript_path: Path | None = None,
        output_path: Path | None = None,
    ) -> None:
        self.manuscript_path = manuscript_path or Path("outputs/full_manuscript_draft_v3_2.md")
        self.output_path = output_path or Path("outputs/manuscript_quality_audit_v3_3.md")

    def run(self) -> ManuscriptQualityAuditReport:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        manuscript = self.read_manuscript()
        findings = self.evaluate(manuscript)
        markdown = self.render_markdown(manuscript, findings)
        self.output_path.write_text(markdown, encoding="utf-8")

        error_count = sum(1 for finding in findings if finding.severity == "error")
        warning_count = sum(1 for finding in findings if finding.severity == "warning")

        return ManuscriptQualityAuditReport(
            title=self.title,
            output_path=str(self.output_path),
            manuscript_path=str(self.manuscript_path),
            section_count=self.section_count(manuscript),
            word_count=self.word_count(manuscript),
            required_section_count=len(self.required_sections),
            missing_required_section_count=len(self.missing_required_sections(manuscript)),
            boundary_phrase_count=self.boundary_phrase_count(manuscript),
            missing_boundary_phrase_count=len(self.missing_boundary_phrases(manuscript)),
            validation_metric_count=self.validation_metric_count(manuscript),
            overclaim_count=len(self.detect_overclaims(manuscript)),
            weak_phrase_count=self.weak_phrase_count(manuscript),
            recommendation_count=len(self.recommendations),
            finding_count=len(findings),
            error_count=error_count,
            warning_count=warning_count,
            passed=error_count == 0,
            interpretation=(
                "The manuscript quality audit checks whether the v3.2 full draft preserves claim boundaries, "
                "validation evidence, and research-prototype caution."
            ),
        )

    def read_manuscript(self) -> str:
        if not self.manuscript_path.exists():
            return ""
        return self.manuscript_path.read_text(encoding="utf-8")

    def evaluate(self, manuscript: str) -> tuple[AuditFinding, ...]:
        findings: list[AuditFinding] = []

        if not self.manuscript_path.exists():
            findings.append(
                AuditFinding(
                    severity="error",
                    code="missing_manuscript",
                    message=f"Manuscript draft not found at {self.manuscript_path}.",
                )
            )
            return tuple(findings)

        missing_sections = self.missing_required_sections(manuscript)
        if missing_sections:
            findings.append(
                AuditFinding(
                    severity="error",
                    code="missing_required_sections",
                    message=f"Missing required sections: {', '.join(missing_sections)}.",
                )
            )

        word_count = self.word_count(manuscript)
        if word_count < self.minimum_word_count:
            findings.append(
                AuditFinding(
                    severity="error",
                    code="manuscript_too_short",
                    message=f"Word count {word_count} is below required {self.minimum_word_count}.",
                )
            )

        if word_count > self.maximum_word_count:
            findings.append(
                AuditFinding(
                    severity="warning",
                    code="manuscript_long_for_first_audit",
                    message=f"Word count {word_count} is above preferred first-audit size.",
                )
            )

        missing_boundary_phrases = self.missing_boundary_phrases(manuscript)
        if missing_boundary_phrases:
            findings.append(
                AuditFinding(
                    severity="error",
                    code="missing_boundary_phrases",
                    message=f"Missing boundary phrases: {', '.join(missing_boundary_phrases)}.",
                )
            )

        validation_metric_count = self.validation_metric_count(manuscript)
        if validation_metric_count < self.minimum_validation_metric_count:
            findings.append(
                AuditFinding(
                    severity="error",
                    code="validation_metrics_underrepresented",
                    message=(
                        f"Only {validation_metric_count} validation metrics were found; "
                        f"required at least {self.minimum_validation_metric_count}."
                    ),
                )
            )

        overclaims = self.detect_overclaims(manuscript)
        if len(overclaims) > self.maximum_overclaim_count:
            findings.append(
                AuditFinding(
                    severity="error",
                    code="unsupported_overclaims_detected",
                    message=f"{len(overclaims)} unsupported overclaim lines were detected.",
                )
            )

        weak_phrase_count = self.weak_phrase_count(manuscript)
        if weak_phrase_count > 0:
            findings.append(
                AuditFinding(
                    severity="warning",
                    code="weak_or_hype_phrases_detected",
                    message=f"{weak_phrase_count} weak or hype phrases were detected.",
                )
            )

        findings.append(
            AuditFinding(
                severity="warning",
                code="needs_related_work",
                message="The draft still needs a related-work section before serious external review.",
            )
        )

        findings.append(
            AuditFinding(
                severity="warning",
                code="needs_formal_notation",
                message="The draft should add formal notation for the model before manuscript submission.",
            )
        )

        findings.append(
            AuditFinding(
                severity="warning",
                code="draft_not_submission_ready",
                message="The draft is suitable for technical review, not for submission or strong public claims.",
            )
        )

        return tuple(findings)

    def missing_required_sections(self, manuscript: str) -> tuple[str, ...]:
        missing = [
            section for section in self.required_sections
            if f"## {section}" not in manuscript
        ]
        return tuple(missing)

    def missing_boundary_phrases(self, manuscript: str) -> tuple[str, ...]:
        lower = manuscript.lower()
        missing = [
            phrase for phrase in self.boundary_phrases
            if phrase.lower() not in lower
        ]
        return tuple(missing)

    def boundary_phrase_count(self, manuscript: str) -> int:
        lower = manuscript.lower()
        return sum(1 for phrase in self.boundary_phrases if phrase.lower() in lower)

    def validation_metric_count(self, manuscript: str) -> int:
        lower = manuscript.lower()
        return sum(1 for metric in self.validation_metrics if metric.lower() in lower)

    def detect_overclaims(self, manuscript: str) -> tuple[str, ...]:
        lines = manuscript.splitlines()
        overclaims: list[str] = []
        in_disallowed_claims = False

        for line in lines:
            stripped = line.strip()
            lower = stripped.lower()

            if stripped == "The current evidence does not support these claims:":
                in_disallowed_claims = True
                continue

            if stripped.startswith("## Future Work"):
                in_disallowed_claims = False

            if in_disallowed_claims:
                continue

            if not stripped:
                continue

            has_negation = any(
                negation in lower
                for negation in (
                    "not ",
                    "does not",
                    "do not",
                    "without",
                    "unsupported",
                    "disallowed",
                    "no external",
                    "not yet",
                )
            )

            for pattern in self.risky_claim_patterns:
                if pattern in lower and not has_negation:
                    overclaims.append(stripped)
                    break

        return tuple(overclaims)

    def weak_phrase_count(self, manuscript: str) -> int:
        lower = manuscript.lower()
        return sum(lower.count(phrase.lower()) for phrase in self.weak_phrases)

    def render_markdown(
        self,
        manuscript: str,
        findings: tuple[AuditFinding, ...],
    ) -> str:
        missing_sections = self.missing_required_sections(manuscript)
        missing_boundary = self.missing_boundary_phrases(manuscript)
        overclaims = self.detect_overclaims(manuscript)

        lines = [
            f"# {self.title}",
            "",
            "## Purpose",
            "",
            (
                "This audit checks whether the full manuscript draft is suitable for cautious technical review. "
                "It focuses on section coverage, validation evidence, claim boundaries, missing limitations, and unsupported overclaims."
            ),
            "",
            "## Summary",
            "",
            f"- Manuscript path: `{self.manuscript_path}`",
            f"- Section count: {self.section_count(manuscript)}",
            f"- Word count: {self.word_count(manuscript)}",
            f"- Required sections: {len(self.required_sections)}",
            f"- Missing required sections: {len(missing_sections)}",
            f"- Boundary phrases found: {self.boundary_phrase_count(manuscript)}",
            f"- Missing boundary phrases: {len(missing_boundary)}",
            f"- Validation metrics found: {self.validation_metric_count(manuscript)}",
            f"- Unsupported overclaims found: {len(overclaims)}",
            f"- Weak or hype phrases found: {self.weak_phrase_count(manuscript)}",
            "",
            "## Required Section Check",
            "",
            "| Section | Present |",
            "|---|---|",
        ]

        for section in self.required_sections:
            lines.append(f"| {section} | {f'## {section}' in manuscript} |")

        lines.extend(
            [
                "",
                "## Boundary Phrase Check",
                "",
                "| Boundary phrase | Present |",
                "|---|---|",
            ]
        )

        lower = manuscript.lower()
        for phrase in self.boundary_phrases:
            lines.append(f"| {phrase} | {phrase.lower() in lower} |")

        lines.extend(
            [
                "",
                "## Validation Metric Check",
                "",
                "| Metric | Present |",
                "|---|---|",
            ]
        )

        for metric in self.validation_metrics:
            lines.append(f"| {metric} | {metric.lower() in lower} |")

        lines.extend(
            [
                "",
                "## Unsupported Overclaim Check",
                "",
            ]
        )

        if overclaims:
            for claim in overclaims:
                lines.append(f"- {claim}")
        else:
            lines.append("- No unsupported overclaim lines detected.")

        lines.extend(
            [
                "",
                "## Recommendations",
                "",
            ]
        )

        for recommendation in self.recommendations:
            lines.append(f"- {recommendation}")

        lines.extend(
            [
                "",
                "## Findings",
                "",
                "| Severity | Code | Message |",
                "|---|---|---|",
            ]
        )

        for finding in findings:
            lines.append(f"| {finding.severity} | {finding.code} | {finding.message} |")

        lines.extend(
            [
                "",
                "## Audit Boundary",
                "",
                (
                    "This quality audit is internal and textual. It does not establish external validation, peer review, "
                    "biological prediction, operational use, or final manuscript readiness. Apparently even a good draft "
                    "still has to survive humans with red pens. Grim, but useful."
                ),
                "",
            ]
        )

        return "\n".join(lines)

    def section_count(self, text: str) -> int:
        return len(re.findall(r"^## ", text, flags=re.MULTILINE))

    def word_count(self, text: str) -> int:
        return len([part for part in re.split(r"\s+", text.strip()) if part])
