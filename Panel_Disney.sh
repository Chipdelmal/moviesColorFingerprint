#!/bin/bash

# PT_I='/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/Disney'
# PT_O='/media/chipdelmal/c158f7c2-ba1a-4b6b-9428-6f4babaa84d1/Disney/Art'
PT_I='/media/chipdelmal/Eunie/Disney'
PT_O='/media/chipdelmal/Eunie/Disney/Art'
###############################################################################
# Filenames and titles
###############################################################################
F_NAMES=(
    "1937_SnowWhiteAndTheSevenDwarfs.mp4"
    "1940_Fantasia.mp4" "1940_Pinocchio.mp4" "1941_Dumbo.mp4" "1941_TheReluctantDragon.mp4"
    "1942_Bambi.mp4" "1942_SaludosAmigos.mp4" "1944_TheThreeCaballeros.mp4"
    "1946_MakeMineMusic.mp4" "1947_FunAndFancyFree.mp4" "1948_MelodyTime.mp4" "1949_TheAdventuresOfIchabodAndMrToad.mp4"
    "1950_Cinderella.mp4" "1951_AliceInWonderland.mp4" "1953_PeterPan.mp4" 
    "1955_LadyAndTheTramp.mp4" "1959_SleepingBeauty.mp4"
    "1961_101Dalmatians.mp4" "1963_TheSwordInTheStone.mp4"
    "1967_TheJungleBook.mp4"
    "1970_TheAristocats.mp4" "1973_RobinHood.mp4"
    "1977_TheManyAdventuresOfWinnieThePooh.mp4" "1977_TheRescuers.mp4"
    "1981_TheFoxAndTheHound.mp4" "1985_TheBlackCauldron.mp4"
    "1986_TheAdventuresOfTheGreatMouseDetective.mp4"
    "1988_OliverAndCompany.mp4" "1989_TheLittleMermaid.mp4"
    "1990_TheRescuersDownUnder.mp4" "1990_DuckTalesTreasureOfTheLostLamp.mp4"
    "1991_BeautyAndTheBeast.mp4" "1992_Aladdin.mp4" 
    "1993_TheNightmareBeforeChristmas.mp4" "1995_AGoofyMovie.mp4"
    "1994_TheLionKing.mp4" "1995_Pocahontas.mp4" "1996_TheHunchbackOfNotreDame.mp4"
    "1995_ToyStory.mp4" "1996_JamesAndTheGiantPeach.mp4" "1997_Hercules.mp4" "1999_Tarzan.mp4"
    "1999_Fantasia2000.mp4" "2000_TheEmperorsNewGroove.mp4" "2000_Dinosaur.mp4" 
    "2002_TreasurePlanet.mp4" "2003_BrotherBear.mp4" "2005_Valiant.mp4"
    "2006_Cars.mp4" "2007_Enchanted.mp4" "2008_WallE.mp4" "2010_TinkerBellAndTheGreatFairyRescue.mp4" "2011_WinnieThePooh.mp4" "2013_TheWindRises.mp4"
    "2013_Frozen.mp4" "2013_Planes.mp4"
    "2014_BigHero.mp4" "2014_PlanesFireAndRescue.mp4" "2014_TinkerBellAndThePirateFairy.mp4" "2016_TheJungleBook.mp4"
    "2016_Moana.mp4" "2017_Cars3.mp4" "2017_Coco.mp4" "2018_MaryPoppinsReturns.mp4" "2019_Aladdin.mp4" "2019_MalifiscentMistressOfEvil.mp4"
    "2019_TheLionKing.mp4" "2019_Frozen2.mp4"
    "2021_Encanto.mp4" "2021_RayaAndTheLastDragon.mp4" "2021_TinkerBellAndTheLegendOfTheNeverBeast.mp4" "2022_TurningRed.mp4"
    "2022_Lightyear.mp4"
)
M_NAMES=(
    "Snow White and the Seven Dwarfs\n(1937)"
    "Fantasia\n(1940)" "Pinocchio\n(1940)" "Dumbo\n(1941)" "The Reluctant Dragon\n(1941)"
    "Bambi\n(1942)" "Saludos Amigos\n(1942)" "The Three Caballeros\n(1944)"
    "Make Mine Music\n(1947)" "Fun and Fancy Free\n(1947)" "Melody Time\n(1948)" "The Adventures of Ichabod and Mr. Toad\n(1949)"
    "Cinderella\n(1950)" "Alice in Wonderland\n(1951)" "Peter Pan\n(1953)"
    "Lady and the Tramp\n(1955)" "Sleeping Beauty\n(1959)"
    "101 Dalmatians\n(1961)" "The Sword in the Stone\n(1963)"
    "The Jungle Book\n(1967)"
    "The Aristocats\n(1970)" "Robin Hood\n(1973)"
    "The Many Adventures of Winnie the Pooh\n(1977)" "The Rescuers\n(1977)"
    "The Fox and the Hound\n(1981)" "The Black Cauldron\n(1985)"
    "The Adventures of the Great Mouse Detective\n(1986)"
    "Oliver and Company\n(1988)" "The Little Mermaid\n(1989)"
    "The Rescuers Down Under\n(1990)" "Duck Tales: Treasure of the Lost Lamp\n(1990)"
    "Beauty and the Beast\n(1991)" "Aladdin\n(1992)"
    "The Nightmare Before Christmas\n(1993)" "A Goofy Movie\n(1995)"
    "The Lion King\n(1994)" "Pocahontas\n(1995)" "The Hunchback of Notre Dame\n(1996)"
    "Toy Story\n(1995)" "James and the Giant Peach\n(1996)" "Hercules\n(1997)" "Tarzan\n(1999)"
    "Fantasia 2000\n(1999)" "The Emperor's New Groove\n(2000)" "Dinosaur\n(2000)"
    "Treasure Planet\n(2002)" "Brother Bear\n(2003)" "Valiant\n(2005)"
    "Cars\n(2006)" "Enchanted\n(2007)" "WALL-E\n(2008)" "Tinker Bell and the Great Fairy Rescue\n(2010)" "Winnie the Pooh\n(2011)" "The Wind Rises\n(2013)"
    "Frozen\n(2013)" "Planes\n(2013)"
    "Big hero\n(2014)" "Planes: Fire & Rescue\n(2014)" "Tinker Bell and the Pirate Fairy\n(2014)" "The Jungle Book\n(2016)"
    "Moana\n(2016)" "Cars 3\n(2017)" "Coco\n(2017)" "Mary Poppins Returns\n(2018)" "Aladdin\n(2019)" "Maleficent: Mistress of Evil\n(2019)"
    "The Lion King\n(2019)" "Frozen II\n(2019)"
    "Encanto\n(2021)" "Raya and the Last Dragon\n(2021)" "Tinker Bell and the Legend of the Never Beast\n(2021)" "Turning Red\n(2022)"
    "Lightyear\n(2022)"
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
    -bs 10 -bsa 10 -bc 255 \
    -w 3960 -c 10 \
    --interpolation lanczos \
    -y