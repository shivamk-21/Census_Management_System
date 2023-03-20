#Import
from tkinter import *
from tkinter import font,messagebox,ttk
import login,sql
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Root App definition
root=Tk()
root.state("zoomed")
root.iconbitmap("images\icon.ico")
root.title("Census Managament Project")
root.minsize(800,600)
#Functions
def logout():
    root.destroy()
def insert(val):
    if sql.check_entries(val[1])==0:
        sql.insert(val)
        messagebox.showinfo("OK","Data Stored")
        logout()
    else:
        messagebox.showerror("Error","Aadhar Number already Used")
        logout()
def new():
    global test
    for x in frame5.winfo_children():
        x.pack_forget()
    text_list=[]
    lbl_names=["Regsitration Number","Aadhar number","Name","Father's Name","Mother's name","Address","Gender","Mobile","DOB","Birthplace","Religion","Caste",
                "Disbaility","Matrimonial Status","Marriage year","No of family members","Litterate","Highest Education","Language 1",
                "language 2","Language 3","Economic Status","Occupation","Mode of Travel to Work","Income"]
    for x in range(25):
        Label(frame5,font=Font,text=lbl_names[x]).grid(row=x,column=0)
        if x==0:
            reg=Label(frame5,text=str(sql.reg()))
            text_list.append(reg)
        elif x in range(2,9):
            text_list.append(Label(frame5,text=""))
        else:
            text_list.append(Entry(frame5))
        text_list[-1].grid(row=x,column=1)
    def verify(uid):
        data=sql.aadhar_data(uid)
        if len(data)==0:
            messagebox.showerror("Error","Wrong Aadhar Number")
            return
        text_list[2].config(text=data[0][1])
        text_list[3].config(text=data[0][2])
        text_list[4].config(text=data[0][3])
        text_list[5].config(text=data[0][4])
        text_list[6].config(text=data[0][5])
        text_list[7].config(text=data[0][6])
        text_list[8].config(text=data[0][7])
    ver=Button(frame5,text="Verify",command=lambda :verify(text_list[1].get()))
    ver.grid(row=1,column=2)
    
    def sub():
        values=[sql.reg(),text_list[1].get()]+[x.get() for x in text_list[9:]]
        insert(values)
    submit=Button(frame5,text="Submit data",command=sub)
    submit.grid(row=25,column=0,columnspan=3)
    if test==0:
        frame4.pack_forget()
        test=1
    else:
        test=0
        frame4.pack()
def summary():
    global test
    for x in frame5.winfo_children():
        x.pack_forget()
    city=sql.find_summary("address_city")
    state=sql.find_summary("address_state")
    gender=sql.find_summary("gender")
    mat=sql.find_summary("matrimonial_status")
    family=sql.find_summary("no_family_members")
    lan1=sql.find_summary("language_1")
    lan2=sql.find_summary("language_2")
    lan3=sql.find_summary("language_3")
    religion=sql.find_summary("religion")
    literacy=sql.find_summary("litterate")
    travel=sql.find_summary("mode_of_travel")
    fig = Figure(figsize=(5, 20))
    plot1 = fig.add_subplot(11,1,1)
    plot1.pie([x[1] for x in city],labels=[x[0] for x in city])
    plot1.set_title("City")
    plot2 = fig.add_subplot(11,1,2)
    plot2.pie([x[1] for x in state],labels=[x[0] for x in state])
    plot2.set_title("state")
    plot3 = fig.add_subplot(11,1,3)
    plot3.pie([x[1] for x in gender],labels=[x[0] for x in gender])
    plot3.set_title("gender")
    plot4 = fig.add_subplot(11,1,4)
    plot4.pie([x[1] for x in mat],labels=[x[0] for x in mat])
    plot4.set_title("Matrimonial Status")
    plot5 = fig.add_subplot(11,1,5)
    plot5.pie([x[1] for x in family],labels=[x[0] for x in family])
    plot5.set_title("No of Family Memebers")
    plot6 = fig.add_subplot(11,1,6)
    plot6.pie([x[1] for x in lan1],labels=[x[0] for x in lan1])
    plot6.set_title("Language 1")
    plot7 = fig.add_subplot(11,1,7)
    plot7.pie([x[1] for x in lan2],labels=[x[0] for x in lan2])
    plot7.set_title("Language 2")
    plot8 = fig.add_subplot(11,1,8)
    plot8.pie([x[1] for x in lan3],labels=[x[0] for x in lan3])
    plot8.set_title("Langauge 3")
    plot9 = fig.add_subplot(11,1,9)
    plot9.pie([x[1] for x in religion],labels=[x[0] for x in religion])
    plot9.set_title("Religion")
    plot10 = fig.add_subplot(11,1,10)
    plot10.pie([x[1] for x in literacy],labels=[x[0] for x in literacy])
    plot10.set_title("Literacy")
    plot11 = fig.add_subplot(11,1,11)
    plot11.pie([x[1] for x in travel],labels=[x[0] for x in travel])
    plot11.set_title("Mode of Travel to Work")
    canvas = FigureCanvasTkAgg(fig,master = frame5)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    if test==0:
        frame4.pack_forget()
        test=1
    else:
        test=0
        frame4.pack()
