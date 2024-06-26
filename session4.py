#IF , ELIF , ELSE 

"""
age = int(input("ENTER YOUR AGE : "))
if(age<18):
    print("TEENAGER")
elif(age>=18 and age<=55):
    print("YOU CAN APPLY FOR LICENCE ")
else: 
    print("INVALID AGE ")
    """
"""""
strColour = str(input("ENTER THE COLOUR : red"))
if(strColour == "green"):
    print("you can go")
elif(strColour == "orange"):
    print("Start your vehicle")
elif(strColour == "red"):
    print("STOP!")
else:
    print("YOU ARE A DONKEY")
"""
"""""
mark = float(input("ENTER YOUR MARK IN % : "))
if(mark<30):
    print("FAIL!")
elif(mark > 30 and mark <= 40):
    print("GRADE - E")
elif(mark > 40 and mark <= 50):
    print("GRADE - D")
elif(mark > 50 and mark <= 60):
    print("GRADE - C")
elif(mark > 60 and mark <= 70):
    print("GRADE - B2")
elif(mark > 70 and mark <= 80):
    print("GRADE - B1")
elif(mark > 80 and mark <= 90):
    print("GRADE - A2")
elif(mark > 90 and mark <= 100):
    print("GRADE - A1")
else:
    print("HASN'T APPEAR THE EXAM")
"""
""""
#1
num = int(input("ENTER YOUR NUMBER : "))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")

        #2
num1 = int(input("ENTER YOUR NUM1 : "))
num2 = int(input("ENTER YOUR NUM2 : "))
num3 = int(input("ENTER YOUR NUM3 : "))
if(num1 > num2 and num3):
    print("greater is ", num1)
elif(num2 > num1 and num3):
    print("greater is", num2)
else:
    print("greater is ", num3)
"""


"""""
list = [45, 67, 34, 90, 6, 32]
print(list)
print(type(list))
print(list[1])
print(list[2])
print(list[0])
print(len(list))
print(list[-1])
"""

"""""
marks =  [20 , 67 , 89 , 64 , 74 , 78]
print(marks[2:5])
print(len(marks[1:4]))
print(marks[:4])
print(marks[2:])
"""

# index = [1,2,3,4,5,6]
# index.append(7)
# print(index)
# index.sort()
# print(index)
# index.sort(reverse = True)
# print(index)
# index.reverse()
# print(index)
# index.insert(5 , 0)
# print(index)
# index.remove(2)
# print(index)
# index.pop(4)
# print(index)