import base64
from tkinter import *#Importing all the required modules
def click():#Making a function which encode the text which will be wriiten on screen by pressing encode button(click function will be binded with this button)
    """This function encodes the text given on the screen"""
    global sv
    
    data=base64.b64encode(sv.get().encode())#encoding the text
    
    
    
    sc.set(data)                 #setting the data
    screen1.update()            #Update the screen
    sv.set("")                  #Text field where text has been written will get cleared and Encoded text will be printed on the other screen with value "sc"
    screen.update()
def jojo():
    """This function Decodes the text given on the screen"""
    global sv                   #Functioning is same as the above function , the only difference is that it decodes the encoded text
    
    data=base64.b64decode(sv.get())
    
    
    
    sc.set(data)
    screen1.update()
    sv.set("")
    screen.update()
root=Tk()                              #Making GUI
root.geometry("500x500")               #Setting geometry
root.title("Message Encoder-Decoder")          #Title of the aplication
Label(root,text="Write Your Message in below placeholder").pack() #Label of the app

sv=StringVar()       #setting the screen to the value of ""
sv.set("")

screen=Entry(root,text=sv,font=200)     #Making the screen
screen.pack(padx=20,pady=20)


f=Frame(root,bg='grey') #Making the frames


b=Button(f,text="Encode",command=click).pack(side=RIGHT)#Making the button by giving them required commands i.e (what will they do if i click them)
b=Button(f,text="Decode",command=jojo).pack(side=RIGHT)
f.pack()
sc=StringVar()
sc.set("")

screen1=Entry(root,text=sc,font=200)#Making another screen annd setting its value to ""
screen1.pack(padx=20,pady=20)
                                                                       #DONE



























root.mainloop()
