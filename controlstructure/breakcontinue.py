"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""

x = 0
while x < 10:
    print("value of x is: " + str(x))
    x = x + 1
# comment out 2 lines below to test 'else'
    if x == 8:
        break
    print("this example is awesome")
    print("*"*20)
else:
    print("just broke out of the loop")

# x = 0
# while x < 10:
#     print("value of x is: " + str(x))
#     x = x + 1
#
#     if x == 8:
#         continue
#     print("this example is awesome")
#     print("*"*20)
#
# print("just broke out of the loop")

