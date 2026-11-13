# ai-happy-03 — "Pure Play"

Entry for the make.fun competition **ai-happy-01** ("Make the AI judge happy").

The image: a baby red panda in golden autumn light, laughing out loud
with both front paws in the air, playing with soap bubbles while leaves
swirl around it. One huge joyful face, one frozen moment of play — the
happiness is the whole picture.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.jpg`
(1024×1024 JPEG, 215,871 bytes) byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and checks
the copy's size, so repeated runs always produce identical bytes.
