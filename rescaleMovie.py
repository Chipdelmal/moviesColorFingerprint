import os

(FILE_NAME, IN_PATH, OUT_PATH) = ('nausicaa.mp4', './in/', './out/')
(width, height) = (640, 320)

os.system(
    "ffmpeg -loglevel panic " +
    "-i " + IN_PATH + FILE_NAME + " " +
    "-vf scale=" + str(width) + ":" + str(height) + " " +
    OUT_PATH + FILE_NAME
)
