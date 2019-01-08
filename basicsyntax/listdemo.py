"""
data type to store more than one value in one variable name
list items are in brackets, separated with "," [1,2,3]
"""

cars = ["bmw" , "honda" , "subaru"]
empty_list =[]
print(cars)
print(empty_list)

print("*"*20)

print(cars[0])
print(cars[1])
print(cars[2])

num_list = [1,2,3]
sum_num = num_list[0] + num_list[2]

print(sum_num)

more_cars = ["toyota" , "audi" , "ford"]
print(more_cars[1])

more_cars[1] = "benz"

print(more_cars[1])
print(more_cars)
