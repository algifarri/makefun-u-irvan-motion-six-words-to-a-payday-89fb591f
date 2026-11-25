"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic, standard library only.
"""

import os

ENTRY = "First payday: I bought the sunset."


def main() -> None:
    # Gate self-check: exactly six words, 1-60 characters.
    assert len(ENTRY.split()) == 6, "entry must be exactly six words"
    assert 1 <= len(ENTRY) <= 60, "entry must be 1-60 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
