# ------------------------------------
# Questions related to arrays or lists
# https://www.educative.io/blog/8-python-data-structures#arrays
# ------------------------------------
import random
import itertools
import math

# Remove even integers from list
def LA_Q1():
    testList = [random.randrange(0, 1000) for x in range(100)]
    print('Test list:', testList)
    
    oddList = [x for x in testList if x % 2 != 0]
    print('List with only odds:', oddList)

# Merge two sorted lists
def LA_Q2():
    testList1 = [random.randrange(0, 50) for x in range(10)]
    print('Test list 1:', testList1)
    
    testList2 = [random.randrange(51, 100) for x in range(10)]
    print('Test list 2:', testList2)
    
    mergeList = testList1 + testList2
    print('Merge lists:', mergeList)
    
    sortedList = sorted(mergeList)
    print('Sort list:', sortedList)
    
# Find minimum value in a list
def LA_Q3():
    testList = [random.randrange(0, 1000) for x in range(100)]
    print('Test list:', testList)
    
    print('Minimum value in list:', min(testList))

# Maximum sum sublist
# Assuming the sublist is three items long
def LA_Q4():
    testList = [random.randrange(1, 10) for x in range(5)]
    print('Test list:', testList)

    start = 0
    end = start + 3
    sum = 0
    maxStart = 0
    maxEnd = 0
    maxSum = 0
    
    while end <= len(testList):
        sum = math.fsum(testList[start:end])
        print(testList[start:end], sum)
        if sum > maxSum:
            maxSum = sum
            maxStart = start
            maxEnd = end
        start += 1
        end += 1

    print('Largest sum sublist:')
    print(testList[maxStart:maxEnd], maxSum)

# Print products of all elements
# Assuming a product is only two factors 
def LA_Q5():
    testList = [random.randrange(1, 10) for x in range(5)]
    print('Test list:', testList)

    factorsList = list(itertools.product(testList, repeat=2))

    prodList = [math.prod(x) for x in factorsList]
    
    for j in range(0, len(factorsList)):
        print(factorsList[j], prodList[j])


#LA_Q1()
#LA_Q2()
#LA_Q3()
#LA_Q4()
#LA_Q5()