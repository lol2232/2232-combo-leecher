import os
import sys
import requests
from multiprocessing import Queue
from time import sleep
import time
import colorama 
from colorama import Fore, Back, Style

colorama.init()
print(Fore.BLUE)
print( """\

                    _             _                _     
  ___ ___  _ __ ___ | |__   ___   | | ___  ___  ___| |__  
 / __/ _ \| '_ ` _ \| '_ \ / _ \  | |/ _ \/ _ \/ __| '_ \ 
| (_| (_) | | | | | | |_) | (_) | | |  __/  __/ (__| | | |
 \___\___/|_| |_| |_|_.__/ \___/  |_|\___|\___|\___|_| |_|

github: MilesBoi

free combolists!!!!!

""")

sleep(5)
q = Queue()
qcount = 0
try:
    os.system("touch " + sys.argv[2])
except:
    print("usage 2232-LEECHER.py inputfile outputfile")
try:
    ff = open(sys.argv[1], "r")
except:
    print(Fore.BLUE)
    print("usage 2232-LEECHER.py inputfile outputfile")
    sys.exit()
links = [line.replace('\n','') for line in ff]
for link in links:
    qcount +=1
    q.put(link)
pasteids = q.get()
for link in links:
    asd = (str(q.get()) + "/download/")
    asd1 = requests.get(asd).text
    try:
        open(sys.argv[2], "r+", encoding="utf8", errors="ignore").write(asd1 + "\n")
    except:
        print(Fore.BLUE)
        print("usage 2232-LEECHER.py inputfile outputfile")
        sys.exit()
    print(asd1)
else:
     print("fail?")
sys.exit()
