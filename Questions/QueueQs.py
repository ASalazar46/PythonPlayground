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


# Implement a stack using a queue

#Q_Q1(0)
#Q_Q1(5)
#Q_Q1(10)