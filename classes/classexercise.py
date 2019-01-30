'''
Create a fruit class
define 3 mothods in this class
    __init__()
    nutrition()
    fruit_shape()

Print anything you like in these methods
****************************************
Create one more class (Any fruit name)
This class should inherit from the Fruit class created above,
this will become the child class and “Fruit” will be referred as
parent class to this class


Define 3 methods in this class
    __init__()
    nutrition()
    color()
Print anything you like in these methods

Created instances of these classes and call methods from them
Call methods from the base class also using the instance of the child class

'''

class Fruit(object):

    def __init__(self):
        print("Ah shit its the Fruit Class")

    def nutrition(self):
        print("Whats the nutrition info on this?")

    def fruit_shape(self):
        print("what shape is this fruit")

class Orange(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("Oh look here we got an orange class")

    def nutrition(self):
        print("this orange is nutritious")

    def color(self):
        print("this orange is very round")


f = Fruit()
f.nutrition()
f.fruit_shape()

o = Orange()
o.nutrition()
o.fruit_shape()
o.color()