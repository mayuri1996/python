
#addition of two numbers
def addition(a,b):
    return a+b

_num1 = int(input("enter first number = "))
_num2 = int(input("enter second number = "))

result = addition(_num1,_num2)
print(f"{_num1} + {_num2} = {result}")

#-------------------------------------------------------------------------------
#default parameter function
def namePrint(name='mayuri'):
    print(f"{name}")

namePrint()
namePrint("suyog")    