"""
object oriented programming
"""

class Car(object):

    def __init__(self, make, model='WRX'):
        self.make = make
        self.model = model

c1 = Car('subaru')
m1 = Car('wrx')
print(c1.make)
print(c1.model)

c2 = Car('honda')
print(c2.make)

