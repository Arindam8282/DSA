from LinkedList import Node,LinkedList

class DoublyCircularLinkedList(LinkedList):
    HEAD = TAIL = None
    reversed = False
    def __init__(self):
        super().__init__()
    def __newNode(self,data):
        self.HEAD = self.TAIL = Node(data)
        self.HEAD.next = self.TAIL
        self.TAIL.next = self.HEAD
        self.HEAD.prev = self.TAIL
        self.TAIL.prev = self.HEAD
    
    def __deleteFirstNode(self):
        if(self.HEAD==self.TAIL):
            self.HEAD = self.TAIL = None
        else:
            temp = self.HEAD
            self.HEAD = self.HEAD.next
            self.HEAD.prev = self.TAIL
            temp.next = None
            temp.prev = None
            del temp


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
        else:
            counter = 1
            if(counter==pos): self.insertAtBeg(data); return
            itr = self.HEAD
            flag = 0
            while itr!=self.TAIL:
                counter += 1
                itr = itr.next
                if(counter==pos): flag = 1; break
            
            if flag:
                newNode = Node(data)
                newNode.next = itr
                itr.prev.next = newNode
                newNode.prev = itr.prev
                itr.prev = newNode
            else:
                itr = itr.next
                counter += 1
                if(counter==pos): self.insertAtEnd(data)


    def deleteAtBeg(self):
        self.__deleteFirstNode()

    def deleteAtEnd(self):
        if(self.HEAD==self.TAIL):
            self.__deleteFirstNode()
        else:
            temp = self.TAIL
            self.TAIL = self.TAIL.prev
            self.TAIL.next = self.HEAD
            self.HEAD.prev = self.TAIL
            temp.next = None
            temp.prev = None
            del temp

    def deleteAt(self,pos):
        counter = 1
        if(counter==pos):self.__deleteFirstNode(); return
        flag = 0
        itr = self.HEAD
        while itr!=self.TAIL:
            counter+=1
            itr = itr.next
            if counter==pos:flag = 1;break

        if flag:
            temp = itr
            itr = itr.next
            itr.prev = temp.prev
            temp.prev.next = itr
            del temp
        else:
            counter+=1
            itr=itr.next
            if counter==pos:self.deleteAtEnd()

    def reverse(self):
        self.reversed = not self.reversed

    def palti(self):
        prev = self.TAIL
        cur = self.HEAD
        nxt = self.HEAD.next
        while cur!=self.TAIL:
            cur.next = prev
            cur.prev = nxt
            prev = cur
            cur = nxt
            nxt = nxt.next
        cur.next = prev
        cur.prev = nxt
        prev = cur
        cur = nxt
        nxt = nxt.next
        temp = self.HEAD
        self.HEAD = self.TAIL
        self.TAIL = temp
        
    
    def display(self):
        print("Doubly Circular LinkedList: ")
        end = self.TAIL
        itr = self.HEAD
        if self.reversed:
            itr = self.TAIL
            end = self.HEAD
        while itr!=end:
            print(itr.data)
            if self.reversed:
                itr = itr.prev
            else:
                itr = itr.next
        print(itr.data)
    
list1 = DoublyCircularLinkedList()
list1.insertAtBeg(10)
list1.insertAtBeg(-10)
list1.insertAtBeg(7)
list1.insertAtEnd(68)
list1.insertAtEnd(5)
list1.insertAt(1,2)
list1.insertAt(4,2)
list1.insertAt(22,7)
# list1.display()
# list1.deleteAt(3)
# list1.display()
# list1.deleteAtBeg()
# list1.display()
# list1.deleteAtEnd()
# list1.display()
list1.reverse()
list1.display()
list1.palti()
list1.display()