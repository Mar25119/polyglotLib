import sys
from polyglot.detect import Detector
from polyglot.text import Text

def analyze_text(text: str):
    """Анализирует текст: определяет язык и токенизирует."""
    if not text.strip():
        raise ValueError("Текст пуст")

    # Определение языка
    detector = Detector(text)
    language = detector.language

    # Токенизация
    polytext = Text(text)
    words = list(polytext.words)

    return {
        "language_name": language.name,
        "language_code": language.code,
        "confidence": round(language.confidence, 2),
        "words": words
    }

def main():
    if len(sys.argv) < 2:
        print("Использование: python polyglot_analyzer.py \"текст на любом языке\"")
        print("Пример: python polyglot_analyzer.py \"Привет, мир!\"")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])

    try:
        result = analyze_text(input_text)

        print("🔤 Анализ текста:")
        print(f"Язык: {result['language_name']} ({result['language_code']})")
        print(f"Уверенность: {result['confidence']}%")
        print(f"Слова: {result['words']}")

    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при анализе: {e}", file=sys.stderr)
        print("Убедитесь, что polyglot и модели установлены.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()