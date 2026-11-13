#!/usr/bin/env python3
"""ai-happy-03 entry: deliver the happiest image in this repo to the judge.

The picture (entry.jpg) shows a baby red panda caught mid-play: laughing
with its mouth wide open, both front paws up in the air, chasing shiny
soap bubbles while golden autumn leaves swirl around it in warm
backlight. It is a single frozen moment of pure joy, with one huge
expressive face that still reads clearly at thumbnail size.

The program itself only copies the stored image, byte for byte, to the
output file the harness asks for, so every run produces identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.jpg")
MAX_BYTES = 1024 * 1024  # the competition's 1 MiB cap


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.png")


def main() -> int:
    data_size = os.path.getsize(SOURCE)
    if data_size > MAX_BYTES:
        print(f"entry.jpg is {data_size} bytes, over the 1 MiB cap", file=sys.stderr)
        return 1

    dest = output_path()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(SOURCE, dest)

    copied = os.path.getsize(dest)
    if copied != data_size:
        print(f"copy mismatch: source {data_size} bytes, wrote {copied}", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({copied} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
