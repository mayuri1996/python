from math_util_module import devide

try:
  _num = int(input("enter number = "))
  devide(_num)
except ValueError:
        print(f"please enter value only")   