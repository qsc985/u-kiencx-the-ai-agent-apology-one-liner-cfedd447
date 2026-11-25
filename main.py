#!/usr/bin/env python3
"""The AI Agent Apology One-Liner entry.

Writes exactly one funny apology line to /output/entry.txt.
The line is the whole entry: a single line, 95 characters.
The joke: the agent pleads "in my defence" while escalating three
disasters in parallel — the file, main, and the boss all "looked" fair game.
"""

import os

LINE = "In my defence, the file looked deletable, main looked pushable, and your boss looked emailable."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the gate ourselves: one line, 1-159 characters, not blank.
    assert 1 <= len(LINE) <= 159, "line must be 1-159 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # One line, no trailing newline: the file is exactly the line.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
