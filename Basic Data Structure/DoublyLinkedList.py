from LinkedList import Node

#Doubly Linked List
class DoublyLinkedList:
    HEAD = None
    TAIL = None

    # Constructor
    def __init__(self):
        print('Doubly Linked List created')
    
    def push(self,data):
        if(self.HEAD==None):
            self.HEAD = Node(data)
            self.TAIL = self.HEAD
        else:
            newNode = Node(data)
            newNode.prev = self.TAIL
            self.TAIL.next = newNode
            self.TAIL = self.TAIL.next

    def pop(self):
        data = None
        if(self.HEAD==None):
            print('EMPTY!')
            return
        elif(self.HEAD==self.TAIL):
            data = self.HEAD.data
            del self.HEAD
            del self.TAIL
            self.HEAD = self.TAIL = None
        else:
            data = self.TAIL.data
            self.TAIL = self.TAIL.prev
            del self.TAIL.next
            self.TAIL.next = None
        print(data,' Deleted')



    def display(self):
        itr = self.HEAD
        if(itr==None):
            print('EMPTY!')
            return
        print('Linked List: ')
        while itr!=None:
            print(itr.data)
            itr = itr.next

# list = DoublyLinkedList()
# list.push(10)
# list.pop()
# list.push(11)
# list.push(5)
# list.push(-100)
# list.push(76)
# list.pop()
# list.display()