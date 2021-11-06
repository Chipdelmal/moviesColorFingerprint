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

JOBS = multiprocessing.cpu_count()
# User inputs -----------------------------------------------------------------
if aux.isNotebook():
    # For testing and debugging in jupyter ------------------------------------
    (FILE, DOMINANT, CLUSTERS, FRAMES, DPI) = (
        "1937_SnowWhite", 2, 10, 3600, 1000
    )
    (IN_PATH, OUT_PATH, TITLE) = (
        "/mnt/Luma/Videos/Movies/Frames", 
        "/mnt/Luma/Pictures/Art/Movies/Disney",
        "Snow White"
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
# Get frames paths and calculate the dominant clusters of the images ----------
filepaths = aux.getFilepaths(IN_PATH, FILE)
clusters = aux.parallelDominantImage(
    filepaths, DOMINANT, CLUSTERS, 
    maxIter=100, VERBOSE=True, jobs=8
)
# clusters = aux.calculateDominantColors(filepaths, DOMINANT, CLUSTERS)
# Export the resulting fingerprints -------------------------------------------
# aux.exportFingerprintPlot(
#     OUT_PATH, FILE+'.png', clusters, dpi=DPI, 
#     aspect=FRAMES/DOMINANT, movieTitle=str(TITLE).format(), 
#     fontsize=30, fontfamily='Gotham XLight', 
#     color='#FFFFFFFF', textpos=(0.5, (.5-.35)/2),
#     facecolor='#000000FF', hspan=(.35, .5)
# )
# Export colorfiles -----------------------------------------------------------
with open(path.join(OUT_PATH, FILE+'.pkl'),'wb') as file:
    pkl.dump(clusters, file)
hexList = [[aux.rgb_to_hex(i) for i in frame] for frame in clusters]
with open(path.join(OUT_PATH, FILE+'.csv'), "w") as f:
    wr = csv.writer(f)
    wr.writerows(hexList)

