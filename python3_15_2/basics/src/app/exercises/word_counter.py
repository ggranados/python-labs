import re


def count_words(text: str) -> int:
    if not text:
        return 0
    cleaned = re.sub(r"[^\w\s]", "", text)
    words = cleaned.split()
    return len(words)


def run() -> None:
    text = input("Introduce un texto: ")
    print(f"Número de palabras: {count_words(text)}")
