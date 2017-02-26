from flask import Flask, request,render_template
import random
import json
import time
import localnetstat
import thread
#import collectdata
import MySQLdb

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    return render_template("mon.html")

@app.route("/signup",methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/signup",methods=["POST"])
def signupok():
    un = request.form['un'];
    pwd = request.form['pwd']
    return render_template("signup_ok.html",uname=un)

@app.route("/moncpu", methods = ["GET"])
def moncpu():
    return render_template("moncpu.html")

@app.route("/data",methods=["GET"])
def getdata():
    item = ""
    '''
    for i in range(0,2000):
            n = random.randint(1,100)
            v = random.randint(0,100)
            item += "%i(%i);" % (i,v)    
    return item
    '''
    #example:
    #ones = [[100,20],[200,30],[300,40]]
    ones = []
    for i in range(0,30):
        tupt = (2016,6,26,6,i,0,0,0,0)
        t = time.mktime(tupt)
        #highstock use UTC time,must change to china local time
        t = t + 8*3600
        # highstock use milisecond, t*1000
        t = t*1000
        x = [t,random.randint(i*10,i*20)]
        ones.append(x)
    item = "%s(%s);"%(request.args.get("callback"),json.dumps(ones))
    print item
    return item

@app.route("/cpudata", methods = ["GET"])
def getcpudata_chart():
    r = getcpudata()
    rlt = "%s(%s);" % (request.args.get("callback"),json.dumps(r))
    return rlt
    
#get cpuinfo from mysql
def getcpudata():
    cpurate = []
    conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "19810623", db = "perf_info")
    cur = conn.cursor()
    
    #get today start time
    today = time.localtime()
    tmp = (today[0],today[1],today[2],0,0,0,today[6],today[7],today[8])
    
    startseq = time.mktime(tmp)
    
    #fetch cpudata (today)
    sql = "select * from cpuinfo where timeseq >= %d" % (startseq)
    
    cur.execute(sql)
    lines = cur.fetchall()
    for k in lines:
        cpurate.append([(1000*(k[1]+8*3600)),k[2]])
    return cpurate


@app.route("/ucpaasdelay", methods = ["GET"])
def ucpaasdelay():
    return render_template("ucpaasdelay.html")

@app.route("/ucpaasdelay_data", methods = ["GET"])
def ucpaasdelay_data():
    r = get_ucpaasdelay_data()
    rlt = "%s(%s);" % (request.args.get("callback"),json.dumps(r))
    return rlt

#get cpuinfo from mysql
def get_ucpaasdelay_data():
    delay = []
    conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "19810623", db = "perf_info")
    cur = conn.cursor()
    
    #get today start time
    today = time.localtime()
    tmp = (today[0],today[1],today[2],0,0,0,today[6],today[7],today[8])
    
    startseq = time.mktime(tmp)
    
    #fetch delay (today)
    sql = "select * from ucpaasdelay where timeseq >= %d" % (startseq)
    
    cur.execute(sql)
    lines = cur.fetchall()
    for k in lines:
        delay.append([(1000*(k[1]+8*3600)),k[2]])
    return delay

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
    print 'hell'
    