# ------------
# ------------
# Binary Search Tree
#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# ------------
# ------------

class BSTNode:
    def __init__(self, data=None):
        self._data = data
        self._left = None
        self._right = None

def insert(root, data):
    if root == None:
        root = BSTNode(data)
    else:
        if data < root._data:
            if root._left != None:
                insert(root._left, data)
            else:
                root._left = BSTNode(data)
        elif data > root._data:
            if root._right != None:
                insert(root._right, data)
            else:
                root._right = BSTNode(data)
    return root

def search(root, data):
    if root == None or root._data == data:
        return root
    elif data < root._data:
        return search(root._left, data)
    elif data > root._data:
        return search(root._right, data)

def printTree(root):
# inorder traversal
    if root:
        printTree(root._left)
        print(root._data)
        printTree(root._right)
