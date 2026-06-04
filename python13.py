# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Dublicates OK
# Set = {} unordered and immutable, but Ass/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates Ok. FASTER

fruit = ["apple", "orange", "banana", "coconut"]
print(fruit)
print(fruit[0])
print(fruit[::2])

for x in fruit:
    print(x)