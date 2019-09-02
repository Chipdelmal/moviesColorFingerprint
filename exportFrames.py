
import os
import ffmpeg

FILE = "GoldenDays.m4v"
(IN_PATH, OUT_PATH, FRAMES) = (
    "./rescaled/",
    "./out/",
    500
)


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
    "-vf scale=1920:-1" + " " +
    OUT_PATH + FILE.split(".")[0] + "%04d.jpg " +
    "-hide_banner"
)
