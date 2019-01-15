"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, lists, tuple, Dictionary
"""
#Strings for loop
my_string = "abcabc"

for c in my_string:
    if c == 'a':
        print("A",  end=' ')
    else:
        print(c, end=' ')

print()

#Lists for loop - same applies to tupple
cars =["benz", "Honda", "bmw"]

for car in cars:
    print(car)

#list manipulation - same applies to tupple
nums = [1,2,3]
for n in nums:
    print(n * 10)

print("*"*20)

#Dictionary for loop - print keys
d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k)

print("*"*20)

#Dictionary - print keys and values
d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k+ " " +str(d[k]))

print("*"*20)
#Dictionary - print keys and values
for k,v in d.items():
    print(k)
    print(v)