
import os
import ffmpeg

FILE = "SpiritedAway.mp4"
(IN_PATH, OUT_PATH, FRAMES) = ("./in/", "./temp/", 1000)

# Calculating fps to match required number of frames
probe = ffmpeg.probe(IN_PATH + FILE)
vInfo = next(s for s in probe['streams'] if s['codec_type'] == 'video')
framesNum = int(vInfo['nb_frames'])
framerate = eval(vInfo['avg_frame_rate'])
fps = FRAMES / framesNum * framerate

# Export frames
os.system(
    "ffmpeg -loglevel panic " +
    "-i " + IN_PATH + FILE + " " +
    "-vf fps=" + str(fps) + " " +
    OUT_PATH + FILE.split(".")[0] + "%04d.jpg " +
    "-hide_banner"
)
