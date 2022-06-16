# ------------------------------------
# Questions related to arrays or lists
# https://www.educative.io/blog/8-python-data-structures#arrays
# ------------------------------------
import random
import itertools

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
# Assuming the sublist contains the largest 3 items
def LA_Q4():
    testList = [random.randrange(1, 10) for x in range(5)]
    print('Test list:', testList)

    sortList = sorted(testList)
    print(sortList)

    maxSubList = sortList[-3:]
    print(maxSubList)

# Print products of all elements
# Assuming only two factors to a product
def LA_Q5():
    testList = [random.randrange(1, 10) for x in range(5)]
    print('Test list:', testList)

    factorsList = list(itertools.product(testList, repeat=2))
    print(factorsList)

    '''prodList = [x*y for (x, y) in factorsList]
    print(prodList)
    '''
    prodList = []
    for (x,y) in factorsList:
        prodList.append(x*y)
        print('{0} * {1} = {2}'.format(x, y, x*y))
    print(prodList)

#LA_Q1()
#LA_Q2()
#LA_Q3()
#LA_Q4()
LA_Q5()