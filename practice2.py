# Python Calculator0

print("Calculator")
operator = input("Enter the operator (+,-,/,*,%)")
op1 = int(input("Enter operand 1"))
op2 = int(input("Enter operand 2"))
if operator == "+":
    print(f"The Addition of {op1} and {op2} is {op1+op2}")
elif operator == "-":
    print(f"The Subtraction of {op1} and {op2} is {op1-op2}")
elif operator == "/":
    print(f"The Division of {op1} and {op2} is {op1/op2}")
elif operator == "*":
    print(f"The Multliplication of {op1} and {op2} is {op1*op2}")
elif operator == "%":
    print(f"The Modulus of {op1} and {op2} is {op1%op2}")
else:
    print("Invalid")


