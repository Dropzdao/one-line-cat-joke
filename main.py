#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun bounty entry.

Writes one joke about cats, a single line under 200 characters, to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I asked my cat for emotional support; he walked across my keyboard, "
    "deleted my work, and left like he'd fixed everything."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
