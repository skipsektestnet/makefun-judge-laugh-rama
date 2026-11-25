#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke.

Writes the joke exactly as stored in entry.txt to /output/entry.txt.
"""

LINE = "The office printer has been warming up since Tuesday, which is officially the longest anyone here has stayed motivated."


def validate():
    """Check the joke is a single office-themed line of 1 to 200 characters."""
    assert LINE.count("\n") == 0, "joke must be a single line"
    assert 0 < len(LINE) <= 200, f"expected 1-200 chars, got {len(LINE)}"
    assert LINE.strip() == LINE, "joke must not have leading/trailing whitespace"
    assert "printer" in LINE, "joke must be about office life"
    return True


def main():
    validate()
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
