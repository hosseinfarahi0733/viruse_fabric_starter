from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GlossaryEntry:
    key: str
    english: str
    persian: str
    category: str
    persian_note: str
    english_note: str


GLOSSARY: tuple[GlossaryEntry, ...] = (
    GlossaryEntry(
        key="causal_fabric",
        english="causal fabric",
        persian="بافت علّی",
        category="core theory",
        persian_note="شبکه‌ای از رخدادها، قیود، تنش‌ها و مسیرها که معنا و فشار علّی را می‌سازد.",
        english_note="A structured field of events, constraints, tensions, and paths.",
    ),
    GlossaryEntry(
        key="constraint_geometry",
        english="geometry of constraints",
        persian="هندسه‌ی قیود",
        category="core theory",
        persian_note="صورت‌بندی علیت به‌عنوان آرایش قیود، نه زنجیره‌ی خطی علت‌ها.",
        english_note="Causality understood as the arrangement of constraints rather than a linear chain.",
    ),
    GlossaryEntry(
        key="causal_curvature",
        english="causal curvature",
        persian="خمیدگی علّی",
        category="geometry",
        persian_note="تمرکز تنش، فشار و اتصال در یک گره از بافت.",
        english_note="The concentration of tension, pressure, and connectivity around an event.",
    ),
    GlossaryEntry(
        key="causal_geodesic",
        english="causal geodesic",
        persian="ژئودزیک علّی",
        category="geometry",
        persian_note="مسیر کم‌هزینه و سازگارتر درون بافت قیود.",
        english_note="A lower-cost coherent route through the constraint fabric.",
    ),
    GlossaryEntry(
        key="constructive_attractor",
        english="constructive attractor",
        persian="جاذب سازنده",
        category="attractor",
        persian_note="گره‌ای که مسیر را پایدار، کم‌هزینه و قابل ادامه می‌کند.",
        english_note="An attractor that stabilizes and supports route formation.",
    ),
    GlossaryEntry(
        key="tension_well",
        english="tension well",
        persian="چاه تنش",
        category="attractor",
        persian_note="گره پرتنشی که توجه یا فشار را متمرکز می‌کند، اما الزاماً مسیرساز نیست.",
        english_note="A high-tension node that concentrates pressure without necessarily organizing a route.",
    ),
    GlossaryEntry(
        key="strained_gateway",
        english="strained gateway",
        persian="دروازه‌ی تحت فشار",
        category="attractor",
        persian_note="نقطه عبور پرهزینه که مسیر را ممکن می‌کند، اما هدفمندی پایدار نمی‌سازد.",
        english_note="A costly passage point that allows transition without producing stable targeting.",
    ),
    GlossaryEntry(
        key="apparent_targeting",
        english="apparent targeting",
        persian="هدفمندی ظاهری",
        category="observer",
        persian_note="هدفمند دیده شدن مسیر، بدون فرض قصد درونی.",
        english_note="The appearance of targeting without attributing intention to the system.",
    ),
    GlossaryEntry(
        key="observer_misreading",
        english="observer misreading",
        persian="قصدخوانی اشتباه مشاهده‌گر",
        category="observer",
        persian_note="فشرده‌سازی مسیر هم‌راستا به داستان قصد یا انتخاب.",
        english_note="The compression of coherent route structure into a story of intention.",
    ),
    GlossaryEntry(
        key="intention_correction",
        english="intention correction",
        persian="اصلاح خوانش قصد",
        category="observer",
        persian_note="بازگرداندن تفسیر از قصد به قیود، مسیر، جاذب و فشار بافت.",
        english_note="Replacing intention-based interpretation with constraint-based interpretation.",
    ),
    GlossaryEntry(
        key="projection",
        english="projection",
        persian="برون‌فکنی مشاهده‌گر",
        category="observer",
        persian_note="تصویری که مشاهده‌گر از بافت علّی می‌سازد، نه خود بافت کامل.",
        english_note="The observer-facing image of the fabric rather than the full fabric itself.",
    ),
    GlossaryEntry(
        key="spacetime_coupling",
        english="space-time coupling",
        persian="کوپلینگ فضا-زمان",
        category="geometry",
        persian_note="اثر هم‌زمان فاصله‌ی فضایی و فاصله‌ی زمانی بر هزینه و سازگاری مسیر.",
        english_note="The joint effect of spatial and temporal distance on route cost and coherence.",
    ),
    GlossaryEntry(
        key="abstract_viral_pattern",
        english="abstract viral pattern",
        persian="الگوی ویروسی انتزاعی",
        category="biology-safe",
        persian_note="خوانش زیستی غیرعملیاتی از نقش‌های علّی، بدون پاتوژن واقعی یا دستور اجرایی.",
        english_note="A non-operational biological reading of causal roles without real pathogen detail.",
    ),
    GlossaryEntry(
        key="safety_boundary",
        english="safety boundary",
        persian="مرز ایمنی",
        category="biology-safe",
        persian_note="جداسازی توضیح مفهومی از دستور زیستی قابل اجرا.",
        english_note="The separation between conceptual explanation and executable biological instruction.",
    ),
)


def get_glossary() -> tuple[GlossaryEntry, ...]:
    return GLOSSARY


def glossary_by_key() -> dict[str, GlossaryEntry]:
    return {entry.key: entry for entry in GLOSSARY}


def required_persian_terms() -> tuple[str, ...]:
    return tuple(entry.persian for entry in GLOSSARY)


def required_english_terms() -> tuple[str, ...]:
    return tuple(entry.english for entry in GLOSSARY)


def render_glossary_markdown() -> str:
    lines = [
        "# Bilingual Glossary",
        "",
        "| Key | English | Persian | Category |",
        "|---|---|---|---|",
    ]

    for entry in GLOSSARY:
        lines.append(
            f"| {entry.key} | {entry.english} | {entry.persian} | {entry.category} |"
        )

    return "\n".join(lines) + "\n"


def render_detailed_glossary_markdown() -> str:
    lines = ["# Detailed Bilingual Glossary", ""]

    for entry in GLOSSARY:
        lines.extend(
            [
                f"## {entry.english} / {entry.persian}",
                "",
                f"- Key: `{entry.key}`",
                f"- Category: {entry.category}",
                f"- Persian note: {entry.persian_note}",
                f"- English note: {entry.english_note}",
                "",
            ]
        )

    return "\n".join(lines)
