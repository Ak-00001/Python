#Logical Operator
#for logical or operator if one condition is true entire condition is true
temp =25
is_raining =False
if temp > 35 or temp<0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor events is still scheduled")

#for AND to be true both conditions must be true 

temp = 28
is_sunny = False
if temp>= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp<= 0 and is_sunny:
    print("It is cold outside ")
    print("It is sunny")
elif 28 > temp> 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")

#not inverts the condition (not False, not True)

elif temp>= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp<= 0 and not is_sunny:
    print("It is cold outside ")
    print("It is sunny")
elif 28 > temp> 0 and not is_sunny:
    print("It is warm outside")
    print("It is sunny")

