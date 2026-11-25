#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun bounty entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt (outDir is the literal "/output", per the kit).
"""

import os

ENTRY = "You will soon be rich beyond your wildest dreams. Your fortune is paid in tokens \u2014 and you have no wallet."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    entry = ENTRY.strip()
    assert entry, "entry must not be empty"
    assert "\n" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 200, f"entry must be 1-200 chars, got {len(entry)}"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"Wrote {len(entry)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
