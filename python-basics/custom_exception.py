# Exception is parent class 
class checkNumCustomException(Exception):
    #__init__ is a constructor methode 
    # if you creating object this method will autometacally call 
    # self is a object of this current class
    def __init__(self, num):
        #called parent class(Exception class) constructor
        super().__init__(f"{num} is less than 20 enter greater than 20")