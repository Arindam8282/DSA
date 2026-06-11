from LinkedList import Node,LinkedList

class CircularLinkedList(LinkedList):
    HEAD = TAIL = None
    def __init__(self):
        super().__init__()
    
    def insertAtBeg(self, data):
        if(self.HEAD==None):
            self.HEAD = self.TAIL = Node(data)
            
        pass
    def insertAtEnd(self,data):
        pass
    def insertAt(self,data,pos):
        pass
    def deleteAtBeg(self):
        pass
    def deleteAtEnd(self):
        pass
    def deleteAt(self,pos):
        pass
    def display(self):
        return super().display()