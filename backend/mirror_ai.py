def mirror_response(message: str) -> str:
    message = (message or "").strip()
    if not message:
        return "Das Mirror-Modul wartet auf eine Eingabe."
    return (
        "MIRROR ANALYSE\n\n"
        f"Ausgangstext: {message}\n\n"
        "Perspektive: Betrachte den Gedanken aus mehreren Blickwinkeln "
        "und prüfe die zugrunde liegenden Annahmen."
    )
