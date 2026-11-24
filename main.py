"""Say What Actually Broke — make.fun entry.

Writes the honest error line to output/entry.txt. Python stdlib
only, no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "Save failed: your file was too big for the disk, which is also full "
    "of photos you swore you'd delete in 2019 — free up 2 GB and try again."
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"


MAX_CHARS = 200  # the brief caps the error line at 200 characters


def check_entry(text: str) -> str:
    """Return the line unchanged, or raise if it breaks the brief."""
    if "\n" in text:
        raise ValueError("the error copy must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"error line is {len(text)} chars, over the {MAX_CHARS} cap")
    if "failed" not in text.lower():
        raise ValueError("the line must name the real failure, not hide it")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
