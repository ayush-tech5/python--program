What is python??

- python is simple,easy & portable.
- python is free & open source.
- python is high level , interpreted language.
- python is developed by guido van rosum.

python is interpreted language means when we write python code its executed the code line by line thats why we called python is interpreted language 

- print is function to output statement in python. simply we can tell "print" is output function.

character set of python language :
1. letter -> A-Z , a-z
2. Digits -> 0-9
3. special character -> +,-,/,* etc..
4. whitespace -> Blank space , Tab , newline

variable:-> 

What is variable in python :- a variable is a name given to a memory location in a program or else we can simply say variable is a container to store some data.

example->
name = "shradha"
age = 23
salary = 23000.56

variable names = name , age , salary
variable values = "shrada" , 23 , 23000.56

Rules for identifires:->
1. identifiers  - names of the variables 
2. identifiers can be combinations of uppercase and lowercase lettter , digits or an underscore(_). ex- myVariable , variable_1 .
3. an identifiers can't start with digit. so while variable1 is valid but 1variable is not valid.
4. we can't use special character or symbols like !, #, @, %etc ...
5. identifiers can be of length.
6. variables names should be small and meaningful like -  when we give our age in that case we take the variable as "myAge".
7. here myAge is camel case letter

- type is a operator to show the datatype name in our variables like which  datatypes we use in our variables.



DATATYPES:->

- mainly datatypes are 5 types in python :
- These datatypes are unmutable or build-in datatypes.
1. integer - +ve value , 0 , -value (int)
2. string - "hello" , "shradha" etc... (str)
3. float - 3.91 , 6.37, etc ... (float)
4. boolean - true , false (boolean)
5. None - not assign

Comments in python:->

- when we write some code but we don"t want to execute it then we give a commentline to that place so that line of code will not executed .
- comments are of 2 types .

1. single line comment:-
- when we the single line comments in python we did it on "#". 
ex- #single line comment
    #this is a comment

2. multiline comment:-
- when we it a multiline comment we did it through """_""" .
ex- 
"""
multiline 
comments
"""

TYPES OF OPERATORS :->
- simply we can say operator is a symbol that performs a certain operation between operands .
ex-
a+b
Here, 
a,b -> operands 
+ -> operator

- There are 4 types of operators in python 

1. Arithmatic Operator - (+, -, /, *, %)
2. Retational Operator - (==, !=, <, >,<=,>=)
3. Assignment Operator - (=, +=, -=, *=, /=, %=)
4. Logical operator - (and, or, not)

Input in python :-

- Input() statement is used to accept values (use keyword) from the user.


STRINGS:->

- String is a datatype that stores a sequence of characters

str1 = "This is a good guy"
str2 = 'this is a good guy'
str3 = """this is a good guy"""

- All these strings are real strings . because in python , it sopports all these syntax like - "" , ' , """


- \n(newLine)- when we want to break our line in to a new line then we can give the new line symbol in that place so the line get breaked automatically. 

Basic operations of string:

concatenation ->
"Hello" + "World" = 
Lentgh of string ->
len(str)


INDEXING OF STRING :->

- WEBBOCKET -> 012345678(indexing)
- Always indexing starts from '0'.

SLICING OF STRING :->

- Accessing parts of a string.
- ending index is not counting.
- syntax - str[starting_index : ending_index]

str = "webbocket"
str[0:3] - web
str[1:3] - eb
str[:3] - web


FUNCTIONS OF STRING :->

EX-
str = "i am a coder."

1. str.endswith("er.") - returns true if string ends with substring
2. str.capitalize() - returns first char is capital
3. str.replace(old , new) - replace all occurences of old with new 
4. str.find(word) - returns 1st index of 1st occurence 
5. str.count("am") - counts the occurence of substring in string



CONDITIONAL STATEMENT:->

- used to handle the condition in your program . 
- syntax (if-elif-else)
- elif means else-if

if(cond):
    statement 1
elif(cond):
    statement 2 
else:
    statement(default)

Lists in python:->

- Lists ina built-in data type that stores set of values.
- it can store elements of different types like integer, float, & string etc... 
- in list we can make indexing.
- in list we can find length of the list also.

- in list we can also do the slicing activity.
ex- 
marks = [87, 45, 67, 83, 45] - array and list
student = ["ayush", 85, "Bhubneswar"] - list


LIST SLICING :->

- it similar to starting slicing .
- syntax - list_name[starting_idx : ending_idx]
- ending index is not included 

marks = [23 , 25 , 34 , 47, 46 , 78]
marks[1:4]-> [25 , 34 , 47 , 46]
marks[:3] -> [23 , 25 , 34 ]
marks[2:] -> [34 , 47 , 46 , 78]

List methods :->

list = [9, 4, 6, 7, 8 ,2]
list.append(6) - adds one element at the end of the list - [9, 4, 6, 7, 8, 2, 6]
list.sort() - sort the elements in assending order - [2,4,6,7,8,9,]
list.sort(reverse=True) - sorts the element in decending order - [9,8,7,6,4,2]
list.reverse() - reversing the list - [2,8,7,6,4,9]
list.insert(idx,el) - insert the element at index
list.remove(1) - remove the first occurence of element - [9,6,7,8,2]
list.pop(idx) - remove element at index 


GIT ->

- it is a open source repository system where we can save , manipulate , colaborate our code with anyone else .
- in our software era, everyone can use git system for their software development . 
- we also call git is a version control system. 
- git provides some tools to use their functionlity and fratures ex- github , gitlab etc...




git init
git add -A
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ayush-tech5/python--program.git
git push -u origin main



