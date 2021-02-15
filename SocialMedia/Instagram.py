import win32gui
import time
import smtplib
import winsound
from .alerts.alert import notif,beep,send

    
    
def main(t,mail):
    timelimit=t
    total=0
    f=0
    usage=0
    starttime = 0
    while True:
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
                send(mail)
                beep()
                break
                
        elif f==1:
            f=0
            total=total+usage
            if total >= timelimit:
                print("You have used Instagram beyond time limit")
                send(mail)
                beep()
                break
        print(total,usage)
        time.sleep(1)

