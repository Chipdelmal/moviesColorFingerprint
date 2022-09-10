#!/bin/bash

PT_I='/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/Disney'
PT_O='/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/Disney/Art'
###############################################################################
# Filenames and titles
###############################################################################
F_NAMES=(
    "1937_SnowWhiteAndTheSevenDwarfs.mp4"
    "1940_Fantasia.mp4" "1940_Pinocchio.mp4" "1941_Dumbo.mp4" "1941_TheReluctantDragon.mp4"
    "1942_Bambi.mp4" "1942_SaludosAmigos.mp4" "1944_TheThreeCaballeros.mp4"
    "1948_MelodyTime.mp4" "1949_TheAdventuresOfIchabodAndMrToad.mp4"
    "1950_Cinderella.mp4" "1951_AliceInWonderland.mp4" "1953_PeterPan.mp4" 
    "1955_LadyAndTheTramp.mp4" "1959_SleepingBeauty.mp4"
    "1961_101Dalmatians.mp4" "1963_TheSwordInTheStone.mp4"
    "1967_TheJungleBook.mp4"
    "1970_TheAristocats.mp4" "1973_RobinHood.mp4"
    "1977_TheManyAdventuresOfWinnieThePooh.mp4" "1977_TheRescuers.mp4"
    "1981_TheFoxAndTheHound.mp4" "1985_TheBlackCauldron.mp4"
    "1986_TheAdventuresOfTheGreatMouseDetective.mp4"
    "1988_OliverAndCompany.mp4" "1989_TheLittleMermaid.mp4"
    "1990_TheRescuersDownUnder.mp4" "1991_BeautyAndTheBeast.mp4" "1992_Aladdin.mp4" 
    "1993_TheNightmareBeforeChristmas.mp4" "1995_AGoofyMovie.mp4"
    "1994_TheLionKing.mp4" "1995_Pocahontas.mp4" "1997_Hercules.mp4" "1999_Tarzan.mp4"
    "2000_TheEmperorsNewGroove.mp4" "2000_Dinosaur.mp4"
)
M_NAMES=(
    "Snow White and the Seven Dwarfs\n(1937)"
    "Fantasia\n(1940)" "Pinocchio\n(1940)" "Dumbo\n(1941)" "The Reluctant Dragon\n(1941)"
    "Bambi\n(1942)" "Saludos Amigos\n(1942)" "The Three Caballeros\n(1944)"
    "Melody Time\n(1948)" "The Adventures of Ichabod and Mr. Toad\n(1949)"
    "Cinderella\n(1950)" "Alice in Wonderland\n(1951)" "Peter Pan\n(1953)"
    "Lady and the Tramp\n(1955)" "Sleeping Beauty\n(1959)"
    "101 Dalmatians\n(1961)" "The Sword in the Stone\n(1963)"
    "The Jungle Book\n(1967)"
    "The Aristocats\n(1970)" "Robin Hood\n(1973)"
    "The Many Adventures of Winnie the Pooh\n(1977)" "The Rescuers\n(1977)"
    "The Fox and the Hound\n(1981)" "The Black Cauldron\n(1985)"
    "The Adventures of the Great Mouse Detective\n(1986)"
    "Oliver and Company\n(1988)" "The Little Mermaid\n(1989)"
    "The Rescuers Down Under\n(1990)" "Beauty and the Beast\n(1991)" "Aladdin\n(1992)"
    "The Nightmare Before Christmas\n(1993)" "A Goofy Movie\n(1995)"
    "The Lion King\n(1994)" "Pocahontas\n(1995)" "Hercules\n(1997)" "Tarzan\n(1999)"
    "The Emperor's New Groove\n(2000)" "Dinosaur\n(2000)"
)
###############################################################################
# Iterate through files
###############################################################################
for idx in "${!F_NAMES[@]}"; do
    file=${F_NAMES[$idx]}
    title=${M_NAMES[$idx]}
    bash fingerprint.sh $PT_I $PT_O "$file" "$title"
done
###############################################################################
# Assemble grid
###############################################################################
image-grid \
    --folder "${PT_O}" \
    --out "${PT_I}/Panel.png" \
    -bs 25  -bc 255 -bsa 25 \
    -w 3960 \
    --interpolation lanczos \
    -y