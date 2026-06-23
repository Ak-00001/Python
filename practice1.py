#Strings

name = "Ayush"
college = "HSM"
print(name)
print(f"Your name is {name} and you study in {college}")

#Integers 

marks =98
rank =2
print(f"Your scored {marks} points out of 100 and you are at {rank}nd position")

#Float

gpa = 1.7
print(f"your gpa is {gpa}")

#Boolean

is_present= True
if is_present:
    print("you were present")
else:
    print("You were absent")

# Typecasting

# So we can use typecasting if we want to convert one data type to another 
a = 5.2
print(type(a))
a=int(a)
print(f"Value of a is {a} and now after typecasting its a  {type(a)}") 
b ="Ayush"
c=""
b = bool(b)
c= bool(c)
print(b)
print(c)
# So bool() function gives true based of if the variable is empty of not if empty then True else False
# So we can actually write a program where we can use typecasting where if the user has entered his name the system gives access and if user has not entered name the programs throws error

print("Enter Your name")
name = input()
name = bool(name)
if name:

    print("Access Given")
else:
    print("Error !!, Please Enter Your Name")

#Input
name= input("Enter your name")
age = int(input("Enter your age"))
new_age = age+1
print(f"Your name is {name} and your age is {age}. Your age next year will be {new_age} ")

print(round(3.14))
print(abs(-4))
print(pow(4,3))
print(max(1,2,3))
print(min(1,2,3))

import math
print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.ceil(9.1))
print(math.floor(9.9))
print(math.ceil(9.9))
print(math.floor(1.2))

print(math.pi)
print(math.e)