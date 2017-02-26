#get local packet recved
import os
#netcard : lo,wlan0,eth0
def getnetstat(netcard):
    pf = open('/proc/net/dev')
    lines = pf.readlines()
    
    item = {}
    for line in lines:
        ifstat = line.split()
        pos = ifstat[0].find(":")
        if pos < 0 :
            continue
        
        k = ifstat[0].rstrip(":")
        if k == netcard:
            #get packets
            #print ifstat
            v = ifstat[2]
            return int(v)
