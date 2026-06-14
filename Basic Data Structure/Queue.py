class QueueArray:
    n = 0
    arr = []
    front = rear = -1
    def __init__(self):
        self.n = int(input("Enter size of the Queue"))
        self.arr = [0 for i in range(self.n+1)]
        
    def isFull(self):
        return self.rear==self.n
    def isEqual(self):
        return self.rear==self.front
    def isEmpty(self):
        return self.front == -1 and self.rear == -1
    def enqueue(self,data):
        if(self.isFull()):
            print("Queue Overflow")
        elif(self.isEmpty()):
            self.front = self.rear = 1
            self.arr[self.rear] = data
        else:
            self.rear += 1
            self.arr[self.rear] = data
    def dequeue(self):
        if(self.isEqual()):
            self.front = self.rear = -1
        elif(self.isEmpty()):
            print("Queue Underflow")
        else:
            self.front += 1
    def display(self):
        if(self.isEmpty()):
            print("Empty")
        else:
            print("Queue: ")
            start = self.front
            end = self.rear
            for i in range(start,end+1):
                print(self.arr[i])
arr = QueueArray()
arr.enqueue(10)
arr.enqueue(11)
arr.enqueue(13)
arr.enqueue(13)
arr.enqueue(13)


arr.dequeue()
arr.display()