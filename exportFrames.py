# ############################################################################
# Color Fingerprint: exportFrames.py
#   This auxiliary script exports a homogeneously spaced set of frames
#   from the provided input video.
# ############################################################################

import os
import ffmpeg

(FILE, FRAMES_NUM) = ("GoldenDays.mp4", 50)
(IN_PATH, OUT_PATH) = ("./rescaled/", "./frames/")

# Calculating fps to match required number of frames
probe = ffmpeg.probe(IN_PATH + FILE)
vInfo = next(s for s in probe['streams'] if s['codec_type'] == 'video')
framesNumMovie = int(vInfo['nb_frames'])
framerate = eval(vInfo['avg_frame_rate'])
fps = FRAMES_NUM / framesNumMovie * framerate

# Export frames
os.system(
        "ffmpeg -loglevel panic "
        + "-i " + IN_PATH + FILE + " "
        + "-vf fps=" + str(fps) + " "
        + OUT_PATH + FILE.split(".")[0] + "%04d.png "
        + "-hide_banner"
    )
