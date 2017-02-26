#定时任务的邮件提醒功能

from threading import Timer
import time
class notify():
    taskid = 0
    def loop(self):
        self.exm()
        t = Timer(3,self.loop)
        t.start()
    def mailnotfiy(self,taskinfo):
        return
    def exm(self):
       print 'hello',time.localtime()

def hl():
    print 'hello',time.localtime()
    
    #start timer again
    x = Timer(3,hl)
    x.start()    
#t = Timer(3,hl)
#t.start()

n = notify()
n.loop()