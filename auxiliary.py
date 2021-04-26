# ############################################################################
# Color Fingerprint: aux.py
#   Auxiliary functions definitions
# ############################################################################
import cv2
import glob
import numpy as np
from itertools import cycle
from itertools import groupby
from operator import itemgetter
from matplotlib import pyplot as plt
from sklearn.cluster import MiniBatchKMeans


def readAndProcessImg(path):
    # Read image and convert from BGR to RGB
    bgr = cv2.imread(path)
    frameBGR = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    # Remove borders
    # gray = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2GRAY)
    # (_, thresh) = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
    # frame = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    # (contours, hierarchy) = cv2.findContours(
    #     thresh,cv2.RETR_EXTERNAL,
    #     cv2.CHAIN_APPROX_SIMPLE
    # )
    # cnt = contours[0]
    # (x, y, w, h) = cv2.boundingRect(cnt)
    # crop = frameBGR[y:y+h,x:x+w]
    # Flatten the image into an RGB vector
    shp = frameBGR.shape
    return (frameBGR, shp)


def calculateDominantColors(
        filepaths, domColNum, clustersNum, maxIter=100, VERBOSE=True
    ):
    # Create an empty array with dimensions: (framesNumber, dominantColors, 3)
    clusters = np.empty((len(filepaths), domColNum, 3))
    # Initialize a KMean instance for clustering
    kMeansCall = MiniBatchKMeans(n_clusters=clustersNum, max_iter=maxIter)
    # Iterate through the files
    for (i, path) in enumerate(filepaths):
        if VERBOSE:
            filesNum = len(filepaths)
            print('\t* Frame {}/{}'.format(i+1, filesNum), end='\r')
        # Read image and reshape to an RGB vector of vectors
        (frame, shp) = readAndProcessImg(path)
        flatFrame = frame.reshape([1, shp[0] * shp[1], 3])[0]
        # Cluster the RGB entries for color dominance detection
        kmeans = kMeansCall.fit(flatFrame)
        # Take the color palette and add it to the clusters container
        if (domColNum==1 and clustersNum==1):
            palette = kmeans.cluster_centers_
            clusters[i] = [rescaleColor(color) for color in palette]
        else:
            frequencies = {
                key: len(list(group)) for key, group in groupby(sorted(kmeans.labels_))
            }
            dominant = dict(
                sorted(frequencies.items(), key = itemgetter(1), reverse = True
            )[:domColNum])
            dominantKeys = list(dominant.keys())
            palette = [kmeans.cluster_centers_[j] for j in dominantKeys]
            myiter = cycle(palette)
            pallettePad = [next(myiter) for _ in range(domColNum)]
            clusters[i] = [rescaleColor(color) for color in pallettePad]
    if VERBOSE:
        print("\33[2K", end='\r')
    return clusters


def getFilepaths(path, namesHead, ext='.png'):
    filepaths = sorted(glob.glob(path + '/' + namesHead + '*' + ext))
    return filepaths


def rescaleColor(colorEightBit):
    colors = list(colorEightBit)
    return [i / 255 for i in colors]


def exportFingerprintPlot(
        path, filename, clusters, dims=(10, 10), 
        dpi=500, aspect=1, movieTitle='', **kwargs
    ):
    fig, ax = plt.subplots(figsize=dims)
    ax.axis('off')
    plt.imshow(list(map(list, zip(*clusters))), aspect=aspect)
    plt.text(
        0.5, 0.5, movieTitle, 
        horizontalalignment='center', verticalalignment='center', 
        transform=ax.transAxes, 
        fontfamily=kwargs['fontfamily'],
        fontsize=kwargs['fontsize'],
        color=kwargs['color']
    )
    plt.savefig(
            path + '/' + filename, dpi=dpi,
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


def isNotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter