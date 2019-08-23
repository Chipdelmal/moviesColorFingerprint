# https://github.com/kkroening/ffmpeg-python/blob/master/examples/README.md#convert-video-to-numpy-array
# https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.cluster.vq.kmeans.html

import ffmpeg
import numpy as np
from PIL import Image
from io import BytesIO
import ipywidgets as widgets
from ipywidgets import interact
from matplotlib import pyplot as plt


probe = ffmpeg.probe('./videos/in.mp4')

vInfo = next(s for s in probe['streams'] if s['codec_type'] == 'video')
(width, height) = [int(vInfo[s]) for s in ['width', 'height']]
framesNum = int(vInfo['nb_frames'])



out, err = (
    ffmpeg
    .input('./videos/in.mp4')
    .output('pipe:', format='rawvideo', pix_fmt='rgb24')
    .run(capture_stdout=True)
)
video = (
    np
    .frombuffer(out, np.uint8)
    .reshape([-1, height, width, 3])
)


video[0][0][1]
