"""
variable scope
"""

#variable defined in a method has a local scope
# a = 10
#
# def test_method(a):
#     print("value of local 'a' is: " + str(a))
#     #change value of a to 2 inside method
#     a = 2
#     print("new value of lacal 'a' is: " + str(a))
#
#
# print("Value of global a is: " + str(a))
# test_method(a)
# print("did the value of global a change? " + str(a))

a = 10

def test_method():
    # tells python to use global a with out passing in a
    global a
    print("2. value of local a is: " + str(a))
    # setting a value to 'a' here changes the global value of 'a'
    a = 2
    print("3. new value of lacal a is: " + str(a))

# this happens first
print("1. Value of global a is: " + str(a))
# then we run the method
test_method()
print("4. did the value of global 'a' change? " + str(a))