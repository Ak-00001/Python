# Conditionals expressions
num = 5

print("Positive " if num>0 else "Negative")

num =7
print("Even " if num%2==0 else "Odd")

a=6
b=7
max_num = a if a>b else b
print(max_num)
min_num = a if a<b else b
print(min_num)

age=25
status = "Adult" if age>=18 else "Child"
print(status)


temp =30
weather = "Hot" if temp >20 else "Cold"
print(weather)


user_role ="admin"
access_level = "Full Access" if user_role== "admin" else "Limited Access"
print(access_level)