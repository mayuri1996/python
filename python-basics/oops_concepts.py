#class and object
class Student:
    #__init__ this is type of constructor
    # called only once when object create
    def __init__(self,name):
        self.name = name

    def marks(self,mark):
        print(f"{self.name} = {mark}")    

#object creation
s1 = Student("msyuri")       
s1.marks(34) 
print(f"{s1.name}")
s2 = Student("suyog")
s2.marks(50)

#-------------------------Inheritance---------------------------------
#Inheritance -> child class can access parent class properties/methodes
#parent class
class Vehicale:
    def color(self):
        print(f"Vehicale having black color")

#child class(Car) inherits parent class(Vehicale) 
class Car(Vehicale):
    def color(self):
        print(f"car color is white")
        super().color()  #called parent class method into child class using super


carObj = Car()
carObj.color()   

#-------------------------Encapsulation---------------------------------
#Encapsulation -> data protection , make data + function at same place
class Account:
    def __init__(self,password):
        self.__password = password  # password is a private variable (declare private variable using __)

    def login(self):
        if self.__password == "mayuri":
            print(f"logged in successfully")
        else:
            print(f"wrong password")    
        
obj1 = Account("mayuri")  
obj1.login()  
#obj1.__password    # we cannot access private variable outside the class this is encapsulation protecting data 


#-------------------------Polymerphysm---------------------------------
#Polymerphysm -> same method names but different behaviour
# inheritance + methode overriding
#parent class
class Animal:
    def sound(self):
        print(f"Animal sound")

#child class with same sound methode name
class Dog(Animal):
    def sound(self):
        print(f"dog sound")    

#child class with same sound methode name
class Cat(Animal):
    def sound(self):
        print(f"cat sound")    

#creating child class object list and interate it using for loop 
for obj in [Dog(),Cat()]:
    obj.sound()