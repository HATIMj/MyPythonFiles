                                                #Email Extracter


import re
st=input()  #Taking Input
q=re.findall(r'\w+@\S+\w',st)  #finding any sentence with  word or number with @ in it and with no space 
k=re.findall(r'\+91\d{10}\b',st)  #finding number started with +91 and then 10 more numbers
print(q,k)