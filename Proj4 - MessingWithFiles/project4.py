import secrets
import string

# Read the contents of the file by ...
readFile = open('asdfRead', 'r', encoding='utf-8')

'''
# ... reading the entire file
fileData = newFile.read()
print(fileData)
'''

# ... reading line by line
for line in readFile:
    print(line, end='')

'''
# ... listing each line 
contents2 = list(newFile)
print(contents2)

newFile.seek(0, 0)

contents1 = newFile.readlines()
print(contents1)
'''

readFile.close()

'''
# Use a with statement to execute file methods and ensure
# that a file closes, regardless of result
with open('asdfRead', encoding='utf-8') as readFile:
    print(readFile.read())
'''

# Write contents to a file by ...
writeFile = open('asdfWrite', 'w', encoding='utf-8')

# ... passing the write() method a string to write
toWrite = 'I am a string, and I have been written to the file.'
chars = writeFile.write(toWrite)
print('Characters written:', chars)

writeFile.close()

# Writing to a file that already exists and has contents in it 
# will have those contents truncated
writeFile = open('asdfWrite', 'w', encoding='utf-8')
symbolSet = string.ascii_lowercase + string.digits
chars = writeFile.write(''.join(secrets.choice(symbolSet) for char in range(10)))
print('Characters written:', chars)

writeFile.close()

# Change the mode to 'a' (appending) if you want to write more to the end of the file
writeFile = open('asdfWrite', 'w', encoding='utf-8')
toWrite = 'I am a string, and I have been written to the file.'
chars = writeFile.write(toWrite)
print('Characters written:', chars)
writeFile.close()

writeFile = open('asdfWrite', 'a', encoding='utf-8')
symbolSet = string.ascii_lowercase + string.digits
chars = writeFile.write(''.join(secrets.choice(symbolSet) for char in range(10)))
print('Characters written:', chars)
writeFile.close()
