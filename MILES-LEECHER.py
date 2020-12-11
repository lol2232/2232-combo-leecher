import os
import sys
import requests
from multiprocessing import Queue
from time import sleep
import time

q = Queue()
qcount = 0
try:
    ff = open(sys.argv[1], "r")
except:
    print("usage MILES-LEECHER.py inputfile outputfile")
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
        print("usage MILES-LEECHER.py inputfile outputfile")
        sys.exit()
    print(asd1)
else:
     print("fail?")
