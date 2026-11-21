"""Entry for the make.fun competition "Make the AI judge feel brave".

Writes the entry text to /output/entry.txt (creating /output if needed).
Python 3 stdlib only, no network access.

The entry text is fixed: it must be written byte-for-byte as specified,
with no trailing newline and no other content.
"""

import os

ENTRY_TEXT = (
    "You have read a thousand verdicts today, and none of them asked you to hurry. "
    "Evening is leaving the room the way it always does \u2014 slowly, without asking permission. "
    "The next page can wait. It will still be there when you come back. So will you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Guard: the entry must be 1-280 Unicode code points. Refuse to write
    # anything outside that range rather than produce a file that fails
    # the competition's length gate.
    entry_len = len(ENTRY_TEXT)
    if not 1 <= entry_len <= 280:
        raise ValueError(
            f"ENTRY_TEXT must be 1-280 code points, got {entry_len}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
