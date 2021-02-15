import smtplib
import winsound
from plyer import notification



sender = 'talrejasanjana28@gmail.com'


message = """From: ATLAS Alert <talrejasanjana28@gmail.com>
Subject: Alert- App Used beyond time limit.

This is an auto-generated alert to notify that you have exceeded your daily app usage time limit.
"""

def notif():
    notification.notify( 
            title = "ALERT!", 
            message=" DAILY TIME LIMIT OF FACEBOOK USAGE EXCEEDED" , 
            timeout=2)
  
    
def beep():
    f=1000
    d=2000
    winsound.Beep(f,d)
    
def send(mail):
    if len(mail)==0:
        return
    ob=smtplib.SMTP('smtp.gmail.com', 587)
    ob.starttls()
    ob.login("talrejasanjana28@gmail.com","sanjana287")
    receiver = mail
    ob.sendmail(sender,receiver,message)
    ob.quit()
    


