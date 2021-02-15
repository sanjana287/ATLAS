from tkinter import *
from _thread import *
from SocialMedia.Facebook import main as m1
from SocialMedia.Instagram import main as m2
from SocialMedia.Twitter import main as m3


def execute():
    if var1.get()==0 and var2.get()==0 and var3.get()==0:
        l=Label(frame, text="Nothing has been selected-select atleast one website!", font=("Helvetica",15),bg="black",fg="red")
        l.pack()
        return
    email=s4.get()
    if var1.get():
        time=s1.get()
        time=time*3600
        start_new_thread(m1,(time,email))
    if var2.get():
        time=s2.get()
        time=time*3600
        start_new_thread(m2,(time,email))
    if var3.get():
        time=s3.get()
        time=time*3600
        start_new_thread(m3,(time,email))
    print(var1.get(),var2.get(),var3.get())
    print(s1.get(),s2.get(),s3.get(),s4.get())
    l=Label(frame, text="Yay! Your Time Limits have been successfully set!", font=("Helvetica",15),bg="black",fg="green")
    l.pack()
    
    

root= Tk()
root.title("A.T.L.A.S")
canvas= Canvas(root,width=700,height=700)
canvas.grid(columnspan=3)

frame= Frame(root,bg="black")
frame.place(relwidth=1,relheight=1)

label= Label(frame, text="~ A.T.L.A.S ~", font=("Comic Sans MS",30, "bold"),bg="black",fg="white")
label.pack(side="top",fill=X)
label= Label(frame, text="Your one stop to regulate your social media usage!", font=("Comic Sans MS",15),bg="black",fg="white")
label.pack(side="top",fill=X)



label= Label(frame, text="Select Websites you want to monitor your time for:", font=("Comic Sans MS",15),bg="black",fg="white")
label.pack(side="top",fill=X,pady=10)

l= Label(frame, text="Enter Time Limit in Hours:", font=("Helvetica",13),bg="black",fg="white")
l1= Label(frame, text="Enter Time Limit in Hours:", font=("Helvetica",13),bg="black",fg="white")
l2= Label(frame, text="Enter Time Limit in Hours:", font=("Helvetica",13),bg="black",fg="white")
l3=Label(frame, text="Enter your email below to receive alerts:", font=("Helvetica",15),bg="black",fg="white")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
s1=DoubleVar()
s2=DoubleVar()
s3=DoubleVar()
s4=StringVar()
c1=Checkbutton(frame, text="Facebook", variable=var1,font=("Helvetica",15),bg='black',fg="#5851DB",onvalue=1,offvalue=0)
c2=Checkbutton(frame, text="Instagram", variable=var2,font=("Helvetica",15),bg='black',fg="#FF08A1",onvalue=1,offvalue=0)
c3=Checkbutton(frame, text="Twitter  ", variable=var3,font=("Helvetica",15),bg='black',fg="#1DA1F2",onvalue=1,offvalue=0)

t1 = Entry(frame, width=5,font=("Helvetica",10),borderwidth=2,textvariable=s1)
t2 = Entry(frame, width=5,font=("Helvetica",10),borderwidth=2,textvariable=s2)
t3 = Entry(frame, width=5,font=("Helvetica",10),borderwidth=2,textvariable=s3)
t4 = Entry(frame, width=30,font=("Helvetica",10),borderwidth=4,relief=RIDGE,textvariable=s4)
b= Button(frame,height=1,width=10,text="Submit",fg="green",activebackground="green",command=execute)
c1.pack(side="top",padx=10,pady=5)
l.pack()
t1.pack(pady=5)
c2.pack(side="top",padx=10,pady=5)
l1.pack()
t2.pack(pady=5)
c3.pack(side="top",padx=10,pady=5)
l2.pack()
t3.pack(pady=5)
l3.pack(fill=X,pady=5)
t4.pack(pady=5)
b.pack(pady=20)

root.mainloop()
