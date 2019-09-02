import aux
import cv2
import glob
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


# User Inputs
(FILE, NAME, DOMINANT) = ("TheWindRises", "The Wind Rises", 20)
(IN_PATH, OUT_PATH, DPI) = (
    "./temp/",
    './out/',
    1000
)
FONT = aux.defineFont(
    fontName='Uroob', size=10, alpha=.6, color='white'
)

# Get frames paths
filepaths = sorted(glob.glob(IN_PATH + FILE + '*.jpg'))
framesNumber = len(filepaths)
framesNumber

# Cluster images' colors
clusters = []
for (i, path) in enumerate(filepaths):
    if i % 10 == 0:
        print("Progress: (" + str(i/len(filepaths)) + " / 1.0)")
    frame = cv2.imread(path)
    flatFrame = []
    for row in frame:
        for col in row:
            flatFrame.append(list(col))
    kmeans = KMeans(n_clusters=DOMINANT, n_jobs=4).fit(flatFrame)
    palette = kmeans.cluster_centers_
    rescale = [aux.rescaleColor(color) for color in palette]
    clusters.append(rescale)

sortedClusters = [sorted(cls) for cls in clusters]

# Export the resulting fingerprint
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
plt.imshow(list(map(list, zip(*clusters))))
plt.savefig(
    OUT_PATH + FILE.split('.')[0] + '.pdf',
    bbox_inches='tight', dpi=DPI, pad_inches=0
)
plt.text(
    .5, .5-.1, NAME, fontdict=FONT, horizontalalignment='center',
    verticalalignment='center', transform=ax.transAxes
)
plt.savefig(
    OUT_PATH + FILE.split('.')[0] + 'N.pdf',
    bbox_inches='tight', dpi=DPI, pad_inches=0
)

# Export the resulting fingerprint
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
plt.imshow(list(map(list, zip(*sortedClusters))))
plt.savefig(
    OUT_PATH + FILE.split('.')[0] + 'S.pdf',
    bbox_inches='tight', dpi=DPI, pad_inches=0
)
plt.text(
    .5, .5-.1, NAME, fontdict=FONT, horizontalalignment='center',
    verticalalignment='center', transform=ax.transAxes
)
plt.savefig(
    OUT_PATH + FILE.split('.')[0] + 'SN.pdf',
    bbox_inches='tight', dpi=DPI, pad_inches=0
)