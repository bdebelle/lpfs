"""
some built in functions
max(): it takes any number of arguments and returns the largest one

min(): it takes any number of arguments and returns the smallest one

abs(): it returns the absolute value of the number, that numbers distance from 0
it always returns a positive value and it only takes a single number

type(): it returns the type of the data it receives as an argument
"""

# the *args lets the function know this can take unlimited arguments
def largest_num(*args):
    # no need for * when calling inside
    print(max(args))

largest_num(-20, -10, 0, 10, 100)

def smallest_num(*args):
    print(min(args))

smallest_num(-20, -10, 0, 10, 100)

def abs_function(a):
    print(abs(a))


abs_function(-100)
abs_function(-19)

print("*"*20)

print(type(99))
print(type(99.9))
print(type("99.9"))
l = [1,2,3]
print(type(l))