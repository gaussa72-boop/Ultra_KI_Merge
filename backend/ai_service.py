import os

SYSTEM = "You are IONOS AI, a modular assistant. Answer clearly in German unless another language is requested."

def ask_ai(message: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return (
            "Demo-Modus: Kein OPENAI_API_KEY gesetzt.\n\n"
            f"Deine Nachricht war: {message}\n\n"
            "Setze den Schlüssel in .env, um die OpenAI Responses API zu aktivieren."
        )
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
            instructions=SYSTEM,
            input=message,
        )
        return response.output_text
    except Exception as exc:
        return f"OpenAI-Fehler: {exc}"
