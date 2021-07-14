                                    #GREATER THAN GAME MADE BY HATIM
win1=0
win2=0

while True:#looping the inputs and the results
  m=float(input("input any number:-player1:--"))#Taking input from first player
  n=float(input("input any number:-player2:--"))#Taking input from second player
  
  if m>=1 or n>=1:#First condition that the number should be greater than or equal to one
    if m>n:
      win1+=1
      print("player1 wins")
    elif n>m:
      win2+=1
      print("player2 wins")
    else:
      win1=0
      win2=0
      print("Draw")

  elif m<1:#if above condition is not satisfied by one player then other player will get 2 points
    win2+=2
  elif n<1:
    win2+=2
  if win1==5:#Now the player who gets the first 5 points will win 
    print(f"Overall player1 wins")
    break
  elif win2==5:
    print(f"Overall player2 wins")
    break#Now when all the conditions will get satisfied loop will break 

