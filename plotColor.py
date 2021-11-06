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
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import interpolate


JOBS = multiprocessing.cpu_count()
# User inputs -----------------------------------------------------------------
if aux.isNotebook():
    # For testing and debugging in jupyter ------------------------------------
    (FILE, DOMINANT, CLUSTERS, FRAMES, DPI) = (
        "2013_Frozen", 2, 10, 3600, 1000
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

# read file -------------------------------------------------------------------
with open(path.join(OUT_PATH, FILE+'.csv'), newline='') as f:
    reader = csv.reader(f)
    clusters = list(reader)
rgbList = [[np.asarray(aux.hex_to_rgb(i))/255 for i in frame] for frame in clusters]
# 3D Plot ---------------------------------------------------------------------
# fig = plt.figure(figsize=(16,16))
# ax = plt.axes(projection='3d')
# for i in range(3):
#     primRGB = np.asarray(list(zip(*rgbList))[i])
#     primHEX = list(zip(*clusters))[i]
#     (x, y, z) = list(zip(*primRGB))
#     ax.scatter3D(x, y, z, c=primRGB, marker='o', alpha=.1, lw=0, s=200)
#     # for (x,y,z) in primRGB:
#     #     ax.plot(x, z, 'x', c=(x,y,z), zdir='-y', zs=0, alpha=.1, ms=20)
#     #     ax.plot(y, z, 'x', c=(x,y,z), zdir='x', zs=0, alpha=.1, ms=20)
#     #     ax.plot(x, y, 'x', c=(x,y,z), zdir='z', zs=0, alpha=.1, ms=20)
# ax.view_init(25, 30)
# ax.set_xlim3d(0, 1)
# ax.set_ylim3d(0, 1)
# ax.set_zlim3d(0, 1)
# ax.set_box_aspect((1, 1, 1))

# Projections -----------------------------------------------------------------
clstr=3
f = interpolate.interp1d([0, 3], [2.5, 10])
(fig, axs) = plt.subplots(figsize=(16,16), ncols=3)
for i in range(clstr):
    primRGB = np.asarray(list(zip(*rgbList))[i])
    primHEX = list(zip(*clusters))[i]
    (x, y, z) = list(zip(*primRGB))
    for ax in axs:
        ax.axis(ymin=0, ymax=1)
        ax.axis(xmin=0, xmax=1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect(1)
    (ap, mrk, sz)=(.1, 'o', f(i))
    for ix in range(len(x)):
        axs[0].plot(x[ix], z[ix], mrk, c=(x[ix], 0, z[ix]), alpha=ap, ms=sz)
    for ix in range(len(x)):
        axs[1].plot(y[ix], z[ix], mrk, c=(0, y[ix], z[ix]), alpha=ap, ms=sz)
    for ix in range(len(x)):
        axs[2].plot(x[ix], y[ix], mrk, c=(x[ix], y[ix], 0), alpha=ap, ms=sz)


axs = (
    plt.subplot2grid((9,9), (0,0), colspan=1), 
    plt.subplot2grid((9,9), (0,1), colspan=1), 
    plt.subplot2grid((9,9), (0,2), colspan=1),
    plt.subplot2grid((9,9), (1,0), colspan=3)
)
for ix in range(len(x)):
    axs[0].plot(x[ix], z[ix], 'o', c=(x[ix], 0, z[ix]), alpha=.1, ms=5)
for ix in range(len(x)):
    axs[1].plot(y[ix], z[ix], 'o', c=(0, y[ix], z[ix]), alpha=.1, ms=5)
for ix in range(len(x)):
    axs[2].plot(x[ix], y[ix], 'o', c=(x[ix], y[ix], 0), alpha=.1, ms=5)
for ax in axs:
    ax.set_aspect(1)

# Ternary Plot ----------------------------------------------------------------
# i = 0
# primRGB = np.asarray(list(zip(*rgbList))[i])
# primHEX = list(zip(*clusters))[i]

# dfX = pd.DataFrame(np.asarray(prim), columns=('r', 'g', 'b'))
# dfC = pd.DataFrame(primHEX, columns=('Hex', ))
# df = pd.concat([dfX, dfC], axis=1)

# fig = px.scatter_ternary(df, a="r", b="g", c="b", color='Hex')
# fig.show()


# fig = px.scatter_ternary()
# for i in range(3):
#     primRGB = np.asarray(list(zip(*rgbList))[i])
#     primHEX = list(zip(*clusters))[i]
#     for (i, row) in enumerate(primRGB):
#         fig.add_trace(
#             go.Scatterternary(
#                 a=[row[0]], b=[row[1]], c=[row[2]],
#                 marker=dict(color=primHEX[i], opacity=.1, size=5),
#                 line=dict(width=0),
#                 showlegend=False
#             )
#         )
# fig.show()


# i = 0
# primRGB = np.asarray(list(zip(*rgbList))[i])
# primHEX = list(zip(*clusters))[i]

# fig = go.Figure()
# for (i, row) in enumerate(primRGB):
#     fig.add_trace(go.Scatter3d(
#             x=[row[0]], y=[row[1]], z=[row[2]],
#             marker=dict(color=primHEX[i], opacity=.1, size=2.5),
#             line=dict(width=0),
#             showlegend=False
#         )
#     )
# fig.show()


# print('ax.azim {}'.format(ax.azim))
# print('ax.elev {}'.format(ax.elev))