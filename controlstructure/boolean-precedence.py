"""
1. not
2. and
3. or
"""

bool_output = True or not False and False
# True or not True and False = True
print(bool_output)

bool_output1 = 10 == 10 or not 10 > 10 and 10 > 10
# True or not False and False = True
print(bool_output1)

bool_output2 = (10 == 10 or not 10 > 10) and 10 > 10
# (True or True) and False = False
print(bool_output2)