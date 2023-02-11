from  tkinter import *
from PIL import ImageTk,Image

def press():
    print(userval.get())
    print(paseval.get())    

def forget():
    pass

root=Tk()
root.title('LAB REPORT')
root.geometry('500x700')
Label(root,text='--- REPORT----',font=('ArialBlack 30 bold'),fg='RED').grid(column=2,row=0,pady=10)

icon= Image.open("doc.png")
icon=icon.resize((500,700),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(icon)
Label(root,image=photo).place(x=0,y=0)
#fm.grid(column=2,padx=2,pady=10)

user=Label(root,text="USERNAME")
password=Label(root,text="PASSWORD")
user.grid(row=2,column=1,padx=5,pady=3)
password.grid(row=3,column=1,padx=5,pady=3)
userval=StringVar()
paseval=StringVar()

userentry=Entry(root,textvariable=userval)
pasevalentry=Entry(root,textvariable=paseval)
userentry.grid(column=2,row=10,pady=3)
pasevalentry.grid(column=2,row=3,pady=3)

Button(root,text="SUBMIT",command=press).grid(column=2,row=8,pady=10)
Button(root,text="FORGET PASSWORD",command=forget).grid(column=2,row=10,pady=5)
root.mainloop()