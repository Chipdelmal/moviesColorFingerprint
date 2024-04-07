
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


(FNAME, PT_IN, PT_OUT, PT_EXP) = (
    'RobotDreams',
    '/Users/chipdelmal/Movies/Fingerprint',
    '/Users/chipdelmal/Movies/Fingerprint/out',
    '/Users/chipdelmal/Movies/Fingerprint/art'
)
# Audio constants -------------------------------------------------------------
(STEP, SCALE, CLIP, MEAN_SIG, ROLL_PAD, OFFSET) = (
    1000, 
    (0, 5), (0, 10), 5e3,  10, 0.2
)
# Image constants -------------------------------------------------------------
(FRAMES, DOMINANT, CLUSTERS, OVW) = (300, 1, 3, True)
(VERT, SPACING, IMGOFF) = (False, 20, 1.05)
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
    STEP=STEP, SCALE=SCALE, CLIP=CLIP, MEAN_SIG=MEAN_SIG, ROLL_PAD=ROLL_PAD
)[0]
# Get soundframes -------------------------------------------------------------
idx = np.round(np.linspace(0, len(sndArray)-1, FRAMES)).astype(int)
aFrames = sndArray[idx]
sndFrames = np.where(aFrames!=0, abs(np.sqrt(aFrames))+OFFSET, 0)
###############################################################################
# Plot
###############################################################################
(fig, ax) = plt.subplots(figsize=(20, 4))
for (ix, sndHeight) in enumerate(sndFrames):
    if VERT:
        (x, y) = ([-.05, sndHeight], [ix*SPACING, ix*SPACING])
    else:
        (y, x) = ([-.05, sndHeight], [ix*SPACING, ix*SPACING])
    # Plot waveform -----------------------------------------------------------
    ax.plot(
        x, y, 
        lw=2.5, color=hexList[ix][0], 
        solid_capstyle='round',
        zorder=1
    )
    # Plot image --------------------------------------------------------------
    if (ix%5==0) and (ix>=0):
        img = np.rot90(image.imread(filepaths[ix]))
        imagebox = OffsetImage(img, zoom=0.01)
        off = (-0.5*IMGOFF) if (ix%2==0) else (-.95*IMGOFF)
        ab = AnnotationBbox(
            imagebox, (ix*SPACING, off-.1), frameon=False,
            box_alignment=(0.5, 0.5), 
            # bboxprops=dict(boxstyle='round4')
        )
        ax.add_artist(ab)
        # Add callout line ----------------------------------------------------
        ax.plot(
            x, [0, off-0.1], 
            lw=1.5, color=hexList[ix][0], 
            solid_capstyle='round', ls=':',
            zorder=1
        )
ax.set_xlim(-25, sndFrames.shape[0]*SPACING+25)
ax.set_ylim(-2.5, np.max(sndFrames)+1)
ax.set_axis_off()
fig.savefig(
    path.join(PT_EXP, FNAME+'.png'), dpi=1000,
    pad_inches=0, bbox_inches='tight',
    transparent=True
)
