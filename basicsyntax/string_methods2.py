"""
Examples to show available string methods
in python
"""

'''
the number in replace dictactes the number of times you want to replace something in the string
'''
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC', 2))

# Substrings
# starting index inclusive and ending index is exclusive, it will
# start where you want it to but will stop 1 before the index you specify
# step - the index works in steps, in the example below we print index 1-5
# jumping 2 steps each time

sub= a[1:6]
step = a[1:6:2]

print("*******************")

print(sub)
print(step)
