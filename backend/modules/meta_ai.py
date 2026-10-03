import ast


def validate_python(code: str):
    try:
        ast.parse(code)
        return {"ok": True, "message": "Python-Syntax ist gültig."}
    except SyntaxError as exc:
        return {"ok": False, "message": f"Syntaxfehler: {exc}"}


def improve_python_code(code: str):
    if not code.strip():
        return {"ok": False, "message": "Kein Code übergeben.", "code": ""}

    result = validate_python(code)

    return {
        "ok": result["ok"],
        "message": result["message"],
        "code": code,
        "next_step": "LLM-Review kann nach erfolgreicher Syntaxprüfung ergänzt werden.",
    }


class MetaAI:
    """Meta-KI für Codeanalyse und Python-Syntaxprüfung."""

    name = "Meta AI"

    def validate(self, code: str):
        return validate_python(code)

    def analyze(self, code: str):
        return improve_python_code(code)

    def improve(self, code: str):
        return improve_python_code(code)

    def process(self, code: str):
        return self.analyze(code)
