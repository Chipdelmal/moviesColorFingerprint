
import os

FILE = "PrincessMononoke.mp4"
(IN_PATH, OUT_PATH, FPS) = ("./in/", "./temp/", 1/60)

os.system(
    "ffmpeg -loglevel panic " +
    "-i " + IN_PATH + FILE + " " +
    "-vf fps=" + str(FPS) + " " +
    OUT_PATH + FILE.split(".")[0] + "%04d.jpg " +
    "-hide_banner"
)
