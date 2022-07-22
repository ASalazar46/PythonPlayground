# Day 7
# Strings and string operations/functions

someStr = 'I am a string.'

# Length of a string
print(len(someStr))

# A string is a list of characters, so someStr is
# can be represented as such
print(list(someStr))

# Because strings are lists, they can be indexed and 
# sliced as such
print(someStr[9])
print(someStr[0:10])

# Strings are iterable
for char in someStr:
    print(char, end='')
print('\n')

# If we want to represent a new line in a string, use '\n'
print('aaaaaaaaaa\nbbbbbbbbbb')
# There are other escape characters:
# \t tab
# \b backspace
# \s space
# so on and so forth, see python docs for others

# Strings can be formatted with variables
# %s expects a string, %d expects an integer
name = 'John String'
age = 9999
print('My name is %s, and I am %d years old.' % (name, age))

# or

print('My name is {}, and I am {} years old.'.format(name, age))

# String Functions
# For a complete list of functions, see the python docs

# Convert a string into all upper case letters
allUpperCaseStr = someStr.upper()
print(allUpperCaseStr)

# Convert a string into all lower case letters
allLowerCaseStr = someStr.lower()
print(allLowerCaseStr)

# Capitalize the first letter of every word (title)
titleStr = someStr.title()
print(titleStr)

# Swap the cases of a string
swappedStr = someStr.swapcase()
print(swappedStr)

# Count the number of times a substring appears in a string.
# Can be used to find number of times a word appears in a string.
repeatedStr = someStr * 4
print(repeatedStr.count('string'))
print(repeatedStr.count(''))

# Find the position of a given substring in a string
# If multiple instances of the substring exist, it
# gives the position of the first instance
print(someStr.find('string'))

# Join elements of a list, separated by a given character
delimiter = '-'
joinList = ['111', '222', '3456']
print(delimiter.join(joinList))

# Split a string into a list by a given character
print(someStr.split(' '))

# Replace all instances of a substring with a
# different substring
print(someStr.replace('string', 'STRINGSTRINGSTRING'))