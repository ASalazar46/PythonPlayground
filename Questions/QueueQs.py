# ------------------------------------
# Questions related to queues
# https://www.educative.io/blog/8-python-data-structures#queues
# ------------------------------------
import random
from collections import deque

# Reverse first k elements of a queue
def Q_Q1(k):
    print('-'*60)
    if k < 0 or k > 10:
        print('Invalid value of k. 0 <= k <= 10')
    else:
        testQueue = deque([random.randrange(1, 51) for x in range(10)])
        print('Test queue:', testQueue)

        firstKElems = []
        for i in range(k):
            firstKElems.append(testQueue.popleft())
        testQueue.extendleft(firstKElems)
        print('Reversed first {0} Elems: {1}'.format(k, testQueue))
    print('-'*60)


# Implement a queue using a linked list
class LinkedList:
    def __init__(self):
        self._headPtr = None
    
    def printList(self):
        print('-'*60)
        temp = self._headPtr
        while(temp):
            print(temp._data)
            temp = temp._nextPtr
        print('-'*60)

    def append(self, node):
        if isinstance(node, LL_Node) == False:
            print('Argument not of the class LL_Node.')
        else:
            if self._headPtr == None:
                self._headPtr = node
            else:
                temp = self._headPtr
                appended = False
                while(appended != True):
                    if temp._nextPtr == None:
                        temp._nextPtr = node
                        appended = True
                    else:
                        temp = temp._nextPtr

    def popHead(self):
        if self._headPtr == None:
            print('Nothing to pop. Linked list is empty.')
        else:
            temp = self._headPtr
            self._headPtr = self._headPtr._nextPtr
            temp._nextPtr = None

class LL_Node:
    def __init__(self, data):
        self._data = data
        self._nextPtr = None

class QFromLL:
    def __init__(self):
        self._queue = LinkedList()

    def showQueue(self):
        self._queue.printList()

    def enqueue(self, data):
        self._queue.append(data)

    def dequeue(self):
        self._queue.popHead()

def Q_Q2():
    newQueue = QFromLL()
    print(newQueue)
    newQueue.enqueue(LL_Node('First'))
    newQueue.showQueue()
    newQueue.enqueue(LL_Node('Second'))
    newQueue.showQueue()
    newQueue.enqueue(LL_Node('Third'))
    newQueue.showQueue()
    newQueue.enqueue(LL_Node('Fourth'))
    newQueue.showQueue()
    newQueue.enqueue(LL_Node('Fifth'))
    newQueue.showQueue()
    newQueue.dequeue()
    newQueue.showQueue()
    newQueue.dequeue()
    newQueue.showQueue()
    newQueue.dequeue()
    newQueue.showQueue()
    newQueue.dequeue()
    newQueue.showQueue()
    newQueue.dequeue()
    newQueue.showQueue()
    newQueue.dequeue()
    newQueue.showQueue()

# Implement a stack using a queue
class Queue:
    def __init__(self):
        self.q = []

    def push(self, item): # Adding items to the queue is slow
        self.q.reverse() 
        self.q.append(item)
        self.q.reverse()

    def pop(self):
        return self.q.pop()

class StackFromQueue:
    def __init__(self):
        self._q = Queue()

    def push2Stack(self, data):
       self._q.push(data) 

    def popFromStack(self):
        self._q.q.reverse()
        self._q.q.pop()
        self._q.q.reverse()

def Q_Q3():
    stack = StackFromQueue()
    print('Stack items:', stack._q.q)
    stack.push2Stack('First')
    print('Stack items:', stack._q.q)
    stack.push2Stack('Second')
    print('Stack items:', stack._q.q)
    stack.push2Stack('Third')
    print('Stack items:', stack._q.q)
    stack.push2Stack('Fourth')
    print('Stack items:', stack._q.q)
    stack.popFromStack()
    print('Stack items:', stack._q.q)
    stack.popFromStack()
    print('Stack items:', stack._q.q)
    stack.popFromStack()
    print('Stack items:', stack._q.q)
    stack.popFromStack()
    print('Stack items:', stack._q.q)

#Q_Q1(0)
#Q_Q1(5)
#Q_Q1(10)
#Q_Q2()
Q_Q3()