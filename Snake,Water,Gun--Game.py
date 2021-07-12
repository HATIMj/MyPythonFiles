import random
a=["snake","water","gun"]






def win():
    """This Function return end result of  the match b performing the certain calculations"""
    matches=0
    wins=0
    loses=0
    draw=0
    #looping  until matches are completed
    while matches<10:
        #input
        c=str(input("s-snake,w-water,g-gun:--"))
        b=random.choice(a)#random choice by pc
        #Below are comnditions for win,loss,Draw
        if c=="s" and b=="water" or c=="g" and b=="snake" or c=="w" and b=="gun":
            print(f"{c},{b}")
            print("Round  won")
            
            wins+=1
           
        
        elif c=="g" and b=="water" or c=="s" and b=="gun" or c=="w" and b=="snake":
            print(f"{c},{b}")
            print("Round lose")
            loses+=1
            
        elif c=="s" and b=="snake" or c=="w" and b=="water" or c=="g" and b=="gun":
            print(f"{c},{b}")
            print("Draw")
            draw+=1
        matches+=1    
    if wins>loses:
      return f"you win by rounds:{wins}"
    elif loses>wins:
        return f"you lose by rounds:{loses}"
    elif draw>loses or draw>wins:
        return f"draw rounds:{draw}"

print(win())#Print the function



    
    