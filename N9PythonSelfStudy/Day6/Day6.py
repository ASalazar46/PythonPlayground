# Day 6
# File Operators

# To work with files, we need to open a file stream
# Use the open() function and give it a filename
# and a mode of operation (r = read, w = write, a = append)
'''file = open('file.txt', 'r')'''

# Opened files must be closed
'''file.close()'''

# Using a 'with' statement automatically opens and closes the stream 
# upon its code block's completion

# Read from a file
with open('readThisFile', 'r') as F:
    print(F.read())

# Write to a file
with open('writeThisFile', 'w') as F:
    F.write('This sentence was written into the file with code.')
    print('Write complete.')
with open('writeThisFile', 'r') as F:
    print(F.read())