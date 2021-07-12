def jojo(number):
   """This Funtion return series of number in Decimal,Octal,Hexadecimal and Binary"""
   w=len("{0:b}".format(n))#Vertical width between the line of series
   for i in range(1,n+1):
      print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=w))

if __name__=='__main__':

   n=int(input("Enter a number:--"))#Taking the input
   print(jojo(n))#calling the fuunction
  
  
    