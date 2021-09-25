                                                                     #Iris Data Pickler


import pickle
import requests
j=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text    #Downloading data and converting into text
l=[[i] for i in j.split("\n")]     #Splitiing the iris data with new line and creating nested lists
with open("newiris.pkl","ab") as m:    #Making a new file in append mode
    pickle.dump(l,m)                       #Dumping the data
#for loading this file follow the below code
#with open("newiris.pkl","rb") as f:


  # print(pickle.load(f))
