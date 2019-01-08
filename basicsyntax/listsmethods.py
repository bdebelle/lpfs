"""
built-in methods to help manipulating a list
"""

cars = ["bmw", "honda", "audi"]
length = len(cars)
print(length)

# add an item to a list
cars.append("Benz")
print(cars)

print("*"*25)
# add an item in a certain index location
cars.insert(1, "subaru")
print(cars)

print("*"*25)
# Find the index location of an list item
x = cars.index("audi")
print(x)

print("*"*25)
# Pop out / remover an item. "y" makes the operator work from the end of the list?
y = cars.pop()
print(y)
print(cars)

print("*"*25)
#Remove a specific item from the list
cars.remove("honda")
print(cars)

print("*"*25)
#Slice a list to certain length / index location
slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

print("*"*25)
#sort a list alphabetically
print(cars)
cars.sort()
print(cars)