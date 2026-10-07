from __future__ import annotations

from typing import Dict, List

from gematria import calculate_value

SOURCES: Dict[str, dict] = {
    "JE_GEMATRIA": {
        "title": "Jewish Encyclopedia, Gematria",
        "url": "https://www.jewishencyclopedia.com/articles/6571-gematria",
        "kind": "enciclopédia histórica",
        "note": "Descreve a história e múltiplos métodos tradicionais de gematria, incluindo valor normal, menor e maior.",
    },
    "MJL_GEMATRIA": {
        "title": "My Jewish Learning, What Is Gematria?",
        "url": "https://www.myjewishlearning.com/article/gematria/",
        "kind": "referência educacional judaica",
        "note": "Resume a atribuição de valores às letras hebraicas e o uso de equivalências numéricas na interpretação.",
    },
    "SEFER_YETZIRAH": {
        "title": "Sefer Yetzirah 1:1-2, Sefaria",
        "url": "https://www.sefaria.org/Sefer_Yetzirah.1.1",
        "kind": "fonte primária da tradição mística judaica",
        "note": "Apresenta os 32 caminhos, as dez sefirot e as vinte e duas letras de fundamento.",
    },
    "MAKKOT_23B": {
        "title": "Makkot 23b-24a, Sefaria",
        "url": "https://www.sefaria.org/Makkot.23b",
        "kind": "Talmud Bavli",
        "note": "Relaciona 613 mitzvot, 365 proibições, 248 preceitos positivos e a gematria 611 de תורה.",
    },
    "MJL_CHAI": {
        "title": "My Jewish Learning, What Is the Meaning of Chai?",
        "url": "https://www.myjewishlearning.com/article/what-is-chai/",
        "kind": "referência educacional judaica",
        "note": "Explica חי como 'vida' e seu valor gemátrico 18.",
    },
    "MJL_NUMBERS": {
        "title": "My Jewish Learning, Significant Numbers in Judaism",
        "url": "https://www.myjewishlearning.com/article/judaism-numbers/",
        "kind": "referência educacional judaica",
        "note": "Apresenta números recorrentes e suas associações na tradição judaica.",
    },
    "MJL_TALLIT": {
        "title": "My Jewish Learning, The Tallit: Spiritual Significance",
        "url": "https://www.myjewishlearning.com/article/the-tallit-spiritual-significance/",
        "kind": "referência educacional judaica",
        "note": "Registra 26 como valor do Tetragrama em uma associação tradicional com tzitzit.",
    },
    "MJL_SEVENTY": {
        "title": "My Jewish Learning, Sotah 36: The seventy languages of the world",
        "url": "https://www.myjewishlearning.com/article/sotah-36/",
        "kind": "referência educacional judaica",
        "note": "Discute o uso rabínico de 70 para totalidade, incluindo nações, faces da Torah, línguas e anciãos.",
    },
    "CHABAD_72": {
        "title": "Chabad.org, 72 Names of G-d",
        "url": "https://www.chabad.org/kabbalah/article_cdo/aid/1388270/jewish/72-Names-of-G-d.htm",
        "kind": "exposição tradicional de Kabbalah",
        "note": "Expõe a tradição cabalística dos 72 tríplices derivados de Êxodo 14:19-21.",
    },
}

# Associações são deliberadamente descritas como pontos de estudo, não como previsões.
NUMBER_INTERPRETATIONS: Dict[int, List[dict]] = {
    1: [{
        "title": "Unidade",
        "interpretation": "Pode remeter ao tema da unidade divina e ao monoteísmo judaico. É uma associação religiosa geral, não uma consequência necessária de qualquer palavra que some 1.",
        "status": "contextual",
        "sources": ["MJL_NUMBERS"],
    }],
    7: [{
        "title": "Ciclo de sete",
        "interpretation": "Sete aparece de modo recorrente em estruturas rituais e temporais judaicas, especialmente na semana e no Shabat. Use como pista temática, não como significado automático.",
        "status": "contextual",
        "sources": ["MJL_NUMBERS"],
    }],
    10: [{
        "title": "Dez sefirot",
        "interpretation": "Sefer Yetzirah apresenta dez sefirot belimah. Em estudo cabalístico, o número 10 pode justificar consultar a estrutura das sefirot.",
        "status": "fonte primária",
        "sources": ["SEFER_YETZIRAH"],
    }],
    13: [{
        "title": "אחד e אהבה",
        "interpretation": "No valor padrão, אחד, 'um', e אהבה, 'amor', somam 13. A equivalência pode ser usada como pista comparativa, mas não prova uma relação textual por si só.",
        "status": "equivalência calculada",
        "sources": ["MJL_GEMATRIA"],
    }],
    18: [{
        "title": "חי, vida",
        "interpretation": "חי, chai, significa 'vida' e soma 18. Por isso, 18 adquiriu forte associação cultural judaica com vida e com doações em múltiplos de 18.",
        "status": "tradição documentada",
        "sources": ["MJL_CHAI", "MJL_NUMBERS"],
    }],
    22: [{
        "title": "Vinte e duas letras",
        "interpretation": "Sefer Yetzirah descreve vinte e duas letras de fundamento. Em contexto cabalístico, 22 pode motivar estudo da dimensão simbólica das letras hebraicas.",
        "status": "fonte primária",
        "sources": ["SEFER_YETZIRAH"],
    }],
    26: [{
        "title": "Tetragrama יהוה",
        "interpretation": "No valor padrão, יהוה soma 26: י=10, ה=5, ו=6, ה=5. É uma associação conhecida na literatura judaica e deve ser tratada com respeito religioso.",
        "status": "tradição documentada",
        "sources": ["MJL_TALLIT"],
    }],
    32: [{
        "title": "Trinta e dois caminhos de sabedoria",
        "interpretation": "Sefer Yetzirah abre com 32 caminhos e a tradição os relaciona às dez sefirot e às vinte e duas letras. לב, lev, 'coração', também soma 32 no valor padrão.",
        "status": "fonte primária + equivalência",
        "sources": ["SEFER_YETZIRAH"],
    }],
    36: [{
        "title": "Trinta e seis justos ocultos",
        "interpretation": "Há uma tradição sobre 36 justos ocultos, os lamed-vavniks. É uma associação posterior e não um princípio universal de gematria.",
        "status": "tradição posterior",
        "sources": ["MJL_NUMBERS"],
    }],
    40: [{
        "title": "Quarenta como período de transição",
        "interpretation": "O número 40 reaparece em narrativas bíblicas como os 40 dias do dilúvio, os 40 dias de Moisés no Sinai e os 40 anos no deserto. Pode sugerir investigar temas de passagem, formação ou transformação no contexto textual.",
        "status": "padrão bíblico recorrente",
        "sources": ["MJL_NUMBERS"],
    }],
    49: [{
        "title": "Sete vezes sete",
        "interpretation": "Quarenta e nove corresponde a sete ciclos de sete e aparece na contagem do Omer. É uma associação calendárica e ritual que pode ser relevante quando o contexto da frase também aponta para ciclos ou preparação.",
        "status": "tradição ritual",
        "sources": ["MJL_NUMBERS"],
    }],
    50: [{
        "title": "Shavuot e jubileu",
        "interpretation": "O quinquagésimo dia encerra a contagem do Omer em Shavuot, e o quinquagésimo ano está ligado ao yovel, jubileu. A associação é contextual e não automática.",
        "status": "tradição ritual e bíblica",
        "sources": ["MJL_NUMBERS"],
    }],
    70: [{
        "title": "Setenta e totalidade comunitária",
        "interpretation": "Fontes rabínicas usam 70 em associações com nações, línguas, anciãos e as chamadas faces da Torah. יין, vinho, e סוד, segredo, também somam 70 no valor padrão, uma equivalência tradicionalmente comentada.",
        "status": "tradição rabínica + equivalência",
        "sources": ["MJL_SEVENTY"],
    }],
    72: [{
        "title": "Setenta e dois tríplices",
        "interpretation": "Na tradição cabalística, três versos consecutivos de Êxodo 14:19-21, cada um com 72 letras, são combinados em 72 tríplices. חסד, Chesed, também soma 72 no valor padrão.",
        "status": "tradição cabalística",
        "sources": ["CHABAD_72"],
    }],
    248: [{
        "title": "Preceitos positivos",
        "interpretation": "Makkot 23b associa 248 aos mandamentos positivos na formulação rabínica dos 613 preceitos.",
        "status": "Talmud",
        "sources": ["MAKKOT_23B"],
    }],
    365: [{
        "title": "Proibições",
        "interpretation": "Makkot 23b associa 365 às proibições na formulação rabínica dos 613 preceitos e as relaciona aos dias do ano solar.",
        "status": "Talmud",
        "sources": ["MAKKOT_23B"],
    }],
    611: [{
        "title": "תורה, Torah",
        "interpretation": "Makkot 23b-24a explicita que תורה soma 611 e usa essa gematria em uma leitura sobre os 613 mandamentos.",
        "status": "Talmud",
        "sources": ["MAKKOT_23B"],
    }],
    613: [{
        "title": "613 mitzvot",
        "interpretation": "Makkot 23b apresenta a tradição de 613 mitzvot, divididas em 248 positivas e 365 proibições.",
        "status": "Talmud",
        "sources": ["MAKKOT_23B"],
    }],
}

