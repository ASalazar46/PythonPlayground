# ------
# ------
# Lists
# ------
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

# -------------------------------------------------
# Lists are a sequence data type in Python, so they
# have access to these methods:
# -------------------------------------------------

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

# Get the smallest and largest item on the list
# Supports ints, but not str
numList = [19, 88, 74, 79, 23, 19, 23, 74, 79, 88]
print('Number List:', numList)
print('Smallest item in the list:', min(numList))
print('Largest item in the list:', max(numList))

# Find the first instance of an item in a list, given a starting point
# and an ending point
print('Finding the first instance of 19 in the second half of the list: index', numList.index(19, 5, 11))

# Count the occurences of an item in the list
print('Total occurences of 19:', numList.count(19))

# ------------------------------------------------------------------
# Lists are a mutable sequence type, meaning its contents can be 
# changed after initialization. As such, lists have access to these methods
# ------------------------------------------------------------------
listA = [1, 2, 3, 4, 5, 'f']
print('List A:', listA)

# Replace a list item with a new item
listA[5] = 6
print('Replaced the 5th index with 6:', listA)

# Or replace a slice of the list with items from another iterable
listA[:] = ['a', 'b', 'c', 'd', 'e', 'f']
print('Replaced the list with new items:', listA)

# Or replace a slice of the list with items form another iterable, but stepping
listA[: : 2] = ['1', '3', '5']
print('Replaced every other list item with a new item:', listA)

# Delete items from the list by adding the 'del' keyword 
# in front of these commands
del listA[5]
print('Deleted \'f\':', listA)

del listA[3:]
print('Deleted \'d\' and 5:', listA)

del listA[: : 2]
print('Deleted every other item in the list:', listA)

listA = ['a', 'b', 'c', 'd', 'e', 'f']
print('Refreshing the list:', listA)

# Append an item to the list
listA.append('g')
print('Appending \'g\' to the list:', listA)

# Create a copy of the list
listB = listA.copy()
print('Created a new copy of the list:', listB)

# and remove all of the copy's items
listB.clear()
print('Emptied the copied list:', listB)

# Extend a list with another list
listB.extend(listA)
# listB += listA also works
print('Extended the copy with the original:', listB)

# Repeat list contents an amount of times
listB *= 2
print('Repeated list contents twice:')
print(listB)

# Insert an item at a specified index
listB.insert(5, 99)
print('Inserted 99 at index 5')
print(listB)

# Pop the last item from the list
listB.pop()
print('Popped the last item from the list:')
print(listB)

# Pop the item in index i
listB.pop(5)
print('Popped the item at index 5')
print(listB)

# Remove the first instance of an item in the list
listB.remove('b')
print('Removed the first instance of \'b\':')
print(listB)

# Reverse the list
listB.reverse()
print('Reversed the list:')
print(listB)

# ----------------------------------------
# A list is an instance of the List class. This class has a 
# method to sort its items
# ----------------------------------------
listB.sort(key=str.lower)
print('Sorting the list in order:')
print(listB)
