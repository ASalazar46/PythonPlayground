# -----
# -----
# Sets and FrozenSets
# -----
# -----

# Initialize a set with values
from random import sample


set1 = {'blue', 'orange', 'green', 'green', 'yellow'}
print('A set initialized:', set1)

# Use a set comprehension
set2 = {char for char in 'alkjhvawfdoliqadfpapksdfpqeow' if char not in 'aeiou'}
print('A set comprehended:', set2)

# Create with set constructor method
set3 = set(['o', 'm', 'e', 'g', 'a'])
print('A set constructed:', set3)

# Create a frozen set with the constructor method
set4 = frozenset(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
print('A frozen set constructed:', set4)

# ---------------------------------------------
# Sets are mutable. Frozen sets are immutable.
# However, both variants share these methods
# ---------------------------------------------

sampleSet = {'blue', 'orange', 'green', 'red', 'yellow', 'purple'}
print('Sample set:', sampleSet)
sampleSet2 = {'gray', 'black', 'white', 'red'}
print('Sample set 2:', sampleSet2)

# Get the length of the set
print('Length of sample set:', len(sampleSet))

# Check for item membership and non-membership
print('Is \'blue\' in the sample set?', 'blue' in sampleSet)
print('Is \'asdf\' NOT in the sample set?', 'asdf' not in sampleSet)

# Check if a set is disjoint to another set
print('Is sample set 1 disjoint to sample set 2?', sampleSet.isdisjoint(sampleSet2))

# Check if a set is subset
print('Is sample set 1 a subset of sample set 2?', sampleSet.issubset(sampleSet2))
print('Is sample set 1 a subset of sample set 2?', sampleSet <= sampleSet2)
print('Is sample set 1 a subset of sample set 2?', sampleSet < sampleSet2)

# Check if a set is a superset
print('Is sample set 1 a superset of sample set 2?', sampleSet.issuperset(sampleSet2))
print('Is sample set 1 a superset of sample set 2?', sampleSet >= sampleSet2)
print('Is sample set 1 a superset of sample set 2?', sampleSet > sampleSet2)

# Create a new set with the union of two sets
print('Uniting two sets:', sampleSet | sampleSet2)

# Create a new set with the intersection of two sets
print('Items in common between two sets:', sampleSet & sampleSet2)

# Create a new set with the difference in items (items in one set, but not the other)
print('Items in sample set 1, and not in sample set 2:', sampleSet - sampleSet2)
print('Items in sample set 2, and not in sample set 1:', sampleSet2 - sampleSet)

# Create a new set with symmetric difference in items (items in either set, but not both)
print('Items in either set, but not both:', sampleSet ^ sampleSet2)

# Copy a set
newSet = sampleSet.copy()
print('Copying sample set 1:', newSet)

# -------------------------------------------------------
# Sets, but not frozen sets, have access to these methods
# -------------------------------------------------------

sampleSet3 = {'blue', 'orange', 'green', 'red', 'yellow', 'purple', 'gray', 'black', 'white'}
print('Sample set 3:', sampleSet3)

# Update a set with all item from another set
tempSet = sampleSet3.copy()
otherSet = {'1', '2', '3'}
tempSet |= otherSet
print('Sample set 3 after update:', tempSet)

# Update a set with intersecting items from another set
tempSet = sampleSet3.copy()
otherSet = {'red', 'yellow', 'blue'}
tempSet &= otherSet
print('Sample set 3 after intersection update:', tempSet)

# Update a set, removing items found in other sets
tempSet = sampleSet3.copy()
otherSet = {'red', 'yellow', 'blue'}
tempSet -= otherSet
print('Sample set 3 after difference update:', tempSet)

# Update a set, removing items found in either set, but not both sets
tempSet = sampleSet3.copy()
otherSet = {'red', 'yellow', 'blue'}
tempSet ^= otherSet
print('Sample set 3 after symmetric difference update:', tempSet)

# Add an item
tempSet = sampleSet3.copy()
tempSet.add('magenta')
print('Added \'magenta\':', tempSet)

# Remove an item (throws error if item not found)
tempSet.remove('magenta')
print('Removed \'magenta\':', tempSet)

# Discard an item if present
tempSet.discard('magenta')
print('Attempted to remove \'magenta\'', tempSet)
tempSet.discard('gray')
print('Attempted to remove \'gray\'', tempSet)

# Pop an item from the set
tempSet.pop()
print('Popped an item:', tempSet)
tempSet.pop()
print('Popped an item:', tempSet)
tempSet.pop()
print('Popped an item:', tempSet)

# Clear the set
tempSet.clear()
print('Cleared the set:', tempSet)