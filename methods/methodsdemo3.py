"""
Positional Parameters
Think "optional parameters
and can be assigned a default value, if no value is provided from the outside
"""
def sum_num(n1=2, n2=4):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

#assign values
sum1 = sum_num(n1=8, n2=12)
print(sum1)

#use default values
sum2 = sum_num()
print(sum2)

#positional -- position doesnt matter
sum3 = sum_num(n2=5, n1=100)
print(sum3)
#positional 
sum4 = sum_num(5, n2=13)
print(sum4)