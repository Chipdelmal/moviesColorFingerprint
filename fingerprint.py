import aux
import cv2
import glob
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# User Inputs
(FILE, DOMINANT, DPI) = ("GoldenDays", 20, 1000)
(IN_PATH, OUT_PATH) = ("./frames/", './fingerprint/')

# Get frames paths
filepaths = sorted(glob.glob(IN_PATH + FILE + '*.png'))
framesNumber = len(filepaths)

# Cluster images' colors
clusters = []
for (i, path) in enumerate(filepaths):
    if i % round(framesNumber / 10) == 0:
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

# Export the resulting fingerprints
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')
plt.imshow(list(map(list, zip(*clusters))))
plt.savefig(
        OUT_PATH + FILE.split('.')[0] + '_unsorted.pdf',
        bbox_inches='tight', dpi=DPI, pad_inches=0
    )

fig, ax = plt.subplots(figsize=(10, 5))
plt.imshow(list(map(list, zip(*sortedClusters))))
plt.savefig(
        OUT_PATH + FILE.split('.')[0] + '_sorted.pdf',
        bbox_inches='tight', dpi=DPI, pad_inches=0
    )
