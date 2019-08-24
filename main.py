# https://github.com/kkroening/ffmpeg-python/blob/master/examples/README.md#convert-video-to-numpy-array
# https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.cluster.vq.kmeans.html

import ffmpeg
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


def rescaleColor(colorEightBit):
    return [i / 255 for i in colorEightBit]


(FILE, IN_PATH, OUT_PATH) = ('nausicaa.mp4', './in/', './out/')
(FILE_NAME, DOMINANT, STEPS) = (IN_PATH + FILE, 25, 500)
probe = ffmpeg.probe(FILE_NAME)

vInfo = next(s for s in probe['streams'] if s['codec_type'] == 'video')
(width, height) = [int(vInfo[s]) for s in ['width', 'height']]
framesNum = int(vInfo['nb_frames'])
framesNum

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

clusters = []
for frame in range(1, framesNum, round(framesNum/STEPS)):
    if frame % 50 == 0:
        print("Frame " + str(frame/framesNum))
    flatFrame = []
    for row in video[frame]:
        for col in row:
            flatFrame.append(list(col))
    kmeans = KMeans(n_clusters=DOMINANT).fit(flatFrame)
    palette = kmeans.cluster_centers_
    rescale = [rescaleColor(color) for color in palette]
    clusters.append(sorted(rescale))

plt.imshow(list(map(list, zip(*clusters))))
plt.axis('off')
plt.savefig(
    OUT_PATH + FILE.split('.')[0] + '.png',
    bbox_inches='tight',
    dpi=1000,
    pad_inches=0
)
