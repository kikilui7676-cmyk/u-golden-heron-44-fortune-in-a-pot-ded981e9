import os
from pathlib import Path

LINE = "Dear brave little fern: this week someone will finally water you on time. Your leaves have already forgiven them."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
