#get local cpu statistics information
#for web display
import json
import os
import sys
import MySQLdb
import string

def getloadaverage():
    r = os.popen("top -bi -n 1")
    ld = r.readlines()
    firstline = ld[0]
    pos1 = firstline.index("load average: ")
    ratetmp = firstline[(pos1+len("load average: ")):(pos1+len("load average: ")+4)]
    rate = string.atof(ratetmp)
    #print rate
    return int(rate*100)

#print getloadaverage()