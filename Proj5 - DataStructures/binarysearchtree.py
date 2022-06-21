# ------------
# ------------
# Binary Search Tree
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
        if root._left == None:
            copyNode = root._right
            root= None
            return copyNode
        elif root._right == None:
            copyNode = root._left
            root = None
            return copyNode
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
print('\n')

print('-'*60)
print('Testing insert()...')
print('-'*60)

print('insert(root, 25)')
root = insert(root, 25)
printTree(root)
print('\n')

print('insert(root, 75)')
root = insert(root, 75)
printTree(root)
print('\n')

print('insert(root, 10)')
root = insert(root, 10)
printTree(root)
print('\n')

print('insert(root, 40)')
root = insert(root, 40)
printTree(root)
print('\n')

print('insert(root, 60)')
root = insert(root, 60)
printTree(root)
print('\n')

print('insert(root, 90)')
root = insert(root, 90)
printTree(root)
print('\n')

print('-'*60)
print('Testing search()...')
print('-'*60)

print('search(root, 25)')
search1 = search(root, 25)
printTree(search1)
print('\n')

print('search(root, 80)')
search2 = search(root, 80)
printTree(search2)
print('\n')

print('-'*60)
print('Testing minimum() and maximum()...')
print('-'*60)

print('minimum(root)')
rootMin = minimum(root)
printTree(rootMin)
print('\n')

print('maximum(root')
rootMax = maximum(root)
printTree(rootMax)
print('\n')

print('-'*60)
print('Testing delete()...')
print('-'*60)

print('Pre deletions')
printTree(root)
print('\n')

print('delete(root, 60)')
root = delete(root, 60)
printTree(root)
print('\n')

print('delete(root, 75)')
root = delete(root, 75)
printTree(root)
print('\n')

print('delete(root, 25)')
root = delete(root, 25)
printTree(root)
print('\n')

print('delete(root, 90)')
root = delete(root, 90)
printTree(root)
print('\n')

print('delete(root, 50)')
root = delete(root, 50)
printTree(root)
print('\n')

print('delete(root, 40)')
root = delete(root, 40)
printTree(root)
print('\n')

print('delete(root, 10)')
root = delete(root, 10)
printTree(root)
print('\n')
