# ----------
# ----------
# Linked List
# ----------
# ----------

class LinkedList:
    def __init__(self):
        self._headPtr = None
    
    def printList(self):
        temp = self._headPtr
        while(temp):
            print(temp._data)
            temp = temp._nextPtr

    def append(self, node):
        print('Appending to list...')
        if isinstance(node, LL_Node) == False:
            print('Argument not of the class LL_Node.')
        else:
            if self._headPtr == None:
                self._headPtr = node
                print('Append complete.')
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

    def appendHead(self, node):
        print('Appending to list head...')
        if isinstance(node, LL_Node) == False:
            print('Argument not of the class LL_Node.')
        else:
            node._nextPtr = self._headPtr
            self._headPtr = node
            print('Append to head complete.')

    def insert(self, insertAfter, node):
        print('Inserting to list...')
        if isinstance(node, LL_Node) == False:
            print('Argument not of the class LL_Node.')
        else:
            if self._headPtr == None:
                print('Linked list is empty. No inserting into an empty list.')
            else:
                temp = self._headPtr
                inserted = False
                while(inserted != True):
                    if temp._data == insertAfter:
                        node._nextPtr = temp._nextPtr
                        temp._nextPtr = node
                        inserted = True
                    else:
                        if temp._nextPtr == None:
                            print('insertAfter not found in linked list.')
                            return
                        else:
                            temp = temp._nextPtr
                print('Insert complete.')
                
    def pop(self):
        print('Popping list tail...')
        if self._headPtr == None:
            print('Nothing to pop. Linked list is empty.')
        else:
            newTail = self._headPtr
            deleteMe = self._headPtr._nextPtr
            deleted = False
            while(deleted != True):
                if newTail._nextPtr == None:
                    self._headPtr = None
                    deleted = True
                    print('Popped list tail.')
                elif deleteMe._nextPtr == None:
                    newTail._nextPtr = None
                    deleted = True
                    print('Popped list tail.')
                else:
                    newTail = deleteMe
                    deleteMe = deleteMe._nextPtr

    def popHead(self):
        print('Popping list head...')
        if self._headPtr == None:
            print('Nothing to pop. Linked list is empty.')
        else:
            temp = self._headPtr
            self._headPtr = self._headPtr._nextPtr
            temp._nextPtr = None
            print('Popped list head.')
    
    def delete(self, deleteData):
        print('Deleting from list...')
        if self._headPtr == None:
            print('Nothing to delete. Linked list is empty.')
        else:
            newTail = self._headPtr
            deleteMe = self._headPtr._nextPtr
            deleted = False
            while(deleted != True):
                if deleteMe._data == deleteData:
                    newTail._nextPtr = deleteMe._nextPtr
                    deleteMe._nextPtr = None
                    deleted = True
                    print('Deleted form list.')
                else:
                    if deleteMe._nextPtr == None:
                        print('deleteData not found in linked list.')
                        return
                    else:
                        newTail = deleteMe
                        deleteMe = deleteMe._nextPtr


class LL_Node:
    def __init__(self, data):
        self._data = data
        self._nextPtr = None

def testAppend():
    print('-'*60)
    print('Testing LinkedList.append():')
    testLL = LinkedList()
    testLL.append(LL_Node('First'))
    testLL.printList()
    testLL.append(LL_Node('Second'))
    testLL.printList()
    testLL.append(LL_Node('Third'))
    testLL.printList()
    print('-'*60)

def testPop():
    print('-'*60)
    print('Testing LinkedList.pop():')
    testLL = LinkedList()
    testLL.append(LL_Node('First'))
    testLL.append(LL_Node('Second'))
    testLL.append(LL_Node('Third'))
    testLL.printList()
    testLL.pop()
    testLL.printList()
    testLL.pop()
    testLL.printList()
    testLL.pop()
    testLL.printList()
    testLL.pop()
    print('-'*60)

def testAppendHead():
    print('-'*60)
    print('Testing LinkedList.appendHead():')
    testLL = LinkedList()
    testLL.appendHead(LL_Node('First'))
    testLL.printList()
    testLL.appendHead(LL_Node('Second'))
    testLL.printList()
    testLL.appendHead(LL_Node('Third'))
    testLL.printList()
    print('-'*60)

def testPopHead():
    print('-'*60)
    print('Testing LinkedList.appendHead():')
    testLL = LinkedList()
    testLL.appendHead(LL_Node('First'))
    testLL.appendHead(LL_Node('Second'))
    testLL.appendHead(LL_Node('Third'))
    testLL.printList()
    testLL.popHead()
    testLL.printList()
    testLL.popHead()
    testLL.printList()
    testLL.popHead()
    testLL.printList()
    testLL.popHead()
    print('-'*60)

def testInsert():
    print('-'*60)
    print('Testing LinkedList.insert():')
    testLL = LinkedList()
    testLL.append(LL_Node('First'))
    testLL.append(LL_Node('Second'))
    testLL.append(LL_Node('Third'))
    testLL.printList()
    testLL.insert('First', LL_Node(111))
    testLL.printList()
    testLL.insert('Second', LL_Node(222))
    testLL.printList()
    testLL.insert('Third', LL_Node(333))
    testLL.printList()
    testLL.insert('Fourth', LL_Node(444))
    emptyLL = LinkedList()
    emptyLL.insert('First', LL_Node(111))
    print('-'*60)

def testDelete():
    print('-'*60)
    print('Testing LinkedList.delete():')
    testLL = LinkedList()
    testLL.append(LL_Node('First'))
    testLL.append(LL_Node('Second'))
    testLL.append(LL_Node('Third'))
    testLL.printList()
    testLL.insert('First', LL_Node(111))
    testLL.printList()
    testLL.insert('Second', LL_Node(222))
    testLL.printList()
    testLL.insert('Third', LL_Node(333))
    testLL.printList()
    testLL.insert('Fourth', LL_Node(444))
    emptyLL = LinkedList()
    emptyLL.insert('First', LL_Node(111))
    testLL.delete(444)
    testLL.printList()
    testLL.delete(222)
    testLL.printList()
    testLL.delete(111)
    testLL.printList()
    testLL.delete(333)
    testLL.printList()
    testLL.delete(000)
    emptyLL = LinkedList()
    testLL.delete(000)
    print('-'*60)

testAppend()
testPop()
testAppendHead()
testPopHead()
testInsert()
testDelete()