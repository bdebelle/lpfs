"""
data type to store more than one value in one variable
name, in term of key value pairs.
Dictionary items are in Brackets {} in key:value pairs
separated with "," {'k1':'v1', 'k2':'v2'}
"""

car = {'make':'bmw', 'model': '328i', 'year':2016}
print(car)

model = car["model"]
d = {}

print(car["model"])
print(car["make"])
print(car["year"])

#print empty dic
print(d)
#add keys and values to dict d
d["one"] = 1
d["two"] = 2


print(d)

#perform operation on value
sum_1 = d["two"] + 8
print(sum_1)
print(d)

d['two'] = d["two"] + 8
print(d)
