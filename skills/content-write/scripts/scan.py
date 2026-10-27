#!/usr/bin/env python3
"""Measure how scannable a post is.

Prints each line with its length, flags lines over the limit, lines holding
more than one sentence, and paragraphs with more than 2 lines, and names the
shape of each list (long to short, short to long, square, arrow, or no
shape). It measures; the writer judges.

Usage:
  python3 scan.py post.md            # a file holding only the post text
  python3 scan.py post.md --max 80   # line limit in characters (default 80)
  cat post.md | python3 scan.py -

Markdown quote markers ("> ") are stripped, so a post copied from a draft
or a chat reply works as-is.
"""

import argparse
import re
import sys

LIST_ITEM = re.compile(r"^\s*(?:[-*•–]|\d+[.)])\s+")
TIMELINE = re.compile(
    r"^\s*(?:(?:Week|Day|Month|Step|Q)\s*\d+|\d{4}"
    r"|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*(?:\s+\d{4})?)\s*:",
    re.I,
)


def is_item(line):
    return bool(LIST_ITEM.match(line) or TIMELINE.match(line))


def item_text(line):
    return LIST_ITEM.sub("", line).strip()


def shape(lengths):
    if len(lengths) < 3:
        return "too short to shape (fewer than 3 items)"
    lo, hi = min(lengths), max(lengths)
    if hi - lo <= max(6, hi * 0.2):
        return "square"
    tol = 3
    pairs = list(zip(lengths, lengths[1:]))
    if all(b <= a + tol for a, b in pairs):
        return "long to short"
    if all(b >= a - tol for a, b in pairs):
        return "short to long"
    peak = lengths.index(hi)
    if 0 < peak < len(lengths) - 1:
        up = all(b >= a - tol for a, b in pairs[:peak])
        down = all(b <= a + tol for a, b in pairs[peak:])
        if up and down:
            return "arrow (>)"
    return "no shape"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("post", help="file with the post text, or - for stdin")
    parser.add_argument("--max", type=int, default=80, help="line length limit in characters (default 80)")
    args = parser.parse_args()

    raw = sys.stdin.read() if args.post == "-" else open(args.post, encoding="utf-8").read()
    lines = [re.sub(r"^\s*>\s?", "", l).rstrip().rstrip("\\").rstrip() for l in raw.splitlines()]

    # Group into paragraphs separated by blank lines.
    paragraphs, current = [], []
    for line in lines:
        if line.strip():
            current.append(line)
        elif current:
            paragraphs.append(current)
            current = []
    if current:
        paragraphs.append(current)

    long_lines = dense = lists = multi = 0
    words = sum(len(l.split()) for p in paragraphs for l in p)
    print(f"{words} words · {len(paragraphs)} paragraphs\n")

    for i, para in enumerate(paragraphs, 1):
        items = [l for l in para if is_item(l)]
        prose = [l for l in para if not is_item(l)]
        for line in para:
            flags = []
            if len(line) > args.max:
                flags.append(f"over {args.max}")
                long_lines += 1
            sentences = len(re.findall(r"[.!?](?:\s+|$)", item_text(line)))
            if sentences > 1:
                flags.append(f"{sentences} sentences on one line")
                multi += 1
            print(f"{len(line):4}  {line}" + (f"  ← {', '.join(flags)}" if flags else ""))
        if len(prose) > 2:
            print(f"      ↳ paragraph {i} has {len(prose)} lines: split it")
            dense += 1
        if items:
            lists += 1
            print(f"      ↳ list shape: {shape([len(item_text(l)) for l in items])}")
        print()

    print(f"Lines over {args.max}: {long_lines} · Lines with 2+ sentences: {multi} · "
          f"Paragraphs over 2 lines: {dense} · Lists: {lists}")


if __name__ == "__main__":
    main()
