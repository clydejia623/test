#-*- coding: utf-8 -*-
#udp client, sender and receiver.
#测试udp传输的丢包率情况
import socket
import time
import string
import sys,getopt

class udpSender():
    host = '127.0.0.1'
    port = 10001
    testtime = 3600   #测试时长，s
    concurr = 1  #并发路数
    packinterval = 20 #ms
    socklist = []
    portlist = []
    timestemplist = []
    lastshowsec = 0 
    #init
    def __init__(self,h='127.0.0.1',p=10001,t=10,c=1,i=20):
        self.host = h
        self.port = p
        self.testtime = t
        self.concurr = c
        self.packinterval = i
        
    def initsender(self):
        for i in range(0,self.concurr):
            ts = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.socklist.append(ts)
            self.portlist.append(self.port+i)
            
            self.timestemplist.append(0)
            
    def dosend(self):
        #endtime = time.localtime + self.testtime; #in second
        while True:
            if False: #nowtime >= endtime:
                print 'test end'
                break
            for i in range(0,self.concurr):
                #every session
                self.sendpacket(self.socklist[i],self.host,self.portlist[i],self.timestemplist[i])
                self.timestemplist[i] += 1
                
            self.showloss()
            time.sleep(float(self.packinterval)/1000)
        return
    
    def sendpacket(self,sock,h,p, stemp):
        msg = str(stemp) + 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        sock.sendto(msg,(h,p))
        #print 'send ok ',h,p
        return
    def showloss(self):
        #every second show once
        t = time.localtime()
        if t.tm_sec != self.lastshowsec:
            for index in range(0,self.concurr):
                print 'port:%d,sendTotal:%d' % (self.portlist[index],self.timestemplist[index])
            self.lastshowsec = t.tm_sec;
        
class udpReceiver():
    socklist = []
    portlist = []
    port = 10001
    host = '0.0.0.0'
    lastsemp = []
    recvtotal = []
    recvlost = []
    lastshowsec = 0
    def __init__(self,port=10001,concurr=1):
        self.port = port
        self.concurr = concurr
        return
    def initsock(self):
        for i in range(0,self.concurr):
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.socklist.append(s)
            self.portlist.append(i+self.port)
            
            self.socklist[i].bind((self.host,self.portlist[i]))
            self.lastsemp.append(-1)
            self.recvtotal.append(0)
            self.recvlost.append(0)
        return
    def dorecv(self):
        while True:
            for i in range(0,self.concurr):
                data,addr = self.socklist[i].recvfrom(2048)
                if not data:
                    print 'client exist'
                else:
                    #print data
                    pos = string.index(data,'a')
                    thisstemp = int(data[0:pos])
                    if self.lastsemp[i] != -1:
                        if thisstemp != self.lastsemp[i]+1:
                            #print 'pack loss, lost port:%d,from:%d,to:%d' %(self.portlist[i],self.lastsemp[i]+1,thisstemp-1)
                            self.recvlost[i] += thisstemp - self.lastsemp[i] - 1
                        else:
                            #packet correct
                            pass
                    else:
                        pass
                    self.lastsemp[i] = thisstemp
                    self.recvtotal[i] += 1
            self.showloss()
                    
    def showloss(self):
        #every second show once
        t = time.localtime()
        if t.tm_sec != self.lastshowsec:
            for index in range(0,self.concurr):
                lossrate = 0
                if self.recvtotal[index]+self.recvlost[index] != 0:
                    lossrate = int(self.recvlost[index]*100/(self.recvtotal[index]+self.recvlost[index]))
                print 'port:%d,recvtotal:%d,losttotal:%d,lostrate:%d' % (self.portlist[index],
                                                                           self.recvtotal[index], self.recvlost[index], 
                                                                           lossrate)
            self.lastshowsec = t.tm_sec;    
class rtpSender():
    pass
class rtpReceiver():
    pass

if __name__ == "__main__":
    
    #get cmd options
    #udptester.py -s -h 119.29.171.248 -p 10001 -c 1000 -t 10 -i 20
    #udptester.py -r
    #-s for sender,-r for receiver,
    #c,concurrency,t,testtime(s),i,packet interval(ms)
    sender = False
    recver = False
    peerport = 10001
    concurr = 1
    testtime = 10
    packinterval = 20
    opts,args = getopt.getopt(sys.argv[1:],"srh:p:c:t:i:")
    for op,val in opts:
        if op=='-s':
            sender = True
        if op =='-r':
            recver = True
        if op=='-h':
            peerhost = val
        if op=='-p':
            peerport = val
        if op=='-c':
            concurr = int(val)
        if op=='-t':
            testtime = val
        if op=='-i':
            packinterval = val
    print packinterval
    
    if sender == True:
        #do send process
        sder = udpSender(h=peerhost,p=int(peerport),c=int(concurr),t=int(testtime),i=int(packinterval))
        sder.initsender()
        sder.dosend()
    if recver == True:
        #do recv process
        recver = udpReceiver(port=int(peerport),concurr=int(concurr))
        recver.initsock()
        recver.dorecv()