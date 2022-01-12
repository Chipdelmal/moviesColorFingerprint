#!/bin/bash

PT_I='/mnt/Luma/Videos/Movies'
PT_O='/mnt/Luma/Pictures/Art/Movies/Disney/'

###############################################################################
# Disney Animated Films
###############################################################################
./fingerprint.sh $PT_I $PT_O "1937_SnowWhite.mp4" "Snow White and the Seven Dwarfs (1937)"
./fingerprint.sh $PT_I $PT_O "1940_Fantasia.mp4" "Fantasia (1940)"
./fingerprint.sh $PT_I $PT_O "1940_Pinocchio.mp4" "Pinocchio (1940)"
./fingerprint.sh $PT_I $PT_O "1941_Dumbo.mp4" "Dumbo (1941)"
./fingerprint.sh $PT_I $PT_O "1942_Bambi.mp4" "Bambi (1942)"
./fingerprint.sh $PT_I $PT_O "1950_Cinderella.mp4" "Cinderella (1950)"
./fingerprint.sh $PT_I $PT_O "1951_AliceInWonderland.mp4" "Alice in Wonderland (1951)"
./fingerprint.sh $PT_I $PT_O "1953_PeterPan.mp4" "Peter Pan (1953)"
./fingerprint.sh $PT_I $PT_O "1955_LandyAndTheTramp.mp4" "Lady and the Tramp (1955)"
./fingerprint.sh $PT_I $PT_O "1961_OneHundredAndOneDalmatians.mp4" "One Hundred and One Dalmatians (1961)"
./fingerprint.sh $PT_I $PT_O "1963_TheSwordInTheStone.mp4" "The Sword in the Stone (1963)"
./fingerprint.sh $PT_I $PT_O "1967_TheJungleBook.mp4" "The Jungle Book (1967)"
./fingerprint.sh $PT_I $PT_O "1970_TheAristocats.mp4" "The Aristocats (1970)"
./fingerprint.sh $PT_I $PT_O "1973_RobinHood.mp4" "Robin Hood (1973)"
./fingerprint.sh $PT_I $PT_O "1974_TheRescuers.mp4" "The Rescuers (1977)"
./fingerprint.sh $PT_I $PT_O "1981_TheFoxAndTheHound.mp4" "The Fox and the Hound (1981)"
./fingerprint.sh $PT_I $PT_O "1985_TheBlackCauldron.mp4" "The Black Cauldron (1985)"
./fingerprint.sh $PT_I $PT_O "1989_TheLittleMermaid.mp4" "The Little Mermaid (1989)"
./fingerprint.sh $PT_I $PT_O "1986_TheGreatMouseDetective.mp4" "The Great Mouse Detective (1986)"
./fingerprint.sh $PT_I $PT_O "1988_OliverAndCompany.mp4" "Oliver & Company (1988)"
./fingerprint.sh $PT_I $PT_O "1991_BeautyAndTheBeast.mp4" "Beauty and the Beast (1991)"
./fingerprint.sh $PT_I $PT_O "1992_Aladdin.mp4" "Aladdin (1992)"
./fingerprint.sh $PT_I $PT_O "1994_TheLionKing.mp4" "The Lion King (1994)"
./fingerprint.sh $PT_I $PT_O "1995_Pocahontas.mp4" "Pocahontas (1995)"
./fingerprint.sh $PT_I $PT_O "1996_TheHunchbackOfNotreDame.mp4" "The Hunchback of Notre Dame (1996)"
./fingerprint.sh $PT_I $PT_O "1997_Hercules.mp4" "Hercules (1997)"
./fingerprint.sh $PT_I $PT_O "1998_Mulan.mp4" "Mulan (1998)"
./fingerprint.sh $PT_I $PT_O "1999_Tarzan.mp4" "Tarzan (1999)"
./fingerprint.sh $PT_I $PT_O "2000_Dinosaur.mp4" "Dinosaur (2000)"
./fingerprint.sh $PT_I $PT_O "2000_TheEmperorsNewGroove.mp4" "The Emperor's New Groove (2000)"
./fingerprint.sh $PT_I $PT_O "2001_AtlantisTheLostEmpire.mp4" "Atlantis: The Lost Empire (2001)"
./fingerprint.sh $PT_I $PT_O "2002_LiloAndStitch.mp4" "Lilo & Stitch (2002)"
./fingerprint.sh $PT_I $PT_O "2002_TreasurePlanet.mp4" "Treasure Planet (2002)"
./fingerprint.sh $PT_I $PT_O "2003_BrotherBear.mp4" "Brother Bear (2003)"
./fingerprint.sh $PT_I $PT_O "2004_HomeOnTheRange.mp4" "Home on the Range (2004)"
./fingerprint.sh $PT_I $PT_O "2005_ChickenLittle.mp4" "Chicken Little (2005)"
./fingerprint.sh $PT_I $PT_O "2007_MeetTheRobinsons.mp4" "Meet the Robinsons (2007)"
./fingerprint.sh $PT_I $PT_O "2008_Bolt.mp4" "Bolt (2008)"
./fingerprint.sh $PT_I $PT_O "2009_ThePrincessAndTheFrog.mp4" "The Princess and the Frog (2009)"
./fingerprint.sh $PT_I $PT_O "2010_Tangled.mp4" "Tangled (2010)"
./fingerprint.sh $PT_I $PT_O "2011_WinnieThePooh.mp4" "Winnie the Pooh (2011)"
./fingerprint.sh $PT_I $PT_O "2012_WreckItRalph.mp4" "Wreck-It Ralph (2012)"
./fingerprint.sh $PT_I $PT_O "2013_Frozen.mp4" "Frozen (2013)"
./fingerprint.sh $PT_I $PT_O "2014_BigHero6.mp4" "Big Hero 6 (2014)"
./fingerprint.sh $PT_I $PT_O "2016_Zootopia.mp4" "Zootopia (2016)"
./fingerprint.sh $PT_I $PT_O "2016_Moana.mp4" "Moana (2016)"
./fingerprint.sh $PT_I $PT_O "2021_RayaAndTheLastDragon.mp4" "Raya and the Last Dragon (2021)"
./fingerprint.sh $PT_I $PT_O "2021_Encanto.mp4" "Encanto (2021)"

image-grid --folder /mnt/Luma/Pictures/Art/Movies/Disney/ -bs 0 -y -n 48 -r 48 -w 7750 --out /mnt/Luma/Pictures/Art/Movies/Disney/image-grid.png