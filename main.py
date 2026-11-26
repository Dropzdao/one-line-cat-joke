#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes the entry line (one line, 121 characters) to /output/entry.txt.
Deterministic, stdlib-only, no network, no input.
"""

import os

ENTRY = (
    "I asked my cat for emotional support; he walked across my keyboard, "
    "deleted my work, and left like he'd fixed everything."
)


def validate(line: str) -> None:
    """The entry must be exactly one line of at most 200 characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > 200:
        raise ValueError("entry must be at most 200 characters")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
