import aux
import cv2
import glob
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# User Inputs
(FILE, DOMINANT) = ("PrincessMononoke", 10)
(IN_PATH, OUT_PATH, FPS) = ("./temp/", "./out/", 1/60)

# Get frames paths
filepaths = sorted(glob.glob(IN_PATH + FILE + '*.jpg'))

# Cluster images' colors
clusters = []
for (i, path) in enumerate(filepaths):
    if i % 10 == 0:
        print("Frame " + str(i/len(filepaths)))
    frame = cv2.imread(path)
    flatFrame = []
    for row in frame:
        for col in row:
            flatFrame.append(list(col))
    kmeans = KMeans(n_clusters=DOMINANT).fit(flatFrame)
    palette = kmeans.cluster_centers_
    rescale = [aux.rescaleColor(color) for color in palette]
    clusters.append(sorted(rescale))

# Export the resulting fingerprint
plt.imshow(list(map(list, zip(*clusters))))
plt.axis('off')
plt.savefig(
    OUT_PATH + FILE.split('.')[0] + '.png',
    bbox_inches='tight',
    dpi=DPI,
    pad_inches=0
)
