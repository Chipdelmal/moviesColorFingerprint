
import csv
import numpy as np
import audio as aud
from os import path
import pickle as pkl
import auxiliary as aux
import matplotlib.image as image
import matplotlib.pyplot as plt
from pydub import (AudioSegment, effects)
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)


(FNAME, PT_IN, PT_OUT, PT_EXP, OVW) = (
    'RobotDreams',
    '/Users/chipdelmal/Movies/Fingerprint',
    '/Users/chipdelmal/Movies/Fingerprint/out',
    '/Users/chipdelmal/Movies/Fingerprint/art',
    True
)
# Audio constants -------------------------------------------------------------
(STEP, BAR_SPACING, LW, YOFFSET) = (1000, 20, 2.5, 0.075)
(SCALE, CLIP, MEAN_SIG, ROLL_PAD, OFFSET) = ((0, 5), (0, 10), 5e3,  10, 0.2)
# Image constants -------------------------------------------------------------
(SFRAME, DFRAMES) = (0, 5)
(OFFSETS, ZOOM, ROTATION) = ((-.5, -.95), 0.0125, 0)
(FRAMES, DOMINANT, CLUSTERS) = (300, 1, 3)
(CW, COFF) = (.9, 0.25)
# Plot constants --------------------------------------------------------------
(REVERSED, XRANGE, YRANGE) = (False, (-20, 20), (-2, 1))
###############################################################################
# Setup paths
###############################################################################
(FVIN, FRIN) = (
    path.join(PT_IN, 'rescaled', FNAME),
    path.join(PT_IN, 'frames', FNAME)
)
###############################################################################
# Get dominant colors
###############################################################################
filepaths = aux.getFilepaths(FRIN, FNAME)
pklFile = path.join(PT_OUT, FNAME+'.pkl')
if path.isfile(pklFile) and not OVW:
    with open(pklFile, 'rb') as f:
        clusters = pkl.load(f)
else:
    clusters = aux.parallelDominantImage(
        filepaths, DOMINANT, CLUSTERS, 
        maxIter=100, VERBOSE=True, jobs=1
    )
# Export colorfiles -----------------------------------------------------------
with open(path.join(PT_OUT, FNAME+'.pkl'),'wb') as file:
    pkl.dump(clusters, file)
hexList = [[aux.rgb_to_hex(i) for i in frame] for frame in clusters]
with open(path.join(PT_OUT, FNAME+'.csv'), "w") as f:
    wr = csv.writer(f)
    wr.writerows(hexList)
###############################################################################
# Get audio data
###############################################################################
sound = effects.normalize(AudioSegment.from_file(f"{FVIN}.mp4", format="mp4"))
sndArray = aud.getSoundwave(
    sound, 
    STEP=STEP, SCALE=SCALE, CLIP=CLIP, 
    MEAN_SIG=MEAN_SIG, ROLL_PAD=ROLL_PAD
)[0]
# Get soundframes -------------------------------------------------------------
idx = np.round(np.linspace(0, len(sndArray)-1, FRAMES)).astype(int)
aFrames = sndArray[idx]
sndFrames = np.where(aFrames!=0, abs(np.sqrt(aFrames))+OFFSET, 0)
###############################################################################
# Plot
###############################################################################
offCounter = 0
if REVERSED:
    (sndFrames, filepaths, hexList) = (
        sndFrames[::-1], filepaths[::-1], hexList[::-1]
    )
    SFRAME = SFRAME + DFRAMES - (len(filepaths)-1)%DFRAMES
    ROTATION = 2
(fig, ax) = plt.subplots(figsize=(20, 4))
for (ix, sndHeight) in enumerate(sndFrames):
    # Plot waveform -----------------------------------------------------------
    (y, x) = ([-YOFFSET, sndHeight], [ix*BAR_SPACING, ix*BAR_SPACING])
    ax.plot(
        x, y, 
        lw=LW, color=hexList[ix][0], 
        solid_capstyle='round', zorder=1
    )
    # Plot image --------------------------------------------------------------
    if ((SFRAME+ix)%DFRAMES==0):
        img = np.rot90(
            image.imread(filepaths[ix]), 
            k=ROTATION, axes=(1, 0)
        )
        imagebox = OffsetImage(img, zoom=ZOOM)
        off = OFFSETS[::][offCounter%len(OFFSETS)]       
        ab = AnnotationBbox(
            imagebox, (ix*BAR_SPACING, off), frameon=False,
            box_alignment=(0.5, 0.5), 
        )
        ax.add_artist(ab)
        offCounter = offCounter + 1
        # Add callout line ----------------------------------------------------
        ax.plot(
            x, [0, off-0.1], 
            lw=CW, color=hexList[ix][0], 
            solid_capstyle='round', ls=':', zorder=1
        )
ax.set_xlim(XRANGE[0], sndFrames.shape[0]*BAR_SPACING+XRANGE[1])
ax.set_ylim(YRANGE[0], np.max(sndFrames)+YRANGE[1])
ax.set_axis_off()
fig.savefig(
    path.join(PT_EXP, FNAME+'.png'), dpi=1000,
    pad_inches=0, bbox_inches='tight',
    transparent=True
)
