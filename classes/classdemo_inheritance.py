
class Car(object):
    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("car started")

    def stop(self):
        print("car stopped")

# BMW class inherits from the car class
class BMW(Car):

    def __init__(self):
        # This initializes the car class in the BMW class
        Car.__init__(self)
        print("you just created the BMW instance")

c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()
