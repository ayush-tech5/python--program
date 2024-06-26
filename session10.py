# class car:
#     colar = "blue"
#     brand = "toyota"
# car1 = car()
# print(car1.colar) # blue
# print(car1.brand) # toyota
 


# class student:
#    def __init__(self, fullname):
#       self.name = fullname
#       print("we can add a student in our database")

# s1 = student("web bocket")
# print(s1.name) #web bocket

# s2 = student("software")
# print(s2.name, s2.marks)

# class Student: 
#   #default constructor 
#   def __init__(self):
#     pass
  
#   #parameterized constructor

#   def __init__ (self , name , marks):
#       self.name = name 
#       self.marks = marks
#       print("Adding new student to the database : ")
# s1 = Student("webbocket" , 89)
# print(s1.name, s1.marks)

# s2 = Student("software" , 98)
# print(s2.name, s2.marks)




# class student:
#    college_name = "ABC college"
#    name = "anonymous" # class attibutes

#    def __init__(self, name, marks):
#       self.name = name # object attributtes > class attribute
#       self.marks = marks
#       print("adding new student to thr DB")

# s1 = student ("rohan", 98) 
# print(s1.name) #rohan



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        print("your mark is", self.marks)

s1 = Student("rohan", 98)
s1.welcome()
s1.get_marks()
