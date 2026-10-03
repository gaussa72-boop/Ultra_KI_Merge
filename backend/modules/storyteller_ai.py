def create_story(prompt: str) -> str:
    prompt = (prompt or "Eine Reise durch ein leuchtendes Quantenuniversum").strip()
    return (
        "STORYTELLER\n\n"
        f"Ausgangsidee: {prompt}\n\n"
        "Kapitel 1 – Das Tor\n"
        "Ein goldenes Licht öffnete sich zwischen den Sternen. "
        "Hinter dem Tor begann eine Welt, in der Gedanken zu Bildern wurden."
    )
