#!/bin/bash

PT_I='/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/Disney'
PT_O='/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/Disney/Art'

###############################################################################
# Disney Animated Films
###############################################################################
F_NAMES=(
    "1950_Cinderella.mp4"
    "1953_PeterPan.mp4"
)
M_NAMES=(
    "Cinderella (1950)"
    "Peter Pan (1953)"
)

for idx in "${!F_NAMES[@]}"; do
  file=${F_NAMES[$idx]}
  title=${M_NAMES[$idx]}
  bash fingerprint.sh $PT_I $PT_O "$file" "$title"
done

# image-grid --folder /mnt/Luma/Pictures/Art/Movies/Disney/ -bs 0 -y -n 48 -r 48 -w 7750 --out /mnt/Luma/Pictures/Art/Movies/Disney/image-grid.png