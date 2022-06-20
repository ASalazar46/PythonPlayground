# ------------
# ------------
# Binary Tree
# ------------
# ------------
from collections import deque

class BLNode:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

#-----------------------------------------
# The following methods are depth first traversals
#-----------------------------------------
def inOrderPrint(rootNode):
# Traverse the left subtree
# Print root data
# Traverse the right subtree
    if rootNode._left != None:
        inOrderPrint(rootNode._left)
    print(rootNode._data)
    if rootNode._right != None:
        inOrderPrint(rootNode._right)

def preOrderPrint(rootNode):
# Print root data
# Traverse the left subtree
# Traverse the right subtree
    print(rootNode._data)
    if rootNode._left != None:
        preOrderPrint(rootNode._left)
    if rootNode._right != None:
        preOrderPrint(rootNode._right)

def postOrderPrint(rootNode):
# Traverse the left subtree
# Traverse the right subtree
# Print root data
    if rootNode._left != None:
        postOrderPrint(rootNode._left)
    if rootNode._right != None:
        postOrderPrint(rootNode._right)
    print(rootNode._data)

#-----------------------------------------
# The following method is a breadth first, 
# or level order, traversal
#-----------------------------------------
def breadthFirstPrint(rootNode):
# Create an empty queue q
# Add root to q
# Loop until q is empty
#   Dequeue item to use as current node
#   Print current node's data
#   Enqueue current node's children to q
#       Left child first, then right
    nodeQ = deque()
    nodeQ.append(rootNode)
    while len(list(nodeQ)) > 0:
        currNode = nodeQ.popleft()
        print(currNode._data)
        if currNode._left != None:
            nodeQ.append(currNode._left)
        if currNode._right != None:
            nodeQ.append(currNode._right)

root = BLNode('1')
root._left = BLNode('2')
root._right = BLNode('3')
root._left._left = BLNode('4')
root._left._right = BLNode('5')

print('Testing inOrderPrint:')
inOrderPrint(root)
print('Testing preOrderPrint:')
preOrderPrint(root)
print('Testing postOrderPrint:')
postOrderPrint(root)
print('Testing breadthFirstPrint:')
breadthFirstPrint(root)        

'''
Tree should look like this
      1      |
     / \     |
    2   3    | Depth First
   / \       | Breadth After
  4   5      V

inOrder result: 4 2 5 1 3
preOrder result: 1 2 4 5 3 
postOrder result: 4 5 2 3 1
'''

'''
Tree should look like this
      1      
     / \     
    2   3    
   / \      
  4   5       
 ----------> Breadth First Depth After

breadthFirst result: 1 2 3 4 5
'''