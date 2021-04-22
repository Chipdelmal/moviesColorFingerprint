#!/bin/bash

FNAME='Interstellar.mp4'
# Constants that shouldn't be constants ---------------------------------------
DOM='1'
SCALE='384:160'
FRNUM='1000'
DPI='1000'
PT_I='/mnt/Luma/Videos/Movies'
# Internally-generated scratch folders ----------------------------------------
PT_R="$PT_I/Rescaled"
PT_F="$PT_I/Frames"
PT_O="$PT_I"
# Create directories ----------------------------------------------------------
mkdir -p $PT_R
mkdir -p $PT_F
mkdir -p $PT_O
# Rescale movie ---------------------------------------------------------------
echo "Processing ${FNAME%.*}"
echo "[1/3] Re-scaling movie..."
ffmpeg -loglevel panic -i "$PT_I/$FNAME" -vf "scale=$SCALE" "$PT_R/$FNAME"
echo "[2/3] Exporting frames..."
python exportFrames.py $FNAME $FRNUM $PT_R $PT_F
echo "[3/3] Generating fingerprint..."
python fingerprint.py "${FNAME%.*}" $DOM $FRNUM $DPI $PT_F $PT_O
echo "Done!"
# Delete scratch folders  -----------------------------------------------------
# rm -r $PT_R
# rm -r $PT_F