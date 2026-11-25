#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one joke about office life to /output/entry.txt. Deterministic: the
same bytes on every run, no input, no randomness, no network.

The joke: the office plant dies, HR sends a condolence email — and the dead
plant still gets more recognition than the narrator did all quarter. The
observation is true to the office (HR emails for everything, recognition
for nothing), the turn is surprising (the plant, not a person, is the one
being mourned — and it still outranks the employee), and it ends on its
strongest beat.
"""

from pathlib import Path

ENTRY = (
    "The office plant died, HR sent a condolence email, and the plant "
    "still got more recognition than I did this quarter.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
