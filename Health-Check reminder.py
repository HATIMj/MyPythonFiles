import datetime
import time
from pygame import mixer
j=datetime.datetime.now().time()
start=datetime.time(9,0,0)
end=datetime.time(23,50,0)
glass_intervals=60*55
physical_interval=60*45
eye_interval = 60*30
def mus(file):
   mixer.init()
   mixer.music.load(file)
   mixer.music.set_volume(0.7)
   mixer.music.play()
def eye():
  
   i=''
   while(i!='EyDone'):
      return mus("WATER.m4a")
      i=input()
      if i =="EyDone":
         mixer.music.stop()
         break
print(eye())
