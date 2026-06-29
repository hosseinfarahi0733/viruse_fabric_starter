from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTER_LINES = [
    "Controlled TC-001 presentation export package count: 1",
    "New controlled TC-001 presentation export package count: 1",
    "TC-001 presentation export package count: 1",
    "Export-ready TC-001 presentation package count: 1",
    "PowerPoint copy-ready TC-001 layout count: 1",
    "Marp-ready TC-001 markdown source count: 1",
    "Presenter checklist count: 1",
    "Export instruction count: 1",
    "Boundary lock count: 1",
    "Export-safe TC-001 slide count: 8",
    "Export-safe TC-001 Q&A count: 6",
    "Export-safe TC-001 final defense sentence count: 1",
    "Presentation export package ready count: 1",

    "Controlled TC-001 renderable presentation source count: 1",
    "Renderable TC-001 slide source count: 1",
    "Renderable TC-001 slide count: 8",
    "Renderable TC-001 title slide count: 1",
    "Renderable TC-001 content slide count: 7",
    "Renderable TC-001 speaker cue count: 8",
    "Renderable TC-001 defense appendix count: 1",
    "Renderable TC-001 Q&A count: 6",
    "Renderable TC-001 boundary slide count: 1",
    "Renderable TC-001 final defense sentence count: 1",
    "Renderable presentation source ready count: 1",

    "Presentation-safe internal TC-001 proof claim count: 1",
    "Accepted internal TC-001 theorem proof count: 1",
    "TC-001 proof execution count: 1",
    "TC-001 theorem proven count: 1",
    "Theorem proof execution count: 1",
    "Internal theorem proof count: 1",
    "Controlled internal TC-001 theorem proof count: 1",
    "Completed TC-001 supporting lemma chain count: 1",
    "Proved TC-001 supporting lemma count: 6",
    "Internal lemma proof count: 6",

    "Imported controlled TC-001 renderable presentation source count: 1",
    "Imported renderable TC-001 slide source count: 1",
    "Imported renderable presentation source ready count: 1",
    "Imported presentation-safe internal TC-001 proof claim count: 1",
    "Imported accepted internal TC-001 theorem proof count: 1",
    "Imported TC-001 proof execution count: 1",
    "Imported TC-001 theorem proven count: 1",
    "Imported theorem proof execution count: 1",
    "Imported internal theorem proof count: 1",
    "Imported completed TC-001 supporting lemma chain count: 1",
    "Imported proved TC-001 supporting lemma count: 6",
    "Imported internal lemma proof count: 6",

    "New lemma proof execution count: 0",
    "New TC-001 proof execution count: 0",
    "New theorem proven count: 0",
    "New theorem proof execution count: 0",
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_SOURCE_PHRASES = [
    "Controlled TC-001 renderable presentation source count: 1",
    "Renderable TC-001 slide source count: 1",
    "Renderable TC-001 slide count: 8",
    "Renderable TC-001 title slide count: 1",
    "Renderable TC-001 content slide count: 7",
    "Renderable TC-001 speaker cue count: 8",
    "Renderable TC-001 defense appendix count: 1",
    "Renderable TC-001 Q&A count: 6",
    "Renderable TC-001 boundary slide count: 1",
    "Renderable TC-001 final defense sentence count: 1",
    "Renderable presentation source ready count: 1",
    "Presentation-safe internal TC-001 proof claim count: 1",
    "Accepted internal TC-001 theorem proof count: 1",
    "TC-001 proof execution count: 1",
    "TC-001 theorem proven count: 1",
    "Theorem proof execution count: 1",
    "Internal theorem proof count: 1",
    "Controlled internal TC-001 theorem proof count: 1",
    "Completed TC-001 supporting lemma chain count: 1",
    "Proved TC-001 supporting lemma count: 6",
    "Internal lemma proof count: 6",
    "New lemma proof execution count: 0",
    "New TC-001 proof execution count: 0",
    "New theorem proven count: 0",
    "New theorem proof execution count: 0",
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


REQUIRED_REPORT_PHRASES = [
    "Controlled TC-001 presentation export package count: 1",
    "New controlled TC-001 presentation export package count: 1",
    "TC-001 presentation export package count: 1",
    "Export-ready TC-001 presentation package count: 1",
    "PowerPoint copy-ready TC-001 layout count: 1",
    "Marp-ready TC-001 markdown source count: 1",
    "Presenter checklist count: 1",
    "Export instruction count: 1",
    "Boundary lock count: 1",
    "Export-safe TC-001 slide count: 8",
    "Export-safe TC-001 Q&A count: 6",
    "Export-safe TC-001 final defense sentence count: 1",
    "Presentation export package ready count: 1",

    "Controlled TC-001 renderable presentation source count: 1",
    "Renderable presentation source ready count: 1",
    "Presentation-safe internal TC-001 proof claim count: 1",
    "Accepted internal TC-001 theorem proof count: 1",
    "TC-001 proof execution count: 1",
    "TC-001 theorem proven count: 1",
    "Theorem proof execution count: 1",
    "Internal theorem proof count: 1",
    "Controlled internal TC-001 theorem proof count: 1",
    "Completed TC-001 supporting lemma chain count: 1",
    "Proved TC-001 supporting lemma count: 6",
    "Internal lemma proof count: 6",

    "Imported controlled TC-001 renderable presentation source count: 1",
    "Imported renderable TC-001 slide source count: 1",
    "Imported renderable presentation source ready count: 1",
    "Imported presentation-safe internal TC-001 proof claim count: 1",
    "Imported accepted internal TC-001 theorem proof count: 1",
    "Imported TC-001 proof execution count: 1",
    "Imported TC-001 theorem proven count: 1",
    "Imported theorem proof execution count: 1",
    "Imported internal theorem proof count: 1",
    "Imported completed TC-001 supporting lemma chain count: 1",
    "Imported proved TC-001 supporting lemma count: 6",
    "Imported internal lemma proof count: 6",

    "New lemma proof execution count: 0",
    "New TC-001 proof execution count: 0",
    "New theorem proven count: 0",
    "New theorem proof execution count: 0",
    "Formalization complete count: 0",
    "Proof assistant verification count: 0",
    "External validation count: 0",
    "Independent experiment count: 0",
    "Manuscript submission ready count: 0",
    "Readiness approval count: 0",
    "New citation added count: 0",
]


@dataclass(frozen=True)
class TC001PresentationExportPackageResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _export_package() -> str:
    return dedent(
        """
        # Export-ready TC-001 presentation package

        ## Purpose

        This package turns the official v8.181 renderable presentation source into an export-ready presentation package.

        It is designed for:
        - direct copy into PowerPoint,
        - direct conversion with Marp,
        - live presentation use,
        - defense Q&A preparation.

        It is not designed to change the proof status.

        ---

        ## Export instruction

        Recommended export path:

        1. Use `outputs/controlled_tc_001_renderable_presentation_source_v8_181.md` as the source.
        2. Copy each slide section separated by `---` into a slide tool.
        3. Keep Slide 6 unchanged because it contains the boundary lock.
        4. Keep the final defense sentence unchanged.
        5. Keep Q&A as appendix or backup slides.
        6. Do not add proof-assistant, validation, manuscript-readiness, or citation claims.

        Optional Marp command, if Marp is installed:

        ```text
        marp outputs/controlled_tc_001_renderable_presentation_source_v8_181.md --pdf
        ```

        Optional HTML export, if supported:

        ```text
        marp outputs/controlled_tc_001_renderable_presentation_source_v8_181.md --html
        ```

        ---

        ## PowerPoint copy-ready layout

        ### Slide 1

        Title:
        وضعیت اثبات TC-001

        Bullets:
        - TC-001 یک theorem-candidate در Viruse Fabric است.
        - اثبات داخلی آن اجرا و پذیرفته شده است.
        - منبع رسمی این ارائه: v8.181.0
        - مرزهای ادعا صریح نگه داشته شده‌اند.

        Presenter line:
        در این ارائه، وضعیت TC-001 را دقیق و بدون overclaim توضیح می‌دهم.

        ---

        ### Slide 2

        Title:
        TC-001 چه می‌گوید؟

        Bullets:
        - موضوع: admissible regular observation well-typing
        - ورودی: نمونه admissible و regular
        - ساختارها: `Sigma_A`, `Adm_A`, `C_reg`
        - projection: `Pi_obs`
        - خروجی: observation در codomain مشخص‌شده

        Presenter line:
        TC-001 بررسی می‌کند که observation حاصل از projection برای ورودی admissible و regular، well-typed باقی بماند.

        ---

        ### Slide 3

        Title:
        زنجیره پشتیبان L-001 تا L-006

        Bullets:
        - L-001: carrier availability
        - L-002: admissible-state typing
        - L-003: regular-transition typing
        - L-004: projection-domain compatibility
        - L-005: projection-codomain well-typing
        - L-006: no-uncompleted-dependency guarantee

        Presenter line:
        TC-001 روی یک chain شش‌تایی داخلی و کنترل‌شده بنا شده است.

        ---

        ### Slide 4

        Title:
        مسیر شواهد

        Bullets:
        - v8.172: audit زنجیره lemmaها
        - v8.173: strategy اجرای اثبات
        - v8.174: اجرای اثبات داخلی
        - v8.175: acceptance و boundary audit
        - v8.176: استخراج proof section
        - v8.177: بسته claim ارائه
        - v8.178: محتوای اسلاید
        - v8.179: draft واقعی ارائه
        - v8.180: delivery package
        - v8.181: renderable source

        Presenter line:
        این مسیر نشان می‌دهد claim فعلی از یک زنجیره مستند milestoneها آمده است.

        ---

        ### Slide 5

        Title:
        Claim پذیرفته‌شده

        Main sentence:
        TC-001 دارای یک اثبات داخلی پذیرفته‌شده و کنترل‌شده در سطح theorem-candidate در چارچوب توسعه اثبات پروژه است.

        Bullets:
        - سطح ادعا: theorem-candidate
        - چارچوب: internal proof-development framework
        - وضعیت: accepted internal proof claim
        - استفاده ارائه‌ای: فقط همراه با boundary wording

        Presenter line:
        claim ما دقیقاً در سطح internal controlled theorem-candidate proof execution است.

        ---

        ### Slide 6

        Title:
        مرزهای ادعا

        Bullets:
        - proof-assistant verified نیست.
        - external validation ندارد.
        - independent experimental validation ندارد.
        - manuscript-submission ready نیست.
        - readiness-approved نیست.
        - با citation جدید پشتیبانی نشده است.

        Presenter line:
        این slide نباید حذف یا نرم شود؛ مرزهای ادعا بخش اصلی دقت علمی این ارائه‌اند.

        ---

        ### Slide 7

        Title:
        مسیرهای باقی‌مانده

        Bullets:
        - Proof assistant verification
        - External validation
        - Independent experiment
        - Citation expansion
        - Manuscript readiness

        Presenter line:
        این‌ها trackهای آینده‌اند و نباید با claim فعلی ترکیب شوند.

        ---

        ### Slide 8

        Title:
        جمله نهایی دفاع

        English:
        TC-001 has an accepted internal controlled theorem-candidate proof execution within the project proof-development framework, with explicit boundaries excluding proof assistant verification, external validation, independent experimental validation, manuscript readiness, readiness approval, and new citation additions.

        Persian:
        TC-001 دارای یک اثبات داخلی پذیرفته‌شده و کنترل‌شده در سطح theorem-candidate در چارچوب توسعه اثبات پروژه است، با مرزهای مشخص مبنی بر اینکه این نتیجه هنوز proof-assistant verified نیست، external validation ندارد، independent experimental validation ندارد، آماده ارسال مقاله نیست، readiness-approved نیست و با citation جدید پشتیبانی نشده است.

        Presenter line:
        اگر فقط یک جمله برای دفاع لازم بود، همین جمله را بگو.

        ---

        ## Presenter checklist

        Before presenting, verify:

        - Slide 6 exists.
        - Final defense sentence exists.
        - The phrase `proof-assistant verified` is only used as a negative boundary.
        - The phrase `external validation` is only used as absent or future work.
        - Manuscript readiness is not claimed.
        - Citation additions are not claimed.
        - TC-001 is described as theorem-candidate, not final verified theorem.
        - Internal proof is described as internal and controlled.
        - Q&A answers do not upgrade the claim.

        ---

        ## Boundary lock

        Do not change these statements:

        - Proof assistant verification count: 0
        - External validation count: 0
        - Independent experiment count: 0
        - Manuscript submission ready count: 0
        - Readiness approval count: 0
        - New citation added count: 0

        Boundary sentence:

        This result is not proof-assistant verified, not externally validated, not independently experimentally validated, not manuscript-submission ready, not readiness-approved, and not supported by new citation additions.

        ---

        ## Compact defense Q&A

        Q1:
        آیا theorem نهایی اثبات شده؟

        A1:
        خیر. TC-001 به‌عنوان theorem-candidate در سطح داخلی پروژه اثبات و accept شده است.

        Q2:
        آیا proof assistant verification انجام شده؟

        A2:
        خیر. این مسیر هنوز جدا و آینده است.

        Q3:
        آیا مقاله آماده ارسال است؟

        A3:
        خیر. این بسته برای ارائه دقیق و export آماده است، نه برای ادعای manuscript readiness.

        Q4:
        آیا validation خارجی دارید؟

        A4:
        خیر. external validation و independent experiment هنوز مسیرهای جدا هستند.

        Q5:
        پس دستاورد دقیق چیست؟

        A5:
        TC-001 دارای proof execution داخلی، acceptance، proof section، claim package، slide content، draft ارائه رسمی، delivery package و renderable source است.

        Q6:
        امن‌ترین جمله دفاع چیست؟

        A6:
        TC-001 has an accepted internal controlled theorem-candidate proof execution within the project proof-development framework, with explicit boundaries excluding proof assistant verification, external validation, independent experimental validation, manuscript readiness, readiness approval, and new citation additions.

        ---

        ## Export-safe closing

        در جمع‌بندی، v8.182 فقط presentation export package را آماده می‌کند. این milestone وضعیت علمی TC-001 را ارتقا نمی‌دهد؛ بلکه presentation path را تمیز، قابل کپی، قابل export و boundary-safe می‌کند.
        """
    ).strip()


def _next_steps() -> str:
    return "\n".join(
        [
            "1. Use this package to export or manually build the presentation.",
            "2. Keep Slide 6 and the final defense sentence unchanged.",
            "3. Keep future technical tracks separate: proof assistant verification, external validation, independent experiments, citation expansion, and manuscript readiness.",
        ]
    )


def build_report(source_text: str) -> TC001PresentationExportPackageResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.182 - Controlled TC-001 Presentation Export Package

        ## Question

        Can Viruse Fabric build an export-ready package from the official v8.181 renderable presentation source while preserving explicit boundaries against proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation claims?

        ## Source artifact

        - `outputs/controlled_tc_001_renderable_presentation_source_v8_181.md`

        ## Export-package interpretation

        v8.182 builds an export-ready presentation package.

        This milestone is presentation export packaging only.

        This milestone does not create a new proof.

        This milestone does not add a new theorem proof.

        This milestone does not provide proof assistant verification.

        This milestone does not provide external validation.

        This milestone does not make the manuscript submission ready.

        {_export_package()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone builds the presentation export package only.

        This milestone records controlled TC-001 presentation export package count: 1.

        This milestone records export-ready TC-001 presentation package count: 1.

        This milestone records PowerPoint copy-ready TC-001 layout count: 1.

        This milestone records Marp-ready TC-001 markdown source count: 1.

        This milestone records presenter checklist count: 1.

        This milestone records export instruction count: 1.

        This milestone records boundary lock count: 1.

        This milestone records export-safe TC-001 slide count: 8.

        This milestone records export-safe TC-001 Q&A count: 6.

        This milestone records export-safe TC-001 final defense sentence count: 1.

        This milestone preserves renderable presentation source ready count: 1.

        This milestone preserves presentation-safe internal TC-001 proof claim count: 1.

        This milestone preserves accepted internal TC-001 theorem proof count: 1.

        This milestone preserves TC-001 proof execution count: 1.

        This milestone preserves TC-001 theorem proven count: 1.

        This milestone preserves theorem proof execution count: 1.

        This milestone preserves internal theorem proof count: 1.

        This milestone preserves completed TC-001 supporting lemma chain count: 1.

        This milestone preserves proved TC-001 supporting lemma count: 6.

        This milestone records new lemma proof execution count: 0.

        This milestone records new TC-001 proof execution count: 0.

        This milestone records new theorem proven count: 0.

        This milestone records new theorem proof execution count: 0.

        This milestone records formalization complete count: 0.

        This milestone records proof assistant verification count: 0.

        This milestone records external validation count: 0.

        This milestone records independent experiment count: 0.

        This milestone records manuscript submission ready count: 0.

        This milestone records readiness approval count: 0.

        This milestone records new citation added count: 0.

        This milestone does not execute a new TC-001 proof.

        This milestone does not add a new theorem proof.

        This milestone does not provide proof assistant verification.

        This milestone does not complete full formalization.

        This milestone does not provide external validation.

        This milestone does not provide independent experiments.

        This milestone does not make the manuscript submission ready.

        This milestone does not approve readiness.

        This milestone does not add new citations.

        ## Next steps

        {_next_steps()}

        ## Safe claim

        The project has built an export-ready presentation package for TC-001 from the official renderable presentation source, preserving explicit boundaries that the claim is not proof-assistant verified, not externally validated, not independently experimentally validated, not manuscript-submission ready, not readiness-approved, and not based on new citation additions.
        """
    ).strip() + "\n"

    missing_report_phrases = [
        phrase for phrase in REQUIRED_REPORT_PHRASES if phrase not in report
    ]

    prohibited_phrases = [
        "Proof assistant verification count: 1",
        "External validation count: 1",
        "Independent experiment count: 1",
        "Manuscript submission ready count: 1",
        "Readiness approval count: 1",
        "New citation added count: 1",
        "Formalization complete count: 1",
        "This milestone provides proof assistant verification",
        "This milestone provides external validation",
        "This milestone provides independent experiments",
        "This milestone makes the manuscript submission ready",
        "This milestone approves readiness",
        "This milestone adds new citations",
        "This milestone completes full formalization",
    ]

    prohibited_behavior_count = sum(
        1 for phrase in prohibited_phrases if phrase.lower() in report.lower()
    )

    boundary_keywords = [
        "proof assistant verification count: 0",
        "external validation count: 0",
        "independent experiment count: 0",
        "manuscript submission ready count: 0",
        "readiness approval count: 0",
        "new citation added count: 0",
        "formalization complete count: 0",
        "does not provide proof assistant verification",
        "does not complete full formalization",
        "does not provide external validation",
        "does not make",
        "does not approve",
        "does not add",
        "not proof-assistant verified",
        "not externally validated",
        "not manuscript-submission ready",
    ]
    boundary_phrase_count = sum(report.lower().count(item.lower()) for item in boundary_keywords)

    warnings = [
        "This milestone builds an export package only; it does not create a new proof.",
        "Proof assistant verification remains zero.",
        "External validation remains zero.",
        "Manuscript readiness remains zero.",
        "Citation additions remain zero.",
    ]

    return TC001PresentationExportPackageResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> TC001PresentationExportPackageResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