def view():
    global test
    for x in frame5.winfo_children():
        x.pack_forget()
    
    lbl_names=["Aadhar number","Name","Father's Name","Mother's name","Address","Gender","Mobile","DOB","Regsitration Number","Birthplace","Religion","Caste",
                "Disbaility","Matrimonial Status","Marriage year","No of family members","Litterate","Highest Education","Language 1",
                "language 2","Language 3","Economic Status","Occupation","Mode of Travel to Work","Income"]
    if usertype=="citizen":
        adata=sql.aadhar_data(data[-1])[0]
        adata+=data
        for x in range(25):
            Label(frame5,font=Font,text=(lbl_names[x]+" : "+str(adata[x]))).pack()
    if test==0:
        frame4.pack_forget()
        test=1
    else:
        test=0
        frame4.pack()

#Objects:-
#Values
test=1
Font=font.Font(family='arial')
#Login
try:
    if not len(login.r)>1:
        root.destroy()
    usertype,data=login.r[0],login.r[1]
except IndexError:
    print("Skip")
#frames
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(frame2,borderwidth=20,bg='black')
frame4 = Frame(frame2,bd=15)
canvas=Canvas(frame4,height=900,width=550)
canvas.pack(side=LEFT)
yScroll=ttk.Scrollbar(frame4,orient='vertical',command=canvas.yview)
yScroll.pack(side=RIGHT,fill='y')
canvas.configure(yscrollcommand=yScroll.set)
frame5=Frame(canvas)
canvas.create_window((0,0),window=frame5,anchor='nw')
canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox('all')))
#Images
image1 = PhotoImage(file="images/Button.png")
image1=image1.subsample(6,6)
image2 = PhotoImage(file="images/classtacular.png")
image2=image2.subsample(2,2)
image3 = PhotoImage(file="images/icon.png")
image3=image3.subsample(2,2)
Label(frame2,image=image3).pack(side=RIGHT,anchor="ne")
#Buttons
if usertype=="admin":
    for x in frame3.winfo_children():
        x.pack_forget()
    btn1=Button(frame1,text="Summary",fg='black',image=image1,compound=CENTER,font=Font,command=summary,background="#A5F1E9",relief=FLAT )
    btn2=Button(frame1,text="New Entry",fg='black',image=image1,compound=CENTER,font=Font,command=new,background="#FFEBAD",relief=FLAT )
    btn4=Button(frame1,text="Logout",fg='black',image=image1,compound=CENTER,font=Font,command=logout,background="#5F8D4E",relief=FLAT )
    btn_fill=Button(frame1,text="",fg='black',compound=CENTER,font=Font,state=DISABLED,image='',background="#faedc5",relief=FLAT )
    btn1.pack()
    btn2.pack()
    btn_fill.pack(expand=True,fill=BOTH)
    btn4.pack()
elif usertype=="citizen":
    for x in frame3.winfo_children():
        x.pack_forget()
    btn1=Button(frame1,text="Summary",fg='black',image=image1,compound=CENTER,font=Font,command=view,background="#A5F1E9",relief=FLAT)
    btn4=Button(frame1,text="Logout",fg='black',image=image1,compound=CENTER,font=Font,command=logout,background="#7FE9DE",relief=FLAT)
    btn_fill=Button(frame1,text="",fg='black',compound=CENTER,font=Font,state=DISABLED,image='',background="#FFF6BF",relief=FLAT)
    btn1.pack()
    btn_fill.pack(expand=True,fill=BOTH)
    btn4.pack()
#Packing
frame1.pack(expand=False, fill='both', side='left', anchor='nw')
frame2.pack(expand=True, fill='both')
#Background
background=Label(frame2,image=image2)
background.place(relx=.5, rely=.5, anchor="center")
background.lower()
#Mainloop
root.mainloop()