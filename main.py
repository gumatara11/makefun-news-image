#!/usr/bin/env python3
"""Write the news-image-01 entry to the output directory.

The entry image is baked at build time (see entry.png) and this program
simply copies it to the required output path, so the run is fully
deterministic: the same bytes come out every time.

v2: six-story front-page collage (3x2 grid) — Ukraine talks, Nvidia,
Microsoft outage, Hormuz tankers, Nasser hospital strike, Storm Charles.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print("wrote " + dst + " (" + str(size) + " bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
