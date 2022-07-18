# Day 3
# Loops and Collections

# Loops
# A "while" loop executes code within its code block
# until its condition becomes false
x = 0
while x < 10:
    print(x)
    x += 1

# Always make sure that the condition eventually returns
# false, otherwise we get an infinite loop. Have some code within
# the block that updates variables used in the condition statement.

# But if you do want an infinite loop, then using True as the 
# statement works
"""
while True:
    print("Infinite Loop!")
"""

# A "for" loop executes code within its code block a specific
# amount of times. The number of times executed is determined by
# the objects given to the "for" loop.
x = 0
for x in range(10):
    print(x)

# In this case, x is an item within the given object, range(10),
# which is a sequence (learn about later). "For" loops are good
# at applying code to each item within a sequence or collection
# of data (learn about later)

# To manually break out of a loop, use "break"
x = 0
while x < 10:
    print(x)
    if x == 5:
        print("x is 5. Breaking out...")
        break
    x += 1

# To go to the next item of the loop without executing code past
# a certain point, use "continue"
x = 0
for x in range(10):
    if x == 5:
        print('5?')
        continue
    print(x)

# Use the "pass" statement to fill in code blocks with temporary
# non functionality. Best for making code stubs; you know, generally,
# what you need but dont exactly know what, and you want to skip the
# errors of putting nothing in a code block before code runtime.

x = 0
y = 10
z = 50

"""
if x == 50 and y == 0 and z == 10:

print('asdf')

This code fails because nothing is written inside of the if statement.
Use 'pass' within it to make it a stub and avoid errors.
"""

if x == 50 and y == 0 and z == 10:
    pass

print('asdf')

# Collections
# A sequence is a collection of indexed elements, the whole of which
# acts as one object. Indices are used to access specific elements of a 
# sequence, starting at index 0 for the first element.

# A list is a mutable sequence. Its size is dynamic, and is not limited 
# to a single data type.
aList = [10, '20', 30.0]
print(aList)

# Access single elements with their index
print('First item:', aList[0]) # from left to right
print('Last item:', aList[-1]) # from right to left

# Get a slice of the sequence
print('A slice of the first two elements:', aList[0:2])

# Replace or update elements with new values
aList[0] = 'Fourty'
print(aList)

# Iterate through a list, printing its contents
for x in aList:
    print(x)

# List operations and methods
# Operations
x = [1, 2, 3]
y = [4, 5, 6]

print(x + y) # Append a list with another list
print(x * 4) # Repeat the give list an amount of times

# Methods
print(len(x)) # Get the length of the list
print(max(x)) # Get the biggest value in the list
print(min(x)) # Get the smallest value in the list
# Use max() and min() in lists of only numeric values, avoid using
# with lists that contain strings

x.append(7) # Append (add to the end) a value to the list
print(x)

x.insert(1, "a value") # Insert at an index a new value
print(x)

x.remove(7) # Remove the first instance of the given value in the list
print(x)

x.pop(0) # Remove the value at the given index
print(x)

print(x.index('a value')) # Get the index of the given value

x = [42, 99, 1, 81, 63]
print(sorted(x)) # Sort the list in ascending order, without saving changes
x.sort() # Sort the list in ascending order, saving changes to the list
print(x)

# Tuples are immutable sequences, so we cannot change its elements after
# its initialization. Tuples share the same methods with lists, but
# all methods that would make changes to a list do not work on a tuple. 
# Accessing elements is the same as a list.
aTuple = (1, 2, 3)
print(aTuple)
print(aTuple[0])
print(aTuple[-1])

# Type casting a tuple into a list makes the tuple contents mutable
mutableTuple = list(aTuple)
print(mutableTuple)
mutableTuple[0] = 'one'
mutableTuple[1] = 'two'
mutableTuple[2] = 'three'
print(mutableTuple)

# and the reverse way works too
reTupled = tuple(mutableTuple)
print(reTupled)

# Dictionaries are not sequences, but mappings. Instead of indices,
# each element is a key:value pair. 
aDict = {'Name': 'John Smith', 'Age': 24, 'Gender': 'M'}
print(aDict)
print(aDict['Name']) # Access dictionary values by keys
# Keys can be anything, but best practices are keys that are
# unique and immutable

aDict['Height'] = 200 # Add a new key:value pair to the dictionary
print(aDict['Height'])

# Print a list of all items in the dictionary
print(aDict.items())
# Print a list of all the keys in the dictionary
print(aDict.keys())
# Print a list of all the values in the dictionary
print(aDict.values())

# The return value of these three methods are view objects. Use
# list() to type cast them into something a bit more readable.
print(list(aDict.items()))
print(list(aDict.keys()))
print(list(aDict.values()))

# Membership operators
# Operators that check if an element exists in a sequence

x = [1, 2, 3]
# 'in' checks if it exists
print(2 in x)

# 'not in' checks if it does not exist
print(10 in x)

# Identity operators
# Operators that check if something is a specific type

# 'is' checks if the object is of a certain data type
# 'is not' checks if the object is not a certain data type
if type(x[0]) is int:
    print("x is int")
elif type(x[0]) is not int:
    print('x is not int')