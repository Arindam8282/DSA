from Node import Node

class Stack:
    HEAD = None
    def __init__(self):
        print('Stack ')

    def top(self) -> int:
        itr = self.HEAD
        while itr.next!=None:
            itr = itr.next
        return itr.data

    def isEmpty(self) -> bool:
        return self.HEAD==None
    
    def push(self,data):
        if(self.isEmpty()):
            self.HEAD = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.HEAD
            self.HEAD = newNode

    def pop(self):
        if(self.isEmpty()):
            print('Stack Underflow!!')
        else:
            if self.top()==self.HEAD:
                self.HEAD = None
                del self.HEAD
            else:
                itr = self.HEAD
                if(itr.next.next):
                    while itr.next.next!=None:
                        itr = itr.next
                temp = itr.next
                itr.next = None
                del temp
                
    def display(self,node = None):
        if(node==None):
            print('Stack Print: ')
            self.display(self.HEAD)
        else:
            if node.next:
                self.display(node.next)
            print(node.data)
st = Stack()
st.push(3)
st.push(-10)
st.push(11)
st.display()
st.pop()
st.display()


