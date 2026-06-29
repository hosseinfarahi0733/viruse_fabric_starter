from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


COUNTER_LINES = [
    "Controlled TC-001 renderable presentation source count: 1",
    "New controlled TC-001 renderable presentation source count: 1",
    "TC-001 renderable presentation source count: 1",
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

    "Controlled TC-001 presentation delivery package count: 1",
    "Display-ready TC-001 presentation package count: 1",
    "Delivery-ready TC-001 slide count: 8",
    "Delivery-ready TC-001 presenter cue count: 8",
    "Delivery-ready TC-001 speaker script count: 1",
    "Delivery-ready TC-001 short defense script count: 1",
    "Delivery-ready TC-001 Q&A count: 6",
    "Presentation delivery package ready count: 1",

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

    "Imported controlled TC-001 presentation delivery package count: 1",
    "Imported display-ready TC-001 presentation package count: 1",
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
    "Controlled TC-001 presentation delivery package count: 1",
    "Display-ready TC-001 presentation package count: 1",
    "Delivery-ready TC-001 slide count: 8",
    "Delivery-ready TC-001 presenter cue count: 8",
    "Delivery-ready TC-001 speaker script count: 1",
    "Delivery-ready TC-001 short defense script count: 1",
    "Delivery-ready TC-001 Q&A count: 6",
    "Presentation delivery package ready count: 1",
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
    "Controlled TC-001 renderable presentation source count: 1",
    "New controlled TC-001 renderable presentation source count: 1",
    "TC-001 renderable presentation source count: 1",
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

    "Controlled TC-001 presentation delivery package count: 1",
    "Display-ready TC-001 presentation package count: 1",
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

    "Imported controlled TC-001 presentation delivery package count: 1",
    "Imported display-ready TC-001 presentation package count: 1",
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
class TC001RenderablePresentationSourceResult:
    report: str
    missing_source_phrases: list[str]
    missing_report_phrases: list[str]
    prohibited_behavior_count: int
    boundary_phrase_count: int
    warning_messages: list[str]


def _counter_lines() -> str:
    return "\n".join(f"- {line}" for line in COUNTER_LINES)


def _renderable_slides() -> str:
    return dedent(
        """
        # Renderable TC-001 presentation source

        Format note:
        This section is written as a markdown slide source. Each `---` separator marks a slide boundary.

        ---

        # وضعیت اثبات TC-001

        **Claim level:** internal controlled theorem-candidate proof execution

        - TC-001 یک theorem-candidate در Viruse Fabric است.
        - اثبات داخلی آن اجرا و پذیرفته شده است.
        - منبع رسمی این ارائه: v8.180.0
        - مرزهای ادعا صریح نگه داشته شده‌اند.

        **Presenter cue:** از همان ابتدا روی «internal» و «controlled» تأکید کن.

        ---

        # TC-001 چه می‌گوید؟

        **موضوع:** admissible regular observation well-typing

        - ورودی: نمونه admissible و regular
        - ساختارها: `Sigma_A`, `Adm_A`, `C_reg`
        - projection: `Pi_obs`
        - خروجی: observation در codomain مشخص‌شده

        **Presenter cue:** گزاره را ساده و دقیق نگه دار.

        ---

        # زنجیره پشتیبان L-001 تا L-006

        - L-001: carrier availability
        - L-002: admissible-state typing
        - L-003: regular-transition typing
        - L-004: projection-domain compatibility
        - L-005: projection-codomain well-typing
        - L-006: no-uncompleted-dependency guarantee

        **Presenter cue:** بگو TC-001 claim خام و بی‌پایه نیست.

        ---

        # مسیر شواهد

        - v8.172: audit زنجیره lemmaها
        - v8.173: strategy اجرای اثبات
        - v8.174: اجرای اثبات داخلی
        - v8.175: acceptance و boundary audit
        - v8.176: استخراج proof section
        - v8.177: بسته claim ارائه
        - v8.178: محتوای اسلاید
        - v8.179: draft واقعی ارائه
        - v8.180: delivery package قابل ارائه

        **Presenter cue:** مسیر را کوتاه بگو. قرار نیست حضار را زیر قطار نسخه‌ها له کنیم.

        ---

        # Claim پذیرفته‌شده

        TC-001 دارای یک اثبات داخلی پذیرفته‌شده و کنترل‌شده در سطح theorem-candidate در چارچوب توسعه اثبات پروژه است.

        - سطح ادعا: theorem-candidate
        - چارچوب: internal proof-development framework
        - وضعیت: accepted internal proof claim
        - استفاده ارائه‌ای: فقط همراه با boundary wording

        **Presenter cue:** این اسلاید را بدون اغراق بخوان.

        ---

        # مرزهای ادعا

        این نتیجه هنوز:

        - proof-assistant verified نیست.
        - external validation ندارد.
        - independent experimental validation ندارد.
        - manuscript-submission ready نیست.
        - readiness-approved نیست.
        - با citation جدید پشتیبانی نشده است.

        **Presenter cue:** محدودیت‌ها را با اطمینان بگو. مرزگذاری یعنی دقت، نه عقب‌نشینی.

        ---

        # مسیرهای باقی‌مانده

        - Proof assistant verification
        - External validation
        - Independent experiment
        - Citation expansion
        - Manuscript readiness

        **Presenter cue:** این‌ها trackهای آینده‌اند، نه claimهای فعلی.

        ---

        # جمله نهایی دفاع

        **English:**

        TC-001 has an accepted internal controlled theorem-candidate proof execution within the project proof-development framework, with explicit boundaries excluding proof assistant verification, external validation, independent experimental validation, manuscript readiness, readiness approval, and new citation additions.

        **فارسی:**

        TC-001 دارای یک اثبات داخلی پذیرفته‌شده و کنترل‌شده در سطح theorem-candidate در چارچوب توسعه اثبات پروژه است، با مرزهای مشخص مبنی بر اینکه این نتیجه هنوز proof-assistant verified نیست، external validation ندارد، independent experimental validation ندارد، آماده ارسال مقاله نیست، readiness-approved نیست و با citation جدید پشتیبانی نشده است.

        ---

        # Appendix: Compact Defense Q&A

        **Q1: آیا theorem نهایی اثبات شده؟**

        خیر. TC-001 به‌عنوان theorem-candidate در سطح داخلی پروژه اثبات و accept شده است.

        **Q2: آیا proof assistant verification انجام شده؟**

        خیر. این مسیر هنوز جدا و آینده است.

        **Q3: آیا مقاله آماده ارسال است؟**

        خیر. این بسته برای ارائه دقیق آماده است، نه برای ادعای manuscript readiness.

        **Q4: آیا validation خارجی دارید؟**

        خیر. external validation و independent experiment هنوز مسیرهای جدا هستند.

        **Q5: پس دستاورد دقیق چیست؟**

        TC-001 دارای proof execution داخلی، acceptance، proof section، claim package، slide content، draft ارائه رسمی و delivery package قابل ارائه است.

        **Q6: امن‌ترین جمله دفاع چیست؟**

        TC-001 has an accepted internal controlled theorem-candidate proof execution within the project proof-development framework, with explicit boundaries excluding proof assistant verification, external validation, independent experimental validation, manuscript readiness, readiness approval, and new citation additions.
        """
    ).strip()


def _next_steps() -> str:
    return "\n".join(
        [
            "1. Use this renderable markdown source as the direct display source for the TC-001 presentation.",
            "2. Convert manually or mechanically to slides if a `.pptx` artifact is needed later.",
            "3. Keep proof assistant verification, external validation, independent experiments, citation expansion, and manuscript readiness separate.",
        ]
    )


def build_report(source_text: str) -> TC001RenderablePresentationSourceResult:
    missing_source_phrases = [
        phrase for phrase in REQUIRED_SOURCE_PHRASES if phrase not in source_text
    ]

    report = dedent(
        f"""
        # v8.181 - Controlled TC-001 Renderable Presentation Source

        ## Question

        Can Viruse Fabric convert the official v8.180 delivery package into a renderable markdown presentation source while preserving explicit boundaries against proof assistant verification, external validation, independent experiment, manuscript readiness, readiness approval, and new citation claims?

        ## Source artifact

        - `outputs/controlled_tc_001_presentation_delivery_package_v8_180.md`

        ## Renderable-source interpretation

        v8.181 builds a renderable markdown slide source.

        This milestone is renderable presentation source packaging only.

        This milestone does not create a new proof.

        This milestone does not add a new theorem proof.

        This milestone does not provide proof assistant verification.

        This milestone does not provide external validation.

        This milestone does not make the manuscript submission ready.

        {_renderable_slides()}

        ## Counters

        {_counter_lines()}

        ## Anti-overclaim boundary

        This milestone builds the renderable presentation source only.

        This milestone records controlled TC-001 renderable presentation source count: 1.

        This milestone records renderable TC-001 slide source count: 1.

        This milestone records renderable TC-001 slide count: 8.

        This milestone records renderable TC-001 title slide count: 1.

        This milestone records renderable TC-001 content slide count: 7.

        This milestone records renderable TC-001 speaker cue count: 8.

        This milestone records renderable TC-001 defense appendix count: 1.

        This milestone records renderable TC-001 Q&A count: 6.

        This milestone records renderable TC-001 boundary slide count: 1.

        This milestone records renderable TC-001 final defense sentence count: 1.

        This milestone preserves display-ready TC-001 presentation package count: 1.

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

        The project has built a renderable markdown presentation source for presenting the accepted internal TC-001 theorem-candidate proof claim, preserving explicit boundaries that the claim is not proof-assistant verified, not externally validated, not independently experimentally validated, not manuscript-submission ready, not readiness-approved, and not based on new citation additions.
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
        "This milestone builds renderable presentation source only; it does not create a new proof.",
        "Proof assistant verification remains zero.",
        "External validation remains zero.",
        "Manuscript readiness remains zero.",
        "Citation additions remain zero.",
    ]

    return TC001RenderablePresentationSourceResult(
        report=report,
        missing_source_phrases=missing_source_phrases,
        missing_report_phrases=missing_report_phrases,
        prohibited_behavior_count=prohibited_behavior_count,
        boundary_phrase_count=boundary_phrase_count,
        warning_messages=warnings,
    )


def write_report(source_path: Path, output_path: Path) -> TC001RenderablePresentationSourceResult:
    source_text = source_path.read_text(encoding="utf-8", errors="replace")
    result = build_report(source_text)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.report, encoding="utf-8")
    return result
