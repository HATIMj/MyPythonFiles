                                              #Healthy Programmer 
from datetime import datetime
from time import time
from pygame import mixer
def musiclooper(file,stopper):
    """This function creates a music looper and stop when input matches the stopper"""
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
       i=input()
       if i==stopper:
           mixer.music.stop()
           break
def logs(msg):
    """This function saves the logs of the different msgs with current time"""
    with open("logs.txt","a") as f:
        f.write(f" {msg} {datetime.now()}\n")
if __name__=="__main__":
    dt=time()     
    et=time()
    pt=time()
    watersec=40*60
    eyessec=30*60
    physicalse=45*60
    while True:

       if time()-dt>watersec: #When time exceeds the given time function executes
           print("Please enter drank to stop the voice msg.")
           musiclooper("mixkit-fast-small-sweep-transition-166.wav","drank")
           dt=time()  #Start the a=ci=ounting of time again
           logs("drank water now")
       if time()-et>eyessec:
           print("write ey to stop loop.")
           musiclooper("mixkit-fast-small-sweep-transition-166.wav","ey")
           et=time()
           logs("eyes rest done at")
       if time()-pt>physicalse:
           print("write pydone to stop the loop")
           musiclooper("mixkit-fast-small-sweep-transition-166.wav","pydone")
           pt=time()
           logs("physical exercise done at ")