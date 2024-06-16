# math functions in python

# round function
# syntax: round(number, digits)
# number: the number to be rounded
# digits: the number of digits to round the number to

# round to the nearest integer
print(round(3.14159, 2)) # 3.14


# abs function
# syntax: abs(number)
# number: the number to find the absolute value of
# abs(-20) = 20

# find the absolute value of a number
print(abs(-32)) # 32
# find the absolute value of the difference between two numbers
print(abs(32 - 56)) # 24


# floor function
# syntax: math.floor(number)
# number: the number to find the floor of

# find the floor of a number
import math
print(math.floor(3.14159)) # 3
print(math.floor(-3.14159)) # -4


# ceil function

# syntax: math.ceil(number)
# number: the number to find the ceiling of

# find the ceiling of a number
print(math.ceil(3.14159)) # 4
print(math.ceil(-3.14159)) # -3



# sqrt function
# syntax: math.sqrt(number)
# number: the number to find the square root of

# find the square root of a number
print(math.sqrt(9)) # 3.0


# pow function
# syntax: math.pow(base, exponent)
# base: the base number
# exponent: the exponent

# find the result of raising a number to a power
print(math.pow(2, 3)) # 8.0


# log10 function
# syntax: math.log10(number)
# number: the number to find the base 10 logarithm of

# find the base 10 logarithm of a number
print(math.log10(1000)) # 3.0