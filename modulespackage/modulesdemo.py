"""
https://docs.python.org/3/library
"""
#imports all math builtins
import math
#imports only sqrt - this saves on memory
from math import sqrt
# import the car file from the other package
# import modulesexternal.car as car
from modulesexternal.car import info
class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(1000))

    def car_description(self):
        make = 'bmw'
        model = '550i'
        #info is imported from car.py
        info(make, model)

m = ModulesDemo()
#m.builtin_modules()
m.car_description()