"""
object oriented programming
"""

class Car(object):
    # Global class attribute
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)


c1 = Car('subaru', 'WRX')
# This will print just the make value of c1
print(c1.make)
# change wheel variable for this instance - will not affect the others
c1.wheels = 5
print(c1.wheels)
# This will run the instance of c1 from the info function
#c1.info()
c1.transmission = '6MT'
c1.color = 'black'
print(c1.transmission)
print(c1.color)

c2 = Car('honda', 'Civic')
print(c2.make)
# print global variable "member variable"
print(c2.wheels)
#c2.info()

print(Car.wheels)

