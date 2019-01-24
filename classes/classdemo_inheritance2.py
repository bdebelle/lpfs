

class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("car started")

    def stop(self):
        print("car stopped")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("you just created the BMW instance")
#overide function in parent class
    def drive(self):
        #super will call the funtions of drive from the parent
        super(BMW, self).drive()
        print('You are driving a BMW, hope it doesnt break down')


    def heads_up(self):
        print("heads up activated")

# c = Car()
# c.drive()
# c.stop()

b = BMW()
b.drive()
b.stop()
#only available in the BMW class, not the car class
b.heads_up()
