# ############################################################################
# Color Fingerprint: aux.py
#   Auxiliary functions definitions
# ############################################################################
import os
import cv2
import glob
import shutil
import numpy as np
from itertools import cycle
from itertools import groupby
from operator import itemgetter
from matplotlib import pyplot as plt
from joblib import Parallel, delayed
from joblib import dump, load
from sklearn.cluster import MiniBatchKMeans
import matplotlib.font_manager
from IPython.core.display import HTML


def readAndProcessImg(path):
    # Read image and convert from BGR to RGB
    bgr = cv2.imread(path)
    frameBGR = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    shp = frameBGR.shape
    return (frameBGR, shp)


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % tuple([int(i*255) for i in rgb])


def dominantImage(
        img, domColNum, clustersNum, maxIter=100
    ):
    (frame, shp) = img
    flatFrame = frame.reshape([1, shp[0] * shp[1], 3])[0]
    kMeansCall = MiniBatchKMeans(n_clusters=clustersNum, max_iter=maxIter)
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
    colors = [rescaleColor(color) for color in pallettePad]
    return colors


def dominatImageWrapper(
        ix, filepaths, clustersArray, 
        domColNum, clustersNum, 
        maxIter=100, VERBOSE=True
    ):
    if VERBOSE:
        filesNum = len(filepaths)
        print('\t* Frame {}/{}'.format(ix+1, filesNum), end='\r')
    img = readAndProcessImg(filepaths[ix])
    cols = dominantImage(img, domColNum, clustersNum, maxIter=maxIter)
    clustersArray[ix] = cols
    # print(clustersArray[ix-1:ix+1])
    return clustersArray


def parallelDominantImage(
        filepaths, domColNum, clustersNum, 
        maxIter=100, VERBOSE=True, jobs=4
    ):
    mmap = 'memmap.job'
    clustersArray = np.memmap(
        mmap, dtype=np.double,
        shape=(len(filepaths), domColNum, 3), mode='w+'
    )
    # clustersArray = np.empty((len(filepaths), domColNum, 3))
    Parallel(n_jobs=jobs)(
        delayed(dominatImageWrapper)(
            ix, filepaths, clustersArray, 
            domColNum, clustersNum, 
            maxIter=maxIter, VERBOSE=VERBOSE
        ) for ix in range(0, len(filepaths))
    )
    os.remove(mmap) 
    return clustersArray

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
    ax.axhspan(
        kwargs['hspan'][0], kwargs['hspan'][1], 
        facecolor=kwargs['facecolor'], transform=ax.transAxes
    )
    ax.axhspan(
        kwargs['hspan'][0]-.0020, kwargs['hspan'][0], 
        facecolor='#ffffff', transform=ax.transAxes
    )
    plt.imshow(list(map(list, zip(*clusters))), aspect=aspect)
    plt.text(
        kwargs['textpos'][0], kwargs['textpos'][1], movieTitle, 
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




# def make_html(fontname):
#     return "<p>{font}: <span style='font-family:{font}; font-size: 24px;'>{font}</p>".format(font=fontname)

# code = "\n".join([make_html(font) for font in sorted(set([f.name for f in matplotlib.font_manager.fontManager.ttflist]))])
# HTML("<div style='column-count: 2;'>{}</div>".format(code))