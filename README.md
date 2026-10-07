# Gematria Flask

Aplicação Flask para cálculo exploratório de gematria em texto hebraico.

## Métodos implementados

- Mispar Hechrechi: valor padrão das letras.
- Mispar Gadol: letras finais ך ם ן ף ץ recebem 500, 600, 700, 800 e 900.
- Mispar Katan: redução de cada letra à unidade decimal correspondente.
- Mispar Siduri: posição ordinal da letra no alfabeto hebraico.

O sistema remove niqqud e cantilações antes do cálculo.

## Interpretação

O módulo `interpretations.py` separa:

1. associações documentadas para números específicos;
2. equivalências exatas com um pequeno léxico hebraico;
3. heurísticas claramente identificadas;
4. referências para estudo posterior.

A aplicação não trata gematria como previsão, prova teológica ou decisão haláchica.

## Executar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Acesse `http://localhost:8000`.

## Docker

```bash
docker compose up --build
```

A aplicação ficará disponível na porta 8000.

## Testes

```bash
pytest -q
```

## Fontes usadas como base

- Jewish Encyclopedia, Gematria: https://www.jewishencyclopedia.com/articles/6571-gematria
- My Jewish Learning, What Is Gematria?: https://www.myjewishlearning.com/article/gematria/
- Sefer Yetzirah 1:1-2, Sefaria: https://www.sefaria.org/Sefer_Yetzirah.1.1
- Makkot 23b-24a, Sefaria: https://www.sefaria.org/Makkot.23b
- My Jewish Learning, What Is the Meaning of Chai?: https://www.myjewishlearning.com/article/what-is-chai/
- My Jewish Learning, Significant Numbers in Judaism: https://www.myjewishlearning.com/article/judaism-numbers/
- My Jewish Learning, The Tallit: Spiritual Significance: https://www.myjewishlearning.com/article/the-tallit-spiritual-significance/

## Limitação importante

Gematria judaica tradicional trabalha com letras hebraicas. Transliterar automaticamente português ou inglês para hebraico acrescentaria decisões linguísticas arbitrárias. Por isso, esta versão exige texto hebraico para o cálculo principal.
- My Jewish Learning, Sotah 36: https://www.myjewishlearning.com/article/sotah-36/
- Chabad.org, 72 Names of G-d: https://www.chabad.org/kabbalah/article_cdo/aid/1388270/jewish/72-Names-of-G-d.htm
