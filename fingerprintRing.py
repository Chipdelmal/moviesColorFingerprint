# #############################################################################
# Color Fingerprint: fingerprint.py
#   Takes the frames from the previous step and clusters them using k-means,
#   then it generates the heatmap fingerprint and exports it.
# https://superuser.com/questions/1552112/ffmpeg-extract-every-frame-from-a-video-no-quality-loss-and-resize-shorter-s
# #############################################################################

import sys
from os import path
import multiprocessing
import auxiliary as aux
import pickle as pkl
import csv
import numpy as np
import matplotlib.pyplot as plt

JOBS = multiprocessing.cpu_count()
# User inputs -----------------------------------------------------------------
if aux.isNotebook():
    # For testing and debugging in jupyter ------------------------------------
    (FILE, DOMINANT, CLUSTERS, FRAMES, DPI) = (
        "2003_BrotherBear", 1, 3, 3600, 1250
    )
    (IN_PATH, OUT_PATH, TITLE) = (
        "/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/Disney/Frames", 
        "/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/Disney/Art",
        "Brother Bear\n2003"
    )
else:
    # For calls from the terminal ---------------------------------------------
    (FILE, DOMINANT, CLUSTERS, FRAMES, DPI) = (
        sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), 
        int(sys.argv[4]), int(sys.argv[5])
    )
    (IN_PATH, OUT_PATH, TITLE) = (
        sys.argv[6], sys.argv[7], sys.argv[8]
    )
    TITLE = bytes(TITLE, "utf-8").decode("unicode_escape")
(STRIP, OVW) = (False, False)
(ringRadius, barHeight) = (15, 8)
# Get frames paths and calculate the dominant clusters of the images ----------
IN_PATH = path.join(IN_PATH, FILE)
filepaths = aux.getFilepaths(IN_PATH, FILE)
pklFile = path.join(OUT_PATH, FILE+'.pkl')
if path.isfile(pklFile):
    with open(pklFile, 'rb') as f:
        clusters = pkl.load(f)
else:
    clusters = aux.parallelDominantImage(
        filepaths, DOMINANT, CLUSTERS, 
        maxIter=100, VERBOSE=True, jobs=8
    )
# clusters = aux.calculateDominantColors(filepaths, DOMINANT, CLUSTERS)
###############################################################################
# Plot Iris
###############################################################################
plt.rcParams['font.size'] = '25'
(astart, aend) = (0, 2*np.pi/2)
ANGLES = np.linspace(astart, aend, clusters.shape[0], endpoint=False)
COLORS = [list(i[0]) for i in clusters]
LABEL =  f'{TITLE}'  #f'{TITLE}'.replace('\n', ' (')+')',
# Figure ----------------------------------------------------------------------
(fig, ax) = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})
fig.add_axes(ax)
ax.set_theta_zero_location('W')
ax.set_theta_direction(-1)
ax.set_axis_off()
ax.set_rscale('linear')
ax.vlines(
    ANGLES, ringRadius, ringRadius+barHeight, 
    lw=1, colors=COLORS, alpha=1, 
    zorder=-1
)
plt.text(
    .5, .5, LABEL, 
    color='#000000CC', font='Gotham Light', rotation=0,
    horizontalalignment='center', verticalalignment='bottom',
    transform=ax.transAxes
)
plt.tight_layout()
# ax.set_xlim(0, ringRadius+barHeight)
ax.set_ylim(0, ringRadius+barHeight)
# ax.set_facecolor("#000000CC")
# fig.patch.set_facecolor("#000000CC")
plt.savefig(
    OUT_PATH + '/' + FILE+'_R.png', dpi=300,
    pad_inches=0,
    transparent=True
)
plt.close()