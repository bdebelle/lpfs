"""
Nested Dictionary
d = {'d': {'nestk1':'nestvalue1', 'nestk2':'nestvalue2'}}
d['k1']['nestk1']
"""

#define nested dictionary
cars = {'bmw':{'model':'550i', 'year':2016}, 'benz':{'model':'e350', 'year':2015}}
# set variable to specific value
bmw_yr = cars['bmw']['year']

#access nested dictionary
print(bmw_yr)
print(cars['bmw']['model'])
print(cars['benz']['year'])
print(cars['benz']['model'])


