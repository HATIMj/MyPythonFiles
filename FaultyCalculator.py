j='FAULTY Calculator'
x=j.center(180)#Aligning the title in the center

print(x)
def sium(n,m):
    """This Function returns the sum of the given Numbers"""
    return int(n) + int(m)
def sub(n,m):
    """This Function returns the difference of the given Numbers"""
    return int(n)-int(m)
def multiply(n,m):
    """This Function returns multiplication"""
    return int(n)*int(m)
def div(n,m):
    """This Function returns the division of the given Numbers"""
    return int(n)//int(m)
#below are the inputs
n=int(input("Give The First Value:--"))
m=int(input("Give The Second Value:--"))
cho=input()
#Below are the conditions needed for making a faulty calculator
if cho=='multiply':
   if n==45 and m==3:
     print("555")
   else:
      print(multiply(n,m))
elif cho=='sum':

   if n==56 and m==9:
      print('77')
   else:
      print(sium(n,m))
elif cho=='div':
   if n==56 and m==6:
      print('4')
   else:
       print(div(n,m))
else:
    print(sub(n,m))

