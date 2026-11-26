"""Make the AI Judge Laugh — one office-life joke, one line.

The brief: write a single joke about office life, one line, under
200 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The joke plays on the most universally true office observation —
the calendar that eats your whole day — and turns it on itself:
booking a meeting to grieve the time lost booking meetings, then
having even that grief meeting rescheduled. No pun, no stock
"this meeting could have been an email" line; the twist is the
second reschedule, which lands because everyone has lived it.
"""

import os

# One line, 96 characters, no trailing newline inside the joke itself.
JOKE = (
    "I had to book a meeting to grieve the free time I lost booking "
    "meetings \u2014 it got rescheduled twice."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    # Gate mirrors the sealed scorer: 1-200 chars, not only whitespace,
    # single line, UTF-8. Fail loudly here rather than shipping invalid.
    assert 1 <= len(text) <= 200, f"joke length {len(text)} out of range"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
