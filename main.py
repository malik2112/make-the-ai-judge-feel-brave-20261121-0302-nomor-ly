#!/usr/bin/env python3
"""Entry for make.fun make-the-ai-judge-feel-brave-20261121-0302.

Writes one short relaxing text to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The text is a clock-repair vignette: gears lifted out one by one
onto a cloth, each tooth brushed clean and set back in order, then
the glass closed and the key wound twice so the tick returns to a
quiet room. Concrete work, unhurried rhythm, no instructions.
"""

import os

TEXT = (
    "He opens the case and lifts the gears out one by one onto a cloth. "
    "With a fine brush he cleans each tooth, then sets them back in "
    "order, no hurry. When the balance wheel swings again he closes "
    "the glass, winds the key twice, and listens to it tick into the "
    "quiet room."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
