from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple

# Mispar Hechrechi (valor padrão). Letras finais mantêm o valor da letra-base.
STANDARD_VALUES: Dict[str, int] = {
    "א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7, "ח": 8, "ט": 9,
    "י": 10, "כ": 20, "ך": 20, "ל": 30, "מ": 40, "ם": 40, "נ": 50, "ן": 50,
    "ס": 60, "ע": 70, "פ": 80, "ף": 80, "צ": 90, "ץ": 90, "ק": 100, "ר": 200,
    "ש": 300, "ת": 400,
}

# Mispar Gadol: formas finais recebem 500..900.
GADOL_VALUES = dict(STANDARD_VALUES)
GADOL_VALUES.update({"ך": 500, "ם": 600, "ן": 700, "ף": 800, "ץ": 900})

# Ordem alfabética. Formas finais recebem a posição de sua letra-base.
_BASE_ORDER = [
    "א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ", "ל", "מ", "נ", "ס", "ע", "פ", "צ", "ק", "ר", "ש", "ת"
]
ORDINAL_VALUES: Dict[str, int] = {letter: i + 1 for i, letter in enumerate(_BASE_ORDER)}
ORDINAL_VALUES.update({"ך": 11, "ם": 13, "ן": 14, "ף": 17, "ץ": 18})

# Mispar Katan: reduz cada valor padrão à unidade decimal correspondente.
KATAN_VALUES: Dict[str, int] = {
    letter: ((value - 1) % 9) + 1 for letter, value in STANDARD_VALUES.items()
}

VALUE_SYSTEMS = {
    "standard": STANDARD_VALUES,
    "gadol": GADOL_VALUES,
    "katan": KATAN_VALUES,
    "ordinal": ORDINAL_VALUES,
}

METHOD_LABELS = {
    "standard": "Mispar Hechrechi, valor padrão",
    "gadol": "Mispar Gadol, letras finais 500 a 900",
    "katan": "Mispar Katan, valor reduzido",
    "ordinal": "Mispar Siduri, valor ordinal",
}

HEBREW_RANGE_RE = re.compile(r"[\u05D0-\u05EA\u05DA\u05DD\u05DF\u05E3\u05E5]")


@dataclass(frozen=True)
class LetterValue:
    letter: str
    value: int


def strip_niqqud(text: str) -> str:
    """Remove sinais massoréticos/cantilações, preservando as letras hebraicas."""
    normalized = unicodedata.normalize("NFD", text)
    cleaned = "".join(
        ch for ch in normalized
        if not (0x0591 <= ord(ch) <= 0x05C7 and unicodedata.category(ch) in {"Mn", "Mc"})
    )
    return unicodedata.normalize("NFC", cleaned)


def normalize_hebrew(text: str) -> str:
    """Normaliza o texto e mantém conteúdo textual, removendo apenas niqqud/cantilações."""
    return strip_niqqud(text or "").strip()


def hebrew_letters(text: str) -> List[str]:
    clean = normalize_hebrew(text)
    return [ch for ch in clean if ch in STANDARD_VALUES]


def calculate_value(text: str, method: str = "standard") -> int:
    if method not in VALUE_SYSTEMS:
        raise ValueError(f"Método desconhecido: {method}")
    mapping = VALUE_SYSTEMS[method]
    return sum(mapping.get(ch, 0) for ch in normalize_hebrew(text))


def breakdown(text: str, method: str = "standard") -> List[LetterValue]:
    if method not in VALUE_SYSTEMS:
        raise ValueError(f"Método desconhecido: {method}")
    mapping = VALUE_SYSTEMS[method]
    return [LetterValue(ch, mapping[ch]) for ch in normalize_hebrew(text) if ch in mapping]


def word_values(text: str, method: str = "standard") -> List[dict]:
    clean = normalize_hebrew(text)
    words = [w for w in re.split(r"\s+", clean) if w]
    out = []
    for word in words:
        letters = [ch for ch in word if ch in VALUE_SYSTEMS[method]]
        if letters:
            out.append({
                "word": word,
                "value": sum(VALUE_SYSTEMS[method][ch] for ch in letters),
                "letters": "".join(letters),
            })
    return out


def calculate_all(text: str) -> dict:
    clean = normalize_hebrew(text)
    letters = hebrew_letters(clean)
    if not letters:
        raise ValueError(
            "Nenhuma letra hebraica foi encontrada. A gematria judaica tradicional trabalha com o alfabeto hebraico."
        )

    methods = {}
    for method in VALUE_SYSTEMS:
        methods[method] = {
            "label": METHOD_LABELS[method],
            "value": calculate_value(clean, method),
            "breakdown": [asdict(item) for item in breakdown(clean, method)],
            "words": word_values(clean, method),
        }

    ignored = [
        ch for ch in clean
        if not ch.isspace() and ch not in STANDARD_VALUES and not unicodedata.category(ch).startswith("P")
    ]

    return {
        "original": text,
        "normalized": clean,
        "hebrew_letter_count": len(letters),
        "ignored_non_hebrew": sorted(set(ignored)),
        "methods": methods,
    }
