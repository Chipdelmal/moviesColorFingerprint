#   colorFingerprint

These routines take a movie, and export it's color fingerpring by calculating the dominant colors present in uniformly-spaced frames across the video.

##  Instructions

1. Place the movie in the `./original/` folder, and run the `rescaleMovie.py` script to downscale the size (640x320 is recommended).
2. Export the frames by running the `exportFrames.py` script (500 is recommended). The frames will be exported to the `./temp/` folder.
3. Run the `mainFrames.py` script to export the fingerprint. The resulting file will be exported to the `./out/` folder.


## Author

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
