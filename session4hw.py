#NO 1. WAP TO CHECK THE NUMBER ENTERED BY THE USER IF ODD OR EVEN.

num = int(input("ENTER YOUR NUMBER : "))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")

#NO 2. WAP  TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER. 

num1 = int(input("ENTER YOUR NUM1 : "))
num2 = int(input("ENTER YOUR NUM2 : "))
num3 = int(input("ENTER YOUR NUM3 : "))
if(num1 > num2 and num3):
    print("greater is ", num1)
elif(num2 > num1 and num3):
    print("greater is", num2)
else:
    print("greater is ", num3)

#NO 3. WAP TO CHECK A NUMBER IS A ULTIPLE OF 7 OR NOT
num = int(input("ENTER THE VALUE OF NUM : "))
if(num % 7 == 0):
    print("IT IS A MULTIPLE OF 7")
else:
    print("NOT A MULTIPLE OF 7")