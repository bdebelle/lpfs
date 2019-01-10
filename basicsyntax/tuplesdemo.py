"""
Tuple
like lists but they are immutable (unchangeable)
"""

my_list = [1,2,3]
print(my_list)
#Change item in list
my_list[0] = 8
print(my_list)

#Tuples are made with ( )
my_tuple = (1,2,3,3,5,2,2,2)
print(my_tuple)
#try to change item
# my_tuple[0] = 8
# Shit dont work
# print(my_tuple)

print(my_tuple[0])

print(my_tuple[1:])

#find the index of 2
print(my_tuple.index(2))

# Print how many times this item is in the tuple
print(my_tuple.count(2))

#use tupple when you dont want any items to be changed
