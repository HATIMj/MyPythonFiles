
a=input("Write the name of the person:-")
b=input("Exercise or Diet:-")
c=input("Status or add:-")
#Taking all input details

def dt():
  """This Function returns present Date and Time"""
  import datetime
  return datetime.datetime.now()
def nok(a):
  """This function returns required Data and it also write the required data into the files"""
  if b=="Exercise":
    if c=="Status":
      f=open(f"{a}.txt")
      print(f.read())
      f.close()
    else:
      d=input("Write your Exercise:-")
      f=open(f"{a}.txt","a")
      f.write(f"{dt()} {d}\n")
      f.close()
  else:
    if c=="Status":
      f=open(f"{a}Diet.txt")
      print(f.read())
      f.close()
    else:
      d=input("Write your Diet:-")
      f=open(f"{a}Diet.txt","a")
      f.write(f"{dt()} {d}\n")
      f.close()
#Below lines Take the given names and run the above function to get a result
if a=="rohan" or a=="sohan" or a=="lo":
  print(nok(a))
  
else:
  print("We don't have any data regarding this person.")




          
   
   

