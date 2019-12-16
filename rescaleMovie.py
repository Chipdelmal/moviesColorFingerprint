# ############################################################################
# Color Fingerprint: rescaleMovie.py
#   This auxiliary script rescales a movie using ffmpeg
# ############################################################################
import os

# User Inputs
(FILE_NAME, DIMS) = ('goldenDays.mp4', (640, 320))
(IN_PATH, OUT_PATH) = ('./original/', './rescaled/')

# Call to ffmpeg's for rescaling
os.system(
        "ffmpeg -loglevel panic "
        + "-i " + IN_PATH + FILE_NAME + " "
        + "-vf scale=" + str(DIMS[0]) + ":" + str(DIMS[1]) + " "
        + OUT_PATH + FILE_NAME
    )
