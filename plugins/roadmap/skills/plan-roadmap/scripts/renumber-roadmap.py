#!/usr/bin/env python3
"""Renumber the global feature sequence in product/ROADMAP.md."""

import re
import sys


def renumber_roadmap(path="product/ROADMAP.md"):
    with open(path) as f:
        lines = f.readlines()

    seq = 0
    out = []
    for line in lines:
        # Match table rows with a numeric first column: | 3 | ... or | 12 | ...
        m = re.match(r'^(\|\s*)\d+(\s*\|.+)', line)
        if m:
            seq += 1
            line = f"{m.group(1)}{seq}{m.group(2)}\n"
        out.append(line)

    with open(path, 'w') as f:
        f.writelines(out)

    print(f"Renumbered {seq} features in {path}")


if __name__ == "__main__":
    renumber_roadmap(sys.argv[1] if len(sys.argv) > 1 else "product/ROADMAP.md")
