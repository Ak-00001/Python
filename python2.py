#input

name = input("What is your name ?")
age= int(input("What is your age ?"))
age=age+1
print(f"Your name is {name}")
print(f"Your age is {age}")

#Exercise1- Area of rectangle

length=int(input("Enter the length of the rectangle"))
breadth= int(input("Enter the breadth of the rectangle"))
area =length*breadth
print(f"The area of the rectangle is {area}")

#Exercise2- Shopping cart program

item=input("What would you linke to buy")
price= float(input("What is the price ?"))
quantity=int(input("How many would you linke to buy ?"))
total = price*quantity
print(f"You have bought {quantity} x {item}")
print(f"YOur total is {total}")