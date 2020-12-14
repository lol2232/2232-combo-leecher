# 2232-combo-leecher
i made this myself works on all platforms im still pretty much a python beginner so not the greatest code scrapes throwbin for combos with your keyword then puts them all in a txt

Installation:
 
sudo apt-get install tor dos2unix -y
 
 
pip3 install -r requirements.txt
 
 
Usage:
 
service tor start
 
./gatherlinks.sh; # this will gather your links to leechedlinks.txt
 
python3 2232-LEECHER.py # if you used gatherlinks.sh your inputfile is leechedlinks.txt
 
once it stops moving and it gets stuck at one place you can hit control c its most likely done
 
check if you have the files usercombo.txt or emailcombo.txt if not do this
 
./format.sh
