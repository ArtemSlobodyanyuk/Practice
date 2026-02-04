def process_text(text: str) -> str:
    if not text.strip():
        return "Текст порожній"

    lines = text.splitlines()
    words = text.split()

    return (
        f"Рядків: {len(lines)}\n"
        f"Слів: {len(words)}\n"
        f"Символів: {len(text)}"
    )