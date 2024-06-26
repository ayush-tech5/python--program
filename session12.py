# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)
#         #we can't access private attributes or methods directly 
#         #so we take a another method to pass these value and execute it

# acc1 = Account("12345" , "abcde")
# print(acc1.acc_no)
# print(acc1.reset_pass())


# class Person:
#     __name = "rohit"

#     def __hello(self):
#         print("hello person!..")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.welcome())



#EXAMPLE OF INHERITANCE 

# class Car:
#     @staticmethod
#     def start():
#         print("Car started...!")

#     @staticmethod
#     def stop():
#         print("Car stopped!!!")

# class Toyotacar(Car):
#     def __init__(self , name):
#         self.name = name

# car1 = Toyotacar("Fortuner")
# car2 = Toyotacar("Legender")
# print(car1.stop())
# print(car2.start())





# multiple inheritance
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C:
    varC = "welcome to class"


class Complex:
    def __init__ (self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i +", self.img , "j")

    def add(self , num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal , newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()