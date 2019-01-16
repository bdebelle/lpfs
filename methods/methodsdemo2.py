"""
A group of statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""

def sum_num(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2
#Return will store that out put for later use below

#set variable equal to method and arguments
sum1 = sum_num(5, 9)
sum2 = sum_num(80, 52)

#print the outcome of the method
print(sum1)
print(sum2)

string_add = sum_num('one', 'two')
print(string_add)

print("*"*20)

def isMetro(city):
    """
    Check if argument is city in our list
    :param city:
    :return:
    """
    l = ["SFO", "NYC", "LA"]

    if city in l:
        return True
    else:
        return False

x = isMetro("Boston")
y = isMetro("LA")
print(x)
print(y)
