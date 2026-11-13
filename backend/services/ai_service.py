import os

SYSTEM = """Du bist die zentrale Ultra-KI.
Antworte standardmäßig auf Deutsch, außer der Benutzer verlangt eine andere Sprache.

Du kannst unterschiedliche interne Module verwenden:
- Quantum AI: symbolische Zustandsanalyse
- Meta AI: Code- und Python-Analyse
- Mirror AI: Perspektiven- und Annahmenanalyse
- Storyteller AI: kreative Geschichten
- Personality Engine: Antwortstil und Persönlichkeit
- Training Engine: Kontext und Weiterentwicklung

Diese Module sind Hilfssysteme. Die eigentliche Sprachgenerierung erfolgt über das konfigurierte OpenAI-Modell.
Antworte klar, hilfreich und nachvollziehbar.
"""


def _client():
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    return OpenAI(api_key=api_key)


def ask_ai(message: str, context=None, profile=None) -> str:
    message = (message or "").strip()
    if not message:
        raise RuntimeError("Bitte gib eine Nachricht ein.")
    if os.getenv("AI_ENABLED", "true").strip().lower() != "true":
        raise RuntimeError("Die KI ist mit AI_ENABLED=false deaktiviert.")
    client = _client()
    if client is None:
        raise RuntimeError("OPENAI_API_KEY fehlt in den Render Environment Variables.")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()
    instructions = SYSTEM
    if profile:
        instructions += f"\nBenutzerprofil:\n{profile}"
    if context:
        instructions += f"\nKontext:\n{context}"
    try:
        response = client.responses.create(model=model, instructions=instructions, input=message)
        return response.output_text or "Die KI hat keine Textantwort zurückgegeben."
    except Exception as exc:
        raise ValueError("OpenAI-Anfrage fehlgeschlagen. Prüfe API-Key, Modellfreigabe und Guthaben.") from exc
