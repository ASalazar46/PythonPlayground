from collections import deque

# Stack implementation from the 'deque' class in the 'collections' module
dequeStack = deque()
print('New stack:', dequeStack)

dequeStack.append(1)
print('Stack list:', dequeStack)
dequeStack.append(2)
print('Stack list:', dequeStack)
dequeStack.append(3)
print('Stack list:', dequeStack)

dequeStack.pop()
print('Stack list:', dequeStack)
dequeStack.pop()
print('Stack list:', dequeStack)
dequeStack.pop()
print('Stack list:', dequeStack)

try:
    dequeStack.pop()
except IndexError:
    print('Attempted to pop, but stack is empty.')
    print('An IndexError was thrown, as a result. (but caught, hence this message.)')

# Stack implementation using a list and its methods
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

# Checking for class functionality
testStack = Stack()
print('New stack:', testStack.stack)

testStack.push('a')
print('Stack list:', testStack.stack)
testStack.push('b')
print('Stack list:', testStack.stack)
testStack.push('c')
print('Stack list:', testStack.stack)

testStack.pop()
print('Stack list:', testStack.stack)
testStack.pop()
print('Stack list:', testStack.stack)
testStack.pop()
print('Stack list:', testStack.stack)

try:
    testStack.pop()
except IndexError:
    print('Attempted to pop, but stack is empty.')
    print('An IndexError was thrown, as a result. (but caught, hence this message.)')
