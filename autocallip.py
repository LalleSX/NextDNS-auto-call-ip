from asyncore import write
import requests
import datetime
import os 
# dirrec is the logfile output directory
# r is is the website you want to connect to and log
direc = "[LOG OUTPUT DIRECTORY HERE REMOVE BRACKETS]"
r = requests.get('[ADD NEXTDNS URL HERE REMOVE BRACKETS]')

x = datetime.datetime.now()
logfile = direc+x.strftime("%b")+"_Nextdns.txt" #%d for day %b for month-name %c for something like: Mon Dec 31 17:41:00 2018
if os.path.exists(logfile): 
    os.remove(logfile)
with open(logfile,"x") as f:
    f.write(r.text+ x.strftime(" %c"))
    f.close()
