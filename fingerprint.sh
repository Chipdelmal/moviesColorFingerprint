#!/bin/bash

PT_I=$1
PT_O=$2
FNAME=$3 # "Nausicaa.mp4"
TITLE=$4 # "Nausicaä\nof the\nValley\nof the\nWind"
# Constants that shouldn't be constants ---------------------------------------
DOM='1'
CLS='7'
SCALE='640:370' # '480:270'
FRNUM='3600'
DPI='500'
# Internally-generated scratch folders ----------------------------------------
PT_R="$PT_I/Rescaled"
PT_F="$PT_I/Frames"
# Create directories ----------------------------------------------------------
mkdir -p $PT_R
mkdir -p $PT_F
mkdir -p $PT_O
# Rescale movie ---------------------------------------------------------------
echo "* Processing: $FNAME"
echo "[1/3] Re-scaling $FNAME..."
# ffmpeg -n -loglevel panic -i "$PT_I/$FNAME" -vf "scale=$SCALE" "$PT_R/$FNAME"
echo "[2/3] Exporting frames..."
# python exportFrames.py $FNAME $FRNUM $PT_R $PT_F
echo "[3/3] Generating fingerprint..."
python fingerprint.py "${FNAME%.*}" $DOM $CLS $FRNUM $DPI $PT_F $PT_O "$TITLE"
# Delete scratch folders  -----------------------------------------------------
# rm -r $PT_R
# rm -r $PT_F