import win32gui
import time
import smtplib
import winsound
from _thread import *
from .alerts.alert import notif,beep,send

    
    
def main(t,mail):
    timelimit=t
    total=0
    f=0
    usage=0
    starttime = 0
    while True:
        x=time.localtime()
        #setting total=0 if day has changed
        if x[3]==0 and x[4]==0 and total>0:
            total=0
        website= win32gui.GetWindowText(win32gui.GetForegroundWindow())
        print(website)
        if "Instagram" in website:
            if f==0:
                starttime=int(time.time())
                f=1
            current=int(time.time())
            usage=current-starttime
            if usage>=timelimit or (total+usage)>=timelimit:
                print("You have used Instagram beyond time limit")
                start_new_thread(beep,())
                start_new_thread(notif,("INSTAGRAM",))
                send(mail)
                break
                
        elif f==1:
            f=0
            total=total+usage
            if total >= timelimit:
                print("You have used Instagram beyond time limit")
                start_new_thread(beep,())
                start_new_thread(notif,("INSTAGRAM",))
                send(mail)
        print(total,usage)
        time.sleep(1)

