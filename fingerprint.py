# ############################################################################
# Color Fingerprint: fingerprint.py
#   Takes the frames from the previous step and clusters them using k-means,
#   then it generates the heatmap fingerprint and exports it.
# ############################################################################
import aux


# User Inputs
(FILE, DOMINANT, DPI) = ("00_Pilot", 10, 500)
(IN_PATH, OUT_PATH) = ("./frames/", './fingerprint/')
# Get frames paths and calculate the dominant clusters of the images
filepaths = aux.getFilepaths(IN_PATH, FILE)
clusters = aux.calculateDominantColors(filepaths, DOMINANT)
# Export the resulting fingerprints
aux.exportFingerprintPlot(
        OUT_PATH, FILE + '.png', clusters,
        dims=(10, 5), dpi=DPI
    )