tuple in python :-

- tuple is a build in data type that iets us create immutable(the value
changeable) sequence of value.
- ex. tup = (87 , 67 ,98 .34, 45)
- tup[0] -> 87
- tup[1] -> 67
-we can do the tuple as
1. tup1 = () -> empty tumple 
2. tup2 = (1,) -> tuple
3. 


tuple methods:-

- tup.index(element) -> returns index of first occurence 
- tup count(element) -> returns the count total occurence 

ex. tup = (2,1,3,1)
tup.index(2) -> 3
tup.count(1) -> 2







office-works :-

1. print numbers from 1 to 100
2. print numbers from 100 to 1
3. print the multiplication table of the number n.
4. print the elements of the following list using a loop.
   [1,4,9,16,25,36,49,81,100]
5. search for a number x in thius tuple using loop
   (1,4,9,16,25,36,49,64,81,100)






dictinory in python :-
 - dictionary are used to store the data value in key:value pair.
 - they are unordered, mutable(changeable) & don't allow duplicate keys.
 - ex- 
 dict = {
    "name" : "shradha",
    "cgpa" : 9.8,
    "marks": [98,96,95],
 }
 - the left part of the dictionary are the keys & right side part in their values so 
 dictionary contains key:value pair structure.


 nested dictionary in python:-

 - dictionary also satisfy the nested property.
 - dictionary under dictionart is called nested dictionary.
 - ex.
 student = {
    "name" : "mithun",
    "score" : {
        "chem" : 98,
        "math" : 87,
        "phy" :79
    }
 }
  Dictionary methods :-

  1. mydict.keys() - it returns all keys.
  2. mydict.value() - it return all value
  3. mydict.items() - it will returns all key:value pair as tuple
  4. mydict.get("way") - returns the key according to value.
  5. mydict.update(newdict) - insert the specified items ri the dictionary.


set in python :- 
- set is the collection of the undered items.
- each element in the set must be unique & immutable (can't change).
- ex. 
nums = {1,2,3,4,5}
set2 = {5,8,9,4}
 set method :- 
 1. set.add (element) -> adds an element
 2. set.remove(element) -> remove an element
 3. set.clear() -> clear all element
 4. set.pop() -> remove a raindom value of set
 5. set.union(set2) -> combine both set value & return a new set 
 6. set.intersation(set)

6. set.intersection(set2) -> combines the common value $ returns a new set.

ex.
set1 = {1,2,3,2,4}
set2 = {3,7,2,6,4}
set1.union(set2) -> {1,2}



break $ continue :-

- break: break is used to terminate the loop encountered.
- continue: terminates execution in the current iteration $ continue execution of the loop 
with the iteration.

2. for loop:-

- for loop are used sequential traversal. for tranversing list, string, tuple etc.
- syntax:-
   for val in list:
       statement..
       
range() :-
- range function returns a sequence of number, starting from 0 by default, and 
increaments by 1 (by default), and stops before a specified number.

- syntex -> range(start , stop, step)


functions in python:-
- function is a block of statements that performs a specific task.
- syntex def func_ name(parament 1, paramenter 2..):
some statement
returns val

func_name(arg1, arg2..) #function call

- functions are of 2 types in python
1. buld-in function - print(), len(), type(), range() ... etc
2. user defined function - user can develop the function.


object otiented programming in python :-

- to map with real world scenarios, we started using objects in code. this is called
object oriented programming(oop).

1st concept-> procedual programming.
2nd concept-> function  programming.
3rd concept-> object oriented programming.


class $ object in python :-
ex. -> creating a class
class student:
name = "web bocket"

ex. -> cerating a object(instance)
s1 = student()
print(s1.name) #web bocket

__init__ function (constructor) :-

- all class have a function called __init__(), which is always executed when class is
being initiated.

ex. -> creating a class 
class student:
   def __init__(self, fullname)
      self.name = fullname

ex. -> creating a object
s1 = student("web bocket")
print(s1.name)

note:- the self parameter is a reference to thr cuttent instance of the class, and is used
to access variable that belongs to the class.


class & instance attibutes:-
 
 university -> college1, college2, college3, college4
               student1, student2, student3, student4

- colleges and student are the attibutes university.




methods in python :-
- method are function that belongs to objects.

ex. -> creating class
class student:
   def __inti__(self, fullname):
   self.name = fullname
def hello(self):
    print("hello", self.name)

ex. -> crearting object

s1 = student ("rohan")
s1.hello()

def hello(self):
    print












ex. -> creating object(instance)
s1 = student()
primt(s1.name) # web  bocket

__inti__ function (constructor) :-

- all class have a function called__inti__(), which is always executed when the class is being
initiated.





practivce question -
- create accout class with 2 attributes - balance & account no. & account no. & create method for debit,
credit & printing the total balance.




private(like) attributes $ methods :-
- private attibutes $ method are to be only within the class are not
accessible from outside the class.
- the private  class attibutes are written in __(attibutes) so that we call it private
attibutes of class.



inheritance :-

- when one class(child class) derives the properties $ method of another class(parent class)
- syntex :-
class car:
  ---------
  class toyotacar(car):
   -------------

 - in python inheritance are of 3 types.
1. single inheritance
2. multi-level inheritence
3. multiple inheritance

polymorphism: operator overloading:-

- when the same operator is allowed to have defferent meaning accordingly to the context.
- in that polymorohism we can use dunder functions.
1. a + b -> __add__
2. a - b -> __sub__
3. a * b -> __mu1__
4. a / b -> __truediv__
5. a % b -> __mod__

ex - (+)
print(1 + 2) #3 