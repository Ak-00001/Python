#while loop

#1

name = input("Enter your name")
while name == "":
    print("Yo !! type your nameeeeeeeeeeeeeeeeeeee")
    name = input("Enter your name")
print(f"Hello {name}")

#2

food = input("Enter a food")

while not food == "q":
    print(f"you like {food}")
    food = print("Enter another food you like")
print("Bye")

#3

num = int(input("Enter a number between 1 -10"))
while num<1 or num >10:
    print(f"{num} is not valid")
    num = int(input('Enter a number between 1-10'))
    print(f"your number is {num}")