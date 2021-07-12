j=int(input("Input Number for the stars pattern iteration:--"))#Input for number of stars required for pattern
n=int(input("True(1) or False(1):--"))#True for correct pattern and False for reversed pattern
#Below the same conditions are applied  as above mentioned in coment statement
if n==0 or False:


  for i in (range(j,-1,-1)):#reversing the pattern here
    for k in range(i+1):
      print('*',end='')
    print('')
elif n==1 or True:#correct pattern without reversing
   for i in range(j):
  
    for k in range(i+1):
    
      print('*',end='' )
    print('')




