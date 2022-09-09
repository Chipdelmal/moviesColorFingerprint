#!/bin/bash

PT_I=$1
PT_O=$2
FNAME=$3 # "Nausicaa.mp4"
TITLE=$4 # "Nausicaä\nof the\nValley\nof the\nWind"
###############################################################################
# Constants that shouldn't be constants
###############################################################################
DOM='1'
CLS='5'
SCALE='640:370' # '480:270'
FRNUM='3600'
DPI='1000'
###############################################################################
# Internally-generated scratch folders
###############################################################################
PT_R="$PT_I/Rescaled"
PT_F="$PT_I/Frames"
###############################################################################
# Create directories
###############################################################################
mkdir -p $PT_R
mkdir -p $PT_F
mkdir -p $PT_O
###############################################################################
# Print colors
###############################################################################
LGREEN='\033[1;36m'
NC='\033[0m'
###############################################################################
# Rescale movie
###############################################################################
printf "${LGREEN}* Processing: $FNAME ${NC}\n"
printf "\t [1/3] Re-scaling $FNAME...\n"
ffmpeg -n -loglevel panic -i "$PT_I/$FNAME" -vf "scale=$SCALE" "$PT_R/$FNAME" 
printf "\t [2/3] Exporting frames...\n"
python exportFrames.py $FNAME $FRNUM $PT_R $PT_F
printf "\t [3/3] Generating fingerprint...\n"
python fingerprint.py "${FNAME%.*}" $DOM $CLS $FRNUM $DPI $PT_F $PT_O "$TITLE"
# echo "[4/4] Generating colorspace plots..."
# python plotColor.py "${FNAME%.*}" $DOM $CLS $FRNUM $DPI $PT_F $PT_O "$TITLE"
###############################################################################
# Delete scratch folders
###############################################################################
# rm -r $PT_R
# rm -r $PT_F