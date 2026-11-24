#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label (120 characters at most) to
/output/entry.txt, where the competition's gate scorer reads it.

The label is fixed text: no randomness, no clock, no network, so
every run writes byte-identical output.
"""

import os
import sys

LABEL = (
    "WARNING: Do not prevent your own birth. "
    "No refund will be issued to someone who never existed."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)


def main() -> int:
    text = LABEL
    if not 1 <= len(text) <= 120:
        print(f"label is {len(text)} characters, must be 1-120", file=sys.stderr)
        return 1
    if not text.strip():
        print("label must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back what was written: the gate scores exactly this file,
    # so the program refuses to exit 0 unless it holds the label byte
    # for byte (no trailing newline, no encoding surprise).
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("written entry.txt does not match the label", file=sys.stderr)
        return 1
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
