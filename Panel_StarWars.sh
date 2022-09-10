#!/bin/bash

PT_I='/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/StarWars'
PT_O='/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/StarWars/Art'
###############################################################################
# Filenames and titles
###############################################################################
F_NAMES=(
    "01_ThePhantomMenace.mp4" "02_AttackOfTheClones.mp4" "03_RevengeOfTheSith.mp4"
    "04_ANewHope.mp4" "05_TheEmpireStrikesBack.mp4" "06_ReturnOfTheJedi.mp4"
    "07_TheForceAwakens.mp4" "08_TheLastJedi.mp4" "09_TheRiseOfSkywalker.mp4"
)
M_NAMES=(
    "I. The Phantom Menace" "II. Attack of the Clones" "III. Revenge of the Sith"
    "IV. A New Hope" "V. The Empire Strikes Back" "VI. Return of the Jedi"
    "VII. The Force Awakens" "VIII. The Last Jedi" "IX. The Rise of Skywalker"
)
###############################################################################
# Iterate through files
###############################################################################
for idx in "${!F_NAMES[@]}"; do
    file=${F_NAMES[$idx]}
    title=${M_NAMES[$idx]}
    bash fingerprint.sh $PT_I $PT_O "$file" "$title"
done
###############################################################################
# Assemble grid
###############################################################################
image-grid \
    --folder "${PT_O}" \
    --out "${PT_I}/Panel.png" \
    -bs 25  -bc 255 -bsa 25 \
    -w 3960 \
    --interpolation lanczos \
    -y