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
with open('./readfile.txt', 'r') as F:
    text = F.read()

print(text)

# Write to a file
with open('writefile.txt', 'w') as F:
    F.write("I wrote this sentence with code into this file.")

