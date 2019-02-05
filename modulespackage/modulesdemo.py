"""
https://docs.python.org/3/library
"""
#imports all math builtins
import math
#imports only sqrt - this saves on memory
from math import sqrt

class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(1000))

m = ModulesDemo()
m.builtin_modules()