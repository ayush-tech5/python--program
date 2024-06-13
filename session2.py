
#variable of python
#Data of a person

name = "shrada" 
age = 23
salary = 23000.56
ontime = False
a = None

print(type(name))#name of the person
print(type(age))#age of the person
print(type(salary))#salary of the person
print(type(ontime))
print(type(a))

#this is single line comment

"""
these are
 multiline
comments
"""

# print sum of 2 nos

a = 60
b = 30
sum = a+b
print("sum is : " ,sum)
print("subtraction is : ",a-b)

#arithmatic operators
a=120
b=10

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# Relational operators
a = 40
b = 30

print (a==b)
print (a<b)
print (a>b)
print (a<=b)
print (a>=b)
print (a!=b)

# Assignment Operators

num = 20
num = num + 20
print (num)

#Logical operators

val1 = True
val2 = False 

print (" AND operatos", val1 and val2) # It takes both val1 & val2
print (" OR operatos", val1 or val2) # either it take val1 or val2


#true + true = true
#true + false = false
#false + true = false
#false + false = false

# INPUT

name = str(input("ENTER YOUR NAME : "))
age = int(input("ENTER YOUR AGE : "))
salary = float(input("ENTER YOUR SALARY : "))

#print("BIODATA IS : ", name ,age ,salary )
print("WELCOME", name)
print("YOUR AGE IS", age)
print("TOTAL SALARY IS", salary)