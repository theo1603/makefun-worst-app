"""Worst App Idea Ever Pitched: Blinkr.

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "Blinkr is the app that counts every blink you make during a film "
    "and emails the weekly total to your dentist, because your "
    "oral-health team has waited long enough to know your viewing habits."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
