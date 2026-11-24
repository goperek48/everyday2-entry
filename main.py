"""Probe entry for "Everyday Things, Two Lines, Longer Run".

The program's whole job is to produce the two lines in
/output/entry.txt: the first line turns a queue into a train of people
so a 10-year-old can picture it in one sentence, and the second line
owns up to where that picture stops being true. The scorer only
accepts UTF-8 text between 1 and 400 characters that is more than
blank space, so the text is measured and checked before anything is
written to disk.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400

LINE_1 = (
    "A queue is a train made of people, where the person at the front "
    "is the engine and everyone else follows one step at a time."
)

LINE_2 = (
    "The train fits because a queue moves in order, front first and "
    "one step at a time, but it leaves out that carriages cannot step "
    "out of line or change their minds, and nobody is really pulling "
    "anyone forward."
)


def build_entry() -> str:
    """Glue the pair together with one newline and nothing after it."""
    return LINE_1 + "\n" + LINE_2


def validate(text: str) -> str:
    """Refuse blank text and anything past the scorer's size cap."""
    if not text.strip():
        raise ValueError("entry must not be empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    return text


def main() -> int:
    entry = validate(build_entry())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
