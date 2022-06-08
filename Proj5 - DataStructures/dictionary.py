# ----------
# ----------
# Dictionary
# ----------
# ----------

# Create a dictionary with initial key:value pairs, called mappings
dict1 = {'a': 1, 'b': 2, 'c': 3}
print('Dictionary 1:', dict1)

# Can also use a dictionary comprehension
dict2 = {str(x)+'**2': x**2 for x in range(10)}
print('Dictionary 2:', dict2)

# Can also use the built-in dict() function
dict3 = dict([('A', 95), ('B', 85), ('C', 75), ('D', 65)])
print('Dictionary 3:', dict3)

# ----------------------------------------------
# A dictionary is a mapping data type, and is the only built-in
# mapping data type in Python (not looking at importable modules
# or libraries). It has access to these methods:
# ----------------------------------------------

# Display all the keys used in the dictionary
print('Listing all of the keys in Dictionary 1:')
print(list(dict1))

# Get the length of the dictionary
print('Length:', len(dict1))

# Get the value mapped to a key
print('Accessing the value of \'a\':', dict1['a'])

# Set a value to a key
dict1['d'] = 4
print('Added \'d\' to dictionary:', dict1)

# Remove a key from the dictionary
del dict1['d']
print('Removed \'d\' from dictionary:', dict1)

# Check if a key exists in the dictionary
print('Does \'a\' exist?', 'a' in dict1)

# Check if a key does not exist in the dictionary
print('Does \'z\' NOT exist?', 'z' not in dict1)

# Copy the contents of the dictionary
tempDict1 = dict1.copy()
print('Copying to new dictionary:', tempDict1)

# and then delete them
tempDict1.clear()
print('Emptied it out:', tempDict1)

# Make a new dictionary by taking keys from an existing
# dictionary and changing its values
newDict1 = dict1.fromkeys(dict1, [10, 20, 30])
print('Made a new dictionary with different values:', newDict1)

# Get the value mapped to a key. Does not throw an error, 
# as a value is always returned. If the key does not exist,
# 'None' is returned.
print('Value of \'a\':', dict1.get('a'))
print('Value of \'z\':', dict1.get('z'))

# Pop a key's value and return it. If key does not exist, then return
#  a specified value. If not both of these, then throw an error 
print('Popped \'a\':', dict1.pop('a'))
print('Could not pop \'z\', so return \'asdf\' instead:', dict1.pop('z', 'asdf'))

# Pop an entire key:value pair from the dictionary, Last-In First-Out style
# i.e: pairs last in are popped from the dictionary first
print('Popped an entry:', dict1.popitem())

# Set or get a key's value. If the key does not exist, make it exist and return that.
# If it does exist, return the existing value
print('Dictionary 1 so far:', dict1)
print('Adding \'c\' with value 3:', dict1.setdefault('c', 3))
print('Accessing \'b\':', dict1.setdefault('b'))
print('Adding \'a\' with default value:', dict1.setdefault('a'))
print('Dictionary 1 now:', dict1)

# Update a dictionary 
dict1.update(a = 1)
dict1.update([('1', 'a'), ('2', 'b'), ('3', 'c')])
dict1.update(dict3)
print('Dictionary 1 after updates:')
print(dict1)

# -------------------------------------
# The below methods return dictionary view objects, which provides a snapshot
# of current dictionary entries. When the dictionary changes, so do the values
# returned by these methods.
# --------------------------------------

# Return a dictionary view object of the items in a dictionary
print('Items in Dictionary 1:', dict1.items())

# Return a dictionary view object of the keys in a dictionary
print('Keys in Dictionary 1:', dict1.keys())

# Return a dictionary view object of the values in a dictionary
print('Values in Dictionary 1:', dict1.values())


