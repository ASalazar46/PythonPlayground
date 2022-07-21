# Day 5
# Exception Handling

# Errors occur when the code does something that it 
# should not have done and it knows about it. Unhandled
# errors terminates the script, so we need to handle them.

# Dividing by zero is an example
'''print(9/0)''' # Console prints "ZeroDivisionError: division by zero"

# Use 'try' and 'except' blocks to handle errors
try:
    x = int(input('Give a number: '))
    y = int(input('Give another number: '))
    print(x / y)
except:
    print('Error caught. Which error, though?')

# You can specify different 'except' blocks for different errors
try:
    x = int(input('Give a number: '))
    y = int(input('Give another number: '))
    print(x / y)
except ZeroDivisionError:
    print('Zero denominator detected. No dividing by zero.')
except ValueError:
    print('Give me numbers, not non-numbers.')

# 'finally' blocks contain code that will always execute 
# regardless of errors or not.
try:
    x = int(input('Give a number: '))
    y = int(input('Give another number: '))
    print(x / y)
except ZeroDivisionError:
    print('Zero denominator detected. No dividing by zero.')
except ValueError:
    print('Give me numbers, not non-numbers.')
finally:
    print('COOL')

# Raise exceptions whenever we know that an error will occur in 
# specific conditions
def raise_exception():
    if True:
        raise Exception('An exception was raised.')
'''raise_exception()'''

# You can specify different exceptions and errors, too
def raise_zeroDivider():
    if True:
        raise ZeroDivisionError('Hey, no dividing by zero.')
'''raise_zeroDivider()'''

# Use 'assert' statements to check for true conditions, and 
# indirectly raise exceptions on false conditions
def assert_this():
    x = 6
    y = 9
    assert(x < y)
    assert (x > y)
assert_this()