# Day 4

# Functions

# Functions are reusable blocks of code. Makes code less repetitive.
def IamAFunction():
    print('I am a function.')

# Call functions in code with this:
IamAFunction()

# Functions can take parameters and do things with those.
def adder(x, y):
    print('Sum:', x + y)
    return x + y

z = adder(10, 20)
print('Returned result:', z)

# Functions that require parameters must be given arguments,
# unless you specify default values
def DefaultAdder(x=0, y=0):
    print('Sum:', x + y)

DefaultAdder()
DefaultAdder(10, 20)

# Sometimes we dont know how many parameters a function
# needs, so we can make a function that takes a variable
# amount of arguments.
def accumulator(*nums):
    acc = 0
    for number in nums:
        acc += number
    return acc

print('Accumulated sum:', accumulator(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))