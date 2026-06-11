from LinkedList import Node,LinkedList

class CircularLinkedList(LinkedList):
    HEAD = TAIL = None
    def __init__(self):
        super().__init__()
    def __newNode(self,data):
        self.HEAD = self.TAIL = Node(data)
        self.HEAD.next = self.TAIL
        self.TAIL.next = self.HEAD
        self.HEAD.prev = self.TAIL
        self.TAIL.prev = self.HEAD

    def insertAtBeg(self, data):
        if(self.HEAD==None):
            self.__newNode(data)
        else:
            newNode = Node(data)
            newNode.next = self.HEAD
            newNode.prev = self.HEAD.prev
            self.HEAD.prev = newNode
            self.TAIL.next = newNode
            self.HEAD = newNode

    def insertAtEnd(self,data):
        if(self.HEAD==None):
            self.__newNode(data)
        else:
            newNode = Node(data)
            newNode.next = self.TAIL.next
            newNode.prev = self.TAIL
            self.TAIL.next = newNode
            self.TAIL = self.TAIL.next
            self.HEAD.prev = newNode

    def insertAt(self,data,pos):
        if(self.HEAD==None):
            self.__newNode(data)

    def deleteAtBeg(self):
        pass
    def deleteAtEnd(self):
        pass
    def deleteAt(self,pos):
        pass
    def display(self):
        itr = self.HEAD
        while itr!=self.TAIL:
            print(itr.data)
            itr = itr.next
        print(itr.data)
    
list1 = CircularLinkedList()
list1.insertAtBeg(10)
list1.insertAtBeg(-10)
list1.insertAtBeg(7)
list1.insertAtEnd(68)
list1.insertAtEnd(5)

list1.display()