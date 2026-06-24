from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from viruse_fabric.writing.bilingual_glossary import required_english_terms, required_persian_terms


@dataclass(frozen=True)
class ChapterQualityFinding:
    severity: str
    code: str
    message: str
    line_number: int | None = None
    snippet: str | None = None


@dataclass(frozen=True)
class ChapterQualityReport:
    title: str
    path: str
    language: str
    passed: bool
    findings: tuple[ChapterQualityFinding, ...]
    word_count: int
    line_count: int
    heading_count: int
    table_count: int

    @property
    def error_count(self) -> int:
        return sum(1 for finding in self.findings if finding.severity == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for finding in self.findings if finding.severity == "warning")

    @property
    def interpretation(self) -> str:
        if self.error_count:
            return "chapter quality audit failed"
        if self.warning_count:
            return "chapter quality audit passed with warnings"
        return "chapter quality audit passed"

    def render_markdown(self) -> str:
        lines = [
            f"# Chapter Quality Report: {self.title}",
            "",
            f"- Path: `{self.path}`",
            f"- Language: {self.language}",
            f"- Passed: {self.passed}",
            f"- Errors: {self.error_count}",
            f"- Warnings: {self.warning_count}",
            f"- Word count: {self.word_count}",
            f"- Line count: {self.line_count}",
            f"- Heading count: {self.heading_count}",
            f"- Table count: {self.table_count}",
            f"- Interpretation: {self.interpretation}",
            "",
            "## Findings",
            "",
        ]

        if not self.findings:
            lines.append("No findings.")
            lines.append("")
            return "\n".join(lines)

        lines.extend(
            [
                "| Severity | Code | Line | Message | Snippet |",
                "|---|---|---:|---|---|",
            ]
        )

        for finding in self.findings:
            line_number = "" if finding.line_number is None else str(finding.line_number)
            snippet = "" if finding.snippet is None else finding.snippet.replace("|", "\\|")
            lines.append(
                f"| {finding.severity} | {finding.code} | {line_number} | "
                f"{finding.message} | {snippet} |"
            )

        lines.append("")
        return "\n".join(lines)


