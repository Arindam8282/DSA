from LinkedList import Node,LinkedList

#Doubly Linked List
class DoublyLinkedList(LinkedList):
    HEAD = None
    TAIL = None

    # Constructor
    def __init__(self):
        print('Doubly Linked List created')

    def insertAtBeg(self,data):
        newNode = Node(data)
        newNode.next = self.HEAD
        self.HEAD.prev = newNode
        self.HEAD = self.HEAD.prev

    def insertAt(self,data,pos):
        counter = 1
        itr = self.HEAD
        flag = 0
        if(counter==pos): self.insertAtBeg(data); return
        while itr!=None:
            counter+=1
            if(counter==pos): flag=1;break
            itr = itr.next
        if(flag):
            newNode = Node(data)
            newNode.next = itr.next
            newNode.prev = itr
            if(itr.next):
                itr.next.prev = newNode
            itr.next = newNode
    
    def push(self,data):
        if(self.HEAD==None):
            self.HEAD = Node(data)
            self.TAIL = self.HEAD
        else:
            newNode = Node(data)
            newNode.prev = self.TAIL
            self.TAIL.next = newNode
            self.TAIL = self.TAIL.next

    def delFromBeg(self):
        ptr = self.HEAD
        self.HEAD = self.HEAD.next
        del ptr
        self.HEAD.prev = None

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
    
    def delFromPos(self,pos):
        counter = 1
        if(pos==counter): self.delFromBeg();return
        itr = self.HEAD
        flag = 0
        while itr.next!=None:
            counter+=1
            itr = itr.next
            if(counter==pos): flag = 1; break
        # print(itr.data)
        if(flag):
            if(itr==self.TAIL): self.pop();return
            ptrPrev = itr.prev
            ptrNext = itr.next
            ptrPrev.next = ptrNext
            if(ptrNext):
                ptrNext.prev = ptrPrev
            del itr


    def display(self):
        itr = self.HEAD
        if(itr==None):
            print('EMPTY!')
            return
        print('Linked List: ')
        while itr!=None:
            print(itr.data)
            itr = itr.next

list = DoublyLinkedList()
list.push(10)
list.pop()
list.push(11)
list.push(5)
list.push(-100)
list.push(76)
list.pop()
list.insertAtBeg(-9)
list.insertAtBeg(83)
list.insertAtBeg(69)
list.insertAt(21,5)
list.display()
list.delFromPos(6)
list.delFromPos(6)
list.delFromPos(5)
list.display()
list.reverse()
list.display()
list.reverse()
list.display()