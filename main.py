#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one one-line review of my Monday to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic: the same line every run.
"""

import os

LINE = (
    "Monday, one star: alarm worked, Wi-Fi didn't, inbox hit 47 "
    "unread emails before breakfast — and my coffee filed for a refund."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
