str1 = "this is a good day \n and i will sleep whole day in my room."
print(str1)


#String concatenation
#ex 1

str1 = "web"
str2 = "bocket"
print (str1 + str2)#webbocket

#ex 2

str3 = "Smrutiranjan"
str4 = " Sahoo"
print (str3 + str4) #Smrutiranjan Sahoo

#Length of String ->
#ex 1 

str5 = "WEBBOCKET"
len1 = len(str5)
print(len1)

#or,

str5 = "WEBBOCKET"
print(len(str5))

#ex 2

str6 = "SMRUTIRANJAN SAHOO"
print(len(str6))

str7 = "web"
str8 = "bocket"
str9 = str7 + " " + str8
print(str9)
print(len(str9))

#INDEXING OF STRING ->

str = "MANAS KUMAR SAHOO"
print(str[1])
print(str[8])
print(str[5])

#SLICING OF STRING

strslice = "smrutiranjansahoo"
print(strslice[0:4]) #smru
print(strslice[:6]) #smruti

 

#FUNCTIONS OF STRING :->

#endswith
str = "i am a student of webbocket . webbocket is the best way for career building"
print(str.endswith("building")) #true
print(str.endswith("ing")) #True
print(str.endswith("odisha")) #False 

#capitalize
str ="I am a student of webbocket . webbocket is the best way for career building"
print(str.capitalize()) #(FIRST CHARACTER WILL BE CAPITAL)

#replace
str = "smrutiranjan sahoo"
print(str.replace("smrutiranjan" , "Manas Kumar")) #Manas Kumar sahoo

#find
str = "i am a student of webbocket . webbocket is the best way for career building"
print (str.find("webbocket"))#18 (index no.)

#count
str = "i am a student of webbocket . webbocket is the best way for career building"
print(str.count("webbocket"))