# we are  going write a program to generates a random number and asks the user to guss it. it the player guss is  higher than the actual number, the the program dispays "lower number please" similar if the user's guess is  too low , the programmer prints " higher value please" when the user guesses the correct number , the  program displays the number of guess the player used to arrive at the number . hint: use the random module 
import random 
randNumber = random.randint(1,100)
# print(randNumber)
userGuess= None
guesses = 0
while(userGuess!= randNumber):
    userGuess = int(input("enter your guess: "))
    guesses+=1
    if userGuess == randNumber:
      print("You guessed it right...")
    else:
        if(userGuess>randNumber):
           print("You guessed wrong! enter a smaller number.")
        else:
          print("You  guessed wrong! enter a bigger number.")
            
       
   

print(f"You guessed the number in {guesses} guesses")

with open('hiscore.txt', 'r') as  f:
   hiscore = int(f.read())

if (guesses<hiscore):
   print("you have just broken the hiscore")
   with open('hiscore.txt', 'w') as f:
      f.write(str(guesses))   


