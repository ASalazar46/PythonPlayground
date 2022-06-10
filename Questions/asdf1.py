# Problem: Compress a string so that it displays the character count
# next to its respective character. Example: aaaabbbcc compresses
# to a4b3c2, or aabbccdd compresses to a2b2c2d2

# My Solution
string = input('Input a string to compress --> ')
checked = []
listStr = []

for char in string:
    if char not in checked:
        listStr.append(char)
        listStr.append(str(string.count(char)))
        checked.append(char)

print(''.join(listStr))
