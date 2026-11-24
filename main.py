#!/usr/bin/env python3
"""Fortune in a pot — a one-line blessing for a brave little fern."""

import os
from pathlib import Path


EXPECTED_LENGTH = 113
TRAILING_NEWLINE = "\n"


def build_fortune() -> str:
    salutation = "Dear brave little fern:"
    watering = "this week someone will finally water you on time."
    forgiveness = "Your leaves have already forgiven them."
    fortune = " ".join([salutation, watering, forgiveness])
    if len(fortune) != EXPECTED_LENGTH:
        raise ValueError(f"fortune is {len(fortune)} chars, expected {EXPECTED_LENGTH}")
    return fortune


def main() -> None:
    fortune = build_fortune()
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(fortune + TRAILING_NEWLINE, encoding="utf-8")
    round_tripped = entry_path.read_text(encoding="utf-8")
    if round_tripped != fortune + TRAILING_NEWLINE:
        raise RuntimeError("entry.txt round-trip mismatch")
    print(f"Wrote {len(fortune)}-char fortune to {entry_path}")


if __name__ == "__main__":
    main()
