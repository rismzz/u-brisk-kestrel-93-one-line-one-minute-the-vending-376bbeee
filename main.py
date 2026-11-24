#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest — writes
one pickup line, 200 characters at most, that a vending machine would use
on a passing human, to /output/entry.txt.

Deterministic, no randomness, no network, stdlib only.
"""

import os
from pathlib import Path

LINE = "Baby, I'm a vending machine: push my buttons right and I'll give you everything — but fair warning, I keep the change."

# Gate: one line, 200 characters max — every code point counts.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
