# ----------
# ----------
# Linked List
# ----------
# ----------

class LinkedList:
    def __init__(self):
        self._headPtr = None
    
    def printList(self):
        print('Printing list...')
        temp = self._headPtr
        while(temp):
            print(temp._data)
            temp = temp._nextPtr
        print('Print complete.')

    def append(self, node):
        print('Appending to list...')
        if isinstance(node, LL_Node) == False:
            print('Argument not of the class LL_Node.')
        else:
            temp = self._headPtr
            appended = False
            while(appended != True):
                if temp._nextPtr == None:
                    temp._nextPtr = node
                    appended = True
                    print('Append complete.')
                else:
                    temp = temp._nextPtr

    def pop(self):
        print('Popping list tail...')
        newTail = self._headPtr
        deleteMe = self._headPtr._nextPtr
    
        deleted = False
        while(deleted != True):
            if deleteMe._nextPtr == None:
                newTail._nextPtr = None
                del deleteMe
                del newTail
                deleted = True
                print('Popped list tail.')
            else:
                newTail = deleteMe
                deleteMe = deleteMe._nextPtr

    def appendHead(self, node):
        print('Appending to list head...')
        if isinstance(node, LL_Node) == False:
            print('Argument not of the class LL_Node.')
        else:
            node._nextPtr = self._headPtr
            self._headPtr = node
            print('Append to head complete.')

    def popHead(self):
        print('Popping list head...')
        temp = self._headPtr
        self._headPtr = self._headPtr._nextPtr
        temp._nextPtr = None
        del temp
        print('Popped list head.')
        
class LL_Node:
    def __init__(self, data):
        self._data = data
        self._nextPtr = None

linkedList = LinkedList()

firstNode = LL_Node('First')
secondNode = LL_Node('Second')
thirdNode = LL_Node('Third')

linkedList._headPtr = firstNode
firstNode._nextPtr = secondNode
secondNode._nextPtr = thirdNode

linkedList.printList()

linkedList.append(LL_Node('Fourth'))
linkedList.printList()

linkedList.append('asdf')

linkedList.popHead()
linkedList.printList()

linkedList.appendHead(LL_Node('Zeroth'))
linkedList.printList()

linkedList.pop()
linkedList.printList()