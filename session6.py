#tup = (3, 73, 79, 38, 8)
#print(tup[1])
#print(tup[2])
#print(tup)

#tup = (1,)
#print(tup)
#print(type(tup))

#tup1 = ("neil" , "noone")
#print(tup1)
#print(type(tup1))

#tup2 = (1.0)
#print(tup2)
#print(type(tup1))

#tup3 = (1 , 9 , 7 , 8 , 5 , 7)
#print(tup3)
#print(tup3[1:4])
#print(tup3[2:])
#print(tup3[:4])


#tup4 = (1 , 9 , 7 , 8 , 5 , 7)
#print(tup4.index(8))# type element find index
#print(tup4.count(7))
#print(tup4[4]) # type index find element

"""""
info = {
    "name" : "neil",
    "learning" : "python",
    "age" : "22",
    "carrier" : "good"
    }
print(info)
print(info["name"])
print(info["carrier"])
print(info["age"])
print(type(info))

info["name"] = "Ayush kumar"
info["surname"] = "Sahoo"
print(info) # This property of changing value is known as THE PROPERTY OF MULTABLE (change their value)
"""

"""""
student = {
    "name" : "Neil",
    "subject" : {
        "java" : {
            "core java" : 78,
            "adv java" : 87
        },
        "c++" : 67,
        "python" : 99
    }
}

print(student)
print(student["name"])
print(student["subject"]["python"])
print(student["subject"]["java"]["core java"])
print(student["subject"])



print(student)
print(student.keys())
print(student["subject"].keys())
print(student["subject"]["java"].keys())
print(student.values())
print(student["subject"].values())
print(student["subject"]["java"].values())
print(student.items())
print(student.get("subject"))
student.update ({"city" : "Puri"})
print(student)

"""
"""""
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set3 = set() #empty set

set1.add(6) # adds an element
print(set1)
set1.remove(6) #remove an element
print(set1)
# set1.clear() # clear all the elements
print(set1)
print(set1.pop()) # Remove random values of set
print(set1.union(set2) )# combine both set values and returns a new set
print(set1.intersection(set2)) # combines the common values and returns a nnew set

"""
set4 = {6,8,3,9}
print(set4.pop())