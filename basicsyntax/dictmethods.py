"""
Dictionary Methods
"""

car = {'make':'bmw', 'model': '550i', 'year':2016}
cars = {'bmw':{'model':'550i', 'year':2016}, 'benz':{'model':'e350', 'year':2015}}

#Print keys in dictionary
print(car.keys())
print(cars.keys())
#Print values in dictionary
print(car.values())
print(cars.values())
#Print out all items in dictionary
print(car.items())

#will make copy
car_copy = car.copy()
print(car_copy)

# will clear dictionary
# car.clear()
# print(car)

# will pop out / remove item from dictionary
print(car.pop('model'))
print(car)