# class node
class Node:
    data = 0
    next = None
    prev = None
    #Constructor
    def __init__(self,data):
        self.data = data

# class linkedlist
class LinkedList:
    HEAD = None

    #Constructor
    def __init__(self):
        print('Linked List Created')

    def push(self,data):
        if(self.HEAD==None):
            self.HEAD = Node(data)
        else:
            ptr = self.HEAD
            while ptr.next!=None:
                ptr = ptr.next
            ptr.next = Node(data)
            ptr = ptr.next

    def pop(self):
        itr = self.HEAD
        data = None
        if(itr==None):
            print('EMPTY!')
        elif(itr.next!=None):
            while itr.next.next!=None:
                itr = itr.next
            data = itr.next.data
            del itr.next
            itr.next = None
            itr = itr.next
        else:
            data = itr.data
            del itr
            itr = None
        print(data,' Deleted ')

    def display(self):
        itr = self.HEAD
        if(itr==None):
            print('EMPTY!')
            return
        print('LinkedList:')
        while itr!=None:
            print(itr.data)
            itr = itr.next

# list = LinkedList()
# list.push(10)
# list.push(5)
# list.pop()
# list.push(-5)
# list.push(11)
# list.pop()
# list.push(98)
# list.display()
    
    