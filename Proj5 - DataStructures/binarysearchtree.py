# ------------
# ------------
# Binary Search Tree
#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
#https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
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

def delete(root, data):
    if root == None:
        return root
    if data < root._data:
        root._left = delete(root._left, data)
    elif data > root._data:
        root._right = delete(root._right, data)  
    else:
        if root._left == None and root._right == None:
            return None
        elif root._left == None:
            copyNode = root._right
            root = None
            return copyNode
        elif root._right == None:
            copyNode = root._left
            root = None
            return copyNode
        else:
            copyNode = minimum(root._right)
            root._data = copyNode._data
            root._right = delete(root._right, copyNode._data)
    return root

def search(root, data):
    if root == None:
        return None
    elif data == root._data:
        return root
    elif data < root._data:
        return search(root._left, data)
    elif data > root._data:
        return search(root._right, data)

def printTree(root):
# inorder traversal
    if root:
        printTree(root._left)
        print(root._data, end=" ")
        printTree(root._right)

def minimum(root):
    if root._left == None:
        return root
    else:
        return minimum(root._left)

def maximum(root):
    if root._right == None:
        return root
    else:
        return maximum(root._right)

print('Initialize BST...')
root = BSTNode(50)
printTree(root)

print('-'*60)
print('Testing insert()...')
print('-'*60)

print('insert(root, 25)')
printTree(insert(root, 25))
print('insert(root, 75)')
printTree(insert(root, 75))
print('insert(root, 10)')
printTree(insert(root, 10))
print('insert(root, 40)')
printTree(insert(root, 40))
print('insert(root, 60)')
printTree(insert(root, 60))
print('insert(root, 90)')
printTree(insert(root, 90))


print('-'*60)
print('Testing search()...')
print('-'*60)

print('search(root, 25)')
printTree(search(root, 25))
print('search(root, 80)')
printTree(search(root, 80))

print('-'*60)
print('Testing minimum() and maximum()...')
print('-'*60)

print('minimum(root)')
printTree(minimum(root))
print('maximum(root')
printTree(maximum(root))

print('-'*60)
print('Testing delete()...')
print('-'*60)

print('Pre deletions')
printTree(root)

print('delete(root, 60)')
printTree(delete(root, 60))
print('delete(root, 75)')
printTree(delete(root, 75))
print('delete(root, 25)')
printTree(delete(root, 25))
print('delete(root, 90)')
printTree(delete(root, 90))
print('delete(root, 50)')
printTree(delete(root, 10))
print('delete(root, 40)')
printTree(delete(root, 40))
print('delete(root, 10)')
printTree(delete(root, 60))
