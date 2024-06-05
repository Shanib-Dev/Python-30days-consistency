"""Python Numbers"""
#There are three numeric types in Python:
""" 1.int 2.float 3.complex """
"1.Int"
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#Example
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

"""Float"""
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#Example
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

"""Complex"""
#Complex numbers are written with a "j" as the imaginary part:
#Example
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

"""Type Conversion"""
#You can convert from one type to another with the int(), float(), and complex() methods:
#Example
#Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

"""Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
"""
#Example
#Import the random module, and display a random number between 1 and 9:

import random
print(random.randrange(1,10))

