# https://github.com/kkroening/ffmpeg-python/blob/master/examples/README.md#convert-video-to-numpy-array
# https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.cluster.vq.kmeans.html

def rescaleColor(colorEightBit):
    return [i / 255 for i in colorEightBit]


import ffmpeg
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
from PIL import Image
from skimage import io
from io import BytesIO
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


(FILE_NAME, DOMINANT, STEPS) = ('./videos/in.mp4', 10, 500)
probe = ffmpeg.probe(FILE_NAME)

vInfo = next(s for s in probe['streams'] if s['codec_type'] == 'video')
(width, height) = [int(vInfo[s]) for s in ['width', 'height']]
framesNum = int(vInfo['nb_frames'])
framesNum

out, err = (
    ffmpeg
    .input(FILE_NAME)
    .output('pipe:', format='rawvideo', pix_fmt='rgb24')
    .run(capture_stdout=True)
)
video = (
    np
    .frombuffer(out, np.uint8)
    .reshape([-1, height, width, 3])
)

clusters = []
for frame in range(1, framesNum, round(framesNum/STEPS)):
    flatFrame = []
    for row in video[frame]:
        for col in row:
            flatFrame.append(list(col))
    kmeans = KMeans(n_clusters=DOMINANT).fit(flatFrame)
    palette = kmeans.cluster_centers_
    rescale = [rescaleColor(color) for color in palette]
    clusters.append(rescale)

plt.imshow(list(map(list, zip(*clusters))))
plt.axis('off')
