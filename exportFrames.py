# #############################################################################
# Color Fingerprint: exportFrames.py
#   This auxiliary script exports a regularly-spaced set of frames
#   from the provided input video.
# #############################################################################
import os
import sys
from os import path
import auxiliary as aux
import ffmpeg

# User inputs -----------------------------------------------------------------
if aux.isNotebook():
    (FILE, IN_PATH, OUT_PATH) = (
        'Barbie'+'.mp4',
        '/Users/chipdelmal/Movies/Fingerprint/rescaled', 
        '/Users/chipdelmal/Movies/Fingerprint/frames'
    )
else:
    (FILE, FRAMES_NUM) = (sys.argv[1], int(sys.argv[2]))
    (IN_PATH, OUT_PATH) = (sys.argv[3], sys.argv[4])
(FRAMES_NUM, OVW, SIZE) = (350, True, (1400, 720))
# Output path -----------------------------------------------------------------
pthStr = FILE.split(".")[0]
OUT_PATH = path.join(OUT_PATH, pthStr)
folderExists = False
try: 
    os.mkdir(OUT_PATH) 
except OSError as error: 
    folderExists = True 
# Calculating fps to match required number of frames --------------------------
probe = ffmpeg.probe(path.join(IN_PATH, FILE))
vInfo = next(s for s in probe['streams'] if s['codec_type'] == 'video')
framesNumMovie = int(vInfo['nb_frames'])
framerate = eval(vInfo['avg_frame_rate'])
fps = FRAMES_NUM/framesNumMovie*framerate
# Export frames ---------------------------------------------------------------
if (not folderExists) or (OVW):
    os.system(
        "ffmpeg -loglevel info "
        + "-i " + path.join(IN_PATH, FILE) + " "
        + "-vf fps=" + str(fps) + " "
        + f"-s {SIZE[0]}x{SIZE[1]} "
        + path.join(OUT_PATH, FILE.split(".")[0] + "%04d.png ")
        + "-hide_banner"
    )
