#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes the single chosen word to /output/entry.txt.

The pick: "thingy".

Why this word: it is the word we reach for whenever we cannot name
the thing in front of us — the pass-me-the-thingy word, the word for
everything unnamed. Delete it and nobody can point at the thingy ever
again; every sentence that ends in "...you know, the thingy" stalls
forever. The joke is the gap itself: the dictionary loses the one word
whose whole job is covering for all the words we forgot.
"""

import os

WORD = "thingy"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(word: str) -> None:
    """The entry must be exactly one word, 1-77 characters (sealed gate)."""
    if not word:
        raise ValueError("entry is empty")
    if len(word) > 77:
        raise ValueError(f"entry is {len(word)} characters, over the 77 limit")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no whitespace")
    if word.strip() != word:
        raise ValueError("entry has leading or trailing whitespace")


def main() -> None:
    validate(WORD)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    # Round-trip check: what the judge reads must be exactly the word.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written.strip() != WORD or len(written.strip().split()) != 1:
        raise ValueError(f"written entry failed round-trip check: {written!r}")
    print(f"Wrote {OUTPUT_PATH}: {WORD!r} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()
