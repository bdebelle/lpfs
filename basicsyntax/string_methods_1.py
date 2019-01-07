"""
Examples to show available string methods in pyhton
"""

# Accessing Characters in a string
# index starts from 0
zero = "nyc"[0]
print(zero)
city = "SFO"
first = "nyc"[1]
print(first)

second = "nyc"[2]
print(second)

ft = city[0]
print(ft)

"""
len() -- return length of string
lower() -- make lower case
upper() -- make upper case
str() -- make non string character string
"""

stri = "This is a mixeD Case"

print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))

"""
concatination
"""

print("Hello " + " "+ " World !!!")
print(zero + " " + city)