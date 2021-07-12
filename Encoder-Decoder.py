import base64
from tkinter import *
def click():
    global sv
    
    data=base64.b64encode(sv.get().encode())
    
    
    
    sc.set(data)
    screen1.update()
    sv.set("")
    screen.update()
def jojo():
    global sv
    
    data=base64.b64decode(sv.get())
    
    
    
    sc.set(data)
    screen1.update()
    sv.set("")
    screen.update()
root=Tk()
root.geometry("500x500")
root.title("Message Encoder")
Label(root,text="Write Your Message in below placeholder").pack()

sv=StringVar()
sv.set("")

screen=Entry(root,text=sv,font=200)
screen.pack(padx=20,pady=20)


f=Frame(root,bg='grey')


b=Button(f,text="Encode",command=click).pack(side=RIGHT)
b=Button(f,text="Decode",command=jojo).pack(side=RIGHT)
f.pack()
sc=StringVar()
sc.set("")

screen1=Entry(root,text=sc,font=200)
screen1.pack(padx=20,pady=20)




























root.mainloop()
