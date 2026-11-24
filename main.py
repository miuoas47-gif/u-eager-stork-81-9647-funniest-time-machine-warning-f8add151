#!/usr/bin/env python3
"""Funniest Time Machine Warning Label - make.fun entry.

Writes a single warning label (120 characters at most) to /output/entry.txt.
The label turns the butterfly effect - a real time-travel hazard - into the
joke, keeps a deadpan safety-notice tone, and saves the surprise for the
last few words.
"""
import os

LABEL = "WARNING: Do not step on any butterflies. Legal is still settling the dinosaur case."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate requires 1-120 characters of UTF-8 text, not only whitespace.
    if not 1 <= len(LABEL) <= 120 or not LABEL.strip():
        raise SystemExit("label fails the 120-character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
