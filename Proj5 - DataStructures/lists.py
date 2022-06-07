# ------
# Lists
# ------

# Create an empty list
list1 = []
print('Creating an empty list called list1:')
print(list1)

# Initialize a list with values
list2 = [1, 2, 3, 4]
print('Initialize list 2 with values:') 
print(list2)

# Use list comprehension to make a list
# [<function> for item in <iterable>]
# Apply <function> to each item in <iterable> and list it
list3 = [item ** 2 for item in list2] 
print('Squaring items in list 2 to make list 3:')
print(list3)

# Use Python's built-in list() constructor
# list(iterable)
list4 = list([item ** 2 for item in list3])
print('Squaring items in list 3 to make list 4:')
print(list4)

# Lists are a sequence data type in Python, so they
# have access to these methods:

# Check if a specific item exists in the list
print('Does 1 exist in list2?', 1 in list2)

# Check if a specific item DOES NOT exist in the list
print('Does \'a\' NOT exist in list 2?', 'a' not in list2)

# Concatenate two lists
listCat = [1, 2, 3] + ['a', 'b', 'c']
print('Concatenating [1, 2, 3] and [\'a\', \'b\', \'c\']')
print(listCat)

# Repeat a list that repeats itself an amount of times
repeatList = listCat * 2
print('Repeating a list twice:')
print(repeatList)

# Access the item at a specific list index
print('Accessing the 2nd item in the list:')
print(repeatList[1])

# Access a slice of the list from i to j
print('Accessing a slice of the list:')
print(repeatList[2:9])

# Access a slice of the list from i to j, stepping by k
print('Same slice, but every other item')
print(repeatList[2:9:2])

# Get the length of the list
print('Length of list:', len(repeatList))

# Get

