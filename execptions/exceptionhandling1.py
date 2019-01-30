'''
Exceptions are errors
we should handle exceptions in our code
to make sure the code is working the way we want
and is handling all the unwanted issues
link to 3.5 built-in exceptions:
https://docs.python.org/3/library/exceptions.html
'''

def exceptionhandling():
    try:
        a = 10
        b = "any string"
        c = 10

        d = (a + b) / c
        print(d)
    except TypeError:
        print("cant add a string to an intiger")

exceptionhandling()

def exceptionhandling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    except ZeroDivisionError:
        print("You are trying to divide by zero")

exceptionhandling()

