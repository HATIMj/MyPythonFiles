from tkinter import *
root = Tk()
root.geometry('500x500')
Label(root,text="MADLIBS \n BY HATIM",font='90').pack()
Label(root,text="let's get started guys",font='120').place(x=200,y=100)
def madlibs1():
   animal=input("choose any animal: ")
   colour=input("choose any colour: ")
   fruit=input("choose any fruit: ")
   thing=input("chooose your favourite thing: ")
   print("once upon a time, bill was passing a jungle with his " + thing + ".Then he saw a "+fruit+" tree. He sat there for some rest and suddenly he saw a "+animal+" which was "+colour+" in colour")
Button(root,text="click here",font="200", command = madlibs1 ).place(x=200,y=200)   
root.mainloop()   
   