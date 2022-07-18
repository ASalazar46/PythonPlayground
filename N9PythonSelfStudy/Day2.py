# Day 2
# User Input and Conditions

# User Input
# Get input from a user with the input() function
userInput = input("Give me an input: ")

# Input is read as a string, so convert it to a 
# different data type if you dont need a string,
# if possible.
print("You gave me:", userInput, ", a ", type(userInput))

# Conditions
# An "if" statements checks for a true statement,
# then executes the code within its code block.
# An "Else" statement can follow an "if" statement
# to execute code when the statement is false.
# An "elif" statement can follow an "if" statement, but
# before an "else" statement to check for different
# true conditions.
x = input("Give a number: ")
y = input("Give another number: ")

x = int(x)
y = int(y)

if x < y:
    print("{0} is less than {1}.".format(x, y))
    if x == 69:
        print("x is 69... Nice.")
    if y == 69:
        print("y is 69... Nice.")

elif x == y:
    print("{0} is equal to {1}.".format(x, y))
    if x == 69 and y == 69:
        print("Double nice.")
else:
    print("{0} is greater than {1}.".format(x, y))
    if x == 69:
        print("x is 69... Nice.")
    if y == 69:
        print("y is 69... Nice.")

# Conditions can be nested in condition code blocks to
# form complex condition checking and logic structures