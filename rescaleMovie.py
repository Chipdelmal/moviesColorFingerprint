# #############################################################################
# Color Fingerprint: rescaleMovie.py
#   This auxiliary script rescales a movie using ffmpeg
# #############################################################################
import os
import sys
from os import path
import auxiliary as aux
# User inputs -----------------------------------------------------------------
if aux.isNotebook():
    (FILE_NAME, DIMS) = ('Interstellar.mp4', (320*2.4, 320))
    (IN_PATH, OUT_PATH) = (
        '/mnt/Luma/Videos/Movies/', 
        '/mnt/Luma/Videos/Movies/Rescaled/'
    )
else:
    (FILE_NAME, DIMS) = (sys.argv[1], sys.argv[2])
    (IN_PATH, OUT_PATH) = (sys.argv[3], sys.argv[4])
# Call to ffmpeg for rescaling ------------------------------------------------
os.system(
        "ffmpeg -loglevel panic "
        + "-i " + str(path.join(IN_PATH, FILE_NAME)) + " "
        + "-vf scale=" + str(DIMS[0]) + ":" + str(DIMS[1]) + " "
        + str(path.join(OUT_PATH, FILE_NAME))
    )