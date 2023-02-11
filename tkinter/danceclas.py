from tkinter import *
from tkinter.font import Font
import io
from tkinter import filedialog

# function to print data
def show():
    fhand=open('file.text','a+')
    print(fhand.read()) 
    print(fhand.readlines())   
    #Label(root,text=fhand.readlines()).grid(column=5,row=13,columnspan=1)
    
# function to save in file         
def savedata():
    Name=v1.get()
    Age=v2.get()
    Time=v3.get() 
    cont=v4.get()
    fhand=open('file.text','a+')
    fhand.write(f"Name :{Name},Age :{Age},Time :{Time},Contact :{cont} \n")
    #(f'Name: {name}, Age:{age}, City: {city}, Contact: {phone}')


root=Tk()
root.geometry('400x300')
# tab name 
root.title('DANCE CLASS')
#heading of the form
Label(root,text='ENTRY FORM',font=('Mangal 20 bold'),fg='blue',pady=10).grid(column=2)
#next heading
Label(root,text="FILL DETAILS -:",font=('Arial black',10,'bold'),padx=20,pady=10).grid(column=1,row=4)

#form details enter by user 
Label(root,text="NAME").grid(column=1,row=5)
Label(root,text="AGE").grid(column=1,row=6)
Label(root,text="TIME").grid(column=1,row=7)
Label(root,text="CONTACT").grid(column=1,row=8)

#varaiable to store entered value
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()

# individual entry
nam=Entry(root,textvariable=v1)
age=Entry(root,textvariable=v2)
time=Entry(root,textvariable=v3)
cont=Entry(root,textvariable=v4)
nam.grid(column=2,row=5)
age.grid(column=2,row=6)
time.grid(column=2,row=7)
cont.grid(column=2,row=8)

#buttons for gui
Button(root,text="SUBMIT",command=savedata).grid(column=2,row=10,pady=10)
Button(root,text="SHOW DATA",command=show).grid(column=2,row=11,pady=7)

root.mainloop()

