import smtplib
import os
import winsound
from plyer import notification


sender = os.getenv('email')
appname=""

def notif(s):
    global appname
    appname=s
    notification.notify( 
            title = "ALERT!",
            message= " DAILY TIME LIMIT OF {s} USAGE EXCEEDED".format(s=s) , 
            timeout=2)
   

def beep():
    f=1000
    d=2000
    winsound.Beep(f,d)
    
def send(mail):
    message = """From: ATLAS Alert <sender>
Subject: Alert- App Used beyond time limit.
This is an auto-generated alert to notify that you have exceeded your daily app usage time limit for {s}.
""".format(s=appname)
    
    if len(mail)==0:
        return
    ob=smtplib.SMTP('smtp.gmail.com', 587)
    ob.starttls()
    email = os.getenv('email')
    password = os.getenv('password')
    ob.login(email,password)
    receiver = mail
    ob.sendmail(sender,receiver,message)
    ob.quit()
