from Node import Node

class Stack:
    HEAD = None
    def __init__(self):
        print('Stack ')

    def top(self):
        if self.isEmpty():
            return None
        return self.HEAD.data

    def isEmpty(self) -> bool:
        return self.HEAD is None
    
    def push(self,data):
        if self.isEmpty():
            self.HEAD = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.HEAD
            self.HEAD = newNode

    def pop(self):
        if self.isEmpty():
            print('Stack Underflow!!')
            return None
        data = self.HEAD.data
        self.HEAD = self.HEAD.next
        return data

    def display(self,node = None,reverse=False):
        if(node==None):
            print('Stack Print: ')
            self.display(self.HEAD)
        else:
            if(not reverse):
                print(node.data)
            if node.next:
                self.display(node.next)
            if(reverse):
                print(node.data)



# st = Stack()
# st.push(10)
# st.push(-3)
# st.push(13)
# st.display()
# st.pop()
# st.display()