# example of abstraction

# class Car:
    
#     def __inti__(Self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(Self):
#         Self.clutch = True
#         Self.acc = True
#         print("car started...")

# Car1 = Car()
# Car1.start()





# example of encapsulation


class student:
    def __inti__(self, name="rajesh", marks=50):
        self.name = name 
        self.marks = marks
s1 = student()
s2 = student("bharat", 25)

print("Name: {} marks: {}".format(s1.name,s1.marks))
print("Name: {} marks: {}".format(s2.name,s2.marks))