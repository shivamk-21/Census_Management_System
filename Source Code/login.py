from tkinter import *
from tkinter import font,messagebox
from functools import partial
import sql

Login=Tk()
Login.state("zoomed")
Login.iconbitmap("images//icon.ico")
Login.overrideredirect(1)
Login.wm_attributes('-transparentcolor','red')
Font=font.Font(family='arial')
r=list()
#Functions
def login(usertype):
    global r
    r=sql.check(usertype,Text1.get(),Text2.get())
    r.insert(0,usertype)
    if len(r)>1:
        Login.destroy()
    else:
        messagebox.showerror("Error","Wrong Username or Password")
#Frames
frame1=Frame(Login,bg='red')
frame2=Frame(frame1)
#Image
image1 = PhotoImage(file="images/login.png")
image2 = PhotoImage(file="images/btn.png")
image2=image2.subsample(1,2)
#Labels
lbl1=Label(frame2,text='Username/Reg No',font=Font,fg='white',image=image2,compound='center',borderwidth=0,bg='black')
lbl2=Label(frame2,text='Password/Aadhar',font=Font,fg='white',image=image2,compound='center',borderwidth=0,bg='black')
lbl3=Label(frame2,image=image1)
#Textboxes
Text1=Entry(frame2,font=Font)
Text2=Entry(frame2,font=Font,show="*")
#Buttons
btn1=Button(frame2,text='Admin Login',fg='white',image=image2,compound='center',font=Font,command=partial(login,'admin'),borderwidth=0,bg='black')
btn2=Button(frame2,text='Citizen Login',fg='white',image=image2,compound='center',font=Font,command=partial(login,'citizen'),borderwidth=0,bg='black')
#Packing
lbl1.grid(row=1,column=1,padx=5,pady=5)
lbl2.grid(row=2,column=1,padx=5,pady=5)
Text1.grid(row=1,column=2,padx=5,pady=5)
Text2.grid(row=2,column=2,padx=5,pady=5)
btn1.grid(row=3,column=1,padx=5,pady=5)
btn2.grid(row=3,column=2,padx=5,pady=5)
lbl3.place(relx=.5, rely=.5, anchor="center")
lbl3.lower()
frame2.rowconfigure(0,minsize=180)
frame2.columnconfigure(0,minsize=150)
frame1.pack(fill=BOTH,expand=True)
frame2.place(relx=.5, rely=.5, anchor="center",height=500,width=700)
#Mainloop
Login.mainloop()
