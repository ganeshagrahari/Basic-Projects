import random
# snake water gun or rock paper Scissor
def gameWin(comp,you):
    # if two values are equal declare a tie!
    if comp==you:
        return None
    #check for all posibilities when computer choose s 
    elif comp=='s':
        if you =='w':
            return False
        elif you=='g':
            return True
        #check for all posibilities when computer choose w
    elif comp=='w':
        if you =='g':
            return False
        elif you=='s':
            return True
        #check for all posibilities when computer choose g
    elif comp=='g':
        if you =='s':
            return False
        elif you=='w':
            return True

print(" comp turn : Snake(s) water(w) or Gun(g)?")
randNo = random.randint(1,3)
# print(randNo)
if randNo ==1:
    comp = 's'
elif randNo ==2:
    comp='w'    
elif randNo ==3:
    comp='g'    

you = input(" your turn : Snake(s) water(w) or Gun(g)?")
a= gameWin(comp,you)

print(f"Computer choose: {comp}")
print(f"you choose: {you}")
if a ==None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")      

