import requests
import json
j=requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=68e8f620409e4d93b2b3734120bc5747") #Importing news
k=j.json()["articles"] #Converting into hjson and taking out the articles
results = []
for ar in k:
   results.append(ar["title"])   #Appending the title into new list


st=''   #Creating an empty string
for i in results:
   st+=i #Creating the list intop long string for gtts to work 
def voice(st):
   """This function save the string into voice and then speak it"""
   from gtts import gTTS
   import os 

   tts=gTTS(text=st,lang='en')
   tts.save("jio.mp3")           #saving into mp3
   os.system("nvlc jio.mp3")  #Playing from os 
voice(st)