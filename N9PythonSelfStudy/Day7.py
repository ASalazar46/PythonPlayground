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
# so on and so forth, see python docs

# Strings can be formatted