# ############################################################################
# Color Fingerprint: aux.py
#   Auxiliary functions definitions
# ############################################################################
import cv2
import glob
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import MiniBatchKMeans


def calculateDominantColors(filepaths, domColNum, maxIter=100):
    framesNumber = len(filepaths)
    clusters = np.empty((framesNumber, domColNum, 3))
    kMeansCall = MiniBatchKMeans(n_clusters=domColNum, max_iter=maxIter)
    for (i, path) in enumerate(filepaths):
        # Read image and convert from BGR to RGB
        bgr = cv2.imread(path)
        frame = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        # Flatten the image into an RGB vector
        shp = frame.shape
        flatFrame = frame.reshape([1, shp[0] * shp[1], 3])[0]
        # Cluster the RGB entries for color dominance detection
        kmeans = kMeansCall.fit(flatFrame)
        # Take the color palette and add it to the clusters container
        palette = kmeans.cluster_centers_
        clusters[i] = [rescaleColor(color) for color in palette]
    return clusters


def getFilepaths(path, namesHead, ext='.png'):
    filepaths = sorted(glob.glob(path + namesHead + '*' + ext))
    return filepaths


def rescaleColor(colorEightBit):
    colors = list(colorEightBit)
    return [i / 255 for i in colors]


def exportFingerprintPlot(path, filename, clusters, dims=(10, 5), dpi=500):
    fig, ax = plt.subplots(figsize=dims)
    ax.axis('off')
    plt.imshow(list(map(list, zip(*clusters))))
    plt.savefig(
            path + filename, dpi=dpi,
            bbox_inches='tight', pad_inches=0
        )
    plt.close()


def fontFromOS(systemName):
    # Select font according to OS
    if systemName == 'Darwin':
        FONT = 'Avenir'
    elif systemName == 'Linux':
        FONT = 'Liberation Sans Narrow'
    else:
        FONT = 'Arial'
    return FONT


def defineFont(fontName, color='black', size=100, alpha=.06):
    fontDict = {
        'fontname': fontName,
        'color': color, 'weight': 'light',
        'size': size, 'alpha': alpha
        }
    return fontDict