# Pequeno léxico de termos para detectar equivalências exatas no Mispar Hechrechi.
LEXICON = [
    {"hebrew": "אחד", "translation": "um / unidade", "theme": "unidade"},
    {"hebrew": "אהבה", "translation": "amor", "theme": "amor"},
    {"hebrew": "חי", "translation": "vida", "theme": "vida"},
    {"hebrew": "יהוה", "translation": "Tetragrama, Nome de quatro letras", "theme": "Nome divino"},
    {"hebrew": "לב", "translation": "coração", "theme": "coração"},
    {"hebrew": "חכמה", "translation": "sabedoria", "theme": "Chokhmah"},
    {"hebrew": "בינה", "translation": "entendimento", "theme": "Binah"},
    {"hebrew": "חסד", "translation": "bondade / benevolência", "theme": "Chesed"},
    {"hebrew": "אור", "translation": "luz", "theme": "luz"},
    {"hebrew": "שלום", "translation": "paz / integridade", "theme": "shalom"},
    {"hebrew": "אמת", "translation": "verdade", "theme": "emet"},
    {"hebrew": "תורה", "translation": "Torah", "theme": "Torah"},
]

for item in LEXICON:
    item["value"] = calculate_value(item["hebrew"], "standard")


def interpret(value: int, method: str = "standard") -> dict:
    direct = NUMBER_INTERPRETATIONS.get(value, [])
    lexical_matches = [item for item in LEXICON if item["value"] == value] if method == "standard" else []

    heuristic = []
    if method == "standard" and value > 0 and value % 18 == 0 and value != 18:
        heuristic.append({
            "title": "Múltiplo de 18",
            "interpretation": f"{value} = {value // 18} × 18. Como 18 corresponde a חי, 'vida', a divisibilidade por 18 pode ser registrada como associação exploratória. Isso não estabelece um significado tradicional específico para {value}.",
            "status": "heurística aritmética",
            "sources": ["MJL_CHAI"],
        })

    if not direct and not lexical_matches:
        heuristic.append({
            "title": "Sem associação curada exata",
            "interpretation": "O catálogo inicial não contém uma associação textual direta para este valor. O procedimento mais seguro é procurar outras palavras hebraicas com o mesmo valor e depois verificar se existe relação contextual em fontes judaicas primárias ou comentários reconhecidos.",
            "status": "orientação metodológica",
            "sources": ["MJL_GEMATRIA", "JE_GEMATRIA"],
        })

    return {
        "value": value,
        "method": method,
        "direct": direct,
        "lexical_matches": lexical_matches,
        "heuristic": heuristic,
        "disclaimer": (
            "Gematria é uma técnica interpretativa. Igualdade numérica pode sugerir uma comparação, "
            "mas não demonstra causalidade, previsão, verdade histórica ou decisão religiosa por si só."
        ),
    }


def source_records(source_ids: List[str]) -> List[dict]:
    seen = set()
    records = []
    for source_id in source_ids:
        if source_id not in seen and source_id in SOURCES:
            records.append({"id": source_id, **SOURCES[source_id]})
            seen.add(source_id)
    return records


def collect_sources(interpretation: dict) -> List[dict]:
    ids: List[str] = ["JE_GEMATRIA", "MJL_GEMATRIA"]
    for bucket in ("direct", "heuristic"):
        for item in interpretation.get(bucket, []):
            ids.extend(item.get("sources", []))
    if interpretation.get("lexical_matches"):
        ids.append("MJL_GEMATRIA")
    return source_records(ids)
