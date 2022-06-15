from collections import deque

# Queue implementation from the 'deque' class in the 'collections' module
dequeQueue = deque()
print('New stack:', dequeQueue)

dequeQueue.appendleft(1)
print('Stack list:', dequeQueue)
dequeQueue.appendleft(2)
print('Stack list:', dequeQueue)
dequeQueue.appendleft(3)
print('Stack list:', dequeQueue)

dequeQueue.pop()
print('Stack list:', dequeQueue)
dequeQueue.pop()
print('Stack list:', dequeQueue)
dequeQueue.pop()
print('Stack list:', dequeQueue)

try:
    dequeQueue.pop()
except IndexError:
    print('Attempted to pop, but queue is empty.')
    print('An IndexError was thrown, as a result. (but caught, hence this message.)')

# Queue implementation using a list and its methods
class Queue:
    def __init__(self):
        self.q = []

    def push(self, item): # Adding items to the queue is slow
        self.q.reverse() 
        self.q.append(item)
        self.q.reverse()

    def pop(self):
        self.q.pop()

# Checking for class functionality
testQueue = Queue()
print('New stack:', testQueue.q)

testQueue.push('a')
print('Stack list:', testQueue.q)
testQueue.push('b')
print('Stack list:', testQueue.q)
testQueue.push('c')
print('Stack list:', testQueue.q)

testQueue.pop()
print('Stack list:', testQueue.q)
testQueue.pop()
print('Stack list:', testQueue.q)
testQueue.pop()
print('Stack list:', testQueue.q)

try:
    testQueue.pop()
except IndexError:
    print('Attempted to pop, but queue is empty.')
    print('An IndexError was thrown, as a result. (but caught, hence this message.)')
