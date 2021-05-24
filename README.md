#   Movies' Color Fingerprint

These routines take a movie, and export it's color fingerprint by calculating the dominant colors present in uniformly-spaced frames across the video. They do so by splitting a movie into frames, clustering the colors in each of the frames, and plotting the most prevalent ones in a heatmap (x-axis shows time, while the y-axis shows the different clusters of colors).


**Princess Mononoke**
<img src="./media/PrincessMononoke.jpg">
**Spirited Away**
<img src="./media/SpiritedAway.jpg">
**Nausicaä of the Valley of the Wind**
<img src="./media/Nausicaa.jpg">
**The Wind Rises**
<img src="./media/TheWindRises.jpg">
**Castle in the Sky**
<img src="./media/CastleInTheSky.jpg">



##  Instructions

After installing the dependencies, run the *bash* script as follows:

```bash
./fingerprint.sh VIDEO_FOLDER OUTPUT_FOLDER VIDEO_NAME MOVIE_TITLE_STRING
```

For example, the following call looks for the `Totoro.mp4` file in the `./Movies` path and generates the output in the `./Art` folder with the supplied title:

```bash
./fingerprint.sh './Movies' './Art' 'Nausicaa.mp4' 'Nausica0xC3\nof the\nValley\nof the\nWind'
```

Which exports this fingerprint:

<img src="./media/NausicaaWind.jpg">

##  Requirements and Dependencies

These routines need [ffmpeg](https://ffmpeg.org/) to re-scale the movie and export frames to disk. Additionally, the following python libraries are needed: [ffmpeg-python](https://pypi.org/project/ffmpeg-python/), [scikit-learn](https://scikit-learn.org/), [matplotlib](https://matplotlib.org/), [numpy](https://numpy.org/).

These libraries can be installed manually, or to anaconda environments with:

```bash
conda env create -f REQUIREMENTS.yml
```

or 

```bash
conda create -n new fingerprint --file REQUIREMENTS.txt
```

## Author

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
