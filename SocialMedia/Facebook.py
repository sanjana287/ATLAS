import win32gui
import time
from _thread import *
from plyer import notification
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
        if "Facebook" in website:
            if f==0:
                starttime=int(time.time())
                f=1
            current=int(time.time())
            usage=current-starttime
            if usage>=timelimit or (total+usage)>=timelimit:
                print("You have used Facebook beyond time limit")
                start_new_thread(beep,())
                start_new_thread(notif,("Facebook"))
                send(mail)
                break
                
        elif f==1:
            f=0
            total=total+usage
            if total >= timelimit:
                print("You have used facebook beyond time limit")
                start_new_thread(beep())
                start_new_thread(notif,("Facebook"))
                send(mail)
                break
        print(total,usage)
        time.sleep(1)

