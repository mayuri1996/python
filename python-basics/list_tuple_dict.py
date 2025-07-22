#list means array 
#we can add ,remove and update the data from list
_fruits = ['banana','apple','orange']
for fruit in _fruits:
    print(f"{fruit}")
print(f"{_fruits[-1]}") #-1 index for last value of list

#add new item into list (end)
_fruits.append("mango")
print(f"{_fruits}")

#remove  item from list
_fruits.remove("apple")
print(f"{_fruits}")

_fruits.remove(_fruits[1])
print(f"{_fruits}")

#----------------------------------------------------------------------------------------------------------

#Tuple 
#tuple is same as a list but we cannot change the tuple values it is fix
_colors = ("red","blue","green","white") 

for color in _colors:
    print(f"{color}")

print(f"{_colors[1]}")

#----------------------------------------------------------------------------------------------------------

#Dictionary (like json)
#key value pair set
_students = {
    "name":"Mayuri",
    "contact":9876787654,
}

print(f"{_students["name"]}")

#add new parameter
_students["email"] = "mayuri@gmail.com"
print(f"{_students}")

#update parameter
_students["name"] = "Suyog"
print(f"{_students}")

#delete parameter
del _students["name"]
print(f"{_students}")

#----------------------------------------------------------------------------------------------------------

#nested list inside dictionary (like array of object)
students = [
    {"name": "Mayuri", "marks": 88},
    {"name": "Ravi", "marks": 92}
]

for s in students:
    print(f"{s['name']} scored {s['marks']}")
print(f"{students[1]['name']} scored {students[1]['marks']}")    