import csv
import array
import numpy as np
from os import path
import pickle as pkl
import auxiliary as aux
import matplotlib.image as image
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.utils import get_array_type
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)


(FNAME, PT_IN, PT_OUT, PT_EXP) = (
    'RogueOne',
    '/Users/chipdelmal/Movies/Fingerprint',
    '/Users/chipdelmal/Movies/Fingerprint/out',
    '/Users/chipdelmal/Movies/Fingerprint/art'
)
(FRAMES, DOMINANT, CLUSTERS) = (250, 1, 3)
(STEP, IN_OFF) = (int(.25e3), 4)
(BITS, SCALE, CLIP, MEAN_SIG) = ((0, 32767), (0, 5), (0, 10), 5e3)
(DIFF_AMP, ROLL_PAD) = (1.35, 10)
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
if path.isfile(pklFile):
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
sound = AudioSegment.from_file(f"{FVIN}.mp4", format="mp4")
channels = sound.split_to_mono()
bitDepth = channels[0].sample_width*8
arrayType = get_array_type(bitDepth)
# Get signal ------------------------------------------------------------------
sigRaw = [array.array(arrayType, sig) for sig in [i._data for i in channels]]
sigAbs = [np.abs(np.array(sig), dtype=np.int64) for sig in sigRaw]
sigSrt = sigAbs if (np.median(sigAbs[1]) < np.median(sigAbs[0])) else sigAbs[::-1]
# Scale signal for plot -------------------------------------------------------
M_POWER = np.mean(sigAbs[0]+sigAbs[1])/2
sigSca = [np.interp(sig, BITS, (SCALE[0], SCALE[1]*MEAN_SIG/M_POWER)) for sig in sigSrt]
sigClp = [np.clip(sig, CLIP[0], CLIP[1]) for sig in sigSca]
# Get soundframes -------------------------------------------------------------
sndArray = sigSca[0]
idx = np.round(np.linspace(0, len(sndArray)-1, FRAMES)).astype(int)
m = sndArray[idx]
sndFrames = np.where(m!=0, abs(np.log(m)), 0)
###############################################################################
# Plot
###############################################################################
(VERT, SPACING, IMGOFF) = (False, 20, 1.5)
(fig, ax) = plt.subplots(figsize=(20, 4))
for (ix, sndHeight) in enumerate(sndFrames):
    if VERT:
        (x, y) = ([0, sndHeight], [ix*SPACING, ix*SPACING])
    else:
        (y, x) = ([0, sndHeight], [ix*SPACING, ix*SPACING])
    # Plot waveform -----------------------------------------------------------
    ax.plot(
        x, y, 
        lw=3, color=hexList[ix][0], solid_capstyle='round',
        zorder=1
    )
    # Plot image --------------------------------------------------------------
    if (ix%5==0) and (ix>0):
        img = image.imread(filepaths[ix])
        imagebox = OffsetImage(img, zoom=0.05)
        off = -IMGOFF if (ix%2==0) else -2*IMGOFF
        ab = AnnotationBbox(
            imagebox, (ix*SPACING, off), frameon=False,
            box_alignment=(0.5, 0.5)
        )
        ax.add_artist(ab)
        # Add callout line ----------------------------------------------------
        ax.plot(
            x, [0, off], 
            lw=1.5, color=hexList[ix][0], solid_capstyle='round',
            zorder=1, ls=':'
        )
ax.set_xlim(-25, sndFrames.shape[0]*SPACING+25)
ax.set_ylim(-5, 10)
ax.set_axis_off()
fig.savefig(
    path.join(PT_EXP, FNAME+'.png'), dpi=500,
    pad_inches=0, bbox_inches='tight'
)
