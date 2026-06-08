#2D list
fruit =      ["apple","oranges","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats=       ["chicken","fish","turkey"]

groceries= [fruit,vegetables,meats]

print(groceries[2][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()