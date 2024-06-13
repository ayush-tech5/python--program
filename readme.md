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
3. soecial character -> -,+,/,* etc..
4. whitespace -> Blank space , Tab , newline

variable:-> 

What is variable in python :- a variable is a name given to a memory location in a program or else we can simply say variable is a cpntainer to store some data.

example->
name = "shrada"
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
student = ["Neil", 85, "Bhubneswar"] - list


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