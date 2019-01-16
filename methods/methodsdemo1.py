"""
METHODS - group of code statements that complete some sort of work flow
"""
#Not a Method
a = 3 + 2
print(a)

#This is a method

def sum_nums():
    print(3 + 2)

sum_nums()

#this method take arguments
def sum_num1(n1, n2):
    print(n1 + n2)

sum_num1(5, 9)
sum_num1(80, 52)

print("*" *20)

# Append is a method in the list class.
# already provided by python
l =[1,2,3]
print(l.append(4))
print(l)

print("*" *20)
#Len is also a method provided by python
print(len(l))