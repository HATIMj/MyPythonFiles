                                    #Lesser Wins GAME MADE BY HATIM
import time
win1=0
win2=0

while True:#looping the inputs and the results
  m=float(input("input any number:-player1:--"))#Taking input from first player
  n=float(input("input any number:-player2:--"))#Taking input from second player
  if m<1 and m<n:#if the condition is not satisfied by one player then other player will get 2 points
    win2+=2
    
    print("player2 wins")
  elif n<1 and m>n:
    win1+=2
    
    print("player1 wins")
  elif m>=1 or n>=1:#First condition that the number should be greater than or equal to one
    if n>m:
      win1+=1
      
      print("player1 wins")
    elif m>n:
      
      win2+=1
      
      print("player2 wins")
    elif m==n:
      win1=0
      win2=0
      
      print("Draw")

  
  if win1==5:#Now the player who gets the first 5 points will win 
    time.sleep(1)
    print(f"Overall player1 wins")
    print("GAME OVER")
    break
  elif win2==5:
    time.sleep(1)
   
    print(f"Overall player2 wins")
    print("GAME OVER")
    break#Now when all the conditions will get satisfied loop will break 

