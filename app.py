from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from gematria import METHOD_LABELS, VALUE_SYSTEMS, calculate_all
from interpretations import SOURCES, collect_sources, interpret

app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "index.html",
        methods=METHOD_LABELS,
        sources=SOURCES,
    )


@app.post("/api/calculate")
def api_calculate():
    payload = request.get_json(silent=True) or {}
    text = str(payload.get("text", ""))
    method = str(payload.get("method", "standard"))

    if not text.strip():
        return jsonify({"ok": False, "error": "Digite uma palavra ou frase em hebraico."}), 400
    if method not in VALUE_SYSTEMS:
        return jsonify({"ok": False, "error": "Método de gematria inválido."}), 400
    if len(text) > 5000:
        return jsonify({"ok": False, "error": "Texto muito longo. Limite: 5.000 caracteres."}), 400

    try:
        result = calculate_all(text)
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400

    selected_value = result["methods"][method]["value"]
    study = interpret(selected_value, method)
    sources = collect_sources(study)

    return jsonify({
        "ok": True,
        "result": result,
        "selected_method": method,
        "selected_method_label": METHOD_LABELS[method],
        "interpretation": study,
        "sources": sources,
    })


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
