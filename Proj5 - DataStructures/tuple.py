# -----
# -----
# Tuple
# -----
# -----

# Create an empty tuple
emptyTuple = ()
print('Empty tuple:', emptyTuple)

# Initialize a tuple with values
initTuple = (1, 2, 3, 4, 5)
print('Filled tuple:', initTuple)

# Initialize a singleton tuple
singleTuple = ('a',)
# Very important to have that trailing comma

# Use the built-in tuple() function to make tuples
emptyTuple2 = tuple()
print('Another empty tuple:', emptyTuple2)

initTuple2 = tuple(['q', 'w', 'e'])
print('Another filled tuple:', initTuple2)

# The parentheses are not needed, but the commas are
noParTuple = 'a', 1, 'b', 2, 'c', 3
print('This is a tuple with no parentheses:', noParTuple)

# ------------------------------------------------------
# Tuples are sequence data types, so they have access to
# sequence methods
# ------------------------------------------------------

seqTuple = ('a', 1, 'b', 2, 'c', 3, 'd', 4)
print('Tuple example:', seqTuple)

print('Is \'a\' in the tuple?', 'a' in seqTuple)
print('Is 99 not in the tuple?', 99 not in seqTuple)

# Concatenating tuples results in a new tuple. Not recommended
# to do this, but you can still do it
print('t0.5_1:', (1, 2, 3))
print('t0.5_2:', ('a', 'b', 'c'))
print('t1:', (1, 2, 3)+('a', 'b', 'c'))

# Repeat a tuple an amount of times
print('Repeat tuple 3 times:', seqTuple*3)

# Access a tuple's items
print('Reading index 2:', seqTuple[2])

# Access a slice of the tuple
print('Reading a slice:', seqTuple[3:7])

# Access a slice, stepping between the slice
print('Stepping between a slice:', seqTuple[3:7:2])

# Get the length of the tuple
print('Length of tuple:', len(seqTuple))

# Get the smallest and largest item in tuple
numTuple = (36451, 34542, 12465, 24146, 12465)
print('Number tuple:', numTuple)

print('Smallest number:', min(numTuple))
print('Largest number:', max(numTuple))

# Find the first occurrence of an item
print('First occurrence of 12465: index', numTuple.index(12465))

# Count total occurrence of an item
print('Total occurrences of 12465 in seqTuple:', numTuple.count(12465))

# ----------------------------------
# Tuples are immutable data types, and have
# access to hash()
# ----------------------------------

# Return a hash value for an object. Used to compare dictionary keys
# in dictionary lookups.
print('Hash value for tuple:', hash(numTuple))
