#-*- coding : UTF-8 -*-
import MySQLdb
import os
import time
import Rest
'''
def getCpuRate():
    tmp = os.popen('top -bi -n 1')
    lines = tmp.readlines()
    firstline = lines[0]
    
    startPos = firstline.index("load average:")
    #print firstline
    #print firstline[startPos+14 : startPos+14+4]
    cpuRate = float(firstline[startPos+14 : startPos+14+4]) * 100
    #print cpuRate
    return cpuRate
'''

def getNowTime():
    tm = time.mktime(time.localtime())
    return tm

def run():
    conn = MySQLdb.connect(host='127.0.0.1', user = 'root', passwd = '19810623', db = 'perf_info')
    cur = conn.cursor()
    
    #get max id
    #maxid
    sql = "select max(id) from ucpaasdelay"
    tmp = cur.execute(sql)
    rlt = cur.fetchone()
    print rlt[0]
    
    if rlt[0] == None:
        idIndex = 1
    else:
        idIndex = rlt[0] + 1
    
    print idIndex
    
    #run
    while(True):
        delay = Rest.ucpaas_delay()
        
        timeInfo = getNowTime()
        
        sql = "insert into ucpaasdelay(id, timeseq, delay) values(%d, %d, %d)" % (idIndex, timeInfo, delay)
        print sql
        cur.execute(sql)
        
        conn.commit()
        idIndex += 1
        print idIndex
        
        #every 60 second
        time.sleep(60)
if __name__ == "__main__":
    run()
    #print getCpuRate()
    #print getNowTime()