#guess the number game 
import random

#create one random number
secrateNum = random.randint(1,100)
attempts = 0

#------------------------------------------------------------------------------------ 
# for module example we are added this code 
def guessingGame():
    while True:
      userNum = int(input("Enter your number to guess "))
      attempts +=1  

      if userNum < secrateNum:
         print(f"your number is low compare to secrate number")
      elif userNum >  secrateNum:
        print(f"your number is high as compare to secrate number")
      else:
        print(f"congratulation your guess number {userNum} is match with secrate number {secrateNum} in {attempts+1}")   
        break; 
 
