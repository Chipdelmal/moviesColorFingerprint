# ############################################################################
# Color Fingerprint
#   This routine parses a movie and clusters colors found at every
#       predetermined number of frames to export the dominant palette
#       throughout the movie.
# ############################################################################
# https://github.com/kkroening/ffmpeg-python/blob/master/examples/README.md#convert-video-to-numpy-array
# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# ############################################################################

import aux
import ffmpeg
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# User inputs
(FILE, IN_PATH, OUT_PATH) = ('PrincessMononoke.mp4', './in/', './out/')
(FILE_NAME, DOMINANT, STEPS, DPI) = (IN_PATH + FILE, 20, 500, 1000)

# Get video information
probe = ffmpeg.probe(FILE_NAME)
vInfo = next(s for s in probe['streams'] if s['codec_type'] == 'video')
(width, height) = [int(vInfo[s]) for s in ['width', 'height']]
framesNum = int(vInfo['nb_frames'])

# Parse frames into a numpy array
out, err = (
    ffmpeg
    .input(FILE_NAME)
    .output('pipe:', format='rawvideo', pix_fmt='rgb24')
    .global_args('-loglevel', 'error')
    .run(capture_stdout=True)
)
video = (
    np
    .frombuffer(out, np.uint8)
    .reshape([-1, height, width, 3])
)

# Cluster the pixels in frames
clusters = []
for frame in range(1, framesNum, round(framesNum/STEPS)):
    if frame % 100 == 0:
        print("Frame " + str(frame/framesNum))
    flatFrame = []
    for row in video[frame]:
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
