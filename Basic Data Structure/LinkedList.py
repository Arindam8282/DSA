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
    
    def insertAtBeg(self,data):
        newNode = Node(data)
        newNode.next = self.HEAD
        self.HEAD = newNode

    def insertAt(self,data,pos):
        newNode = Node(data)
        counter = 1
        flag = 0
        itr = self.HEAD;
        if(counter==pos):
            self.insertAtBeg(data)
            return 
        while itr.next!=None:
            counter+=1
            if(counter==pos): flag = 1;break
            itr = itr.next
        if(flag):
            newNode.next = itr.next
            itr.next = newNode
            itr = itr.next



    def push(self,data):
        if(self.HEAD==None):
            self.HEAD = Node(data)
        else:
            ptr = self.HEAD
            while ptr.next!=None:
                ptr = ptr.next
            ptr.next = Node(data)
            ptr = ptr.next

    def deleteAtBeg(self):
        temp = self.HEAD
        self.HEAD = temp.next
        del temp
        temp = None
    
    def deleteAt(self,pos):
        counter = 1
        itr = self.HEAD
        flag = 0
        if(pos==counter): self.deleteAtBeg();return 
        while itr.next!=None:
            counter+=1
            if(counter==pos): flag = 1;break
            itr = itr.next
        if(flag):
            temp = itr.next
            itr.next = temp.next
            del temp
            temp = None
            itr = itr.next

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
        return data

    def reverse(self,node=None):
        if(node==None):
            self.reverse(self.HEAD)
        elif(node.next!=None):
            self.reverse(node.next)
        if(node!=None):
            self.push(node.data)
            self.deleteAtBeg()

    def length(self,node=None):
        if(node==None):
            return 1+self.length(self.HEAD)
        elif(node.next!=None):
            return 1+self.length(node.next)
        else:
            return 0
        
    def print(self,node=None):
        if(node==None):
            self.print(self.HEAD)
        elif(node.next!=None):
            self.print(node.next)
        if(node!=None):
            print(node.data)
        
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
# list.push(101)
# list.push(65)
# list.push(110)
# list.push(75)
# list.pop()
# list.push(-5)
# list.push(11)
# list.pop()
# list.push(98)
# list.insertAtBeg(-1)
# list.insertAt(11,2)
# list.deleteAtBeg()
# list.deleteAt(5)
# list.reverse()
# list.display()
# print(list.length())
# list.print()
    
    