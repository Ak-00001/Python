# Python weight calculator

weight = float(input("Enter your weight"))
unit= input("Killograms or pounds (K or L): ")

if unit=="K":
    print(f"Your current weight is Killograms is {weight}Kg")
    weight =weight * 2.205
    print(f"Your weight in Pounds is {round(weight,2)}pounds")
elif unit== "L":
    print(f"Your current weight in pounds is {weight}pounds")
    weight=weight/2.205
    print(f"your weight in killograms is {round(weight,2)}killograms")
else:
    print("Invalid input")
