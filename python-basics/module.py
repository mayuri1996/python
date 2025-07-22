import math

#this line imprting all code inside the file 
#add if any globally code is available inside the file it will run before your current file coding 
#import guesguessingGame

#this line imported only guesguessingGame function if other code is available inside the file then it will not work
from  package import guess_number_game

# module means importing another file and use functions to that file into current file 
# find square root and power of number using math module
_num = int(input("enter number for square root and power = "))
_result = math.sqrt(_num)
_power = math.pow(_num,3)
print(f"squareroot = {_result}")
print(f"power = {_power}")

#costume module
guess_number_game.guessingGame()