"""
File I/O
Reading a file -> .read()
reading line by line -> .readline()
"""

my_file = open("firstfile.txt", 'r')

print(str(my_file.read()))
my_file.close()

print("=====READ LINE BY LINE======")

my_file = open("firstfile.txt", 'r')
print(str(my_file.readline()))
print(str(my_file.readline()))
print(str(my_file.readline()))

my_file.close()
