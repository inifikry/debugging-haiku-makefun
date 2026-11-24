#!/usr/bin/env python3
"""Write the haiku entry to /output/entry.txt."""

import os

HAIKU = "breakpoint set at last\nthe program runs straight past it\nit never gets there\n"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
