from DoublyLinkedList import DoublyLinkedList
class Queue(DoublyLinkedList):
    def __init__(self):
        super().__init__()
    def peek(self):
        return super().HEAD.data
    def enqueue(self,data):
        super().push(data)
    def dequeue(self):
        super().deleteAtBeg()
    def print(self):
        super().display()
q = Queue()
q.enqueue(3)
q.enqueue(2)
q.enqueue(-10)
q.dequeue()
q.print()

    