"""
execute statements repeatedly
conditions are used to stop the execution of loops
iterable items are strings, lists, tuples, dictionary
"""

# while x < 10:
#    print("value of x is " + str(x))
#     x = x + 1
#     print("one more line")

l =[]
num =0
while num < 10:
    l.append(num)
    print("Value if x is " + str(num))
    num += 1
print(l)


import time

y = 10

while y > 0:
    y = y-1
    print("%d" % (y))
    time.sleep(1)
print("poof")
