# dictonary = a collection of key value pairs, ordered and changable , no duplicates

capitals = {"USA":"Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))

print(capitals.get("USA"))
if capitals.get("Japan"):
    print("That capital exisats")
else:
    print("That capital dosn't exist")


capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear

keys = capitals.keys()

#for key in capitals.keys():
    #print(key)
values = capitals.values()
for values in capitals.values():
    print(values)

items = capitals.items()
print(items)




print(capitals)