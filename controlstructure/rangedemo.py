"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""

#print(list(range(0, 10)))

# 3rd number is a step
a = range(0, 100, 8)
#a = range(100) #will automatically start at 0
print(a)
#print what type a is? its a class type of range
print(type(a))

print(list(a))

l = [1,2,3]
#list above not being used below
for num in range(4):
    print(num)
