# The world on Friday 13 November 2026

A front-page collage summing up the world's news of Friday 13 November 2026
in one image (1024x1024), built for the make.fun competition
`news-image-01` ("Sum up 13 November's world news in one image").

## The four stories

1. **Europe joins Ukraine peace talks** — Europe joins the next round of
   Ukraine peace talks; Putin met US envoys Witkoff and Kushner in Moscow
   and restated full terms; Zelensky confirmed Europe is directly
   represented; the largest prisoner exchange of the war is being prepared.
2. **Nvidia chief Huang resigns, shares fall** — CEO Jensen Huang resigned
   on Thursday 12 November (president, CEO and director, effective
   immediately, no reason given); CFO Colette Kress is interim CEO and
   Harvey C. Jones is the first board chair; shares fell as much as 14% at
   the open and closed down 4.34% at $166.19; earnings are due Tuesday
   17 November.
3. **Microsoft 365 down worldwide** — Microsoft 365 mail and Teams were down
   worldwide across regions.
4. **Tankers hit in the Strait of Hormuz** — Four oil tankers were hit by
   explosions in the Strait of Hormuz; Iran says an LNG tanker struck a
   naval mine; Israel's cabinet ordered preparations for a possible strike
   on Iran.

## How it was made

Four photographic panels were generated separately (one per story, no text
in the generated images), then composited with PIL into a 2x2 grid under a
header band. All labels were drawn with PIL in DejaVu Sans Bold, never by
the image generator, so the text stays crisp and legible.

## Run it

```sh
python3 main.py
```

This copies the baked `entry.png` to `/output/entry.png`
(or `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set).
The program is stdlib-only and deterministic: repeated runs produce
byte-identical output.
