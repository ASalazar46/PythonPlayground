# Day 1
# Hello World, Data Types, and Operators

# First program (not really, but still)
print('Hello World (again)')

# Data Types and Variables

# Variables are data holders
# Define variables like this: <varName> = <some value>
# In Python, no need to define a variable data type at creation 
intNum = 10 # whole numbers like this
floatNum = 10.999999 # numbers with floating points like this
complexNum = complex(10, 9) # numbers that are complex like this (10 + 9i)
boolVar = True # or False
stringVar = 'I am a string' # Strings are text like this

#Use type() to find the data type of a given object
print(type(intNum)) # gives int
print(type(floatNum)) # gives floats

# Type Casting
# Use this when you want to cast a variable
# as a different data type, if possible
x = "120"
# print(x / 4) gives an error,so cast x as an integer 
x = int(x)
print('After casting x as an int:', x / 4)

# Attempting to cast a string with non numbers into
# a number type will give an error

# Operators

# Arithmetic operators
print("150 + 50 =", 150+50) # addition
print("150 - 50 =", 150-50) # subtraction
print("150 * 50 =", 150*50) # multiplication
print("150 / 50 =", 150/50) # division
print("151 % 50 =", 150%50) # modulus (remainder of division)
print("150 ** 2 =", 150**2) # Exponent
print("151 // 50 =", 150//50) # Floor division (whole number of division)

# Assignment operators
x = 10 # '=' is the assignment operator
x += 10 # '+=' adds 1o to x and assigns x as the new value
# and variants exist for the other arithmetic operators too
x -= 10
x *= 10
x /= 10
x %= 10
x **= 10
x //= 10

# Comparison operators
# Returns True or False depending on what is being compared
10 == 15 # False
10 != 15 # True
10 < 15 # True
10 > 15 # False
10 <= 15 # True
10 >= 15 # False

# Logical operator
# Combine comparison expressions for complex comparisons
# 'and' requires both sides to be true to return true 
10 < 15 and 25 < 35 # True
15 < 10 and 25 < 35 # False 

# 'or' requires only one side to be true to return true
10 < 15 or 25 < 35 # True
15 < 10 or 25 < 35 # True
15 < 10 or 35 < 25 # False

# 'not' negates a comparison result
not True # False
not False # True
not 10 < 15 # False
not 15 < 10 # True