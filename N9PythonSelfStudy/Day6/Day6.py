# Day 6
# File Operators
from os import *

# To work with files, we need to open a file stream
# Use the open() function and give it a filename
# and a mode of operation (r = read, w = write, a = append)
'''file = open('file.txt', 'r')'''

# Opened files must be closed
'''file.close()'''

# Closing a file writes data in the file stream to the
# file and then closes the stream.
# To keep the stream open, but write file stream data
# to the file, use flush()

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

# Append to a file
with open('writeThisFile', 'a') as F:
    F.write('I am an appended sentence.')
with open('writeThisFile', 'r') as F:
    print(F.read())

# We can use the 'os' module to do more file operations

# Make a new directory/folder
'''mkdir('mkdirFolder')'''

# Navigate to the directory
'''chdir('mkdirFolder')'''

# Rename a file
'''rename('readThisFile', 'read')'''

# Remove a file
'''remove('read')'''