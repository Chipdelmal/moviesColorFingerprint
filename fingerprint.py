# #############################################################################
# Color Fingerprint: fingerprint.py
#   Takes the frames from the previous step and clusters them using k-means,
#   then it generates the heatmap fingerprint and exports it.
# #############################################################################
import sys
from os import path
import numpy as np
import auxiliary as aux
# User inputs -----------------------------------------------------------------
if aux.isNotebook():
    (FILE, DOMINANT, FRAMES, DPI) = ("PrincessMononoke", 1, 3600, 1000)
    (IN_PATH, OUT_PATH, TITLE) = (
        "/mnt/Luma/Videos/Movies/Frames", 
        '/mnt/Luma/Videos/Movies/',
        'Princess\nMononoke'
    )
else:
    (FILE, DOMINANT, FRAMES, DPI) = (
        sys.argv[1], int(sys.argv[2]), 
        int(sys.argv[3]), int(sys.argv[4])
    )
    (IN_PATH, OUT_PATH, TITLE) = (
        sys.argv[5], sys.argv[6], sys.argv[7]
    )
# Get frames paths and calculate the dominant clusters of the images ----------
filepaths = aux.getFilepaths(IN_PATH, FILE)
clusters = aux.calculateDominantColors(filepaths, DOMINANT)
# Export the resulting fingerprints -------------------------------------------
aux.exportFingerprintPlot(
    OUT_PATH, FILE+'.png', clusters, dpi=DPI, 
    aspect=FRAMES/DOMINANT, movieTitle=str(TITLE), fontsize=100, 
    fontfamily='Gotham Light', color='#FFFFFF88'
)
