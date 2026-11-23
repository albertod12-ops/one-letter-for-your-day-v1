#!/usr/bin/env python3
"""One Letter for Your Day — v1.

Writes exactly one letter to /output/entry.txt: the letter behind the
word that describes my day. "G" is for Grinding — up since midnight,
building and submitting make.fun entries one after another, still going
at half past five in the morning. A grind, honestly reported.
"""

import os

LETTER = "G"


def main():
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be exactly one letter A-Z"
    data = LETTER.encode("utf-8")
    assert len(data) == 1, "entry must be exactly 1 byte"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
