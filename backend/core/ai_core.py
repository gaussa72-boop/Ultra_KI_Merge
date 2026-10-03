"""
Zentrale KI-Engine der Ultra-KI.
"""

from backend.services.ai_service import ask_ai


class AICore:
    """Zentrale Schnittstelle für die eigentliche KI-Verarbeitung."""

    def __init__(self):
        self.model = "OpenAI"
        self.version = "2.0.0"

    def process(self, prompt, profile=None, context=None):
        prompt = (prompt or "").strip()

        if not prompt:
            return {
                "model": self.model,
                "version": self.version,
                "response": "Bitte gib eine Nachricht ein.",
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "profile_applied": profile is not None,
            }

        response = ask_ai(
            prompt,
            context=context,
            profile=profile,
        )

        return {
            "model": self.model,
            "version": self.version,
            "response": response,
            "prompt_tokens": len(prompt.split()),
            "completion_tokens": len(response.split()),
            "profile_applied": profile is not None,
        }


def create_ai_core():
    return AICore()
