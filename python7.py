# String Methods

#name = input("Enter your full name :")
#result = len(name)
# result = name.find(" ")
# result = name.rfind("d")
#result = name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#print(result)

#phone_number = input("Enter your phone number")
#result = phone_number.count("-")
#result = phone_number.replace("-", "@")

#print(result)


# Exercise - Validate user input

username = input("Enter a username : ")



if len(username) > 12:
    print("YOur username cannot be more than 12 characters")
elif not username .isalpha():
    print("Your username cannot contain numbers")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
else:
    print(f"Welcome {username}")



