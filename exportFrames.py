
import os
import ffmpeg

FILE = "PrincessMononoke.mp4"
(IN_PATH, OUT_PATH, FRAMES) = ("./in/", "./temp/", 100)

# Calculating fps to match required number of frames
probe = ffmpeg.probe(IN_PATH + FILE)
vInfo = next(s for s in probe['streams'] if s['codec_type'] == 'video')
framesNum = int(vInfo['nb_frames'])
fps = FRAMES / framesNum

# Export frames
os.system(
    "ffmpeg -loglevel panic " +
    "-i " + IN_PATH + FILE + " " +
    "-vf fps=" + str(fps) + " " +
    OUT_PATH + FILE.split(".")[0] + "%04d.jpg " +
    "-hide_banner"
)
