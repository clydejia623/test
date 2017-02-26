import smtplib
from email.mime.text  import MIMEText
#send mail class
class smtp_send():
    def initmail(self,type,usessl,host,usr,pwd):
        if type == 'smtp':
            self.svr = smtplib.SMTP()

            self.svr.connect(host)
            if usessl == True:
                self.svr.starttls()
            self.svr.login(usr,pwd)
            return True
    def sendmail(self,frommail,tomail,subject,content):
        msg = MIMEText(content)
        msg['Subject'] =  subject
        msg['From'] = frommail
        msg['To'] = tomail
        self.svr.sendmail(frommail,tomail,msg.as_string())
        return True



#ucphost = 'mail.ucpaas.com'
#ucpusr = 'jiajunjie@ucpaas.com'
#ucppwd = '19810623'
#sm.initmail('smtp',False,ucphost,ucpusr,ucppwd)
#sm.sendmail('jiajunjie@ucpaas.com','16408015@qq.com','hello world','good man, just do it')