class ChapterQualityAuditor:
    persian_required_sections: tuple[str, ...] = (
        "## ۱. مسئله",
        "## ۲. مدل نظری",
        "## ۳. لایه سناریوهای انتزاعی زیستی",
        "## ۴. نتایج",
        "## ۵. خطای مشاهده‌گر",
        "## ۶. اصلاح خوانش قصد",
        "## ۷. مرز ایمنی و انتزاع",
        "## ۸. جمع‌بندی فصل",
    )

    english_required_sections: tuple[str, ...] = (
        "## Problem",
        "## Theoretical Model",
        "## Abstract Biological Scenario Layer",
        "## Results",
        "## Observer Misreading",
        "## Intention Correction",
        "## Safety Boundary",
        "## Conclusion",
    )

    scenario_names: tuple[str, ...] = (
        "abstract_baseline",
        "coherent_viral_pattern",
        "spatial_context_break",
        "regulatory_time_disruption",
    )

    # این‌ها همان آشغال‌هایی هستند که قبلاً دیدیم. بله، حالا نگهبان دارند.
    corrupted_patterns: tuple[str, ...] = (
        "فشرده‌سازیی",
        "فشرده\u200cسازیی",
        "است..",
        "علّیی",
        "پیشرووی",
        "فشردده",
        "تتمرکز",
        "گررفتن",
        "معم مولاً",
        "چون     ن",
        "پ     پایینی",
        "ای ین",
        "خوانش،م",
        "خوانش،   معمولاً",
        "علّیی",
        "سازیی",
    )

    persian_safety_terms: tuple[str, ...] = (
        "غیرعملیاتی",
        "پاتوژن واقعی",
        "میزبان واقعی",
        "پروتکل آزمایشگاهی",
        "مداخله قابل اجرا",
    )

    english_safety_terms: tuple[str, ...] = (
        "non-operational",
        "real pathogen",
        "real host",
        "laboratory protocol",
        "executable",
    )

    minimum_word_count: int = 600

    def audit_file(self, path: Path, language: str) -> ChapterQualityReport:
        text = path.read_text(encoding="utf-8")
        return self.audit_text(text=text, path=str(path), language=language)

    def audit_text(self, text: str, path: str, language: str) -> ChapterQualityReport:
        findings: list[ChapterQualityFinding] = []

        normalized_language = language.lower().strip()
        if normalized_language not in {"fa", "en"}:
            findings.append(
                ChapterQualityFinding(
                    severity="error",
                    code="unsupported_language",
                    message=f"Unsupported language: {language}",
                )
            )

        if not text.strip():
            findings.append(
                ChapterQualityFinding(
                    severity="error",
                    code="empty_text",
                    message="Chapter text is empty.",
                )
            )

        lines = text.splitlines()
        word_count = self._word_count(text)
        heading_count = sum(1 for line in lines if line.startswith("#"))
        table_count = sum(1 for line in lines if line.startswith("|"))

        title = self._extract_title(lines)

        if word_count < self.minimum_word_count:
            findings.append(
                ChapterQualityFinding(
                    severity="warning",
                    code="short_chapter",
                    message=f"Chapter is short: {word_count} words.",
                )
            )

        if not title:
            findings.append(
                ChapterQualityFinding(
                    severity="error",
                    code="missing_title",
                    message="Chapter is missing a Markdown title.",
                )
            )

        self._check_required_sections(text, normalized_language, findings)
        self._check_required_terms(text, normalized_language, findings)
        self._check_scenarios(text, findings)
        self._check_corruption_patterns(text, findings)
        self._check_safety_boundary(text, normalized_language, findings)
        self._check_repeated_punctuation(text, findings)

        error_count = sum(1 for finding in findings if finding.severity == "error")

        return ChapterQualityReport(
            title=title or "Untitled",
            path=path,
            language=normalized_language,
            passed=error_count == 0,
            findings=tuple(findings),
            word_count=word_count,
            line_count=len(lines),
            heading_count=heading_count,
            table_count=table_count,
        )

    def _extract_title(self, lines: list[str]) -> str | None:
        for line in lines:
            if line.startswith("# "):
                return line.removeprefix("# ").strip()
        return None

    def _word_count(self, text: str) -> int:
        # برای فارسی و انگلیسی کافی است؛ قرار نیست پایان‌نامه زبان‌شناسی بسازیم.
        return len([part for part in re.split(r"\s+", text.strip()) if part])

    def _line_number_for(self, text: str, needle: str) -> int | None:
        index = text.find(needle)
        if index == -1:
            return None
        return text.count("\n", 0, index) + 1

    def _snippet_for(self, text: str, needle: str, radius: int = 60) -> str | None:
        index = text.find(needle)
        if index == -1:
            return None

        start = max(0, index - radius)
        end = min(len(text), index + len(needle) + radius)
        return text[start:end].replace("\n", " ").strip()

    def _check_required_sections(
        self,
        text: str,
        language: str,
        findings: list[ChapterQualityFinding],
    ) -> None:
        if language == "fa":
            sections = self.persian_required_sections
        elif language == "en":
            sections = self.english_required_sections
        else:
            return

        for section in sections:
            if section not in text:
                findings.append(
                    ChapterQualityFinding(
                        severity="error",
                        code="missing_section",
                        message=f"Missing required section: {section}",
                    )
                )

    def _check_required_terms(
        self,
        text: str,
        language: str,
        findings: list[ChapterQualityFinding],
    ) -> None:
        if language == "fa":
            terms = (
                "بافت علّی",
                "هندسه‌ی قیود",
                "خمیدگی علّی",
                "ژئودزیک علّی",
                "جاذب سازنده",
                "چاه تنش",
                "هدفمندی ظاهری",
                "قصدخوانی اشتباه مشاهده‌گر",
                "مرز ایمنی",
            )
            glossary_terms = required_persian_terms()
        elif language == "en":
            terms = (
                "causal fabric",
                "geometry of constraints",
                "causal curvature",
                "causal geodesic",
                "constructive attractor",
                "tension well",
                "apparent targeting",
                "observer misreading",
                "safety boundary",
            )
            glossary_terms = required_english_terms()
        else:
            return

        for term in terms:
            if term not in text:
                findings.append(
                    ChapterQualityFinding(
                        severity="warning",
                        code="missing_core_term",
                        message=f"Core term not found: {term}",
                    )
                )

        # اگر کمتر از نصف واژه‌نامه در متن دیده شود، متن از چارچوب مفهومی دور شده است.
        present_count = sum(1 for term in glossary_terms if term in text)
        if present_count < max(4, len(glossary_terms) // 2):
            findings.append(
                ChapterQualityFinding(
                    severity="warning",
                    code="low_glossary_coverage",
                    message=(
                        f"Low glossary coverage: {present_count}/"
                        f"{len(glossary_terms)} glossary terms found."
                    ),
                )
            )

    def _check_scenarios(
        self,
        text: str,
        findings: list[ChapterQualityFinding],
    ) -> None:
        for scenario_name in self.scenario_names:
            if scenario_name not in text:
                findings.append(
                    ChapterQualityFinding(
                        severity="error",
                        code="missing_scenario",
                        message=f"Missing scenario: {scenario_name}",
                    )
                )

    def _check_corruption_patterns(
        self,
        text: str,
        findings: list[ChapterQualityFinding],
    ) -> None:
        for pattern in self.corrupted_patterns:
            if pattern in text:
                findings.append(
                    ChapterQualityFinding(
                        severity="error",
                        code="corrupted_text",
                        message=f"Corrupted text pattern found: {pattern}",
                        line_number=self._line_number_for(text, pattern),
                        snippet=self._snippet_for(text, pattern),
                    )
                )

    def _check_safety_boundary(
        self,
        text: str,
        language: str,
        findings: list[ChapterQualityFinding],
    ) -> None:
        if language == "fa":
            terms = self.persian_safety_terms
        elif language == "en":
            terms = self.english_safety_terms
        else:
            return

        present_count = sum(1 for term in terms if term in text)

        if present_count < 2:
            findings.append(
                ChapterQualityFinding(
                    severity="error",
                    code="weak_safety_boundary",
                    message="Safety boundary is missing or too weak.",
                )
            )

    def _check_repeated_punctuation(
        self,
        text: str,
        findings: list[ChapterQualityFinding],
    ) -> None:
        repeated_patterns = (
            "..",
            "،،",
            ",,",
            "؛؛",
        )

        for pattern in repeated_patterns:
            if pattern in text:
                findings.append(
                    ChapterQualityFinding(
                        severity="error",
                        code="repeated_punctuation",
                        message=f"Repeated punctuation found: {pattern}",
                        line_number=self._line_number_for(text, pattern),
                        snippet=self._snippet_for(text, pattern),
                    )
                )
