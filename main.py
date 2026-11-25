#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes one line: a hardware wallet refusing to sign a transaction at 3 AM.
Stdlib only; no network, no arguments.
"""

import os

ENTRY = (
    "3:06 AM. You've jabbed my buttons 14 times in the dark, and I've "
    "signed zero 3 AM transactions in 412 days. The streak lives \u2014 "
    "come back at breakfast, human."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
